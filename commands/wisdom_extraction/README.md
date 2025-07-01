# Wisdom Extraction 🧠

Extract valuable insights, quotes, habits, and recommendations from YouTube videos or text content using Daniel Miessler's proven extractwisdom pattern.

## 🎯 Overview

The Wisdom Extraction command transforms any text content or YouTube video into structured, actionable insights. Based on Daniel Miessler's [extractwisdom pattern](https://github.com/danielmiessler/fabric) from the Fabric framework, this tool helps you capture and organize the most valuable information from learning materials.

## ✨ Features

### 📺 **YouTube Processing**
- **Auto-Subtitle Extraction** - Fast processing using YouTube's auto-generated captions
- **SOTA Audio Transcription** - Whisper large-v3 fallback for maximum accuracy
- **Smart Detection** - Automatic URL format recognition
- **Metadata Capture** - Video title, duration, uploader, timestamps

### 📄 **Text Processing**
- **File Support** - Direct processing of `.md` and `.txt` files
- **Paste Support** - Analyze any text content directly
- **Path Detection** - Automatic file vs text vs URL recognition

### 🎨 **Rich Output**
- **25+ Insight Categories** - Comprehensive analysis framework
- **Exact Word Counts** - Precisely formatted bullet points
- **Professional Markdown** - Publication-ready documentation
- **Timestamped Files** - Organized output with metadata

## 🚀 Installation

### Prerequisites
- **Claude Code** - Latest version with command support
- **UV** - Python package manager (for YouTube processing)

### Setup
```bash
# Copy command to Claude Code directory
cp wisdom.md ~/.claude/commands/

# Verify installation
ls ~/.claude/commands/wisdom.md
```

Dependencies are automatically managed via UV when processing YouTube content.

## 📖 Usage

### Basic Syntax
```bash
/wisdom [content]
```

### YouTube Videos
```bash
# Standard YouTube URLs
/wisdom https://youtube.com/watch?v=abc123

# Short URLs  
/wisdom https://youtu.be/abc123

# Mobile URLs
/wisdom https://m.youtube.com/watch?v=abc123

# Embed URLs
/wisdom https://youtube.com/embed/abc123
```

### Text Files
```bash
# Local files
/wisdom document.txt
/wisdom /path/to/file.md

# Files in current directory
/wisdom notes.txt
```

### Direct Text
```bash
# Paste content directly
/wisdom [paste your text content here]
```

## 📊 Output Structure

### Generated Files
- **Transcription:** `yt_transcriptions/Video_Title_VideoID_Timestamp.txt` (YouTube only)
- **Wisdom Analysis:** `Video_Title_VideoID_Timestamp_extracted_wisdom.md`

### Content Sections

| Section | Count | Format | Purpose |
|---------|-------|--------|---------|
| **SUMMARY** | 1 | 25 words | Overview with presenter/content |
| **IDEAS** | 25-50 | 16 words each | Most surprising/insightful concepts |
| **INSIGHTS** | 10-20 | 16 words each | Refined, abstracted wisdom |
| **QUOTES** | 15-30 | Exact text | Best quotes with attribution |
| **HABITS** | 15-30 | 16 words each | Practical personal habits |
| **FACTS** | 15-30 | 16 words each | Surprising world facts |
| **REFERENCES** | Variable | List | Tools, books, projects mentioned |
| **TAKEAWAY** | 1 | 15 words | Core essence sentence |
| **RECOMMENDATIONS** | 15-30 | 16 words each | Actionable advice |

## 🔧 Technical Implementation

### YouTube Processing Pipeline

**Method 1: Fast Subtitle Extraction (Preferred)**
```bash
uv run --with yt-dlp yt-dlp --write-auto-sub --sub-lang en --skip-download
```

**Method 2: SOTA Audio Transcription (Fallback)**
```python
# /// script
# dependencies = ["yt-dlp", "faster-whisper"]
# ///
```

