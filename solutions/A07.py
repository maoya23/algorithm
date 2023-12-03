#イベントの参加人数を求める
'''
D=int(input())
N=int(input())
A=[None]*N
B=[None]*N
for i in range(N):
    A[i],B[i]=list(map(int,input().split()))

S=[0]*(D+1)
S[0]=0

for i in range(N):
    for j in range(A[i],B[i]+1):
        S[j]=S[j]+1

for i in range(1,D+1):
    print(S[i])


'''


#正解のコード
D = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
	L[i], R[i] = map(int, input().split())

# 前日比に加算
B = [ 0 ] * (D+2)
for i in range(N):
	B[L[i]] += 1
	B[R[i]+1] -= 1

# 累積和をとる
Answer = [ None ] * (D+2)
Answer[0] = 0
for d in range(1, D+1):
	Answer[d] = Answer[d - 1] + B[d]

# 出力
for d in range(1, D+1):
	print(Answer[d])

#イベントの当日の要素に１を足して最後の日の翌日に１を引くことで、後々累積和を取る際に
#当日から最後の日までの人数を足し合わせることができる
#結局後で累積和を取るから、当日に１のふらぐを立てておけばその区間ずっと１が経っていることになる。