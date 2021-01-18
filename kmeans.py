from typing import Generator
from models.centroid import Centroid
from stats import pearson
from models.centroidgenerator import Centroid_generator


def check_if_same_cluster(centroids):
    same_assignments = 0
    n_centroids = len(centroids)
    for centroid in centroids:
        if centroid.assignments == centroid.previous_assignments:
            same_assignments += 1
    if same_assignments == n_centroids:
        return True
    return False

def update_clusters(centroids,blog_len):
    for centroid in centroids:
        for i in range(blog_len):
            avg = 0
            for blog in centroid.assignments:
                avg += blog.words[i]
                avg /= len(centroid.assignments)
            
            centroid.update_word_count(avg,i)
        centroid.blogs = centroid.assignments
        centroid.record_previous_assignments()
        centroid.clear_assignments()

def k_means(blogs,k,n):
    generator = Centroid_generator()
    centroids = generator.generate_centroids(k,blogs)
    blog_len = len(blogs)
    for i in range (n):
        for blog in blogs:
            distance = 1000
            best_fit = Centroid()
            for centroid in centroids.centroids:
                c_distance = pearson(blog,centroid.word_count)
                if c_distance < distance:
                    best_fit = centroid
                    distance = c_distance
            best_fit.assign(blog)

        if check_if_same_cluster(centroids.centroids):
            for centroid in centroids.centroids:
                centroid.clear_assignments()
                centroid.clear_previous_assignments()
            return centroids.centroids
        update_clusters(centroids.centroids,blog_len)
    return centroids.centroids