"""SUSE Linux Enterprise Scraper (Fixed rowspan and colspan handling)"""

# Import required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Setup Chrome WebDriver with headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the Wikipedia page
driver.get("https://en.wikipedia.org/wiki/SUSE_Linux_Enterprise")
time.sleep(2)

# Find all tables on the page
tables = driver.find_elements(By.XPATH, "//table")
























































# Function to extract table data while handling rowspan and colspan
def extract_table(table):
    rows = table.find_elements(By.XPATH, ".//tr")
    table_data = []
    rowspan_tracker = {}  # Dictionary to track rowspan data
    
    for row_index, row in enumerate(rows):
        row_data = []
        col_index = 0  # Column index tracker

        cells = row.find_elements(By.XPATH, ".//th | .//td")
        
        for cell in cells:
            # Handle 'rowspan'
            rowspan = int(cell.get_attribute("rowspan") or 1)
            colspan = int(cell.get_attribute("colspan") or 1)
            cell_text = cell.text.strip()
            
            # Fill previous row data if rowspan exists
            while col_index in rowspan_tracker:
                row_data.append(rowspan_tracker[col_index])
                rowspan_tracker[col_index] -= 1  # Decrease remaining rowspan count
                if rowspan_tracker[col_index] == 0:
                    del rowspan_tracker[col_index]  # Remove fully used rowspan cell
                col_index += 1  # Move to next column

            # Add the current cell data
            row_data.append(cell_text)
            
            # Store rowspan data if needed
            if rowspan > 1:
                rowspan_tracker[col_index] = rowspan - 1  # Store remaining rows to be filled
            
            # Handle 'colspan' (Extend data across multiple columns)
            for _ in range(colspan - 1):
                row_data.append(cell_text)  # Duplicate the text across colspan
                col_index += 1  # Move to the next column

            col_index += 1  # Move to the next column

        # Fill in any remaining rowspan data
        while col_index in rowspan_tracker:
            row_data.append(rowspan_tracker[col_index])
            rowspan_tracker[col_index] -= 1
            if rowspan_tracker[col_index] == 0:
                del rowspan_tracker[col_index]
            col_index += 1

        table_data.append(row_data)

    # Normalize the table (Ensure all rows have equal columns)
    max_cols = max(len(row) for row in table_data)
    for row in table_data:
        while len(row) < max_cols:
            row.append("")  # Fill missing columns with empty values

    # Convert to DataFrame
    df = pd.DataFrame(table_data[1:], columns=table_data[0]) if len(table_data) > 1 else pd.DataFrame(table_data)
    
    return df

# Extract tables and handle rowspan/colspan issues
df_table_1 = extract_table(tables[0])
df_table_2 = extract_table(tables[1])
df_table_3 = extract_table(tables[2])

# Save the DataFrames to CSV files
df_table_1.to_csv("table1.csv", index=False, encoding="utf-8-sig")
df_table_2.to_csv("table2.csv", index=False, encoding="utf-8-sig")
df_table_3.to_csv("table3.csv", index=False, encoding="utf-8-sig")

# Print DataFrames (if needed)
print("Table 1:")
print(df_table_1)
print("\nTable 2:")
print(df_table_2)
print("\nTable 3:")
print(df_table_3)

# Close the browser
driver.quit()
