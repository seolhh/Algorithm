# 시작한 열의 행에서 바로 다음열로 이동, 범위만 사각형 안에서
# 처음 시작한 행도 숫자 카운트
# 점화식이니까 뒤에서 부터 카운트 -> 가장 오른쪽 특정위치는
# 왼쪽 위, 왼쪽, 왼쪽 아래 중에서 온 것.




N = int(input())
for i in range(N):
    n,m = map(int,input().split())
    gold_list = list(map(int,input().split()))
    # print(n,m,gold_list)
    dp = []
    for i in range(n):
        dp.append(gold_list[i*m : i*m+m])
        print(dp)

    # dp시작
    for j in range(1, m):# 행은 상관 없으니까
        for i in range(n):
            # print(dp[i][j])
            # 왼쪽 위가 없다면
            if (i == 0):
                dp[i][j] += max(dp[i][j - 1], dp[i + 1][j - 1])
                # print(dp[i][j],dp[i][j - 1],dp[i + 1][j - 1])
            # 왼쪽 아래가 없다면
            elif (i == n - 1):
                dp[i][j] += max(dp[i - 1][j - 1], dp[i][j - 1])
            # 왼쪽 위와 왼쪽 아래가 다 있다면
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

        # 얻을 수 있는 금의 최대 크기 비교
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
