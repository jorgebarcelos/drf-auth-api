const formEl = document.querySelector(".user-data")

formEl.addEventListener('submit', event =>{
    event.preventDefault()

    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData)

    fetch('http://127.0.0.1:8000/api/signup', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
})