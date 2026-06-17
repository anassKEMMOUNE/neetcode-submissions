class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {str(sorted(i)):[] for i in strs}
        for i in strs :
            hsh[str(sorted(i))].append(i)
        return [i for i in hsh.values()]
        