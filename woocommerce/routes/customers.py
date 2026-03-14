from ..models.customer import Customer


class Customers:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('customers', params=params).json()
        return [Customer.from_dict(item) for item in response]

    def get(self, customer_id):
        response = self.client.get(f'customers/{customer_id}').json()
        return Customer.from_dict(response)

    def create(self, customer):
        if isinstance(customer, Customer):
            data = customer.to_dict()
        else:
            data = customer
        response = self.client.post('customers', data=data).json()
        return Customer.from_dict(response)

    def update(self, customer_id, customer):
        if isinstance(customer, Customer):
            data = customer.to_dict()
        else:
            data = customer
        response = self.client.put(f'customers/{customer_id}', data=data).json()
        return Customer.from_dict(response)

    def delete(self, customer_id, force=False, reassign=None):
        params = {'force': force}
        if reassign:
            params['reassign'] = reassign
        response = self.client.delete(f'customers/{customer_id}', params=params).json()
        return Customer.from_dict(response)

    def batch(self, data):
        response = self.client.post('customers/batch', data=data).json()
        result = {}
        if 'create' in response:
            result['create'] = [Customer.from_dict(item) for item in response['create']]
        if 'update' in response:
            result['update'] = [Customer.from_dict(item) for item in response['update']]
        if 'delete' in response:
            result['delete'] = [Customer.from_dict(item) for item in response['delete']]
        return result
