
class Post:
    def __init__(self, id, author, title, description, url, urlToImage, content, publishedAt=None) -> None:
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
