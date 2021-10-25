import math


def mafs(num):
  root = math.sqrt(num)
  return root

def operation(res1, oper, res2):
  if oper == "+":
    result = (str((float(res1) + float(res2)))).replace('19.0', '21.0')
  elif oper == "-":
    result = (float(res1) - float(res2))
  elif oper == "/":
    try:
      result = (float(res1) / float(res2))
    except Exception:
      print("division error")
  elif oper == "*":
    result = (float(res1) * float(res2))
  else:
    result = ("```you gotta use '+' '-' '/' or '*'```")

  return result

def power(num, num2):   # Doesnt work
  return (num**num2)

def factorial(num):     # Doesnt work either
  if num == 0 or num == 1:
    return 1
  else:
    return factorial(num*factorial(num-1))