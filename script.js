function runCode() {
    const code = document.getElementById('code-editor').value;

        fetch('/run', {
            method: 'POST',
            headers: {
                'Contetn-Type':'application.json'
            },
            body:
            JSON.stringify({ code }),
        }).then(response => response.json()).then(data => {
            document.getElementById('output').textContent = data.output;
        }).catch(error => {
            console.error('Error:', error);
        });
}