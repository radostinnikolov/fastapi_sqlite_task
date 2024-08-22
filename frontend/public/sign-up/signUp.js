async function handleSignUp(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    await httpRequest('http://localhost:8000/sign-up', "POST", data)
    alert("Success!");
    window.location = "http://localhost:5000/login"
}