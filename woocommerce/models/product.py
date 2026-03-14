class Product:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.slug = kwargs.get('slug')
        self.permalink = kwargs.get('permalink')
        self.date_created = kwargs.get('date_created')
        self.date_created_gmt = kwargs.get('date_created_gmt')
        self.date_modified = kwargs.get('date_modified')
        self.date_modified_gmt = kwargs.get('date_modified_gmt')
        self.type = kwargs.get('type', 'simple')
        self.status = kwargs.get('status', 'publish')
        self.featured = kwargs.get('featured', False)
        self.catalog_visibility = kwargs.get('catalog_visibility', 'visible')
        self.description = kwargs.get('description', '')
        self.short_description = kwargs.get('short_description', '')
        self.sku = kwargs.get('sku', '')
        self.price = kwargs.get('price')
        self.regular_price = kwargs.get('regular_price', '')
        self.sale_price = kwargs.get('sale_price', '')
        self.date_on_sale_from = kwargs.get('date_on_sale_from')
        self.date_on_sale_from_gmt = kwargs.get('date_on_sale_from_gmt')
        self.date_on_sale_to = kwargs.get('date_on_sale_to')
        self.date_on_sale_to_gmt = kwargs.get('date_on_sale_to_gmt')
        self.on_sale = kwargs.get('on_sale', False)
        self.purchasable = kwargs.get('purchasable', True)
        self.total_sales = kwargs.get('total_sales', 0)
        self.virtual = kwargs.get('virtual', False)
        self.downloadable = kwargs.get('downloadable', False)
        self.downloads = kwargs.get('downloads', [])
        self.download_limit = kwargs.get('download_limit', -1)
        self.download_expiry = kwargs.get('download_expiry', -1)
        self.external_url = kwargs.get('external_url', '')
        self.button_text = kwargs.get('button_text', '')
        self.tax_status = kwargs.get('tax_status', 'taxable')
        self.tax_class = kwargs.get('tax_class', '')
        self.manage_stock = kwargs.get('manage_stock', False)
        self.stock_quantity = kwargs.get('stock_quantity')
        self.backorders = kwargs.get('backorders', 'no')
        self.backorders_allowed = kwargs.get('backorders_allowed', False)
        self.backordered = kwargs.get('backordered', False)
        self.low_stock_amount = kwargs.get('low_stock_amount')
        self.sold_individually = kwargs.get('sold_individually', False)
        self.weight = kwargs.get('weight', '')
        self.dimensions = kwargs.get('dimensions', {})
        self.shipping_required = kwargs.get('shipping_required', True)
        self.shipping_taxable = kwargs.get('shipping_taxable', True)
        self.shipping_class = kwargs.get('shipping_class', '')
        self.shipping_class_id = kwargs.get('shipping_class_id', 0)
        self.reviews_allowed = kwargs.get('reviews_allowed', True)
        self.average_rating = kwargs.get('average_rating', '0')
        self.rating_count = kwargs.get('rating_count', 0)
        self.upsell_ids = kwargs.get('upsell_ids', [])
        self.cross_sell_ids = kwargs.get('cross_sell_ids', [])
        self.parent_id = kwargs.get('parent_id', 0)
        self.purchase_note = kwargs.get('purchase_note', '')
        self.categories = kwargs.get('categories', [])
        self.tags = kwargs.get('tags', [])
        self.images = kwargs.get('images', [])
        self.attributes = kwargs.get('attributes', [])
        self.default_attributes = kwargs.get('default_attributes', [])
        self.variations = kwargs.get('variations', [])
        self.grouped_products = kwargs.get('grouped_products', [])
        self.menu_order = kwargs.get('menu_order', 0)
        self.price_html = kwargs.get('price_html', '')
        self.related_ids = kwargs.get('related_ids', [])
        self.meta_data = kwargs.get('meta_data', [])
        self.stock_status = kwargs.get('stock_status', 'instock')
        self.has_options = kwargs.get('has_options', False)

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
        return f"Product(id={self.id}, name='{self.name}', sku='{self.sku}')"
