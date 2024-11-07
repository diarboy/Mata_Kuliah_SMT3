document.addEventListener('DOMContentLoaded', function () {

    const form = document.querySelector('form');
    const feedback = document.getElementById("formFeedback");
    const fileInput = document.getElementById('files');
    const fileFeedback = document.getElementById('fileFeedback');
    const maxFileSize = 2 * 1024 * 1024;
    const statusRadios = document.querySelectorAll('input[name="pelaku"]');
    const uploadSuratKuasa = document.getElementById('uploadSuratKuasa');

    flatpickr("#lahir", {
        dateFormat: "d/m/Y",
        allowInput: true,
    });

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const dateInput = document.getElementById("lahir").value;
        const datePattern = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/(\d{4})$/;

        if (!datePattern.test(dateInput)) {
            feedback.textContent = 'Format tanggal tidak valid. Gunakan dd/mm/yyyy.';
            feedback.style.display = 'block';
            return;
        }

        if (!fileInput.files.length) {
            feedback.textContent = 'Anda harus mengunggah dokumen.';
            feedback.style.display = 'block';
            return;
        }

        const file = fileInput.files[0];
        if (file.size > maxFileSize) {
            feedback.textContent = 'Ukuran file tidak boleh lebih dari 2 MB.';
            feedback.style.display = 'block';
            return;
        }

        feedback.textContent = 'Formulir berhasil dikirim!';
        feedback.style.display = 'block';
        form.reset();

        setTimeout(() => {
            feedback.style.display = 'none';
        }, 10000);
    });

    statusRadios.forEach(radio => {
        radio.addEventListener('change', function () {
            if (this.value === 'Selaku Kuasa') {
                uploadSuratKuasa.style.display = 'block';
            } else {
                uploadSuratKuasa.style.display = 'none';
            }
        });
    });

    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];
        fileFeedback.style.display = 'none';
        fileFeedback.classList.remove('error', 'success');

        if (file && file.size > maxFileSize) {
            fileFeedback.textContent = 'Ukuran file tidak boleh lebih dari 2 MB.';
            fileFeedback.style.display = 'block';
            fileInput.value = '';
        }
    });
});