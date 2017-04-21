__author__ = 'RobinLin'
import random


class ChengYu:
    def __init__(self,line):
        self.word = None
        self.pinyins = []
        arrPinyin = line.split(' ')
        self.word = arrPinyin[0]
        for i in range(1,len(arrPinyin)):
            self.pinyins.append(arrPinyin[i].strip())

    def getFirstPinYin(self):
        return self.pinyins[0]

    def getLastPinYin(self):
        return self.pinyins[len(self.pinyins)-1]

    def matchWord(self,nextWord):
        lastPinYin = self.getLastPinYin().strip()
        nextFirstPinYin = nextWord.getFirstPinYin().strip()
        if lastPinYin == nextFirstPinYin:
            return True
        return False


class ChengYuMap:
    def __init__(self):
        self.ChengYuList = []
        self.Words = []
        self.ChengYuMap = {}
        return

    def add(self, chengYu):
        firstPinYin = chengYu.getFirstPinYin()
        list = []
        if self.ChengYuMap.get(firstPinYin) != None:
            list = self.ChengYuMap.get(firstPinYin)
        list.append(chengYu)
        self.Words.append(chengYu.word)
        self.ChengYuList.append(chengYu)
        self.ChengYuMap[firstPinYin] = list
        return

    def getNextWord(self,lastPinYin):
        chengyuList = self.ChengYuMap.get(lastPinYin)
        return chengyuList[random.randint(0,len(chengyuList)-1)]

    def isChengYu(self,word):
        if word in self.Words:
            return True
        return False

    def getRandomChengYu(self):
        return self.ChengYuList[random.randint(0,len(self.ChengYuList)-1)]
        pass
