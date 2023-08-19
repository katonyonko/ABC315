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
4
1 4
2 10
2 8
3 6
4
4 10
3 2
2 4
4 12
"""

def solve(test):
  N=int(input())
  cup=[[] for _ in range(N)]
  for i in range(N):
    F,S=list(map(int, input().split()))
    F-=1
    cup[F].append(S)
  for i in range(N):
    cup[i].sort(reverse=True)
  ans=0
  for i in range(N):
    if len(cup[i])>=2:
      ans=max(ans, cup[i][0]+cup[i][1]//2)
  x=[]
  for i in range(N):
    if len(cup[i])>=1: x.append(cup[i][0])
  x.sort(reverse=True)
  if len(x)>=2:
    ans=max(ans, x[0]+x[1])
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