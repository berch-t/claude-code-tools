#!/usr/bin/env python3
# /// script
# dependencies = ["mcp"]
# ///
"""
{{SERVER_NAME}} MCP Server - Python Implementation

{{DESCRIPTION}}
"""

import asyncio
import logging
import sys
from typing import Any, Dict, List, Optional

# MCP imports
try:
    from mcp.server import Server
    from mcp.server.models import InitializationOptions
    import mcp.server.stdio
    import mcp.types as types
except ImportError as e:
    print(f"Error: MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("{{SERVER_NAME}}")

# Initialize the server
server = Server("{{SERVER_NAME}}")

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="example_tool",
            description="Example tool for {{SERVER_NAME}}",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Message to process"
                    },
                    "count": {
                        "type": "number",
                        "description": "Number of times to repeat",
                        "default": 1
                    }
                },
                "required": ["message"]
            }
        ),
        # Add more tools here
        {{ADDITIONAL_TOOLS}}
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Handle tool calls."""
    try:
        if name == "example_tool":
            message = arguments.get("message", "")
            count = arguments.get("count", 1)
            
            # Validate inputs
            if not message:
                raise ValueError("Message cannot be empty")
            if not isinstance(count, int) or count < 1 or count > 10:
                raise ValueError("Count must be between 1 and 10")
            
            # Process the tool
            result = " ".join([message] * count)
            
            return [types.TextContent(
                type="text",
                text=f"{{SERVER_NAME}} processed: {result}"
            )]
        
        # Add more tool handlers here
        {{ADDITIONAL_TOOL_HANDLERS}}
        
        else:
            raise ValueError(f"Unknown tool: {name}")
            
    except Exception as e:
        logger.error(f"Error in tool {name}: {str(e)}")
        return [types.TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]

# Optional: Add prompts support
@server.list_prompts()
async def handle_list_prompts() -> List[types.Prompt]:
    """List available prompts."""
    return [
        types.Prompt(
            name="example_prompt",
            description="Example prompt for {{SERVER_NAME}}",
            arguments=[
                types.PromptArgument(
                    name="topic",
                    description="Topic to generate content about",
                    required=True
                ),
                types.PromptArgument(
                    name="style",
                    description="Writing style to use",
                    required=False
                )
            ]
        ),
        # Add more prompts here
        {{ADDITIONAL_PROMPTS}}
    ]

@server.get_prompt()
async def handle_get_prompt(name: str, arguments: Dict[str, Any]) -> types.GetPromptResult:
    """Handle prompt requests."""
    try:
        if name == "example_prompt":
            topic = arguments.get("topic", "")
            style = arguments.get("style", "professional")
            
            if not topic:
                raise ValueError("Topic is required")
            
            messages = [
                types.PromptMessage(
                    role="system",
                    content=types.TextContent(
                        type="text",
                        text=f"You are an expert writer creating {style} content about {topic}."
                    )
                ),
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"Write comprehensive content about {topic} in a {style} style."
                    )
                )
            ]
            
            return types.GetPromptResult(
                description=f"Generate {style} content about {topic}",
                messages=messages
            )
        
        # Add more prompt handlers here
        {{ADDITIONAL_PROMPT_HANDLERS}}
        
        else:
            raise ValueError(f"Unknown prompt: {name}")
            
    except Exception as e:
        logger.error(f"Error in prompt {name}: {str(e)}")
        raise

# Optional: Add resources support
@server.list_resources()
async def handle_list_resources() -> List[types.Resource]:
    """List available resources."""
    return [
        types.Resource(
            uri="{{SERVER_NAME}}://info",
            name="Server Information",
            description="Information about {{SERVER_NAME}}",
            mimeType="text/plain"
        ),
        # Add more resources here
        {{ADDITIONAL_RESOURCES}}
    ]

@server.read_resource()
async def handle_read_resource(uri: str) -> str:
    """Handle resource reading."""
    try:
        if uri == "{{SERVER_NAME}}://info":
            return f"""{{SERVER_NAME}} MCP Server

Description: {{DESCRIPTION}}
Version: {{VERSION}}
Author: {{AUTHOR}}

This server provides:
- Tools: Custom functions and commands
- Prompts: Structured prompts for AI interactions
- Resources: Dynamic content and data access

Capabilities:
- Example tool for message processing
- Example prompt for content generation
- Server information resource

For more information about MCP, visit: https://modelcontextprotocol.io/
"""
        
        # Add more resource handlers here
        {{ADDITIONAL_RESOURCE_HANDLERS}}
        
        else:
            raise ValueError(f"Unknown resource: {uri}")
            
    except Exception as e:
        logger.error(f"Error reading resource {uri}: {str(e)}")
        raise

async def main():
    """Run the server."""
    # Server initialization options
    options = InitializationOptions(
        server_name="{{SERVER_NAME}}",
        server_version="{{VERSION}}",
        capabilities=server.get_capabilities(
            notification_options=None,
            experimental_capabilities=None,
        )
    )
    
    logger.info("Starting {{SERVER_NAME}} MCP Server...")
    
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