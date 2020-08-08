
def quicksortMain(array: [int]):
    return quicksort(array, 0, len(array)-1)
    
def quicksort(array:[int], left: int, right: int):
    if(left >= right):
        return
    pivot = array[int((left+right)/2)]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index-1)
    quicksort(array, index, right)

def partition(array: [int], left: int, right: int, pivot: int) -> int:
    while(left <= right):
        while(array[left] < pivot):
            left += 1
        while(array[right] > pivot):
            right -= 1
        if(left <= right):
            swap(array, left, right)
            left+=1
            right-=1
    return left
            
def swap(array: [int], left: int, right: int):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

if __name__ == "__main__":
    ex = [19,84,1,2,6,4,3,5,9]
    quicksortMain(ex)
    print(ex)