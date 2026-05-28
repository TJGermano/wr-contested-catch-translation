import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

input_file = DATA_DIR / "player_ccr_summary.csv"
output_file = OUTPUT_DIR / "college_vs_nfl_ccr_scatter.png"

df = pd.read_csv(input_file)

# -----------------------
# Filters
# -----------------------
MIN_COLLEGE_CTT = 15
MIN_NFL_CTT = 10

plot_df = df[
    (df["college_contested_targets"] >= MIN_COLLEGE_CTT)
    & (df["nfl_contested_targets"] >= MIN_NFL_CTT)
    & (df["college_cc_rate_weighted"].notna())
    & (df["nfl_cc_rate_weighted"].notna())
].copy()

# Convert rates to percentages
plot_df["college_cc_pct"] = plot_df["college_cc_rate_weighted"] * 100
plot_df["nfl_cc_pct"] = plot_df["nfl_cc_rate_weighted"] * 100

# -----------------------
# Basic correlation
# -----------------------
corr = plot_df["college_cc_pct"].corr(plot_df["nfl_cc_pct"])

print(f"Players included: {len(plot_df)}")
print(f"Correlation: {corr:.3f}")

# -----------------------
# Plot
# -----------------------
plt.figure(figsize=(10, 7))

plt.scatter(
    plot_df["college_cc_pct"],
    plot_df["nfl_cc_pct"],
    s=plot_df["nfl_contested_targets"] * 5,
    alpha=0.6
)

plt.xlabel("College Contested Catch Rate (%)")
plt.ylabel("NFL Contested Catch Rate (%)")
plt.title(
    "Does Contested Catch Ability Persist from College to NFL?\n"
    f"Min College CTT: {MIN_COLLEGE_CTT}, Min NFL CTT: {MIN_NFL_CTT}, Corr: {corr:.2f}"
)

plt.grid(True, alpha=0.3)

# Label top NFL contested-target players
label_df = plot_df.sort_values("nfl_contested_targets", ascending=False).head(12)

for _, row in label_df.iterrows():
    plt.annotate(
        row["player"],
        (row["college_cc_pct"], row["nfl_cc_pct"]),
        fontsize=8,
        alpha=0.8
    )

plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Saved plot to {output_file}")