import time,sys

indent = 0
indenIncreasing = True

try:
    while True:
        print(' ' * indent,end='')
        print('********')
        time.sleep(0.1)

        if indenIncreasing:
            indent=indent + 1
            if indent == 20:
                indenIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indenIncreasing = True
except KeyboardInterrupt:
    sys.exit()