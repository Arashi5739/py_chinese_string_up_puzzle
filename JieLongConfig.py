import random
# 群聊间隔时间，秒
GroupChatGap = 10
# 私聊间隔时间，秒
PrivateChatGap = 2

WARNING_IN_GAME = '已经在成语接龙中，请勿重复开启游戏'

StartGameWords = [
    '开始游戏',
    '游戏开始',
    '成语接龙',
    '开启游戏'
]

EndGameWords = [
    '结束游戏',
    '关闭游戏',
    '游戏结束'
]

CMD_SwitchWords = [
    '换一个',
    '太难了'
]

GameStartWords = [
    '欢迎开始游戏接龙，我先起个头：{0}，尾音是{1},如果觉得太难就输入：换一个，不玩了就输入：结束游戏~）'
]

GameEndWords = [
    '结束成语接龙游戏，下次再见'
]

SwitchWords = [
    '好吧，是不是太难了，那我自己来接：{0}，尾音是{1}'
]

def getRandomWords(strs):
    if strs is None:
        return None
    l = len(strs)
    if l == 1:
        return strs[0]
    return strs[random.randint(0,l)]


def getGameStartWords():
    return getRandomWords(GameStartWords)

def getGameEndWords():
    return getRandomWords(GameEndWords)

def getSwitchWords():
    return getRandomWords(SwitchWords)
