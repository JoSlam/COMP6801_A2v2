function redirectTime(url, delay) {
    setTimeout(function () {
        window.location.href = url;
    }, delay);
}

function connectToService(url){
    fetch(url)
    .then(data => {return data.json()})
    .then(res => alert(res.data))
}