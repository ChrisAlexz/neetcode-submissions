class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap to count occurence of each value 
        freq = [[] for i in range(len(nums) + 1) ] #index is count of an element, value is list of value that occur to that num 

        for n in nums: 
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items(): # for every key value pair of number and its count
            freq[c].append(n) # this value n occurs c number of times 

        res = []
        for i in range (len(freq) -1,0,-1): #loop backwards 
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        


        