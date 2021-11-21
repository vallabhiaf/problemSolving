class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list) #to protect corner case of no count array
        
        for s in strs:
            count=[0] *26
            for char in s:
                count[ord(char)-ord("a")] +=1
            
            res[tuple(count)].append(s) #count is a list which cannot be stored in dict so converting it to tuple 
            
        return res.values()