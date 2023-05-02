import sqlite3
import matplotlib.pyplot as plt

# 데이터베이스 연결
conn = sqlite3.connect('C:/Users/min17/Desktop/과제/2-1학기/경원2 데이터.db')
cur = conn.cursor()

# 데이터 가져오기
cur.execute('SELECT volume, interest, date FROM economy2')
data = cur.fetchall()

# 그래프 그리기
x = [d[0] for d in data]
y = [d[1] for d in data]
dates = [d[2] for d in data]

plt.scatter(x, y)
plt.xlabel('Volume')
plt.ylabel('Interest')
plt.title('Supply and Demand Graph')

# 그래프를 png 파일로 저장
plt.savefig('graph.png')