import time

# 1. 재귀 함수를 이용한 피보나치 수열 구현
def fib_recursive(n):
    """
    재귀를 사용하여 n번째 피보나치 수를 계산합니다.
    n이 30-40 이상으로 커지면 매우 비효율적입니다.
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# 2. 반복문을 이용한 피보나치 수열 구현
def fib_iterative(n):
    """
    반복문을 사용하여 n번째 피보나치 수를 효율적으로 계산합니다.
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# 3. 실행 시간 측정 및 비교
if __name__ == "__main__":
    while True:
        try:
            num = int(input("계산할 피보나치 수열의 n번째 항을 입력하세요 (종료하려면 0 또는 음수 입력): "))
            if num <= 0:
                print("프로그램을 종료합니다.")
                break

            # --- 재귀 방식 실행 및 시간 측정 ---
            print(f"\n--- 재귀 방식 (n={num}) ---")
            start_time_rec = time.time()
            try:
                # 재귀 깊이 제한에 걸릴 수 있으므로 n이 너무 크면 실행하지 않음
                if num > 35:
                     print("n이 너무 큽니다. 재귀 방식은 시간이 매우 오래 걸리므로 건너뜁니다.")
                     result_rec = "N/A"
                     end_time_rec = start_time_rec
                else:
                    result_rec = fib_recursive(num)
                    end_time_rec = time.time()
                    print(f"결과: {result_rec}")

                elapsed_time_rec = end_time_rec - start_time_rec
                print(f"실행 시간: {elapsed_time_rec:.10f} 초")

            except RecursionError:
                print("오류: 재귀 깊이가 너무 깊습니다. 더 작은 n 값을 입력해주세요.")


            # --- 반복 방식 실행 및 시간 측정 ---
            print(f"\n--- 반복 방식 (n={num}) ---")
            start_time_iter = time.time()
            result_iter = fib_iterative(num)
            end_time_iter = time.time()
            elapsed_time_iter = end_time_iter - start_time_iter
            
            print(f"결과: {result_iter}")
            print(f"실행 시간: {elapsed_time_iter:.10f} 초")
            print("-" * 20)

        except ValueError:
            print("잘못된 입력입니다. 정수를 입력해주세요.")
