def descending_order(num):
    # global l_num
    l_num = [int(i) for i in str(num)]  # converting number to array.
    # print(l_num)
    def quicksort(array):

        ## We define our 3 arrays
        less = []
        equal = []
        greater = []

        ## if the length of our array is greater than 1
        ## we perform a sort
        if len(array) > 1:
            ## Select our pivot. This doesn't have to be
            ## the first element of our array
            pivot = array[0]

            ## recursively go through every element
            ## of the array passed in and sort appropriately
            for x in array:
                if x < pivot:
                    less.append(x)
                if x == pivot:
                    equal.append(x)
                if x > pivot:
                    greater.append(x)

            ## recursively call quicksort on gradually smaller and smaller
            ## arrays until we have a sorted list.
            # return quicksort(less) + equal + quicksort(greater)
            return quicksort(greater) + equal + quicksort(less)

        else:
            return array
    # print(quicksort(array=l_num))
    sorted_list = quicksort(array=l_num)
    for i in sorted_list:
        print(i, end='')


descending_order(445478545521)