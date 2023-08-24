from api.Kiwoom import *
import sqlite3
import traceback
from datetime import datetime, timedelta
import math
import time



class C_strategy(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.strategy_name="C_strategy"
        self.kiwoom=Kiwoom()
        self.universe={}
        self.deposit = 0
        self.is_init_success=False
        self.init_strategy()

    def init_strategy(self):
        try:
            # self.show_code_list()
            self.kiwoom.get_order()
            self.kiwoom.get_balance()
            self.selected_stocks=self.check_code_list()
            self.deposit=self.kiwoom.get_deposit()
            self.set_universe_real_time()
            self.is_init_success=True

        except Exception as e:
            print(traceback.format_exc())



    def set_universe_real_time(self):
        fids = get_fid("체결시간")
        # self.kiwoom.set_real_reg("1000", "", get_fid("장운영구분"), "0")

        # 확인하고 고치기
        selected_stocks = self.selected_stocks
        codes = [stock[1] for stock in selected_stocks]  # 종목 코드만 추출
        codes = ";".join(map(str, codes))
        self.kiwoom.set_real_reg("9999", codes, fids, "0")



    def run(self):
        print("run함수를 실행합니다")
        while self.is_init_success:
            try:
                # 현재 시간 확인
                now = datetime.now()
                start_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
                end_time = now.replace(hour=15, minute=50, second=0, microsecond=0)
                print(f"현재 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")
                selected_stocks = self.selected_stocks

                if not start_time <= now <= end_time:
                    wait_seconds = (start_time - now).seconds
                    print(f"장 운영 시간이 아니므로 {wait_seconds}초 대기합니다.")
                    time.sleep(wait_seconds)
                    continue

                # 장 운영 시간(예시: 09:00 ~ 15:30)인지 확인
                if start_time <= now <= end_time:
                    print("장 운영 시간입니다.")
                    if selected_stocks:
                        print("선택된 종목 정보:")
                        for stock in selected_stocks:
                            company_name, code, 접수일, 전환가액 = stock
                            전환가액 = int(전환가액)

                    else:
                        print("조건에 해당하는 종목이 없습니다.")

                for row in selected_stocks:
                    company_name, code, 접수일, 전환가액 = row
                    전환가액 = int(전환가액)

                    # (1)접수한 주문이 있는지 확인
                    if code in self.kiwoom.order.keys():
                        # (2)주문이 있음
                        print('접수 주문', self.kiwoom.order[code])

                        # (2.1) '미체결수량' 확인하여 미체결 종목인지 확인
                        if self.kiwoom.order[code]['미체결수량'] > 0:
                            pass

                    # (3)보유 종목인지 확인
                    elif code in self.kiwoom.balance.keys():
                        print('보유 종목', self.kiwoom.balance[code])
                        self.order_sell(code, 전환가액)

                    else:
                        # (4)접수 주문 및 보유 종목이 아니라면 매수대상인지 확인 후 주문접수
                        self.order_buy(code, 전환가액)

            except Exception as e:
                print(traceback.format_exc())

            # 5초 대기
            time.sleep(5)

    def order_sell(self, code, 전환가액):
        # 잔고에 해당 종목이 있으면 매도 주문
        전환가액 = int(전환가액)
        quantity = self.kiwoom.balance[code]['보유수량']
        sell_price = 전환가액 * 1.2
        self.kiwoom.send_order("매도주문", "0101", 2, code, quantity, sell_price, "00")

    def order_buy(self, code, 전환가액):
        # 전환가액보다 현재 가격이 쌀 때 매수
        전환가액 = int(전환가액)
        budget = self.deposit
        budget= 0.1 * budget
        전환가액=전환가액*0.9
        quantity = math.floor(budget / 전환가액)

        amount=전환가액*quantity
        budget=math.floor(budget-amount*1.00025)
        if budget < 0:
            return

        self.kiwoom.send_order("send_buy_order", "0101", 1, code, quantity, 전환가액, "00")


    def check_and_sell(self):
        orders_to_sell = []
        for order_code, order_info in self.order.items():
            order_time = datetime.strptime(order_info["주문시간"], "%Y%m%d%H%M%S")
            if datetime.now() >= order_time + timedelta(days=180):
                # 6개월 이상된 주문은 시장가로 매도하기 위해 매도 주문 추가
                orders_to_sell.append((order_code, order_info["주문수량"]))

        for code, quantity in orders_to_sell:
            self.send_order("매도주문", "0101", 1, code, quantity, 0, "03")
            # 매도 주문 전에 기존 주문을 삭제
            self.order.pop(code, None)

    def check_code_list(self):

        conn = sqlite3.connect('C:/Users/min17/Desktop/증권 백테스팅/전환사채 목록2(금리추가).db')
        cursor = conn.cursor()
        cursor.execute(
            """SELECT 회사명, code, 접수일, 전환가액
            FROM convertible_bond
            WHERE 접수일 >= date('now', '-1 year')  -- 1년 미만인 데이터 선택
            AND 금리차 > 2
            AND 시가총액 > 1000000000000""")
        selected_stocks = cursor.fetchall()
        cursor.close()
        conn.close()
        return selected_stocks

    def show_code_list(self):
        selected_stocks = self.check_code_list()
        if selected_stocks:
            print("선택된 종목 정보:")
            for stock in selected_stocks:
                company_name, code, 접수일, 전환가액 = stock
                print(f"회사명: {company_name}, 종목코드: {code}, 접수일: {접수일}, 전환가액: {전환가액}")
        else:
            print("조건에 해당하는 종목이 없습니다.")

