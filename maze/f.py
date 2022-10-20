import copy

double_list = []
line = []

def loadMap():
    with open("/home/pji/catkin_ws/src/py/map.txt", 'r', encoding='utf-8') as f:
        mapp = f.readlines()      #내용 읽음
        return mapp
        
mapp = loadMap()



for i in range(9):
    double_list = mapp[i].split()
    # line.append(''.join(double_list))
    line.append(double_list)
    
def ch():
    global a,b
    temp = a
    a = b
    b = temp

number = input("입력: ")

for i in range(9):

    if 'S' in line[i]:
        print(f"현재위치: 행: {i} 열: {line[i].index('S')}")
        line_index = copy.deepcopy(i)
        print("line_index:",line_index)
        if number == '1':
            a = line[line_index][0]
            b = line[line_index -1][0] = 'P'
            ch()
            print(line)
        

        elif number == '2':
            a = line[line_index][0]
            b = line[line_index +1][0] = 'P'
            ch()
            print(line)
        elif number == '3':
            a = line[line_index][0]
            b = line[line_index][1] = 'P'
            ch()
            print(line)
        elif number == '4':
            a = line[line_index][0]
            b = line[line_index -1][0] = 'P'
            ch()
            print(line)

            


        break
    else:
        pass

up = 0
down = 0
right = 0
left = 0


# for i in range(9):
#         if 'P' in line[i]:

# if number == 1:
#     line[]


# print(line)







# if __name__ == "__main__":
#     prepare()
#     pass