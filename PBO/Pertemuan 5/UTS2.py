# Kelas parent / Super class
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

class Admin(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
    
    def removeUser(self, userId):
        print(f"Pengguna dengan ID '{userId}' berhasil dihapus oleh Admin {self.username}.")

    def generateReport(self, reportType, startDate, endDate):
        print(f"Laporan '{reportType}' dari {startDate} hingga {endDate} sedang dihasilkan oleh Admin {self.username}.")

seller1 = Seller("Ardi Syah", "ardibukan@gmail.com", "NB001")
seller1.login()
seller1.addProduct("Laptop", "Notebook Acer Nitro", 15000000, 10)
seller1.processOrder("TRX001", "sedang dalam pengiriman")
seller1.logout()

admin1 = Admin("Administrator", "admin@gmail.com", "ADM001")
admin1.login()
admin1.removeUser("NB001")
admin1.generateReport("transaksi", "2024-01-01", "2024-12-31")
admin1.logout()