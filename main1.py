print("what is your name?")
name = str(input()) 

def multiples(v1, vstart, vend):
  print("hi, " , name, ", here is your times table") 
  for i in range(vstart, vend+1):
    print(v1, "* ", i, "=" , v1 * i)

print("enter times table number (number you want to ouput a times table for), starting multiple and end multiple") 
timestable = int(input()) 
start = int(input()) 
end = int(input()) 
multiples(timestable, start, end) 