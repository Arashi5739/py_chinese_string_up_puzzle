__author__ = 'RobinLin'
import itchat
import time


def send_msg(msg, user_id, is_group = False):
    print('itchat send:',user_id,msg)
    itchat.send(msg,user_id)
    if is_group :
        time.sleep(5)
    pass


def send_msgs(msgs, user_id, is_group=False):
    strs = ''
    for msg in msgs:
        if msg is None:
            continue
        if msg == '':
            continue
        strs += "{0}\n".format(msg)
    strs = strs.strip()
    if strs != '':
        send_msg(strs, user_id, is_group)
    pass


def get_nickname(msg, is_group=False):
    nickname = ''
    try:
        if is_group:
            nickname = msg.get('ActualNickName')
        else:
            user = msg.get('User')
            if user is None:
                nickname = ''
            else:
                nickname = user.get('NickName')
                if nickname is None:
                    nickname = ''
    except:
        pass
    return nickname




