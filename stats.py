from models.blog import Blog
from math import sqrt


def pearson(a,c):
    sum_a = 0
    sum_b = 0
    sum_a_sq = 0
    sum_b_sq = 0
    p_sum = 0
    n = len(c)

    for i in range(n):
        count_a = a.words[i]
        count_b = c[i]
        sum_a += count_a
        sum_b += count_b
        sum_a_sq += count_a**2
        sum_b_sq += count_b**2
        p_sum += count_a * count_b
    num = p_sum - (sum_a * sum_b / n)
    den = sqrt((sum_a_sq - sum_a**2 / n) * (sum_b_sq - sum_b**2 / n))
    return 1.0 - (num/den)
