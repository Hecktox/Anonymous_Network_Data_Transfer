 // Function to get the value of a query parameter by name
 function getQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Get the selected IP from the query parameter
const selectedIP = getQueryParam('selectedIP');

if (selectedIP) {
    // Display the selected IP in a box
    document.write('<p>Selected IP: ' + selectedIP + '</p>');
} else {
    document.write('<p>No IP selected</p>');
}