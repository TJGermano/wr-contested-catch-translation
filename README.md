# wr-contested-catch-translation
Exploratory football analytics study analyzing whether contested catch ability translates from college football to the NFL using PFF charting data.
# WR Contested Catch Translation Study

## Overview

This project explores whether contested catch ability translates from college football to the NFL.

Using PFF receiving data from 2021–2025, the study analyzes:

* Contested Catch Rate (CCR)
* Contested Target Volume
* Player-level contested usage
* Season-level contested usage
* College-to-NFL metric persistence

The original hypothesis was that wide receivers with strong contested catch production in college would continue to demonstrate similar contested catch success in the NFL.

Initial findings showed limited direct relationship between:

* College CCR and NFL CCR
* College contested target volume and NFL contested target volume

The results suggest contested environments may be significantly more context-dependent than commonly assumed.

---

## Key Questions

This project attempted to answer:

1. Does contested catch efficiency persist from college to the NFL?
2. Do receivers who operate in high contested-target environments in college continue to occupy those roles in the NFL?
3. Is high contested catch usage potentially more reflective of separation limitations than a translatable standalone skill?

---

## Data

Data was sourced from PFF charting data and includes:

* College WR data (2021–2024)
* NFL WR data (2022–2025)

Metrics used:

* Contested targets
* Contested receptions
* Contested catch rate
* Receiving production
* Season-level and player-level aggregates

---

## Methodology

### Data Pipeline

The project was built entirely in Python using:

* pandas
* matplotlib

Workflow:

1. Raw college and NFL WR data exports
2. Data cleaning and normalization
3. Player-level joins using Player ID
4. Construction of:

   * Long-form translation datasets
   * Aggregated player summary datasets
5. Scatter plot analysis
6. Top-10 leaderboards and exploratory comparisons

---

## Key Findings

### 1. Limited Relationship Between College and NFL CCR

Initial scatter plot analysis showed almost no linear relationship between:

* College contested catch rate
* NFL contested catch rate

Correlation values were near zero, suggesting contested catch efficiency alone may not strongly persist across levels.

---

### 2. Limited Relationship Between College and NFL Contested Target Volume

Receivers with extremely high contested target volume in college did not consistently maintain similar contested usage in the NFL.

This may suggest:

* NFL role changes
* Increased athletic competition
* Better NFL coverage
* Greater importance of separation ability
* Offensive/QB context dependence

---

### 3. Contested Environments May Be Context-Driven

The analysis suggests contested catch metrics may reflect:

* offensive structure
* quarterback tendencies
* route profile
* receiver role
* inability to consistently separate

rather than functioning as a fully isolated translatable WR skill.

---

## Important Caveats

This project intentionally isolated contested catch metrics only.

The analysis does NOT currently include:

* Separation metrics
* Height/weight
* Draft capital
* Alignment data
* Route tree information
* QB aggressiveness
* Target share
* Man/zone coverage splits

Future iterations could incorporate these variables to better understand *when* contested catch ability translates successfully.

Additionally, contested catch charting is dependent on PFF definitions and tracking methodology.

## Limitations

This project is exploratory in nature and should not be interpreted as a definitive evaluation model.

The final filtered sample size for many analyses was relatively small due to:
- limited contested target volume
- players not yet reaching the NFL
- threshold filtering to remove noisy observations
- limited NFL sample years

As a result, many visualizations included roughly 50–70 qualifying receivers depending on the filters applied.

Contested catch data is inherently sparse.

Many receivers accumulate relatively few contested targets across a season, making contested catch efficiency highly sensitive to small-sample variation.

Additionally, this study intentionally isolated contested catch metrics only and did not control for:
- separation ability
- offensive structure
- quarterback play
- target quality
- route tree
- draft capital
- athletic profile
---

## Future Work

Potential future expansions:

* Add athletic testing data
* Add draft capital
* Compare WR archetypes
* Incorporate separation metrics
* Analyze role-based translation
* Build predictive clustering models
* Compare contested catch skill vs separation-based efficiency

---

## Repository Structure

```text
data/
outputs/
scripts/
charts/
portfolio/
```

---

## Author

Thomas Germano
MS Sports Management Candidate — Columbia University
Football Operations & Analytics
