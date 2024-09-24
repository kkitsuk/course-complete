def calculate_structure_sum(structure):
    count = 0
    for i in structure:
        if isinstance(i, (tuple, list, set)):
            count += calculate_structure_sum(i)
        elif isinstance(i, (float, int)):
            count += i
        elif isinstance(i, dict):
            for k, v in i.items():
                count += sum(get_length_or_value(x) for x in (k, v))
        else:
            count += len(i)
    return count


def get_length_or_value(item):
    if isinstance(item, (int, float)):
        return item
    return len(item)


data_structure = [
    [1, 2, 3.9],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]


result = calculate_structure_sum(data_structure)
print(result)
