from woocommerce import WooCommerceAPI, Product, Order, Customer

# Initialize API client
api = WooCommerceAPI(
    url='https://yourstore.com',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    version='wc/v3'
)

# Example 1: Create a product
print("Creating a product...")
product = Product(
    name="Premium T-Shirt",
    type="simple",
    regular_price="29.99",
    sale_price="24.99",
    sku="TSHIRT-PREMIUM-001",
    description="A premium quality t-shirt",
    short_description="Premium t-shirt",
    categories=[{"id": 9}],
    images=[
        {
            "src": "https://example.com/tshirt.jpg"
        }
    ]
)
created_product = api.products.create(product)
print(f"Created: {created_product.name} (ID: {created_product.id})")

# Example 2: List products
print("\nListing products...")
products = api.products.list(per_page=5, status="publish")
for p in products:
    print(f"- {p.name} - ${p.price} (SKU: {p.sku})")

# Example 3: Update a product
print("\nUpdating product...")
created_product.regular_price = "34.99"
updated_product = api.products.update(created_product.id, created_product)
print(f"Updated price: ${updated_product.regular_price}")

# Example 4: Create a customer
print("\nCreating a customer...")
customer = Customer(
    email="john.doe@example.com",
    first_name="John",
    last_name="Doe",
    username="johndoe",
    billing={
        "first_name": "John",
        "last_name": "Doe",
        "company": "Acme Inc",
        "address_1": "123 Main St",
        "city": "New York",
        "state": "NY",
        "postcode": "10001",
        "country": "US",
        "email": "john.doe@example.com",
        "phone": "555-1234"
    }
)
created_customer = api.customers.create(customer)
print(f"Created: {created_customer.first_name} {created_customer.last_name}")

# Example 5: Create an order
print("\nCreating an order...")
order = Order(
    payment_method="bacs",
    payment_method_title="Direct Bank Transfer",
    set_paid=True,
    billing={
        "first_name": "John",
        "last_name": "Doe",
        "address_1": "123 Main St",
        "city": "New York",
        "state": "NY",
        "postcode": "10001",
        "country": "US",
        "email": "john.doe@example.com",
        "phone": "555-1234"
    },
    shipping={
        "first_name": "John",
        "last_name": "Doe",
        "address_1": "123 Main St",
        "city": "New York",
        "state": "NY",
        "postcode": "10001",
        "country": "US"
    },
    line_items=[
        {
            "product_id": created_product.id,
            "quantity": 2
        }
    ]
)
created_order = api.orders.create(order)
print(f"Created order #{created_order.number} - Total: ${created_order.total}")

# Example 6: List orders
print("\nListing recent orders...")
orders = api.orders.list(per_page=5, orderby="date", order="desc")
for o in orders:
    print(f"- Order #{o.number} - {o.status} - ${o.total}")

# Example 7: Batch operations
print("\nBatch creating products...")
batch_result = api.products.batch({
    "create": [
        {"name": "Batch Product 1", "regular_price": "10.00", "type": "simple"},
        {"name": "Batch Product 2", "regular_price": "20.00", "type": "simple"},
        {"name": "Batch Product 3", "regular_price": "30.00", "type": "simple"}
    ]
})
print(f"Created {len(batch_result['create'])} products in batch")

# Example 8: Get product variations
print("\nGetting product variations...")
variations = api.product_variations.list(product_id=123, per_page=10)
for v in variations:
    print(f"- Variation ID {v.id} - ${v.price}")

print("\nDone!")
