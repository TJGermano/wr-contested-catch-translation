import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

input_file = DATA_DIR / "college_wr_all_2021_2024.csv"
output_file = DATA_DIR / "college_wr_clean.csv"

df = pd.read_csv(input_file)

# Keep WR only, just in case
df = df[df["POS"] == "WR"].copy()

# Create contested catch rate
df["college_cc_rate"] = df["CTC"] / df["CTT"]
df.loc[df["CTT"] == 0, "college_cc_rate"] = None

# Keep useful columns
df = df[
    [
        "Player Id",
        "Name", "Team", "S", "POS",
        "TGT", "REC", "REC YDS", "REC TD",
        "CTT", "CTC", "college_cc_rate",
        "YAC", "YAC/REC"
    ]
].copy()

# Rename columns
df.columns = [
"player_id",
    "player", "college_team", "college_season", "position",
    "college_targets", "college_receptions", "college_rec_yards", "college_rec_tds",
    "college_contested_targets", "college_contested_receptions", "college_cc_rate",
    "college_yac", "college_yac_per_rec"
]

df.to_csv(output_file, index=False)

print(df.head())
print(df.shape)
print(f"Saved to {output_file}")