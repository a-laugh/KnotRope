#!/usr/bin/env python3
# coding: utf-8

import sys
import logging

from knot_rope import KnotRope

if __name__ == '__main__':
    if len(sys.argv) != 2:
        logging.error("usage: ./elementary_chinese_characters.py /path/to/dir")

    rope = KnotRope(sys.argv[1])
    info = rope.run()

    sorted_info = sorted(info.items(), key=lambda x: x[1], reverse=True)
    no = 0
    no_1000 = 0
    for ch, _ in sorted_info:
        no += 1

        print(ch, end="")
        if no % 3 == 0:
            print("，", end="")
        if no % (3*6) == 0:
            print()
        if no % (3*6*4) == 0:
            print()
            if int(no/1000) != no_1000:
                no_1000 = int(no/1000)
                print("============== Top %d ==============" % (no_1000*1000))
                print()
