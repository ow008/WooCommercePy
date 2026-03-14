class Customer:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.date_created = kwargs.get('date_created')
        self.date_created_gmt = kwargs.get('date_created_gmt')
        self.date_modified = kwargs.get('date_modified')
        self.date_modified_gmt = kwargs.get('date_modified_gmt')
        self.email = kwargs.get('email')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.role = kwargs.get('role')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.billing = kwargs.get('billing', {})
        self.shipping = kwargs.get('shipping', {})
        self.is_paying_customer = kwargs.get('is_paying_customer', False)
        self.avatar_url = kwargs.get('avatar_url')
        self.meta_data = kwargs.get('meta_data', [])

    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if value is not None and value != '' and value != [] and value != {}:
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"Customer(id={self.id}, email='{self.email}', name='{self.first_name} {self.last_name}')"
