class TimeMap:

    def __init__(self):
        self.timestamps = {}
        self.keyStamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.timestamps:
            self.timestamps[timestamp] = {}
        self.timestamps[timestamp][key] = value
        self.keyStamps[key].append(timestamp)

        # print(f"timestamps:{self.timestamps}")
        # print(f"keyStamps:{self.keyStamps}")
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keyStamps:
            if timestamp in self.keyStamps[key]:
                return self.timestamps[timestamp][key]
            else:
                index = float('inf')
                for i in range(len(self.keyStamps[key])):
                    if self.keyStamps[key][i] < timestamp:

                        index = self.keyStamps[key][i]
                        # print(index)
                
                
                return self.timestamps[index][key] if index != float('inf') else ""
        else:
            return ""
                
                

        





    
#    {1: {alice: happy},
#    2: { }
#    }
#    alice: [1,2,3]

        
