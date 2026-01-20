import random

# Customize these for your bestie
bestie_name = "Alex"  # Replace with his name
your_name = "Your Name"  # Replace with your name

def birthday_quest():
    print(f"🎉 Welcome to the Ultimate Birthday Quest, {bestie_name}! 🎉")
    print(f"Prepared by your bro, {your_name}. Let's make this birthday legendary!")
    print("Your mission: Navigate challenges to unlock epic birthday surprises.\n")
    
    score = 0
    level = 1
    
    # Level 1: Friendship Trivia
    print("Level 1: Bro Trivia Challenge!")
    print("Answer these questions about our friendship. (Type your answers)")
    
    q1 = input("What's the name of our favorite inside joke? ").strip().lower()
    if "chaos" in q1 or "epic" in q1:  # Customize based on real answers
        print("Correct! +10 points for remembering the chaos!")
        score += 10
    else:
        print("Close enough – bros don't sweat the small stuff. +5 points!")
        score += 5
    
    q2 = input("How many years have we been causing trouble together? ").strip()
    if q2.isdigit() and int(q2) > 0:
        print("Solid guess! +10 points for the memories!")
        score += 10
    else:
        print("Time flies! +5 points anyway.")
        score += 5
    
    # Level 2: Random Luck Challenge
    print("\nLevel 2: Luck of the Bro!")
    print("Roll a virtual die (1-6). Guess if it's even or odd.")
    guess = input("Even or odd? ").strip().lower()
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!")
    if (roll % 2 == 0 and guess == "even") or (roll % 2 != 0 and guess == "odd"):
        print("Jackpot! +15 points!")
        score += 15
    else:
        print("Better luck next time! +5 points for trying.")
        score += 5
    
    # Level 3: Final Wish
    print("\nLevel 3: The Ultimate Birthday Wish!")
    print("Type a fun birthday wish for yourself:")
    wish = input().strip()
    print(f"Here's your wish echoed back: '{wish}' – Make it happen, {bestie_name}!")
    score += 20  # Bonus for participating
    
    # Endgame
    print(f"\n🎊 Quest Complete! Your total score: {score}/50")
    if score >= 40:
        print("Legendary status unlocked! You're the GOAT of birthdays. 🐐")
    elif score >= 25:
        print("Epic run! Bros for life. 🤝")
    else:
        print("Fun times anyway – let's replay and crush it!")
    
    print(f"Happy Birthday, {bestie_name}! From {your_name} with love. 🎂")

# Run the game
birthday_quest()