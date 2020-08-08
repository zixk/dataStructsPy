
def bubblesort(array: [int]):
    isSorted = False
    lastUnsorted = len(array)-1
    while(not isSorted):
        isSorted = True
        for i in range(0, lastUnsorted):
            if(array[i] > array[i+1]):
                swap(array, i, i+1)
                isSorted = False
        lastUnsorted-=1

def swap(array: [int], index1: int, index2: int):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

if __name__ == "__main__":
    ex = [19,84,1,2,6,4,3,5,9,15]
    bubblesort(ex)
    print(ex)