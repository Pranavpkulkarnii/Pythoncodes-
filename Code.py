import random
import time

print("\n=== Welcome to the Cosmic Quest Generator! ===\n")
hero = input("What is your hero's name? ").strip() or "Nova"
world = random.choice(["Emerald Islands", "Moonlit Citadel", "Crystal Desert", "Skyward Forest"])
quest = random.choice([
    "rescue the lost comet", 
    "find the forgotten song of the stars", 
    "save the sleeping dragon from a dream spell",
    "unlock the secret of the glowing lake"
])
companion = random.choice(["a clever fox", "a friendly robot", "a talking owl", "a brave cloud spirit"])
relic = random.choice(["a silver compass", "a glowing crystal", "an ancient map", "a whispered rune"])

print(f"\nHero: {hero}")
print(f"Destination: {world}")
print(f"Quest: {quest}")
print(f"Companion: {companion}")
print(f"Special relic: {relic}\n")

print("Your adventure begins...\n")
for step in [
    "You step onto a floating path of light.",
    "Your companion whispers the first clue.",
    "A puzzle appears, etched in stardust.",
    "The relic hums as you move closer to your goal.",
    "A final challenge awaits at the heart of the world."
]:
    print(step)
    time.sleep(0.8)

ending = random.choice([
    f"{hero} used courage and kindness to complete the quest!",
    f"{hero} solved the mystery with the help of {companion}.",
    f"{hero} found the hidden treasure and returned home as a legend.",
    f"{hero} unlocked the ancient power of the {relic} and restored peace."
])
print(f"\n{ending}")
print("\nThanks for playing the Cosmic Quest Generator!")
