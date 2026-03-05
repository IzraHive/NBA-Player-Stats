# Overview

AI Disclosure: AI assistance (Claude) was used to help improve grammar and ensure best practices in data analysis workflows. All analytical logic, code structure, question formulation, and interpretation of results represent original work.

As a software engineer expanding my data analysis capabilities, I developed this Python-based analytical tool to explore NBA player performance patterns and team offensive strategies. This project allows me to apply statistical programming concepts while working with real-world sports data—combining my interests in technology and basketball analytics.

The dataset I'm analyzing contains comprehensive NBA player statistics spanning from the 1997-98 season through the 2021-22 season (25 years of data), including metrics like points scored, games played, field goal percentages, rebounds, assists, and more. I obtained this data from [Kaggle - NBA Player Stats](https://www.kaggle.com/datasets/raunakpandey030/nba-player-stats?resource=download&select=NBA_Player_Stats.csv). The dataset includes player-level data across different teams and seasons, enabling deep analysis of individual and team performance trends across different eras of basketball.

**Dataset Source:** [Kaggle - NBA Player Stats](https://www.kaggle.com/datasets/raunakpandey030/nba-player-stats?resource=download&select=NBA_Player_Stats.csv)
**Data Format:** CSV with 31 columns including player demographics, team affiliations, and comprehensive performance metrics

I created this software to answer critical questions about NBA performance:
1. **Who are the top scoring players in NBA history (by total points in a season)?**
2. **Which teams demonstrate the strongest offensive performance based on average points per game per player?**

By developing this analytical tool, I'm strengthening my skills in data manipulation with Pandas, statistical analysis, and data visualization with Matplotlib—all essential capabilities for modern software engineering roles involving data-driven decision making.

## Quick Setup (Run from Clean Clone)

```bash
# Clone the repository
git clone https://github.com/IzraHive/CSE310_NBA_Stats_Analysis.git
cd CSE310_NBA_Stats_Analysis

# Install required libraries
# On Windows, if 'pip' is not recognized, use:
python -m pip install pandas matplotlib numpy

# On Mac/Linux, you can use:
pip install pandas matplotlib numpy

# Run the analysis
python analysis.py
```

**Requirements:**
- Python 3.7 or higher
- Libraries: pandas, matplotlib, numpy
- The `data/NBA_Player_Stats.csv` file must be in the data directory

**Windows Users:** If you get "pip is not recognized" error, always use `python -m pip` instead of just `pip`.

**Output:**
- Console output with analysis results spanning 1997-98 through 2021-22 seasons
- `team_performance.png` - Bar chart visualization saved in project root

[Software Demo Video](https://youtu.be/bc_mlnQQ3Dg)

# Data Analysis Results

## Question 1: Top Scoring Players
**Analysis Method:** Filtered and sorted player data by total points (PTS) in descending order to identify the highest-scoring individual seasons.

**Key Findings:**
- The analysis reveals the most dominant individual scoring seasons in NBA history
- The top 10 scorers demonstrate exceptional offensive production, with point totals significantly above league averages
- These elite performances often correlate with high games played (G) and minutes per game (MP), showing consistency throughout the season
- The data shows that scoring leaders typically come from teams with offensive-focused strategies

**Example Results (Top 3):**
1. Multiple players have achieved 2,000+ point seasons, representing elite scoring efficiency
2. The gap between #1 and #10 highlights the rarity of truly exceptional scoring seasons
3. Historical context shows scoring trends have evolved with rule changes and play styles

## Question 2: Team Offensive Performance
**Analysis Method:** Aggregated player data by team (Tm), calculated average points per game (PPG) for each player, then averaged across all players on each team to measure overall team offensive strength.

**Key Findings:**
- Teams with higher average PPG per player indicate deeper offensive rosters and more balanced scoring
- The data reveals significant variation between teams, suggesting different strategic approaches (star-focused vs. balanced offense)
- Top-performing teams average considerably higher PPG per player than bottom-tier teams
- This metric accounts for roster depth—teams with multiple scoring threats rank higher

**Statistical Insights:**
- Highest scoring team demonstrates strong offensive culture and player development
- The distribution shows most teams cluster around league average with outliers on both ends
- Teams with very low averages often feature defensive-oriented strategies or developmental rosters

## Stretch Challenge: Data Visualization
Created an interactive bar chart (`team_performance.png`) that visualizes the top 20 teams by average PPG per player. The chart includes:
- Color-coded bars for easy comparison
- Value labels on each bar for precise reading
- Sorted display from highest to lowest performing teams
- Grid lines for easier value estimation

This visualization makes it immediately clear which teams prioritize offensive production and reveals the competitive gaps between top and bottom performers.

# Development Environment

I developed this project using VS Code as my primary editor with the Python extension for syntax highlighting and debugging. The project uses Python 3.x with three key libraries: Pandas for data manipulation (loading CSV, filtering, sorting, grouping), Matplotlib for creating the bar chart visualization, and NumPy as a dependency for numerical operations.

**Tools:**
- VS Code with Python extension
- Python 3.14.2 (or 3.7+)
- Git/GitHub for version control

**Libraries:**
- Pandas 2.x - Data loading, cleaning, filtering, sorting, and aggregation
- Matplotlib 3.x - Data visualization and chart generation
- NumPy - Numerical computing support

**Installation:**
```bash
# Windows (if pip is not recognized):
python -m pip install pandas matplotlib numpy

# Mac/Linux:
pip install pandas matplotlib numpy
```

# Useful Websites

These resources were invaluable during development:

* [Pandas Documentation](https://pandas.pydata.org/docs/) - Essential for understanding DataFrame operations and groupby aggregations
* [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) - Helped me design the bar chart visualization
* [Basketball Reference](https://www.basketball-reference.com/) - Source for understanding NBA statistics and data structure
* [Real Python - Pandas Tutorial](https://realpython.com/pandas-python-explore-dataset/) - Great for learning practical data analysis workflows

# Future Work

Things I want to add or improve:

* Expand analysis to include defensive statistics (steals, blocks, defensive rating) to get a complete picture of player value
* Add position-based filtering so I can compare players within their roles (PG vs PG, C vs C)
* Create time-series visualizations to see how scoring trends have evolved across different NBA eras
* Implement command-line arguments to let users specify custom filters without editing the code
* Build interactive charts using Plotly instead of static Matplotlib images

* Add correlation analysis to explore relationships between different stats (does higher usage correlate with lower efficiency?)
