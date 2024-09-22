import numpy as np
# 1. Create an array
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 15, 25, 35, 45])

print("Array 1:", array1)
print("Array 2:", array2)

# 2. Perform arithmetic operations
sum_array = array1 + array2
difference_array = array1 - array2
product_array = array1 * array2
quotient_array = array1 / array2

print("\nArithmetic Operations:")
print("Sum:", sum_array)
print("Difference:", difference_array)
print("Product:", product_array)
print("Quotient:", quotient_array)

# 3. Calculate statistics
mean_value = np.mean(array1)
median_value = np.median(array1)
std_deviation = np.std(array1)

print("\nStatistics:")
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)

# 4. Reshaping the array
reshaped_array = array1.reshape(5, 1)
print("\nReshaped Array (5x1):")
print(reshaped_array)




import pandas as pd

# 1. Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago'],
    'Salary': [70000, 80000, 60000, 90000, 75000]
}

df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

# 2. Adding a new column
df['Experience'] = [2, 5, 1, 8, 3]  # Years of experience
print("\nDataFrame after adding 'Experience' column:")
print(df)

# 3. Filtering data (e.g., finding employees from New York)
ny_employees = df[df['City'] == 'New York']
print("\nEmployees from New York:")
print(ny_employees)

# 4. Aggregating data (e.g., average salary by city)
average_salary = df.groupby('City')['Salary'].mean().reset_index()
print("\nAverage Salary by City:")
print(average_salary)

# 5. Filtering and aggregating (e.g., average salary of employees older than 25)
avg_salary_above_25 = df[df['Age'] > 25]['Salary'].mean()
print("\nAverage Salary of Employees Older than 25:", avg_salary_above_25)




