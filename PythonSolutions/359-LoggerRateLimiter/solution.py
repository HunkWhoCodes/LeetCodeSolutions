class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logger_map = {}
        
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.logger_map:
            if timestamp < self.logger_map[message]:
                return False
            else:
                timestamp += 10
                self.logger_map[message] = timestamp
                return True
        else: 
            timestamp += 10
            self.logger_map[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
