def get_totals() -> list[int]:
    with open('./input') as buffer:
        input_data = buffer.read()
    meals_by_elve = input_data.split('\n\n')
    return [sum(map(int, elve.split('\n'))) for elve in meals_by_elve]


def part_1():
    print(max(get_totals()))


def part_2():
    sorted_total_cal = sorted(iter(get_totals()), reverse=True)
    print(sum(sorted_total_cal[0:3]))

if __name__ == '__main__':
    # part_1()
    part_2()
