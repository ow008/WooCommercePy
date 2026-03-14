from ..models.order import Order


class Orders:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('orders', params=params).json()
        return [Order.from_dict(item) for item in response]

    def get(self, order_id):
        response = self.client.get(f'orders/{order_id}').json()
        return Order.from_dict(response)

    def create(self, order):
        if isinstance(order, Order):
            data = order.to_dict()
        else:
            data = order
        response = self.client.post('orders', data=data).json()
        return Order.from_dict(response)

    def update(self, order_id, order):
        if isinstance(order, Order):
            data = order.to_dict()
        else:
            data = order
        response = self.client.put(f'orders/{order_id}', data=data).json()
        return Order.from_dict(response)

    def delete(self, order_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'orders/{order_id}', params=params).json()
        return Order.from_dict(response)

    def batch(self, data):
        response = self.client.post('orders/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [Order.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [Order.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [Order.from_dict(item) for item in response['delete']]
        return result
