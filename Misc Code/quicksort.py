def quick_sort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop()

    items_greater = []
    items_lower = []

    for item in seq:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)