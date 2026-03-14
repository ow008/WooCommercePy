from ..models.product_review import ProductReview


class ProductReviews:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('products/reviews', params=params).json()
        return [ProductReview.from_dict(item) for item in response]

    def get(self, review_id):
        response = self.client.get(f'products/reviews/{review_id}').json()
        return ProductReview.from_dict(response)

    def create(self, review):
        if isinstance(review, ProductReview):
            data = review.to_dict()
        else:
            data = review
        response = self.client.post('products/reviews', data=data).json()
        return ProductReview.from_dict(response)

    def update(self, review_id, review):
        if isinstance(review, ProductReview):
            data = review.to_dict()
        else:
            data = review
        response = self.client.put(f'products/reviews/{review_id}', data=data).json()
        return ProductReview.from_dict(response)

    def delete(self, review_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'products/reviews/{review_id}', params=params).json()
        return ProductReview.from_dict(response)

    def batch(self, data):
        response = self.client.post('products/reviews/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [ProductReview.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [ProductReview.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [ProductReview.from_dict(item) for item in response['delete']]
        return result
