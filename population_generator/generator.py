import random

import faker
import pandas as pd

# Create a Faker instance
fake = faker.Faker()

# Number of records to generate
num_records = 500000

# Generate random data
data = {
    "name": [],
    "date_of_birth": [],
    "death_date": [],
    "identity_number": [],
    "gender": [],
    "nationality": [],
}

for _ in range(num_records):
    data["name"].append(fake.name())
    data["date_of_birth"].append(
        fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d")
    )
    data["death_date"].append(
        fake.date_of_birth(minimum_age=0, maximum_age=0).strftime("%Y-%m-%d")
        if random.choice([True, False])
        else ""
    )
    data["identity_number"].append(fake.ssn())
    data["gender"].append(random.choice(["MALE", "FEMALE"]))
    data["nationality"].append(
        random.choice(["SINGAPORE_CITIZEN", "FOREIGNER", "DUAL_CITIZEN"])
    )

# Create a DataFrame
df = pd.DataFrame(data)

# Specify the filename
filename = "../data/population_data.csv"

# Write DataFrame to CSV file
df.to_csv(filename, index=False)

print(f"CSV file '{filename}' with {num_records} records has been created.")
