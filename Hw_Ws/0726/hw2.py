x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.append(y)
print('x:', x)
#append는 y값을 그대로 추가한다

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y)
print('x:', x)

#extend는 가장 바깥쪽 iterable의 모든 항목을 넣어준다