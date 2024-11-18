# SQLite Installation Guide

SQLite is a lightweight, serverless, and self-contained SQL database engine that is easy to use and requires minimal setup. This guide will walk you through the installation process of SQLite on various platforms and how to get started using SQLite in your projects.

## Table of Contents
- [Installing SQLite on Linux](#installing-sqlite-on-linux)
- [Installing SQLite on macOS](#installing-sqlite-on-macos)
- [Installing SQLite on Windows](#installing-sqlite-on-windows)
- [Verifying SQLite Installation](#verifying-sqlite-installation)
- [Basic SQLite Commands](#basic-sqlite-commands)

---

## Installing SQLite on Linux

To install SQLite on a Linux-based system (Debian/Ubuntu), use the following commands:

1. Open your terminal.
2. Update your package list:
    ```bash
    sudo apt-get update
    ```

3. Install SQLite:
    ```bash
    sudo apt-get install sqlite3
    ```

4. Optionally, you can install the `sqlite3` command-line shell to interact with SQLite databases:
    ```bash
    sudo apt-get install sqlite3 libsqlite3-dev
    ```
---

## Installing SQLite on macOS

On macOS, the easiest way to install SQLite is through **Homebrew**:

1. Open your terminal.

2. If you don’t have **Homebrew** installed, install it by running:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. Once Homebrew is installed, run the following command to install SQLite:
    ```bash
    brew install sqlite
    ```
---

## Installing SQLite on Windows

To install SQLite on Windows:

1. Download the **SQLite precompiled binaries** from the official SQLite website:
   - Go to the SQLite download page: [SQLite Download Page](https://www.sqlite.org/download.html)
   - Under the **"Precompiled Binaries for Windows"** section, download the `sqlite-tools-win32-x86-*.zip` file.

2. Extract the ZIP file to a folder on your system.

3. Add the folder containing `sqlite3.exe` to your system’s PATH environment variable.

4. You can now run `sqlite3` from your command prompt or terminal.

---

## Verifying SQLite Installation

To verify that SQLite is installed correctly, open a terminal or command prompt and run:

```bash
sqlite3 --version
