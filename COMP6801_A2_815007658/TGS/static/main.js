function redirectTime(url, delay) {
    setTimeout(function () {
        window.location.href = url;
    }, delay);
}