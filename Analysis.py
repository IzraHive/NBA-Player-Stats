# analysis.py
# NBA Player Stats Analysis - Module 2
# This program analyzes NBA player statistics to explore performance trends
# across players and teams from historical NBA seasons

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(filepath):
    """
    Load the NBA player statistics dataset from CSV file.
    
    Args:
        filepath: Path to the CSV file containing NBA stats
        
    Returns:
        DataFrame containing the loaded data
    """
    print("=" * 60)
    print("NBA PLAYER STATISTICS ANALYSIS")
    print("=" * 60)
    print("\nLoading dataset...")
    
    try:
        data = pd.read_csv(filepath)
        print(f"✓ Dataset loaded successfully!")
        print(f"✓ Total records: {len(data)}")
        print(f"✓ Total columns: {len(data.columns)}")
        return data
    except FileNotFoundError:
        print(f"✗ Error: File '{filepath}' not found!")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None


def preview_data(data):
    """
    Display a preview of the dataset structure and basic information.
    
    Args:
        data: DataFrame to preview
    """
    print("\n" + "-" * 60)
    print("DATASET PREVIEW")
    print("-" * 60)
    print("\nFirst 5 rows:")
    print(data.head())
    
    print("\nColumn names:")
    print(data.columns.tolist())
    
    print("\nData types:")
    print(data.dtypes)
    
    print("\nBasic statistics:")
    print(data.describe())


def clean_data(data):
    """
    Clean the dataset by handling missing values and converting data types.
    
    Args:
        data: DataFrame to clean
        
    Returns:
        Cleaned DataFrame
    """
    print("\n" + "-" * 60)
    print("DATA CLEANING")
    print("-" * 60)
    
    # Store original row count
    original_rows = len(data)
    
    # Drop rows with missing critical values (Player, Team, Points, Games)
    print("\nRemoving rows with missing critical data...")
    data = data.dropna(subset=['Player', 'Tm', 'PTS', 'G'])
    
    # Convert numeric columns to proper types
    numeric_columns = ['PTS', 'G', 'MP', 'TRB', 'AST', 'STL', 'BLK']
    for col in numeric_columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
    
    # Remove any rows where numeric conversion failed
    data = data.dropna(subset=['PTS'])
    
    rows_removed = original_rows - len(data)
    print(f"✓ Rows removed: {rows_removed}")
    print(f"✓ Remaining rows: {len(data)}")
    
    return data


def analyze_top_scorers(data, top_n=10):
    """
    Question 1: Which players scored the most points in a single season?
    
    This analysis identifies the top scorers by total points (PTS) in a season.
    We filter, sort, and display the top performers.
    
    Args:
        data: DataFrame containing player stats
        top_n: Number of top players to display
        
    Returns:
        DataFrame with top scorers
    """
    print("\n" + "=" * 60)
    print("QUESTION 1: TOP SCORING PLAYERS (BY TOTAL POINTS)")
    print("=" * 60)
    
    # Select relevant columns and sort by points
    top_scorers = data[['Player', 'Tm', 'Year', 'PTS', 'G', 'MP']].copy()
    
    # Sort by points in descending order
    top_scorers = top_scorers.sort_values(by='PTS', ascending=False)
    
    # Get top N players
    top_scorers = top_scorers.head(top_n)
    
    # Add a rank column
    top_scorers.insert(0, 'Rank', range(1, len(top_scorers) + 1))
    
    print(f"\nTop {top_n} Players by Total Points Scored:")
    print(top_scorers.to_string(index=False))
    
    # Calculate and display some insights
    avg_points = top_scorers['PTS'].mean()
    max_points = top_scorers['PTS'].max()
    min_points = top_scorers['PTS'].min()
    
    print(f"\nInsights:")
    print(f"  • Highest scoring season: {max_points:.1f} points")
    print(f"  • Average among top {top_n}: {avg_points:.1f} points")
    print(f"  • Lowest in top {top_n}: {min_points:.1f} points")
    
    return top_scorers


