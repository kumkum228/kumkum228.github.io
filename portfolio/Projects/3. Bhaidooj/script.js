// Play background music when the page loads
window.addEventListener('load', function() {
    var bgMusic = document.getElementById('bgMusic');
    bgMusic.play();
});

// Play sound effect when button is clicked
document.getElementById('messageButton').addEventListener('click', function() {
    var message = document.getElementById('message');
    var clickSound = document.getElementById('clickSound');
    
    // Play the click sound
    clickSound.play();
    
    // Toggle the message visibility
    if (message.classList.contains('hidden')) {
        message.classList.remove('hidden');
    } else {
        message.classList.add('hidden');
    }
});
