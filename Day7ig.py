import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
d = np.array([[1, 3, 5], [7, 7, 8], [3, 6, 8]])
# why do we convert a list into a 2D array ******************************************
# print(np.shape([1,2,3,4]))
# print(np.shape([[1,2,3,4]]))
# we do this to perform matrix operations dot, cartesian ...(math), Many ML functions expect 2D input (n_samples, n_features),
# print(c.shape)
# print(c.dtype)
# print(c.ndim)#no.of dimensions
#
# np.zeros((1,2))
# np.ones((2,1))
# print(np.full((100,100),2))

# print(np.arange(10))
# print(np.arange(2,10,2))

# print(np.arange(3,9,3))
# print(np.linspace(0, 1, 5))
# print(np.random.rand(4,4))
# z = c+d
# print(z)
# print(np.mean(z))
# print(np.max(z))
# print(np.min(z))
# print(np.sum(z))
# print(np.sin(z))
# print(np.tan(z))
# print(z.size)

# np.zeros((3, 4))
# np.ones((2, 2))
# np.arange(0, 10, 2)
# np.linspace(0, 1, 5)
# np.eye(3)
#
# print(a.shape)  # dimensions
# print(a.ndim)  # number of axes
# print(a.size)  # total elements
# print(a.dtype)  # data type
# print(a.itemsize)  # bytes per element
# print("____+++++______+++++______")
# print(b.shape)  # dimensions
# print(b.ndim)  # number of axes
# print(b.size)  # total elements
# print(b.dtype)  # data type
# print(b.itemsize)

# bag = np.full((3,10),90)

bag = np.random.rand(3, 10)
bagged = bag * 100
res = np.floor(bagged)
# print(res)

scores = np.array([78, 85, 92, 70, 88, 94, 67, 73, 82, 90,
                   76, 84, 95, 69, 80, 87, 91, 77, 83, 86,
                   79, 81, 89, 72, 68, 93, 74, 75, 96, 88])

# avg = np.std(scores)
# avg = np.round(avg) #average, max. min, sum, std
# print(avg)

# print(scores[scores > np.mean(scores)])  # greater than average.

# why we use numpy, use the sales dataset and see what can be done to each columns in the dataset. ************************************
#Python lists are flexible but slow for large-scale numeric computations.

# dim_sale['Price'] = dim_sale['Price'].apply(clean_price)
# dim_sale['Price'] = dim_sale.groupby('category_id')['Price'].transform(
#     lambda x: x.fillna(x[x > 0].mean())
# )

# Convert grades to numerical scores
# grade_map = {'A+': 4.3, 'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
# numeric_grades = df['grade'].map(grade_map).values
#
# # NumPy statistics
# mean_gpa = np.mean(numeric_grades)
# std_gpa = np.std(numeric_grades)
# median_gpa = np.median(numeric_grades)
#
# # Grade distribution percentiles
# percentiles = np.percentile(numeric_grades, [25, 50, 75])


# Sales by date
# date_sales = sales_df.groupby('date_id')['total_amount'].sum().values
#
# # Moving average using NumPy
# window = 3
# moving_avg = np.convolve(date_sales, np.ones(window)/window, mode='valid')
#
# # Growth rate
# growth_rates = np.diff(date_sales) / date_sales[:-1] * 100
