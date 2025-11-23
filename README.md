# password-security-toolkit 🔐

<!-- badges -->
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Status](https://img.shields.io/badge/status-in%20development-yellow)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC--BY--NC--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
![Style](https://img.shields.io/badge/code%20style-pep8-informational)
![Stars](https://img.shields.io/github/stars/devogabs/password-security-toolkit?style=social)
![Forks](https://img.shields.io/github/forks/devogabs/password-security-toolkit?style=social)

Password Security Toolkit (PST) is a lightweight command-line toolkit for analyzing password strength and generate safe passwords. This project was created for learning purposes, focusing on Python, cybersecurity fundamentals, CLI design, and practical tooling.

---

## 🚀 Features

- **Password Strength Checker**  
  Evaluates a password using multiple criteria:
  - Length
  - Uppercase & lowercase letters
  - Digits
  - Special characters
  - Common patterns (e.g., repeated characters) *(WIP)*
  - Dictionary-based weakness detection *(WIP)*
  - Entropy estimation *(Planned)*


- **Detailed Feedback**  
  Explains exactly **why** a password is weak and how to improve it.

- **Secure Password Generator**
  Generates a random, strong password with customizable rules.

- **CLI Interface**  
  Clean and extendable command-line interface using Python’s `argparse`.


---
## 🗺 Roadmap

  **Next Steps:**

  * Password Checker:
  
    - Add entropy estimation

    - Add breach verification using a Bloom Filter

    - Add pattern detection

    - Improve password scoring model & feedback

  * Password Generator:

    - Allow generating multiple passwords (--count) *(Done! ✅)*

  * CLI:
  
    - Improve CLI UX (colors, formatting, subcommands)
    - Improve --help/usage descriptions


  * Miscellaneous & Extras (Future implementations):
    - Turn into an installable package

    - Performance improvements

    - Add automated unit tests

    - Put more *emojis* into the documentation!! =) *(Done! ✅)*

---

## 📦 Installation

Clone the repository:

```bash
git clone git@github.com:devogabs/password-security-toolkit.git
cd password-security-toolkit

```
Install dependencies:

```bash
pip install -r requirements.txt
```

### Requirements
  * Python 3.13 or above
  * 'pip' package manager

## 🖥️ Usage (CLI)

Run the password checker:
```bash
python3 src/cli.py check "your_password_here"
```

Example output:
```bash
Score: 3/5

Feedback:
- Good length ✔️
- Contains uppercase letters ✔️
- Contains digits ✔️
- Contains predictable patterns like '123' ❗

```
Run the password generator:
```bash
python3 src/cli.py generate
# Example output: "t-!Z1;\5Y~hT"
```

---

## 🏛 Project Structure
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
    ├── bug_report.md
    └── feature_request.md
 └── PULL_REQUEST_TEMPLATE.md
```

---

## Best Practices Used

This project follows several conventions to keep the codebase, commits, and contribution workflow clean and consistent:

### ✦ Commit Style (Conventional Commits)
Commits follow the format:

- `feat:` a new feature  
- `fix:` bug fix  
- `docs:` documentation changes  
- `style:` formatting changes with no logic impact  
- `refactor:` code improvements that do not change behavior  
- `test:` adding or updating tests  
- `chore:` internal tasks with no effect on the tool’s logic  

More details are available in **CONTRIBUTING.md**.

---

## Contribution Guide

Contributions are welcome!  
Please read the full guidelines before opening an issue or submitting a pull request:

👉 **[See CONTRIBUTING.md](CONTRIBUTING.md)**

---

## Issue & Pull Request Templates

This repository includes templates to streamline communication:

- **Bug Report Template**  
- **Feature Request Template**  
- **Pull Request Template**

They are located in:  
`.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md`


---
## 📄 License

This project is licensed under the **CC BY-NC-SA 4.0** license.

You are free to:
- **Use**, **modify**, **and share** the code for *noncommercial* purposes  
- Create derivative works, as long as:
  - You **credit** the author (Gabriel Bonesso)  
  - You **share your changes** under the same license  

You are **not allowed to**:
- Use this project for **commercial purposes**
- Redistribute adaptations under a more permissive license

Full details are in the [LICENSE](LICENSE) file.

---

Thank you! :3
