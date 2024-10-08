---
title: Introduction to Linux
author: OSDG @ IIIT-H
date: 14th September, 2024
---

# Installing WSL on Windows

- Open Windows Terminal.
- Type `wsl --install` and wait for it to run.
- After installation has completed, it will prompt you for a reboot, wait at that point.

---

# About the session

## About Us

- Presenters: Ankith Pai, Praneeth Jain and Abhiram Tilak
- 3rd year students at IIIT-H and members of the Open Source Developers Group (OSDG) student club.

## Agenda

- Install WSL on Windows.
- Learn more about what Linux and related softwares are.
- Cover basic `bash` scripting.
- Introduce Regular Expressions (`regex`).
- Dive into `vi`/`vim` editor.

---

# What is Unix?

- **Unix** is a powerful, multiuser, multitasking operating system.
- Developed in the 1960s and 70s.
- Known for its stability, security, and efficiency.

---

# What is GNU/Linux?

## What is GNU?

- **GNU** stands for "GNU's Not Unix".
- A free software operating system that is Unix-compatible.
- Includes tools and utilities to provide a complete operating environment.

## What is Linux?

- A kernel created by Linus Torvalds in 1991.
- Acts as an intermediary between hardware and user applications.
- Manages hardware resources, system calls, and hardware drivers.
- The term **"Linux"** often refers to the complete system of GNU+Linux

---

# Linux Distros

Linux distributions (distros) are various versions of GNU/Linux, each customized with different software, features, and user interfaces to meet specific needs or preferences.

- **Debian**: A versatile and stable distribution used as the base for many other distros, including Ubuntu.
- **Ubuntu:** User-friendly, suitable for beginners.
- **Linux Mint**: An Ubuntu-based distribution that focuses on providing a familiar and user-friendly desktop experience.
- **Fedora:** Cutting-edge features, community-driven.
- **Arch Linux:** Highly customizable, for advanced users.
- **Manjaro**: A user-friendly derivative of Arch Linux that provides a more accessible experience with pre-configured environments.
- **Alpine Linux**: A lightweight and security-oriented distribution often used in container environments.

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

# Terminal and Shell Basics

A shell is a command interpreter that processes user commands. It provides an interface between the user and the operating system.

## Command

A command is an instruction to the shell, that executes the program given by *name* with 0 or more *arguments*.

## Useful shell tips

- **Cursor Control**: Use `←` and `→` arrow keys to move the cursor within a command.
- **Command History**: Use the `↑` and `↓` arrow keys to scroll through previous commands.
- **Autocompletion**: Press `Tab` to auto-complete.

---

# Installing WSL on Windows (continued)

- Reboot your system.
- A prompt for username and password will be shown
- Enter any username and password (remember them!)

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

# `apt` package manager

**`apt`** is used for package management on Debian-based systems.

## Most commonly used sub-commands

- **Upgrading all packages**: `sudo apt update` and `sudo apt upgrade`
- **Install package**: `sudo apt install {package_names}`
- **Remove package**: `sudo apt remove {package_names}`
- **Search packages**: `apt search {search_term}`
- **Auto-remove unneeded packages**: `sudo apt autoremove`

---

# Accessing Windows Filesystem

`cd /mnt/c`

---

## Additional resources on Scripting

This was a tutorial for one of my courses named ISS, [Here's](https://github.com/abhiramtilakiiit/test-tutorial) the link for it.

This is obviously way more required than what was taught in the session, but there is a document called "Tutorial-1.pdf" which
contains information about everything you might need.

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

## Additional Resources on Regex

Regex is not something you can learn in a single day, and it is common
to forget some of the specifics. Our tutorial was just an introduction,
I would recommend following through a detailed playlist.


- [The Coding Train](https://youtube.com/playlist?list=PLGyavLZl7i6NLY1aWdd-ouJ0wk13cADvQ): This is a good playlist to get started, it contains anywhere from beginner to advanced regex. Also goes over the turing-completeness of regex.

---

## Vi

Vi whose full form stands for 'Visual' is a very basic "screen-based" text editor
originally invented for the Unix Operating system.

### Some Brief History (Source: [wikipedia](https://en.wikipedia.org/wiki/Vi_(text_editor)))

The original code for vi was written by Bill Joy in 1976 as the visual mode for the ex 
line editor that Joy had written with Chuck Haley. Joy's ex 1.1 (popular text editr at time) 
was released as part of the first BSD Unix. 

Vi's success sparked the development of similar which ended up being updated versions of 
Vi called "ViM" and "NeoVim" etc, which is the most widely used text editor in UNIX based
systems at 36% popularity.

---

### How to exit Vi

There are two methods to exit Vi:

- The most common method to exit is to just use the "command mode" and type the command `:q`
- Another common way to exit is to just type `Shift + Z + Q` when in "normal mode".

### Install Vi in Linux

Most Distributions of Linux ship with Vim by default, if not you can always install
it from the main repos.

For instance, in Ubuntu-based distributions:
```
$ sudo apt install vim
```

### ViM Tutor

ViM is not something that can be learn or taught overnight, it requires a lot of 
practice and there are a so many key combinations that even we as daily users tend
to forget. 

Modern ViM comes pre-installed with a "tutor" program which we can launch after installing
vim with command:
```
$ vimtutor
```








