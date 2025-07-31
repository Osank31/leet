class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result=set()
        prev=set()

        for num in arr:
            curr=set()
            
            for x in prev:
                curr.add(x | num)
                result.add(x | num)
            
            curr.add(num)
            result.add(num)

            prev=curr
        
        return len(result)