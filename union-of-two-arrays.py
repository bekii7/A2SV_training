class Solution:    
    def findUnion(self, a, b):
        # code here
        result_set = set(a) | set(b) 
        return sorted(list(result_set))