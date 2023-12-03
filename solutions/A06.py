
#遊園地に来た人の人数を求める
N,Q=map(int,input().split())
A=list(map(int,input().split()))

a=[None]*Q
b=[None]*Q
for i in range(Q):
    a[i],b[i]=map(int,input().split())

S=[None]*(N+1)
S[0]=0
for i in range(N):
    S[i+1]=S[i]+A[i]

for i in range(Q):
    print(S[b[i]]-S[a[i]-1])
