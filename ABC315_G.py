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
5 3 1 5 15
1 1 1 1 1
100000 31415 92653 58979 1000000000
"""

#拡張ユークリッド ax+by=gcd(a,b)となるようなx,yを求める。同時にgcdも求める
#aとbが互いに素な時、xはmod bにおいてのaの逆元
def ExtGCD(a, b):
    if b:
        g, y, x = ExtGCD(b, a % b)
        y -= (a // b)*x
        return g, x, y
    return a, 1, 0

#mが素数と限らない場合にmod.mに置けるaの逆元（aとmが互いに素であることが必要十分条件）を求める関数
def Inv(a,m):
    return ExtGCD(a,m)[1]%m

# 中国剰余定理。以下を満たすxを求める
# x≡b1 (mod.m1)
# x≡b2 (mod.m2)
import math
def Ch_Rem(b1,b2,m1,m2):
    g,p,q=ExtGCD(m1,m2)
    d=math.gcd(m1,m2)
    lcm=m1*m2//d
    return (b1+m1//d*(b2-b1)*p)%lcm

def solve(test,_):
  N,A,B,C,X=map(int,input().split())
  d=math.gcd(B,C)
  ans=0
  for i in range(1,N+1):
    m=X-A*i
    if m%d!=0:
      continue
    l=max(1,(m-C*N-1)//B+1)-1
    r=min(N,(m-C)//B)
    if l>=r:
      continue
    j=m//d*Inv(B//d,C//d)%(C//d)
    ans+=(r-j)//(C//d)-(l-j)//(C//d)
    if _==1: print(i,j,l,r,(r-j)//(C//d)-(l-j)//(C//d))
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
    solve(0,0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0,_)
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