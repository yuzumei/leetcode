class Solution():
    def bestRotation(self, A):
        #score[k]:表示移动K步后，当前分数应该加几分，正数为加，负数为扣
        score = [0] * len(A)
        for i in range(len(A)):
            score[(i + len(A) - A[i] + 1) % len(A)] -= 1
        for i in range(1, len(A)):
            score[i] += score[i - 1] + 1
        return score.index(max(score))

作者：my10yuan
链接：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score/solution/zui-gao-xiao-de-jie-fa-by-wu-yan-34/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。