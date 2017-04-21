import JieLongManager
import JieLongUtils
import JieLongConfig
import threading


IDLE = 0
GAMING = 1

LENGTH_CHENGYU = 4


class Room:

    def __init__(self, user_id,is_group=False):
        # 是否是群聊，如果是私聊成语接龙，无延迟，随意聊
        self.isGroup = is_group

        self.wordsMap = JieLongManager.get_cheng_yu_map()

        self.timerGap = 0
        if is_group:
            self.timerGap = JieLongConfig.GroupChatGap
        else:
            self.timerGap = JieLongConfig.PrivateChatGap
        self.judgeTimer = threading.Timer(self.timerGap, self.judge_input)
        self.judgeTimer.setDaemon(True)
        self.userId = user_id

        # 游戏状态，有2个，一个是IDLE（空闲状态），另一个是GAMING（正在游戏中）
        self.gameStatus = IDLE
        self.timeOut = 0
        self.nowWord = None
        self.inputBuffer = []
        self.outputWarning = None
        self.outputGameResult = None
        pass

    def reset(self):
        self.gameStatus = IDLE
        self.timeOut = 0
        self.nowWord = None
        self.inputBuffer = []
        self.outputWarning = None
        self.outputGameResult = None

    def judge_input(self):
        for input_msg in self.inputBuffer:
            input_text = input_msg.get('Text')
            inputWord = JieLongManager.createChengYu(input_text)
            if inputWord == None:
                self.outputGameResult = ( '这些真的是成语吗？！不对吧，当前接龙成语是{0}，尾音是{1}'.format(self.nowWord.word,self.nowWord.getLastPinYin()).strip())
                continue
            if self.nowWord.matchWord(inputWord):
                # 匹配正确
                nextWord = self.wordsMap.getNextWord(inputWord.getLastPinYin().strip())
                self.nowWord = nextWord
                nickname = JieLongUtils.get_nickname(input_msg, True)
                self.outputGameResult = ( '恭喜{}！{}接龙正确，我接"{}"，尾音是{}'.format(nickname, inputWord.word,nextWord.word,nextWord.getLastPinYin()).strip())
                break
        JieLongUtils.send_msgs([self.outputWarning,self.outputGameResult], self.userId, self.isGroup)

        self.outputWarning = None
        self.outputGameResult = None
        if len(self.inputBuffer) == 0:
            self.timeOut += 1
        else:
            self.timeOut = 0
        self.inputBuffer.clear()
        if self.timeOut > 30:
            self.timeOut = 0
            self.end_game()
        else:
            self.judgeTimer = threading.Timer(self.timerGap, self.judge_input)
            self.judgeTimer.start()
        pass

    def input_msg(self, msg):
        if self.gameStatus == IDLE:
            return
        text = msg.get('Text')
        if len(text) != LENGTH_CHENGYU:
            return

        self.inputBuffer.append(msg)
        pass

    # 游戏开始
    def start_game(self):
        if self.gameStatus == GAMING:
            self.outputWarning = JieLongConfig.WARNING_IN_GAME
            return
        self.nowWord = self.wordsMap.getRandomChengYu()
        start_word_text = JieLongConfig.getGameStartWords()
        send_text = start_word_text.format(self.nowWord.word, self.nowWord.getLastPinYin()).strip()
        JieLongUtils.send_msg(send_text, self.userId, self.isGroup)
        self.gameStatus = GAMING
        self.judgeTimer = threading.Timer(self.timerGap, self.judge_input)
        self.judgeTimer.start()
        pass

    # 游戏结束
    def end_game(self):
        end_word_text = JieLongConfig.getGameEndWords()
        send_text = end_word_text
        JieLongUtils.send_msg(send_text, self.userId, self.isGroup)

        self.reset()
        self.judgeTimer.cancel()
        pass

    def switch_word(self):
        lastPY = self.nowWord.getLastPinYin()
        now_word = self.wordsMap.getNextWord(lastPY)
        self.nowWord = now_word
        switch_word_text = JieLongConfig.getSwitchWords()
        send_text = switch_word_text.format(now_word.word, now_word.getLastPinYin()).strip()
        JieLongUtils.send_msg(send_text, self.userId, self.isGroup)
        pass


