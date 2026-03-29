# Gemini Instructions for MkDocs & Terraform Learning

This file provides foundational mandates for any AI agent interacting with the `MkDocs` repository. These instructions ensure consistency in documentation formatting, guided learning structure, and navigation management.

## 🏗 Documentation Standards

### 1. Terraform Interview Questions
- **Format:** Always use MkDocs Material **interactive admonitions** (`??? question "Question Text"`) for interview questions.
- **Answers:** Provide clear, concise answers within the admonition.
- **Metadata:** Use `!!! tip`, `!!! info`, or `!!! warning` for supplemental insights (e.g., "Senior Tip", "Production Risk").

### 2. Guided Learning / Lab Exercises
- **Structure:** Use **MkDocs Tabs** (`=== "Exercise X"`) to separate different lab tasks.
- **Content:** Within each tab, include a **Question** section and a **Solution** section (separated by `---" or a bold header).
- **Code Blocks:** Always specify the language (e.g., `hcl`, `bash`, `yaml`) for proper syntax highlighting.

### 3. Navigation Management
- **`mkdocs.yml` Updates:** Whenever a new documentation file is created or renamed, the `nav` section in `mkdocs.yml` **must** be updated immediately to ensure the file is reachable in the generated site.
- **Hierarchy:** Maintain the existing folder-based hierarchy (e.g., `Terraform/", `Kubernetes/", `AWS/").

## 🛠 Terraform Learning Workflow

When helping with Terraform learning:
1. **Research:** Look for existing questions in `docs/Terraform/" or `docs/questions/".
2. **Implementation:** If adding new labs, follow the tabbed exercise format.
3. **Verification:** Ensure that code examples follow best practices (e.g., using `for_each` over `count` for dynamic resources, using remote backends with locking).

## 🔐 Environment & Security
- Follow the global preference for `direnv` and `.envrc`.
- Never store plaintext secrets. Fetch them from macOS Keychain or GitHub CLI.
- Ensure Terraform state files are stored in remote backends (S3 + DynamoDB) with encryption and versioning enabled.
