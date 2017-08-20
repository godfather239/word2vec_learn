#!/usr/bin/env python
# encoding=utf-8
import time
import re


def log(func):
    def wrapper(*args, **kvargs):
        print ('[%s] *********** Start function %s ***********' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), func.__name__))
        ret = func(*args, **kvargs)
        print ('[%s] *********** Finish function %s **********' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), func.__name__))
        return ret
    return wrapper


def remove_control_chars(s):
    control_chars = ''.join(map(unichr, range(0,32) + range(127,160)))
    control_char_re = re.compile('[%s]' % re.escape(control_chars))
    return control_char_re.sub('', s)
