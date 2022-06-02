#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    add_num = 0

    for j in sys.argv[i:]:
        add_num += int(j)
        i += 1
    print("{:d}".format(add_num))
