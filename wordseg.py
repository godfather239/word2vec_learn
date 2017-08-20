#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import re
import codecs
import jieba.posseg as pseg
import jieba
from common import *
from config import CONFIG


@log
def load_stop_words(filepath):
    stop_words_dict = {}
    for line in codecs.open(filepath, 'r', 'utf-8'):
        line = remove_control_chars(line)
        stop_words_dict[line] = 1
    stop_puncs = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~。？！，、；：“”‘’（）·《》〈〉＋【】•'''
    for ch in stop_puncs.decode('utf-8'):
        stop_words_dict[ch] = 1
    return stop_words_dict


g_filtered_postags = {'m', 'q'}
g_stop_words = load_stop_words('stop_words.dic')


@log
def seg_search_word(filepath, stop_words_dict):
    # input file format: <search_word_no>____<search_word>
    out_file = codecs.open(CONFIG['data_dir'] + '/search_word.seg', 'w', 'utf-8')
    for line in codecs.open(filepath, 'r', 'utf-8'):
        line = line.replace('\n', '')
        line = remove_control_chars(line)
        arr = line.split('____')
        if len(arr) < 2:
            continue
        pos = 1
        for word, flag in pseg.cut(arr[1]):
            if is_word_invalid(word, flag):
                continue
            out_file.write('%s____%s____%s____%d\n' % (line, word, flag, pos))
            pos += 1
    out_file.close()


@log
def seg_product_short_name(filepath, stop_words_dict):
    # Input file format: <product_id>____<product_short_name>
    out_file = codecs.open(CONFIG['data_dir'] + '/product_short_name.seg', 'w', 'utf-8')
    for line in codecs.open(filepath, 'r', 'utf-8'):
        line = line.replace('\n', '')
        line = remove_control_chars(line)
        arr = line.split('____')
        if len(arr) != 4:
            continue
        res = ''
        for word, flag in pseg.cut(','.join(arr[1:2]).lower()):
            if is_word_invalid(word, flag):
                continue
            res += word + ' '
        out_file.write('%s\n' % res)
    out_file.close()


def is_word_invalid(word, postag):
    if word in g_stop_words or postag in g_filtered_postags or (postag=='x' and re.match(r'[\+\-\#\.]+', word)):
        return True
    else:
        return False


if __name__ == '__main__':
    jieba.load_userdict("words-jumei.dic")
    conf = ConfigParser.ConfigParser()
    conf.read(CONFIG['data_dir'] + '/sedata.flag')

    stop_words_dict = load_stop_words('stop_words.dic')
    # seg_search_word(CONFIG['data_dir'] + '/' + conf.get('table', 'search_word'), stop_words_dict)
    seg_product_short_name(CONFIG['data_dir'] + '/' + conf.get('table', 'product_short_name'), stop_words_dict)

