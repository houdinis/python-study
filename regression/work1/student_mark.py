# 判断学生成绩，成绩等级A-E.其中，90分以上为“A‘，80-89分为’B‘,70-79分为"C'，60-69分为"D",60分以下为"E"

score = 92

def mark(score):
    if score > 90:
        print("A")
    elif score > 80 and score < 89:
        print("B")
    elif score > 70 and score < 79:
        print("C")
    elif score > 60 and score < 69:
        print("D")
    elif score < 60:
        print("E")

mark(score)