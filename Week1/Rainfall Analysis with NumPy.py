import numpy as np

sample_rainfall=( [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
sample_rainfall_np=np.array(sample_rainfall)
sample_rainfall_days=np.array([('mon',0.0),('Tue',5.2),('Wed',3.1),('Thu',0.0),('Fri',12.4),('Sat',0.0),('Sun',7.5)], dtype=[('dayss','U10'),('rainn','f4')])

# sample_rainfall_days

print("Convert the list to a NumPy array and print it",sample_rainfall_days)

print("Convert the list to a NumPy array and print it",sample_rainfall_np)

total_rainfall=np.sum(sample_rainfall_np)
print("Print the total rainfall for the week.",round(total_rainfall,2))

avg_rainfall=np.mean(sample_rainfall_np)
print('Print the average rainfall for the week.',round(avg_rainfall,2))

no_rain=np.where(sample_rainfall_np==0.0)
count_no_rain=np.count_nonzero(sample_rainfall==0.0)
print('how many days had no rain (0 mm)',count_no_rain,' days')


more_5_Rain=np.where(sample_rainfall_days['rainn']>5)
print("Days where rainfall was more than 5 mm is ", sample_rainfall_days[more_5_Rain],' days')



