import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

summary = pd.read_csv(DATA_DIR / "player_ccr_summary.csv")
college = pd.read_csv(DATA_DIR / "college_ccr_dataset.csv")
nfl = pd.read_csv(DATA_DIR / "nfl_ccr_dataset.csv")

# Thresholds to avoid tiny-sample nonsense
MIN_COLLEGE_CTT_PLAYER = 15
MIN_NFL_CTT_PLAYER = 10
MIN_COLLEGE_CTT_SEASON = 10
MIN_NFL_CTT_SEASON = 8

# -------------------------
# Player-level top 10s
# -------------------------

top_college_ccr_player = (
    summary[summary["college_contested_targets"] >= MIN_COLLEGE_CTT_PLAYER]
    .sort_values("college_cc_rate_weighted", ascending=False)
    .head(10)
    [[
        "player",
        "college_seasons",
        "college_contested_targets",
        "college_contested_receptions",
        "college_cc_rate_weighted",
    ]]
)

top_nfl_ccr_player = (
    summary[summary["nfl_contested_targets"] >= MIN_NFL_CTT_PLAYER]
    .sort_values("nfl_cc_rate_weighted", ascending=False)
    .head(10)
    [[
        "player",
        "nfl_seasons",
        "nfl_contested_targets",
        "nfl_contested_receptions",
        "nfl_cc_rate_weighted",
    ]]
)

top_college_ctt_player = (
    summary.sort_values("college_contested_targets", ascending=False)
    .head(10)
    [[
        "player",
        "college_seasons",
        "college_contested_targets",
        "college_contested_receptions",
        "college_cc_rate_weighted",
    ]]
)

top_nfl_ctt_player = (
    summary.sort_values("nfl_contested_targets", ascending=False)
    .head(10)
    [[
        "player",
        "nfl_seasons",
        "nfl_contested_targets",
        "nfl_contested_receptions",
        "nfl_cc_rate_weighted",
    ]]
)

# -------------------------
# Single-season top 10s
# -------------------------

top_college_ccr_season = (
    college[college["college_contested_targets"] >= MIN_COLLEGE_CTT_SEASON]
    .sort_values("college_cc_rate", ascending=False)
    .head(10)
    [[
        "player",
        "college_team",
        "college_season",
        "college_contested_targets",
        "college_contested_receptions",
        "college_cc_rate",
    ]]
)

top_nfl_ccr_season = (
    nfl[nfl["nfl_contested_targets"] >= MIN_NFL_CTT_SEASON]
    .sort_values("nfl_cc_rate", ascending=False)
    .head(10)
    [[
        "player",
        "nfl_team",
        "nfl_season",
        "nfl_contested_targets",
        "nfl_contested_receptions",
        "nfl_cc_rate",
    ]]
)

top_college_ctt_season = (
    college.sort_values("college_contested_targets", ascending=False)
    .head(10)
    [[
        "player",
        "college_team",
        "college_season",
        "college_contested_targets",
        "college_contested_receptions",
        "college_cc_rate",
    ]]
)

top_nfl_ctt_season = (
    nfl.sort_values("nfl_contested_targets", ascending=False)
    .head(10)
    [[
        "player",
        "nfl_team",
        "nfl_season",
        "nfl_contested_targets",
        "nfl_contested_receptions",
        "nfl_cc_rate",
    ]]
)

# -------------------------
# Format percentages
# -------------------------

tables = {
    "top_college_ccr_player": top_college_ccr_player,
    "top_nfl_ccr_player": top_nfl_ccr_player,
    "top_college_ctt_player": top_college_ctt_player,
    "top_nfl_ctt_player": top_nfl_ctt_player,
    "top_college_ccr_season": top_college_ccr_season,
    "top_nfl_ccr_season": top_nfl_ccr_season,
    "top_college_ctt_season": top_college_ctt_season,
    "top_nfl_ctt_season": top_nfl_ctt_season,
}

for name, table in tables.items():
    for col in table.columns:
        if "cc_rate" in col:
            table[col] = (table[col] * 100).round(1)

# -------------------------
# Save outputs
# -------------------------

with pd.ExcelWriter(OUTPUT_DIR / "top_10_ccr_outputs.xlsx") as writer:
    for name, table in tables.items():
        table.to_excel(writer, sheet_name=name[:31], index=False)

for name, table in tables.items():
    table.to_csv(OUTPUT_DIR / f"{name}.csv", index=False)

# Print to console
for name, table in tables.items():
    print("\n" + "=" * 80)
    print(name)
    print("=" * 80)
    print(table.to_string(index=False))

print("\nSaved Excel workbook and CSVs to outputs/")