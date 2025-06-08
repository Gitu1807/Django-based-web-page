// fileapp/static/fileapp/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    const dropdown = document.getElementById('fileDropdown');
    const viewBtn = document.getElementById('viewBtn');
    const modal = document.getElementById('modal');
    const downloadBtn = document.getElementById('downloadBtn');

    dropdown.addEventListener('change', () => {
        viewBtn.disabled = !dropdown.value;
    });

    viewBtn.addEventListener('click', () => {
        const selectedFile = dropdown.value;
        fetch(`/check-file/?filename=${selectedFile}`)
            .then(response => response.json())
            .then(data => {
                if (data.exists) {
                    window.location.href = `/open-file/?filename=${selectedFile}`;
                } else {
                    modal.classList.remove('hidden');
                }
            });
    });

    downloadBtn.addEventListener('click', () => {
        const selectedFile = dropdown.value;
        window.location.href = `/download-file/?filename=${selectedFile}`;
        modal.classList.add('hidden');
    });
});
