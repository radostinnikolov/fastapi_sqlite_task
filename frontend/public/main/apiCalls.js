async function handleSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    httpRequest('http://localhost:8000/create-order', "POST", data)
    form.reset();
    
};
async function handleUpdate() {
    table = document.getElementById("rows")
    while (table.firstChild) {
    table.firstChild.remove()
    }

    orders = await httpRequest('http://localhost:8000/orders', "GET")
    orders.forEach((item) => table.appendChild(createTableRow(item)));
}
async function handleDelete(id) {
    await httpRequest(`http://localhost:8000/orders/${id}`, "DELETE")
    await handleUpdate();
}

