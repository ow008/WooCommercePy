from ..client import WooCommerceAPI
from ..models.product import Product


class Products:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('products', params=params).json()
        return [Product.from_dict(item) for item in response]

    def get(self, product_id):
        response = self.client.get(f'products/{product_id}').json()
        return Product.from_dict(response)

    def create(self, product):
        if isinstance(product, Product):
            data = product.to_dict()
        else:
            data = product
        response = self.client.post('products', data=data).json()
        return Product.from_dict(response)

    def update(self, product_id, product):
        if isinstance(product, Product):
            data = product.to_dict()
        else:
            data = product
        response = self.client.put(f'products/{product_id}', data=data).json()
        return Product.from_dict(response)

    def delete(self, product_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'products/{product_id}', params=params).json()
        return Product.from_dict(response)

    def batch(self, data):
        response = self.client.post('products/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [Product.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [Product.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [Product.from_dict(item) for item in response['delete']]
        return result

    def duplicate(self, product_id, data=None):
        response = self.client.post(f'products/{product_id}/duplicate', data=data).json()
        return Product.from_dict(response)
