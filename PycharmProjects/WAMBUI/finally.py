import time

f = None
try:
    f = open("poem.txt")
    while True:#our usual file-readiing idiom
        line = f.readline()
        break
        print(line,end="",flush=True)
        time.sleep(2)#To make sure it runs for a while
except FileNotFoundError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("Cleaning up: Closed the file")