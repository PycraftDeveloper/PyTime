# PyTime
A Github repository testing just how fast different Python functions are!

## About
The use of the programming language Python is growing, as such it's seen used in a growing number of applications. And yet - despite this - little is publicly available about the performance of the programming language on a per-function basis. Given that there is a growing demand for faster performance in almost all applications, knowing which functions are good to use and which ones are best avoided is key. This repository is intended to help you to make a more informed decision in your development process about how your application may perform, and may also provide insight into alternative functions that may do the job faster.

## How to use
There are two main ways to use this repository, you can either access the data that you need in the results section, or you can contribute to the database by running the tests on your system.

### Accessing
Accessing the data stored within this repository is super simple.
1. First, you need to identify which Python version (in the form w.x.y) and operating system (z) you require data for.
2. Then, you need to navigate to the file in the results section that corresponds to the details you identified above.
3. The file will be in the form: `w-x-y_z.md`
4. If you download the file or open it in a browser, you can use a [search function](https://www.howtogeek.com/671304/how-to-quickly-search-for-text-on-the-current-web-page/) to find the specific function you are looking for.

_Note: Its unlikely that there will be a Python version that will exactly match the one you need, however the w and x version numbers will need to match for the most accuracy, and so will the operating system_

### Contributing
Contributing to this repository is also just as easy, just follow the instructions below!
1. Download and extract the latest version of the source code from the green button at the top of this page.
2. Download and install the Python version you want to test (if you don't have it installed already).
3. Close all applications running on the system.
4. Open a terminal window and navigate to the folder containing the extracted files.
5. Navigate to the directory labelled `src`.
6. Run the python file called `main.py` using the version you want to use.

_Note: You can use a virtual environment, or any python version you wish, if you're struggling to get started, run this command: `python main.py` to run using the default Python install._

Once started the process will take a significant amount of time to complete, and the results will automatically be written and formatted to a results file, which you can add via a pull request to this repository. This is best run overnight if possible.

By default there is a list of functions to test, using the standard library, however by modifying the `functions.txt` file you can test any additional functions from first and third party modules. You can even test your own functions through the `ext.py` program. For more information on how to do this, please see the documentation!

## Testing Methodology
This is a minimal example of the testing methodology.

```
import time

total_execution_time = 0
for _ in range(10_000_000):
  start = time.perf_counter()

  function_to_benchmark()

  end = time.perf_counter()
  total_execution_time += end-start

print(total_execution_time/10_000_000)
```

Gives an uncertainty of ±0.0000000005 seconds
