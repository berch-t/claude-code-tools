# Tools 🛠️

Utility scripts, helpers, and automation tools that enhance Claude Code development workflows.

## 🎯 Overview

This directory contains standalone tools and utilities designed to complement Claude Code's capabilities. These tools handle common development tasks, automate repetitive processes, and provide specialized functionality for specific workflows.

## 📁 Repository Structure

```
tools/
├── README.md                    # This file
├── automation/                  # Development automation scripts
│   ├── setup-project.py
│   ├── generate-docs.py
│   └── sync-configs.py
├── analyzers/                   # Code and project analysis tools
│   ├── dependency-analyzer.py
│   ├── complexity-metrics.py
│   └── security-scanner.py
├── generators/                  # Code and content generators
│   ├── component-generator.py
│   ├── api-client-generator.py
│   └── test-generator.py
├── integrations/               # Third-party integrations
│   ├── github-tools/
│   ├── ai-service-connectors/
│   └── deployment-helpers/
└── utilities/                  # General-purpose utilities
    ├── file-processors/
    ├── data-converters/
    └── development-helpers/
```

## 🚀 Featured Tools

### 🤖 **Automation Scripts**

#### Project Setup Automation
**File:** `automation/setup-project.py`
```python
# /// script  
# dependencies = ["uv", "click", "pathlib"]
# ///

# Automated project initialization with Claude Code optimization
uv run automation/setup-project.py --template react-typescript --ai-ready
```

**Features:**
- Template-based project creation
- Automatic dependency management with UV
- Claude Code configuration setup
- Git initialization with proper .gitignore
- Documentation generation

#### Documentation Generator
**File:** `automation/generate-docs.py`
```python
# /// script
# dependencies = ["ast", "markdown", "jinja2"]
# ///

# Extract documentation from code and generate markdown
uv run automation/generate-docs.py --source src/ --output docs/
```

**Features:**
- Automatic API documentation from TypeScript/Python
- README generation from code comments
- Changelog creation from git history
- Integration with `/populate_docs` command

### 📊 **Analysis Tools**

#### Dependency Analyzer
**File:** `analyzers/dependency-analyzer.py`

Analyzes project dependencies for security, licensing, and maintenance issues.

```bash
# Analyze package.json dependencies
uv run analyzers/dependency-analyzer.py --project-type npm

# Check Python requirements
uv run analyzers/dependency-analyzer.py --project-type python
```

**Output:**
- Security vulnerability reports
- License compatibility analysis
- Outdated dependency detection
- Dependency tree visualization

#### Code Complexity Metrics
**File:** `analyzers/complexity-metrics.py`

Measures code complexity to guide refactoring efforts.

```bash
# Analyze TypeScript/JavaScript
uv run analyzers/complexity-metrics.py --lang typescript --path src/

# Analyze Python code
uv run analyzers/complexity-metrics.py --lang python --path .
```

**Metrics:**
- Cyclomatic complexity
- Cognitive complexity
- Technical debt estimation
- Refactoring recommendations

### 🏗️ **Code Generators**

#### Component Generator
**File:** `generators/component-generator.py`

Generates React components with TypeScript, tests, and documentation.

```bash
# Generate data table component
uv run generators/component-generator.py \
  --name DataTable \
  --type component \
  --props "data,columns,onSort" \
  --tests \
  --storybook
```

**Generated Files:**
- `DataTable.tsx` - Main component
- `DataTable.test.tsx` - Unit tests
- `DataTable.stories.tsx` - Storybook stories  
- `DataTable.md` - Component documentation

#### API Client Generator
**File:** `generators/api-client-generator.py`

Creates type-safe API clients from OpenAPI specifications.

```bash
# Generate from OpenAPI spec
uv run generators/api-client-generator.py \
  --spec api-spec.yaml \
  --output src/api/ \
  --client-type fetch
```

**Features:**
- TypeScript type generation
- Request/response validation
- Error handling patterns
- Authentication integration

### 🔗 **Integration Tools**

#### GitHub Tools
**Path:** `integrations/github-tools/`

Collection of GitHub automation utilities.

```bash
# Sync repository settings
uv run integrations/github-tools/sync-repo-settings.py --config repo-config.yaml

# Generate release notes
uv run integrations/github-tools/generate-release-notes.py --from v1.0.0 --to v1.1.0
```

#### AI Service Connectors
**Path:** `integrations/ai-service-connectors/`

Pre-built connectors for AI services and APIs.

```bash
# OpenAI API wrapper
uv run integrations/ai-service-connectors/openai-client.py --prompt "Analyze this code"

# Anthropic Claude API
uv run integrations/ai-service-connectors/claude-client.py --file input.txt
```

## 🎯 Usage with Claude Code

### Command Integration

Most tools are designed to work seamlessly with Claude Code commands:

