from ._abstract import AbstractScraper


class CdKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "cdkitchen.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def joined_instructions(self):
        return self.schema.joined_instructions()

    def image(self):
        return self.schema.image()
