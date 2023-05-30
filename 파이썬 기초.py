
################################################
#모듈 임포트 방법
################################################
import 더미임포트예제
#from 더미임포트 import dummyHello #이런 방식을 쓰면 더 짧게 쓸수 있다.

################################################
#기초
################################################   

#0. 클래스 생성법 
class ElementalClass:
    classProperty="이건 클래스 속성입니다"#모든 인스턴스가 공유함
    
    def __init__(self,name="Student"):
        self.name=name #속성
        print("기초부터 시작해 볼까요, {}?".format(self.name))
        print()
    
    # 1. 가감승제 & 출력
    def plus2Div(self):
        a=10
        b=3
        plus=a+b # +=, -= 등의 축소 연산은 생략
        minus=a-b
        times=a*b
        power=a**b
        div=a/b
        divFloor=a//b #소숫점 버림
        mod=a%b #나머지 연산
       
        print("[가감승제]\n plus {0}, minus {1}, times {2}, power {3}, div {4}, divFloor {5}, mod {6}"
              .format(plus,minus, times,power,div,divFloor,mod))
        print()
       
    #1.1 비트연산
    def usebit(self):
        print("[비트 연산법]")
        print("11의 이진수: {}".format(bin(11))) #bin은 문자형으로 반환
        print("0b1011의 십진수: {}".format(0b1011)) 
        print("'1011'의 숫자화: {}".format(int("1011",2))) #(문자, 진수)
        print("1011(11)과 1101(13)의 비트 AND, OR, XOR, NOt: {} {} {} {}".format(11&13,11|13,11^13,~11))
        print("11의 이트 이동: {} {}".format(11<<2,11>>2))
        print()
        
        
    #2. 입력받기, 형변환
    def getConsole(self):
        inputValue=input() #숫자를 입력해도 string취급 
        inputNumberList=list(map(int, input().split())) #입력값을 리스트화
        inputNumber, _=inputNumberList #리스트 원소 나누기
        
        print("[입력값과 자료형]\n 1. {}:{}\n 2. {}:{}"
              .format(inputValue,type(inputValue),inputNumber,type(inputNumber)))
        print()
        
        print()
    
    #2.1 스트링
    def useString(self):
        print("[스트링 특징]")
        myStr="  012345 가나다라  "
        print("문자열: {}".format(myStr))
        print("문자열 결합: {}".format(myStr+"결합된 문자"))
        print("문자열 사이 공백삭제: {}".format(myStr.strip()))
        print("문자열 대->소문자 변경: {}".format("ABCD".lower()))
        print("문자열 변경: {}".format(myStr.replace("012345","abcd")))
        print("리스트(튜플) 조인: {}".format(str.join(" ",["안녕","하세요","1234"])))
        print()
        
        print()       
    

        
         
    #3. 로직 비교, if, while, for, bool
    def logic(self):
        print("[로직 사용법]")
        
        #주소가 달라도 같은 값만 들어있으면 같은 값 취급, 값이 바뀌면 다른 취급
        a=[1]
        b=[1]
        print(a==b)
        a.append(2)
        print(a==b)
        print()
        
        #다음과 같은 참거짓을 표현하는 자료형이 boolean이다
        #복수개의 조건은 and or 을 이용가능
        if 10>10:
            print("10>10")
        elif 10==10:
            print("10==10")
        else:
            print("10<10")
        print()
        
        

        
        #while문으로 [0,10) 세기
        count=0
        while count<10:
            print(count)
            count+=1
            #break나 continue로 반복문 제어 가능
        print()

        #for문으로 [0,10) 세기. 레인지 말고도 리스트, 튜플로도 가능
        for count in range(0,10): 
            print(count)
        print()
        
        print()
    
    
    #4. 리스트 사용법 & range & 튜플  == 시퀸스 자료형
    def useList(self):
        #리스트(가변)
        print("[리스트 사용법]")
        myList=[]
        myList=list()
        print(myList)
        myList=[1,"2",[3],4,5]
        print(myList)
        myList[0]=0 #값 삽입
        print("인덱스 0: {}".format(myList[0]))
        del myList[0] #값 삭제
        print(myList)
        print()
        
        #레인지
        print("[레인지 사용법]")
        myRange=range(1,11,2) #시작, 끝(비포함), 인터벌
        print(myRange)
        print(list(myRange))
        print("인덱스 0: {}".format(myRange[0]))
        print()
        
        #튜플(불변)
        print("[튜플 사용법]")
        myTuple=(1,2)  #그외 리스트와 비슷한 선언방법들
        print(myTuple)
        print(myTuple[0])
        print()     
        
        #시퀸스 자료형 공통 기능
        print("[시퀸스 특징]")
        print("1. 값 확인: {}".format([2] in myList))
        print("2. 길이 확인: {}".format(len(myRange)))
        print("3. 요소 확인: {}".format(myTuple[0])) # -가 붙으면 뒤에서 부터
        print("4. 반복 복제: {}".format(myTuple*3)) # 레인지는 안된다
        print("5. 슬라이싱 {}".format(myList[0:1:1])) #시작, 끝(비포함), 인터벌
        print()
        
        print()
   
    #4.1 리스트 업그레이드
    def useListUpgrade(self):
        print("[리스트 사용법 업그레이드]")
        myList=[]
        print("현제 리스트: {}".format(myList))
        myList.append(0)
        myList.append([1]) #리스트 그 자체 삽입
        myList.extend([2,3]) #리스트를 연결
        myList.insert(0,10) #특정위치에 추가
        print("현제 리스트: {}, 갯수: {}".format(myList, len(myList)))
        search=myList.index([1]) #입력값의 인덱스를 찾음(리스트안에 없으면 에러) 
        print("[1] 원소 위치 {}".format(search)) #원소 인덱스 위치 찾는법
        myList.remove([1])
        poppingEle=myList.pop()
        myList.sort() #오름차순 정렬
        myList.reverse() #뒤집기
        print("현제 리스트: {}, pop 원소 {}".format(myList,poppingEle))
        newList=myList.copy() #복제본 생성
        myList.clear() #전체 원소 삭제 del[:] 과 같음
        print("현제 리스트: {}, 복제 리스트 {}".format(myList,newList))
        print()
        
        print("[다차원 리스트]") 
        myList=[[0,1],[2,3],[4,5]]
        endEle=myList[len(myList)-1][1]
        print("현제 리스트: {}, 맨 끝 원소 {}".format(myList,endEle))
        print()
        
        print("[컴프리헨션]") 
        myList=[[0,1],[2,3],[4,5]]
        newList=[i+i for i in myList if i[0]<4] 
        print("현제 리스트: {}".format(newList))
        print()
        
        print("빈복문")
        for i in myList:
            print(i)
        print()
 
        print()
   
   
    #5. 딕셔너리 사용법
    def useDic(self):
        print("[딕셔너리 사용법]")
        dic={}
        dic=dict()
        dic={"키1":1,"키2":2}
        print("현제 딕셔너리: {}".format(dic))
        dic[3]=3 #삽입(꼭 문자형이 아니라도 된다.)
        print("현제 딕셔너리: {}".format(dic[3]))
        del dic["키1"] #삭제
        print("현제 딕셔너리: {}".format(dic))
        print()
        
        print("[딕셔너리 사용법 업데이트]")
        dic={"0":0}
        dic["1"]=1
        dic.update({"2":2})
        print("현제 딕셔너리: {}".format(dic))
        print("딕셔너리에서 값가져오는 법: {}".format(dic.get("3",3))) #(키, 디폴트)
        print("값을 가져오고 삭제하는 법: {}".format(dic.pop("4",4))) #(키, 디폴트)
        print()
        
        print("[딕셔너리 반복문]")
        print("item: {},\nkeys: {},\nvalue: {}".format(dic.items(),dic.keys(),dic.values()))    
        for key, value in dic.items():
            print("{}:{}".format(key,value)) 
        print()
    
        print()
        
    #6.셋
    def useSet(self):
        print("[세트 사용법]")
        mySet={1,2,3,1}
        print("현제 셋: {}, 셋 길이: {}".format(mySet, len(mySet)))
        print("셋안의 원소 확인: {}".format(1 in mySet))
        print("셋 합치기".format({0,1,2}|{2,3,4})) #셋은 비트연산과 같음
        print()
        
        print()      
    


       
        
################################################
#메서드 생성 & 디폴트 매개변수 & 리턴
    #(파이썬은 동명함수 오버로딩 불가)
################################################
def hello(name="MyName"):
    print(f"안녕하세요 {name}? 지금부터 기초중의 기초 예제를 시작해 볼까요?\n")
    return name


################################################
#메인 함수 호출, 함수호출
################################################

if __name__=="__main__":

    기초클래스=ElementalClass()  #0 파이썬은 한글 이름도 가능
    # 기초클래스.plus2Div() #1
    # 기초클래스.usebit() #1.1
    # 기초클래스.getConsole() #2
    # 기초클래스.useString() #2.1
    # 기초클래스.logic() #3
    # 기초클래스.useList() #4
    # 기초클래스.useListUpgrade() #4.1
    # 기초클래스.useDic() #5   
    # 기초클래스.useSet() #6

    # hello() #함수 호출법
    # 더미임포트.dummyHello() #외부 함수 호출법