#### With `/ai_docs`
```bash
# Get tool-specific guidance
/ai_docs How do I use the component generator for a complex data visualization?

# Tool configuration help
/ai_docs What are the best settings for the dependency analyzer?
```

#### With `/prime`
```bash
# Prime context with project analysis
/prime && uv run analyzers/complexity-metrics.py --summary
```

#### With `/infinite`
```bash
# Iteratively improve generated code
/infinite Use the component generator to create and refine a dashboard component
```

### Workflow Integration

#### Development Workflow
```bash
# 1. Set up new project
uv run automation/setup-project.py --template react-typescript

# 2. Generate initial components
uv run generators/component-generator.py --name App --type page

# 3. Analyze code quality
uv run analyzers/complexity-metrics.py --path src/

# 4. Generate documentation
uv run automation/generate-docs.py --output docs/
```

#### Maintenance Workflow
```bash
# 1. Check dependencies
uv run analyzers/dependency-analyzer.py --security-check

# 2. Update configurations
uv run automation/sync-configs.py --latest

# 3. Generate release docs
uv run integrations/github-tools/generate-release-notes.py
```

## 🔧 Tool Development

### Creating New Tools

#### Standard Tool Structure
```python
#!/usr/bin/env python3
# /// script
# dependencies = ["click", "pathlib", "rich"]
# ///

"""
Tool Name - Brief description
Usage: uv run tool-name.py [options]
"""

import click
from pathlib import Path
from rich.console import Console

console = Console()

@click.command()
@click.option('--input', '-i', help='Input file or directory')
@click.option('--output', '-o', help='Output destination')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def main(input: str, output: str, verbose: bool):
    """Tool description and usage information."""
    
    if verbose:
        console.print("[green]Starting tool execution...[/green]")
    
    # Tool implementation
    
    if verbose:
        console.print("[green]Tool execution completed![/green]")

if __name__ == "__main__":
    main()
```

#### Best Practices

1. **UV Integration** - Use inline dependencies for easy execution
2. **Rich Output** - Provide beautiful, informative console output  
3. **Click CLI** - Consistent command-line interface
4. **Error Handling** - Graceful failure with helpful messages
5. **Documentation** - Clear docstrings and help text
6. **Testing** - Unit tests for core functionality

### Tool Categories

#### **Automation Tools**
- Project setup and initialization
- Configuration synchronization
- Repetitive task automation
- CI/CD pipeline helpers

#### **Analysis Tools**
- Code quality assessment
- Security vulnerability scanning
- Performance bottleneck detection
- Architecture analysis

#### **Generation Tools**
- Code scaffolding and templates
- Documentation generation
- Test case creation
- Configuration generation

#### **Integration Tools**
- API client wrappers
- Service connectors
- Deployment utilities
- External tool bridges

## 📖 Tool Documentation

### Documentation Standards

Each tool should include:

1. **Header Comment** with description and usage
2. **Click Help Text** for command-line options
3. **Docstrings** for functions and classes
4. **Examples** in tool README or docstring
5. **Error Messages** that guide users to solutions

### Example Documentation
```python
"""
Component Generator - Create React components with TypeScript

This tool generates complete React components including:
- TypeScript component file
- Unit tests with Jest/Vitest
- Storybook stories
- Component documentation

Usage:
    uv run generators/component-generator.py --name Button --props "text,onClick,variant"

Examples:
    # Simple component
    uv run generators/component-generator.py --name Alert --props "message,type"
    
    # Complex component with tests
    uv run generators/component-generator.py --name DataGrid --props "data,columns" --tests --storybook
"""
```

## 🚨 Troubleshooting

### Common Issues

**UV not found:**
```bash
# Install UV package manager
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Dependencies not installing:**
```bash
# Clear UV cache
uv cache clean

# Reinstall dependencies
uv run --refresh tool-name.py
```

**Permission errors:**
```bash
# Make tools executable
chmod +x tools/**/*.py
```

### Performance Tips

1. **Use UV caching** - Dependencies are cached for faster execution
2. **Batch operations** - Process multiple files/projects together
3. **Parallel execution** - Use asyncio for I/O bound operations
4. **Progress indicators** - Use Rich progress bars for long operations

## 🤝 Contributing

### Adding New Tools

1. **Choose appropriate category** (automation, analyzers, generators, etc.)
2. **Follow standard structure** with UV dependencies
3. **Include comprehensive documentation**
4. **Add usage examples** and test cases
5. **Update this README** with tool description

### Tool Requirements

- Python 3.9+ compatibility
- UV dependency management
- Click for CLI interface
- Rich for output formatting
- Comprehensive error handling
- Clear documentation

---

**Supercharge your development workflow with specialized tools** 🛠️⚡

*Designed to work seamlessly with Claude Code for maximum productivity*