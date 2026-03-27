# direnv

[direnv](https://direnv.net/) is an extension for your shell. It augments existing shells with a new feature that can load and unload environment variables depending on the current directory.

## Key Features

*   **Automatic Environment Management:** Loads environment variables when you enter a directory containing a `.envrc` file and unloads them when you leave.
*   **Shell Agnostic:** Supports hooks for all common shells (bash, zsh, fish, etc.).
*   **Language Agnostic:** Works for any programming language.
*   **Security:** Prevents loading `.envrc` files until explicitly authorized.
*   **Standard Library (stdlib):** Provides utility functions like `PATH_add` to simplify common tasks.

## Installation on macOS

Standard method for macOS is via **Homebrew**:

1.  **Install via Homebrew:**
    ```bash
    brew install direnv
    ```
2.  **Hook into your shell:** Add the hook to your shell configuration file (e.g., `~/.zshrc`).
    ```bash
    # For Zsh, add to ~/.zshrc
    eval "$(direnv hook zsh)"
    ```
3.  **Restart your shell** or source your config file.

## Basic Usage

1.  **Create a `.envrc` file:**
    ```bash
    echo "export FOO=bar" > .envrc
    ```
2.  **Authorize the file:**
    ```bash
    direnv allow .
    ```
3.  **Verify:** The variable `FOO` is now available. If you `cd ..` out of the directory, the variable will be automatically unset.
