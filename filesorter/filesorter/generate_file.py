"""Generate a file with a specific percentage of duplicate lines."""

import csv
import faker

# Initialize the Faker instance
fake = faker.Faker()

# Define the target input size and the percentage of matching lines
file_size = 1000  # Number of lines in the CSV file
match_percentage = 0.20  # 20% of the lines will match the given line

# Define the line that should appear in some of the rows
fixed_line = ['April Mcguire', 'Kyrgyz Republic', '+1-927-438-7339', 'Advertising copywriter', 'aadams@example.net']

# Calculate the number of matching lines and the number of random lines
num_matches = int(file_size * match_percentage)
num_randoms = file_size - num_matches

# Create the CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the matching lines
    for _ in range(num_matches):
        writer.writerow(fixed_line)
    
    # Write the random lines
    for _ in range(num_randoms):
        name = fake.name()
        country = fake.country()
        phone = fake.phone_number()
        job_title = fake.job()
        email = fake.email()
        writer.writerow([name, country, phone, job_title, email])

print(f'CSV file "output.csv" with {file_size} rows has been generated.')
