from models.centroidlist import Centroid_list
from models.centroid import Centroid
from random import randint


class Centroid_generator():
    def __init__(self):
        self

    def get_max_min_dict(self,blogs):
        min_set = dict()
        max_set = dict()
        for j, blog in enumerate(blogs):
            for k, val in enumerate(blog.words):
                if k not in min_set.keys():
                    min_set[k] = val
                    max_set[k] = val
                else:
                    if min_set[k] > val:
                        min_set[k] = val
                    elif max_set[k] < val:
                        max_set[k] = val
        return min_set, max_set

    def set_random_vals(self,min_set, max_set, c):
        for i in range(len(min_set)):
            random_num = randint(min_set[i], max_set[i])
            c.word_count.append(random_num)

    def generate_centroids(self,k, blogs):
        centroids = list()
        for i in range(k):
            c = Centroid()
            min_set, max_set = self.get_max_min_dict(blogs)
            self.set_random_vals(min_set, max_set, c)
            centroids.append(c)
        return Centroid_list(centroids)
