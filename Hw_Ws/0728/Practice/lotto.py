# 여기에 필요한 모듈을 추가합니다.
import json
from operator import is_
import random

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.numbers_lines = []

        pass

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        
        for i in range(n):
            lotto_numbers=list(random.sample(range(1,46),6))
            lotto_numbers.sort()
            self.numbers_lines.append(lotto_numbers)

        # line_numbers=[sorted(list(random.sample(range(1,46),6))) for _ in range(n)]
        return self.numbers_lines
    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self,draw_number):
        print('==================================================')
        print(f'            제 {draw_number} 회 로또              ')
        print('==================================================')
        year,month,day=self.get_draw_date(draw_number)
        print(f'추첨일 : {year}/{month}/{day} (토)         ')
        print('==================================================')
        list_1=['A','B','C','D','E']
        
        for i in range(len(self.numbers_lines)):
            print(list_1[i],': ',self.numbers_lines[i])    
        pass

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        dang,bonus =self.get_lotto_numbers(draw_number)
        print('===============================================')
        print('당첨 번호 : ',dang,'+',bonus)
        print('===============================================')
        list_1=['A','B','C','D','E']
        # for i in range(len(self.numbers_lines)):
        # self.get_same_info(dang, bonus, self.numbers_lines[0])
        for i in range(len(self.numbers_lines)):
            
            same_main_counts, is_bonus=self.get_same_info(dang,bonus,self.numbers_lines[i])
            ranking=self.get_ranking(same_main_counts, is_bonus)
            if ranking==0:
                ranking='낙첨'
            else:
                ranking=f'({ranking}등 당첨!)'
            if is_bonus==True:
                pass    
            
            print(list_1[i],':',f'{same_main_counts}','개 일치',f'{is_bonus}',ranking) 

        pass

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
                      
        d = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        data = json.load(d)
        data.get('drwNoDate') # 2022-23-32
        
        # year=data.get('drwNoDate')[:4]
        # month=data.get('drwNoDate')[5:7]
        # day=data.get('drwNoDate')[8:10]
        a, b, c = map(str,data.get('drwNoDate').split('-'))  
               
        return a, b , c
        # return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        d = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        data = json.load(d)
        main_numbers=[]
        bonus_number=0
        for i in range(1,7):
            main_numbers.append(data.get(f'drwtNo{i}'))
        main_numbers.sort()
        bonus_number=data.get('bnusNo')
        pass
        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts=0
        is_bonus=''
        same_main_counts=len(set(main_numbers)&set(line))
     
        # print(set(main_numbers),set(line))
        if len(set(line)&{bonus_number})==1:
            is_bonus=True
        else:
            is_bonus=False
        
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranking=0

        if same_main_counts==3:
            ranking=5
        elif same_main_counts==4:
            ranking=4
        elif same_main_counts==5 & is_bonus !=True:
            ranking=3
        elif same_main_counts==5 & is_bonus ==True:
            ranking=2
        elif same_main_counts==6:
            ranking=1
                 
        return ranking 
