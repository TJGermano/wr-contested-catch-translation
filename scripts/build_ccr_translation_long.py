import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

college_file = DATA_DIR / "college_ccr_dataset.csv"
nfl_file = DATA_DIR / "nfl_ccr_dataset.csv"
output_file = DATA_DIR / "ccr_translation_long.csv"

college = pd.read_csv(college_file)
nfl = pd.read_csv(nfl_file)

# Make seasons numeric
college["college_season"] = pd.to_numeric(college["college_season"], errors="coerce")
nfl["nfl_season"] = pd.to_numeric(nfl["nfl_season"], errors="coerce")

# Join every college player-season to every NFL player-season for same player
master = college.merge(
    nfl,
    on="player_id",
    how="inner",
    suffixes=("_college", "_nfl")
)

# Keep only NFL seasons after the college season
master = master[master["nfl_season"] > master["college_season"]].copy()

# Add timing variable
master["years_after_college"] = master["nfl_season"] - master["college_season"]

# Clean duplicated player name columns
if "player_college" in master.columns:
    master["player"] = master["player_college"]
elif "player" not in master.columns and "player_nfl" in master.columns:
    master["player"] = master["player_nfl"]

# Reorder useful columns
keep_cols = [
    "player_id",
    "player",
    "college_team",
    "college_season",
    "college_targets",
    "college_contested_targets",
    "college_contested_receptions",
    "college_cc_rate",
    "nfl_team",
    "nfl_season",
    "years_after_college",
    "nfl_targets",
    "nfl_contested_targets",
    "nfl_contested_receptions",
    "nfl_cc_rate",
    "nfl_receptions",
    "nfl_rec_yards",
    "nfl_rec_tds",
]

# Keep only columns that exist, just in case
master = master[[col for col in keep_cols if col in master.columns]]

master.to_csv(output_file, index=False)

print(master.head())
print(master.shape)
print(f"Saved to {output_file}")