#Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. 
# A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  z=1
  sum=0
  while n>z:
    if n%z == 0:
      sum = sum + z
      z=z+1
    else:
      z=z+1
  return sum
print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16