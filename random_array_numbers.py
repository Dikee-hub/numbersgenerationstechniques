import random

# Function to generate a flat list of unique random numbers

def generate_unique_random_numbers(size, lower_bound, upper_bound):
    if size > (upper_bound - lower_bound + 1):
        raise ValueError("Size must be less than or equal to the range of unique numbers.")
    return random.sample(range(lower_bound, upper_bound + 1), size)

# Generating 16 unique random numbers between 1 and 100
unique_random_numbers = generate_unique_random_numbers(16, 1, 100)
print(unique_random_numbers)