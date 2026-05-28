import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

input_file = DATA_DIR / "player_ccr_summary.csv"
output_file = OUTPUT_DIR / "college_vs_nfl_ctt_scatter.png"

df = pd.read_csv(input_file)

# -----------------------
# Filters
# -----------------------
MIN_COLLEGE_CTT = 15
MIN_NFL_CTT = 10

plot_df = df[
    (df["college_contested_targets"] >= MIN_COLLEGE_CTT)
    & (df["nfl_contested_targets"] >= MIN_NFL_CTT)
].copy()

# -----------------------
# Correlation
# -----------------------
corr = plot_df["college_contested_targets"].corr(
    plot_df["nfl_contested_targets"]
)

print(f"Players included: {len(plot_df)}")
print(f"Correlation: {corr:.3f}")

# -----------------------
# Plot
# -----------------------
plt.figure(figsize=(10, 7))

plt.scatter(
    plot_df["college_contested_targets"],
    plot_df["nfl_contested_targets"],
    s=plot_df["nfl_targets"] * 2,
    alpha=0.6
)

plt.xlabel("College Contested Targets")
plt.ylabel("NFL Contested Targets")
plt.title(
    "Do Contested Target Roles Persist from College to NFL?\n"
    f"Min College CTT: {MIN_COLLEGE_CTT}, Min NFL CTT: {MIN_NFL_CTT}, Corr: {corr:.2f}"
)

plt.grid(True, alpha=0.3)

# Label biggest NFL volume players
label_df = plot_df.sort_values("nfl_contested_targets", ascending=False).head(12)

for _, row in label_df.iterrows():
    plt.annotate(
        row["player"],
        (row["college_contested_targets"], row["nfl_contested_targets"]),
        fontsize=8,
        alpha=0.8
    )

plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Saved plot to {output_file}")