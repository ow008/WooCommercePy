class ProductAttribute:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.slug = kwargs.get('slug')
        self.type = kwargs.get('type', 'select')
        self.order_by = kwargs.get('order_by', 'menu_order')
        self.has_archives = kwargs.get('has_archives', False)

    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if value is not None and value != '':
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"ProductAttribute(id={self.id}, name='{self.name}')"
