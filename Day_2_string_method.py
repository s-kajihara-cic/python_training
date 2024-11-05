quote = "I love Python"

# Array
# [] -> bracket
# [Index]
print(quote[2])
print(quote[3])

print(quote[2] + quote[3] + quote[4] + quote[5])

# quote[start:end:skip]
# end is not include 
print(quote[2:6])

print(quote[2:]) # love Python

# skip
print(quote[2:10:2])

# Nagative Index
print(quote[-1])
print(quote[-2])

# Whole string
print(quote[-1:])

# Reverse string
print(quote[::-1])

name = '  Natusmi  '
print(name.upper())
print(name.lower())

# trim white words
print(name.strip())


# Task   
secret_message = "   Programming in Python is not only powerful but also fun!   "

# Expected Output
# "PYTHON-POWERFUL"
message = secret_message.upper()
word1 = message[18:24]
word2 = message[37:45]
print(f"{word1}-{word2}")

word3 = secret_message[18:24]
word4 = secret_message[37:45]
print(f"{word1}-{word2}".upper())

# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"
original_message = flipped_message[::-1]
print(original_message)
word5 = original_message[0:6]
word6 = original_message[11:20]
print(f"{word5} 🗡️  {word6} 🌸".lower())

