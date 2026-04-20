import random
#get the set of achievement for a player
def get_player_achievements():
    achievements = [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Unstoppable',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind'
    ]
    num = random.randint(1, len(achievements))
    result = set()
    while len(result) < num:
        achievement = random.choice(achievements)
        result.add(achievement)
    return result

def main() -> None:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements = {}
    # dict with name:set
    for player in players:
        player_achievements[player] = get_player_achievements()
    for player in player_achievements:
        print(f"Player {player}: {player_achievements[player]}")
        print()
    #distinct achievements
    all_achievements = set()
    for achievements in player_achievements.values():
        all_achievements = all_achievements.union(achievements)
        common_achievements = all_achievements.intersection(achievements)
    print(f"All distinct achievements: {all_achievements}")
    print(f"Common achievements: {common_achievements}\n")


    for player in player_achievements:
        missing = all_achievements - player_achievements[player]
        print(player, "is missing", missing)


if __name__ == "__main__":
    main()