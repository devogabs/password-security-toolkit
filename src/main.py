from password_checker import check_password_strength
import argparse

def main():

    parser = argparse.ArgumentParser(
        description="Password Security Toolkit: Check password strength."
    )

   # parser.add_argument("check", help="Check the strength of the provided password.")
    parser.add_argument("password", type=str, help="The password that will be evaluated.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args() # parse the command line arguments

    
    results = check_password_strength(args.password)
    score = results['score']
    feedback = results['feedback']
    max_score = results['max_score']

    print(f"Password Strength Score: {score}/{max_score}")
    if args.verbose and feedback:
        print("Feedback:")
        for message in feedback:
            print(f"- {message}")

if __name__ == "__main__":
    main()