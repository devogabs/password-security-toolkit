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
  - Common patterns (e.g., repeated characters) (Currently working on it!)
  - Dictionary-based weakness detection (Currently working on it!)


- **Detailed Feedback**  
  Explains exactly **why** a password is weak and how to improve it.

- **Secure Password Generator**
  Generates a random strong password, following the criteria determined by the user

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
# Example output: "t-!Z1;\5Y~hT"'
```

---
## Roadmap

  - **Next Steps:**
    - Implement password's entropy estimative
    - Implement breach verification with Bloom Filter
    - Add strength classifications and normalize the score
    - Add a "count" argument to the generate command, so you can generate more than one password per go.
    - Improve CLI (Add some color)
    - Turn into a instalable package
    - Optimization
    - Create automated tests