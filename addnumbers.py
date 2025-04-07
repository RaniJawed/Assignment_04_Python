
print("01_add_many_number")

def add_numbers(numbers)->int:
  num:int = 0
  for n in numbers:
    num += n

  return num

def main():
  numbers:list[int] = [1,2,3,4,5,6]
  sum:int = add_numbers(numbers)
  print(sum)

if __name__ == "__main__":
    main()