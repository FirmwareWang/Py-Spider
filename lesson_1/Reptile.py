class car():
  color = "red"
  def __init__(self):
    print("It's a car.")

  def speed(self):
    return 100

class airplane():
  color = "blue"

  
print("I'm Reptile")
if __name__ == "__main__":
  # implicitly
  car_A = car()
  print(car_A.color)
  print(car_A.speed())

'''
- package
--- module1
--- module2
'''


# def init():
#   print("init")

# explicitly
# init()