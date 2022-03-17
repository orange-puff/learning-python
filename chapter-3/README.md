# Chapter 3: Loops, Conditionals, Functions, A Deeper Look

***

In this chapter, we will mostly focus on more challenging problems using conditionals, loops, and functions

***

### conditionals
Depending on the scenario, you may want to use an `if else` or sequential `if`

**Reminder** The way an `if else` block works is

```
if condition1:
    <code>...
elif condition2:
    <code>...
elif condition3:
    <code>...
else:
    <code>...
```

if `condition1` evaluates to a `True`, then we execute the code therein and after doing so we exit the `if else` block.
On the other hand, if `condition1` is false, we move on to check if `condition2` is `True`
We continue doing so until we get to `else`, where we only execute the code in `else` when none of the previous
`if elif` were true

We don't need an else. Suppose we want to append `5` to a list if the `len(list) == 3` and
append `3` to the list if `len(list) == 5`

```
def maybe_append_to_list(arr):
    if len(arr) == 3:
        arr.append(5)
    elif len(arr) == 5:
        arr.append(3)
```

note that in `maybe_append_to_list`, we don't always append to arr.

Sometimes, we want sequential `if` instead of `if else`. Suppose we want to append `1` to a list if it contains the number `5` and `2` to a list if it contains 
the number `10`, and append `1` twice if it contains both `5` and `10`

The first option is to use `if elif`
```
def maybe_append_to_list(arr):
    if 5 in arr and 10 in arr:
        arr += [1, 1]
    elif 5 in arr:
        arr.append(1)
    elif 10 in arr:
        arr.append(1)
```

But this is easier solved with sequential `if`
```
def maybe_append_to_list(arr):
    if 5 in arr:
        arr.append(1)
    if 10 in arr:
        arr.append(1)
```

In this function, we first check if `5` is in the list, and if so, append `1`. We then check if `10` is in 
the list, regardless of if `5` was in the list, and append `1` if so.

### loops