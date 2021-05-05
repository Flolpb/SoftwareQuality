import time


def readFile(filename):
    print("Reading the file...")
    file = open(filename, "r")
    numbers = []
    for line in file:
        items = line.split()
        for item in items:
            if item[0] == "-":
                if item[1:].isdigit():
                    numbers.append(int(item))

            if item.isdigit():
                numbers.append(int(item))
    time.sleep(0.8)
    shellSort(numbers)


def shellSort(array):
    n = len(array)
    gap = n//2
    print("The list of number is under treatment... ")
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    time.sleep(1)
    print("list of number sorted: ")
    time.sleep(0.5)
    for nb in array:
        time.sleep(0.3)
        print("- " + str(nb))


if __name__ == '__main__':
    readFile("numbers.txt")


