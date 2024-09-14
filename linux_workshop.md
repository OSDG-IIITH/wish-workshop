---
title: Introduction to Linux
author: OSDG @ IIIT-H
date: 14th September, 2024
---

# What is Linux

Linux a family of open-source operating systems.​

## Linux Distros

Linux distributions (distros) are various versions of the Linux operating system, each customized with different software, features, and user interfaces to meet specific needs or preferences.

- **Ubuntu:** User-friendly, suitable for beginners.
- **Fedora:** Cutting-edge features, community-driven.
- **Arch Linux:** Highly customizable, for advanced users.

---

# What is WSL

- **WSL** allows you to run a Linux distro directly on Windows.
- WSL works like a light-weight virtual machine (VM), no need for a dual-boot setup.

## Pros of WSL
- Easy Setup: Simple installation and configuration process.
- Resource Efficiency: Lightweight compared to full virtual machines.

## Cons of WSL
- File System Differences: File system performance and compatibility can vary between Linux and Windows files.
- Not a Full VM: Some Linux-specific functionalities and kernel modules might not work as expected.

---

# Installing WSL

- Open Windows Terminal
- Type `wsl --install`
- After installation has completed, reboot
- A prompt for username and password will be shown
- Enter any username and password (remember them!)

---

# Terminal and Shell Basics

A shell is a command interpreter that processes user commands. It provides an interface between the user and the operating system.

## Command

A command is an instruction to the shell, that executes the program given by *name* with 0 or more *arguments*.

## Useful shell tips

- **Cursor Control**: Use `←` and `→` arrow keys to move the cursor within a command.
- **Command History**: Use the `↑` and `↓` arrow keys to scroll through previous commands.
- **Autocompletion**: Press `Tab` to auto-complete.

---

# Basic Linux Commands

- **`pwd`:** Prints the current working directory's absolute path.
- **`ls`:** Lists the contents of a directory.
- **`cd`:** Changes the current working directory.
- **`echo`:** Displays a line of text or variable value to the terminal.
- **`cat`:** Concatenates and displays the content of files.
- **`mkdir`:** Creates a new directory with the specified name.
- **`cp`:** Copy a file from one path to another.
- **`mv`:** Move a file from one path to another.
- **`rm`:** Remove a file at a given path.
- **`sudo`:** Execute a command as another user, typically root.

---

# Piping and I/O Redirection

- **Output Redirection (`>`):** Redirects command output to a file, creating or overwriting it.
- **Append Redirection (`>>`):** Appends output to the end of a file.
- **Input Redirection (`<`):** Uses a file's content as input for a command.
- **Error Redirection (`2>`):** Redirects error messages to a file.
- **Piping (`|`):** Passes output from one command directly as input to another command.


---

# Accessing Windows Filesystem

`cd /mnt/c`

---

# Basic Regex
Regex, short for Regular Expression, is a powerful tool for pattern matching and text manipulation. It allows you to:

- Search for specific patterns in text
- Validate input formats (e.g., email addresses, phone numbers)
- Extract information from strings
- Replace or modify text based on patterns

---

# Practice Regex
- https://regexr.com/
- https://regexone.com/

# Basic Patterns:
- `.` - Any character
- `^` - Start of line
- `$` - End of line
- `*` - Zero or more occurrences
- `+` - One or more occurrences
- `?` - Zero or one occurrence
- `[abc]` - Any of a, b, or c
- `[^abc]` - Not a, b, or c
- `\d` - Digit
- `\w` - Word character (letter, digit, underscore)
- `\s` - Whitespace

---

# Examples:
- `^hello` - Lines starting with "hello"
- `world$` - Lines ending with "world"
- `a[bcd]+` - "a" followed by one or more b, c, or d
- `\d{3}-\d{3}-\d{4}` - US phone number format

---

# Grep

Grep searches for patterns in files or input.

## Basic Usage:
```
grep [options] pattern [file...]
```

# Common Options:
- `-i`: Case-insensitive search
- `-v`: Invert match (show non-matching lines)
- `-r`: Recursive search in directories
- `-n`: Show line numbers

---

# Examples:
```bash
grep "error" log.txt
grep -i "warning" *.log
grep -r "TODO" .
```
---

# Sed

Sed is a stream editor for filtering and transforming text.

## Basic Usage:
```
sed [options] 'command' [file...]
```

## Common Commands:
- `s/pattern/replacement/`: Substitute
- `d`: Delete line
- `p`: Print line

---

# Examples:
```bash
sed 's/old/new/' file.txt
sed '1,5d' file.txt
```

---

# vi
