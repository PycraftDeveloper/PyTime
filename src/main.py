import os
import time
import builtins
import string
import random
import platform

run_time = time.perf_counter()

SEPARATOR = os.sep

def up(path: str) -> str:
    return path[::-1].split(SEPARATOR, 1)[-1][::-1]

def random_word(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def data_filler(array, arg):
    if arg == "NONE":
        pass
    elif arg == "STR":
        array.append(random_word(5))
    elif arg == "BOOL":
        array.append(random.choice([True, False]))
    elif arg == "FLOAT":
        array.append(random.choice([-1, 1]) * round(random.random(), 5))
    elif arg == "INT":
        array.append(random.choice([-1, 1]) * random.randint(10000, 99999))
    elif arg == "POSINT":
        array.append(random.randint(10000, 99999))
    elif arg == "NEGINT":
        array.append(random.randint(-99999, -10000))
    else:
        array.append(arg)
    return array

base_path = up(up(__file__))

formatted_version = platform.python_version().replace(".", "-")
functions_path = f"{base_path}{SEPARATOR}data files{SEPARATOR}functions.txt"
results_path = f"{base_path}{SEPARATOR}results{SEPARATOR}{formatted_version}_{platform.system()}.md"

header = "# PyTime\nA Github repository testing just how fast different Python functions are!\n\n## Results"
header += f"\n\nRunning PyTime using Python {platform.python_version()} on {platform.system()}"

with open(results_path, "w") as out_file:
    out_file.write(header)

delay = 1/50_000
RUNS = 1_000_000

test_data = []
module_name_header = ""
with open(functions_path, 'r') as file:
    for line in file.readlines():
        if line.startswith("#"):
            continue
        if "," in line:
            function_data = line.split(',')
            module_name = function_data[0]
            function_name = function_data[1]
            args = function_data[2]

            if module_name_header != module_name:
                if module_name == "BUILT_IN":
                    header = "\n\n### Standard Library"
                else:
                    header = f"\n\n### {module_name}"
                header += "\n\n| Function | Mean execution time of 1,000,000 runs, measured in seconds, s | Shortest execution time, measured in seconds, s | Longest execution time, measured in seconds, s | Range in execution time, measured in seconds, s | Normalized execution time |"
                header += "\n| --- | --- | --- | --- | --- | --- |"

                with open(results_path, "a") as out_file:
                    out_file.write(header)

                module_name_header = module_name
            if module_name == "BUILT_IN":
                module = builtins

            else:
                module = __import__(module_name)
            function = getattr(module, function_name)

            total_execution_time = 0
            range_min = [0, float("inf")]
            range_max = [0, 0]
            for iter in range(RUNS):
                test_args = []
                for arg in args.split(","):
                    arg = arg.strip()
                    split_arg = arg.split("*")
                    arg = split_arg[0]
                    if len(split_arg) > 1:
                        count = split_arg[1]
                        element = []
                        for _ in range(int(count)):
                            element = data_filler(element, arg)
                            time.sleep(delay)
                        test_args.append(element)
                    else:
                        test_args = data_filler(test_args, arg)

                start = time.perf_counter()
                function(*test_args)
                end = time.perf_counter()
                run_delta = end - start
                if run_delta < range_min[1]:
                    range_min = [iter, run_delta]

                if run_delta > range_max[1]:
                    range_max = [iter, run_delta]
                total_execution_time += run_delta
                time.sleep(delay)

            mean_execution_time = total_execution_time / RUNS
            execution_range = range_max[1] - range_min[1]
            n = (mean_execution_time - range_min[1])/execution_range
            result = f"\n| {function_name} | {mean_execution_time} | {range_min[1]} | {range_max[1]} | {execution_range} | {n} |"
            with open(results_path, "a") as out_file:
                out_file.write(result)

            print(result)
            print(f"Running for: {time.perf_counter()-run_time} seconds")