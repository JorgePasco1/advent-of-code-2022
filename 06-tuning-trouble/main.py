def read_input():
    with open('input', 'r') as buffer:
        datastream = buffer.read()
    return datastream


def all_different(string: str) -> bool:
    return len(set(string)) == len(string)


def find_unique_sequence_position(string: str, sequence_length: int) -> int:
    for idx in range(len(string)):
        if idx < sequence_length:
            continue

        if all_different(string[idx - sequence_length: idx]):
            return idx
    return 0


def find_start_of_packet(buffer: str) -> int:
    return find_unique_sequence_position(buffer, 4)


def find_start_of_message(buffer: str) -> int:
    return find_unique_sequence_position(buffer, 14)


def part_one() -> None:
    datastream = read_input()
    print(find_start_of_packet(datastream))


def part_two() -> None:
    datastream = read_input()
    print(find_start_of_message(datastream))


if __name__ == "__main__":
    part_one()
    part_two()
