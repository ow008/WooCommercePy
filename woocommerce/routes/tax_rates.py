class TaxRates:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('taxes', params=params).json()
        return response

    def get(self, tax_rate_id):
        response = self.client.get(f'taxes/{tax_rate_id}').json()
        return response

    def create(self, data):
        response = self.client.post('taxes', data=data).json()
        return response

    def update(self, tax_rate_id, data):
        response = self.client.put(f'taxes/{tax_rate_id}', data=data).json()
        return response

    def delete(self, tax_rate_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'taxes/{tax_rate_id}', params=params).json()
        return response

    def batch(self, data):
        response = self.client.post('taxes/batch', data=data).json()
        return response
