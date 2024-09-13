---
title: Introduction to Linux
author: OSDG
date: September 2024
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

# Basic Linux Commands

- **`ls`:** Lists the contents of a directory.
- **`cd`:** Changes the current working directory.
- **`echo`:** Displays a line of text or variable value to the terminal.
- **`cat`:** Concatenates and displays the content of files.

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

---

# grep

---

# sed

---

# Aftab sir
- vi
- bare metal linux install
- some regex examples you want us to cover  (email, phone number)
- more advanced bash scripting (variables etc)
- do they know programming and how much