class Order:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.parent_id = kwargs.get('parent_id', 0)
        self.number = kwargs.get('number')
        self.order_key = kwargs.get('order_key')
        self.created_via = kwargs.get('created_via')
        self.version = kwargs.get('version')
        self.status = kwargs.get('status', 'pending')
        self.currency = kwargs.get('currency')
        self.date_created = kwargs.get('date_created')
        self.date_created_gmt = kwargs.get('date_created_gmt')
        self.date_modified = kwargs.get('date_modified')
        self.date_modified_gmt = kwargs.get('date_modified_gmt')
        self.discount_total = kwargs.get('discount_total', '0')
        self.discount_tax = kwargs.get('discount_tax', '0')
        self.shipping_total = kwargs.get('shipping_total', '0')
        self.shipping_tax = kwargs.get('shipping_tax', '0')
        self.cart_tax = kwargs.get('cart_tax', '0')
        self.total = kwargs.get('total')
        self.total_tax = kwargs.get('total_tax', '0')
        self.prices_include_tax = kwargs.get('prices_include_tax', False)
        self.customer_id = kwargs.get('customer_id', 0)
        self.customer_ip_address = kwargs.get('customer_ip_address', '')
        self.customer_user_agent = kwargs.get('customer_user_agent', '')
        self.customer_note = kwargs.get('customer_note', '')
        self.billing = kwargs.get('billing', {})
        self.shipping = kwargs.get('shipping', {})
        self.payment_method = kwargs.get('payment_method', '')
        self.payment_method_title = kwargs.get('payment_method_title', '')
        self.transaction_id = kwargs.get('transaction_id', '')
        self.date_paid = kwargs.get('date_paid')
        self.date_paid_gmt = kwargs.get('date_paid_gmt')
        self.date_completed = kwargs.get('date_completed')
        self.date_completed_gmt = kwargs.get('date_completed_gmt')
        self.cart_hash = kwargs.get('cart_hash', '')
        self.meta_data = kwargs.get('meta_data', [])
        self.line_items = kwargs.get('line_items', [])
        self.tax_lines = kwargs.get('tax_lines', [])
        self.shipping_lines = kwargs.get('shipping_lines', [])
        self.fee_lines = kwargs.get('fee_lines', [])
        self.coupon_lines = kwargs.get('coupon_lines', [])
        self.refunds = kwargs.get('refunds', [])
        self.set_paid = kwargs.get('set_paid', False)

    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if value is not None and value != '' and value != [] and value != {} and value != 0:
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"Order(id={self.id}, number='{self.number}', status='{self.status}', total='{self.total}')"
