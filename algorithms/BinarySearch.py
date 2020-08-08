
def binarySearchRecursive(array: [int], x: int, left: int, right: int) -> bool:
    if(left > right):
        return False
    mid = int((left + right)/2)
    if(x == array[mid]):
        return True
    elif(x > array[mid]):
        return binarySearchRecursive(array, x, mid+1, right)
    else:
        return binarySearchRecursive(array, x, left, mid-1)

def binarySearchRecursiveMain(array: [int], x: int) -> bool:
    return binarySearchRecursive(array, x, 0, len(array)-1)

def binarySearchIterative(array: [int], x: int) -> bool:
    left = 0
    right = len(array)-1

    while(left <= right):
        mid = int((left + right)/2)
        if(x == array[mid]):
            return True
        elif(x > array[mid]):
            left = mid+1
        else:
            right = mid-1
    return False

if __name__ == "__main__":
    ex = sorted([1,2,54,23,65,23,68,63,23,53])

    print(binarySearchRecursiveMain(ex, 54))
    print(binarySearchRecursiveMain(ex, 3))
    print(binarySearchIterative(ex, 54))
    print(binarySearchIterative(ex, 3))

    ex2 = sorted(['a','h','t','y','z','f','g','j','q'])
    print(binarySearchRecursiveMain(ex2, 'h'))
    print(binarySearchIterative(ex2, 'h'))
    print(binarySearchRecursiveMain(ex2, 'b'))
    print(binarySearchIterative(ex2, 'b'))
