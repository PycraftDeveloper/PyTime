import os
import time
import builtins
import string
import random
import json

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
        array.append(random_word(10))
    elif arg == "BOOL":
        array.append(random.choice([True, False]))
    elif arg == "FLOAT":
        array.append(random.choice([-1, 1]) * round(random.random(), 5))
    elif arg == "INT":
        array.append(random.choice([-1, 1]) * random.randint(10000, 99999))
    return array

base_path = up(up(__file__))

functions_path = f"{base_path}{SEPARATOR}data files{SEPARATOR}functions.csv"
results_path = f"{base_path}{SEPARATOR}data files{SEPARATOR}results.csv"

try:
    os.remove(results_path)
except FileNotFoundError:
    pass

delay = 1/50_000

test_data = []
with open(functions_path, 'r') as file:
    for line in file.readlines():
        if line.startswith("#"):
            continue
        if "," in line:
            function_data = line.split(',')
            module_name = function_data[0]
            function_name = function_data[1]
            args = function_data[2]

            if module_name == "BUILT_IN":
                module = builtins

            else:
                module = __import__(module_name)
            function = getattr(module, function_name)

            total_execution_time = 0
            for _ in range(10_000_000):
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
                        test_args.append(data_filler(test_args, arg))

                start = time.perf_counter()
                function(*test_args)
                end = time.perf_counter()
                total_execution_time += end - start
                time.sleep(delay)

            mean_execution_time = total_execution_time / 10_000_000
            with open(results_path, "a") as out_file:
                result = json.dumps(f"{function_name},{mean_execution_time}")
                out_file.write(result+"\n")
            print(f"Execution time: {total_execution_time/10_000_000}")