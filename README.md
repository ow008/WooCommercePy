# WooPY - WooCommerce Python API Wrapper

A modern, type-friendly Python wrapper for the WooCommerce REST API with intuitive model classes and dedicated methods for all resources.

## About

This library was created to address the limitations of the [official WooCommerce Python SDK](https://github.com/woocommerce/wc-api-python). While the official SDK provides basic `get()`, `post()`, `put()`, and `delete()` methods, mine goes further by offering:

- **Dedicated methods** like `create_product()`, `update_order()`, `list_customers()` instead of generic HTTP methods
- **Model classes** for type safety and IDE autocomplete (e.g., `Product`, `Order`, `Customer`)
- **Intuitive API** that matches the WooCommerce REST API structure
- **Full CRUD operations** for all major WooCommerce resources

The OAuth 1.0a implementation is based on the official [wc-api-python](https://github.com/woocommerce/wc-api-python) library, ensuring compatibility with WooCommerce's authentication requirements.

## Features

- ✨ Clean, intuitive interface
- 🎯 Model classes for all major WooCommerce entities
- 🔄 Support for all CRUD operations
- 📦 Batch operations support
- 🔐 OAuth 1.0a authentication
- 🚀 Easy to use and extend

## Installation

```bash
pip install -r requirements.txt
```

## Authentication

WooPY supports three authentication methods:

### 1. HTTPS with Basic Auth (Recommended)

For HTTPS sites, use HTTP Basic Authentication:

```python
api = WooCommerceAPI(
    url='https://yourstore.com',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    verify_ssl=True  # Set to False for self-signed certificates
)
```

### 2. HTTPS with Query String Auth

For HTTPS sites where Basic Auth doesn't work:

```python
api = WooCommerceAPI(
    url='https://yourstore.com',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    query_string_auth=True
)
```

### 3. HTTP with OAuth 1.0a

For HTTP (non-HTTPS) sites, OAuth 1.0a is automatically used:

```python
api = WooCommerceAPI(
    url='http://yourstore.com',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
)
```

## Quick Start

```python
from woocommerce import WooCommerceAPI, Product, Order

# Initialize API client (HTTPS with Basic Auth - Recommended)
api = WooCommerceAPI(
    url='https://yourstore.com',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    version='wc/v3',
    timeout=30,
    verify_ssl=True
)

# Create a product using model class
product = Product(
    name="Cool T-Shirt",
    type="simple",
    regular_price="29.99",
    sku="TSHIRT-001",
    description="An awesome t-shirt"
)
created_product = api.products.create(product)

# Or use a dictionary
created_product = api.products.create({
    "name": "Another Product",
    "regular_price": "19.99"
})

# List products
products = api.products.list(per_page=10, status="publish")
for product in products:
    print(f"{product.name} - ${product.price}")

# Get a single product
product = api.products.get(123)
print(product.name, product.sku)

# Update a product
product.regular_price = "39.99"
updated = api.products.update(product.id, product)

# Delete a product
api.products.delete(123, force=True)
```

## Available Resources

### Products
- `api.products` - Products management
- `api.product_variations` - Product variations
- `api.product_attributes` - Product attributes
- `api.product_attribute_terms` - Attribute terms
- `api.product_categories` - Product categories
- `api.product_tags` - Product tags
- `api.product_reviews` - Product reviews

### Orders & Customers
- `api.orders` - Orders management
- `api.customers` - Customers management
- `api.refunds` - Order refunds

### Marketing
- `api.coupons` - Discount coupons

### Settings & Configuration
- `api.payment_gateways` - Payment gateways
- `api.shipping_zones` - Shipping zones
- `api.shipping_zone_locations` - Zone locations
- `api.shipping_zone_methods` - Zone shipping methods
- `api.tax_rates` - Tax rates
- `api.webhooks` - Webhooks

## Model Classes

All major entities have corresponding model classes:

```python
from woocommerce import (
    Product,
    ProductVariation,
    ProductCategory,
    ProductTag,
    ProductAttribute,
    ProductReview,
    Order,
    Customer,
    Coupon,
    Refund
)
```

## Common Operations

### Working with Products

```python
# Create a product
product = Product(
    name="Laptop",
    regular_price="999.99",
    sale_price="899.99",
    categories=[{"id": 15}],
    images=[{"src": "https://example.com/image.jpg"}]
)
api.products.create(product)

# Batch operations
api.products.batch({
    "create": [
        {"name": "Product 1", "regular_price": "10.00"},
        {"name": "Product 2", "regular_price": "20.00"}
    ],
    "update": [
        {"id": 123, "regular_price": "15.00"}
    ],
    "delete": [456]
})
```

### Working with Orders

```python
# Create an order
order = Order(
    payment_method="bacs",
    payment_method_title="Direct Bank Transfer",
    set_paid=True,
    billing={
        "first_name": "John",
        "last_name": "Doe",
        "address_1": "123 Main St",
        "city": "New York",
        "postcode": "10001",
        "country": "US",
        "email": "john@example.com",
        "phone": "555-1234"
    },
    line_items=[
        {
            "product_id": 93,
            "quantity": 2
        }
    ]
)
created_order = api.orders.create(order)

# List orders
orders = api.orders.list(status="processing", per_page=20)

# Update order status
api.orders.update(order_id, {"status": "completed"})
```

### Working with Customers

```python
# Create a customer
customer = Customer(
    email="customer@example.com",
    first_name="Jane",
    last_name="Smith",
    username="janesmith",
    billing={
        "first_name": "Jane",
        "last_name": "Smith",
        "company": "",
        "address_1": "123 Main St",
        "city": "New York",
        "postcode": "10001",
        "country": "US",
        "email": "customer@example.com",
        "phone": "555-5678"
    }
)
api.customers.create(customer)

# List customers
customers = api.customers.list(role="customer")
```

### Working with Coupons

```python
# Create a coupon
coupon = Coupon(
    code="SUMMER2024",
    discount_type="percent",
    amount="20",
    individual_use=True,
    product_ids=[123, 456],
    usage_limit=100,
    free_shipping=False
)
api.coupons.create(coupon)

# Get coupon by ID
coupon = api.coupons.get(789)
```

### Product Variations

```python
# List variations for a product
variations = api.product_variations.list(product_id=123)

# Create a variation
variation = api.product_variations.create(
    product_id=123,
    variation={
        "regular_price": "29.99",
        "attributes": [
            {
                "id": 1,
                "option": "Large"
            }
        ]
    }
)

# Generate all possible variations
api.product_variations.generate(product_id=123)
```

### Refunds

```python
# Create a refund
refund = api.refunds.create(
    order_id=456,
    refund={
        "amount": "10.00",
        "reason": "Defective product",
        "api_refund": True
    }
)

# List refunds for an order
refunds = api.refunds.list(order_id=456)
```

### Webhooks

```python
# Create a webhook
webhook = api.webhooks.create({
    "name": "Order Created",
    "topic": "order.created",
    "delivery_url": "https://yoursite.com/webhooks/order-created"
})

# List webhooks
webhooks = api.webhooks.list()
```

## Batch Operations

Batch operations allow you to create, update, and delete multiple items in a single request:

```python
batch_data = {
    "create": [
        {"name": "Product 1", "regular_price": "10.00"},
        {"name": "Product 2", "regular_price": "20.00"}
    ],
    "update": [
        {"id": 123, "regular_price": "15.00"},
        {"id": 456, "name": "Updated Name"}
    ],
    "delete": [789, 101]
}

result = api.products.batch(batch_data)
print(result['create'])  # List of created products
print(result['update'])  # List of updated products
print(result['delete'])  # List of deleted products
```

## Query Parameters

All list methods support WooCommerce query parameters:

```python
# Pagination
products = api.products.list(page=2, per_page=50)

# Filtering
orders = api.orders.list(
    status="completed",
    after="2024-01-01T00:00:00",
    before="2024-12-31T23:59:59"
)

# Searching
customers = api.customers.list(search="john@example.com")

# Ordering
products = api.products.list(orderby="date", order="desc")
```

## Error Handling

```python
try:
    product = api.products.get(99999)
except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")
    print(f"Response: {e.response.json()}")
```

## Requirements

- Python 3.7+
- requests

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

Built with ❤️ for the WooCommerce community.
(Yes AI wrote the README)
