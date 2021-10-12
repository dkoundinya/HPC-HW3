# PartA-Question 4
s=str(input("Please enter a string: "))
a=0;
new_s=[]
for i in range(0,len(s)):
        if s[i] in s[0:i-1]: 
            new_s.append(s[a:i])
            a=i+1
if i==len(s) and s[i] not in s[0:i-1]:
    new_s.append(s)
ans = max(new_s, key= len)
print(len(ans))
