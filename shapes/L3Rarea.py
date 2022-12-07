#lab 3 Rev Area
#similar process to the CSII Lab3 area, except value and type errors have been added.


import math

#circle
#Pi * Radius ^2
#Added error handling for value and type errors
def AreaCircle(CircleAreaRadius):
    #error for less than zero
    if CircleAreaRadius <= 0:
        raise ValueError("Value must be greater then 0.")
    #error for incorrect types
    if (type(CircleAreaRadius) != float and type(CircleAreaRadius) != int):
        raise TypeError("Input must be a whole number, or a decimal.")
    AreaCircleResult = math.pi * CircleAreaRadius ** 2
    return AreaCircleResult


#rectangle
#Length * Width
#Added some error handling
def AreaRect(RectAreaLength,RectAreaWidth):
    #error for less than zero.
    if RectAreaLength <= 0 or RectAreaWidth <=0:
        raise ValueError("Value must be greater then 0.")
    #error for incorrect types
    if (type(RectAreaLength) != int and type(RectAreaLength) != float) or (type(RectAreaWidth) != int and type(RectAreaWidth) != float):
        raise TypeError("Input must be a whole number, or a decimal.")
    AreaRectResult = RectAreaLength * RectAreaWidth
    return AreaRectResult


#square
#Side ^2
def AreaSqr(SqrAreaSide1):
    #error for less than zero.
    if SqrAreaSide1 <= 0:
        raise ValueError("Value must be greater then 0.")
    if (type(SqrAreaSide1) != int and type(SqrAreaSide1) != float):
        raise TypeError("Input must be a whole number, or a decimal.")
    SqrAreaResult = SqrAreaSide1 **2
    return SqrAreaResult


#riangle
#Base * Height /2
def AreaTri(TriAreaBase1, TriAreaHeight2):
    #error for less than zero.
    if TriAreaBase1 <=0 or TriAreaHeight2 <=0:
        raise ValueError("Value must be greater then 0.")
    if (type(TriAreaBase1) != int and type(TriAreaBase1) != float) or (type(TriAreaHeight2) != int and type(TriAreaHeight2) != float):
        raise TypeError("Input must be a whole number, or a decimal.")
    TriAreaResult = TriAreaBase1 * TriAreaHeight2 / 2
    return TriAreaResult