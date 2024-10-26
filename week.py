# Function to add the digits of a number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Input from the user
user_input = input("Enter a number: ")

# Convert the input to an integer
number = int(user_input)

# Step 1: Add the digits of the number
digit_sum = sum_of_digits(number)

# Step 2: Print the digit sum
print(f"The sum of the digits is: {digit_sum}")

# Step 3: Determine the relevant digit for the next steps
if digit_sum == 10:
    relevant_digit = 0
elif digit_sum > 10:
    relevant_digit = digit_sum % 10  # Take the last digit
else:
    relevant_digit = digit_sum

# Step 4: Determine the previous and next numbers
previous_number = (relevant_digit - 1) % 10
next_number = (relevant_digit + 1) % 10

# Step 5: Print previous and next numbers
print(f"Previous number is {previous_number} and next number is {next_number}.")
