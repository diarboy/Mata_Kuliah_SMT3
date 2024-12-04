SELECT 
	tbl_pengadaan.kode_pengadaan,
	tbl_pengadaan.tgl_pengadaan,
	tbl_supplier.kode_supplier,
   tbl_supplier.nama_supplier,
   tbl_supplier.alamat_supplier,
   tbl_detail_pengadaan.kode_barang 
   tbl_barang.nama_barang,
   tbl_detail_pengadaan.jumlah,
   tbl_barang.harga,
   tbl_detail_pengadaan.total_harga
FROM
tbl_pengadaan
JOIN 
tbl_supplier ON tbl_pengadaan.kode_supplier = tbl_supplier.kode_supplier
JOIN 
tbl_detail_pengadaan ON tbl_pengadaan.kode_pengadaan = tbl_detail_pengadaan.kode_pengadaan
JOIN 
tbl_barang ON tbl_detail_pengadaan.kode_barang = tbl_barang.kode_barang