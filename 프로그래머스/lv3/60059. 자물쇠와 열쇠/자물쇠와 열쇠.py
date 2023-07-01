def solution(key, lock):
    global arr, N, M
    answer = False
    M = len(key)
    N = len(lock)
    
    # 자물쇠 범위 생성
    arr = [[0] * (3 * N) for _ in range(3 * N)]
    
    # 키 회전
    for _ in range(4):
        
        for i in range(1, 2 * N):
            for j in range(1, 2 * N):
                
                # 자물쇠 범위에 값 대입
                init_lock(lock)
                
                # 키 이동
                move_key(key, i, j)
                
                # 자물쇠 열림 여부 체크
                if check_lock():
                    return True
        
        # 키 회전
        key = turn_key(key)
        
    return answer


# 자물쇠 범위에 값 대입
def init_lock(lock):
    for i in range(N, 2 * N):
        for j in range(N, 2 * N):
            arr[i][j] = lock[i - N][j - N]

            
# 키 이동 함수
def move_key(key, x, y):
    for i in range(x, x+M):
        for j in range(y, y+M):
            if key[i-x][j-y] == 1:
                # 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됨
                if arr[i][j] == 1:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 1
                

# 키 회전 함수
def turn_key(key):
    rotate = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotate[j][M-i-1] = key[i][j]
    return rotate
    

# 자물쇠 범위 체크 함수
def check_lock():
    for i in range(N, 2 * N):
        for j in range(N, 2 * N):
            if arr[i][j] == 0:
                return False
    return True
            
