import threading

def sum_part(start, end, return_dict, key): #굳이 함수 인수로 넣어야하나?
    part_sum = sum(range(start, end + 1))
    return_dict[key] = part_sum

# 첫 번째 스레드가 담당할 범위
start1, end1 = 1, 50000000

# 두 번째 스레드가 담당할 범위
start2, end2 = 50000001, 100000000

# 스레드의 결과를 저장할 사전 (딕셔너리)
return_dict = {}

# 두 개의 스레드를 생성
thread1 = threading.Thread(target=sum_part, args=(start1, end1, return_dict, 't1'))
thread2 = threading.Thread(target=sum_part, args=(start2, end2, return_dict, 't2'))

# 스레드 시작
thread1.start()
thread2.start()

# 스레드가 끝날 때까지 대기
thread1.join()
thread2.join()

# 각 스레드의 결과를 합산
total_sum = return_dict['t1'] + return_dict['t2']

# 최종 결과 출력
print(f"1부터 100,000,000까지의 합: {total_sum}")