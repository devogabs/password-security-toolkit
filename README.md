# password-security-toolkit 🔐
Password Security Toolkit (PST) is a lightweight command-line toolkit for analyzing password strenght and generate safe passwords. This project was created for learning purposes, focusing on Python, cybersecurity fundamentals, CLI design, and practical tooling).

---

## 🚀 Features

- **Password Strength Checker**  
  Evaluates a password using multiple criteria:
  - Length
  - Uppercase & lowercase letters
  - Digits
  - Special characters
  - Common patterns (e.g., repeated characters)
  - Dictionary-based weakness detection

- **Clear Score System**  
  Returns a numerical score and a descriptive classification:  
  *Weak · Moderate · Strong · Very Strong*

- **Detailed Feedback**  
  Explains exactly **why** a password is weak and how to improve it.

- **CLI Interface**  
  Simple command-line tool using Python’s `argparse`, fully ready for extension.

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
python3 src/main.py --check "your_password_here"
```

Example output:
```bash
Score: 72/100
Strength: Strong

Feedback:
- Good length ✔️
- Contains uppercase letters ✔️
- Contains digits ✔️
- Contains predictable patterns like '123' ❗

