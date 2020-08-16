import os

def get_all_post_names():
    try:
        post_files = os.listdir('templates/posts')
        post_names = list(map(lambda x: x.split('.')[0], post_files))
        return post_names
    except:
        print('An error occurred while fetching posts')
        return []