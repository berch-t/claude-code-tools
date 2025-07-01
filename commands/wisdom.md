I need to extract wisdom from the following content using Daniel Miessler's extractwisdom pattern: $ARGUMENTS

I will analyze the input (text, file, or YouTube URL) and extract valuable insights following these specific requirements:

**Step 1: Input Processing & Detection**
- If $ARGUMENTS contains a YouTube URL (youtube.com, youtu.be, m.youtube.com), I'll process it through the YouTube transcription pipeline
- If $ARGUMENTS contains a file path ending in .md or .txt, I'll read that file
- If $ARGUMENTS contains direct text content, I'll process it immediately
- If $ARGUMENTS contains just a filename without path, I'll search the current directory

**YouTube Processing Pipeline (when URL detected):**

I'll use a streamlined approach with `uv` for dependency management and optimized subtitle extraction for faster processing.

**Method 1: Fast Subtitle Extraction (Preferred)**
```bash
# Extract auto-generated subtitles directly (fastest method)
uv run --with yt-dlp yt-dlp --write-auto-sub --sub-lang en --skip-download --output "%(title)s.%(ext)s" "$YOUTUBE_URL"
```

**Method 2: SOTA Audio Transcription (When subtitles unavailable)**
```python
#!/usr/bin/env python3
# /// script
# dependencies = ["yt-dlp", "faster-whisper"]
# ///

import yt_dlp
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, parse_qs

def is_youtube_url(url):
    """Detect if input is a YouTube URL"""
    youtube_patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+',
        r'(?:https?://)?(?:www\.)?youtu\.be/[\w-]+',
        r'(?:https?://)?(?:m\.)?youtube\.com/watch\?v=[\w-]+',
        r'(?:https?://)?youtube\.com/embed/[\w-]+',
        r'(?:https?://)?youtube\.com/v/[\w-]+'
    ]
    return any(re.match(pattern, url.strip()) for pattern in youtube_patterns)

def extract_video_id(url):
    """Extract YouTube video ID from various URL formats"""
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[-1].split('?')[0]
    elif 'youtube.com/watch?v=' in url:
        return parse_qs(urlparse(url).query)['v'][0]
    elif 'youtube.com/embed/' in url:
        return url.split('youtube.com/embed/')[-1].split('?')[0]
    return None

def process_youtube_efficiently(youtube_url):
    """Efficient YouTube processing with subtitle extraction first"""
    print(f"🎥 Processing YouTube URL: {youtube_url}")
    
    # Create yt_transcriptions directory
    transcription_dir = Path("yt_transcriptions")
    transcription_dir.mkdir(exist_ok=True)
    
    # Try subtitle extraction first (much faster)
    try:
        print("📋 Attempting subtitle extraction...")
        ydl_opts_subs = {
            'writeautomaticsub': True,
            'writesubtitles': True,
            'subtitleslangs': ['en'],
            'skip_download': True,
            'outtmpl': '%(title)s.%(ext)s'
        }
        
        with yt_dlp.YoutubeDL(ydl_opts_subs) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            video_title = info.get('title', 'Unknown_Video')
            video_id = info.get('id', extract_video_id(youtube_url))
            duration = info.get('duration', 0)
            uploader = info.get('uploader', 'Unknown')
            
            print(f"📺 Title: {video_title}")
            print(f"⏱️  Duration: {duration//3600}h {(duration%3600)//60}m {duration%60}s")
            
            # Download subtitles
            ydl.download([youtube_url])
        
        # Find and process VTT file
        vtt_files = list(Path('.').glob('*.en.vtt'))
        if vtt_files:
            vtt_file = vtt_files[0]
            print(f"✅ Subtitles found: {vtt_file}")
            
            # Convert VTT to clean text
            with open(vtt_file, 'r', encoding='utf-8') as f:
                vtt_content = f.read()
            
            # Parse VTT and extract text
            lines = vtt_content.split('\n')
            text_lines = []
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('WEBVTT') and not re.match(r'^\d+$', line) and not '-->' in line:
                    # Clean up HTML tags and formatting
                    clean_line = re.sub(r'<[^>]+>', '', line)
                    clean_line = re.sub(r'&[a-zA-Z]+;', '', clean_line)
                    clean_line = clean_line.strip()
                    
                    if clean_line and clean_line not in text_lines:
                        text_lines.append(clean_line)
            
            transcription_text = ' '.join(text_lines)
            word_count = len(transcription_text.split())
            
            # Save transcription
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_title = re.sub(r'[^\w\s-]', '', video_title).strip()[:40]
            safe_title = re.sub(r'\s+', '_', safe_title)
            
            transcription_filename = transcription_dir / f"{safe_title}_{video_id}_{timestamp}.txt"
            
            with open(transcription_filename, 'w', encoding='utf-8') as f:
                f.write("# YouTube Video Transcription\n\n")
                f.write("## Video Metadata\n")
                f.write(f"**Title:** {video_title}\n")
                f.write(f"**Video ID:** {video_id}\n")
                f.write(f"**URL:** {youtube_url}\n")
                f.write(f"**Uploader:** {uploader}\n")
                f.write(f"**Duration:** {duration//3600}h {(duration%3600)//60}m {duration%60}s\n")
                f.write(f"**Transcribed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("**Language:** English\n")
                f.write(f"**Word Count:** {word_count}\n")
                f.write("**Source:** YouTube Auto-Generated Subtitles\n\n")
                f.write("---\n\n")
                f.write("## Transcription\n\n")
                f.write(transcription_text)
            
            # Cleanup VTT file
            vtt_file.unlink()
            
            print(f"💾 Transcription saved: {transcription_filename}")
            print(f"📊 Extracted {word_count} words from subtitles")
            
            return transcription_text, str(transcription_filename), {
                'title': video_title,
                'video_id': video_id,
                'duration': duration,
                'uploader': uploader,
                'word_count': word_count
            }
            
    except Exception as e:
        print(f"⚠️  Subtitle extraction failed: {e}")
        print("🎵 Falling back to audio transcription...")
        
        # Fallback to audio transcription (only if needed)
        from faster_whisper import WhisperModel
        
        # Configure yt-dlp for audio download
        ydl_opts_audio = {
            'format': 'bestaudio[ext=m4a]/bestaudio/best',
            'outtmpl': 'temp_youtube_audio.%(ext)s',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
            ydl.download([youtube_url])
        
        # Find audio file
        audio_files = list(Path('.').glob('temp_youtube_audio.*'))
        if not audio_files:
            raise Exception("Audio download failed")
        
        audio_file = audio_files[0]
        print(f"✅ Audio downloaded: {audio_file}")
        
        # Transcribe with Whisper
        print("🤖 Loading Whisper model...")
        model = WhisperModel("base", device="cpu", compute_type="int8")  # Use base for speed
        
        print("🎙️  Transcribing audio...")
        segments, info = model.transcribe(str(audio_file), language="en")
        
        transcription_text = ""
        for segment in segments:
            transcription_text += f"{segment.text.strip()}\n"
        
        word_count = len(transcription_text.split())
        
        # Save and cleanup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_title = re.sub(r'[^\w\s-]', '', video_title).strip()[:40]
        safe_title = re.sub(r'\s+', '_', safe_title)
        
        transcription_filename = transcription_dir / f"{safe_title}_{video_id}_{timestamp}.txt"
        
        with open(transcription_filename, 'w', encoding='utf-8') as f:
            f.write("# YouTube Video Transcription\n\n")
            f.write("## Video Metadata\n")
            f.write(f"**Title:** {video_title}\n")
            f.write(f"**Video ID:** {video_id}\n")
            f.write(f"**URL:** {youtube_url}\n")
            f.write(f"**Uploader:** {uploader}\n")
            f.write(f"**Duration:** {duration//3600}h {(duration%3600)//60}m {duration%60}s\n")
            f.write(f"**Transcribed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("**Language:** English\n")
            f.write(f"**Word Count:** {word_count}\n")
            f.write("**Model:** Whisper base (faster-whisper)\n\n")
            f.write("---\n\n")
            f.write("## Transcription\n\n")
            f.write(transcription_text)
        
        # Cleanup audio file
        audio_file.unlink()
        
        print(f"💾 Transcription saved: {transcription_filename}")
        
        return transcription_text, str(transcription_filename), {
            'title': video_title,
            'video_id': video_id,
            'duration': duration,
            'uploader': uploader,
            'word_count': word_count
        }

# Main processing logic
input_text = "$ARGUMENTS".strip()

if is_youtube_url(input_text):
    print("🔍 YouTube URL detected - initiating efficient transcription...")
    transcription_text, transcription_file, metadata = process_youtube_efficiently(input_text)
    
    content_to_process = transcription_text
    content_source = f"YouTube: {metadata['title']}"
    
    print("🧠 Proceeding to wisdom extraction...")
else:
    # Original text/file processing logic
    if input_text.endswith(('.md', '.txt')) and Path(input_text).exists():
        with open(input_text, 'r', encoding='utf-8') as f:
            content_to_process = f.read()
        content_source = f"File: {input_text}"
    else:
        content_to_process = input_text
        content_source = "Direct Input"
```

