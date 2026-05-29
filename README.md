# WR Contested Catch Translation Study

## Overview

This project explores whether contested catch ability translates from college football to the NFL using PFF charting data and player-level receiving metrics.

The study was motivated by a common scouting belief that receivers who consistently win in contested situations in college should continue to demonstrate similar success at the NFL level.

Using player-level data from college and NFL receiving datasets, this project examines whether contested catch efficiency persists across levels and whether contested catch metrics provide meaningful predictive value when evaluated in isolation.

---

## Research Question

Does contested catch ability translate from college football to the NFL?

More specifically:

1. Does contested catch efficiency persist from college to the NFL?
2. Is contested catch rate a translatable standalone receiver trait?
3. Can contested catch production be used as a meaningful projection tool without additional contextual variables?

---

## Data

Data was sourced from PFF charting data and includes:

* College WR data (2021–2024)
* NFL WR data (2022–2025)

Metrics used:

* Contested Targets
* Contested Receptions
* Contested Catch Rate (CCR)
* Receiving Production
* Season-Level Receiving Statistics
* Player-Level Aggregated Statistics

---

## Methodology

### Data Pipeline

The project was built entirely in Python using:

* pandas
* matplotlib

Workflow:

1. Raw college and NFL WR data exports
2. Data cleaning and normalization
3. Player matching using Player ID
4. Construction of player-level comparison datasets
5. Aggregation of contested catch metrics across available seasons
6. Scatter plot analysis and correlation testing
7. Top-10 leaderboard comparisons and exploratory analysis

---

## CCR Translation Analysis

![CCR Translation](Charts/College%20V%20NFL%20CCR%20(1).png)

### Finding

College contested catch rate showed virtually no relationship to NFL contested catch rate.

**Correlation: -0.03**

Receivers who posted strong contested catch efficiency in college did not consistently demonstrate similar contested catch efficiency in the NFL.

The findings suggest that contested catch rate alone may not be a strongly translatable standalone trait when projecting wide receiver performance across levels.

---

## Interpretation

One possible explanation is that contested catch production is heavily influenced by contextual factors beyond the receiver's ball skills, including:

* Offensive structure
* Quarterback tendencies
* Route profile
* Receiver role
* Defensive competition
* Separation ability

As a result, contested catch rate may reflect surrounding circumstances as much as individual receiver skill.

---

## Limitations

This project is exploratory in nature and should not be interpreted as a definitive player evaluation model.

Several important variables were intentionally excluded:

* Separation metrics
* Height and weight
* Draft capital
* Alignment data
* Route tree information
* Quarterback aggressiveness
* Target quality
* Target share
* Coverage tendencies

Additionally:

* Contested catch charting is dependent on PFF definitions and methodology.
* Contested catch opportunities are relatively rare events, creating small-sample volatility.
* The final filtered sample contained approximately 50–70 qualifying receivers depending on thresholds applied.

---

## Future Work

Potential future expansions include:

* Contested target volume translation
* Career-length normalization
* Per-season usage analysis
* Athletic testing data
* Draft capital integration
* Receiver archetype comparisons
* Separation metrics
* Role-based translation analysis
* Predictive clustering models

A current area of investigation is whether contested target volume persists across levels after controlling for differences in career length and available NFL seasons.

---

## Repository Structure

```text
data/
outputs/
scripts/
charts/
```

---

## Author

Thomas Germano

MS Sports Management Candidate — Columbia University

Football Operations & Analytics
