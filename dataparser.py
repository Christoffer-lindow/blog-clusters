from models.blog import Blog
def get_id_for_word(dict, word):
    if word not in dict:
        id = len(dict)
        dict[word] = id
        return id


def set_dict_words(dict,line):
    [get_id_for_word(dict,word) for word in line.split("\t")[1:]]

def add_blog_to_dict(list: list,line):
            blog = line.split("\t")
            blog_title = blog[0]
            blog_counts = [int(word_count) for word_count in blog[1:]]
            list.append(Blog(blog_title,blog_counts))

def parse_data(url):
    with open(url, "r") as reader:
        word_dict = dict()
        blog_list  = list()
        count = 0
        for line in reader:
            if count == 0:
                set_dict_words(word_dict,line)
            else:
                add_blog_to_dict(blog_list,line)
            count += 1
    return {"words": word_dict, "blogs":blog_list}