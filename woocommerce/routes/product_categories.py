from ..models.product_category import ProductCategory


class ProductCategories:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('products/categories', params=params).json()
        return [ProductCategory.from_dict(item) for item in response]

    def get(self, category_id):
        response = self.client.get(f'products/categories/{category_id}').json()
        return ProductCategory.from_dict(response)

    def create(self, category):
        if isinstance(category, ProductCategory):
            data = category.to_dict()
        else:
            data = category
        response = self.client.post('products/categories', data=data).json()
        return ProductCategory.from_dict(response)

    def update(self, category_id, category):
        if isinstance(category, ProductCategory):
            data = category.to_dict()
        else:
            data = category
        response = self.client.put(f'products/categories/{category_id}', data=data).json()
        return ProductCategory.from_dict(response)

    def delete(self, category_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'products/categories/{category_id}', params=params).json()
        return ProductCategory.from_dict(response)

    def batch(self, data):
        response = self.client.post('products/categories/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [ProductCategory.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [ProductCategory.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [ProductCategory.from_dict(item) for item in response['delete']]
        return result
