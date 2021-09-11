N=10
memo={1:[1],2:[1,2]}
def f(n):
    if n in memo:
        return memo[n]
    print(memo)
    odds=int(n/2 if n%2==0 else (n+1)/2)
    evens=int(n/2 if n%2==0 else (n-1)/2)
    '''平分后的奇偶 odds evens'''
    if odds not in memo:
        f(odds)
    if evens not in memo:
        f(evens)
    memo[n]=[2*x-1 for x in memo[odds]]+[2*x for x in memo[evens]]
    print(memo)
    return memo[n]
print(f(15))


