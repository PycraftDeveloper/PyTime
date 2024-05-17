# PyTime
A Github repository testing just how fast different Python functions are!

## Configuring custom tests
Configuring your own tests in PyTest is nice and easy, allow me to explain.

PyTest works by reading the testing criteria from a file located in `~/data files/functions.txt`.
Each line represents a new test to run, and the structure of each line is explored below:

* Any line preceded with a `#` will be skipped and not tested.
* Any empty line will also be skipped - this is used for formatting.

Each non-empty line contains a series of arguments, separated by commas (no spaces):
1. The first argument represents the module to use, with `BUILT_IN` being the only pre-programmed argument representing any function that doesn't need to be imported to use. Alternatively, specifying the name of the module will automatically import the module as needed. For example `random` imports the standard library `random`, `pygame` imports the 3rd party module `pygame` and `ext` imports the extension library, which is where custom functions can be created.
2. This represents the name of the function to run. There are no pre-programmed attributes here.
3. Any additional arguments represent the parameters to pass into a function. Where possible the pre-programmed attributes should be used to avoid Python trying to accelerate the process by caching the results when calling the same function with the same arguments repeatedly. The pre-programmed attributes are:
* `NULL` - If no arguments are needed, this must be added.
* `NONE` - If the keyword "None" is needed then use this.
* `STR` - Automatically (and randomly) generates a 5 character ASCII string.
* `BOOL` - Automatically (and randomly) generates a binary True or False value.
* `FLOAT` - Automatically (and randomly) generates a positive or negative floating point number to 5 decimal places.
* `INT` - Automatically (and randomly) generates a positive or negative number between 10000 and 99999.
* `POS_INT` - Automatically (and randomly) generates a positive number between 10000 and 99999.
* `NEG_INT` - Automatically (and randomly) generates a negative number between -10000 and -99999.
* `ANY` - Randomly picks a data type from any of the data types mentioned here (Excluding the `ANY_EXCLUDING_NULL` data type).
* `ANY_EXCLUDING_NULL` - Randomly picks a non-empty data type from any of the data types mentioned here (Excluding the `ANY` data type).

You can use the `*` character to randomly generate a sequence to a specified number of elements. For example: `BOOL*5` is identical to `BOOL,BOOL,BOOL,BOOL,BOOL` and could create an array that looks like this: `[True, False, True, True, False]`.