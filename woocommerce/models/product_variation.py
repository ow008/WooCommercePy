class ProductVariation:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.date_created = kwargs.get('date_created')
        self.date_created_gmt = kwargs.get('date_created_gmt')
        self.date_modified = kwargs.get('date_modified')
        self.date_modified_gmt = kwargs.get('date_modified_gmt')
        self.description = kwargs.get('description', '')
        self.permalink = kwargs.get('permalink')
        self.sku = kwargs.get('sku', '')
        self.price = kwargs.get('price')
        self.regular_price = kwargs.get('regular_price', '')
        self.sale_price = kwargs.get('sale_price', '')
        self.date_on_sale_from = kwargs.get('date_on_sale_from')
        self.date_on_sale_from_gmt = kwargs.get('date_on_sale_from_gmt')
        self.date_on_sale_to = kwargs.get('date_on_sale_to')
        self.date_on_sale_to_gmt = kwargs.get('date_on_sale_to_gmt')
        self.on_sale = kwargs.get('on_sale', False)
        self.status = kwargs.get('status', 'publish')
        self.purchasable = kwargs.get('purchasable', True)
        self.virtual = kwargs.get('virtual', False)
        self.downloadable = kwargs.get('downloadable', False)
        self.downloads = kwargs.get('downloads', [])
        self.download_limit = kwargs.get('download_limit', -1)
        self.download_expiry = kwargs.get('download_expiry', -1)
        self.tax_status = kwargs.get('tax_status', 'taxable')
        self.tax_class = kwargs.get('tax_class', '')
        self.manage_stock = kwargs.get('manage_stock', False)
        self.stock_quantity = kwargs.get('stock_quantity')
        self.stock_status = kwargs.get('stock_status', 'instock')
        self.backorders = kwargs.get('backorders', 'no')
        self.backorders_allowed = kwargs.get('backorders_allowed', False)
        self.backordered = kwargs.get('backordered', False)
        self.low_stock_amount = kwargs.get('low_stock_amount')
        self.weight = kwargs.get('weight', '')
        self.dimensions = kwargs.get('dimensions', {})
        self.shipping_class = kwargs.get('shipping_class', '')
        self.shipping_class_id = kwargs.get('shipping_class_id', 0)
        self.image = kwargs.get('image', {})
        self.attributes = kwargs.get('attributes', [])
        self.menu_order = kwargs.get('menu_order', 0)
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
        return f"ProductVariation(id={self.id}, sku='{self.sku}')"
