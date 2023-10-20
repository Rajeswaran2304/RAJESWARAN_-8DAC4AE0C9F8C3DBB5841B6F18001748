#Implement a recursive function to calculate the factorial of a given number.
def factorial(n: int) -> int:
  """Calculates the factorial of a given number.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
factorial(5)
#120
