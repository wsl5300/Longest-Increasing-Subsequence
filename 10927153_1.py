# 演算法分析機測
# 學號: 10927153 / 10927248 /10927256
# 姓名: 吳上玲 / 連翊安 / 姜美羚
# 中原大學資訊工程系

def find_ans( test ) : #輸入一列測資
    n = []
    ns = []
    for i in test :
        #if len(ns) == 0:
        n = [i]
        ns.append(n)
        for j in range(len(ns)) : #與目前陣列的最後一個數比較
            if i > ns[j][len(ns[j])-1] :
                n = ns[j].copy()
                n.append(i)
                #print(n)
                ns.append(n)
                n = []
                
        n = []

    for i in range(len(ns)):
        if i == 0 :
            max = i
        elif len(ns[i]) > len(ns[max]):
            max = i
        #print(ns[i])
    return ns[max]


tests = []
ans = []

while True :
    m = input("continue?(y/n)")
    if m != 'y':
        break
    i = int(input("size:"))
    while i != 0 :
        tests.append(list(map( int, input().split() ) ) )
        i = int(input("size:"))
        
    for answer in tests :
        answer = find_ans(answer)
        ans.append(answer)
    

    for i in range(len(ans)):
        print(f"Case {i+1}")
        print(f"Length of LIS = {len(ans[i])}")
        print(f"LIS = {', '.join(map( str, ans[i]))}")
    tests = []
    ans = []
    print("\n")
        