with open("input.txt") as task_input:
    contents = task_input.read()
    trimmed_contents = "".join(contents.split())
    print(eval(trimmed_contents))
