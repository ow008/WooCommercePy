from ..models.product_tag import ProductTag


class ProductTags:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('products/tags', params=params).json()
        return [ProductTag.from_dict(item) for item in response]

    def get(self, tag_id):
        response = self.client.get(f'products/tags/{tag_id}').json()
        return ProductTag.from_dict(response)

    def create(self, tag):
        if isinstance(tag, ProductTag):
            data = tag.to_dict()
        else:
            data = tag
        response = self.client.post('products/tags', data=data).json()
        return ProductTag.from_dict(response)

    def update(self, tag_id, tag):
        if isinstance(tag, ProductTag):
            data = tag.to_dict()
        else:
            data = tag
        response = self.client.put(f'products/tags/{tag_id}', data=data).json()
        return ProductTag.from_dict(response)

    def delete(self, tag_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'products/tags/{tag_id}', params=params).json()
        return ProductTag.from_dict(response)

    def batch(self, data):
        response = self.client.post('products/tags/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [ProductTag.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [ProductTag.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [ProductTag.from_dict(item) for item in response['delete']]
        return result
