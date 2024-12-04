SELECT * FROM tbl_pengadaan WHERE kode_supplier 
IN (SELECT kode_supplier FROM tbl_supplier WHERE nama_supplier LIKE "PT. ABC%")