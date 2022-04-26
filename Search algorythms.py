# unordered linear search
def linear_search(seq, item):
    for i in seq:
        if item == i:
            #print(f'{item} found at index {seq.index(i)}')
            return seq.index(i)
    #print(f'{item} not found')
    return None

# ordered linear search
def linear_search_ord(seq, item):
    for i in seq:
        if item == i:
            #print(f'{item} found at index {seq.index(i)}')
            return seq.index(i)
        elif item < i:
            #print(f'{item} not found')
            return None

# very fast search in ordered lists and arrays
def binary_search(seq, item):
    end_idx = len(seq) - 1
    start_idx = 0
    while start_idx <= end_idx:
        mid = (start_idx + end_idx) // 2
        if item == seq[mid]:
            return mid
        elif item > seq[mid]:
            start_idx = mid + 1
        else:
            end_idx = mid - 1
    return None

# greater efficiency than binary search if items are rather equally distributed
def interpolation_search(seq, item):
    end_idx = len(seq) - 1
    start_idx = 0
    while start_idx <= end_idx:
        mid = start_idx + ((end_idx - start_idx) // (seq[end_idx] - seq[start_idx])) * (item - seq[start_idx])
        if item == seq[mid]:
            return mid
        elif mid > end_idx or mid < start_idx:
            return None
        elif item > seq[mid]:
            start_idx = mid + 1
        else:
            end_idx = mid - 1
