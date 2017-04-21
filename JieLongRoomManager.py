import JieLongConfig
import JieLongRoom


# 游戏房间管理类
class RoomManager:

    # 单例，管理房间
    _sManager = None

    def __init__(self):
        self.roomMap = {}
        pass

    def get_room(self, user_id, is_group=False):
        room = self.roomMap.get(user_id)
        if room is None:
            room = JieLongRoom.Room(user_id, is_group)
            self.roomMap[user_id] = room
        return room

    @staticmethod
    def get_instance():
        if RoomManager._sManager is None:
            RoomManager._sManager = RoomManager()
        return RoomManager._sManager

    @staticmethod
    def get_input_msg(msg):
        manager = RoomManager.get_instance()
        user_id = msg.get('FromUserName')
        is_group = False
        if user_id.find('@@') >= 0:
            is_group = True
        text = msg.get('Text')
        room = manager.get_room(user_id, is_group)
        if text in JieLongConfig.StartGameWords:
            room.start_game()
            pass
        elif text in JieLongConfig.EndGameWords:
            room.end_game()
            pass
        elif text in JieLongConfig.CMD_SwitchWords:
            room.switch_word()
            pass
        else:
            room.input_msg(msg)
            pass
        pass
