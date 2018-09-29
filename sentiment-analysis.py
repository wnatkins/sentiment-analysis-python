from __future__ import division
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as mplot
import numpy as np
import glob

words = []
values = []
uniqueWordsAF = []
negativeWords = []
weakNegative = []
neutral = []
weakPositive = []
positive = []
y = []
uniqueWordsBG = []

afscript = sorted(glob.glob('a*script.txt'))
afscript = afscript[0:21]

bgscript = sorted(glob.glob('bg*script.txt'))
bgscript = bgscript[0:12]

for b in bgscript:
    battlestar = open(b, "r").read().split(" ")

for f in afscript:
    affirmingflame = open(f, "r").read().split(" ")


file = open("sentiment_lex.csv", "r")
data = file.read()
data = data.split("\n")


for line in data:
    line = line.split(",")
    words.append(line[0])
    values.append(float(line[1]))

showName = raw_input("\nEnter series name: ")

if showName.lower() == "affirming flame" or showName.lower() == "an affirming flame":
    for x in range(0, len(words)):
        if words[x] in affirmingflame:
            uniqueWordsAF.append(words[x])
            if values[x] >= -1.0 and values[x] < -0.6:
                negativeWords.append(words[x])
                count = len(negativeWords)
            elif values[x] > -0.6 and values[x] <= -0.2:
                weakNegative.append(words[x])
                wCount = len(weakNegative)
            elif values[x] >= -0.2 and values[x] <= 0.2:
                neutral.append(words[x])
                nCount = len(neutral)
            elif values[x] > 0.2 and values[x] <= 0.6:
                weakPositive.append(words[x])
                wpCount = len(weakPositive)
            else:
                positive.append(words[x])
                pCount = len(positive)
    y.append(count)
    y.append(wCount)
    y.append(nCount)
    y.append(wpCount)
    y.append(pCount)
    y = np.log10(y)

    mplot.bar(["Neg", "W. Neg", "Neu", "W. Pos", "Pos"], y, color = "blue")
    mplot.title("An Affirming Flame")
    mplot.xticks(["Neg", "W. Neg", "Neu", "W. Pos", "Pos"])
    mplot.xlabel("Sentiment")
    mplot.ylabel("log10 Word Count")
    mplot.show()

elif showName.lower() == "battlestar galactica":
    for x in range(0, len(words)):
        if words[x] in battlestar:
            uniqueWordsBG.append(words[x])
            if values[x] >= -1.0 and values[x] < -0.6:
                negativeWords.append(words[x])
                negCount = len(negativeWords)
            elif values[x] >= -0.6 and values[x] < -0.2:
                weakNegative.append(words[x])
                wCount = len(weakNegative)
            elif values[x] >= -0.2 and values[x] <= 0.2:
                neutral.append(words[x])
                nCount = len(neutral)
            elif values[x] > 0.2 and values[x] <= 0.6:
                weakPositive.append(words[x])
                wpCount = len(weakPositive)
            else:
                positive.append(words[x])
                pCount = len(positive)
    y.append(negCount)
    y.append(wCount)
    y.append(nCount)
    y.append(wpCount)
    y.append(pCount)
    y = np.log10(y)

    mplot.bar(["Neg", "W. Neg", "Neu", "W. Pos", "Pos"], y, color="red")
    mplot.title("Battlestar Galactica")
    mplot.xticks(["Neg", "W. Neg", "Neu", "W. Pos", "Pos"])
    mplot.xlabel("Sentiment")
    mplot.ylabel("log10 Word Count")
    mplot.show()


