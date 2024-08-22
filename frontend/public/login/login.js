async function handleLogin(event) {
    console.log("here")
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const info = Object.fromEntries(formData);

    data = new URLSearchParams({
        'grant_type': 'password',
        'username': info.username,
        'password': info.password
    })
    await httpLoginRequest("http://localhost:8000/token", "POST", data)
}