class Centroid:
    def __init__(self):
        self.assignments = []
        self.previous_assignments = []
        self.word_count = []
        self.blogs = []
    
    def set_word_count(self,val):
        self.word_count.append(val)
    
    def clear_previous_assignments(self):
        self.previous_assignments = []
    
    def update_word_count(self,val,i):
        self.word_count[i] = val
    
    def assign(self,blog):
        self.assignments.append(blog)
    
    def clear_assignments(self):
        self.assignments = []
    
    def record_previous_assignments(self):
        self.previous_assignments = self.assignments
