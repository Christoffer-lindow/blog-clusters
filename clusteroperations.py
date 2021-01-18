from statistics import pearson
from models.cluster import Cluster
from models.blog import Blog
from time import time


def generate_cluster_list(blog_dict):
    cluster_list = list()
    for blog in blog_dict.values():
        cluster = Cluster(blog=blog)
        cluster_list.append(cluster)
    return cluster_list


def iterate(cluster_list: list):

    closest = float("inf")
    cluster_a = Cluster()
    cluster_b = Cluster()

    for cluster_a_in_dict in cluster_list:
        for cluster_b_in_dict in cluster_list:
            distance = pearson(cluster_a_in_dict.blog, cluster_b_in_dict.blog)
            if distance < closest and cluster_a_in_dict != cluster_b_in_dict:
                closest = distance
                cluster_a = cluster_a_in_dict
                cluster_b = cluster_b_in_dict

    cluster_c = merge(cluster_a, cluster_b, closest)
    cluster_list.append(cluster_c)
    cluster_list.remove(cluster_a)
    cluster_list.remove(cluster_b)


def merge(cluster_a: Cluster, cluster_b: Cluster, distance: float):
    n = len(cluster_a.blog.words)
    cluster_p = Cluster()
    cluster_p.left = cluster_a
    cluster_p.right = cluster_b
    cluster_a.parent = cluster_p
    cluster_b.parent = cluster_p
    blog = Blog()

    for i in range(n):
        count_a = cluster_a.blog.words[i]
        count_b = cluster_b.blog.words[i]
        count = count_a + count_b
        if len(blog.words) < 706:
            blog.words.append(count)
        else:
            blog.words[i] = count
    cluster_p.blog = blog
    cluster_p.distance = distance
    return cluster_p
