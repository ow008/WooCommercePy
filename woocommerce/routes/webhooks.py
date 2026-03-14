class Webhooks:

    def __init__(self, client):
        self.client = client

    def list(self, **params):
        response = self.client.get('webhooks', params=params).json()
        return response

    def get(self, webhook_id):
        response = self.client.get(f'webhooks/{webhook_id}').json()
        return response

    def create(self, data):
        response = self.client.post('webhooks', data=data).json()
        return response

    def update(self, webhook_id, data):
        response = self.client.put(f'webhooks/{webhook_id}', data=data).json()
        return response

    def delete(self, webhook_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'webhooks/{webhook_id}', params=params).json()
        return response

    def batch(self, data):
        response = self.client.post('webhooks/batch', data=data).json()
        return response
