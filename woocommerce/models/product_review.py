class ProductReview:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.date_created = kwargs.get('date_created')
        self.date_created_gmt = kwargs.get('date_created_gmt')
        self.product_id = kwargs.get('product_id')
        self.product_name = kwargs.get('product_name')
        self.product_permalink = kwargs.get('product_permalink')
        self.status = kwargs.get('status', 'approved')
        self.reviewer = kwargs.get('reviewer')
        self.reviewer_email = kwargs.get('reviewer_email')
        self.review = kwargs.get('review', '')
        self.rating = kwargs.get('rating', 0)
        self.verified = kwargs.get('verified', False)
        self.reviewer_avatar_urls = kwargs.get('reviewer_avatar_urls', {})

    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if value is not None and value != '' and value != {} and value != 0:
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"ProductReview(id={self.id}, product_id={self.product_id}, rating={self.rating})"
