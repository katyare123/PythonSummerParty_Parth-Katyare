import pandas as pd

# Load the dim_groups data (you may already have this DataFrame)
# Example: dim_groups = pd.read_csv("dim_groups.csv")  # or however you're importing it

# Ensure created_date is in datetime format
dim_groups['created_date'] = pd.to_datetime(dim_groups['created_date'])

# Filter groups created in October 2024
october_2024_groups = dim_groups[
    (dim_groups['created_date'].dt.year == 2024) &
    (dim_groups['created_date'].dt.month == 10)
]

# Get the maximum participant_count
max_participants = october_2024_groups['participant_count'].max()

print("Maximum number of participants in groups created in October 2024:", max_participants)
