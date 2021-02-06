from art import logo

def add(n,m):
  return n+m
def subtract(n,m):
  return n-m
def multiply(n,m):
  return n*m
def divide(n,m):
  return n/m

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))
  for i in operations:
    print (i)
  while True:
    ops = input("What operation do you want? ")
    num2 = float(input("What is the next number? "))
    result1 = operations[ops](num1,num2)
    print(f"{num1} {ops} {num2} = {result1}")
    if input(f"Type 'y' to continue calculating with {result1}. Or type 'n' to recur. ")=='y':
      num1=result1
    else:
      calculator()

calculator()