n = 10
m = 6 #this is simply to call an entire empty carpark before
carpark = ["[empty]"] * 10
for i in range(n):
    carpark[i] = ["[empty]"] * m
  
def emptyCarPark():
  n = 10
  m = 6 
  global carpark
  carpark = ["[empty]"] * 10
  for i in range(n):
    carpark[i] = ["[empty]"] * m
  
def parkACar(carpark):
  check1 = 0 
  reentry = 1 
  check2 = 0 
  while reentry == 1: #this determines whether or not the row and column are entered correctly and repeats if it is not
    reentry = 0 
    print("parks a car:")
    print("registration number is? ")
    regnum = str(input())
    print("Enter row:")
    row = int(input())
    print("Enter column: ") 
    column = int(input())
    if row > 0 and row < 11: 
      check1 = 1 
    else:
      reentry = 1 
    if column > 0 and column < 7:
      check2 = 1 
    else:
      reentry = 1 
  
    if check1 == 1 and check2 == 1: 
      if carpark[row-1][column-1] == "[empty]": 
        carpark[row-1][column-1] = [regnum]
      else:
        print("that space is taken")  
        reentry = 1

def removeACar(carpark):
  check1 = 0 
  reentry = 1 
  check2 = 0 
  
  while reentry == 1: #this determines whether or not the row and column are entered correctly and repeats if it is not
    reentry = 0 
    print("removes a car:")
    print("Enter row:")
    row = int(input())
    print("Enter column: ") 
    column = int(input())
    if row > 0 and row < 11: 
      check1 = 1 
    else:
      reentry = 1 
    if column > 0 and column < 7:
      check2 = 1 
    else:
      reentry = 1 
  
    if check1 == 1 and check2 == 1: 
      if carpark[row-1][column-1] != "[empty]": 
        carpark[row-1][column-1] = "[empty]"
      else:
        print("that space is not taken")  
        
def displayCarParkGrid(carpark):
  for row in carpark:
    print(' '.join([str(elem) for elem in row]))
  

#main program
#display menu of options
print("1. Reset all spaces in the car park to 'empty'")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit\n")
option = input("Enter your choice: ")
#accept choice
while option != "5":
  if option == "1":
    emptyCarPark()
  elif option == "2":
    parkACar(carpark)
  elif option == "3":
    removeACar(carpark)
  elif option == "4":
    displayCarParkGrid(carpark)
  else:
    print("Invalid choice please re-enter: ")
  print("1. Reset all spaces in the car park to 'empty'")
  print("2. Park a car")
  print("3. Remove a car")
  print("4. Display the car park grid")
  print("5. Quit\n")
  option = input("Enter your choice: ")
print("Goodbye")
