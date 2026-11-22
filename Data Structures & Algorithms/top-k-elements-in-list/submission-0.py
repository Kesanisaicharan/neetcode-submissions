class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}
        for num in nums:#countfreq
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        sorted_nums=sorted(freq,key=freq.get,reverse=True)#sortnum

        return sorted_nums[:k]#return num


