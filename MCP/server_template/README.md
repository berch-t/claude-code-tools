# {{SERVER_NAME}} {{EMOJI}}

{{DESCRIPTION}}

## 🚀 Installation

1. **Copy this template:**
   ```bash
   cp -r server_template {{SERVER_NAME}}
   cd {{SERVER_NAME}}
   ```

2. **Choose your backend:**
   ```bash
   # For Python (recommended for data/AI tasks)
   cp src/backends/python/* .
   
   # For Node.js (recommended for web/API integrations)
   cp src/backends/nodejs/* .
   
   # For TypeScript (recommended for complex projects)
   cp src/backends/typescript/* .
   ```

3. **Customize the template:**
   - Replace `{{SERVER_NAME}}` with your server name
   - Replace `{{DESCRIPTION}}` with your description
   - Replace `{{VERSION}}` with your version (default: 1.0.0)
   - Replace `{{AUTHOR}}` with your name
   - Replace `{{LICENSE}}` with your license (default: MIT)

4. **Install and run:**
   ```bash
   # Python with UV
   uv run server.py
   
   # Node.js
   npm install && npm start
   
   # TypeScript  
   npm install && npm run build && npm start
   ```

5. **Configure Claude Code:**
   ```json
   {
     "mcpServers": {
       "{{SERVER_NAME}}": {
         "command": "uv|node",
         "args": ["run", "server.py"] // or ["server.js"] or ["build/server.js"]
       }
     }
   }
   ```

## 🔧 Development

### Available Tools

#### example_tool
- **Purpose:** Example tool demonstrating basic MCP functionality
- **Parameters:** 
  - `message` (required) - A message to process

### Building
```bash
npm run build    # Build once
npm run dev      # Build with watch mode
npm run start    # Run the server
```

### Testing
```bash
# Test the server
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}' | node build/index.js
```

## 📁 Template Structure

```
{{SERVER_NAME}}/
├── src/
│   ├── index.ts          # Main TypeScript server (original)
│   └── backends/         # Multiple backend implementations
│       ├── python/       # Python implementation with UV support
│       │   ├── server.py
│       │   ├── requirements.txt
│       │   └── pyproject.toml
│       ├── nodejs/       # Node.js implementation  
│       │   ├── server.js
│       │   └── package.json
│       ├── typescript/   # Advanced TypeScript implementation
│       │   ├── server.ts
│       │   ├── package.json
│       │   └── tsconfig.json
│       └── README.md     # Backend selection guide
├── examples/             # Configuration examples
├── package.json         # Default dependencies and scripts
├── tsconfig.json        # TypeScript configuration
└── README.md           # This file
```

## 🎯 Customization

### Adding New Tools

1. Create a new tool in `src/tools/`
2. Add it to the tools list in `src/index.ts`
3. Add a handler in the `CallToolRequestSchema` handler

### Adding Prompts/Resources

1. Add capabilities to the server configuration
2. Implement the appropriate request handlers
3. Create the prompt/resource definitions

---

**Built with the claude-code-tools MCP Server Template** 🔧