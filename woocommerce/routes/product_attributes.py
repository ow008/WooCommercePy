from ..models.product_attribute import ProductAttribute


class ProductAttributes:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('products/attributes', params=params).json()
        return [ProductAttribute.from_dict(item) for item in response]

    def get(self, attribute_id):
        response = self.client.get(f'products/attributes/{attribute_id}').json()
        return ProductAttribute.from_dict(response)

    def create(self, attribute):
        if isinstance(attribute, ProductAttribute):
            data = attribute.to_dict()
        else:
            data = attribute
        response = self.client.post('products/attributes', data=data).json()
        return ProductAttribute.from_dict(response)

    def update(self, attribute_id, attribute):
        if isinstance(attribute, ProductAttribute):
            data = attribute.to_dict()
        else:
            data = attribute
        response = self.client.put(f'products/attributes/{attribute_id}', data=data).json()
        return ProductAttribute.from_dict(response)

    def delete(self, attribute_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'products/attributes/{attribute_id}', params=params).json()
        return ProductAttribute.from_dict(response)

    def batch(self, data):
        response = self.client.post('products/attributes/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [ProductAttribute.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [ProductAttribute.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [ProductAttribute.from_dict(item) for item in response['delete']]
        return result


class ProductAttributeTerms:

    def __init__(self, client):
        self.client = client

    def list(self, attribute_id, **params):
        response = self.client.get(f'products/attributes/{attribute_id}/terms', params=params).json()
        return response

    def get(self, attribute_id, term_id):
        response = self.client.get(f'products/attributes/{attribute_id}/terms/{term_id}').json()
        return response

    def create(self, attribute_id, data):
        response = self.client.post(f'products/attributes/{attribute_id}/terms', data=data).json()
        return response

    def update(self, attribute_id, term_id, data):
        response = self.client.put(f'products/attributes/{attribute_id}/terms/{term_id}', data=data).json()
        return response

    def delete(self, attribute_id, term_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'products/attributes/{attribute_id}/terms/{term_id}', params=params).json()
        return response

    def batch(self, attribute_id, data):
        response = self.client.post(f'products/attributes/{attribute_id}/terms/batch', data=data).json()
        return response
