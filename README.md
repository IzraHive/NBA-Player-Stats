# Overview

As a software engineer expanding my data analysis capabilities, I developed this Python-based analytical tool to explore NBA player performance patterns and team offensive strategies. This project allows me to apply statistical programming concepts while working with real-world sports data—combining my interests in technology and basketball analytics.

The dataset I'm analyzing contains comprehensive NBA player statistics spanning multiple seasons, including metrics like points scored, games played, field goal percentages, rebounds, assists, and more. I obtained this data from Basketball Reference, which provides extensive historical NBA statistics. The dataset includes player-level data across different teams and seasons, enabling deep analysis of individual and team performance.

**Dataset Source:** Basketball Reference NBA Player Statistics  
**Data Format:** CSV with 31 columns including player demographics, team affiliations, and comprehensive performance metrics

The purpose of this software is to answer critical questions about NBA performance:
1. **Who are the top scoring players in NBA history (by total points in a season)?**
2. **Which teams demonstrate the strongest offensive performance based on average points per game per player?**

By developing this analytical tool, I'm strengthening my skills in data manipulation with Pandas, statistical analysis, and data visualization with Matplotlib—all essential capabilities for modern software engineering roles involving data-driven decision making.

[Software Demo Video](http://youtube.link.goes.here)

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

**Development Tools:**
- **VS Code** - Primary code editor with Python extension
- **Python 3.x** - Programming language for analysis
- **Git/GitHub** - Version control and code repository hosting
- **Terminal/Command Line** - Script execution and package management

**Programming Language & Libraries:**
- **Python 3.x** - Core programming language chosen for its robust data science ecosystem
- **Pandas 2.x** - Data manipulation and analysis library for loading, cleaning, filtering, sorting, and aggregating the dataset
- **Matplotlib 3.x** - Data visualization library for creating publication-quality charts and graphs
- **NumPy** - Numerical computing library (dependency for Pandas calculations)

**Installation Commands:**
```bash
pip install pandas matplotlib numpy
```

# Useful Websites

* [Pandas Official Documentation](https://pandas.pydata.org/docs/) - Comprehensive guide for DataFrame operations, groupby aggregations, and data manipulation techniques
* [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) - Complete reference for creating visualizations, customizing plots, and chart formatting
* [Basketball Reference](https://www.basketball-reference.com/) - Primary source for NBA statistics and historical data
* [Kaggle NBA Datasets](https://www.kaggle.com/datasets?search=nba) - Alternative sources for NBA data and example analysis projects
* [Real Python - Pandas Tutorial](https://realpython.com/pandas-python-explore-dataset/) - Practical tutorials for data analysis workflows
* [Python Official Documentation](https://docs.python.org/3/) - Core Python language reference

# Future Work

**Data Analysis Enhancements:**
* Add analysis for additional performance metrics like Player Efficiency Rating (PER), True Shooting Percentage (TS%), or Win Shares
* Implement filtering by position (PG, SG, SF, PF, C) to compare players within their roles
* Create time-series analysis to track how scoring and team performance have evolved across different eras of basketball
* Add defensive statistics analysis (steals, blocks, defensive rating) to complement offensive metrics

**Technical Improvements:**
* Implement error handling for edge cases (empty datasets, malformed CSV files)
* Add command-line arguments to allow users to specify custom filters (year range, team, minimum games played)
* Create additional visualizations: scatter plots for PPG vs. shooting efficiency, heatmaps for team comparisons
* Optimize performance for larger datasets using chunking or parallel processing
* Export analysis results to formatted PDF reports

**Feature Additions:**
* Build an interactive web dashboard using Plotly or Streamlit for dynamic data exploration
* Add player comparison functionality to analyze head-to-head statistics
* Implement predictive modeling to forecast player performance based on historical trends
* Create correlation analysis between different stats (e.g., does higher usage rate correlate with lower efficiency?)