**Step 2: Wisdom Extraction**
I will extract the following sections with exact formatting requirements:

- **SUMMARY**: 25-word summary including presenter and content
- **IDEAS**: 25-50 most surprising/insightful ideas (exactly 16 words each)
- **INSIGHTS**: 10-20 refined, abstracted insights (exactly 16 words each)  
- **QUOTES**: 15-30 best quotes with exact text and speaker attribution
- **HABITS**: 15-30 practical personal habits mentioned (exactly 16 words each)
- **FACTS**: 15-30 surprising facts about the world (exactly 16 words each)
- **REFERENCES**: All mentioned writing, art, tools, projects, and inspiration sources
- **ONE-SENTENCE TAKEAWAY**: 15-word sentence capturing the essence
- **RECOMMENDATIONS**: 15-30 actionable recommendations (exactly 16 words each)

**Step 3: Output Generation**
I will create a comprehensive markdown file with intelligent naming:

For YouTube content: `{video_title}_{video_id}_{timestamp}_extracted_wisdom.md`
For other content: `truncated-query_$(date +%Y%m%d_%H%M%S)_extracted_wisdom.md`

The output will be richly formatted with:
- Professional markdown structure with source metadata
- Bullet points (not numbered lists)
- No repeated content across sections
- Varied opening words for each bullet
- Complete extraction of all valuable content
- Link back to original transcription file (if from YouTube)

**Step 4: File Creation & Cleanup**
- Transcription saved in `yt_transcriptions/` folder (if YouTube)
- Wisdom extraction saved in current directory
- Temporary files automatically cleaned up
- Full metadata preserved in both files

**Key Improvements with uv:**
- No virtual environment creation needed
- Faster dependency resolution
- Automatic script execution with inline dependencies
- Cleaner, more maintainable workflow
- Fallback subtitle extraction for speed

Let me begin the processing pipeline...