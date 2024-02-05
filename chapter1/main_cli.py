"""Main executable script - Chapter 1"""
from models import Player, Performance
from database import Session # Import the correct Session object

def main():
    """Fetch and print player and performance data from the database."""
    with Session() as session:
        players = session.query(Player).all()
        for player in players:
            print(f'Player ID: {player.player_id}')
            print(f'NFL Player ID: {player.nfl_player_id}')
            print(f'First Name: {player.first_name}')
            print(f'Last Name: {player.last_name}')
            for performance in player.performances:
                print(f'Week Number: {performance.week_number}')
                print(f'Week Number: {performance.fantasy_points}')
                print('---') # Separator between players

# standard instructions for calling from command line
if __name__ == "__main__":
    main()
