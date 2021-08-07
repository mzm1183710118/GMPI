import numpy as np
import random

book=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# (a)
# res_list=[]
# for i in range(100):
#     ind=list(np.random.randint(0,26,4))
#     temp=[book[i] for i in ind]
#     a=''.join(temp)
#     res_list.append(a)
# res=', '.join(res_list)
# print(res)

# (b)
# counts=[]
# with open('saki_story.txt','r') as f:
#     txt=f.read()
#     txt=txt.strip()
#     txt=txt.replace(' ','')
#     txt=txt.replace('\n','').lower()
#     for a in book:
#         counts.append(txt.count(a))
# a=sum(counts)
# counts=np.cumsum(np.array(counts,dtype='float'))
# counts/=a
# print(counts)
# res_list=[]
# np.random.rand(100,4)
# for i in range(100):
#     word=''
#     for j in range(4):
#         x=random.uniform(0,1)
#         for num,k in enumerate(counts):
#             if x <k:
#                 word+=book[num]
#                 break
#     res_list.append(word)
# res=' '.join(res_list)
# print(res)

# # (c)
transition_matrx_without_block=[]
counts=[]
with open('saki_story.txt','r') as f:
    txt=f.read()
    txt=txt.strip()
    txt=txt.replace(' ','')
    txt=txt.replace('\n','').lower()
    for a in book:
        counts.append(txt.count(a))
    for i in range(26):
        if(counts[i]==0):
            transition_matrx_without_block.append([0]*26)
            continue
        line=[]
        for j in range(26):
            line.append(txt.count(book[i]+book[j]))
        count=sum(line)
        line=list(np.array(line,dtype='float')/count)
        transition_matrx_without_block.append(line)


transition_matrx_with_block=[]

with open('saki_story.txt','r') as f:
    txt=f.read()
    txt=txt.strip()
    txt=txt.lower()
    for i in range(26):
        if(counts[i]==0):
            transition_matrx_with_block.append([0]*26)
            continue
        line=[]
        for j in range(26):
            line.append(txt.count(book[i]+book[j]))
        count=sum(line)
        line=list(np.array(line,dtype='float')/count)
        transition_matrx_with_block.append(line)

res_list=[]
a=sum(counts)
countss=np.cumsum(np.array(counts,dtype='float'))
countss/=a
for i in range(100):
    word=''
    #first letter
    x=random.uniform(0,1)
    last_letter_ind=-1
    for num,k in enumerate(countss):
        if x <k:
            last_letter_ind=num
            word+=book[num]
            break
    
    #2,3,4 letter
    for i in range(3):
        if counts[last_letter_ind]==0:
            break
        line=transition_matrx_with_block[last_letter_ind]
        x=random.uniform(0,1)
        sum=0
        for letter_num in range(26):
            if x<sum+line[letter_num]:
                last_letter_ind=letter_num
                word+=book[letter_num]
                break
            sum+=line[letter_num]
    res_list.append(word)
res=' '.join(res_list)
print(res)