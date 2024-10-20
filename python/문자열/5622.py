dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] #다이얼 별 문자 리스트
word = list(input()) # 리스트로 받기
result = 0

for i in word: # 리스트 순회
    for j in dial: # 다이얼 리스트 순회
        if i in str(j): # 다이얼 리스트를 문자열으로 바꿨을 때 그 안에 특정 i 요소가 있는지 찾기
            num = dial.index(j) + 3 # 시간 계산
            result += num
        
    
print(result)