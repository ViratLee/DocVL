import win32api, win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click_at = 150
plus = 200
if __name__ == '__main__':
    try:
        while True:
            time.sleep(5) # Delay for 18 seconds.
            click(click_at,10)
            time.sleep(5) # Delay for 18 seconds.
            click_at += plus
            click(click_at,10)
            time.sleep(5) # Delay for 18 seconds.
            click_at += plus
            click(click_at,10)
            time.sleep(5) # Delay for 18 seconds.
            click_at += plus
            click(click_at,10)
            click_at = 10
    except KeyboardInterrupt:
        print('\nDone.')