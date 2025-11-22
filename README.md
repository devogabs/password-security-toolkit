# password-security-toolkit 🔐

<!-- badges -->
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
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
  Generates a random, strong password with costumizable rules.

- **CLI Interface**  
  Clean and extendable command-line interface using Python’s `argparse`.

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
## Project Structure
```bash
src/
 ├── cli.py
 ├── password_checker.py
 ├── password_generator.py
 └── __init__.py
.gitignore
README.md
requirements.txt
```

---
## Roadmap

  **Next Steps:**
  - Add entropy estimation

  - Add breach verification using a Bloom Filter

  - Improve password scoring model

  - Allow generating multiple passwords (--count)

  - Improve CLI UX (colors, formatting, subcommands)

  - Package and publish as an installable tool

  - Performance improvements

  - Add automated unit tests