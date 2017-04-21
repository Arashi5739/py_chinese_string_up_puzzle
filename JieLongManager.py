from pypinyin import lazy_pinyin
from JieLongEntity import *

input_file = open('chengyujielong.txt', 'r', encoding='utf-8')
lines = input_file.readlines()
input_file.close()

_chengYuMap = ChengYuMap()


def get_cheng_yu_map():
    return _chengYuMap

for line in lines:
    line = line.strip()
    if line == '':
        continue
    chengyu = ChengYu(line)
    _chengYuMap.add(chengyu)

def createChengYu(msg):
    if msg not in _chengYuMap.Words:
        return None
    pinyins = lazy_pinyin(msg)
    pinyinstream = ''
    for pinyin in pinyins:
        pinyinstream += ' ' + pinyin
    line = '{0}{1}'.format(msg, pinyinstream)
    return ChengYu(line)

