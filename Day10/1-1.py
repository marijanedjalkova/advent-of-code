import re


def tests():
    pass


def string_to_dict(string, pattern):
    regex = re.sub(r'{(.+?)}', r'(?P<_\1>.+)', pattern)
    values = list(re.search(regex, string).groups())
    keys = re.findall(r'{(.+?)}', pattern)
    _dict = dict(zip(keys, values))
    return _dict


def main():
    with open("input.txt") as task_input:
        contents = task_input.read().split("\n")
        print(contents)
        for line in contents:
            line = "".join(line.split())
            data_map = string_to_dict(line.strip(), "position=<{x_pos},{y_pos}>velocity=<{x_v},{y_v}>")


if __name__ == "__main__":
    tests()
    main()