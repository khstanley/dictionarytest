dic = {}

try:
    f = open('dictionary.txt', 'r', encoding='UTF8')
except FileNotFoundError as e:
    print(e)
else:
    if f.readable():
        for line in f.readlines():
            item = line.split(':')
            key = item[0].strip()
            value = item[1][:-1].strip()
            dic[key] = value
        f.close()

print(dic)

line = '*' * 20
print(line)
print('영어단어사전 어플')
print(line)

stop = False
word_count = 0  # 현재 저장된 단어 개수를 나타내는 변수

while not stop:
    print('메뉴: 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료')
    menu = input('메뉴선택 : ')
    
    if menu == '1':
        if word_count < 5:  # 최대 5개의 단어 저장
            word = input('단어 : ')
            if word in dic:
                print('이미 등록되었습니다.')
            else:
                meaning = input('뜻 : ')
                dic[word] = meaning
                word_count += 1
        else:
            print('최대 5개까지만 저장 가능합니다.')
    elif menu == '2':
        search_word = input('검색할 단어: ')
        found = False
        for key, value in dic.items():
            if search_word == key:
                print(f'{key}: {value}')
                found = True
                break
        if not found:
            print('단어를 검색할수 없습니다.')
    elif menu == '3':
        edit_word = input('수정할 단어: ')
        if edit_word in dic:
            new_meaning = input('새로운 뜻: ')
            dic[edit_word] = new_meaning
            print('단어의 뜻을 수정하였습니다.')
        else:
            print('단어를 검색할수 없습니다.')
    elif menu == '4':
        delete_word = input('삭제할 단어: ')
        if delete_word in dic:
            del dic[delete_word]
            print('단어를 삭제 하였습니다.')
        else:
            print('단어를 검색할수 없습니다.')
    elif menu == '5':
        print('1. 오름차순 2. 내림차순')
        order = input('순서를 선택하세요: ')
        
        if order == '1':
            # 사전순 오름차순으로 출력
            for key in sorted(dic.keys()):
                print(f'{key}: {dic[key]}')
        elif order == '2':
            # 사전순 내림차순으로 출력
            for key in sorted(dic.keys(), reverse=True):
                print(f'{key}: {dic[key]}')
        else:
            print('잘못된 선택입니다.')
    elif menu == '6':
        print("1. 저장된 단어 갯수:", len(dic))

        if dic:
            longest_word = max(dic.keys(), key=len)
            print("2. 단어의 문자수가 가장 많은 단어:", longest_word)

            sorted_words = sorted(dic.keys(), key=len, reverse=True)
            print("3. 단어 글자수 내림차순 출력(단어만):")
            for word in sorted_words:
                print(word)
        else:
            print("단어장에 단어가 없습니다.")
    elif menu == '7':
        stop = True
        f = open('dictionary.txt', 'w', encoding='UTF8')
        if f.writable():
            for key, value in dic.items():
                key = key.strip()
                value = value.strip()
                f.write(f'{key} : {value}\n')
            f.close()
    else:
        pass