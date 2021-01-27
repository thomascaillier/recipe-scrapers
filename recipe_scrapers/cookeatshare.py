from ._abstract import AbstractScraper


class CookEatShare(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookeatshare.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return 0

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def joined_instructions(self):
        return self.schema.joined_instructions()
