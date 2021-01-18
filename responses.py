from models.centroid_view_model import Centroid_View_Model


def centroid_response(centroids):
    centroid_view_model_list = list()

    for centroid in centroids:
        c_view_model = Centroid_View_Model()
        for blog in centroid.blogs:
            c_view_model.blogs.append(blog.title) 
        centroid_view_model_list.append(c_view_model)


    return centroid_view_model_list