import re
from copy import deepcopy


def get_stacks_and_instructions() -> tuple[list[list[str]], list[list[int]]]:
    with open('input', 'r') as buffer:
        raw_data = buffer.read()

    raw_stacks, raw_instructions = raw_data.split('\n\n')
    stacks = list(map(list, raw_stacks.split('\n')))
    instructions = list(map(extract_numbers, raw_instructions.split('\n')))
    return stacks, instructions


def extract_numbers(string: str) -> list[int]:
    return [int(s) for s in re.findall(r'\b\d+\b', string)]


def move(stacks: list[list[str]], amount: int, from_: int, to: int) -> list[list[str]]:
    result = deepcopy(stacks)
    left_to_move = amount
    while left_to_move > 0:
        item = result[from_ - 1].pop()
        result[to - 1].append(item)
        left_to_move -= 1
    return result


def get_top_items(stacks: list[list[str]]) -> str:
    return ''.join(stack[-1] for stack in stacks)


def part_one() -> None:
    stacks, instructions = get_stacks_and_instructions()
    for instruction in instructions:
        stacks = move(stacks, instruction[0], instruction[1], instruction[2])
    result = get_top_items(stacks)
    print(result)


######## Part 2 ########
def move_in_batch(stacks: list[list[str]], amount: int, from_: int, to: int) -> list[list[str]]:
    result = deepcopy(stacks)
    result[to - 1].extend(result[from_ - 1][-amount:])
    result[from_ - 1] = result[from_ - 1][0: -amount]
    return result


def part_two():
    stacks, instructions = get_stacks_and_instructions()
    for instruction in instructions:
        stacks = move_in_batch(stacks, instruction[0], instruction[1], instruction[2])
    result = get_top_items(stacks)
    print(result)


if __name__ == "__main__":
    # part_one()
    part_two()
