class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        res = {}
        for w in words:
            if w in count:
                count[w] = count[w] + 1
            else:
                count[w] = 1
        res = dict(sorted(count.items(), key = lambda x: (-x[1], x[0])))
        result = list(islice(res, k))
        return result
