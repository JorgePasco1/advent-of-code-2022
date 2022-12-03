def priority(char: str) -> int:
    return ord(char) - 38 if char.isupper() else ord(char) - 96


def shared_type(rucksack: str) -> str:
    half = len(rucksack) // 2
    return next(iter(set(rucksack[0: half]).intersection(set(rucksack[half:]))))


def part_one():
    with open('./input', 'r') as buffer:
        rucksacks = buffer.read().splitlines()
    result = sum(map(priority, map(shared_type, rucksacks)))
    print(result)


def shared_group_type(rucksacks: list[str]) -> str:
    return next(iter(set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2]))))


def part_two():
    GROUP_LENGTH = 3

    with open('./input', 'r') as buffer:
        rucksacks = buffer.read().splitlines()

    rucksack_groups = [rucksacks[n: n + GROUP_LENGTH] for n in range(0, len(rucksacks), GROUP_LENGTH)]
    result = sum(map(priority, map(shared_group_type, rucksack_groups)))
    print(result)


if __name__ == "__main__":
    # part_one()
    part_two()
