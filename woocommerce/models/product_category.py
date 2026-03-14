class ProductCategory:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.slug = kwargs.get('slug')
        self.parent = kwargs.get('parent', 0)
        self.description = kwargs.get('description', '')
        self.display = kwargs.get('display', 'default')
        self.image = kwargs.get('image')
        self.menu_order = kwargs.get('menu_order', 0)
        self.count = kwargs.get('count', 0)

    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if value is not None and value != '' and value != 0:
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"ProductCategory(id={self.id}, name='{self.name}')"
