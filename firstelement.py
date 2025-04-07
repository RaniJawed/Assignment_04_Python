
print("05_get_first_element")

def get__first_element(lst):
  print(lst[0])

def get_lst():
  lst = []
  element:str = input("Enter an element to add to the list: ")
  while element != "":
    lst.append(element)
    return lst

def main():
  lst = get_lst()
  get__first_element(lst)

if __name__ == "__main__":
  main()