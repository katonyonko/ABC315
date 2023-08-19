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
4 3
aaa
aaa
abc
abd
2 5
aaaaa
abcde
3 3
ooo
ooo
ooo
3 3
ooo
oob
ook
"""

def solve(test):
  H,W=list(map(int, input().split()))
  S=[input() for _ in range(H)]
  ansh=[[0]*26 for _ in range(H)]
  answ=[[0]*26 for _ in range(W)]
  vh=0 #消えている数
  vw=0
  vh2=[0]*H #消えているか
  vw2=[0]*W
  hs=[0]*H #種類数
  ws=[0]*W
  for i in range(H):
    for j in range(W):
      if ansh[i][ord(S[i][j])-ord('a')]==0:
        hs[i]+=1
      if answ[j][ord(S[i][j])-ord('a')]==0:
        ws[j]+=1
      ansh[i][ord(S[i][j])-ord('a')]+=1
      answ[j][ord(S[i][j])-ord('a')]+=1
  p=[]
  for i in range(H):
    if hs[i]==1:
      p.append((i,0))
  for i in range(W):
    if ws[i]==1:
      p.append((i,1))
  while p:
    tmp=p.copy()
    tmp2=[]
    p=[]
    while tmp:
      x,y=tmp.pop()
      if y==0:
        if vw>=W-1:
          continue
        tmp2.append((x,y))
        for i in range(W):
          if vw2[i]==0:
            answ[i][ord(S[x][i])-ord('a')]-=1
            if answ[i][ord(S[x][i])-ord('a')]==0:
              ws[i]-=1
              if ws[i]==1 and vw2[i]==0:
                p.append((i,1))
      else:
        if vh>=H-1:
          continue
        tmp2.append((x,y))
        for i in range(H):
          if vh2[i]==0:
            ansh[i][ord(S[i][x])-ord('a')]-=1
            if ansh[i][ord(S[i][x])-ord('a')]==0:
              hs[i]-=1
              if hs[i]==1 and vh2[i]==0:
                p.append((i,0))
    for x,y in tmp2:
      if y==0:
        vh+=1
        vh2[x]=1
      else:
        vw+=1
        vw2[x]=1
  print(max(0,(H-vh))*max(0,(W-vw)))

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