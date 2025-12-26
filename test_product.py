from product import product_details

def test_product_details():
    expected_output = (
        "product_name: Headphones\n"
        "product_id: E1273\n"
        "quantity: 1\n"
        "price: 1000"
    )

    assert product_details("Headphones", "E1273", 1, 1000) == expected_output
