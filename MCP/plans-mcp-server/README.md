# Plans MCP Server 📋

A Model Context Protocol server for automatically saving and managing validated project plans from Claude Code's plan mode.

## 🎯 Overview

The Plans MCP Server provides seamless integration with Claude Code to automatically capture, organize, and manage validated project plans. When you exit plan mode in Claude Code, your plans are automatically saved as structured markdown files with metadata, creating a searchable repository of proven project blueprints.

## ✨ Features

### 🔧 **Tools**
- **save_plan** - Automatically save validated plans as structured markdown files
- **list_plans** - List all saved project plans with filtering options
- **get_plan** - Retrieve content of specific plans for reference
- **get_plans_index** - Access the master index of all plans
- **search_plans** - Search through plans by content and tags

### 📋 **Prompts**
*This version focuses on tools for plan management. Prompts may be added in future versions.*

### 📚 **Resources**
*Dynamic resources for accessing plan templates and indexes are planned for future versions.*

## 🚀 Installation

### Prerequisites
- **Claude Code** - Latest version with MCP support
- **Python 3.8+** - For the MCP server runtime
- **MCP SDK** - Python MCP implementation

### Setup

1. **Clone the MCP server:**
   ```bash
   git clone <your-repo-url>
   cd claude-code-tools/MCP/plans-mcp-server
   ```

2. **Install dependencies:**
   ```bash
   # Using uv (recommended - frictionless dependency management)
   # Dependencies are automatically managed via script header
   uv run src/server.py --help
   
   # Or using pip
   pip install mcp
   ```

3. **Configure Claude Code:**
   ```json
   // Add to ~/.claude/claude_desktop_config.json
   {
     "mcpServers": {
       "plans-mcp-server": {
         "command": "uv",
         "args": ["run", "/path/to/claude-code-tools/MCP/plans-mcp-server/src/server.py"],
         "env": {
           "PLANS_DIR": "~/.claude/Plans"
         }
       }
     }
   }
   ```

4. **Restart Claude Code:**
   ```bash
   # Restart Claude Code to load the MCP server
   ```

## 📖 Usage

### Available Tools

#### save_plan
**Purpose:** Automatically save validated project plans as structured markdown files with metadata

**Parameters:**
- `plan_content` (required) - The validated plan content to save
- `project_name` (optional) - Project name (auto-extracted from plan title if not provided)

**Example:**
```bash
Use save_plan with your validated plan content from exit_plan_mode
```

#### list_plans
**Purpose:** List all saved project plans with optional filtering

**Parameters:**
- `project_filter` (optional) - Filter plans by specific project name

**Example:**
```bash
Use list_plans to see all your saved plans, or list_plans with project_filter="my-project"
```

#### get_plan
**Purpose:** Retrieve the content of a specific saved plan

**Parameters:**
- `project_name` (required) - Name of the project
- `filename` (optional) - Specific plan filename (uses most recent if not provided)

**Example:**
```bash
Use get_plan with project_name="my-project" to get the latest plan for that project
```

#### get_plans_index
**Purpose:** Access the master index showing all plans and project overview

**Parameters:**
*No parameters required*

**Example:**
```bash
Use get_plans_index to see the complete overview of your plans repository
```

#### search_plans
**Purpose:** Search through saved plans by content keywords and tags

**Parameters:**
- `query` (required) - Search query to match against plan content
- `tags` (optional) - Array of tags to filter by

**Example:**
```bash
Use search_plans with query="React" to find all plans mentioning React
```

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `PLANS_DIR` | No | Custom directory for storing plans | `~/.claude/Plans` |

### Configuration File
The server uses the default Plans directory structure:
```json
{
  "plans_directory": "~/.claude/Plans",
  "auto_extract_project_names": true,
  "max_recent_plans": 10,
  "supported_tags": ["web", "api", "database", "ai", "react", "python", "javascript"]
}
```

## 📊 Architecture

### MCP Server Structure
```
plans-mcp-server/
├── src/
│   ├── server.py           # Main MCP server implementation
│   ├── plan_manager.py     # Core plan management logic
│   └── __init__.py         # Package initialization
├── tests/
├── docs/
└── README.md
```

### Data Flow
1. **Plan Creation** - User creates plan in Claude Code plan mode
2. **Plan Validation** - User validates plan and calls exit_plan_mode
3. **Automatic Saving** - MCP server receives plan content via save_plan tool
4. **Processing** - Plan content is processed, project name extracted, metadata added
5. **Storage** - Plan saved as structured markdown in appropriate project folder
6. **Indexing** - Master index updated with new plan entry

## 🎯 Use Cases

### Development Workflow
- **Plan Mode Integration** - Seamlessly capture validated plans during development planning
- **Project Documentation** - Build a library of proven project blueprints
- **Plan Reuse** - Reference and adapt existing plans for similar projects

