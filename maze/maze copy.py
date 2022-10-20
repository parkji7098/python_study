import copy

map =[]

def loadMap():
    with open("/home/pji/python_study/python_study/maze/map.txt", 'r', encoding='utf-8') as f:
        mapp = f.readlines()      #내용 읽음
        for line in mapp:
            print(line)
        return mapp
        
map = loadMap()



# for i in range(9):
#     double_list = mapp[i].split()
#     # line.append(''.join(double_list))
#     line.append(double_list)
    
# def ch():
#     global a,b
#     temp = a
#     a = b
#     b = temp


# while True:
#         number = input("입력: ")
#         for i in range(9):

#             if 'S' in line[i]:
#                 line_col = line[i].index('S')
#                 line_index = copy.deepcopy(i)
#                 if number == '1':
#                     a = line[line_index][0]
#                     b = line[line_index -1][0] = 'P'
#                     ch()
#                     print(line)
#                     print(f"현재위치: 행: {line_index -1} 열: {line[i].index('S')}")



                
#                 elif number == '2':
#                     a = line[line_index][0]
#                     b = line[line_index +1][0] = 'P'
#                     ch()
#                     print(line)

#                 elif number == '3':
#                     a = line[line_index][0]
#                     b = line[line_index][line_col -1] = 'P'
#                     ch()
#                     print(line)

#                 elif number == '4':                                                     
#                     a = line[line_index][0]
#                     b = line[line_index -1][line_col -1] = 'P'
#                     ch()
#                     print(line)
                    
#                 else:
#                     print("잘못입력하셨습니다")




# f.close()

# for i in range(9):
#         if 'P' in line[i]:

# if number == 1:
#     line[]


# print(line)







# if __name__ == "__main__":
#     prepare()
#     pass