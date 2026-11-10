import pandas as pd
import os

def clean_excel(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)

    print("Original data rows:", len(df))

    # Remove completely empty rows
    df = df.dropna(how='all')

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean column names (remove extra whitespace)
    df.columns = df.columns.str.strip()

    # Reset index
    df = df.reset_index(drop=True)

    # Save the cleaned file
    df.to_excel(output_file, index=False)

    print("Cleaned data rows:", len(df))
    print(f"File successfully saved: {output_file}")

# Provide your file names here
input_file = "dirty_data.xlsx"      # Name of your raw file
output_file = "cleaned_data.xlsx"   # Name of the cleaned file

if os.path.exists(input_file):
    clean_excel(input_file, output_file)
else:
    print("File not found. Please check the correct file name.")
