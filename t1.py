# %%
import pandas as pd
from datetime import datetime

print(f"🟢 Rerun at: {datetime.now()}")

DATA_PATH = "./data/resale_data.csv"

# df = pd.read_csv(DATA_PATH)
# Convert the 'month' column to datetime format because it is read as object/string by default
# If the data had been cleaned earlier, this step might not be necessary
# df["month"] = pd.to_datetime(df["month"])

def load_data(path):
    df = pd.read_csv(path)
    df["month"] = pd.to_datetime(df["month"])
    return df

df = load_data(DATA_PATH)

# %%
import plotly.express as px
# df_town = df.groupby("town", as_index=False)["resale_price"].mean().sort_values("resale_price")
df_town = df.groupby("town", as_index=False)["resale_price"].mean().head(5)

# Create a Plotly bar chart with towns on x-axis and average resale price on y-axis
fig_town = px.bar(df_town, x="town", y="resale_price",
                  labels={"resale_price": "Average Resale Price", "town": "Town"},
                  title="Average Resale Price by Town in Singapore",
                  height=500)
fig_town.show()

# %%

# %%
i = 10
with i:
    print("Hello, World!")
    