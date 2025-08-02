import numpy as np


#Calculate and print the average temperature for the week using NumPy.
# Temperature data (in °C): [18.5, 19, 20, 25.0, 2, 30, 13.9]

temp = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
temp_days=np.array([('sun',18.5),('mon',19),('tue',20),('wed',25.0),('thu',2),('fri',30),('sat',13.9)],dtype=[('name','U10'),('temps','i4')])
avg_temp=np.mean(temp)
print("The average temperature for the week: ",avg_temp)


# Determine and display the highest and lowest recorded temperatures
high_temp=np.max(temp)
low_temp=np.min(temp)
print("The highest recorded  temperature for the week: ",high_temp)
print("The lowest recorded  temperature for the week: ",low_temp)


# Convert all temperatures to Fahrenheit and print the converted values.
# (Use the formula: F = C × 9/5 + 32)
convert_temp=(temp*9/5+32)
print("Converted all temperature to Fahrenheit and printed the converted values",convert_temp)


# Identify and print the indices of days where the temperature exceeded 20°C.

temp_exceed_20=np.where(temp_days['temps']>20)

print("Printed the indices of days where the temperature exceeded 20°C",temp_days[temp_exceed_20])