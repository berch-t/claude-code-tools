#!/usr/bin/env python3
"""
Plans System Manager

This module provides functionality to automatically save validated plans
from Claude Code's plan mode into organized markdown files.

This is a standalone version that can be used independently or as part of the MCP server.
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class PlanManager:
    def __init__(self, plans_dir: str = None):
        """Initialize the plan manager with the Plans directory."""
        if plans_dir is None:
            # Default to ~/.claude/Plans for compatibility
            plans_dir = os.path.join(os.path.expanduser("~"), ".claude", "Plans")
        
        self.plans_dir = Path(plans_dir)
        self.projects_dir = self.plans_dir / "projects"
        self.templates_dir = self.plans_dir / "templates"
        self.index_file = self.plans_dir / "index.md"
        
        # Ensure directories exist
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Ensure all required directories exist."""
        self.plans_dir.mkdir(exist_ok=True)
        self.projects_dir.mkdir(exist_ok=True)
        self.templates_dir.mkdir(exist_ok=True)
        
        # Create initial index if it doesn't exist
        if not self.index_file.exists():
            self._create_initial_index()
    
    def _create_initial_index(self):
        """Create the initial index.md file."""
        initial_content = """# Plans Index

This is the master index of all validated project plans stored in the Plans system.

## Overview
The Plans system automatically captures and stores validated project plans created in Claude Code's plan mode. Each plan is saved as a markdown file with metadata and structured content.

## Recent Plans
*No plans have been saved yet.*

## Projects
*No projects have been created yet.*

## Usage
When you exit plan mode in Claude Code, your validated plan will be automatically saved to the appropriate project folder and indexed here.

## File Structure
```
Plans/
├── index.md (this file)
├── templates/
│   └── plan-template.md
└── projects/
    └── [project folders will be created automatically]
```

---
*Last updated: {date}*
*Total plans: 0*""".format(date=datetime.now().strftime("%Y-%m-%d"))
        
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(initial_content)
    
    def _sanitize_project_name(self, name: str) -> str:
        """Sanitize project name for use as folder name."""
        # Replace spaces and special characters with hyphens
        sanitized = re.sub(r'[^\w\s-]', '', name)
        sanitized = re.sub(r'[-\s]+', '-', sanitized)
        return sanitized.lower().strip('-')
    
    def _extract_project_name_from_plan(self, plan_content: str) -> str:
        """Extract project name from plan content."""
        # Look for common patterns in plan titles
        lines = plan_content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# ') and 'plan' in line.lower():
                # Extract project name from title like "# Project Name Plan"
                title = line[2:].replace(' Plan', '').replace(' Implementation', '').strip()
                return self._sanitize_project_name(title)
            elif line.startswith('## ') and any(word in line.lower() for word in ['overview', 'summary']):
                # Sometimes project name might be in overview section
                continue
        
        # Fallback: use timestamp if no clear project name found
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"project_{timestamp}"
    
    def _create_project_folder(self, project_name: str) -> Path:
        """Create project folder if it doesn't exist."""
        project_path = self.projects_dir / project_name
        project_path.mkdir(exist_ok=True)
        return project_path
    
    def _generate_filename(self, project_name: str) -> str:
        """Generate filename for the plan."""
        timestamp = datetime.now().strftime("%Y-%m-%d")
        return f"{timestamp}_plan.md"
    
    def _create_plan_metadata(self, project_name: str, plan_content: str) -> str:
        """Create frontmatter metadata for the plan."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Extract tags from plan content (basic implementation)
        tags = []
        content_lower = plan_content.lower()
        if 'web' in content_lower or 'website' in content_lower:
            tags.append('web')
        if 'api' in content_lower:
            tags.append('api')
        if 'database' in content_lower:
            tags.append('database')
        if 'ai' in content_lower or 'machine learning' in content_lower:
            tags.append('ai')
        if 'react' in content_lower:
            tags.append('react')
        if 'python' in content_lower:
            tags.append('python')
        if 'typescript' in content_lower or 'javascript' in content_lower:
            tags.append('javascript')
        
        metadata = f"""---
project_name: "{project_name}"
date: "{current_date}"
status: "validated"
tags: {tags}
version: "1.0"
auto_generated: true
---

