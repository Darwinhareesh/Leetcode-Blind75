# We use defaultdict because it automates missing key handling, making code shorter, safer, and more expressive compared to plain dict
from collections import defaultdict
class Solution:
    def groupAnagrams(self, str: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        res = []
        for i in str:
            sorted_string = tuple(sorted(i))
            map[sorted_string].append(i)
        
        return list(map.values())
