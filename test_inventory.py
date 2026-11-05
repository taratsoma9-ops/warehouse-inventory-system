def update_inventory(current_quantity, added_quantity):
    return current_quantity + added_quantity


def test_update_inventory():
    assert update_inventory(10, 5) == 20
