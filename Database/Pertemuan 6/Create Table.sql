CREATE TABLE tbl_detail_pengadaan (
kode_pengadaan VARCHAR(10),
kode_barang VARCHAR(10),
jumlah INT,
total_harga DECIMAL(15, 2),
PRIMARY KEY (kode_pengadaan, kode_barang),
FOREIGN KEY (kode_pengadaan) REFERENCES tbl_pengadaan(kode_pengadaan),
FOREIGN KEY (kode_barang) REFERENCES tbl_barang(kode_barang)
);