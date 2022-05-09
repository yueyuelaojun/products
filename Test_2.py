# function 函式/功能

def wash(dry):
    print('加水')
    print('加洗衣精')
    print('旋转')
    if dry:
        print('烘衣')


wash(False)
wash(True)


def say_hi():
    print('hi')


# say_hi()

def add(x, y):
    return x + y


print(add(3, 4))


def average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg


print(average([1, 2, 3]))
print(average([23, 32, 6]))
print(average([180, 34, 92]))