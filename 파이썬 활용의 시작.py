
################################################
#활용
################################################
class Lineage: #0 1
    def __init__(self):
        print("안녕하세요")
        
def testFunc(): #6
    print("테스트 함수입니다")

#0 클래스 활용
class MidClass(Lineage): #다중 상속 가능함

    #1 오버라이드
    def __init__(self): #클래스 초기화 함수
        super().__init__() #부모를 자동으로 불러주진 않음&부모의 함수 접근방법
        print("활용을 시작해 볼까요")
        print()
    
    #2 파일사용법
    def useFile(self):
        print("[파일 사용법]")
        fi=open("더미임포트.py","at+",encoding="utf-8") #r(읽기),w(쓰기),a(추가) 등이 있음
        fi.seek(0) #위치설정(맨앞)
        print("모든 줄: {}".format(fi.read()))
        fi.seek(0)
        print("모든 줄 리스트화: {}".format(fi.readlines()))
        fi.seek(0)
        print("첫줄 값: {}".format(fi.readline()))
        fi.seek(0)
        fi.write("# 연습") #맨앞으로 위치 바꿔도 끝에 써진다.
        fi.close()
        
        with open("더미임포트.py","at+") as fi:
            pass
        
        print()
        
    #2 함수의 다양한 활용
    def useFuncUpgrade(self,first=1,second=2): #매개변수를 받는 여러 방법(초기값 설정)
        print("[함수의 다양한 활용]")
        print("input {}, {}".format(first,second))
        lam=lambda 매개변수1, 매개변수2: 매개변수1+매개변수2      
        print("input {}".format(lam(first,second)))
        print()
        
        print()
        return 0,1 #여러값 반환 가능

    #3 예외를 처리하자
    def useTryCatch(self):
        print("[예외를 처리하는 방법]")
        try:
            print("실행 시작")
            raise Exception("예외") #오류 발생방법
            print("실행 완료")
        except:
            print("예외 발생")
            # raise #예외를 그대로 상위로 넘겨버림(해결미루기)
        else:
            print("예외가 안 발생")
        finally:
            print("무조건 출력") #이건 예외 발생을 넘겨도 무조건 실행된다
        print()
        
        print()  
        
    #4 이터레이터
    def useIter(self):
        print("[이터레이터 사용법]")
        myList=[0,1,2]
        myIter=myList.__iter__() #반복가능한 객체
        for i in myIter: #반복문 사용
            print(i)

        print()
        myIter=iter(myList)
        print(next(myIter)) #이터레이터를 모두 순회 후 호출시 예외 발생
        print()   
        
        print()

    #5. 이터레이터를 쉽게 만들자
    def useGenerator(self):
        print("[제네레이터 사용법]")
        def makeGen():
            yield "1번 값 생성"
            def innerGen():
                yield "2번 값 생성"
                yield "3번 값 생성"
            yield from innerGen() #디른 이터레이터로 부터 받아오기(다 끝날때까지 대행)
            yield "4번 값 생성"
            
        myIter=makeGen()
        print(myIter.__next__())
        print(myIter.__next__())
        print(myIter.__next__())
        print(myIter.__next__())
        print()
        
        print("[코루틴 사용법]")
        def makeCo():
            while True:
                입력값=(yield) #값을 전달 받을 수 있음
                print(입력값)
        myIter=makeCo()
        myIter.__next__() #yield까지는 실행해야 입력가능
        myIter.send(1) #값을 전달함
        myIter.send(2)   
        print()  
        
        print()    
    
    #6 함수 전달
    def useGivenFunc(self, func):
        print("전달받은 함수 사용법")
        func() #데코레이터라는 방법도 있지만 생략
        print()
        
        print()


      
if __name__=="__main__":
    활용클래스=MidClass() #0 1
    # 활용클래스.useFile() #2
    # 활용클래스.useFuncUpgrade(first=1,second=2) #2
    # 활용클래스.useTryCatch() #3
    # 활용클래스.useIter() #4
    # 활용클래스.useGenerator() #5
    # 활용클래스.useGivenFunc(testFunc) #6
    
    
    
