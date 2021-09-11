class Trie:
    def __init__(self, words):
        self.root = {}
        for word in words:
            node = self.root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['leaf'] = word

    def search(self, s):
        ret = []
        node = self.root
        for c in s:
            if c in node:
                node = node[c]
            else:
                break
            if 'leaf' in node:
                ret.append(node['leaf'])
        print(ret)
        return ret


from collections import defaultdict

class Solution:
    def multiSearch(self,big,smalls):
        trie = Trie(smalls)
        hit = defaultdict(list)

        for i in range(len(big)):
            matchs = trie.search(big[i:])
            for word in matchs:
                hit[word].append(i)

        ret = []
        for m in smalls:
            ret.append(hit[m])

        return ret

big="mississippi"
smalls=["is","iss","ppi","hi","sis","ids","ssippi"]
ft=Solution()
ft.multiSearch(big,smalls)