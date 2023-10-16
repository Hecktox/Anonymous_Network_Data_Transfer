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
    function getQueryParam(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    }
    
    // Get the selected IP from the query parameter
    const selectedIP = getQueryParam('selectedIP');

    
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;
    
    console.log('Selected IP:', selectedIP);
    console.log('Message:', message);

    fetch('/send-message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ip: selectedIP,
            message: message
        })
    });

    // Add your logic to send the message

    // Show the snackbar
    const snackbar = document.getElementById('snackbar');
    snackbar.className = 'show';

    // Hide the snackbar after 2 seconds (2000 milliseconds)
    setTimeout(() => {
        snackbar.className = snackbar.className.replace('show', '');
    }, 2000);
}