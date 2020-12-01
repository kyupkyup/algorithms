input = input()

def solution(input):
    cross = input[0]
    row = int(input[1])


    if cross == "a":
        cross = 1
    elif cross == "b":
        cross=2
    elif cross == "c":
        cross=3
    elif cross == "d":
        cross=4
    elif cross == "e":
        cross=5
    elif cross == "f":
        cross=6
    elif cross == "g":
        cross=7
    elif cross == "h":
        cross=8

    count = 0

    if 8 >= cross + 2 > 0 and 0 < row + 1 <=8:
        count += 1
    if 8 >= cross + 2 > 0 and 0 < row - 1 <=8:
        count += 1
   
    if 8 >= cross - 2 > 0 and 0 < row + 1 <=8:
        count += 1
    if 8 >= cross - 2 > 0 and 0 < row - 1 <=8:
        count += 1

    if 8 >= row + 2 > 0 and 0 < cross + 1 <=8:
        count += 1
    if 8 >= row + 2 > 0 and 0 < cross - 1 <=8:
        count += 1
   
    if 8 >= row - 2 > 0 and 0 < cross + 1 <=8:
        count += 1
    if 8 >= row - 2 > 0 and 0 < cross - 1 <=8:
        count += 1
    print(count)
solution(input)