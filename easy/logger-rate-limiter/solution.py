class Logger:
    def __init__(self):
        # Dictionary to store message -> last printed timestamp
        self.message_dict = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If message hasn't been printed before, allow it and store timestamp
        if message not in self.message_dict:
            self.message_dict[message] = timestamp
            return True
        
        # If 10 seconds have passed since last print, allow it and update timestamp
        if self.message_dict[message] + 10 <= timestamp:
            self.message_dict[message] = timestamp
            return True
        
        # Otherwise, rate limit - don't print
        return False
