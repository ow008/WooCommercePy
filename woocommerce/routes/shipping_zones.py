class ShippingZones:

    def __init__(self, client):
        self.client = client

    def list(self):
        response = self.client.get('shipping/zones').json()
        return response

    def get(self, zone_id):
        response = self.client.get(f'shipping/zones/{zone_id}').json()
        return response

    def create(self, data):
        response = self.client.post('shipping/zones', data=data).json()
        return response

    def update(self, zone_id, data):
        response = self.client.put(f'shipping/zones/{zone_id}', data=data).json()
        return response

    def delete(self, zone_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'shipping/zones/{zone_id}', params=params).json()
        return response


class ShippingZoneLocations:

    def __init__(self, client):
        self.client = client

    def list(self, zone_id):
        response = self.client.get(f'shipping/zones/{zone_id}/locations').json()
        return response

    def update(self, zone_id, data):
        response = self.client.put(f'shipping/zones/{zone_id}/locations', data=data).json()
        return response


class ShippingZoneMethods:

    def __init__(self, client):
        self.client = client

    def list(self, zone_id):
        response = self.client.get(f'shipping/zones/{zone_id}/methods').json()
        return response

    def get(self, zone_id, method_id):
        response = self.client.get(f'shipping/zones/{zone_id}/methods/{method_id}').json()
        return response

    def create(self, zone_id, data):
        response = self.client.post(f'shipping/zones/{zone_id}/methods', data=data).json()
        return response

    def update(self, zone_id, method_id, data):
        response = self.client.put(f'shipping/zones/{zone_id}/methods/{method_id}', data=data).json()
        return response

    def delete(self, zone_id, method_id, force=False):
        params = {'force': force}
        response = self.client.delete(f'shipping/zones/{zone_id}/methods/{method_id}', params=params).json()
        return response
