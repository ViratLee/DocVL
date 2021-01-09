import win32api, win32con
import time
import threading

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def run(stop): 
    count = 0
    while True: 
        #click(10,10)
        #time.sleep(10) # Delay for 18 seconds.
        #click(500,500)
        click(50,10)
        time.sleep(10) # Delay for 18 seconds.
        if stop(): 
            break    

if __name__ == '__main__':
    stop_threads = False
    t1 = threading.Thread(target = run, args =(lambda : stop_threads, )) 
    t1.start() 
    input("Press Enter to exit...")
    stop_threads = True
    t1.join()