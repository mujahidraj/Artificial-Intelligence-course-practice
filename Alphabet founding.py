text = "@This is A teXt 123$"

capital_count = 0
small_count = 0
number_count = 0
character_count = 0

capital_chars = []
small_chars = []
number_chars = []
character_chars = []

for char in text:
    if char.isupper():
        capital_count += 1
        capital_chars.append(char)
    elif char.islower():
        small_count += 1
        small_chars.append(char)
    elif char.isdigit():
        number_count += 1
        number_chars.append(char)
    else:
        character_count += 1
        character_chars.append(char)

print("Capital Alphabets:", capital_count, "Characters:", capital_chars)
print("Small Alphabets:", small_count, "Characters:", small_chars)
print("Numbers:", number_count, "Characters:", number_chars)
print("Characters:", character_count, "Characters:", character_chars)
