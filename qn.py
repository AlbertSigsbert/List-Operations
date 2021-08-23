
def insert(i, e):
    num.insert(i, e)


def printList(num):
    print(num)


def remove(e):
    num.remove(e)


def append(e):
    num.append(e)


def sort():
    num.sort()


def pop():
    num.pop()


def reverse():
    num.reverse()


N = int(input())
num = list()
for cmd in range(N):
    cmd = str(input())
    if cmd.startswith('insert'):
        arr = cmd.split()
        i = int(arr[1])
        e = int(arr[2])
        insert(i, e)

    elif cmd.startswith('print'):
        printList(num)

    elif cmd.startswith('remove'):
        arr = cmd.split()
        e = int(arr[1])
        remove(e)

    elif cmd.startswith('append'):
        arr = cmd.split()
        e = int(arr[1])
        append(e)

    elif cmd.startswith('sort'):
        sort()

    elif cmd.startswith('pop'):
        pop()

    elif cmd.startswith('reverse'):
        reverse()
