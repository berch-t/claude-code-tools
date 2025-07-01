# Contributing to Claude Code Tools 🤝

Thank you for your interest in contributing to Claude Code Tools! This repository is designed to be a collaborative effort to build the best possible tools and documentation for the Claude Code community.

## 🎯 Ways to Contribute

### 🛠️ **Commands**
- Add new Claude Code slash commands
- Improve existing command functionality
- Create command variations for specific use cases
- Enhance command documentation

### 🔌 **MCP Servers**
- Develop new MCP servers for specific domains
- Contribute tools, prompts, and resources
- Improve existing MCP server implementations
- Add integration examples

### 📚 **Documentation**
- Expand ai_docs with new guides
- Update existing documentation
- Create tutorials and examples
- Improve README files

### 📋 **Templates**
- Contribute project templates
- Add component templates
- Create configuration templates
- Develop workflow templates

### 🛠️ **Tools**
- Build automation scripts
- Create analysis utilities
- Develop code generators
- Add integration helpers

## 🚀 Getting Started

### Prerequisites

- **Claude Code** - Latest version
- **UV** - Python package manager
- **Git** - Version control
- **Node.js** - For MCP servers (optional)

### Setup

1. **Fork the repository:**
   ```bash
   git clone https://github.com/berch-t/claude-code-tools.git
   cd claude-code-tools
   ```

2. **Create feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Test your changes:**
   ```bash
   # Test commands
   cp commands/your-command/your-command.md ~/.claude/commands/
   
   # Test tools
   uv run tools/your-tool/your-tool.py
   ```

## 📋 Contribution Guidelines

### **Commands**

#### Structure Requirements
```
commands/
└── your-command/
    ├── README.md              # Comprehensive documentation
    └── your-command.md        # Claude Code command file
```

#### Documentation Standards
- Use the [`commands_readme_template.md`](ai_docs/commands_readme_template.md)
- Include installation instructions
- Provide usage examples
- Document all parameters and options
- Add troubleshooting section

#### Testing Requirements
- Test with various input types
- Verify error handling
- Ensure clean output formatting
- Test with different Claude Code versions

### **MCP Servers**

#### Structure Requirements
```
MCP/
└── your-server/
    ├── README.md              # Server documentation
    ├── package.json           # Dependencies and scripts
    ├── src/
    │   ├── index.ts          # Main server file
    │   ├── tools/            # Tool implementations
    │   ├── prompts/          # Prompt definitions
    │   └── resources/        # Resource handlers
    └── tests/                # Test files
```

#### Development Standards
- Use TypeScript for type safety
- Follow MCP specification standards
- Include comprehensive error handling
- Provide clear tool descriptions
- Document all configuration options

#### Testing Requirements
- Unit tests for all tools
- Integration tests with Claude Code
- Error scenario testing
- Performance testing for resource-heavy operations

### **Documentation**

#### AI Docs Standards
- Follow existing format and structure
- Include practical examples
- Reference latest tool versions
- Provide troubleshooting guidance
- Include related resources

#### Content Requirements
- Clear, actionable guidance
- Code examples that work
- Screenshots when helpful
- Links to official documentation
- Regular updates for accuracy

### **Templates**

#### Structure Requirements
```
templates/
└── category/
    └── template-name/
        ├── README.md          # Template documentation
        ├── package.json       # Dependencies (if applicable)
        ├── src/              # Template source code
        ├── tests/            # Test files
        └── examples/         # Usage examples
```

#### Quality Standards
- Production-ready code
- Comprehensive configuration
- Clear customization instructions
- Multiple usage examples
- Integration with Claude Code commands

### **Tools**

#### Development Requirements
- Use UV for dependency management
- Include inline script dependencies
- Provide rich console output
- Implement proper error handling
- Include comprehensive help text

#### Structure Standards
```python
#!/usr/bin/env python3
# /// script
# dependencies = ["click", "rich", "pathlib"]
# ///

"""
Tool description and usage information.
"""

import click
from rich.console import Console

@click.command()
@click.option('--input', '-i', help='Input description')
def main(input: str):
    """Main tool functionality."""
    # Implementation
```

## 🔍 Code Review Process

### Submission Requirements

1. **Clear Description** - Explain what your contribution does
2. **Testing Evidence** - Show that your changes work
3. **Documentation** - Include or update relevant docs
4. **Following Standards** - Adhere to project conventions

### Review Criteria

#### **Functionality**
- ✅ Works as described
- ✅ Handles edge cases
- ✅ Provides clear error messages
- ✅ Integrates well with Claude Code

#### **Code Quality**
- ✅ Clean, readable code
- ✅ Proper error handling
- ✅ Follows project conventions
- ✅ Includes necessary comments

#### **Documentation**
- ✅ Comprehensive README
- ✅ Clear usage examples
- ✅ Installation instructions
- ✅ Troubleshooting guidance

#### **Testing**
- ✅ Works in multiple scenarios
- ✅ Error cases handled
- ✅ Performance acceptable
- ✅ No regressions introduced

## 📝 Pull Request Template

When submitting a pull request, please use this template:

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] New command
- [ ] New MCP server
- [ ] Documentation update
- [ ] Template addition
- [ ] Tool creation
- [ ] Bug fix
- [ ] Enhancement

## Testing
- [ ] Tested with Claude Code
- [ ] Tested error scenarios
- [ ] Verified documentation accuracy
- [ ] Checked for regressions

## Screenshots/Examples
Include relevant examples or screenshots.

## Related Issues
Closes #(issue number)
```

## 🐛 Reporting Issues

### Bug Reports

Include the following information:

1. **Environment**
   - Claude Code version
   - Operating system
   - Python version (for tools)
   - Node.js version (for MCP servers)

2. **Reproduction Steps**
   - Exact commands used
   - Input data (if applicable)
   - Expected vs actual behavior

3. **Error Messages**
   - Complete error output
   - Log files (if available)
   - Screenshots (if relevant)

### Feature Requests

Provide the following details:

1. **Use Case** - What problem does this solve?
2. **Proposed Solution** - How should it work?
3. **Alternatives** - What other approaches were considered?
4. **Implementation** - Any ideas about how to build it?

## 🏆 Recognition

Contributors will be recognized in several ways:

- **GitHub Contributors** - Listed in repository contributors
- **Documentation Credits** - Mentioned in relevant documentation
- **Release Notes** - Acknowledged in version releases
- **Community Showcase** - Featured in community examples

## 📚 Resources

### Documentation
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [MCP Specification](https://modelcontextprotocol.io/)
- [UV Documentation](https://docs.astral.sh/uv/)

### Templates
- [Command Template](ai_docs/commands_readme_template.md)
- [MCP Server Template](ai_docs/MCP_readme_template.md)

### Examples
- Browse existing commands in [`commands/`](commands/)
- Review MCP servers in [`MCP/`](MCP/)
- Check documentation in [`ai_docs/`](ai_docs/)

## ❓ Questions?

- **GitHub Issues** - For bug reports and feature requests
- **GitHub Discussions** - For questions and general discussion
- **Documentation** - Check existing docs first

---

**Thank you for helping make Claude Code Tools better for everyone!** 🚀

*Every contribution, no matter how small, makes a difference in the community.*