class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sum_dig(n):
            sum = 0
            while n > 0:
                sum += (n %10)*(n%10)
                n= n//10
            return sum
        

        while n != 1:
            if n not in visited:
                visited.add(n)
            else:
                return False
            
            n = sum_dig(n)
            print(n)
        
        return True
        

        
                