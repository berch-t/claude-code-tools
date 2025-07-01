# Templates 📋

Reusable code templates, project scaffolds, and boilerplates for accelerated development with Claude Code.

## 🎯 Overview

This directory contains production-ready templates for common development patterns, project structures, and workflow configurations. Templates are designed to work seamlessly with Claude Code's agentic development capabilities.

## 📁 Repository Structure

```
templates/
├── README.md                    # This file
├── projects/                    # Full project templates
│   ├── react-typescript-app/
│   ├── python-cli-tool/
│   └── mcp-server-starter/
├── components/                  # Reusable component templates
│   ├── react-components/
│   └── ui-patterns/
├── configs/                     # Configuration templates
│   ├── eslint-configs/
│   ├── typescript-configs/
│   └── vite-configs/
└── workflows/                   # CI/CD and automation templates
    ├── github-actions/
    └── deployment-scripts/
```

## 🚀 Quick Start

### Using Templates with Claude Code

Templates are designed to be used with Claude Code's intelligent code generation:

```bash
# Generate project from template
/ai_docs Create a new React TypeScript project using our template structure

# Customize component template  
/ai_docs Generate a data table component based on our React component template

# Apply configuration template
/ai_docs Set up ESLint configuration using our standard template
```

## 📋 Available Templates

### 🎯 **Project Templates**

#### React TypeScript Application
**Path:** `projects/react-typescript-app/`
- Modern React 18+ with TypeScript 5.0+
- Vite build system with optimized configuration
- ESLint + Prettier + Husky setup
- Testing with Vitest and React Testing Library
- Component library ready (Aceternity UI compatible)

#### Python CLI Tool
**Path:** `projects/python-cli-tool/`
- Click-based CLI framework
- UV for dependency management
- Type hints with Pydantic
- Pytest testing setup
- GitHub Actions CI/CD

#### MCP Server Starter
**Path:** `projects/mcp-server-starter/`
- TypeScript MCP server template
- Tools, prompts, and resources structure
- Claude Code integration ready
- Comprehensive testing setup
- Documentation templates

### 🧩 **Component Templates**

#### React Components
**Path:** `components/react-components/`
- **Data Display** - Tables, cards, lists, grids
- **Forms** - Input components, validation, submission
- **Navigation** - Menus, breadcrumbs, pagination
- **Feedback** - Alerts, toasts, modals, loading states
- **Layout** - Containers, sidebars, headers, footers

#### UI Patterns  
**Path:** `components/ui-patterns/`
- **Animation Patterns** - Framer Motion implementations
- **State Management** - Zustand and React Query patterns
- **Accessibility** - WCAG compliant component patterns
- **Performance** - Optimized rendering patterns

### ⚙️ **Configuration Templates**

#### ESLint Configurations
**Path:** `configs/eslint-configs/`
- **React Projects** - React-specific rules and plugins
- **TypeScript Projects** - Type-aware linting
- **Node.js Projects** - Server-side JavaScript rules
- **Monorepo** - Shared configurations across packages

#### TypeScript Configurations
**Path:** `configs/typescript-configs/`
- **Strict Mode** - Maximum type safety
- **Library Mode** - For package development
- **Application Mode** - For applications
- **Monorepo** - Project references setup

### 🔄 **Workflow Templates**

#### GitHub Actions
**Path:** `workflows/github-actions/`
- **CI/CD Pipeline** - Test, build, deploy
- **Release Automation** - Semantic versioning
- **Code Quality** - Linting, testing, coverage
- **Security** - Dependency scanning, SAST

## 🛠️ Usage Patterns

### With Claude Code Commands

#### `/ai_docs` Integration
```bash
# Reference templates in documentation requests
/ai_docs Show me how to set up a React TypeScript project using our template

# Get template-specific guidance
/ai_docs What's the best way to customize our MCP server template?
```

#### `/infinite` Enhancement
```bash
# Iteratively improve templates
/infinite Optimize our React component template for better performance

# Evolve templates based on usage
/infinite Update Python CLI template with latest best practices
```

#### `/populate_docs` Documentation
```bash
# Document template usage
/populate_docs React TypeScript Template Usage Guide

# Create implementation guides
/populate_docs MCP Server Development with Templates
```

### Direct File Usage

#### Copy Template Structure
```bash
# Copy entire project template
cp -r templates/projects/react-typescript-app/ ./my-new-project

# Copy specific component
cp templates/components/react-components/DataTable.tsx ./src/components/

# Apply configuration
cp templates/configs/eslint-configs/react.js ./.eslintrc.js
```

#### Template Customization
```bash
# Use template as starting point
/ai_docs Customize the Python CLI template for a data processing tool

# Merge multiple templates
/ai_docs Combine React component patterns with our TypeScript config
```

## 📖 Template Structure

### Standard Template Format

```
template-name/
├── README.md                    # Template documentation
├── package.json                 # Dependencies and scripts (if applicable)
├── .eslintrc.js                # Linting configuration
├── tsconfig.json               # TypeScript configuration (if applicable)
├── src/                        # Source code
│   ├── index.ts
│   └── components/
├── tests/                      # Test files
├── docs/                       # Additional documentation
└── examples/                   # Usage examples
```

### Template Documentation Requirements

Each template must include:

1. **Purpose & Use Cases** - When to use this template
2. **Dependencies** - Required tools and packages
3. **Setup Instructions** - Step-by-step initialization
4. **Customization Guide** - How to adapt for specific needs
5. **Examples** - Real-world usage scenarios
6. **Integration Notes** - Claude Code compatibility details

## 🎯 Creating New Templates

### Template Development Process

1. **Identify Common Patterns**
   - Analyze frequently used code structures
   - Document repetitive setup processes
   - Gather community feedback on needs

2. **Design Template Structure**
   - Create modular, reusable components
   - Include comprehensive configuration
   - Add thorough documentation

3. **Test with Claude Code**
   - Verify `/ai_docs` integration works
   - Test with various customization scenarios
   - Ensure generated code is production-ready

4. **Documentation & Examples**
   - Write comprehensive README
   - Include real-world examples
   - Document customization patterns

### Best Practices

- **Modular Design** - Templates should be composable
- **Configuration Driven** - Easy to customize without editing core files
- **Well Documented** - Clear setup and usage instructions
- **Production Ready** - Include testing, linting, CI/CD
- **Claude Code Optimized** - Designed for AI-assisted development

## 🔧 Maintenance

### Template Updates

- **Regular Reviews** - Monthly updates for dependencies
- **Community Feedback** - Incorporate usage suggestions
- **Best Practice Evolution** - Update based on industry changes
- **Claude Code Compatibility** - Ensure ongoing integration

### Versioning Strategy

- **Semantic Versioning** - Major.Minor.Patch for templates
- **Changelog** - Document all template changes
- **Migration Guides** - Help users upgrade existing projects
- **Backward Compatibility** - Maintain support when possible

## 🤝 Contributing

### Adding New Templates

1. **Follow structure standards** outlined above
2. **Test thoroughly** with multiple use cases
3. **Document comprehensively** with examples
4. **Integrate with Claude Code** commands
5. **Update this README** to list new template

### Template Guidelines

- Use TypeScript when applicable for better Claude Code integration
- Include comprehensive ESLint and Prettier configurations
- Provide multiple customization examples
- Ensure accessibility and performance best practices
- Document Claude Code-specific usage patterns

---

**Accelerate development with battle-tested templates** 📋⚡

*Designed for seamless integration with Claude Code's agentic workflows*