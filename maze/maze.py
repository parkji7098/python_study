import copy
import numbers
import os

map =[]
player = [8,0]

# 맵 디스플레이
def display():
    for y in range(len(map)):
        row = map[y]
        for x in range(len(row)):
            item = row[x]
            # if player[0] == y and player[1] == x:
            if player == [y,x]:
                print('P', end=" ")
            else:
                print(item, end=" ")
        print()
    print()
            
#map파일 불러오기
def loadMap():
    with open("/home/pji/python_study/python_study/maze/map.txt", 'r', encoding='utf-8') as f:
        mapp = f.readlines()
        for line in mapp:
            row = line.split()
            map.append(row)

#위치 옮기기
def Input():
    print(f"현재 위치: y:{player[0]} x:{player[1]}")
    print('위:w  아래:s  왼쪽:a  오른쪽:d')
    num = input("입력(w,s,a,d,): ")
    y,x = player[0], player[1]
    if num == 'w':
        player[0] = y-1
    elif num == 's':
        player[0] = y+1
    elif num == 'd':
        player[1] = x+1
    elif num == 'a':
        player[1] = x-1
    else:
        print("탈출! 축하합니다!")
    return player

# 실행
def run():
    global player
    loadMap()
    display()
    while player != [0,8]:
        player = Input()
        print(player)
        os.system('clear')
        display()
    else:
        print("탈출! 축하합니다!")      

if __name__ == "__main__":
    run()
    pass