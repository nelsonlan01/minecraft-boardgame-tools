import random

t = open("sample.txt", encoding="utf-8")

result = []
check = []
global same
same = 0


def initial_result_array():
    for i in range(0, 6):
        result.append(0)


def print_result():
    result.sort()
    print("\nToday rolled out numbers are...\n ============== \n")
    print(result)
    print("\n==============")


def check_result(t):
    for i in range(len(t)):
        num = t[i]
        if num in result:
            same += 1


# def check_result():


initial_result_array()

result = random.sample(range(1, 51), 6)

print_result()
check_result(t.readline())
print(same)