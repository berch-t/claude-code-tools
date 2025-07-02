# Plans MCP Server Usage Examples

## Basic Usage Workflow

### 1. Plan Creation and Saving
```markdown
# In Claude Code plan mode:
# Create your project plan...

## My Web App Plan

### Overview
Building a modern web application with React and Node.js...

### Implementation Steps
1. Set up project structure
2. Create React components
3. Build API endpoints
4. Add authentication
5. Deploy to production

### Requirements
- React 18+
- Node.js 18+
- PostgreSQL database
- Authentication system

# When you exit plan mode, the plan is automatically saved!
```

**Result:**
- Plan saved to `~/.claude/Plans/projects/my-web-app/2025-07-02_plan.md`
- Master index updated
- Metadata added with tags like `["web", "react", "api", "database"]`

### 2. Listing Your Plans
```bash
# Use the list_plans tool in Claude Code
"Please list all my saved plans"
```

**Output:**
```
📋 Found 5 plan(s):

• **my-web-app** - 2025-07-02_plan.md
  📁 projects/my-web-app/2025-07-02_plan.md

• **api-microservice** - 2025-07-01_plan.md
  📁 projects/api-microservice/2025-07-01_plan.md

• **data-pipeline** - 2025-06-30_plan.md
  📁 projects/data-pipeline/2025-06-30_plan.md
```

### 3. Retrieving a Specific Plan
```bash
# Get a specific plan for reference
"Please get the plan for my-web-app project"
```

**Output:**
```markdown
---
project_name: "my-web-app"
date: "2025-07-02"
status: "validated"
tags: ["web", "react", "api", "database"]
version: "1.0"
auto_generated: true
---

# My Web App Plan

## Overview
Building a modern web application with React and Node.js...
[... full plan content ...]
```

### 4. Searching Plans
```bash
# Search for all React-related plans
"Please search my plans for React projects"
```

**Output:**
```
🔍 Found 3 plan(s) matching 'react':

• **my-web-app** - 2025-07-02_plan.md
  📁 projects/my-web-app/2025-07-02_plan.md

• **dashboard-ui** - 2025-06-28_plan.md
  📁 projects/dashboard-ui/2025-06-28_plan.md

• **component-library** - 2025-06-25_plan.md
  📁 projects/component-library/2025-06-25_plan.md
```

## Advanced Usage Scenarios

### Scenario 1: Project Series Planning
```markdown
# Plan 1: Core API
# My E-commerce Platform - API Plan
## Overview
Building the core API for an e-commerce platform...

# Plan 2: Frontend App  
# My E-commerce Platform - Frontend Plan
## Overview
Building the React frontend for the e-commerce platform...

# Plan 3: Admin Dashboard
# My E-commerce Platform - Admin Plan
## Overview
Building the admin dashboard for managing the platform...
```

**Result:** Three related plans saved under different projects, all searchable and cross-referenceable.

### Scenario 2: Iterative Planning
```markdown
# Initial plan
# Mobile App MVP Plan
## Overview
Building a minimum viable product for a mobile app...

# Later revision (saved as new file in same project)
# Mobile App MVP Plan - Phase 2
## Overview
Expanding the MVP with advanced features...
```

**Result:** Multiple plan versions in the same project folder, with the index showing the evolution of your planning.

### Scenario 3: Learning and Reference
```bash
# Finding patterns in your successful projects
"Search my plans for projects that used TypeScript"
"List all my API-related plans"
"Get the plan for that project I did last month with the microservices architecture"
```

## Integration Examples

### With Other MCP Servers
```json
// Example: Using with filesystem and git MCP servers
{
  "mcpServers": {
    "plans-mcp-server": {
      "command": "python",
      "args": ["/path/to/plans-mcp-server/src/server.py"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
    },
    "git": {
      "command": "npx", 
      "args": ["-y", "@modelcontextprotocol/server-git", "--repository", "/workspace"]
    }
  }
}
```

**Workflow:**
1. Create plan in plan mode → automatically saved by plans-mcp-server
2. Use filesystem server to create project structure
3. Use git server to initialize repository and make initial commit
4. Reference saved plan throughout development

### Custom Plan Templates
```markdown
# Template-based Planning
# Use saved plans as templates for similar projects

"Get the plan for my-successful-api project"
# Use the retrieved plan as a template
# Modify for new requirements
# Save as new plan for current project
```

## Directory Structure After Usage

```
~/.claude/Plans/
├── index.md                              # Updated with all plans
├── templates/
│   └── plan-template.md                  # Reference template
└── projects/
    ├── my-web-app/
    │   ├── 2025-07-02_plan.md            # Initial plan
    │   └── 2025-07-05_plan.md            # Revised plan
    ├── api-microservice/
    │   └── 2025-07-01_plan.md
    ├── data-pipeline/
    │   └── 2025-06-30_plan.md
    ├── mobile-app-mvp/
    │   ├── 2025-06-20_plan.md            # Phase 1
    │   └── 2025-06-27_plan.md            # Phase 2
    └── e-commerce-platform-api/
        └── 2025-06-15_plan.md
```

## Best Practices

### 1. Effective Plan Titles
```markdown
# Good examples:
"# E-commerce API Plan"
"# React Dashboard Implementation"
"# Data Pipeline Architecture Plan"

# Less effective:
"# Plan"
"# Project"
"# Implementation"
```

### 2. Consistent Project Naming
- Use descriptive, hyphenated names
- Include domain/technology when relevant
- Keep names concise but clear

### 3. Rich Plan Content
```markdown
# Include all key sections for better tagging:
- Overview with technology mentions
- Requirements (functional, technical, non-functional)
- Implementation steps
- Architecture decisions
- Technology stack
- Timeline and milestones
```

### 4. Regular Plan Reviews
```bash
# Periodically review your plan collection:
"List all my plans from the last month"
"Search for plans using PostgreSQL"
"Get the plans index to see my project evolution"
```

This creates a powerful knowledge base of your planning expertise that grows more valuable over time!