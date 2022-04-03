from build.gui import fullgui
from manual_control import task1start, task1stop

def main():
    
    fullgui(task1start,task1stop,print("task2start"),print('task2stop'),
    print('task3start'),print('task3stop'),print('task3pause'))

if __name__ == "__main__":
    main()