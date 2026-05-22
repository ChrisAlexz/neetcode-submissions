class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) 
        freq = [[] for i in range(len(nums)+1)]
    
        for n in nums: 
            count[n] += 1 # counts how many times each values occurs
        for number, c in count.items(): # for every key value pairs
            freq[c].append(number) #this val number occurs c number of times

        res = []
        for i in range(len(freq)-1, 0, -1): #-1 is decremeter, going to 0, and index -1
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res