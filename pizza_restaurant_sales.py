# -*- coding: utf-8 -*-
"""Pizza restaurant sales

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DmMc9Gq270xp7pm1nH6QM5wK_CKCKwUz
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

colors_dict = {
    "Red": "#8c0404",
    "Pink": "#f25ed0",
    "Black": "#000000",
    "Green": "#16A085",
    "Dark Blue": "#34495E",
    "Navy Blue": "#21618C",
    "Purple": "#512E5F",
    "Turquoise": "#45B39D",
    "Gray": "#AAB7B8",
    "Light Blue": "#20B2AA",
    "Hot Pink": "#FF69B4",
    "Dark Turquoise": "#00CED1",
    "Coral": "#FF7F50",
    "Lime": "#7FFF00",
    "Orchid": "#DA70D6"
}

df = pd.read_csv('pizza_sales.csv', encoding='latin1')
print(df)

"""## Exploratory Data Analysis (EDA)"""

df.info()

df.isna().sum()

df.duplicated().sum()

df.head()

df.describe()

# replace the abbreciations

df['pizza_size'] = df['pizza_size'].replace({'S' : 'Small', 'M' : 'Medium', 'L' : 'Large', 'XL' : 'X-Large', 'XXL' : 'XX-Large'})

# grouping by 'order_id' and summing the 'total_price' for each unique order

total_sales_per_order = df.groupby('order_id')['total_price'].sum().reset_index()
total_sales_per_order

"""## Data Visualization

1. What is the most selling pizza?
"""

top_5_sold_pizza = df.groupby('pizza_name')['total_price'].sum().nlargest(5).reset_index()
top_5_sold_pizza

top_5_types = df['pizza_name'].value_counts().head(5).index.tolist()

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='pizza_name', order=top_5_types ,color = colors_dict["Pink"] )
plt.xticks(rotation=90)
plt.title('Top 5 Pizza Names')
plt.xlabel('Pizza Type')
plt.ylabel('Count')

"""2. What is the most selling category?"""

df['pizza_category'].value_counts().plot(kind='pie', autopct="%0.1f%%")
plt.xlabel('Pizza Category')
plt.ylabel('Category Percentage')
plt.show()

"""3. Number of sales of each pizza size"""

sns.countplot(data =df , x= 'pizza_size' , color =colors_dict["Orchid"])
plt.title('Count of each pizza size')
plt.xlabel('pizza size')
plt.ylabel('pizza counts')

"""4. How is the distribution of total price by the category?"""

sns.countplot(data =df , x= 'pizza_category' , color =colors_dict["Orchid"])
plt.title('Count of each pizza category by price')
plt.xlabel('pizza size')
plt.ylabel('pizza counts')