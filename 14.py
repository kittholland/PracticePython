def set_deduper(l):
    return list(set(l))

def loop_deduper(l):
    results = []
    for item in l:
        if item not in results:
            results.append(item)
    return results

l = [1,2,3,4,5,6,1,2,3,9,9,9]

print(set_deduper(l))
print(loop_deduper(l))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_deduper(a, b):
    return(list(set([number for number in a if number in b])))

print(list_deduper(a, b))