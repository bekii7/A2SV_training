#User function Template for python3
from collections import Counter
class Solution:
    def isSubset(self, a, b):
        # Your code here
        
        return not (Counter(b) - Counter(a))