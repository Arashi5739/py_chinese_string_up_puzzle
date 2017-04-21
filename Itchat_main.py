import itchat, time
from itchat.content import *
import JieLongUtils
import JieLongRoomManager


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print(msg)
    JieLongRoomManager.RoomManager.get_input_msg(msg)
    pass


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    return


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
    return


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    group_id = msg.fromUserName
    nickname = JieLongUtils.get_nickname(msg)
    if nickname == '测试群':
        print(msg)
    if msg.isAt:
        JieLongUtils.send_msg('指令：【成语接龙】 【换一个】 【结束游戏】', group_id, True)
        return
    else:
        JieLongRoomManager.RoomManager.get_input_msg(msg)


# 扫码登录，开启成语机器人
itchat.auto_login(True)
itchat.run(True)