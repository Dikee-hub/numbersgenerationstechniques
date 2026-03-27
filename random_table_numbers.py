import random

# Function to generate a 16x16 matrix with random numbers

def generate_random_table():
    matrix = []
    for _ in range(16):
        row = [random.randint(1, 100) for _ in range(16)]
        matrix.append(row)
    return matrix

# Generate the random table and print it
if __name__ == '__main__':
    random_table = generate_random_table()
    for row in random_table:
        print(row)