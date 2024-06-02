class Article:
    def __init__(self, title, author, page, description):
        self.title = title
        self.author = author
        self.page = page
        self.description = description

    def __str__(self):
        return f"{self.title} ({self.author})"


class ArticleModel:
    def __init__(self):
        self.articles = {}

    # def __repr__(self):
    #     return f"{self.articles}" # просмотр сохр. данных str -> repr

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article
        # print(self.articles)

    def get_all_articles(self):
        return self.articles.values()

