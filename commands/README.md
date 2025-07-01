# Claude Code Commands 🎯

A collection of powerful slash commands for Claude Code that enhance development productivity through agentic workflows and intelligent automation.

## 📋 Commands Overview

| Command | Purpose | Use Case | Output |
|---------|---------|----------|---------|
| [`/ai_docs`](#-ai_docs) | Smart documentation assistant | Context-aware help using ai_docs folder | Intelligent responses |
| [`/infinite`](#-infinite) | Infinite agentic loops | Iterative generation & refinement | Self-improving code |
| [`/populate_docs`](#-populate_docs) | Documentation generator | Extract docs from conversation history | Markdown files |
| [`/prime`](#-prime) | Context window priming | Load git files for context | File listings |
| [`/wisdom`](#-wisdom) | Wisdom extraction | Extract insights from YouTube/text | Rich analysis |

## 🧠 `/ai_docs` - Smart Documentation Assistant

**Purpose:** Provides intelligent assistance by referencing your ai_docs folder content for the most current patterns, components, and best practices.

### Features
- Automatic relevance detection for documentation files
- Framework-specific guidance (React, TypeScript, Framer Motion, etc.)
- Pattern-based recommendations
- Best practices integration

### Usage
```bash
/ai_docs How do I create animated gradients with Framer Motion?
/ai_docs Show me React TypeScript patterns for data fetching
/ai_docs What are Claude Code best practices for large projects?
```

### How It Works
1. Analyzes your request to determine relevant documentation
2. Reads appropriate files from `~/.claude/ai_docs/`
3. Provides solutions using documented patterns
4. References latest features and best practices

---

## 🔄 `/infinite` - Infinite Agentic Loop Generation

**Purpose:** Creates sophisticated iterative generation processes for complex development tasks that benefit from multiple refinement cycles.

### Features
- Self-improving code generation
- Quality checkpoints and validation
- Iterative refinement processes
- Automated testing integration
- Convergence detection

### Usage
```bash
/infinite Create a React component that progressively improves its performance
/infinite Build a Python script that optimizes itself through iterations
/infinite Design an API that refines its schema based on usage patterns
```

### Use Cases
- Complex algorithm development
- UI/UX iterative improvement
- Performance optimization cycles
- Architecture refinement
- Test-driven development loops

---

## 📚 `/populate_docs` - Documentation Generator

**Purpose:** Analyzes conversation history to extract meaningful work accomplished and creates comprehensive documentation files.

### Features
- Conversation history analysis
- Real implementation extraction
- Automatic markdown generation
- Discovery documentation
- Best practices capture

### Usage
```bash
/populate_docs React Authentication System
/populate_docs MCP Server Development Guide
/populate_docs Python Automation Workflows
```

### Output
- Creates new `.md` file in `ai_docs/` folder
- Documents actual implementation details
- Includes code examples and patterns
- Captures lessons learned and discoveries

---

## ⚡ `/prime` - Context Window Priming

**Purpose:** Efficiently primes Claude Code's context window with essential project information using git file listings.

### Features
- Git repository file enumeration
- Instant context loading
- Project structure awareness
- Fast startup for new sessions

### Usage
```bash
/prime
```

### How It Works
1. Runs `git ls-files` to get complete file listing
2. Loads project structure into context
3. Enables immediate project awareness
4. Eliminates need for manual file exploration

### Benefits
- Faster project onboarding
- Complete codebase visibility
- Efficient context utilization
- Reduced exploration time

---

## 🧠 `/wisdom` - YouTube/Text Wisdom Extraction

**Purpose:** Extracts valuable insights from YouTube videos or text content using Daniel Miessler's proven extractwisdom pattern from the Fabric framework.

### Features
- **YouTube Processing:** Auto-subtitle extraction + Whisper fallback
- **Text Analysis:** Direct content processing
- **Rich Output:** 25+ insight categories (IDEAS, QUOTES, HABITS, etc.)
- **SOTA Transcription:** faster-whisper with UV dependency management
- **Smart Detection:** Automatic URL vs text vs file detection

### Usage
```bash
# YouTube video analysis
/wisdom https://youtube.com/watch?v=abc123

# Text file processing  
/wisdom document.txt
/wisdom /path/to/file.md

# Direct text analysis
/wisdom [paste your text content here]
```

### Output Structure
- **SUMMARY:** 25-word overview with presenter/content
- **IDEAS:** 25-50 insights (exactly 16 words each)
- **INSIGHTS:** 10-20 refined abstractions (exactly 16 words each)
- **QUOTES:** 15-30 best quotes with attribution
- **HABITS:** 15-30 practical habits (exactly 16 words each)
- **FACTS:** 15-30 surprising facts (exactly 16 words each)
- **REFERENCES:** All mentioned tools, books, projects
- **RECOMMENDATIONS:** 15-30 actionable items (exactly 16 words each)
- **ONE-SENTENCE TAKEAWAY:** 15-word essence capture

### Technical Implementation
- **Method 1:** Fast subtitle extraction (preferred)
- **Method 2:** SOTA audio transcription (Whisper fallback)
- **Dependency Management:** UV with inline script headers
- **File Organization:** `yt_transcriptions/` for source, timestamped outputs
- **Cleanup:** Automatic temporary file removal

### Attribution
Based on Daniel Miessler's [extractwisdom pattern](https://github.com/danielmiessler/fabric) from the Fabric framework.

---

## 🚀 Installation

### Quick Setup
```bash
# Copy all commands to Claude Code
cp -r commands/* ~/.claude/commands/

# Verify installation
ls ~/.claude/commands/
```

### Individual Command Installation
```bash
# Install specific command
cp commands/wisdom_extraction/wisdom.md ~/.claude/commands/
```

## 📖 Usage Guidelines

### Best Practices
1. **Context Priming:** Use `/prime` when starting new sessions
2. **Documentation First:** Reference `/ai_docs` for established patterns
3. **Iterative Development:** Leverage `/infinite` for complex problems
4. **Knowledge Capture:** Use `/populate_docs` to document discoveries
5. **Content Analysis:** Process learning materials with `/wisdom`

### Workflow Examples

**New Project Setup:**
```bash
/prime                              # Load project context
/ai_docs React TypeScript setup    # Get best practices
/infinite Create project structure # Iterate on architecture
```

**Learning & Documentation:**
```bash
/wisdom https://youtube.com/watch?v=tech-talk    # Extract insights
/populate_docs Implementation Learnings         # Document discoveries
```

## 🔧 Dependencies

### Required Tools
- **Claude Code:** Latest version
- **UV:** Python package manager (for wisdom extraction)
- **Git:** For prime command functionality
- **yt-dlp:** YouTube processing (auto-installed via UV)

### Optional Dependencies
- **faster-whisper:** SOTA transcription (auto-installed when needed)

## 🤝 Contributing

### Adding New Commands
1. Create command directory: `commands/new_command/`
2. Add command file: `new_command.md`
3. Create documentation: `README.md`
4. Update this global README
5. Test thoroughly with various inputs

### Command Template
See `ai_docs/commands_readme_template.md` for the standard structure.

---

**Built for the Claude Code community to accelerate AI-assisted development** 🚀