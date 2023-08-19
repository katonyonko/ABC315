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
0 0
1 1
2 0
0 1
1 0
2 1
10
1 8
3 7
9 4
4 9
6 1
7 5
0 0
1 3
6 8
6 4
10
34 24
47 60
30 31
12 97
87 93
64 46
82 50
14 7
17 24
3 78
"""

inf=1<<30
def idx(i, j):
  return i*31+j

def solve(test):
  N=int(input())
  P=[list(map(int, input().split())) for _ in range(N)]
  dp=[inf]*N*31
  dp[idx(0,0)]=0
  for i in range(N-1):
    for j in range(31):
      for k in range(1,min(31-j, N-1-i)+1):
        dp[idx(i+k,j+k-1)]=min(dp[idx(i+k,j+k-1)], dp[idx(i,j)]+((P[i][0]-P[i+k][0])**2+(P[i][1]-P[i+k][1])**2)**.5)
  ans=min([dp[idx(N-1,j)]+(1<<(j-1) if j>0 else 0) for j in range(31)])
  if test==0:
    print(ans)
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