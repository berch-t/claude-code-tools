# {MCP_SERVER_NAME} {EMOJI}

{ONE_LINE_DESCRIPTION}

## 🎯 Overview

{DETAILED_DESCRIPTION}

## ✨ Features

### 🔧 **Tools**
- **{TOOL_1}** - {tool_1_description}
- **{TOOL_2}** - {tool_2_description}
- **{TOOL_3}** - {tool_3_description}

### 📋 **Prompts**
- **{PROMPT_1}** - {prompt_1_description}
- **{PROMPT_2}** - {prompt_2_description}

### 📚 **Resources**
- **{RESOURCE_1}** - {resource_1_description}
- **{RESOURCE_2}** - {resource_2_description}

## 🚀 Installation

### Prerequisites
- **Claude Code** - Latest version with MCP support
- **{DEPENDENCY_1}** - {dependency_1_purpose}
- **{DEPENDENCY_2}** - {dependency_2_purpose} (optional)

### Setup

1. **Clone the MCP server:**
   ```bash
   git clone {repository_url}
   cd {repository_directory}
   ```

2. **Install dependencies:**
   ```bash
   {installation_command}
   ```

3. **Configure Claude Code:**
   ```json
   // Add to ~/.claude/claude_desktop_config.json
   {
     "mcpServers": {
       "{server_name}": {
         "command": "{command}",
         "args": ["{args}"],
         "env": {
           "{env_var}": "{env_value}"
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

#### {TOOL_1_NAME}
**Purpose:** {tool_1_detailed_purpose}

**Parameters:**
- `{param_1}` (required) - {param_1_description}
- `{param_2}` (optional) - {param_2_description}

**Example:**
```bash
Use {tool_1_name} with {example_parameters}
```

#### {TOOL_2_NAME}
**Purpose:** {tool_2_detailed_purpose}

**Parameters:**
- `{param_3}` (required) - {param_3_description}
- `{param_4}` (optional) - {param_4_description}

**Example:**
```bash
Use {tool_2_name} with {example_parameters}
```

### Available Prompts

#### {PROMPT_1_NAME}
**Purpose:** {prompt_1_detailed_purpose}

**Usage:**
```bash
/{prompt_1_name} {prompt_1_usage_example}
```

**Example Output:**
{prompt_1_example_output}

#### {PROMPT_2_NAME}
**Purpose:** {prompt_2_detailed_purpose}

**Usage:**
```bash
/{prompt_2_name} {prompt_2_usage_example}
```

**Example Output:**
{prompt_2_example_output}

### Available Resources

#### {RESOURCE_1_NAME}
**Purpose:** {resource_1_detailed_purpose}

**Access Pattern:**
{resource_1_access_pattern}

#### {RESOURCE_2_NAME}
**Purpose:** {resource_2_detailed_purpose}

**Access Pattern:**
{resource_2_access_pattern}

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `{ENV_VAR_1}` | Yes | {env_var_1_description} | `{env_var_1_example}` |
| `{ENV_VAR_2}` | No | {env_var_2_description} | `{env_var_2_example}` |
| `{ENV_VAR_3}` | No | {env_var_3_description} | `{env_var_3_example}` |

### Configuration File
```json
{
  "{config_section_1}": {
    "{config_key_1}": "{config_value_1}",
    "{config_key_2}": "{config_value_2}"
  },
  "{config_section_2}": {
    "{config_key_3}": "{config_value_3}"
  }
}
```

## 📊 Architecture

### MCP Server Structure
```
{server_name}/
├── src/
│   ├── {main_file}           # Main server implementation
│   ├── tools/
│   │   ├── {tool_1_file}     # {tool_1_description}
│   │   └── {tool_2_file}     # {tool_2_description}
│   ├── prompts/
│   │   ├── {prompt_1_file}   # {prompt_1_description}
│   │   └── {prompt_2_file}   # {prompt_2_description}
│   └── resources/
│       └── {resource_file}   # {resource_description}
├── tests/
├── docs/
└── README.md
```

### Data Flow
1. **{STEP_1}** - {step_1_description}
2. **{STEP_2}** - {step_2_description}
3. **{STEP_3}** - {step_3_description}
4. **{STEP_4}** - {step_4_description}

## 🎯 Use Cases

### {USE_CASE_CATEGORY_1}
- **{USE_CASE_1}** - {use_case_1_description}
- **{USE_CASE_2}** - {use_case_2_description}
- **{USE_CASE_3}** - {use_case_3_description}

### {USE_CASE_CATEGORY_2}
- **{USE_CASE_4}** - {use_case_4_description}
- **{USE_CASE_5}** - {use_case_5_description}

### {USE_CASE_CATEGORY_3}
- **{USE_CASE_6}** - {use_case_6_description}
- **{USE_CASE_7}** - {use_case_7_description}

## 📋 Examples

### Example 1: {EXAMPLE_1_TITLE}
```bash
# {example_1_description}
{example_1_command}
```

**Expected Output:**
```
{example_1_output}
```

### Example 2: {EXAMPLE_2_TITLE}
```bash
# {example_2_description}
{example_2_command}
```

**Expected Output:**
```
{example_2_output}
```

### Example 3: {EXAMPLE_3_TITLE}
```bash
# {example_3_description}
{example_3_command}
```

**Expected Output:**
```
{example_3_output}
```

## 🚨 Troubleshooting

### Common Issues

**{ISSUE_1_TITLE}:**
```bash
# Problem: {issue_1_problem}
# Solution: {issue_1_solution}
{issue_1_fix_command}
```

**{ISSUE_2_TITLE}:**
- **Symptoms:** {issue_2_symptoms}
- **Cause:** {issue_2_cause}
- **Fix:** {issue_2_fix}

**{ISSUE_3_TITLE}:**
```json
// Check configuration in ~/.claude/claude_desktop_config.json
{
  "mcpServers": {
    "{server_name}": {
      // Ensure these settings are correct
      "{setting_1}": "{correct_value_1}",
      "{setting_2}": "{correct_value_2}"
    }
  }
}
```

### Debugging

1. **Check server status:**
   ```bash
   {debug_command_1}
   ```

2. **Validate configuration:**
   ```bash
   {debug_command_2}
   ```

3. **View logs:**
   ```bash
   {debug_command_3}
   ```

## 🔄 Development

### Contributing

1. **Fork the repository**
2. **Create feature branch:** `git checkout -b feature/{feature_name}`
3. **Make changes and test**
4. **Submit pull request**

### Testing

```bash
# Run tests
{test_command}

