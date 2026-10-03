from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        angram_map = defaultdict(list)

        for word in strs:

            sorted_word  = "".join(sorted(word))

            angram_map[sorted_word].append(word)

        return list(angram_map.values())