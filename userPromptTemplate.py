def promptUser(prompt: str, *options: str):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"[{i}] {option}")
    print("> ")
    
print("\nWelcome to [Game Title]")
promptUser("Choose your class.", "Warrior", "Mage", "Rogue")