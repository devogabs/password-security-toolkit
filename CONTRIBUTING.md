# Contributing Guide

Thanks for wanting to contribute with this project !!
This document explains how to run the project localy, coding patterns, commits style and how to send contributions in a organized way.

---

## How to run the project localy ##

1. Fork the repository

2. Clone the fork:
```bash
git clone https://github.com/seu-usuario/password-tool.git
cd password-security-toolkit
```

3. Start a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.\.venv\Scripts\activate    # Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure ##
```bash
src/
 ├── cli.py
 ├── password_checker.py
 ├── password_generator.py
 └── __init__.py
.gitignore
README.md
LICENSE
CONTRIBUTING.md
.github/
 ├── ISSUE_TEMPLATE/
 └── PULL_REQUEST_TEMPLATE.md
```

---

## Commits Style (Conventional Commits) ##
In this repo, we use the following format:
```bash
<type>: short description
```

Most common types:
| Type       | Usage                                        |
| ---------- | -------------------------------------------- |
| `feat`     | new feature                                  |
| `fix`      | bug fix                                      |
| `docs`     | changes in documentation                     |
| `refactor` | code improvements without changing its logic |
| `style`    | format, identation, etc                      |
| `test`     | add or alter tests                           |
| `chore`    | inner tasks, CI, configs                     |


Examples:
```bash
feat: add entropy calculation
fix: correct symbol inclusion in generator
docs: update usage examples in README
```
---

## Branches ##
Always create branches with descriptive names. For example:

* feat/entropy-checker
* fix/cli-argument-bug
* docs/improve-readme

---

## How to open a Pull Request ##
1. Make a commit following the convention.
2. Push it into your branch.
3. Open a Pull Request and select a template.
4. Fill up:
    * What's changed?
    * Why did it change?
    * How to test it?   

---

## Reporting Bugs ##

* Make sure to use the template 'Bug Report'.
* Include:
    * Steps to reproduce it.
    * Expected behavior
    * Logs/prints (if possible)

---

## Requesting New Features ##

* Make sure to use the template 'Feature Request'.
* Explain: 
    * Motivation
    * Expected behavior
    * Considered alternatives

---

## Code of Conduct ##

Be respectful, clear and kind. Always.  
We wish this project to be a safe space for learning and colaboration, without jugdment &/or conflicts.  
Thank you! <3