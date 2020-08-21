"""
name: star428
time: 2020/8/21 09:39:26
"""


def quickSort(aList):
    quickSortHelper(aList, 0, len(aList - 1))


def quickSortHelper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quickSortHelper(alist, first, split_point - 1)
        quickSortHelper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark += 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = \
                alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = \
        alist[rightmark], alist[first]

    return rightmark


# test
aList = [1, 2, 23, 657, 67, 23, 23, 5, 23, 2, 2, 87, 9, 34, 89, 34, 9]
quickSort(aList)
