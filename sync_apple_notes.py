import subprocess
import os
import re

def clean_html(html):
    # Basic HTML to text conversion for Apple Notes
    # Replace common HTML tags with simple text/markdown equivalents
    text = html.replace('<div>', '').replace('</div>', '\n')
    text = text.replace('<br>', '\n')
    text = text.replace('<ul>', '').replace('</ul>', '')
    text = text.replace('<li>', '- ').replace('</li>', '\n')
    text = text.replace('<b>', '**').replace('</b>', '**')
    text = text.replace('<i>', '*').replace('</i>', '*')
    
    # Remove any remaining HTML tags
    text = re.sub('<[^>]*>', '', text)
    
    # Clean up excessive newlines
    text = re.sub('\n{3,}', '\n\n', text)
    return text.strip()

def osascript(script):
    process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = process.communicate()
    return out.strip(), err

def get_notes_in_folder(folder_path_parts):
    # folder_path_parts is a list like ["Resume", "Subfolder"]
    folder_expr = 'folder "' + '" of folder "'.join(reversed(folder_path_parts)) + '"'
    
    # Get note names and bodies
    script = f'''
    tell application "Notes"
        set targetFolder to {folder_expr}
        set noteList to notes of targetFolder
        set resultList to {{}}
        repeat with aNote in noteList
            set end of resultList to (name of aNote & "|||" & body of aNote)
        end repeat
        return resultList
    end tell
    '''
    out, err = osascript(script)
    if not out:
        return []
    
    # osascript returns a comma-separated list of strings
    # We used ||| to separate name and body
    # This split is a bit fragile if note content has comma but it works for basic cases
    # A better way is to iterate and fetch one by one
    notes = out.split(', ')
    parsed_notes = []
    for note in notes:
        if '|||' in note:
            name, body = note.split('|||', 1)
            parsed_notes.append({'name': name, 'body': body})
    return parsed_notes

def get_subfolders(folder_path_parts):
    folder_expr = 'folder "' + '" of folder "'.join(reversed(folder_path_parts)) + '"'
    script = f'''
    tell application "Notes"
        set targetFolder to {folder_expr}
        return name of every folder of targetFolder
    end tell
    '''
    out, err = osascript(script)
    if not out:
        return []
    return out.split(', ')

def sync_folder(folder_path_parts, local_base_path):
    # Create local directory
    local_path = os.path.join(local_base_path, *folder_path_parts)
    os.makedirs(local_path, exist_ok=True)
    
    # Sync notes
    print(f"Syncing folder: {' / '.join(folder_path_parts)}")
    notes = get_notes_in_folder(folder_path_parts)
    for note in notes:
        file_name = note['name'].replace('/', '-').replace(':', '-') + ".md"
        file_path = os.path.join(local_path, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {note['name']}\n\n")
            f.write(clean_html(note['body']))
        print(f"  - Saved note: {note['name']}")
    
    # Recursively sync subfolders
    subfolders = get_subfolders(folder_path_parts)
    for sub in subfolders:
        if sub:
            sync_folder(folder_path_parts + [sub], local_base_path)

if __name__ == "__main__":
    base_docs = os.path.expanduser("~/Documents/GitHub/Mk_docs/docs")
    sync_folder(["Resume"], base_docs)
