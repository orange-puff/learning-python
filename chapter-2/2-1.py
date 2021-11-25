def clean(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def clean_pure(lines):
    to_ret = [line for line in lines]
    for i in range(len(lines)):
        to_ret[i] = to_ret[i].strip()
    return to_ret

def clean_pure2(lines):
    to_ret = []
    for line in lines:
        to_ret.append(line.strip())
    return to_ret

def test(lines):
    to_ret = ''
    max_a = 0
    for line in lines:
        m = {}
        for c in line:
            if c not in m:
                m[c] = 0
            m[c] += 1
        if 'a' in m and m['a'] > max_a:
            max_a = m['a']
            to_ret = line

    print(to_ret)


if __name__=='__main__':
    file = open('data.txt')

    arr = list(file.readlines())
    print(arr[:5])

    clean(arr)
    print(arr[:5])

    test(arr)