def analyze_team_performance(data):
    """
    Question 2: Which teams have the highest average points per game per player?
    
    This analysis aggregates player data by team to calculate average scoring
    and identify which teams had the most offensive production.
    
    Args:
        data: DataFrame containing player stats
        
    Returns:
        DataFrame with team averages
    """
    print("\n" + "=" * 60)
    print("QUESTION 2: TEAM OFFENSIVE PERFORMANCE")
    print("=" * 60)
    
    # Calculate average points per game for each player
    data['PPG'] = data['PTS'] / data['G']
    
    # Group by team and calculate average PPG
    team_stats = data.groupby('Tm').agg({
        'PPG': 'mean',
        'Player': 'count',
        'PTS': 'sum',
        'G': 'mean'
    }).reset_index()
    
    # Rename columns for clarity
    team_stats.columns = ['Team', 'Avg_PPG_Per_Player', 'Total_Players', 'Total_Points', 'Avg_Games_Played']
    
    # Sort by average PPG
    team_stats = team_stats.sort_values(by='Avg_PPG_Per_Player', ascending=False)
    
    # Add rank
    team_stats.insert(0, 'Rank', range(1, len(team_stats) + 1))
    
    print("\nTeam Performance Rankings (by Average Points Per Game Per Player):")
    print(team_stats.to_string(index=False))
    
    # Display insights
    print(f"\nInsights:")
    print(f"  • Highest scoring team: {team_stats.iloc[0]['Team']} ({team_stats.iloc[0]['Avg_PPG_Per_Player']:.2f} PPG)")
    print(f"  • Lowest scoring team: {team_stats.iloc[-1]['Team']} ({team_stats.iloc[-1]['Avg_PPG_Per_Player']:.2f} PPG)")
    print(f"  • Average across all teams: {team_stats['Avg_PPG_Per_Player'].mean():.2f} PPG")
    print(f"  • Total teams analyzed: {len(team_stats)}")
    
    return team_stats


def create_visualization(team_stats):
    """
    STRETCH CHALLENGE: Create a bar graph showing team offensive performance.
    
    This visualization displays the average points per game per player
    for each team, making it easy to compare team performance at a glance.
    
    Args:
        team_stats: DataFrame containing team statistics
    """
    print("\n" + "=" * 60)
    print("STRETCH CHALLENGE: DATA VISUALIZATION")
    print("=" * 60)
    print("\nGenerating bar chart...")
    
    # Create figure and axis
    plt.figure(figsize=(14, 8))
    
    # Create bar chart - top 20 teams only for readability
    top_teams = team_stats.head(20)
    bars = plt.bar(range(len(top_teams)), top_teams['Avg_PPG_Per_Player'], 
                   color='steelblue', edgecolor='navy', linewidth=1.2)
    
    # Customize the chart
    plt.xlabel('Team', fontsize=12, fontweight='bold')
    plt.ylabel('Average Points Per Game (Per Player)', fontsize=12, fontweight='bold')
    plt.title('NBA Team Offensive Performance\nAverage Points Per Game Per Player (Top 20 Teams)', 
              fontsize=14, fontweight='bold', pad=20)
    
    # Set x-axis labels
    plt.xticks(range(len(top_teams)), top_teams['Team'], rotation=45, ha='right')
    
    # Add value labels on top of bars
    for i, (bar, value) in enumerate(zip(bars, top_teams['Avg_PPG_Per_Player'])):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{value:.1f}', ha='center', va='bottom', fontsize=9)
    
    # Add grid for easier reading
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('team_performance.png', dpi=300, bbox_inches='tight')
    print("✓ Chart saved as 'team_performance.png'")
    
    # Display the chart
    plt.show()
    print("✓ Chart displayed successfully!")


def generate_summary_report(data, top_scorers, team_stats):
    """
    Generate a comprehensive summary report of all analyses.
    
    Args:
        data: Original dataset
        top_scorers: DataFrame of top scoring players
        team_stats: DataFrame of team statistics
    """
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY REPORT")
    print("=" * 60)
    
    print(f"\nDataset Overview:")
    print(f"  • Total player records analyzed: {len(data)}")
    print(f"  • Unique players: {data['Player'].nunique()}")
    print(f"  • Teams represented: {data['Tm'].nunique()}")
    print(f"  • Years covered: {data['Year'].min()} to {data['Year'].max()}")
    
    print(f"\nTop Scorer:")
    print(f"  • Player: {top_scorers.iloc[0]['Player']}")
    print(f"  • Team: {top_scorers.iloc[0]['Tm']}")
    print(f"  • Points: {top_scorers.iloc[0]['PTS']:.1f}")
    print(f"  • Year: {top_scorers.iloc[0]['Year']}")
    
    print(f"\nBest Offensive Team:")
    print(f"  • Team: {team_stats.iloc[0]['Team']}")
    print(f"  • Avg PPG per player: {team_stats.iloc[0]['Avg_PPG_Per_Player']:.2f}")
    print(f"  • Total players: {team_stats.iloc[0]['Total_Players']:.0f}")
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)


def main():
    """
    Main function to orchestrate the entire analysis workflow.
    """
    # File path to dataset
    filepath = "data/NBA_Player_Stats.csv"
    
    # Step 1: Load the data
    data = load_data(filepath)
    if data is None:
        return
    
    # Step 2: Preview the data
    preview_data(data)
    
    # Step 3: Clean the data
    data = clean_data(data)
    
    # Step 4: Answer Question 1 - Top Scorers
    top_scorers = analyze_top_scorers(data, top_n=10)
    
    # Step 5: Answer Question 2 - Team Performance
    team_stats = analyze_team_performance(data)
    
    # Step 6: Stretch Challenge - Create Visualization
    create_visualization(team_stats)
    
    # Step 7: Generate Summary Report
    generate_summary_report(data, top_scorers, team_stats)


# Entry point of the program
if __name__ == "__main__":
    main()