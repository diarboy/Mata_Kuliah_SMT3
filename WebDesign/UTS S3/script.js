document.addEventListener('DOMContentLoaded', function () {
    flatpickr("#lahir", {
        dateFormat: "d/m/Y", 
        allowInput: true,
    });

    const form = document.querySelector('form');
    const feedback = document.getElementById("formFeedback");

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const dateInput = document.getElementById("lahir").value;
        const datePattern = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/(\d{4})$/;

        if (!datePattern.test(dateInput)) {
            feedback.textContent = 'Format tanggal tidak valid. Gunakan dd/mm/yyyy.';
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
});
