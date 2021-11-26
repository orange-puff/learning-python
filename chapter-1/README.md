# Chapter 1: Basics

In this chapter, we will look at many common things in python very briefly. You won't be expected to remember everything we discuss, but this should introduce you to most of what we will cover in this course in a shallow way.

***

Open up `main.py` to get started.

Python is an interpreted language. Typically, languages are either `compiled` or `interpreted`. Typically, a compiled language will need a [compiler](https://en.wikipedia.org/wiki/Compiler) to translate source code files to machine code and then to link them together into an executable. Interpreted languages needs an [interpreter](https://en.wikipedia.org/wiki/Interpreter_(computing) to read the source code files and execute them. When the python interpreter is running on `main.py`, for instance by calling `python main.py` from the terminal, it will read each line in the order that they show up and execute them.
 
You probably already know what a function is. If not, it is a callable group of logic. `def function_name():` is how you declare a function in Python. `def` is a [Python keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords), meaning it has some behavior associated with it that the interpreter knows about. Therefore, when creating variable names, you cannot use any of these keywords as the variable name. So `def = 5` would not work, but `def_ = 5` would. To interact with a function you must call it.

That would look something like

```
def my_func():
    print('hello, world')

my_func()
```

Therefore, as you look through `main.py`, you will note that there is nothing to execute until line `17`. But on line `16`, you'll see `if __name__=='__main__':`. This is an `if` statement. They look like

```
if condition:
    code...
elif condition2:
    code...
else:
    code...
```

Where condition is some expression that results in `True` or `False`. For instance `x == 5`, or `10 < 20`. `__name__=='__main__'` may look confusing. Most python projects will have many files. There is always a file that serves as the entry point for the project. These files are called modules in the context of the interpreter, and this specific file is named `__main__`. Thus, each file has a `__name__` variable set by the interpreter, but  the file that the Python interpreter is using as the entry point has its `__name__` set to `'__main__'`, whereas files that aren't the entry point have `__name__` set to their file name, so `my_module.py` would have `__name__` set to `my_module`

On line `17` you'll notice the first function call. `for_loop(10)`. This calls the function declared on line `1`. You'll notice this function is declared as `def for_loop(n):`. `n` is called a `parameter`. It means that anytime you call `for_loop`, you must pass an `argument` to it, which is some value you are passing to the function. In this case, the `argument` is `10`.

On line `18` we call another function using a different type of loop called a `while loop`. 

A `for loop` can be read as `for value in iterable`, where `value` is a variable holding the value of some entry in the `iterable`, which is a set of objects we can `iterate` over.

On line `19` we wrap the `print` function around a call to `function_with_return()`. `print` takes an argument and outputs it to the console. `function_with_return()` is returning a value that is passed to `print`

On line `20` we call `function_without_return()`. If we tried to do `print(function_without_return())`, first`function_without_return` runs and outputs `155`. Since `function_without_return` returns nothing, the argument passed to `print` is `None`. `None` is another Python keyword that represents something without value. 

Finally, on line `21`, we have `x = 5`. We call `x` a variable and say that we are `initializing x with value 5`. Now, in any place that you wanted to use the value `5`, you can instead use `x`

**IMPORTANT: Since the interpreter reads one line at a time, you need to declare your functions before calling them.**

### Exercises 

1. Write a `for loop` that prints out every even number between 0 and 10

    `hint: Use the % operator, where a % b == remainder of a / b, and == to check for equality`

2. Do `1.` but with a `while loop`

3. If you didn't already, make sure `1` and `2` are in their own functions, and give each function a parameter `n` which will be the high point of the `for loop`

***

## Variables and Operations: 1-1
Open up `1-1.py` to get started. Just as before, we start by looking at the `if __name__=='__main__':`, the entry point for this program. We start by initializing `x` with value `5`. `x += 10` means `x = x + 10`. We are setting `x` equal to what `x` currently is, `5`, and adding `10`. The operators in Python are

* `+`, `-`, `*`, `/`
* `//` which is integer division and is equivalent to `floor(5/2)` where `floor` is the mathematical floor function.
* `%` which for `a % b` returns the remainder when a is divided by b. E.g. `5 % 2 = 1`, `3 % 7 = 3`, `11 % 2 = 1`, `10 % 5 = 0`

### Exercises

1. Start with `a = [1, 2, 3, 4, 5]`. We can iterate this by doing `for val in a:` where val will take on `1`, `2`, `3`, `4`, and `5`. E.g.

    ```
   a = [1, 2, 3, 4, 5]
   for val in a:
       print(val * 2)
   
   -->
   2
   4
   6
   8
   10
   ```
   find the total sum, difference, product, and quotient of this list, i.e.
   
   ```
   1 + 2 + 3 + 4 + 5
   1 - 2 - 3 - 4 - 5
   1 * 2 * 3 * 4 * 5
   1 / 2 / 3 / 4 / 5
   ```
    You can use the following variables to store these values:
    ```
   tot1
   tot2
   tot3
   tot4
   ```
   
   **Do Not type this out. You must use a for loop (or while loop)**
***

## math module 1-2
Open up `1-2.py` to get started

You will notice at the top there is the line `import math`. This is an incredibly important `module` that comes when downloading Python. Modules are python files that we can import into our own python file. Somewhere, there is a file called `math.py` that we are importing. It likely imports many other files itself to build up all the methods it offers

Let's go over some of the important ones

`math.sqrt(5)` returns the square root of 5. What if we want the floor of that? `int(math.sqrt(5))` or `math.floor(math.sqrt(5))`. What if we want the ceiling of that? `math.ceil(math.sqrt(5))`. How about if we want to round that? `round(math.sqrt(5))`

What if we want to do exponentiation? We can do `math.pow(2, 4)` or `2 ** 4`, which is `16`

`math` has the exponential and logarithmic function built in as well as all standard trigonometry functions, and much more.

### Excercises
1. `print` the ceiling of the square root of 16 to the power of 5 in one line **(Answer = 1024)**

***

## lists, sets, tuples, dictionaries 1-3
Open up `1-3.py` to get started

#### list
The `list` data structure is one of the most important that is built into Python. We can initialize a list like

`arr = [1, 2, 3, 4, 5, 6, 7]`

We can also use something called `list comprehension` and the `range` function. `range`. [For a full list of Python functions, see](https://docs.python.org/3/library/functions.html)

`range` has 3 `overloads`, meaning it has 3 separate signatures with different amounts of parameters. 

```
range(10) returns an iterable with values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 10) returns an iterable with values 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 10, 2) returns an iterable with values 1, 3, 5, 7, 9
```

Now, we can combine that with `list comprehension` like

`arr = [i for i in range(10]`, which could also simply be `arr = list(range(10))`

We can also use conditionals in list comprehension like `arr = [i for i in range(10) if i % 2 == 0]` which is `[0, 2, 4, 6, 8]`, or 
`arr = [i if i % 2 == 0 else -1 for i in range(10]` which is `[0, -1, 2, -1, 4, -1, 6, -1, 8, -1]`.

Just like we can do

```
x = 5
x += 10
--->
x = 15
```

we can do that with lists:

```
arr = [1, 2, 3]
arr += [4, 5, 6]
--->
arr = [1, 2, 3, 4, 5, 6]
```

#### set
The `set` data structure is a lot like the `list`, but it cannot have duplicates.

```
s = set()
s = set([1, 2, 3, 4])
```

When we do something like `if 5 in arr:`, where `arr` is a `list`, this is implicitly searching the entire list `arr` for `5`. We can easily imagine that `arr` has many values and this search could take a long time, assuming `5` doesn't appear early in the list. 

This is where sets come in. When doing `if 5 in s:` where `s` is a `set`, this search happens in what we call `constant` time (whereas we call the search of the list `linear` time). This is also true for insertions and deletions.

Therefore, sets are indispensable when we need fast lookup.

#### tuple
A `tuple` is like a list but it is immutable. It's great for storing data that will never change

```
t = (1, 2, 3)
t2 = 1, 2
t3 = (9)
```

#### dictionary
The `dictionary` data structure, referred to by the keyword `dict` in Python, may be one of the most useful data structures. In a `list`, we access an element by its `index`. To access the 3rd value in a `list`, we'd do

```
arr = [1, 2, 3, 4, 5]
print(arr[2]) # because indexes start at 0
``` 

`dictionary` allows you to index by a `key` of your choice. A `key` can be anything that is immutable, meaning unchanging. So a `key` can be a `string`, an `int`, a `tuple`. The `key` corresponds to a `value`, which is the data associated with a `key`. A `value` can be basically anything

`dictionary` is similar to `set` in that it has constant time lookup, storage, and deletion

### Excercises
Implement the solutions to the following questions by writing a function for each. Something you should note from the questions is that lists are common ways of storing data whereas sets and dictionaries are common ways of processing data.
1. Write a function that takes a `list` and sums their values. **You could use the built in `sum` function here, but don't**
2. Write a function that takes a `list` and returns the first duplicate value found by looking left to right.

    For instance, given `[1, 2, 3, 2, 1, 6]` returns `2`, since it is the first duplicate found
    
    `Hint: Use a set or a dictionary`
3. Write a function that takes a `list` and returns a new `list` with the values in reverse order
    For instance, given `[1, 2, 3, 4]` returns `[4, 3, 2, 1]`
4. Write a function that takes a `list` and returns the most frequent element in the list, if there isn't one, returns `None`

    For instance, given `[1, 2, 3, 4]` returns `None`, `[1, 2, 2, 3, 4]` returns `2`, `["Hello", "a", 'b', 'c', "b"]` returns `b`
    
    `Hint: You can use the counter code in 1-3.py, but you'll still have more work to do to find the most frequent value.`
5. Write a function that takes the following dictionary and returns a list with all of those values combined

    `m = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}`

    should return `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`.
    
    **Note that the key here is irrelevant and we could have used a list of lists. Also, note that dictionaries do not guarantee order when iterating, so we won't necessarily be iterating keys in order `1`, `2`, `3`, `4`.**