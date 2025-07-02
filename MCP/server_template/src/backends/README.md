# Backend Script Templates 🔧

This directory contains complete MCP server implementations in different languages and runtimes. Choose the one that best fits your needs and environment.

## 📁 Available Backends

### 🐍 Python (`python/`)
**Best for:** Data processing, AI/ML integration, scientific computing

- **File:** `server.py`
- **Dependencies:** `mcp` (via UV or pip)
- **Features:** 
  - UV script dependencies (`# /// script`)
  - Async/await support
  - Type hints
  - Comprehensive error handling

**Usage:**
```bash
# With UV (recommended)
uv run server.py

# With pip
pip install mcp
python server.py
```

### 🟨 Node.js (`nodejs/`)
**Best for:** Web integrations, API connections, JavaScript ecosystem

- **File:** `server.js` 
- **Dependencies:** `@modelcontextprotocol/sdk`
- **Features:**
  - ES modules
  - Modern JavaScript
  - Built-in watch mode
  - Lightweight and fast

**Usage:**
```bash
npm install
npm start

# Development mode
npm run dev
```

### 🔷 TypeScript (`typescript/`)
**Best for:** Large projects, type safety, enterprise development

- **File:** `server.ts`
- **Dependencies:** `@modelcontextprotocol/sdk` + TypeScript toolchain
- **Features:**
  - Full type safety
  - Interface definitions
  - Compile-time error checking
  - Advanced IDE support

**Usage:**
```bash
npm install
npm run build
npm start

# Development mode
npm run dev
```

## 🎯 Choosing a Backend

### Use **Python** when:
- Building data analysis or ML tools
- Integrating with Python libraries
- Processing files or scientific data
- Prefer UV dependency management

### Use **Node.js** when:
- Building web integrations
- Working with APIs and HTTP requests
- Need lightweight, fast startup
- Prefer JavaScript ecosystem

### Use **TypeScript** when:
- Building complex, large-scale servers
- Need strong type safety
- Working in team environments
- Want comprehensive IDE support

## 🔄 Template Placeholders

All backends use the same placeholder system:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{SERVER_NAME}}` | Server name | `data-processor` |
| `{{DESCRIPTION}}` | Brief description | `Process and analyze data files` |
| `{{VERSION}}` | Version number | `1.0.0` |
| `{{AUTHOR}}` | Author info | `John Doe <john@example.com>` |
| `{{LICENSE}}` | License type | `MIT` |
| `{{KEYWORDS}}` | Additional keywords | `data,analysis,processing` |

## 🚀 Quick Start

1. **Choose your backend** based on your needs
2. **Copy the backend files** to your project root:
   ```bash
   # For Python
   cp src/backends/python/* .
   
   # For Node.js  
   cp src/backends/nodejs/* .
   
   # For TypeScript
   cp src/backends/typescript/* .
   ```
3. **Replace placeholders** with your actual values
4. **Install dependencies** and run

## 🔧 Customization

### Adding Tools
All backends follow the same pattern:
1. Add tool definition to the tools array
2. Add handler function 
3. Add case in the tool switch statement

### Adding Prompts/Resources
1. Add to respective arrays
2. Implement handler functions
3. Add request handlers

### Configuration Examples

Each backend includes example configurations for Claude Code:

**Python with UV:**
```json
{
  "command": "uv",
  "args": ["run", "server.py"]
}
```

**Node.js:**
```json
{
  "command": "node", 
  "args": ["server.js"]
}
```

**TypeScript:**
```json
{
  "command": "node",
  "args": ["build/server.js"]
}
```

## 📚 Examples

Each backend includes:
- ✅ **Example tool** - Message processing with validation
- ✅ **Example prompt** - Content generation with parameters  
- ✅ **Example resource** - Server information access
- ✅ **Error handling** - Comprehensive error management
- ✅ **Type safety** - Appropriate for each language

## 🎯 Production Ready

All backends include:
- **Graceful shutdown** handling
- **Error boundary** protection  
- **Input validation** and sanitization
- **Logging** and debugging support
- **Configuration** examples for Claude Code

Choose the backend that matches your project needs and start building powerful MCP servers! 🚀