import pandas as pd

# Convert created_date to datetime
dim_groups['created_date'] = pd.to_datetime(dim_groups['created_date'])

# Filter groups: created in October 2024 AND participant_count > 50
filtered_groups = dim_groups[
    (dim_groups['created_date'].dt.year == 2024) &
    (dim_groups['created_date'].dt.month == 10) &
    (dim_groups['participant_count'] > 50)
]

# Calculate average number of messages
average_messages = filtered_groups['total_messages'].mean()

print("Average messages sent in large groups (Oct 2024):", average_messages)
