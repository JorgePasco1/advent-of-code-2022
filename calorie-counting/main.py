def run():
    with open('./input') as buffer:
        input_data = buffer.read()
    meals_by_elve = input_data.split('\n\n')
    total_cal_by_elve = [sum(map(int, elve.split('\n'))) for elve in meals_by_elve]
    print(max(total_cal_by_elve))


def part_2():
    with open('./input') as buffer:
        input_data = buffer.read()
    meals_by_elve = input_data.split('\n\n')
    total_cal_by_elve = [sum(map(int, elve.split('\n'))) for elve in meals_by_elve]
    sorted_total_cal = sorted(iter(total_cal_by_elve), reverse=True)
    print(sum(sorted_total_cal[0:3]))

if __name__ == '__main__':
    # run()
    part_2()