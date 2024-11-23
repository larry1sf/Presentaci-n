
    document.querySelectorAll('.toggle-btn').forEach(button => {
        button.addEventListener('click', () => {
            const targetId = button.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);

            if (targetElement.style.display === 'none') {
                targetElement.style.display = 'block';
                button.textContent = 'Leer menos'; // Cambia el texto del botón
            } else {
                targetElement.style.display = 'none';
                button.textContent = 'Leer más'; // Restablece el texto del botón
            }
        });
    });


    

