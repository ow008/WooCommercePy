class Coupon:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.code = kwargs.get('code')
        self.amount = kwargs.get('amount', '0')
        self.date_created = kwargs.get('date_created')
        self.date_created_gmt = kwargs.get('date_created_gmt')
        self.date_modified = kwargs.get('date_modified')
        self.date_modified_gmt = kwargs.get('date_modified_gmt')
        self.discount_type = kwargs.get('discount_type', 'fixed_cart')
        self.description = kwargs.get('description', '')
        self.date_expires = kwargs.get('date_expires')
        self.date_expires_gmt = kwargs.get('date_expires_gmt')
        self.usage_count = kwargs.get('usage_count', 0)
        self.individual_use = kwargs.get('individual_use', False)
        self.product_ids = kwargs.get('product_ids', [])
        self.excluded_product_ids = kwargs.get('excluded_product_ids', [])
        self.usage_limit = kwargs.get('usage_limit')
        self.usage_limit_per_user = kwargs.get('usage_limit_per_user')
        self.limit_usage_to_x_items = kwargs.get('limit_usage_to_x_items')
        self.free_shipping = kwargs.get('free_shipping', False)
        self.product_categories = kwargs.get('product_categories', [])
        self.excluded_product_categories = kwargs.get('excluded_product_categories', [])
        self.exclude_sale_items = kwargs.get('exclude_sale_items', False)
        self.minimum_amount = kwargs.get('minimum_amount', '0')
        self.maximum_amount = kwargs.get('maximum_amount', '0')
        self.email_restrictions = kwargs.get('email_restrictions', [])
        self.used_by = kwargs.get('used_by', [])
        self.meta_data = kwargs.get('meta_data', [])

    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if value is not None and value != '' and value != [] and value != 0:
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"Coupon(id={self.id}, code='{self.code}', amount='{self.amount}')"
