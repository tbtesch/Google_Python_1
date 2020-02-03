def reverse(s):
  s = s.replace(" ", "")
  s = s.lower()
  return s[::-1]
def is_palindrome(s):
  s = s.replace(" ", "")
  s = s.lower()
  rev = ''.join(reverse(s))
  
  if (s==rev):
    return True
  return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True