def main():
  print("Hello learners!")

def addmultiplenumbers(numbers):
  total = 0
  for n in numbers:
    total += n
  return total
def multiplymultiplenumbers(numbers):
  total = 1
  for n in numbers:
    total *= n
  return total
def isiteven(number):
  if number % 2 == 0:
    return True
  else:
    return False
def isitaninteger(number):
  if isinstance(number, int):
    return True
  else:
    return False

if __name__=="__main__":
  main()