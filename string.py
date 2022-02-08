name = input()

upper = ''
for char in name:
    if char.isupper():
        upper += char
result = ''.join(sorted(upper))

lower = ''
for char in name:
    if char.islower():
        lower += char
result1 = ''.join(sorted(lower))


def solve(result, result1):
   i = j = 0
   res = ""
   while i < len(result) and j < len(result1):
      res += result[i] + result1[j]
      i+=1
      j+=1
   while i < len(result):
      res += result[i]
      i += 1
   while j < len(result1):
      res += result1[j]
      j += 1
   return res

print(solve(result, result1))
