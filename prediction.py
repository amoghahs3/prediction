# Dataset mapping
dataset = {
    1: 6,
    2: 7,
    3: 8,
    4: 9,
    5: 0,
    0: 5,
    9: 4,
    8: 3,
    7: 2,
    6: 1
}

# Input number from the user
number = int(input("Enter a number: "))

# Step 1: Add 44 to the input number
added_number = number + 44
print(f"Added result: {added_number}")

# Step 2: Split the added number into individual digits
added_str = str(added_number)
digit_1 = int(added_str[0])  # first digit
digit_2 = int(added_str[1])  # second digit

print(f"First digit: {digit_1}, Second digit: {digit_2}")

# Step 3: Compare the digits with the dataset and print the corresponding pair (if any)
def get_corresponding_pair(digit):
    # If the digit is in the dataset, return the pair (digit - corresponding value), else return None
    if digit in dataset:
        return f"{digit}-{dataset[digit]}"
    else:
        return None

# Fetch corresponding pairs for both digits
corresponding_1 = get_corresponding_pair(digit_1)
corresponding_2 = get_corresponding_pair(digit_2)

# Step 4: Print corresponding pairs
if corresponding_1:
    print(f"Corresponding value for {digit_1}: {corresponding_1}")
else:
    print(f"No corresponding value for {digit_1}")

if corresponding_2:
    print(f"Corresponding value for {digit_2}: {corresponding_2}")
else:
    print(f"No corresponding value for {digit_2}")
