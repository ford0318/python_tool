import time
from multiprocessing import Pool

def run(fn) :  
  time.sleep(2)  
  print(fn)

if __name__ == "__main__" :  
    startTime = time.time()  
    testFL = [1,2,3,4,5] # run function 的參數
    pool = Pool() # Pool() 不放參數則默認使用電腦核的數量
    pool.map(run,testFL) 
    pool.close()
    pool.join()     
    endTime = time.time()  
    print("time :", endTime - startTime) 