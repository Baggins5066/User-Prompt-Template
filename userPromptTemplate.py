def promptUser(prompt: str, option1: str, option2: str, option3: str):
    print(f"""
{prompt}
[1] {option1}
[2] {option2}
[3] {option3}
> 
    """)

print("\nWelcome to [Game Title]")
promptUser("Choose your class.", "Warrior", "Mage", "Rogue")