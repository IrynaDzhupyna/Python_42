# exercise requires you to use lists to store scores
# try/except blocks to handle invalid input gracefully (e.g., when a user provides non-numeric values).
import sys

print("=== Player Score Analytics ===")
length = len(sys.argv)
if length < 2:
    print("No scores provided. Usage python ft_score_analytics.py <score1> <score2> ...")
    sys.exit(1)
scores = []
length = len(sys.argv)
i = 1
while i < length:
    try:
        score = int(sys.argv[i])
        scores.append(score)
        i += 1
    except ValueError:
        print(f"Invalid parameter '{sys.argv[i]}'")
        sys.argv.pop(i)
        length -= 1
if not scores:
    print("No scores provided. Usage python ft_score_analytics.py <score1> <score2> ...")
    sys.exit(1)

while scores:
    print(f"Current scores: {scores}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    break