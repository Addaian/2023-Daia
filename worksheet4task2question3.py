def getpword():
  check = 0  
  attempt = 1 
  if attempt == 1: 
    print("Enter password") 
    password = str(input()) 
    if len(password) < 6 or len(password) > 8:
      print("Error. Password must be 6 to 8 characters long")
    else: 
      attempt = attempt + 1 
  if attempt == 2:
    print("enter password again: ")
    password2 = str(input()) 
    if password != password2:
      print("Error – passwords do not match -- try again") 
    else:
      print("password change successful")
      check = 1
      return check
x = 0
while x != 1:
  x = getpword() 