"""
        return metadata
    
    def save_plan_as_md(self, plan_content: str, project_name: str = None) -> Path:
        """
        Save a validated plan as a markdown file.
        
        Args:
            plan_content: The plan content from exit_plan_mode
            project_name: Optional project name override
            
        Returns:
            Path to the saved plan file
        """
        # Extract project name if not provided
        if project_name is None:
            project_name = self._extract_project_name_from_plan(plan_content)
        else:
            project_name = self._sanitize_project_name(project_name)
        
        # Create project folder
        project_path = self._create_project_folder(project_name)
        
        # Generate filename
        filename = self._generate_filename(project_name)
        plan_file_path = project_path / filename
        
        # Create metadata
        metadata = self._create_plan_metadata(project_name, plan_content)
        
        # Combine metadata and content
        full_content = metadata + plan_content
        
        # Save the file
        with open(plan_file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        # Update index
        self._update_index(project_name, filename, plan_file_path)
        
        return plan_file_path
    
    def _update_index(self, project_name: str, filename: str, file_path: Path):
        """Update the master index with the new plan."""
        # Read current index
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = ""
        
        # Extract current stats
        total_plans = len(list(self.projects_dir.rglob("*.md")))
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Create new entry
        relative_path = file_path.relative_to(self.plans_dir)
        new_entry = f"- [{project_name}]({relative_path}) - {filename.replace('_plan.md', '')} - {current_date}"
        
        # Update recent plans section
        if "*No plans have been saved yet.*" in content:
            content = content.replace("*No plans have been saved yet.*", new_entry)
        else:
            # Add to recent plans (keep last 10)
            recent_section_start = content.find("## Recent Plans")
            if recent_section_start != -1:
                projects_section_start = content.find("## Projects", recent_section_start)
                if projects_section_start != -1:
                    recent_content = content[recent_section_start:projects_section_start].strip()
                    entries = [line for line in recent_content.split('\n') if line.strip().startswith('- [')]
                    entries.insert(0, new_entry)
                    entries = entries[:10]  # Keep only last 10
                    
                    new_recent_section = "## Recent Plans\n" + '\n'.join(entries) + "\n\n"
                    content = content[:recent_section_start] + new_recent_section + content[projects_section_start:]
        
        # Update projects section
        projects = set()
        for plan_file in self.projects_dir.rglob("*.md"):
            project_folder = plan_file.parent.name
            projects.add(project_folder)
        
        projects_list = "\n".join([f"- {project}" for project in sorted(projects)])
        if "*No projects have been created yet.*" in content:
            content = content.replace("*No projects have been created yet.*", projects_list)
        else:
            # Update projects list
            projects_start = content.find("## Projects")
            if projects_start != -1:
                usage_start = content.find("## Usage", projects_start)
                if usage_start != -1:
                    content = content[:projects_start] + f"## Projects\n{projects_list}\n\n" + content[usage_start:]
        
        # Update footer stats
        content = re.sub(r'\*Last updated: \d{4}-\d{2}-\d{2}\*', f'*Last updated: {current_date}*', content)
        content = re.sub(r'\*Total plans: \d+\*', f'*Total plans: {total_plans}*', content)
        
        # Save updated index
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def list_plans(self) -> List[Dict]:
        """List all saved plans."""
        plans = []
        for plan_file in self.projects_dir.rglob("*.md"):
            project_name = plan_file.parent.name
            plans.append({
                'project': project_name,
                'filename': plan_file.name,
                'path': plan_file,
                'date': plan_file.stat().st_mtime
            })
        
        return sorted(plans, key=lambda x: x['date'], reverse=True)
    
    def get_plan_content(self, project_name: str, filename: str = None) -> Optional[str]:
        """Get the content of a specific plan."""
        project_path = self.projects_dir / project_name
        
        if filename:
            plan_file = project_path / filename
        else:
            # Get the most recent plan file
            plan_files = list(project_path.glob("*.md"))
            if not plan_files:
                return None
            plan_file = max(plan_files, key=lambda x: x.stat().st_mtime)
        
        if plan_file.exists():
            with open(plan_file, 'r', encoding='utf-8') as f:
                return f.read()
        
        return None


def save_plan_as_md(plan_content: str, project_name: str = None) -> str:
    """
    Convenience function to save a plan as markdown.
    This is the main function that should be called when exiting plan mode.
    
    Args:
        plan_content: The plan content from exit_plan_mode
        project_name: Optional project name override
        
    Returns:
        Path to the saved plan file as string
    """
    manager = PlanManager()
    saved_path = manager.save_plan_as_md(plan_content, project_name)
    return str(saved_path)


if __name__ == "__main__":
    # Example usage
    example_plan = """# Example Project Plan

## Overview
This is an example project plan to demonstrate the Plans system.

## Implementation Steps
1. Step one
2. Step two  
3. Step three

## Requirements
- Requirement 1
- Requirement 2
"""
    
    print("Testing plan manager...")
    saved_path = save_plan_as_md(example_plan, "test-project")
    print(f"Plan saved to: {saved_path}")