class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7
        # dp[i][j] 表示用j首不同的歌填充长度为i的歌单
        dp = [[0] * (N + 1) for _ in range(L + 1)]
        dp[0][0] = 1
        for i in range(1, L + 1):
            for j in range(1, N + 1):
                # 分成两种情况
                # 如果当前的歌和前面的都不一样，歌单前i-1首歌只包括了j-1首不同的歌曲，
                # 那么当前的选择有dp[i-1][j-1] * (N-j+1)
                # 如果当前的歌和前面的有重复的，那最近的K首必然是不能重复的，
                # 所以选择就是dp[i-1][j] * max(0, j-K)
                dp[i][j] = (dp[i-1][j-1] * (N - j + 1) + dp[i-1][j] * max(0, j - K)) % mod
        return dp[-1][-1]

作者：lu-gui-chen-2
链接：https://leetcode-cn.com/problems/number-of-music-playlists/solution/python-dp-chao-jian-ji-by-lu-gui-chen-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。