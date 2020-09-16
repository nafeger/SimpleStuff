# Borrowed from daily coding problem
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# You are given a list of data entries that represent entries and
# exits of groups of people into a building. An entry looks like this:
#
# {"timestamp": 1526579928, count: 3, "type": "enter"}
#
# This means 3 people entered the building. An exit looks like this:
#
# {"timestamp": 1526580382, count: 2, "type": "exit"}
#
# This means that 2 people exited the building. timestamp is in Unix time.
#
# Find the busiest period in the building, that is, the time with the most people in the building.
# Return it as a pair of (start, end) timestamps. You can assume the building always
# starts off and ends up empty, i.e. with 0 people inside.


def calculate_busy_time(data: list):
    current_count = 0
    max_count = 0
    busiest_start = 0
    busiest_end = 0
    for i in range(len(data)):
        point = data[i]
        change = point['count']
        action = point['type']
        current_time = point['timestamp']
        if action == 'enter':
            current_count += change
        elif action == 'exit':
            current_count -= change
        else:
            print(f"Unknown value: {action}")  # just in case

        # I'm about to enter a period of the max people
        if current_count > max_count:
            max_count = current_count
            busiest_start = current_time
            if i < len(data):
                busiest_end = data[i + 1]['timestamp']

    return busiest_start, busiest_end


def test_1():
    test_set_1 = [{"timestamp": 1,
                   "count": 1,
                   "type": "enter"},
                  {"timestamp": 2,
                   "count": 1,
                   "type": "exit"}
                  ]
    x = calculate_busy_time(test_set_1)
    print(x)
    assert (1, 2) == x


def test_2():
    test_set_2 = [{"timestamp": 1,
                   "count": 1,
                   "type": "enter"},
                  {"timestamp": 2,
                   "count": 1,
                   "type": "enter"},
                  {"timestamp": 3,
                   "count": 1,
                   "type": "enter"},
                  {"timestamp": 4,
                   "count": 3,
                   "type": "exit"}
                  ]
    x = calculate_busy_time(test_set_2)
    print(x)
    assert (3, 4) == x


def test_3():
    test_set = [{"timestamp": 1, "count": 1, "type": "enter"},
                {"timestamp": 2, "count": 1, "type": "exit"},
                {"timestamp": 3, "count": 2, "type": "enter"},
                {"timestamp": 4, "count": 2, "type": "exit"}
                ]
    x = calculate_busy_time(test_set)
    print(x)
    assert (3, 4) == x


def test_4():
    test_set = [{"timestamp": 1, "count": 1, "type": "enter"},
                {"timestamp": 2, "count": 1, "type": "exit"},
                {"timestamp": 3, "count": 1, "type": "enter"},
                {"timestamp": 4, "count": 10, "type": "enter"},
                {"timestamp": 5, "count": 2, "type": "exit"},
                {"timestamp": 6, "count": 2, "type": "exit"},
                {"timestamp": 4, "count": 1, "type": "enter"},
                {"timestamp": 4, "count": 1, "type": "enter"},
                {"timestamp": 7, "count": 9, "type": "exit"},
                ]
    x = calculate_busy_time(test_set)
    print(x)
    assert (4, 5) == x


def test_5():
    test_set = [{"timestamp": 1, "count": 1, "type": "enter"},
                {"timestamp": 2, "count": 1, "type": "exit"},
                {"timestamp": 3, "count": 1, "type": "enter"},
                {"timestamp": 4, "count": 10, "type": "enter"},
                {"timestamp": 5, "count": 2, "type": "exit"},
                {"timestamp": 6, "count": 7, "type": "exit"},
                {"timestamp": 7, "count": 8, "type": "enter"},
                {"timestamp": 8, "count": 10, "type": "enter"},
                {"timestamp": 9, "count": 9, "type": "exit"},
                ]
    x = calculate_busy_time(test_set)
    print(x)
    assert (8, 9) == x


if __name__ == '__main__':
    print("here")
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
