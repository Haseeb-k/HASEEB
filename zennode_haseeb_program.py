

def calculate_total(quantity_list, gift_wrap_list):
    subtotal = 0
    total_discount = 0
    total_quantity = 0
    discount_amount = 0
    discount_amount1 = 0
    discount_amount2 = 0
    discount_amount3 = 0
    discount_amount4 = 0
    discount_applied = ""

    for i, (product, quantity) in enumerate(quantity_list.items()):
        price = catalog[product]
        gift_wrap_fee = gift_wrap_list[i]
        subtotal += quantity * price
        total_quantity += quantity
       

    if total_quantity > 30:
        for i, (product, quantity) in enumerate(quantity_list.items()):
            price = catalog[product]
            if quantity > 15 :
                total_discount += quantity * price * 0.5
                discount_amount1 = total_discount
                
                    
              
    if subtotal > 200 :
        discount_amount2 = 10
          
          

    if total_quantity > 20:
        d = subtotal / 10
        discount_amount3 = d

    for i, (product, quantity) in enumerate(quantity_list.items()):
            price = catalog[product]
            if quantity > 10:
                discount_amount4 =(quantity * price / 20)
   
    if  discount_amount1 > discount_amount:
         discount_applied = "tiered_50_discount"
         discount_amount = discount_amount1
         
    
    if  discount_amount2 > discount_amount:
         discount_applied = "flat_10_discount"
         discount_amount = discount_amount2
         

    if  discount_amount3 > discount_amount:
         discount_applied = "bulk_10_discount"
         discount_amount = discount_amount3
         
    if  discount_amount4 > discount_amount:
         discount_applied = "bulk_5_discount"
         discount_amount = discount_amount4

    shipping_fee = 5 * (total_quantity // 10)
    gift_wrap_fee = sum(gift_wrap_list)
    total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

    # Output results
    print("Product\t\tQuantity\tPrice")
    for product, quantity in quantity_list.items():
        price = catalog[product]
        print(f"{product}\t\t{quantity}\t\t${quantity * price}")
    print("-----------------------------")
    print(f"Subtotal: ${subtotal}")
    if discount_applied:
        print(f"Discount Applied: {discount_applied}\tAmount: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print("-----------------------------")
    print(f"Total: ${total}")


# Main program

catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

quantity_list = {}
gift_wrap_list = []
print("PRICE_LIST\n",catalog)
for product in catalog:
    quantity = int(input(f"Enter the quantity of {product}: "))
    wrapped_as_gift = input(f"Is {product} wrapped as a gift? (yes/no): ")
    quantity_list[product] = quantity
    gift_wrap_list.append(quantity if wrapped_as_gift.lower() == "yes" else 0)

calculate_total(quantity_list, gift_wrap_list)

