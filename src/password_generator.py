from password_checker import check_password_strength
import secrets # "secrets" is better than "random" for cryptographic purposes
import string

def generate_password(length: int = 12, use_upper: bool = True, use_lower: bool = True, use_digits: bool = True, use_symbols: bool = True) -> str:
    '''
    Generate a random password with the specified criteria.
    
    Args:
        length (int): Length of the password (minimum 4).
        use_upper (bool): Include uppercase letters.
        use_lower (bool): Include lowercase letters.
        use_digits (bool): Include digits.
        use_symbols (bool): Include symbols.
    
    Returns:
        str: The generated password.
    
    Raises:
        ValueError: If the length is less than 4 or no character types are selected.
    '''
    
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    character_pool = ""
    
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    while True:

        password = ''.join(secrets.choice(character_pool) for _ in range(length)) # list comprehension to build the password
        results = check_password_strength(password)
        if results['score'] >= 50:
            return password
        else:
            continue

    