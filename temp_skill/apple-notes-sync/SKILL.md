---
name: apple-notes-sync
description: Synchronize Apple Notes to local Markdown documentation. Use when you need to export notes from macOS Notes.app, clean their HTML content, and intelligently categorize them into topical project folders like Kubernetes, Terraform, or Langchain.
---

# Apple Notes Sync Skill

This skill allows you to export content from Apple Notes and integrate it into your local documentation workflow.

## Workflow

### 1. Synchronization
Use the bundled Python script to fetch notes from a specific Apple Notes folder and convert them to Markdown files.

```bash
python3 scripts/sync_apple_notes.py
```
*   **Note:** The script uses AppleScript. Ensure the Terminal/IDE has "Automation" permissions for "Notes.app" in macOS System Settings.

### 2. Intelligent Reorganization
After syncing, analyze the content of the exported `.md` files and move them from the temporary sync directory to their respective domain-specific folders.

**Recommended Mapping:**
- **Infrastructure:** `docs/Terraform/`
- **Orchestration:** `docs/Kubernetes/`
- **AI/LLMs:** `docs/Langchain/` or `docs/AI/`
- **Interview Prep:** `docs/questions/`
- **Career:** `docs/Career/`
- **Scripts:** `docs/shell-script/`

### 3. Navigation Update
Always run the project's navigation generator (e.g., `python3 docs.py`) after moving files to ensure the `mkdocs.yml` sidebar is updated.

## Security & Privacy
- **Credentials:** Apple Notes often contain secrets. Scan exported files for passwords or API keys before committing them to Git.
- **Permissions:** If AppleScript fails, check **System Settings > Privacy & Security > Automation**.
