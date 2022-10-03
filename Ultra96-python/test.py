import threading
 
 
def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))
 
 
def print_square(value):
    value.append(10)
    
 
 
if __name__ =="__main__":
    # creating thread
    mylist = []
    t1 = threading.Thread(target=print_square, args=(mylist,))
 
    # starting thread 1
    t1.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    print(mylist)
    # both threads completely executed
    print("Done!")