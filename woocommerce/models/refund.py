class Refund:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.date_created = kwargs.get('date_created')
        self.date_created_gmt = kwargs.get('date_created_gmt')
        self.amount = kwargs.get('amount')
        self.reason = kwargs.get('reason', '')
        self.refunded_by = kwargs.get('refunded_by')
        self.refunded_payment = kwargs.get('refunded_payment', False)
        self.meta_data = kwargs.get('meta_data', [])
        self.line_items = kwargs.get('line_items', [])
        self.api_refund = kwargs.get('api_refund', True)

    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if value is not None and value != '' and value != []:
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"Refund(id={self.id}, amount='{self.amount}', reason='{self.reason}')"
