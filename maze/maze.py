import copy
import numbers

map =[
    #[],
    #[],
]
li = []


player = (8,8)

def display():
    # for row in map:
    #     for item in row:
    #         print(item, end=" ")
    #     print()

    for y in range(len(map)):
        row = map[y]
        for x in range(len(row)):
            item = row[x]
            # print(f'({y},{x}) {item}', end=" ")
            # print(item, end=" ")
            if player[0] == y and player[1] == x:
                print('P', end=" ")
            else:
                print(item, end=" ")
            
        print()

    pass



#map파일 불러오기
def loadMap():
    with open("/home/pji/python_study/python_study/maze/map.txt", 'r', encoding='utf-8') as f:
        mapp = f.readlines()      #내용 읽음
        for line in mapp:
            row = line.split()
            map.append(row)
            # print(line)

loadMap()


display()






# map2을 리스트로 만듬
# map2 = copy.deepcopy(map)
# for i in range(9):
#     double_list = map2[i].split()
#     li.append(double_list)
# map2=li
# print(map2)


player_start = 'P'
map[8][0] = player_start

# 시작위치 알아내는 함수
def player_xy():
    for i in range(9):
        if 'P' in map[i]:
            player_x = i
            player_y = map[i].index('P')
            print(f"현재위치: x: {player_x}, y: {player_y}")
            return player_x, player_y
        else:
            pass


player = list(player_xy())

print(player)

num = input("입력(1~4): ")
if num == '1':
    x = player[0]
    y = player[1]
    map[x-1][y] = 'P'
    print(map)
elif num == '2':
    x = player[0]
    y = player[1]
    map[x+1][y] = 'P'
    print(map)
elif num == '3':
    x = player[0]
    y = player[1]
    map[x][y+1] = 'P'
    print(map)
elif num == '4':
    x = player[0]
    y = player[1]
    map[x-1][y-1] = 'P'
    print(map)

else:
    pass

# print(map2)



# 복사하기
# 보여주기


# 사용자가 갈수있는방향체크

# 초기에 준비 

# run함수






# if __name__ == "__main__":
#     run()
#     pass