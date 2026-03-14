class PaymentGateways:

    def __init__(self, client):
        self.client = client

    def list(self):
        response = self.client.get('payment_gateways').json()
        return response

    def get(self, gateway_id):
        response = self.client.get(f'payment_gateways/{gateway_id}').json()
        return response

    def update(self, gateway_id, data):
        response = self.client.put(f'payment_gateways/{gateway_id}', data=data).json()
        return response
