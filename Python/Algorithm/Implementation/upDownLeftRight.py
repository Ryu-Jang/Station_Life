#예제 4-1 상하좌우 23-01-10

'''
최초 알고리즘 접근 방향
n = input
option = [U,D,R,L]

for i in option
    if ((0,0)< n(k,k) + i(1,0) < (0,0))
        sum(n,up)

즉 실제로 2차원 평면 배열을 만들어서 푸는 방법
개발 측면에선 적합하지만 코딩테스트에선 적합하지 않은것 같다.
'''

# n = int(input())
n = 5
dn = [n,n]
startpoint = [1,1]
option = [(1,0),(-1,0),(0,-1),(0,1)]
# selectOption = list(map(chr,input().split()))
selectOption = ["R","R","R","U","D","D"]
for i in selectOption :
        if (i == "D" and 0 <startpoint[0]+option[0][0]< 5) :
            startpoint = [startpoint[j] + option[0][j] for j in range(len(startpoint))]
            print("==>> startpoint: ", startpoint)
        elif (i == "U" and 0 <startpoint[0]+option[1][0]< 5) :
            startpoint = [startpoint[j] + option[1][j] for j in range(len(startpoint))]
            print("==>> startpoint: ", startpoint)
        elif (i == "L"and 0 <startpoint[0]+option[2][1]< 5) :
            startpoint = [startpoint[j] + option[2][j] for j in range(len(startpoint))]
            print("==>> startpoint: ", startpoint)
        elif (i == "R"and 0 <startpoint[0]+option[3][1]< 5) :
            startpoint = [startpoint[j] + option[3][j] for j in range(len(startpoint))]
            print("==>> startpoint: ", startpoint)

print(startpoint[0] , startpoint[1])

'''
문제의 의도대로 작성헀지만 보기 어렵고 난해한 스파게티 코드가 됐다.
다시 소스코드를 재 작성해 쉽고 빠른 코드로 만들어보겠다.

'''

