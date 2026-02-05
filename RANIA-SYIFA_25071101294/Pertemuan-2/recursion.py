#Recursion
def countdown(n): #fungsinya dia sendiri
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1) #akhirnya memanggil diri sendiri

countdown(5)

#Identifying base case and recursive case:
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))