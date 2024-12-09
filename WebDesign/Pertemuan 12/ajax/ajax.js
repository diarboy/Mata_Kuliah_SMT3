// Membuat Objek untuk menampung XMLHttpRequest
var xhr = new XMLHttpRequest();
// Membuat GET untuk mengambil data
xhr.open("GET",
    "https://jsonplaceholder.typicode.com/posts", true);
// Membuat IF untuk menangani perubahan data server 
xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
        var responData = JSON.parse(xhr.responseText);
        console.log(responData);
    }
};
xhr.send();