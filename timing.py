import timeit
def timing(func):
    t = timeit.timeit(lambda: func)
    print (t)
    

#import time
#def lengthh(func,value):
#    start_time= time.time()
#    func(value)
#    return ("--- %s seconds ---" % (time.time() - start_time))