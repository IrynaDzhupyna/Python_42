import random

def gen_player_achievement() -> set:
    achievements = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
                     'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme',
                     'Untouchable', 'Sharp Mind', 'Boss Slayer']
    num = random.randint(1, len(achievements))
    return set(random.sample(achievements, num))

def main():
    print("=== Achievement Tracker System===\n")
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    players_achievement = {}
    # Generate random achievement for each player and store it in a dictionary
    for player in players:
        players_achievement[player] = gen_player_achievement()
    for player in players_achievement:
        print(f"Player {player}: {players_achievement[player]}")
    # set.union() method to combine all the achievements from all players into a single set of unique achievements
    # set.itersection() method to find the common achievements that all players have unlocked
    # set.difference() method to find the achievements that are unique to each player
    all_achievements = set()
    common_achievements = set(players_achievement[players[0]])
    different_achievements = set(players_achievement[players[0]])
    for achievement in players_achievement.values():
        all_achievements = set(all_achievements.union(achievement))
        common_achievements = set(common_achievements.intersection(achievement))
        # different_achievements = different_achievements.difference(achievement)
    print(f"All distinct achievements: {all_achievements}\n")
    print(f"Common achievements: {common_achievements}\n")
    for player in players:
        other_players = set()
        for other_player in players:
            if other_player != player:
                other_players = other_players.union(players_achievement[other_player])
        unique = players_achievement[player].difference(other_players)
        print(f"Only {player} has: {unique}")
    print()
    for player in players:
        other_players = set()
        for other_player in players:
            if other_player != player:
                other_players = other_players.union(players_achievement[other_player])
        print(f"{player} is missing: {other_players.difference(players_achievement[player])}")


if __name__ == "__main__":
    main()