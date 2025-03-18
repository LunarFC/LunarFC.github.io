document.addEventListener("DOMContentLoaded", function() {
    // Get the current page URL
    const currentPage = window.location.pathname.split("/").pop();
    
    // Select all links
    const navLinks = document.querySelectorAll("nav ul li a");

    // Loop through all links
    navLinks.forEach(function(link) {
        // If the link's href matches the current page URL, add the "active" class
        if (link.getAttribute("href") === currentPage) {
            link.parentElement.classList.add("active");
        }
    });
});
