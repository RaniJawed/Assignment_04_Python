print("00_joke_bot")

PROMPT: str = "What do you want? "
JOKE:str = "Why don’t skeletons fight each other? \n Because they don’t have the guts! 😆"
SORRY:str = "Sorry I only tell jokes."

def main():
  user_input = input(PROMPT)
  user_input = user_input.strip().lower()

  if "joke" in user_input:
    print(JOKE)
  else:
    print(SORRY)

if __name__ == "__main__":
  main()