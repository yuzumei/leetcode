items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
ans=0
if ruleKey=="type":
    k=0
elif ruleKey=="color":
    k=1
else:
    k=2
for i in range(len(items)):
    if items[i][k]==ruleValue:
        ans+=1
return ans

