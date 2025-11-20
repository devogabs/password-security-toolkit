import re

def check_password_strength(password: str) -> dict:
    score = 0
    feedback = []

    if len >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    return {
        'score': score,
        'max_score': 5,
        'feedback': feedback
    }
