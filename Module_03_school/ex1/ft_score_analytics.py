import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    length = len(sys.argv)
    if length < 3:
        print("No score provided."
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    else:
        scores = []
        i = 1
        while i < length:
            try:
                score = int(sys.argv[i])
                scores += [score]
                i += 1
            except ValueError:
                print(f"Invalid parameter: {sys.argv[i]}")
                # length -= 1
                i += 1
    if not scores:
        print("No score provided."
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("Scores processed:", scores)
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
