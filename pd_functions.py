## Practical on functions: #Functions Operation on Netflix dataset:  
#a)mean()
#b)min()
#c)max()
#d)sum()
#e)agg()
#f)Average()

import pandas as pd
import random
from datetime import datetime, timedelta

# Set a seed for reproducibility
random.seed(42)

# Generate synthetic data for a smaller dataset
num_users = 30
user_ids = list(range(1, num_users + 1))
ages = [random.randint(18, 60) for _ in range(num_users)]
genres = ['Action', 'Comedy', 'Drama', 'Science Fiction', 'Documentary']
preferred_genres = [random.choice(genres) for _ in range(num_users)]
watch_times = [random.randint(30, 240) for _ in range(num_users)]  # Watch time in minutes

# Generate random dates for the past month
start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now()
watch_dates = [start_date + timedelta(days=random.randint(0, 30)) for _ in range(num_users)]

# Create a DataFrame
data = {
    'User_ID': user_ids,
    'Age': ages,
    'Preferred_Genre': preferred_genres,
    'Watch_Time_Minutes': watch_times,
    'Watch_Date': watch_dates
}
netflix_df = pd.DataFrame(data)

# Display the smaller dataset
print("Original Dataset:")
print(netflix_df)

# Mean, Min, Max, Sum
mean_watch_time = netflix_df['Watch_Time_Minutes'].mean()
min_watch_time = netflix_df['Watch_Time_Minutes'].min()
max_watch_time = netflix_df['Watch_Time_Minutes'].max()
sum_watch_time = netflix_df['Watch_Time_Minutes'].sum()

print("\nMean Watch Time:", mean_watch_time, "minutes")
print("Min Watch Time:", min_watch_time, "minutes")
print("Max Watch Time:", max_watch_time, "minutes")
print("Sum Watch Time:", sum_watch_time, "minutes")

# e) Agg
agg_results = netflix_df['Watch_Time_Minutes'].agg(['mean', 'min', 'max', 'sum'])
print("\nAggregated Results:")
print(agg_results)

# f) Average
average_watch_time = netflix_df['Watch_Time_Minutes'].mean()
print("\nAverage Watch Time:", average_watch_time, "minutes")
