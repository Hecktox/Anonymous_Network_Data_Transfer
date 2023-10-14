function handleDragOver(event) {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
}

function handleDrop(event) {
    event.preventDefault();

    const files = event.dataTransfer.files;
    if (files.length > 0) {
        // Handle dropped files here
        console.log('Dropped files:', files);
    }
}

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;
    console.log('Message:', message);

    // Add your logic to send the message
}