
def whatFlavors(cost, money):
    cost_dict = {}
    for i,icost in enumerate(cost):
        print(i)
        if money-icost in cost_dict:
            print(str(cost_dict[money-icost]+1) + ' ' + str(i+1))
            return 
        else:
            cost_dict[icost] = i

if __name__ == "__main__":

    menu = [5,9,5,4,2,6,5]
    whatFlavors(menu, 10)    
