n_lines = int(input())

winning_team = None
goals_ahead = 0

for i in range(n_lines):
    team = input()
    if winning_team == team:
        # print(f"Winning team is now {team}")
        goals_ahead += 1
    elif goals_ahead == 0:
        # print(f"Winning team is now {team}")
        winning_team = team
        goals_ahead += 1
    else:
        # print(f"Scores tied")
        goals_ahead -= 1


print(winning_team)