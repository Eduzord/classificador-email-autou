document.getElementById('email-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Erro na resposta do servidor.');
        }

        const data = await response.json();
        const resultsDiv = document.getElementById('results');
        const resultContentDiv = document.getElementById('result-content');

        resultContentDiv.innerHTML = `
            <p><strong>Classificação:</strong> <span class="badge ${data.categoria === 'Produtivo' ? 'bg-success' : 'bg-secondary'}">${data.categoria}</span></p>
            <p><strong>Resposta Sugerida:</strong></p>
            <div class="alert alert-info">
                ${data.resposta_sugerida}
            </div>
        `;

        resultsDiv.style.display = 'block';

    } catch (error) {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao processar o e-mail. Tente novamente.');
    }
});