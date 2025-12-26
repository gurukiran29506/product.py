def product_details(product_name, product_id, quantity, price):
    result = (
        f"product_name: {product_name}\n"
        f"product_id: {product_id}\n"
        f"quantity: {quantity}\n"
        f"price: {price}"
    )
    return result

if __name__ == "__main__":
    product_name = "Headphones"
    product_id = "E173"
    quantity = 1
    price = 1000
    print(product_details(product_name, product_id, quantity, price))
