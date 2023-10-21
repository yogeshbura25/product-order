class Product:
  
    def __init__(self, name, price, deal_price, ratings):
       self.name = name
       self.price = price
       self.deal_price = deal_price
       self.ratings = ratings
       self.you_save = price - deal_price

    def display_product_details(self):
           print("Product: {}".format(self.name))
           print("Price: {}".format(self.price))
           print("Deal Price: {}".format(self.deal_price))
           print("You Saved: {}".format(self.you_save))
           print("Ratings: {}".format(self.ratings))
    
    def get_deal_price(self):
        return self.deal_price

class ElectronicItem(Product):
   def set_warranty(self, warranty_in_months):
       self.warranty_in_months = warranty_in_months
      
   def get_warranty(self):
       return self.warranty_in_months

class GroceryItem(Product):
    pass
   
class Order:
    def __init__(self, delivery_speed, delivery_address):
         self.items_in_cart = []
         self.delivery_speed = delivery_speed
         self.delivery_address = delivery_address 
         
    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
          
    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
             price = product.get_deal_price() * quantity
             total_bill += price
        print("Total Bill: {}".format(total_bill))

milk = GroceryItem("Milk",40, 25, 3.5)
tv = ElectronicItem("TV",45000, 40000, 3.5)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(milk, 2)
order.add_item(tv, 1)
order.display_order_details()
order.display_total_bill()