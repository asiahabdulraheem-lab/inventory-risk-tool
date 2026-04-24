import csv


def check_inventory(file_name):
    low_stock_items = []

    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                stock_level = int(row['stock_level'])
                reorder_threshold = int(row['reorder_threshold'])

                if stock_level < reorder_threshold:
                    low_stock_items.append((row['product_id'], row['category']))

            except ValueError:
                continue

    return low_stock_items


def main():
    items = check_inventory("inventory_data.csv")

    print("Items that need reordering:\n")

    for product_id, category in items:
        print(f"Product ID: {product_id}, Category: {category}")


if __name__ == "__main__":
    main()
