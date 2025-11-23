from password_checker import check_password_strength
from password_generator import generate_password
import argparse


def cli():

    parser = argparse.ArgumentParser(
        description="Password Security Toolkit: Check password strength or generate secure passwords."
    )

    # Create subparsers for different functionalities
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands")
    # Subcommand for checking password strength
    check_parser = subparsers.add_parser(
        "check", help="Check the strength of a password")
    check_parser.add_argument("password", type=str,
                              help="The password that will be evaluated.")
    check_parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output.")
    # Subcommand for generating a secure password
    generate_parser = subparsers.add_parser(
        "generate", help="Generate a secure password")
    generate_parser.add_argument("-l", "--length", type=int, default=12,
                                 help="Length of the password (minimum 4, default: 12).")
    generate_parser.add_argument(
        "-c", "--count", type=int, default=1, help="Number of passwords to generate (default: 1).")
    generate_parser.add_argument(
        "--no-upper", action="store_false", dest="use_upper", help="Exclude uppercase letters.")
    generate_parser.add_argument(
        "--no-lower", action="store_false", dest="use_lower", help="Exclude lowercase letters.")
    generate_parser.add_argument(
        "--no-digits", action="store_false", dest="use_digits", help="Exclude digits.")
    generate_parser.add_argument(
        "--no-symbols", action="store_false", dest="use_symbols", help="Exclude symbols.")

    args = parser.parse_args()  # parse the command line arguments

    if args.command == "check":
        results = check_password_strength(args.password)
        score = results['score']
        feedback = results['feedback']
        max_score = results['max_score']

        print(f"Password Strength Score: {score}/{max_score}")
        if args.verbose and feedback:
            print("Feedback:")
            for message in feedback:
                print(f"- {message}")

    elif args.command == "generate":
        try:
            pwds = []
            for _ in range(args.count):

                password = generate_password(
                    length=args.length,
                    use_upper=args.use_upper,
                    use_lower=args.use_lower,
                    use_digits=args.use_digits,
                    use_symbols=args.use_symbols
                )
                pwds.append(password)
            if args.count > 1:
                print("Generated Passwords:")
                for pwd in pwds:
                    print(f"- {pwd}")
            else:
                print(f"Generated Password: {password}")
        except ValueError as ve:
            print(f"Error: {ve}")


if __name__ == "__main__":
    cli()
