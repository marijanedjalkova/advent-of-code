import time

beginning_time = time.time()
with open("input.txt") as task_input:
    contents_array = task_input.read().split()
    running_total = 0
    frequencies = set()
    frequencies.add(0)
    set_size = len(frequencies)
    found_result = False
    while not found_result:
        for line in contents_array:
            before = running_total
            expr = str(running_total) + line
            running_total = eval(expr)
            frequencies.add(running_total)
            if len(frequencies) == set_size:
                print("FOUND REPETITION", running_total)
                found_result = True
                break
            else:
                set_size += 1
    print("Finished execution", running_total, found_result)
print("Time to run", round(time.time()-beginning_time, 2), "s")
