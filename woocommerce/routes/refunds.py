from ..models.refund import Refund


class Refunds:

    def __init__(self, client):
        self.client = client

    def list(self, order_id, **params):
        response = self.client.get(f'orders/{order_id}/refunds', params=params).json()
        return [Refund.from_dict(item) for item in response]

    def get(self, order_id, refund_id):
        response = self.client.get(f'orders/{order_id}/refunds/{refund_id}').json()
        return Refund.from_dict(response)

    def create(self, order_id, refund):
        if isinstance(refund, Refund):
            data = refund.to_dict()
        else:
            data = refund
        response = self.client.post(f'orders/{order_id}/refunds', data=data).json()
        return Refund.from_dict(response)

    def delete(self, order_id, refund_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'orders/{order_id}/refunds/{refund_id}', params=params).json()
        return Refund.from_dict(response)
