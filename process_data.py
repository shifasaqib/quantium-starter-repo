import pandas as pd
import glob

# Step 1: Load all CSV files from data folder
files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)
    all_data.append(df)

# Step 2: Combine all CSVs
combined_df = pd.concat(all_data, ignore_index=True)

# Step 3: Keep only Pink Morsels (ignore case and strip spaces)
combined_df['product'] = combined_df['product'].astype(str)  # ensure it's string
pink_df = combined_df[combined_df["product"].str.strip().str.lower() == "pink morsel"]

# Step 4: Create sales column (numeric)
# Remove $ sign if present and convert to float
pink_df['price'] = pink_df['price'].replace('[\$,]', '', regex=True).astype(float)
pink_df['quantity'] = pink_df['quantity'].astype(float)
pink_df["Sales"] = pink_df["quantity"] * pink_df["price"]

# Step 5: Keep only required columns
final_df = pink_df[["Sales", "date", "region"]]

# Step 6: Save formatted output
final_df.to_csv("formatted_output.csv", index=False)

print("Processing Complete ✅")
