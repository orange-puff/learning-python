# Chapter 2: File Input/Output  

***

In this chapter, we will discuss reading from files, processing data, and writing to files. This chapter should be shorter than the first but the questions should take more time to answer.

***

## Reading From Files: 2-1
Open `2-1.py` to get started.

We start by opening a file with the `open` method. This takes a string as argument which corresponds to the path to the file you want to open. It can be a relative or absolute path, but in our case it is simply `data.txt`, as `data.txt` is in the same folder as `2-1.py`

`file = open(file_path)` means we now have a pointer to that file data. Now, we need to access it.

We can do `file.readlines()` to return a list of strings, where each string is a line from the file. We can also do `file.read()` which return a string, this string contains all of the contents of the file. You can use whichever is appropriate depending on how the data look and what you want to do with it.

**NOTE: `file` is a pointer to the beginning of the file content. When we do `file.readline()`, which reads the first line, `file` is now pointing at the next line** 

We also have to clean the contents, and do so with our function `clean`. This is called an `impure` function because, instead of leaving the argument in its original state and creating a new value, altering it, and returning that, it alters the argument itself
Present is also `clean_pure` and `clean_pure2` to see how to do this purely. 

Notice in `clean_pure`, instead of saying `to_ret = lines`, we say `to_ret = [line for line in lines]`. Why?

In Python, most things are references. `arr = [1, 2, 3]` means a reference, or a memory address, is stored in arr. `arr[1]` looks at that memory address and finds the value at `1`. So saying
`arr2 = arr` is simply saying `arr2` now holds the reference to the memory with `[1, 2, 3]`. Thus, we need to `copy` `arr` into `arr2`.

Python gives us a simply way to do this:

```
import copy
arr = [1, 2, 3]
arr2 = copy.copy(arr)
```

This performs a `shallow copy` of `arr` and stores that copy in `arr2` (really, stores the reference to that value). You might be wondering why this copy is `shallow`. This simply means we go 1 level deep and copy all of the values over.

```
import copy
arr = [
        [1, 2, 3],
        [4, 5, 6]
      ]
arr2 = copy.copy(arr)
```

By 1 level deep, we mean a new `list` was created, but its values `[1, 2, 3]` and `[4, 5, 6]` simply are the references to the original `[1, 2, 3]` and `[4, 5, 6]`

Thus,

```
arr = [
        [1, 2, 3],
        [4, 5, 6]
      ]
arr2 = copy.copy(arr)
arr2[0] = [10, 10, 10]
print(arr[0])
print(arr2[0])
-->
[1, 2, 3]
[10, 10, 10]

arr2[1][0] = -50
print(arr[1])
print(arr2[1])
-->
[-50, 5, 6]
[-50, 5, 6]
```

Thankfully, Python also offers a `copy.deepcopy` for this situation.

```
arr = [
        [1, 2, 3],
        [4, 5, 6]
      ]
arr2 = copy.deepcopy(arr)
arr2[0][0] = -50
print(arr[0])
print(arr2[0])
-->
[1, 2, 3]
[-50, 2, 3]
```

### Exercises
1. Write a function that reads through `data.txt` and stores the words in a list, and then returns that list. Make sure the words do not have `\n` with them. This code is already in 2-1, but familiarize yourself with it

    **Aside: `\n` is the ascii value for a new line. A text editor may show us a file content with words
    ```
    word1
    word2
   ```
    but that is read by a computer as `word1\nword2`**
    
2. Write a function that uses `1.` to get the contents of `data.txt` as a list. Find the word that has the highest frequency of `a` and return it.

    **The answer is `appearance`**

***
   
## Writing to Files: 2-2

## CSV Files