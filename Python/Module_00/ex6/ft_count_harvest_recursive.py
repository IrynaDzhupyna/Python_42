def print_days(n, days):
    print("Day", n)
    if (n < days):
        print_days(n + 1, days)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    print_days(1, days)
