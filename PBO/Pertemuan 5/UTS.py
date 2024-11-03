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

# Kelas turunan pertama
class BasicUser(User):
    def viewProduct(self, productId):
        print(f"Menampilkan informasi untuk produk dengan ID: {productId}")

    def addToCart(self, productId, quantity):
        print(f"Produk dengan ID {productId} sebanyak {quantity} berhasil ditambahkan ke keranjang")

# Kelas turunan kedua
class PremiumUser(BasicUser):
    def applyVoucher(self, voucherCode, cartTotal):
        discount = 0.10
        if cartTotal > 0:
            newTotal = cartTotal * (1 - discount)
            print(f"Voucher '{voucherCode}' berhasil diterapkan! Total belanja setelah diskon: {newTotal}")
        else:
            print("Total belanja harus lebih dari 0 untuk menerapkan voucher")

    def requestPrioritySupport(self, issueDescription):
        print(f"Menghubungi dukungan prioritas untuk masalah: {issueDescription}")

user1 = User("ardibukan", "ardibukan@live.com", "ardi123")
user1.login()
user1.logout()

basicUser = BasicUser("aboy", "aboy@gmail.com", "boyyah87")
basicUser.login()
basicUser.viewProduct("PRD001")
basicUser.addToCart("PRD001", 2)
basicUser.logout()

premiumUser = PremiumUser("masboy", "masboy@gmail.com", "masboy89")
premiumUser.login()
premiumUser.viewProduct("PRD002")
premiumUser.addToCart("PRD002", 3)
premiumUser.applyVoucher("DISC10", 50000)
premiumUser.requestPrioritySupport("Transaksi Gagal")
premiumUser.logout()