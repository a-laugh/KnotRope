# coding: utf-8

import os


def is_chinese(ch):
    if u'\u4e00' <= ch <= u'\u9fa5':
        return True
    else:
        return False


class KnotRope(object):
    def __init__(self, directory):
        self._dir = directory
        self._dict = {}

    def analyze_file(self, path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                for ch in line:
                    if not is_chinese(ch):
                        continue

                    if ch in self._dict:
                        self._dict[ch] += 1
                    else:
                        self._dict[ch] = 1

    def run(self):
        for root, dirs, files in os.walk(self._dir):
            for f in files:
                path = os.path.join(root, f)
                self.analyze_file(path)

        return self._dict
