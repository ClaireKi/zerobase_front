# Section04-2

# 문자열 생성, 길이
str1 = "I am a Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str('ace')

print(len(str1), len(str2), len(str3), len(str4))

print('--------------------------------------------------------------------------------')

# escape 문자
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \tTab\t"
print(escape_str2)

print('--------------------------------------------------------------------------------')

# Raw String : 안에 escape문 무시
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\a"
print(raw_s2)

print('--------------------------------------------------------------------------------')

# 멀티라인 : 사전에 escape 시켜놓으면 멀티라인 가능
multi = \
""" 
문자열 

멀티라인 
       테스트 
"""
print(multi)

print('--------------------------------------------------------------------------------')

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'NiceMan'

print(str_o1 * 10)
print(str_o2 + str_o3)
print('a' in str_o4)        # a라는 문자가 str_o4에 포함됐는지 묻는 질문
print('z' not in str_o4)    # z라는 문자가 str_o4에 포함되지 않았는지를 묻는 질문

print('--------------------------------------------------------------------------------')

# 문자열 형변환
print(str(77) + 'a')        # 문자간 덧셈 가능
print(str(10.4))

print('--------------------------------------------------------------------------------')

# 문자열 함수
a = 'niceMan'
b = 'orange'

print(a.islower())          # 변수 a가 소문자로 이루어졌는지 묻는 질문
print(a.endswith('n'))      # 변수 a의 마지막 철자가 n으로 끝나는지 묻는 질문
print(a.capitalize())       # 변수 a의 첫번째 철자만 대문자 나머지는 다 소문자로 바꿔 출력
print(a)                    # 다시 변수 a를 출력해보니 위의 함수들이 a에 영향을 직접적으로 주진 않음 
print(reversed(b))
print(b)
print(list(reversed(b)))    # reversed(변수) 의 결과물을 보기 위해선 list()함수가 필요함

print('--------------------------------------------------------------------------------')

# 문자열 슬라이싱
c = 'niceman'
d = 'orange1'

print(c[0:4])
print(c[0:len(c)])          
print(c[0:])                
print(c[:])                 
print(d[0:7:2])             # 0~(7-1) 까지의 인덱스에서 (2-1)개씩 건너뛸 것
print(d[1:-2])              # 인덱스 1에서 인덱스 (-2-1)까지 출력 // 오른쪽부터 인덱싱 먹일 떄는 -1부터 시작함
print(d[::-2])              # 처음부터 끝까지 나오는데 오른쪽에서 (2-1)개씩 건너뛰고 나옴