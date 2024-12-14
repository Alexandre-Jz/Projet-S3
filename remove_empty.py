import pandas as pd

def find_non_empty_rows(file_path, column_name):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Filter rows where the specified column is NOT empty
    non_empty_rows = df[df[column_name].notna()]  # Keeps rows where column_name is not NaN

    # Print and return the non-empty rows
    print(non_empty_rows)
    return non_empty_rows

# Usage example:
file_path = "donnees_arbre.xlsx"  # Replace with your Excel file path
column_name = "Nombre de chemin trouve"      # Replace with the column header you want to check
non_empty_data = find_non_empty_rows(file_path, column_name)

# Save the non-empty rows to a new Excel file if needed
non_empty_data.to_excel("non_empty_rows.xlsx", index=False)
