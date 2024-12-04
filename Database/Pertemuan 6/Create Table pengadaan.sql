CREATE TABLE tbl_pengadaan (
kode_pengadaan VARCHAR(10) PRIMARY KEY,
tgl_pengadaan DATE,
kode_supplier VARCHAR(10),
FOREIGN KEY (kode_supplier) REFERENCES tbl_supplier(kode_supplier)
);
