import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

input_file = DATA_DIR / "nfl_wr_raw_2022_2025.csv"
output_file = DATA_DIR / "nfl_wr_clean.csv"

df = pd.read_csv(input_file)

df = df[df["POS"] == "WR"].copy()

df["nfl_cc_rate"] = df["CTC"] / df["CTT"]
df.loc[df["CTT"] == 0, "nfl_cc_rate"] = None

df = df[
    [   "Player Id",
        "Name", "Team", "S", "POS",
        "TGT", "REC", "REC YDS", "REC TD",
        "CTT", "CTC", "nfl_cc_rate",
        "YAC", "YAC/REC"
    ]
].copy()

df.columns = [
"player_id",
    "player", "nfl_team", "nfl_season", "position",
    "nfl_targets", "nfl_receptions", "nfl_rec_yards", "nfl_rec_tds",
    "nfl_contested_targets", "nfl_contested_receptions", "nfl_cc_rate",
    "nfl_yac", "nfl_yac_per_rec"
]

df.to_csv(output_file, index=False)

print(df.head())
print(df.shape)
print(f"Saved to {output_file}")