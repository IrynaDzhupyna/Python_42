import random


def gen_player_achievements() -> set:
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer']
    num = random.randint(5, len(achievements))
    return set(random.sample(achievements, num))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    players_achievement = {}

    for player in players:
        players_achievement[player] = gen_player_achievements()

    for player in players_achievement:
        print(f"Player {player}: {players_achievement[player]}")

    all_achiev: set = set()
    common = set(players_achievement[players[0]])

    for achievement in players_achievement.values():
        all_achiev = set(all_achiev.union(achievement))
        common = set(common.intersection(achievement))

    print(f"\nAll distinct achievements: {all_achiev}\n")
    print(f"Common achievements: {common}\n")

    for player in players:
        other_players = all_achiev.difference(players_achievement[player])
        unique = players_achievement[player].difference(other_players)
        print(f"Only {player} has: {unique}")

    print()

    for player in players:
        print(f"{player} is missing: "
              f"{other_players.difference(players_achievement[player])}")


if __name__ == "__main__":
    main()
