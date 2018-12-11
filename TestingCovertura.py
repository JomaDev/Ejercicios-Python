# SPECIFICATION:
#
# The stats function computes some basic statistics functions
# when given a list of numbers as input.
#
# TASK:
#
# Achieve full statement coverage on the stats function. 
# All you should have to do is modify the test function 
# to call stats with different lists of values.

def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        i=abs(i)
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted)%2 == 0:
        middle = len(lst_sorted)//2
        median = (lst_sorted[middle] + lst_sorted[middle-1])//2
    else:
        median = lst_sorted[len(lst_sorted)//2]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append (num)
    print ("list = " + str(lst))
    print ("min = " + str(min))
    print ("max = " + str(max))
    print ("median = " + str(median))
    print ("mode(s) = " + str(mode))

def test1():
    l = [31,32,33,33,34]
    stats(l)
    l = [31,32,33,33]
    stats(l)
    pass

def test2():
    l = [-33,-34]
    stats(l)
    l = [31,32,33,33]
    stats(l)
    l = [31,32,33]
    stats(l)
    pass

test1()
test2()