#!/usr/bin/env python3
# /// script
# dependencies = ["mcp"]
# ///
"""
Plans MCP Server

A Model Context Protocol server that provides tools for automatically 
saving and managing validated project plans created in Claude Code's plan mode.
"""

import json
import logging
import sys
from typing import Any, Dict, List, Optional
import asyncio
from pathlib import Path

# MCP imports
try:
    from mcp.server import Server
    from mcp.server.models import InitializationOptions
    import mcp.server.stdio
    import mcp.types as types
except ImportError as e:
    print(f"Error: MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Import our plan manager
try:
    from .plan_manager import PlanManager
except ImportError:
    # For standalone execution
    from plan_manager import PlanManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("plans-mcp-server")

# Initialize the server
server = Server("plans-mcp-server")

# Global plan manager instance
plan_manager = None

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="save_plan",
            description="Save a validated project plan as markdown with metadata",
            inputSchema={
                "type": "object",
                "properties": {
                    "plan_content": {
                        "type": "string",
                        "description": "The validated plan content to save"
                    },
                    "project_name": {
                        "type": "string",
                        "description": "Optional project name (auto-extracted if not provided)"
                    }
                },
                "required": ["plan_content"]
            }
        ),
        types.Tool(
            name="list_plans",
            description="List all saved project plans",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_filter": {
                        "type": "string",
                        "description": "Optional project name to filter by"
                    }
                }
            }
        ),
        types.Tool(
            name="get_plan",
            description="Retrieve content of a specific plan",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_name": {
                        "type": "string",
                        "description": "Name of the project"
                    },
                    "filename": {
                        "type": "string", 
                        "description": "Optional specific plan filename (uses most recent if not provided)"
                    }
                },
                "required": ["project_name"]
            }
        ),
        types.Tool(
            name="get_plans_index",
            description="Get the master index of all plans",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="search_plans",
            description="Search plans by content or metadata",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query to match against plan content"
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional tags to filter by"
                    }
                },
                "required": ["query"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Handle tool calls."""
    global plan_manager
    
    # Initialize plan manager if not already done
    if plan_manager is None:
        plan_manager = PlanManager()
    
    try:
        if name == "save_plan":
            plan_content = arguments.get("plan_content", "")
            project_name = arguments.get("project_name")
            
            if not plan_content.strip():
                return [types.TextContent(
                    type="text",
                    text="Error: plan_content cannot be empty"
                )]
            
            # Save the plan
            saved_path = plan_manager.save_plan_as_md(plan_content, project_name)
            
            # Get relative path for display
            relative_path = saved_path.relative_to(plan_manager.plans_dir)
            
            result = f"✅ Plan saved successfully!\n\n"
            result += f"📁 Location: {relative_path}\n"
            result += f"🔗 Project: {saved_path.parent.name}\n"
            result += f"📅 Date: {saved_path.name.split('_')[0]}\n\n"
            result += f"View all plans: check the Plans/index.md file"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "list_plans":
            project_filter = arguments.get("project_filter")
            plans = plan_manager.list_plans()
            
            if project_filter:
                plans = [p for p in plans if p['project'] == project_filter]
            
            if not plans:
                filter_text = f" for project '{project_filter}'" if project_filter else ""
                return [types.TextContent(
                    type="text", 
                    text=f"No plans found{filter_text}"
                )]
            
            result = f"📋 Found {len(plans)} plan(s):\n\n"
            for plan in plans:
                result += f"• **{plan['project']}** - {plan['filename']}\n"
                result += f"  📁 {plan['path'].relative_to(plan_manager.plans_dir)}\n\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_plan":
            project_name = arguments.get("project_name", "")
            filename = arguments.get("filename")
            
            if not project_name:
                return [types.TextContent(
                    type="text",
                    text="Error: project_name is required"
                )]
            
            content = plan_manager.get_plan_content(project_name, filename)
            
            if content is None:
                return [types.TextContent(
                    type="text",
                    text=f"Plan not found for project '{project_name}'"
                )]
            
            return [types.TextContent(type="text", text=content)]
        
        elif name == "get_plans_index":
            if plan_manager.index_file.exists():
                with open(plan_manager.index_file, 'r', encoding='utf-8') as f:
                    index_content = f.read()
                return [types.TextContent(type="text", text=index_content)]
            else:
                return [types.TextContent(
                    type="text",
                    text="Plans index not found. Create your first plan to initialize the index."
                )]
        
        elif name == "search_plans":
            query = arguments.get("query", "").lower()
            tags_filter = arguments.get("tags", [])
            
            if not query:
                return [types.TextContent(
                    type="text",
                    text="Error: search query is required"
                )]
            
            # Get all plans and search through them
            plans = plan_manager.list_plans()
            matching_plans = []
            
            for plan in plans:
                content = plan_manager.get_plan_content(plan['project'], plan['filename'])
                if content and query in content.lower():
                    # Basic tag filtering (would need more sophisticated implementation)
                    if not tags_filter or any(tag.lower() in content.lower() for tag in tags_filter):
                        matching_plans.append(plan)
            
            if not matching_plans:
                return [types.TextContent(
                    type="text",
                    text=f"No plans found matching query: '{query}'"
                )]
            
            result = f"🔍 Found {len(matching_plans)} plan(s) matching '{query}':\n\n"
            for plan in matching_plans:
                result += f"• **{plan['project']}** - {plan['filename']}\n"
                result += f"  📁 {plan['path'].relative_to(plan_manager.plans_dir)}\n\n"
            
            return [types.TextContent(type="text", text=result)]
        
        else:
            return [types.TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]
    
    except Exception as e:
        logger.error(f"Error in tool {name}: {str(e)}")
        return [types.TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]

async def main():
    """Run the server."""
    # Server initialization options
    options = InitializationOptions(
        server_name="plans-mcp-server",
        server_version="1.0.0",
        capabilities=server.get_capabilities(
            notification_options=None,
            experimental_capabilities=None,
        )
    )
    
    logger.info("Starting Plans MCP Server...")
    
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            options,
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)