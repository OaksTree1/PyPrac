import uuid
from Models.Post import Post
import datetime
from Database.database import dataBase

class blog(object):
    def __init__(self, author, title, description, id = None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = raw_input("enter Post title")
        content = raw_input("enter post content")
        date = raw_input("Enter Post Date (in format DDMMYYYY)")
        if date == "" or " ":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id = self.id, author = self.author, title = title, content = content, date= date)
        post.SaveMongo()

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        dataBase.insert(collection='Blogs', data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def From_mongo(cls, id):
        blog_data = dataBase.find_one(collection='Blogs', query={'id':id})
        return cls(author=blog_data['author'], title=blog_data['title'], description=blog_data['description'], id=blog_data['id'])