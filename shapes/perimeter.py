#lab 3 perimeter
import math




#circle
#2 * pi * Radius
def PeriCircle(CirclePeriRadius):
    PeriCircleResult = 2 * math.pi * CirclePeriRadius
    return PeriCircleResult

#rectangle
#2 * (Length + width)
def PeriRect(RectPeriLength,RectPeriWidth):
    PeriRectRes = (2 * RectPeriLength) + (2 * RectPeriWidth)
    return PeriRectRes

#square
# #2 * (Length + width)

def PeriSqr(SqrPeriSide1):
    SqrPeriResult = SqrPeriSide1 + SqrPeriSide1 + SqrPeriSide1 + SqrPeriSide1
    return SqrPeriResult


#riangle
# S + S + S aka p + l + w

def PeriTri(TriPeriSide1,TriPeriSide2,TriPeriSide3):
    TriPeriResult = TriPeriSide1 + TriPeriSide2 +TriPeriSide3
    return TriPeriResult
