class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"{self.username} ({self.email}) berhasil login")

    def logout(self):
        print(f"{self.username} berhasil logout")

class Seller(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
        self.products = []

    def addProduct(self, productName, description, price, stock):
        product = {
            "productName": productName,
            "description": description,
            "price": price,
            "stock": stock
        }
        self.products.append(product)
        print(f"Produk '{productName}' berhasil ditambahkan oleh {self.username}.")

    def processOrder(self, orderId, status):
        print(f"Pesanan dengan ID '{orderId}' diproses dengan status '{status}' oleh {self.username}.")

class PremiumUser(User):
    def viewProduct(self, productName):
        print(f"{self.username} melihat produk '{productName}'.")

    def addToCart(self, productName):
        print(f"{self.username} menambahkan '{productName}' ke keranjang.")

    def applyVoucher(self, voucherCode):
        print(f"{self.username} menggunakan voucher '{voucherCode}'.")

    def requestPrioritySupport(self):
        print(f"{self.username} meminta dukungan prioritas.")

premiumUser = PremiumUser("Ardi-syah", "ardibukan@example.com", 101)
premiumUser.viewProduct("Smartphone")
premiumUser.addToCart("Smartphone")
premiumUser.applyVoucher("DISKON50")
premiumUser.requestPrioritySupport()

seller = Seller("sellerPro", "seller@example.com", 202)
seller.addProduct("Laptop", "Laptop untuk desain grafis", 18000000, 5)
seller.processOrder("O456", "dalam pengiriman")