


class Category:
    def __init__(self, name:str):

        self.category_id = None
        self.name = name
    
    @classmethod
    def factory(cls, id, name: str):
        old_category = cls(name)
        old_category.category_id = id
        return old_category

