x="2*3-4*5"


def calc(s):
    ans = []
    if s.isdigit():
        return [int(s)]
    for i,item in enumerate(s):
        if item in ['+','-','*']:
            left=calc(s[:i])
            right=calc(s[i+1:])
            for l in left:
                for r in right:
                    if item == "+":
                        ans.append(l + r)
                    if item == "-":
                        ans.append(l - r)
                    if item == "*":
                        ans.append(l * r)
    return ans

print(calc(x))
class Solution:
    def diffWaysToCompute(self, input) :
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res

solu=Solution()
print(solu.diffWaysToCompute(x))