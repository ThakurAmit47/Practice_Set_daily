a = input("enter string: ").lower()
vowels = "aeiou"

count = sum(1 for vow in a if vow in vowels)
print(count)
#day 5 q2