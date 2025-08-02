import pandas as pd

# Let's assume dim_groups is already defined or loaded in your environment
# Example: dim_groups = pd.read_csv("dim_groups.csv")

# Convert 'created_date' to datetime format
dim_groups['created_date'] = pd.to_datetime(dim_groups['created_date'])

# Filter groups created in October 2024
october_2024_groups = dim_groups[
    (dim_groups['created_date'].dt.year == 2024) &
    (dim_groups['created_date'].dt.month == 10)
]

# Calculate the average number of participants
average_participants = october_2024_groups['participant_count'].mean()

print("Average number of participants in groups created in October 2024:", average_participants)
