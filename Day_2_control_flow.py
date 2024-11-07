# control flow

# if ... else

# indentation(tab)
x = 10
y = 4

if x > y:
    print(f"{x} is greatder")
else :
    print(f"{y} is greatder")

# Task
# Get two person name

# Case 1
# Yuma, Yoshi
# 173 cm, 163 cm
# Expected
# Yuma is taller than Yoshi

print("\n-- Task(Case1) --")
user1_name = input(f"Please input your Name: ")
user1_height = float(input(f"Please input {user1_name} height: "))
user2_name = input(f"Please input your Name: ")
user2_height = float(input(f"Please` input {user2_name} height: "))

if user1_height > user2_height:
    print(f"{user1_name} is taller than {user2_name}.")
else:
    print(f"{user2_name} is taller than {user1_name}.")

# Case 2
# Yuma, Yoshi
# 173cm, 185cm
# Expected
# Yoshi is taller than Yuma by 12cm

print("\n-- Task(Case2) --")
user1_name = input(f"Please input your Name: ")
user1_height = float(input(f"Please input {user1_name} height: "))
user2_name = input(f"Please input your Name: ")
user2_height = float(input(f"Please` input {user2_name} height: "))
diff_height = abs(user1_height - user2_height)
if user1_height > user2_height:
    print(f"{user1_name} is taller than {user2_name} by {diff_height}.")
elif user1_height == user2_height:
    print(f"{user1_name} and {user2_name} are of same heghit.")
else:
    print(f"{user2_name} is taller than {user1_name} by {diff_height}.")

# if and else -> Only one
# elif -> Many


