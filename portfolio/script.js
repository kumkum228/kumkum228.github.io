document.getElementById('contact-form').addEventListener('submit', function(event) 
{
    event.preventDefault();
    alert('Thank you for contacting me!');
});

document.getElementById("year").textContent = new Date().getFullYear();
