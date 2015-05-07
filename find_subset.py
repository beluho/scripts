
list = [] ##your comma separated list of numbers


fun = ##the number you’re trying to reach

def subsetsum(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]

        else:
            with_v = subsetsum(array[1:],(num - array[0]))
            if with_v:
                print [array[0]] + with_v
                return [array[0]] + with_v

            else:
                print subsetsum(array[1:],num)
                return subsetsum(array[1:],num)


subsetsum(list, fun)
