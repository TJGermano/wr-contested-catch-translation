import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

college = pd.read_csv(DATA_DIR / "college_wr_clean.csv")
nfl = pd.read_csv(DATA_DIR / "nfl_wr_clean.csv")

# -----------------------
# 1. College CCR dataset
# -----------------------
college_ccr = college.copy()

# For now, keep every player-season.
# Later we can filter to final college season only after joining draft data.
college_ccr = college_ccr[
    [
        "player_id",
        "player",
        "college_team",
        "college_season",
        "college_targets",
        "college_contested_targets",
        "college_contested_receptions",
        "college_cc_rate",
        "college_receptions",
        "college_rec_yards",
        "college_rec_tds",
        "college_yac",
        "college_yac_per_rec",
    ]
]

college_ccr.to_csv(DATA_DIR / "college_ccr_dataset.csv", index=False)

# --------------------
# 2. NFL CCR dataset
# --------------------
nfl_ccr = nfl[
    [
        "player_id",
        "player",
        "nfl_team",
        "nfl_season",
        "nfl_targets",
        "nfl_contested_targets",
        "nfl_contested_receptions",
        "nfl_cc_rate",
        "nfl_receptions",
        "nfl_rec_yards",
        "nfl_rec_tds",
        "nfl_yac",
        "nfl_yac_per_rec",
    ]
].copy()

nfl_ccr.to_csv(DATA_DIR / "nfl_ccr_dataset.csv", index=False)

print("College CCR dataset:", college_ccr.shape)
print("NFL CCR dataset:", nfl_ccr.shape)
print("Saved college_ccr_dataset.csv and nfl_ccr_dataset.csv")