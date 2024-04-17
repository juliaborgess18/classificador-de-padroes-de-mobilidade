document.getElementById("uploadForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById("fileInput");
    formData.append("file", fileInput.files[0]);
    postArquivoCsv(formData);

    async function postArquivoCsv(formData){
        try {
            const response = await fetch('http://localhost:8000/upload/', {
                method: 'POST',
                body: formData
            });
    
            if (response.ok) {
                document.getElementById("status").innerText = "Arquivo enviado com sucesso!";
            } else {
                const data = await response.json();
                throw new Error(data.detail);
            }
        } catch (error) {
            document.getElementById("status").innerText = "Erro ao enviar arquivo: " + error.message;
        }
    }

    
});
