# import time
# import sys
#
# toolbar_width = 40
#
# # setup toolbar
# sys.stdout.write("[%s]" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
#
# for i in range(toolbar_width):
#     time.sleep(0.1) # do real work here
#     # update the bar
#     sys.stdout.write("-")
#     sys.stdout.flush()
#
# sys.stdout.write("\n")
#


#
import time
import sys
sys.stdout.write("[%s]" % (" " * 10))
sys.stdout.flush()
sys.stdout.write("\b"*11)

for c in range(10):
    time.sleep(0.2)
    sys.stdout.write("=")
    sys.stdout.flush()
print("\n")
# sys.stdout.write("]")

############ SENSACIONAL!!! :
# import time
# import curses
#
# curses.initscr()
#
# rows = 10
# cols= 30
# winlist = []
# for r in range(2):
#     for c in range(2):
#         win = curses.newwin(rows, cols, r*rows, c*cols)
#         win.clear()
#         win.border()
#         winlist.append(win)
#
# for i in range(100):
#     for win in winlist:
#         win.addstr(5,5,"You have finished - %d%%"%i)
#         win.refresh()
#     time.sleep(.05)
# curses.endwin()