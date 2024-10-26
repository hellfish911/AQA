"""
This module processes a human data.

It performs various data manipulations and analyses, aimed at extracting
and counting specific elements within the data.
"""

# Constants for indexes
NEW_RECORD_INDEX = 0
SWAP_FIRST_INDEX = 1
SWAP_SECOND_INDEX = 5
AGE_CHECK_INDEXES = (6, 10, 13)  # Immutable tuple for constant indexes
AGE_THRESHOLD = 30  # Constant for the age threshold

# Original list of people records
people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]

# Step 1: Add a new record to the beginning of the list
new_record = ('Liam', 'King', 32, 'Data Scientist', 'Philadelphia')
people_records.insert(NEW_RECORD_INDEX, new_record)

# Step 2: Swap elements with indexes 1 and 5 (1 <-> 5)
temp = people_records[SWAP_FIRST_INDEX]
people_records[SWAP_FIRST_INDEX] = people_records[SWAP_SECOND_INDEX]
people_records[SWAP_SECOND_INDEX] = temp

# Print the modified list after insertion and swapping
print('Modified List:')
for person in people_records:
    print(person)

# Step 3: Check if people with specified indexes have age >= AGE_THRESHOLD
age_check = all(
    people_records[i][2] >= AGE_THRESHOLD
    for i in AGE_CHECK_INDEXES
)

# Print condition check result
print(
    '\nAge condition check (all ages >= 30 at indexes 6, 10, and 13):',
    age_check,
)