### Team Collaboration
- **Shared Plan Repository** - Maintain team-wide collection of validated approaches
- **Best Practices** - Document and share successful project planning patterns
- **Knowledge Base** - Create searchable archive of project planning wisdom

### Personal Organization
- **Project Tracking** - Keep organized record of all project plans
- **Learning Reference** - Build personal collection of successful planning approaches
- **Pattern Recognition** - Identify recurring themes and improve planning skills

## 📋 Examples

### Example 1: Automatic Plan Saving
```bash
# When you exit plan mode in Claude Code, the plan is automatically saved
# The MCP server processes the plan content and creates structured files
```

**Expected Output:**
```
✅ Plan saved successfully!

📁 Location: projects/my-web-app/2025-07-02_plan.md
🔗 Project: my-web-app
📅 Date: 2025-07-02

View all plans: check the Plans/index.md file
```

### Example 2: Listing All Plans
```bash
# Use list_plans tool to see all your saved project plans
```

**Expected Output:**
```
📋 Found 3 plan(s):

• **my-web-app** - 2025-07-02_plan.md
  📁 projects/my-web-app/2025-07-02_plan.md

• **api-service** - 2025-07-01_plan.md
  📁 projects/api-service/2025-07-01_plan.md

• **data-pipeline** - 2025-06-30_plan.md
  📁 projects/data-pipeline/2025-06-30_plan.md
```

### Example 3: Searching Plans
```bash
# Use search_plans with query="React" to find React-related plans
```

**Expected Output:**
```
🔍 Found 2 plan(s) matching 'react':

• **my-web-app** - 2025-07-02_plan.md
  📁 projects/my-web-app/2025-07-02_plan.md

• **dashboard-ui** - 2025-06-28_plan.md
  📁 projects/dashboard-ui/2025-06-28_plan.md
```

## 🚨 Troubleshooting

### Common Issues

**MCP Server not appearing in Claude Code:**
```bash
# Problem: Server not loading in Claude Code
# Solution: Check configuration and restart Claude Code
# Verify the path in claude_desktop_config.json is correct
```

**Plans directory not found:**
- **Symptoms:** Error messages about missing Plans directory
- **Cause:** Plans directory not initialized or incorrect path
- **Fix:** The server automatically creates the directory structure on first use

**Permission errors:**
```json
// Check configuration in ~/.claude/claude_desktop_config.json
{
  "mcpServers": {
    "plans-mcp-server": {
      // Ensure the path is accessible and correct
      "command": "python",
      "args": ["/correct/path/to/server.py"]
    }
  }
}
```

### Debugging

1. **Check server status:**
   ```bash
   python src/server.py
   ```

2. **Validate configuration:**
   ```bash
   cat ~/.claude/claude_desktop_config.json | jq '.mcpServers["plans-mcp-server"]'
   ```

3. **View logs:**
   ```bash
   # Check Claude Code logs for MCP server connection errors
   tail -f ~/.claude/logs/claude_code.log
   ```

## 🔄 Development

### Contributing

1. **Fork the repository**
2. **Create feature branch:** `git checkout -b feature/new-feature`
3. **Make changes and test**
4. **Submit pull request**

### Testing

```bash
# Run basic functionality test
python src/plan_manager.py

# Test MCP server independently
python src/server.py

# Manual integration test with Claude Code
# (Configure server and test with Claude Code MCP integration)
```

### Building

```bash
# No build step required for Python MCP server
# Server runs directly from source

# For packaging:
pip install -e .
```

## 📚 API Reference

### Tool Specifications

#### save_plan
```json
{
  "name": "save_plan",
  "description": "Save a validated project plan as markdown with metadata",
  "inputSchema": {
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
}
```

#### list_plans
```json
{
  "name": "list_plans",
  "description": "List all saved project plans",
  "inputSchema": {
    "type": "object",
    "properties": {
      "project_filter": {
        "type": "string",
        "description": "Optional project name to filter by"
      }
    }
  }
}
```

#### search_plans
```json
{
  "name": "search_plans",
  "description": "Search plans by content or metadata",
  "inputSchema": {
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
}
```

### Resource Specifications

*Resources are planned for future versions and will include:*
- Dynamic plan templates
- Project statistics
- Plan relationship mapping

## 🔗 Related Projects

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - AI-powered development environment
- [MCP Specification](https://modelcontextprotocol.io/) - Official MCP documentation
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Python implementation of MCP

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- **GitHub Issues:** [Report bugs or request features](https://github.com/your-repo/issues)
- **Documentation:** [Plans System Documentation](./docs/)
- **Community:** [Claude Code Community](https://docs.anthropic.com/en/docs/claude-code)

---

**Automatically capture and organize your best project plans** 📋✨

*Transform your Claude Code planning sessions into a searchable library of proven project blueprints*