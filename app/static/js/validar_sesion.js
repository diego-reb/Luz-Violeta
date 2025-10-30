window.onload = function() {
    fetch('/check_session')
        .then(res => res.json())
        .then(data => {
            if (!data.logged_in) {
                window.location.href = '/login';
            }
        });
};