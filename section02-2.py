# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this # 파이썬을 사용하는 방법, 장점 등이 출력됨
import sys 

# 파이썬 기본 인코딩 : 2.0.0 대 버전 = 유니코드 / 3.0.0 대 버전 = utf-8
print(sys.stdin.encoding)   # 파이썬 입력 기본 : utf-8
print(sys.stdout.encoding)  # 파이썬 출력 기본 : utf-8

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Goodboy'

# 조건문
if myName == "Goodboy":
    print('Ok')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i,j,(i*j)))

# 변수 선언(한글)
이름 = "좋은사람"

# 출력
print(이름)

# 함수선언
def 인사():
    print("안녕하세요. 반갑습니다.")

인사()

def greeting():
    print("Hello")

greeting()

# 클래스 _ 복습 필요
class Cookie:
    pass

# 객체 생성 _ 복습 필요
cookie = Cookie()

print(id(cookie))   # 숫자가 계속 변함 (id값 계속 새로 할당하는 건가... 모르겠음)
print(dir(cookie))
