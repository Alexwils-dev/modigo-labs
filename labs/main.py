def fulfill_orders(stock, orders):
    remaining_stock = stock.copy()
    fulfilled = []
    rejected = []

    for order in orders:
        order_id = order["id"]
        items = order["items"]

        can_fulfill = True

        for item, quantity in items.items():
            available = remaining_stock.get(item, 0)

            if available < quantity:
                can_fulfill = False
                break

        if can_fulfill:
            for item, quantity in items.items():
                remaining_stock[item] -= quantity

            fulfilled.append(order_id)
        else:
            rejected.append(order_id)

    return {
        "fulfilled": fulfilled,
        "rejected": rejected,
        "remaining_stock": remaining_stock
    }





print(fulfill_orders({"apple": 5}, [{"id": "o1", "items": {"apple": 2}}, {"id": "o2", "items": {"apple": 4}}]))