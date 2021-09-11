digits = "23"
def conbine(a,b):
    ans=[]
    for fir in a:
        for sec in b:
            ans.append(fir+sec)
    return ans
alpha={"2": "abc","3": "def","4": "ghi", "5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz",}
if not digits:
    return []
if len(digits)==1:
    return list(alpha[digits])
else:
    ans=conbine(list(alpha[digits[0]]),list(alpha[digits[1]]))
    for i in range(2,len(digits)):
        ans=conbine(ans,list(alpha[digits[i]]))
    return ans
