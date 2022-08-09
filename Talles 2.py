A, B, D, cont = set(), set(), set(), 0

for x in range(6,21):
  A.add(x)

for x in range(1,25):
  if x % 2 == 0:
    B.add(x)

C = {1,4,8,10,12,15,18,20}

for x in range(2,46):
  for y in range(2,46):
    if x % y == 0:
      cont += 1
  if cont == 1:
    D.add(x)
  cont = 0

def union(a,b):
  c = set()
  for x in a:
    c.add(x)
  for x in b:
    c.add(x)
  return c

def inter(a,b):
  c = set()
  for x in a:
    if x in b:
      c.add(x)
  return c

def difer(a,b):
  c = set()
  for x in a:
    if x not in b:
      c.add(x)
  return c

def difer_sime(a,b):
  c = set()
  for x in a:
    if x not in b:
      c.add(x)
  for x in b:
    if x not in a:
      c.add(x)
  return c

print("A =",A)
print("B =",B)
print("C =",C)
print("D =",D)

print("\nB ∩ (C ⊕ D) =",inter(B,difer_sime(C,D)))
print("(A ∩ C) ∪ B =",union(inter(A,C),B))
print("(B ∪ D) - C =",difer(union(B,D),C))
print("(A - B) ⊕ (A ∩ D) =",difer_sime(difer(A,B),inter(A,D)))
