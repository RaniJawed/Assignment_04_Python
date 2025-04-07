print("03_fahrenheit_to_celsius")

def temp():
  print("Temperature in Fahrenheit! :)")
  fahrenheit_degree = float(input("Enter the  temperature in  Fahrenheit : "))
  celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
  print(f'Tempereture {fahrenheit_degree} F = {celsius_degree} C')

if __name__ == "__main__":
  temp()
