import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Read the CSV file 'apps.csv' into a pandas DataFrame named 'df_apps'
df_apps = pd.read_csv('apps.csv')

# Display basic information about the DataFrame
print("Basic information about the DataFrame:")
print(df_apps.info())

# Display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df_apps.head())

# Display summary statistics of the numeric columns
print("\nSummary statistics of the numeric columns:")
print(df_apps.describe())

# Group the data by Category and calculate the mean of each group (average rating per category)
average_rating_by_category = df_apps.groupby('Category')['Rating'].mean()

# Display the average ratings by category
print("\nAverage Ratings by Category:")
print(average_rating_by_category)

# Create a circular donut chart using matplotlib to visualize the average ratings by category
plt.figure(figsize=(10, 6))
plt.pie(average_rating_by_category, labels=average_rating_by_category.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))
plt.title('Average Ratings by Category (Donut Chart)')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.tight_layout()

# Show the matplotlib plot
plt.show()

# Create a pie chart using Plotly to visualize the average ratings by category
fig = px.pie(labels=average_rating_by_category.index, values=average_rating_by_category.values, title="Average Ratings by Category")
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()
