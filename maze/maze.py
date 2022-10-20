import copy

map =[]

#map파일 불러오기
def loadMap():
    with open("/home/pji/python_study/python_study/maze/map.txt", 'r', encoding='utf-8') as f:
        mapp = f.readlines()      #내용 읽음
        for line in mapp:
            print(line)
        return mapp

map = loadMap()

map2 = copy.deepcopy(map)

for i in range(9):
    li = []
    double_list = map2[i].split()
    # line.append(''.join(double_list))
    li.append(double_list)
    print(li)



# 시작위치 알아내는 함수
def raw_col():
    for i in range:
        if 'S' in map2[i]:
            p_y = map2[i].index('S')
            print(p_y)


print(raw_col())

# 복사하기
# 보여주기

# 사용자가 갈수있는방향체크

# 초기에 준비 

# run함수






# if __name__ == "__main__":
#     run()
#     pass