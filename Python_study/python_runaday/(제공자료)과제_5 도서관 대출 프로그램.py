class Book:
    ## 생성자
    def __init__(self, name, author, publisher):
        # 책이름
        self.name=name
        # 작가
        self.author=author
        # 출판사
        self.publisher=publisher
        # 대여 횟수
        self.number=0
        # 대여 가능 여부
        self.rentable=True
        # 대여자
        self.myid=""
        
    ## 대출 메서드
    def rent(self, day, myid):
        if self.rentable==True:
            print("대출날짜: {} " .format(day))
            print("대여자: {} " .format(myid))
            self.number=
            self.rentable=
            self.myid=
        else:
            print("현재 대출이 불가합니다")
            
    ## 반납 메서드
    def turnin(self, myid):
        if (self.rentable==    ) and (self.myid==     ):
            print("반납이 완료되었습니다")
            self.rentable=True
            self.myid=""
        else:
            print("반납이 불가합니다. 안내데스크에 문의바랍니다")
            
    ## 확인 메서드
    def identify(self):
        print("현재 대여자 : {}" .format(     ))
        print("대여횟수  : {}" .format(     ))