### Key Technologies
- **yt-dlp** - Reliable YouTube content extraction
- **faster-whisper** - Optimized Whisper implementation (4x faster)
- **UV** - Modern Python dependency management
- **VTT Processing** - Clean subtitle text extraction

### Performance Optimizations
- **Subtitle-first approach** - Seconds vs minutes processing
- **Automatic cleanup** - Temporary file management
- **Error handling** - Graceful fallbacks
- **Memory efficient** - No persistent environments

## 📋 Examples

### Example 1: Tech Talk Analysis
```bash
/wisdom https://youtube.com/watch?v=tech-conference-talk
```

**Output:** `Tech_Conference_Talk_abc123_20250701_120000_extracted_wisdom.md`

### Example 2: Documentation Processing
```bash
/wisdom project-readme.md
```

**Output:** `project-readme_20250701_120000_extracted_wisdom.md`

### Example 3: Direct Text Analysis
```bash
/wisdom "In this article, we explore the future of AI development and its impact on software engineering practices..."
```

**Output:** `direct-input_20250701_120000_extracted_wisdom.md`

## 🎯 Use Cases

### 📚 **Learning & Development**
- Conference talk analysis
- Technical documentation synthesis
- Educational video processing
- Research paper insights

### 🏢 **Business & Strategy**
- Meeting transcript analysis
- Industry report processing
- Thought leadership content
- Competitive intelligence

### 📝 **Content Creation**
- Source material research
- Quote compilation
- Reference gathering
- Insight documentation

### 🧠 **Knowledge Management**
- Personal learning logs
- Team knowledge sharing
- Best practices capture
- Wisdom libraries

## 🔍 Attribution & Inspiration

This tool is directly inspired by and implements Daniel Miessler's **extractwisdom** pattern from the [Fabric](https://github.com/danielmiessler/fabric) framework.

### Original Fabric Pattern
- **Creator:** Daniel Miessler ([@DanielMiessler](https://github.com/danielmiessler))
- **Project:** [Fabric - AI Augmentation Framework](https://github.com/danielmiessler/fabric)
- **Pattern:** [extractwisdom](https://github.com/danielmiessler/fabric/tree/main/patterns/extract_wisdom)
- **Purpose:** "Extract wisdom from any text content"

### Our Implementation
- **Platform:** Claude Code command integration
- **Enhancement:** YouTube video processing pipeline
- **Technology:** UV dependency management + SOTA transcription
- **Output:** Enhanced markdown formatting with metadata

**Massive thanks to Daniel Miessler for creating this incredibly valuable pattern that addresses the problem of "too much content and too little time." 🙏**

## 🚨 Troubleshooting

### Common Issues

**YouTube URL not recognized:**
```bash
# Ensure proper URL format
✅ https://youtube.com/watch?v=abc123
❌ youtube.com/watch?v=abc123  (missing protocol)
```

**UV not installed:**
```bash
# Install UV package manager
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**No subtitles available:**
- Tool automatically falls back to Whisper transcription
- Processing time increases from seconds to minutes
- Quality remains high with large-v3 model

**File not found:**
```bash
# Use absolute paths for files outside current directory
/wisdom /full/path/to/document.txt
```

### Performance Tips

1. **Use subtitle extraction** - Much faster than audio transcription
2. **Shorter videos** - Under 60 minutes process most efficiently  
3. **Clear audio** - Better transcription quality
4. **English content** - Optimized for English language processing

## 🤝 Contributing

### Improvements Welcome
- Additional video platforms support
- More output formats
- Enhanced error handling
- Performance optimizations

### Development Setup
```bash
# Clone repository
git clone https://github.com/berch-t/claude-code-tools.git

# Navigate to command
cd claude-code-tools/commands/wisdom_extraction/

# Test with sample content
/wisdom "Sample text for testing extraction patterns..."
```

---

**Transform any content into actionable wisdom with proven patterns** 🧠⚡

*Powered by Daniel Miessler's extractwisdom pattern from Fabric*