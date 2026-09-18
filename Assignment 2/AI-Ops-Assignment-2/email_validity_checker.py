def classify(email):
    if not isinstance(email, str) or not email.strip():
        return "invalid"
    if not email or "@" not in email or "." not in email or " " in email:
        return 'Invalid'
    return 'Valid'

import json
import os
import pandas as pd

shard_index = int(os.environ.get("JOB_COMPLETION_INDEX", "0"))
node_name = os.environ.get("NODE_NAME", "unknown")
pod_name = os.environ.get("POD_NAME", "unknown")

file_path = f"/app/data/signup_shard_{shard_index}.csv"
df = pd.read_csv(file_path)

invalid_count = 0

for idx,row in df.iterrows():
    result = classify(row['email'])
    if(result == 'Invalid'):
        invalid_count += 1

results = {'completion_index' : shard_index, 'invalid_counts' : invalid_count}

print(f"RESULT_JSON:{json.dumps(results)}")
