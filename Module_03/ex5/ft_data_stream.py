import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ['Alice', 'Bob', 'Dylan', 'Charlie']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim']
    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(
    list_of_events,
) -> typing.Generator[tuple[str, str], None, None]:
    while list_of_events:
        event = random.choice(list_of_events)
        list_of_events.remove(event)
        yield event


def main() -> None:
    event_stream = gen_event()
    for i in range(1000):
        player, action = next(event_stream)
        print(f'Event {i}: Player {player} did action {action}.')
    list_of_events = []
    for i in range(10):
        list_of_events.append(next(event_stream))
    print("Built list of 10 events: ", list_of_events)
    for event in consume_event(list_of_events):
        print("Got event from list:", event)
        print("Remains in list: ", list_of_events)


if __name__ == "__main__":
    main()
