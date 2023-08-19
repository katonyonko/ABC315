import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
6
3 2 3 4
2 3 5
0
1 5
0
0
6
1 2
1 3
1 4
1 5
1 6
0
8
1 5
1 6
1 7
1 8
0
0
0
0
3
2 2 3
0
1 2
"""

def bfs(G,s):
  inf=10**30
  D=[inf]*len(G)
  D[s]=0
  dq=deque()
  dq.append(s)
  while dq:
    x=dq.popleft()
    for y in G[x]:
      if D[y]>D[x]+1:
        D[y]=D[x]+1
        dq.append(y)
  return D

def TopologicalSort(G):
  G2=[set() for _ in range(len(G))]
  for i in range(len(G)):
    for v in G[i]:
      G2[v].add(i)
  res=[]
  h=[]
  for i in range(len(G)):
    if len(G2[i])==0:
      heappush(h,i)
  while len(h):
    x=heappop(h)
    res.append(x)
    for y in G[x]:
      G2[y].remove(x)
      if len(G2[y])==0:
        heappush(h,y)
  if len(res)==len(G):
    return res
  else:
    return -1

def solve(test):
  N=int(input())
  G=[[] for _ in range(N)]
  for i in range(N):
    A=list(map(int, input().split()))
    for j in range(1, len(A)):
      G[i].append(A[j]-1)
  tmp=[]
  D=bfs(G,0)
  ans=TopologicalSort(G)[::-1]
  for i in range(N):
    if D[ans[i]]!=10**30:
      tmp.append(ans[i]+1)
  ans=tmp
  if test==0:
    print(*ans[:-1])
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)