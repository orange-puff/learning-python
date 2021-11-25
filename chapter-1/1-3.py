def list_section():
    print('\nLIST SECTION')
    arr = [1, 2, 3, 4, 5]
    arr += [10, 11, 12]

    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr[2:5])

    arr.append(155)
    print(arr)
    print(arr[-1])

    arr.remove(1)
    print(arr)

    if 1 in arr:
        pass
    else:
        print('1 is not in arr')

def set_section():
    print('\nSET SECTION')
    s = set()
    s.add(1)
    for i in range(0, 5):
        s.add(i)

    print(i)

    if 1 in s:
        print('1 is in s')

def tuple_section():
    print('\nTUPLE SECTION')
    t1 = tuple([1, 2, 3])
    t2 = 2, 3
    print(t1)
    print(t2)

    print(t2[0])
    print(t2[-1])

def dictionary_section():
    print('\nDICTIONARY SECTION')
    d = {}
    d['hello'] = 5
    d[5] = 'hello'
    d[123] = 0
    print(d)

    del(d[123])
    print(d)

    d = {1: 2, 3: 4, 5: 6, 7: 8}
    for key, val in d.items():
        print(key, val)

    for key in d.keys():
        print(key)

    for val in d.values():
        print(val)

    # let's create a counter of the values in arr, to see how frequent the elements show up
    arr = [1, 2, 1, 4, 199, 4, 204, 203, 202, 200, 199]
    counter = {}
    for val in arr:
        # can be: if val not in counter.keys()
        if val not in counter:
            counter[val] = 0
        counter[val] += 1

    print(counter)


if __name__=='__main__':
    list_section()
    set_section()
    tuple_section()
    dictionary_section()