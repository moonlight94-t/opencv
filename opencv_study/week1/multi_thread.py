import threading

# 결과를 저장할 전역 변수
result = 0
lock = threading.Lock()

def sum_part(start, end):
    global result
    part_sum = sum(range(start, end + 1))
    
    # 스레드가 결과를 더할 때 충돌이 없도록 Lock 사용
    with lock:
        result += part_sum

# 첫 번째 스레드가 담당할 범위
start1, end1 = 1, 50000000

# 두 번째 스레드가 담당할 범위
start2, end2 = 50000001, 100000000

# 두 개의 스레드를 생성
thread1 = threading.Thread(target=sum_part, args=(start1, end1))
thread2 = threading.Thread(target=sum_part, args=(start2, end2))

# 스레드 시작
thread1.start()
thread2.start()

# 스레드가 끝날 때까지 대기
thread1.join()
thread2.join()

# 최종 결과 출력
print(f"1부터 100,000,000까지의 합: {result}")
