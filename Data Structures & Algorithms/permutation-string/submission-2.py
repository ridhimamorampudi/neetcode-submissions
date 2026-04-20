class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_counter = collections.Counter(s1)
        window_counter = collections.Counter(s2[:len(s1)])
        
        if s1_counter == window_counter:
            return True
        
        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            end_char = s2[i]
            
            window_counter[end_char] += 1
            window_counter[start_char] -= 1
            
            if window_counter[start_char] == 0:
                del window_counter[start_char]
            
            if window_counter == s1_counter:
                return True
        
        return False