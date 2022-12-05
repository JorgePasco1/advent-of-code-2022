import re
from copy import deepcopy


instruction = tuple[int, int, int]
stack = list[str]


def get_stacks_and_instructions() -> tuple[list[stack], list[instruction]]:
    with open('input', 'r') as buffer:
        raw_data = buffer.read()

    raw_stacks, raw_instructions = raw_data.split('\n\n')
    stacks = list(map(list, raw_stacks.split('\n')))
    instructions = list(map(extract_instruction, raw_instructions.split('\n')))
    return stacks, instructions


def extract_instruction(string: str) -> instruction:
    result = [int(s) for s in re.findall(r'\b\d+\b', string)]
    return result[0], result[1] - 1, result[2] - 1


def move(stacks: list[stack], amount: int, from_: int, to: int) -> list[stack]:
    result = deepcopy(stacks)
    for _ in range(amount):
        item = result[from_].pop()
        result[to].append(item)
    return result


def get_top_items(stacks: list[stack]) -> str:
    return ''.join(stack[-1] for stack in stacks)


def part_one() -> None:
    stacks, instructions = get_stacks_and_instructions()
    for instruction in instructions:
        stacks = move(stacks, *instruction)
    result = get_top_items(stacks)
    print(result)


######## Part 2 ########
def move_in_batch(stacks: list[list[str]], amount: int, from_: int, to: int) -> list[list[str]]:
    result= deepcopy(stacks)
    result[to].extend(result[from_][-amount:])
    result[from_] = result[from_][0: -amount]
    return result


def part_two():
    stacks, instructions = get_stacks_and_instructions()
    for instruction in instructions:
        stacks = move_in_batch(stacks, *instruction)
    result = get_top_items(stacks)
    print(result)


if __name__ == "__main__":
    part_one()
    part_two()
