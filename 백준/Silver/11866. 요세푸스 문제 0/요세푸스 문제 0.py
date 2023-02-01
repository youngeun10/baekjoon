n,k=map(int,input().split())
i,*q=range(n+1)
print(f"<{str([q.pop(i:=(i+k-1)%p)for p in q[::-1]])[1:-1]}>")