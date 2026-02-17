import pandas as pd
import glob

# Get all CSV files from data folder
files = glob.glob("data/*.csv")

# Create empty list to store data
all_data = []

for file in files:
    df = pd.read_csv(file)
    all_data.append(df)

# Combine all files into one dataframe
combined_df = pd.concat(all_data)

# Keep only Pink Morsels
pink_df = combined_df[combined_df["product"] == "pink morsel"]

# Create sales column
pink_df["Sales"] = pink_df["quantity"] * pink_df["price"]

# Keep only required columns
final_df = pink_df[["Sales", "date", "region"]]

# Save final output
final_df.to_csv("formatted_output.csv", index=False)

print("Processing Complete ✅")
