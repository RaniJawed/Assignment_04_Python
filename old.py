print("04_how_old_are_they")

def add_ages():
  anthon:int = 21
  beth:int = anthon + 6
  chen:int = beth + 20
  drew:int = chen + anthon
  ethan:int = chen

  print("Anthon is " + str(anthon))
  print("Beth is " + str(beth))
  print("Chen is " + str(chen))
  print("Drew is " + str(drew))
  print("Ethen is " + str(ethan))


if __name__ == "__main__":
  add_ages()




  print("05_triangle_perimeter.")

def triangle():
  print("This code is about perimeter of triangle.")
  side1:float = float(input("what is the length of side 1 ? "))
  side2:float= float(input("what is the length of side 2? "))
  side3:float = float(input("what is the length of side 3 ? "))
  total:float = float(side1 + side2 + side3)
  print(f'The perimeter of the triangle is {total}')

if __name__ == "__main__":
  triangle()
     