from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.article_model = ArticleModel()  # связывается model
        self.user_interface = UserInterface()  # с view

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            article = self.user_interface.add_user_article()
            self.article_model.add_article(article)
        if answer == "2":
            article = self.article_model.get_all_articles()
            self.user_interface.show_all_articles(article)

