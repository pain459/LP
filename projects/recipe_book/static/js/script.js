document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function(event) {
        const title = document.getElementById('title').value;
        const ingredients = document.getElementById('ingredients').value;
        const instructions = document.getElementById('instructions').value;

        if (!title || !ingredients || !instructions) {
            event.preventDefault();
            alert('Please fill out all fields.');
        }
    });
});
