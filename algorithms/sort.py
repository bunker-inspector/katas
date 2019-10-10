def merge(a, b):
    merged = []
    ai, bi = 0,0
    al, bl = len(a), len(b)
    while ai < al or bi < bl:
        if ai == al and bi < bl:
            merged.append(b[bi])
            bi += 1
        elif bi == bl and ai < al:
            merged.append(a[ai])
            ai += 1
        elif a[ai] < b[bi]:
            merged.append(a[ai])
            ai += 1
        else:
            merged.append(b[bi])
            bi += 1
    return merged

def _merge_sort(arr, start, end):
    mid = (end + start) // 2
    if (end - start) <= 1:
        return [arr[start]]
    else:
        return merge(_merge_sort(arr, start, mid), _merge_sort(arr, mid, end))

def merge_sort(arr):
    ln = len(arr)
    return _merge_sort(arr, 0, ln)


if __name__ == '__main__':
    print("t".islower())
   # import random

   # l = list(range(10000))
   # random.shuffle(l)
   # print(merge_sort(l))
