from ..models.product_variation import ProductVariation


class ProductVariations:

    def __init__(self, client):
        self.client = client

    def list(self, product_id, **params):
        response = self.client.get(f'products/{product_id}/variations', params=params).json()
        return [ProductVariation.from_dict(item) for item in response]

    def get(self, product_id, variation_id):
        response = self.client.get(f'products/{product_id}/variations/{variation_id}').json()
        return ProductVariation.from_dict(response)

    def create(self, product_id, variation):
        if isinstance(variation, ProductVariation):
            data = variation.to_dict()
        else:
            data = variation
        response = self.client.post(f'products/{product_id}/variations', data=data).json()
        return ProductVariation.from_dict(response)

    def update(self, product_id, variation_id, variation):
        if isinstance(variation, ProductVariation):
            data = variation.to_dict()
        else:
            data = variation
        response = self.client.put(f'products/{product_id}/variations/{variation_id}', data=data).json()
        return ProductVariation.from_dict(response)

    def delete(self, product_id, variation_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'products/{product_id}/variations/{variation_id}', params=params).json()
        return ProductVariation.from_dict(response)

    def batch(self, product_id, data):
        response = self.client.post(f'products/{product_id}/variations/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [ProductVariation.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [ProductVariation.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [ProductVariation.from_dict(item) for item in response['delete']]
        return result

    def generate(self, product_id, data=None):
        response = self.client.post(f'products/{product_id}/variations/generate', data=data).json()
        return [ProductVariation.from_dict(item) for item in response]
