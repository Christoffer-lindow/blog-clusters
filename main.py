from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from time import time
from kmeans import k_means
from dataparser import parse_data
from responses import centroid_response
url = "./data/blogdata.txt"
data = parse_data(url)
blogs = data["blogs"]

app = FastAPI()
origins = ["http://localhost:3000", "https://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/k-means/{k}/{n}")
def get_k_means(k: int, n: int):
    start = time()
    centroids = k_means(blogs, k, n)

    response = centroid_response(centroids)

    end = time()
    run_time = end-start

    return {"centroids": response, "runtime": run_time}
