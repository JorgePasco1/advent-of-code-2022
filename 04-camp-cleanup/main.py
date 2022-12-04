def get_pairs() -> list[str]:
    with open('./input', 'r') as buffer:
        pairs = buffer.read().splitlines()
    return pairs


def get_sets(pair: str) -> tuple[set, set]:
    range_a, range_b = pair.split(',')
    a, b = map(int, range_a.split('-'))
    c, d = map(int, range_b.split('-'))
    return set(range(a, b + 1)), set(range(c, d + 1))


def contains_the_other(pair: str) -> bool:
    set_a, set_b = get_sets(pair)
    return set_a.issubset(set_b) or set_b.issubset(set_a)


def part_one() -> None:
    pairs = get_pairs()
    print(sum(map(contains_the_other, pairs)))


##### Part 2 ######
def overlap(pair: str) -> bool:
    set_a, set_b = get_sets(pair)
    return len(set_a.intersection(set_b)) > 0


def part_two() -> None:
    pairs = get_pairs()
    print(sum(map(overlap, pairs)))


if __name__ == "__main__":
    part_one()
    part_two()
