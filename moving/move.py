import time

result = input("입력하세요(1~9): ")

if len(result)<9:
    result = "{0:@^9}".format(result)
else :
    result = result[0:9]

print('\r' + result, end='')

while True:
    move = result[:1]
    move2 = result[1:]
    result = move2 + move
    time.sleep(1)
    print('\r' + result, end='')
