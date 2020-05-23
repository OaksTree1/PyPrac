from Models.Post import Post
from Models.Blog import blog
from Database.database import dataBase
from Models.Menu import Menu

import pymongo

dataBase.initialize()

call_menu = Menu()

call_menu.run_menu()

#post = Post(blog_id="2728", title="A man Post", content="Man made this", author="Perko")

# writeposts = Post.from_blog("2728")

# for writepost in writeposts:
 #   print(writepost)

# blog_write = blog(author="Oak", title="A man who sees", description="he sees things")

# blog_write.new_post()

# blog_write.save_to_mongo()

# from_db = blog.From_mongo(blog_write.id)

# print(blog_write.get_post())


# print(post.author)

# uri = "123"

# client = pymongo.MongoClient(uri)
# database = client['admin']
# collection = database['cities']

# cities = [cities["Name"] for cities in collection.find({}) if cities["Name"] != "Baltimore"]

# print cities