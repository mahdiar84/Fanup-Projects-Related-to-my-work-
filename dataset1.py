import pandas as pd
import numpy as np

year = 2025

start = np.datetime64(f'{year}-01-01')
end   = np.datetime64(f'{year}-12-31')

days = (end - start).astype(int) + 1
random_day = np.random.randint(0, days)

random_date = start + np.timedelta64(random_day, 'D')
random_days = np.random.randint(0, days, size=100)
random_dates = start + random_days.astype("timedelta64[D]")

# Essential Data for our csv file
data = {
    "Date" : random_dates,
    "Sale" : np.random.uniform(low=50, high=120, size=100),
    "product" : np.random.random(100)
}

# Creating the csv file
df = pd.DataFrame(data=data)
df.to_csv("Dataset1", index=False)