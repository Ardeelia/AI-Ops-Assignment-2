import random
import pandas as pd
import os

random.seed(42)

FIRST_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Taylor", "Miller", "Wilson", "Moore", "Anderson", "Thomas", "Jackson"]
DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "company.org", "mail.net"]
PLANS = ["free", "pro", "enterprise"]

os.makedirs("data", exist_ok=True)

total_records = 1200
shards = 8
records_per_shard = total_records // shards

for shard_id in range(shards):
    rows = []
    for i in range(records_per_shard):
        user_id = f"USR-{shard_id}-{i:04d}"
        
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        username = f"{first.lower()}_{last.lower()}_{random.randint(10, 99)}"
        
        if random.random() < 0.1:
            username = ""

        email_roll = random.random()
        if email_roll < 0.12:
            email = random.choice([
                f"{username}gmail.com", 
                f"{first} @ {random.choice(DOMAINS)}", 
                "invalid_email_format", 
                f"missing_domain@{first}"
            ])
        elif email_roll < 0.18:
            email = ""
        else:
            email = f"{username}@{random.choice(DOMAINS)}"

        signup_date = f"2026-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        
        plan = random.choice(PLANS)
        if random.random() < 0.04:
            plan = None

        rows.append({
            "user_id": user_id,
            "username": username,
            "email": email,
            "signup_date": signup_date,
            "plan": plan
        })

    df = pd.DataFrame(rows)
    file_path = f"data/signup_shard_{shard_id}.csv"
    df.to_csv(file_path, index=False)

print(f"Successfully generated {shards} CSV shards in the 'data/' directory.")