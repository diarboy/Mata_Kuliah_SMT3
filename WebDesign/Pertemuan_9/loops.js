// Membuat Loop dengan For
for (let i = 0; i < 10; i++) {
    // template literal string
    console.log(`ini perulangan ke ${i + 1}`); // Opsi 1
    console.log("ini perulangan ke " + (i + 1)); // Opsi 2
    console.log("ini perulangan ke", i + 1); // Opsi 3
}

// Membuat Loop dengan For
for (let i = 10; i > 0; i--) { 
    // template literal string
    console.log(`ini perulangan ke ${i}`); // Opsi 1
    console.log("ini perulangan ke " + i); // Opsi 2
    console.log("ini perulangan ke", i); // Opsi 3
}

// Loops dengan While
let j = 1;
while (j < 10) {
    console.warn(`ini perulangan While ke ${j}`);
    j++;
}

// Contoh Menampilkan Data Mahasiswa
let mhs = ["Budi", "Andi", "Joko", "Joni"];
for (let i = 0; i < mhs.length; i++) {
    console.log(mhs[i]);
}

// Membuat function
function salamPembuka(name) {
    console.log("Halo, Selamat Datang " + name);
}

salamPembuka("Budi");

// Membuat Function Expression
let salamPenutup = function (name) {
    console.log("Halo, Sampai Jumpa " + name);
}
salamPenutup("Andi");

// Membuat Arrow Function
let salamPenutup2 = (name) => {
    console.log("Halo, Hati-hati di jalan " + name); // Opsi 1
    console.log(`Halo, Hati-hati di jalan ${name} Widodo`); // Opsi 2
}
salamPenutup2("Joko");

// Scope Variable Local dan Global
let varGlobal = "Ini Variable Global";
let shapeArea = (panjang, lebar) => {
    let varLocal = "ini Variable Local";
    console.log(`Luas untuk persegi dengan Panjang ${panjang} dan Lebar ${lebar} adalah ${panjang * lebar}`);
    console.log(varLocal);
    console.log(varGlobal);
};
shapeArea(5, 10);