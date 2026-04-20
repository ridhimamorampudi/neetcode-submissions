class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 6/2 = 3 hrs pop + 1
        # 9/2 = 4.5 pop + 1
        # 10/1 = 10 hrs pop +1
        # 3/1 = 3



        stack = []
        flattened = [(p,s) for (p,s) in zip(position,speed)]
        flattened.sort(reverse=True)
        count = 0
        print(stack)
        for (pos,spd) in (flattened):
            stack.append((target-pos)/spd)
            if len(stack) >=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)

      

            
            


