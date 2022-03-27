import curses
import time
from curses import COLOR_CYAN, wrapper
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(5,25,"Welcome to speed test!!",curses.color_pair(3))
    stdscr.addstr(7,25,"press any key to begin",curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()
def display_text(stdscr,target,current,wpm=0):
  stdscr.addstr(target,curses.color_pair(3))
  stdscr.addstr(1,0, f"WPM:{wpm}")
  
  for i , char in enumerate(current):
      correct_char=target[i]
      color=curses.color_pair(1)
      if char !=correct_char:
          color=curses.color_pair(2)

      stdscr.addstr(0,i,char, color)
      
def load_text():
 with open("type.txt","r") as f:
     lines=f.readlines()
     return random.choice(lines).strip()#.strip is to remove \n
def wpm_test(stdscr):
    target_text=load_text()
    current_text=[]
    wpm =0
    start_time=time.time()
    stdscr.nodelay(True)
  

    
    while(True):
        time_elapsed =max(time.time() - start_time,1)
        wpm=round((len(current_text)/(time_elapsed/60))/5)

        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()
        if "".join(current_text)==target_text:
            stdscr.nodelay(False)
            break



        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key)==27:
            break
        if key in ("KEY_BACKSPACE",'\b',"\X7F"):
            if(len(current_text)>0):
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)

       

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN , curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(3,curses.COLOR_BLUE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    
    while(True):
      wpm_test(stdscr)
      stdscr.addstr(2,0,"YOu completed the test--press any key to continue")
      stdscr.addstr(3,20,"press escape to exit")
      ket=stdscr.getkey()
      if ord(ket)==27:
        break

 
    #time.sleep(1)

wrapper(main)
