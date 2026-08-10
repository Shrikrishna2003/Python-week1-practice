text = input("Enter text: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
others = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

print(f"Uppercase Letters: {uppercase}")
print(f"Lowercase Letters: {lowercase}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Other Characters: {others}")