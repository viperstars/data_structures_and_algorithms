def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst) - 1):
            if lst[i] > lst[j - 1]:
                lst[i], lst[j - 1] = lst[j - 1], lst[i]


def insertion_sort(lst):
    for i in range(0, len(lst)):
        j = i
        while j > 1 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1


def selection_sort(lst):
    for i in range(0, len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]


def shell_sort(lst):
    length = len(lst)
    h = 1
    while h < length / 3:
        h = h * 3 + 1
    while h >= 1:
        for i in range(h, length):
            j = i
            while j > 0 and lst[j] < lst[j - h]:
                lst[j], lst[j - h] = lst[j - h], lst[j]
                j -= h
        h /= 3


def quick_sort(lst):
    def q_sort(lst, begin, end):
        if begin >= end:
            return
        p = lst[begin]
        i = begin
        for j in range(begin + 1, end + 1):
            if lst[j] < p:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]
        q_sort(lst, begin, i - 1)
        q_sort(lst, i + 1, end)

    q_sort(lst, 0, len(lst) - 1)


def merge(lf, lt, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lf[i] < lf[j]:
            lt[k] = lf[i]
            i += 1
        else:
            lt[k] = lf[j]
            j += 1
        k += 1
    while i < mid:
        lt[k] = lf[i]
        i += 1
        k += 1
    while j < high:
        lt[k] = lf[j]
        j += 1
        k += 1


def merge_pass(lf, lt, llen, slen):
    i = 0
    while i + 2 * slen < llen:
        merge(lf, lt, i, i + slen, i + 2 * slen)
        i += 2 * slen
    if i + slen < llen:
        merge(lf, lt, i, i + slen, llen)
    else:
        for j in range(i, llen):
            lt[j] = lf[j]


def merge_sort(lst):
    slen, llen = 1, len(lst)
    tmplst = [None] * llen
    while slen < llen:
        merge_pass(lst, tmplst, llen, slen)
        slen *= 2
        merge_pass(tmplst, lst, llen, slen)
        slen *= 2
