
import random
import string

print("\n ✨Welcome to the Password Generator App.✨ \n")
def generate_password(length=12,use_numbers=True,use_symbols=True):
  '''Generate strong password with given options.'''
  if length < (use_numbers + use_symbols):  # Check if length is enough for constraints
        return "❌ Password length is too short for selected options!"

  characters = string.ascii_letters
  if use_numbers:
    characters += string.digits
  if use_symbols:
    characters += string.punctuation
  password = "".join(random.choice(characters) for _ in range(length))
  return password

try:
  length = int(input("Enter password length: "))
  use_numbers = input("includes numbers? (yes/no):").lower() == "yes"
  use_symbols = input("Includes symbols? (yes/no):").lower() == "yes"

  password = generate_password(length,use_numbers,use_symbols)
  print("\n🔑 Your Generated Password: ", password)
except ValueError:
    print("❌ Please enter a valid number!")
