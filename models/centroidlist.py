class Centroid_list():
    def __init__(self, list):
        self.centroids = list
    
    def clear_assignments(self):
        for centroid in self.centroids:
            centroid.clear_assignments()

    