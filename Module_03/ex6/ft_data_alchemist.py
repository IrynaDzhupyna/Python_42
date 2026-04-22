import random


names = ['Alice', 'bob', 'Charlie', 'dylan',
         'Emma', 'Gregory', 'john', 'kevin', 'Liam']
all_capitalized = [name.capitalize() for name in names]
only_capitalized = [name for name in names if name[0].isupper()]
print("Initial list of players: ", names)
print("New list with all names capitalized: ", all_capitalized)
print("New list of capitalized names only: ", only_capitalized)
score_dict = {name: random.randint(1, 907) for name in names}
print("Score dict: ", score_dict)
score_average = sum(score_dict.values()) / len(score_dict)
print(f"Score average: {score_average:.2f}")
max_scores = {
    name: score
    for name, score in score_dict.items()
    if score > score_average}
print("High scores: ", max_scores)
