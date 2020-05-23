from Database.database import dataBase
import uuid
import datetime

class Post(object):
    def __init__(self, blog_id, title, content, author, id = None, date = datetime.datetime.utcnow()):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id =  uuid.uuid4().hex if id is None else id
        self.date = date

    def SaveMongo(self):
        dataBase.insert(collection='Posts', data=self.Json())

    def Json(self):
        return{
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title': self.title,
            'date_created':self.date
        }

    @classmethod
    def From_mongo(cls, Id):
        post_data =  dataBase.find_one(collection='Posts', query= {'id' : Id})
        return cls(blog_id = post_data['blog_id'], title = post_data['title'], content = post_data['content'],
                   author = post_data['author'], id = post_data['id'], date = post_data['date'])


    @staticmethod
    def from_blog(Id):
        return [post for post in dataBase.find(collection='Posts',query= {'blog_id': Id})]

