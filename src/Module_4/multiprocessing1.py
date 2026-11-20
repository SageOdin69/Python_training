import time
import multiprocessing
 
def Task_1():
    for i in range(5):
        print("Task 1 is running")
        time.sleep(1)
def Task_2():
    for i in range(5):
        print("Task 2 is running")
        time.sleep(1)
 
if __name__ == '__main__':
    P1=multiprocessing.Process(target=Task_1)
    P2=multiprocessing.Process(target=Task_2)
    P1.start()
    P2.start()
    P1.join()
    P2.join()
 
    print("All tasks are completed")