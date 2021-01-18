from models.blog import Blog


class Cluster:
    def __init__(self, left=None, right=None, parent=None, blog=None, distance=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.blog = blog
        self.distance = distance

