from requests.auth import HTTPBasicAuth
import requests
import json
from urllib.parse import urlencode


class WooCommerceAPI:
    def __init__(self, url, consumer_key, consumer_secret, version="wc/v3", timeout=30, verify_ssl=True, query_string_auth=False):
        self.url = url.rstrip("/")
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.version = version
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.is_ssl = url.startswith("https")
        self.query_string_auth = query_string_auth

        self._init_routes()

    def _init_routes(self):
        from .routes.products import Products
        from .routes.product_variations import ProductVariations
        from .routes.product_attributes import ProductAttributes, ProductAttributeTerms
        from .routes.product_categories import ProductCategories
        from .routes.product_tags import ProductTags
        from .routes.product_reviews import ProductReviews
        from .routes.orders import Orders
        from .routes.customers import Customers
        from .routes.coupons import Coupons
        from .routes.refunds import Refunds
        from .routes.payment_gateways import PaymentGateways
        from .routes.shipping_zones import ShippingZones, ShippingZoneLocations, ShippingZoneMethods
        from .routes.tax_rates import TaxRates
        from .routes.webhooks import Webhooks

        self.products = Products(self)
        self.product_variations = ProductVariations(self)
        self.product_attributes = ProductAttributes(self)
        self.product_attribute_terms = ProductAttributeTerms(self)
        self.product_categories = ProductCategories(self)
        self.product_tags = ProductTags(self)
        self.product_reviews = ProductReviews(self)
        self.orders = Orders(self)
        self.customers = Customers(self)
        self.coupons = Coupons(self)
        self.refunds = Refunds(self)
        self.payment_gateways = PaymentGateways(self)
        self.shipping_zones = ShippingZones(self)
        self.shipping_zone_locations = ShippingZoneLocations(self)
        self.shipping_zone_methods = ShippingZoneMethods(self)
        self.tax_rates = TaxRates(self)
        self.webhooks = Webhooks(self)

    def _build_url(self, endpoint):
        return f"{self.url}/wp-json/{self.version}/{endpoint.lstrip('/')}"

    def _get_oauth_url(self, url, method):
        from .oauth import OAuth
        oauth = OAuth(
            url=url,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            version=self.version,
            method=method
        )
        return oauth.get_oauth_url()

    def _request(self, method, endpoint, data=None, **kwargs):
        url = self._build_url(endpoint)
        params = kwargs.pop('params', {})
        headers = {
            "user-agent": "WooCommerce-Python-REST-API/3.0.0",
            "accept": "application/json"
        }

        auth = None

        if self.is_ssl and not self.query_string_auth:
            auth = HTTPBasicAuth(self.consumer_key, self.consumer_secret)
        elif self.is_ssl and self.query_string_auth:
            params.update({
                "consumer_key": self.consumer_key,
                "consumer_secret": self.consumer_secret
            })
        else:
            encoded_params = urlencode(params)
            url = f"{url}?{encoded_params}" if encoded_params else url
            url = self._get_oauth_url(url, method)
            params = {}

        request_data = None
        if data is not None:
            request_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
            headers["content-type"] = "application/json;charset=utf-8"

        kwargs.setdefault("timeout", self.timeout)
        kwargs.setdefault("verify", self.verify_ssl)

        return requests.request(
            method=method,
            url=url,
            params=params,
            data=request_data,
            auth=auth,
            headers=headers,
            **kwargs
        )

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        return self._request("POST", endpoint, data, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self._request("PUT", endpoint, data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
