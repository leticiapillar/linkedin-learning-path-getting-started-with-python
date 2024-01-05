# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        pass
        # TODO: calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # TODO: if item is found, return the index
        if item == itemlist[midPt]:
            return midPt

        # TODO: otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(" 23 is in the list?", binarysearch(23, items))
print(" 87 is in the list?", binarysearch(87, items))
print("250 is in the list?", binarysearch(250, items))
