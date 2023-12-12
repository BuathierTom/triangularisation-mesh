class Face: 
    def __init__(self, s1, s2, s3):
        self.sommets = [s1, s2, s3]
        
    
    def __repr__(self):
        return f"Face({self.sommets[0]}, {self.sommets[1]}, {self.sommets[2]})"