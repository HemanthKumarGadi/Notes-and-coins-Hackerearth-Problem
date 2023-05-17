#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
coins = []
notes = []
for i in range(n):
    inp = input()
    if("Coin" in inp):
        coins.append(inp.split()[1])
    elif("Note" in inp):
        notes.append(inp.split()[1])
print("Coins :")
for i in coins:
    print(i)
print("Notes :")
for i in notes:
    print(i)

