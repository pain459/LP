import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import sys

def save_dataframe_as_image(df, filename='output.png'):
    # Create a figure and a plot
    fig, ax = plt.subplots(figsize=(12, 4))  # Adjust the size as needed
    ax.axis('off')
    ax.axis('tight')

    # Create a table from the DataFrame
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    # Save the plot as an image
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

# Database connection parameters
DB_TYPE = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_USER = 'your_username'
DB_PASS = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'your_database'

# Create the connection string
DATABASE_URI = f"{DB_TYPE}+{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create a database engine
engine = create_engine(DATABASE_URI)

# Load the query from the query.sql file
with open('query.sql', 'r') as file:
    query = file.read()

# Fetch data from the database into a DataFrame
df = pd.read_sql(query, engine)

# Display the DataFrame without the index column
print(df.to_string(index=False))

# Optional: Save the DataFrame as an image
if '--save-image' in sys.argv:
    save_dataframe_as_image(df)
    print("DataFrame saved as image: output.png")
