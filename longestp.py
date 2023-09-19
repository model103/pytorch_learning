def longest(s:str):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    max_length = 1
    begin = 0
    for i in range(n):
        dp[i][i] = True

    for l in range(2,n+1):  #先扫描长度
        for i in range(n): #在扫描begin
            j = i+l-1
            if j >=n:
                break
            if s[i] == s[j]:
                if j - i > 2:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = True
            if dp[i][j] and j-i+1 >max_length:
                max_length = j-i+1
                begin = i
    return s[begin:begin+max_length]


s = 'abcccccab'
print(longest(s))
