# MCP Servers 🔌

Model Context Protocol servers for extending Claude Code with custom tools, prompts, and resources.

## 🎯 Overview

This directory contains MCP (Model Context Protocol) servers that extend Claude Code's capabilities with domain-specific tools, structured prompts, and dynamic resources. MCP servers enable powerful integrations and custom workflows.

## 📁 Repository Structure

```
MCP/
├── plans-mcp-server/            # MCP server template
├── README.md                    # This file
└── server_template/             # Template for new MCP servers
    ├── src/
    ├── README.md
    ├── package.json
    └── tsconfig.ts
```

## 🚀 Getting Started

### What is MCP?

Model Context Protocol (MCP) is a standard for connecting AI assistants to external systems. MCP servers provide:

- **🔧 Tools** - Functions Claude can call to perform actions
- **📋 Prompts** - Pre-built prompts for common tasks  
- **📚 Resources** - Dynamic content that Claude can access

### Basic MCP Server Structure

```typescript
// Server implementation example
import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server(
  {
    name: "my-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
      prompts: {},
      resources: {}
    }
  }
);

// Register tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "my_tool",
        description: "Description of what this tool does",
        inputSchema: {
          type: "object",
          properties: {
            // Tool parameters
          }
        }
      }
    ]
  };
});
```

## 📋 Available Servers

*This section will be updated as MCP servers are added to the repository.*

### Coming Soon
- **Data Analysis Server** - Tools for data processing and visualization
- **Web Scraping Server** - Resources for web content extraction
- **API Integration Server** - Tools for external API connections
- **Development Tools Server** - Utilities for development workflows

## 🛠️ Development

### Creating a New MCP Server

1. **Use the template:**
   ```bash
   cp -r MCP/server_template MCP/my-new-server
   cd MCP/my-new-server
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Implement your server:**
   - Add tools in `src/tools/`
   - Add prompts in `src/prompts/`
   - Add resources in `src/resources/`

4. **Test the server:**
   ```bash
   npm run build
   npm run start
   ```

5. **Configure Claude Code:**
   ```json
   // Add to ~/.claude/claude_desktop_config.json
   {
     "mcpServers": {
       "my-new-server": {
         "command": "node",
         "args": ["path/to/my-new-server/build/index.js"]
       }
     }
   }
   ```

### Best Practices

- **Follow MCP standards** - Use official SDK and patterns
- **Document thoroughly** - Include README with setup and usage
- **Test extensively** - Verify tools work in Claude Code
- **Handle errors gracefully** - Provide meaningful error messages
- **Use TypeScript** - Better type safety and development experience

## 📖 Documentation Templates

Use the provided template for consistent documentation:

- [`MCP_readme_template.md`](../ai_docs/MCP_readme_template.md) - Standard MCP server documentation

## 🔗 Resources

### Official Documentation
- [MCP Specification](https://modelcontextprotocol.io/) - Official MCP documentation
- [MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk) - TypeScript SDK
- [Claude Code MCP Guide](https://docs.anthropic.com/en/docs/claude-code/mcp) - Integration guide

### Example Servers
- [MCP Examples](https://github.com/modelcontextprotocol/servers) - Official example servers
- [Community Servers](https://github.com/modelcontextprotocol/servers#community-servers) - Community contributions

## 🤝 Contributing

### Adding MCP Servers

1. **Create server directory** with descriptive name
2. **Follow template structure** for consistency
3. **Add comprehensive README** using template
4. **Test with Claude Code** before submission
5. **Update this README** to list new server

### Contribution Guidelines

- Use TypeScript for better maintainability
- Include unit tests for tools and functions
- Follow MCP naming conventions
- Document all tools, prompts, and resources
- Provide setup and configuration instructions

## 🚨 Troubleshooting

### Common Issues

**Server not appearing in Claude Code:**
```json
// Check ~/.claude/claude_desktop_config.json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["correct/path/to/server.js"]
    }
  }
}
```

**Permission errors:**
```bash
# Make sure server files are executable
chmod +x path/to/server.js
```

**Connection errors:**
```bash
# Test server independently
node path/to/server.js
```

### Debugging Tips

1. **Check Claude Code logs** for connection errors
2. **Validate JSON configuration** syntax
3. **Test server independently** before integration
4. **Use TypeScript** for better error detection

---

**Extend Claude Code with powerful MCP servers** 🔌⚡

*Build custom tools, prompts, and resources for specialized workflows*
