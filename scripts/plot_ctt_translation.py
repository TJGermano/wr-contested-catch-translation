import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

input_file = DATA_DIR / "player_ccr_summary.csv"
output_file = OUTPUT_DIR / "college_vs_nfl_ct_per_season_scatter.png"

df = pd.read_csv(input_file)

# -----------------------
# Filters
# -----------------------
MIN_COLLEGE_CTT = 15
MIN_NFL_CTT = 10

plot_df = df[
    (df["college_contested_targets"] >= MIN_COLLEGE_CTT)
    & (df["nfl_contested_targets"] >= MIN_NFL_CTT)
    & (df["college_ct_per_season"].notna())
    & (df["nfl_ct_per_season"].notna())
].copy()

# -----------------------
# Correlation
# -----------------------
corr = plot_df["college_ct_per_season"].corr(
    plot_df["nfl_ct_per_season"]
)

print(f"Players included: {len(plot_df)}")
print(f"Correlation: {corr:.3f}")

# -----------------------
# Plot
# -----------------------
plt.figure(figsize=(10, 7))

plt.scatter(
    plot_df["college_ct_per_season"],
    plot_df["nfl_ct_per_season"],
    s=plot_df["nfl_targets"] * 2,
    alpha=0.6
)

plt.xlabel("College Contested Targets Per Season")
plt.ylabel("NFL Contested Targets Per Season")
plt.title(
    "Do Contested Target Roles Persist from College to NFL?\n"
    f"Per Season | Min College CT: {MIN_COLLEGE_CTT}, Min NFL CT: {MIN_NFL_CTT}, Corr: {corr:.2f}"
)

plt.grid(True, alpha=0.3)

# Label biggest NFL contested-target-per-season players
label_df = plot_df.sort_values("nfl_ct_per_season", ascending=False).head(12)

for _, row in label_df.iterrows():
    plt.annotate(
        row["player"],
        (row["college_ct_per_season"], row["nfl_ct_per_season"]),
        fontsize=8,
        alpha=0.8
    )

plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Saved plot to {output_file}")
