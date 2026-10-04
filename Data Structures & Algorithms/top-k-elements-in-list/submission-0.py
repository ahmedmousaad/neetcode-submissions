class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = defaultdict(int)

        for num in nums:
            freq_counter[num] += 1
            
        sorted_dict = dict(
            sorted(freq_counter.items(), key=lambda item: item[1], reverse=True)
        )
        
        top_k_element = list(sorted_dict.keys())[:k]

        return top_k_element