# Run specific test
{specific_test_command}

# Run with coverage
{coverage_command}
```

### Building

```bash
# Build for development
{dev_build_command}

# Build for production
{prod_build_command}
```

## 📚 API Reference

### Tool Specifications

#### {TOOL_1_NAME}
```json
{
  "name": "{tool_1_name}",
  "description": "{tool_1_description}",
  "inputSchema": {
    "type": "object",
    "properties": {
      "{property_1}": {
        "type": "{type_1}",
        "description": "{property_1_description}"
      }
    },
    "required": ["{required_property}"]
  }
}
```

### Resource Specifications

#### {RESOURCE_1_NAME}
```json
{
  "uri": "{resource_1_uri}",
  "name": "{resource_1_name}",
  "description": "{resource_1_description}",
  "mimeType": "{resource_1_mime_type}"
}
```

## 🔗 Related Projects

- [{RELATED_PROJECT_1}]({related_project_1_url}) - {related_project_1_description}
- [{RELATED_PROJECT_2}]({related_project_2_url}) - {related_project_2_description}
- [MCP Specification](https://modelcontextprotocol.io/) - Official MCP documentation

## 📄 License

This project is licensed under the {LICENSE_TYPE} License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- **GitHub Issues:** [Report bugs or request features]({issues_url})
- **Documentation:** [Full documentation]({docs_url})
- **Community:** [Join discussions]({community_url})

---

**{CLOSING_TAGLINE}** {CLOSING_EMOJI}

*{ADDITIONAL_NOTES_OR_ATTRIBUTION}*