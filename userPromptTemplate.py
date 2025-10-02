def promptUser(prompt: str, *options: str):
    while True:
        print(f"\n{prompt}")
        for i, option in enumerate(options, 1):
            print(f"[{i}] {option}")
        
        try:
            choice = int(input("> "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("\nERROR: Invalid input.")
        except ValueError:
            print("\nERROR: Invalid input.")

# promptUser() example
print("\npromptUser() Example")
userClass = promptUser("Choose your class.", "Warrior", "Mage", "Rogue")
print(f"\nYou have chosen the {userClass} class.\n")