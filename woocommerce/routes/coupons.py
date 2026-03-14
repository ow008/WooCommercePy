from ..models.coupon import Coupon


class Coupons:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('coupons', params=params).json()
        return [Coupon.from_dict(item) for item in response]

    def get(self, coupon_id):
        response = self.client.get(f'coupons/{coupon_id}').json()
        return Coupon.from_dict(response)

    def create(self, coupon):
        if isinstance(coupon, Coupon):
            data = coupon.to_dict()
        else:
            data = coupon
        response = self.client.post('coupons', data=data).json()
        return Coupon.from_dict(response)

    def update(self, coupon_id, coupon):
        if isinstance(coupon, Coupon):
            data = coupon.to_dict()
        else:
            data = coupon
        response = self.client.put(f'coupons/{coupon_id}', data=data).json()
        return Coupon.from_dict(response)

    def delete(self, coupon_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'coupons/{coupon_id}', params=params).json()
        return Coupon.from_dict(response)

    def batch(self, data):
        response = self.client.post('coupons/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [Coupon.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [Coupon.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [Coupon.from_dict(item) for item in response['delete']]
        return result
