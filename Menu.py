from Database.database import dataBase
from Models.Blog import blog

class Menu(object):
    def __init__(self):
        self.user = raw_input("Enter your username: ")
        self.user_have_blog = None
        if self._user_account():
            print("Welcome Back {user}".format(user = self.user))
        else:
            self._register_user()
    def run_menu(self):
        read_or_write = raw_input("Do you want to read (R) or write(W):")
        if(read_or_write == "R"):
            self._list_blogs()
            self._view_blogs()
        elif(read_or_write == "W"):
            self.user_have_blog.new_post()
        else:
            print("Thank you for Trying")

    def _user_account(self):
        blogsearch = dataBase.find_one(collection='Blogs',query= {'author': self.user})
        if blogsearch is not None:
            self.user_have_blog = blog.From_mongo(blogsearch['id'])
            return True
        else:
            return False
    def _register_user(self):
        title = raw_input("enter Post title")
        description = raw_input("enter post description")
        blog_write = blog(author=self.user, title = title, description = description)
        blog_write.save_to_mongo()
        self.user_have_blog = blog_write

    def _list_blogs(self):
        AllBlogs = dataBase.find(collection='Blogs', query={})
        for dablog in AllBlogs:
            print("ID: {id}, :Title: {title}, Author: {author}".format(id = dablog['id'], title = dablog['title'], author = dablog['author']))

    def _view_blogs(self):
        blog_to_see = raw_input("What is the ID of the blog you want:")
        blogsee = blog.From_mongo(blog_to_see)
        postsee = blogsee.get_post()

        for dapost in postsee:
            print("Date: {date}, Title: {title}\n\n{content}".format(date = dapost['date_created'], title = dapost['title'], content = dapost['content']))




