import requests

# url = 'http://www.naver.com'
# res = requests.get(url)
# # print('res', res.text)    # utf-8 인코딩된 내용
# print('res', res.content)   # 바이너리 타입


# url = 'https://pokeapi.co/api/v2/pokemon?limit=508offset=51'
# res = requests.get(url)
# # print('res', res.text)    # utf-8 인코딩된 내용
# # print('res', res.content)   # 바이너리 타입

# # dict

# resonseData = res.json()
# # print('keys:', resonseData.keys())

# results = resonseData['results']
# # print('abilities:', results)

# for result in results:
#     print(result)



limit = 0
api = 'https://pokeapi.co/api/v2/pokemon'

while True:
    inputText = input('page number: ')

    if not inputText.isdigit():
        continue

    page = int(inputText)

    if page <= 0:
        continue

    url = f'{api}?limit={limit}&offset={limit * (page-1)}'

    res = requests.get(url)
    resonseData = res.json()
    results = resonseData['results']

    for result in results:
        print(result)
    