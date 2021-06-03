input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])-int(ord('a'))+1) #시작점은 1이기때문에 영어를 숫자 좌표로 환산해주는것

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

# 8가지 방향에 대하여 이동이 가능한지 확인

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)