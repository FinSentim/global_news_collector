import time



def dum():
    p = 0
    for i in range(100_000_000):
        p=p+1
    
    print(p)

if __name__=="__main__":
    start = time.time()
    dum()
    end = time.time()
    print("Elapsed time " + str(end-start))