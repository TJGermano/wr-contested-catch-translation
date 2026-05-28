import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

college_file = DATA_DIR / "college_ccr_dataset.csv"
nfl_file = DATA_DIR / "nfl_ccr_dataset.csv"
output_file = DATA_DIR / "player_ccr_summary.csv"

college = pd.read_csv(college_file)
nfl = pd.read_csv(nfl_file)

# -----------------------
# College player summary
# -----------------------
college_summary = (
    college.groupby(["player_id", "player"])
    .agg(
        college_seasons=("college_season", "nunique"),
        first_college_season=("college_season", "min"),
        last_college_season=("college_season", "max"),
        college_targets=("college_targets", "sum"),
        college_receptions=("college_receptions", "sum"),
        college_rec_yards=("college_rec_yards", "sum"),
        college_rec_tds=("college_rec_tds", "sum"),
        college_contested_targets=("college_contested_targets", "sum"),
        college_contested_receptions=("college_contested_receptions", "sum"),
    )
    .reset_index()
)

college_summary["college_cc_rate_weighted"] = (
    college_summary["college_contested_receptions"]
    / college_summary["college_contested_targets"]
)

college_summary.loc[
    college_summary["college_contested_targets"] == 0,
    "college_cc_rate_weighted"
] = None

# --------------------
# NFL player summary
# --------------------
nfl_summary = (
    nfl.groupby(["player_id", "player"])
    .agg(
        nfl_seasons=("nfl_season", "nunique"),
        first_nfl_season=("nfl_season", "min"),
        last_nfl_season=("nfl_season", "max"),
        nfl_targets=("nfl_targets", "sum"),
        nfl_receptions=("nfl_receptions", "sum"),
        nfl_rec_yards=("nfl_rec_yards", "sum"),
        nfl_rec_tds=("nfl_rec_tds", "sum"),
        nfl_contested_targets=("nfl_contested_targets", "sum"),
        nfl_contested_receptions=("nfl_contested_receptions", "sum"),
    )
    .reset_index()
)

nfl_summary["nfl_cc_rate_weighted"] = (
    nfl_summary["nfl_contested_receptions"]
    / nfl_summary["nfl_contested_targets"]
)

nfl_summary.loc[
    nfl_summary["nfl_contested_targets"] == 0,
    "nfl_cc_rate_weighted"
] = None

# --------------------
# Join summaries
# --------------------
summary = college_summary.merge(
    nfl_summary,
    on="player_id",
    how="inner",
    suffixes=("_college", "_nfl")
)

# Clean player name
summary["player"] = summary["player_college"].fillna(summary["player_nfl"])

# Reorder columns
summary = summary[
    [
        "player_id",
        "player",
        "college_seasons",
        "first_college_season",
        "last_college_season",
        "college_targets",
        "college_receptions",
        "college_rec_yards",
        "college_rec_tds",
        "college_contested_targets",
        "college_contested_receptions",
        "college_cc_rate_weighted",
        "nfl_seasons",
        "first_nfl_season",
        "last_nfl_season",
        "nfl_targets",
        "nfl_receptions",
        "nfl_rec_yards",
        "nfl_rec_tds",
        "nfl_contested_targets",
        "nfl_contested_receptions",
        "nfl_cc_rate_weighted",
    ]
]

summary.to_csv(output_file, index=False)

print(summary.head())
print(summary.shape)
print(f"Saved to {output_file}")