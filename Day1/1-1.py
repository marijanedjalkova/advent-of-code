with open("input.txt") as input:
    contents = input.read()
    trimmed_contents = "".join(contents.split())
    print(eval(trimmed_contents))
