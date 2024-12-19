# 30
def series30(collections):
    results = []
    for collection in collections:
        results.append(sum(collection))
    return results


n, k = 3, 2
collections = [[1, 2, 3], [4, 5, 6]]
print(series30(collections)) 
# 31
def series31(collections):
    count = 0
    for collection in collections:
        if 2 in collection:
            count += 1
    return count


n, k = 3, 2
collections = [[1, 2, 3], [4, 5, 6]]
print(series31(collections))  
# 32
def series32(collections):
    results = []
    for collection in collections:
        if 2 in collection:
            results.append(collection.index(2) + 1)  
        else:
            results.append(0)
    return results


n, k = 3, 2
collections = [[1, 2, 3], [4, 5, 6]]
print(series32(collections)) 
# 33
def series33(collections):
    results = []
    for collection in collections:
        if 2 in collection:
            results.append(len(collection) - collection[::-1].index(2)) 
        else:
            results.append(0)
    return results


n, k = 3, 2
collections = [[1, 2, 3, 2], [4, 5, 6]]
print(series33(collections)) 
# 34
def series34(collections):
    results = []
    for collection in collections:
        if 2 in collection:
            results.append(sum(collection))
        else:
            results.append(0)
    return results


n, k = 3, 2
collections = [[1, 2, 3], [4, 5, 6]]
print(series34(collections))  
# 35
def series35(collections):
    results = []
    for collection in collections:
        results.append(len(collection) - 1)  
    return results


collections = [[1, 2, 0], [4, 5, 6, 0]]
print(series35(collections))  
# 36
def series36(collections):
    count = 0
    for collection in collections:
        if all(x < y for x, y in zip(collection, collection[1:])):
            count += 1
    return count


collections = [[1, 2, 3, 0], [1, 2, 3, 4, 0]]
print(series36(collections)) 
# 37
def series37(collections):
    count = 0
    for collection in collections:
        if all(x < y for x, y in zip(collection, collection[1:])) or \
           all(x > y for x, y in zip(collection, collection[1:])):
            count += 1
    return count

collections = [[1, 2, 3, 0], [4, 3, 2, 1, 0]]
print(series37(collections)) 
# 38
def series38(collections):
    results = []
    for collection in collections:
        if all(x < y for x, y in zip(collection, collection[1:])):
            results.append(1)
        elif all(x > y for x, y in zip(collection, collection[1:])):
            results.append(-1)
        else:
            results.append(0)
    return results


collections = [[1, 2, 3, 0], [4, 3, 2, 1, 0], [1, 3, 2, 0]]
print(series38(collections))  
