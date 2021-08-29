# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 (순서 ㅇ, 중복 ㅇ, 수정 ㅇ, 삭제 ㅇ)

# 선언
a = []              # 선언방식 1
b = list()          # 선언방식 2
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])      # 이중리스트는 이런 식으로 꺼내오는구나
print(e[-1][-2])    # 이중리스트는 이런 식으로 꺼내오는구나

print('--------------------------------------------------------------------------------')

# 슬라이싱
print(d[0:3])
print(e[2][1:3])
print(e[2][1:4])    # 슬라이싱은 최대 범위를 벗어나도 에러가 뜨진 않음

print('--------------------------------------------------------------------------------')

# 연산
print(c + d)
print(c * 3, type(c * 3))        # 리스트 c 3번 반복해서 한 리스트로 출력
print(str(c[1]) + 'hi')

print('--------------------------------------------------------------------------------')

# 리스트 수정
c[0] = 77                        # 리스트 c의 인덱스 0의 값을 77로 수정
print(c)
c[1:2] = [100, 1000, 10000]      # 리스트 c의 구간 값 수정 가능
print(c)
c[0] = ['a', 'b']                # 리스트 c의 인덱스 0의 값을 리스트로 수정
print(c)

print('--------------------------------------------------------------------------------')

# 리스트 삭제
del c[0]                         #  del VS .remove()  : del은 인덱스로 접근 remove는 값으로 접근                        
print(c)
del c[-1]
print(c)

print('--------------------------------------------------------------------------------')

# 리스트를 함수로 제어
y = [5, 2, 3, 1, 4]
y.append(6)                      # 리스트 마지막 부분에 6 삽입
print(y)
y.sort()                         # 왼쪽에서 오른쪽으로 오름차순 정렬
print(y)
y.reverse()                      # 왼쪽에서 오른쪽으로 내림차순 정렬
print(y)
y.insert(2, 7)                   # 인덱스 2 자리에 7 삽입
print(y)
y.remove(2)                      # 인덱스 2 자리에 있는 7이 지워지는 게 아니라 2가 지워짐
print(y)
y.pop()                          # 마지막 요소를 꺼내고 다시 y 저장  = LIFO (Last In First Out) : stack에서 사용
print(y)
ex = [88, 77]
y.extend(ex)                     # extend VS append : .extend()는 리스트에 원소로서 연장가능 // .append()로 리스트 넣으면 리스트로 들어감
print(y)
y.append(ex)
print(y)

# 삭제 : del, remove, pop

print('--------------------------------------------------------------------------------')

# 튜플 (순서ㅇ, 중복ㅇ, 수정x, 삭제x) 
# 용례 : 변경되면 실행이 오작동 되거나 프로그램의 흐름에 critical한 영향을 끼치는 정보들을 저장할 때 사용

a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', c))
#del c[2]                         # 에러 뜸 = 튜플은 삭제기능이 없기 때문에

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)                      # 튜플도 더하기 가능
print(c * 3)                      # 튜플도 확장 가능

print('--------------------------------------------------------------------------------')

# 튜플 함수

z = (5, 2, 1, 3, 1)
print(z)
print(3 in z)                     # 튜플 z 안에 3이 있냐
print(z.index(1))                 # 튜플 z의 인덱스 1에 해당하는 값이 뭐냐
print(z.count(1))                 # 튜플 z 안에 1 개수 세라