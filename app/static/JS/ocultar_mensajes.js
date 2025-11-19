document.addEventListener("DOMContentLoaded", () => {
    const messages = document.querySelectorAll(".flash-message");

    messages.forEach((msg, index) => {
        setTimeout(() => {
            msg.classList.add("fade-out");
        }, 4000);

        setTimeout(() => {
            msg.remove();
        }, 5000); 
    });
});
