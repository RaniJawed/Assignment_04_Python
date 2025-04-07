
print("7_tiny_mad_lib")

def mad_lib():
  noun:str = str(input("Enter a noun: "))
  adjective:str = str(input("Enter an adjective: "))
  verb:str = str(input("Enter a verb: "))
  print(f"Are you {verb} live in {adjective} {noun}?")



if __name__=="__main__":
  mad_lib()
