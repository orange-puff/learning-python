def for_loop(n):
    for i in range(n):
        print(i)

def while_loop(n):
    i = 0
    while i < len(n):
        print(i)

def function_with_return():
    return 155

def function_without_return():
    print(155)

if __name__=='__main__':
    for_loop(10)
    while_loop(10)
    print(function_with_return())
    function_without_return()
    x = 5
    y = 2.7