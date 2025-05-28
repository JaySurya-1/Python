print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

inventory = {'sword': 2,'shield': 1,'healing potion': 5,'gold coin': 100}

def display_inventory(inv):
    print("Inventory:")
    total_items = 0
    for item, count in inv.items():
        print(f"{count} x {item}")
        total_items += count
    print(f"\nTotal number of items: {total_items}")

display_inventory(inventory)
