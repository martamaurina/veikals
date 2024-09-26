class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def get_total_price(self):
        total_price=self.price*self.quantity
        return total_price

maize=Product("Baltmaize", 0.95, 4)
maize.get_total_price()
print("Cena par maizi: ", maize.get_total_price(), "eur")
risi=Product("Rīsi - valdo", 2.45, 2)
risi.get_total_price()
print("Cena par rīsiem: ", risi.get_total_price(), "eur")

#print(maize.get_total_price) 
#print(risi.get_total_price)

class ShoppingCart():
    #def __init__(name):
       # super().__init__(name)
    def add_product_to_cart(self, product):
        print("Produkts", product.name , "Pievienots grozam")
    def remove_product_from_cart_(self, product):
        print("Produkts", product.name , "Nodzēsts no groza" )
    def get_total_price(self, product):
        print("Kopējā summa", product.get_total_price(),"eur")

IepirkumuGrozs = ShoppingCart()
IepirkumuGrozs.add_product_to_cart(maize)
IepirkumuGrozs.get_total_price(maize)
IepirkumuGrozs.add_product_to_cart(risi)
IepirkumuGrozs.get_total_price(risi)

class SystemUser():
    def __init__(self, username, password, email):
        self.username=username
        self.password=password
        self.email=email
    def set_user_info(self, newusername, newpassword, newemail):
        self.nweusername=newusername
        self.newpassword=newpassword
        self.newemail=newemail
        print("Informācija ir nomainīta")
    def get_user_info(self):
        print("Informācija par lietotāju")
        print("Lietotājvārds: ",self.username)
        print("Parole: ", self.password)
        print("E-pasts: ", self.email)

Andris=SystemUser("Andris", "esnezinu", "andrism@gmail.com")
Andris.set_user_info("Andris", "aaaaaaaaa", "andri@gmail.com")
Andris.get_user_info()
