function createTableRow(obj) {
    const sortedObj = {
        'id': obj.id,
        "sender_name": obj.sender_name,
        "receiver_name": obj.receiver_name,
        "sender_email": obj.sender_email,
        "sender_phone": obj.sender_phone,
        "receiver_phone": obj.receiver_phone,
        "item": obj.item,
        "quantity": obj.quantity,
        "weight": obj.weight,
    }
    const tr = document.createElement('tr');
    Object.values(sortedObj).forEach(data => {
        const td = document.createElement('td');
        td.textContent = data;
        tr.appendChild(td);
    });
    const tdDel = document.createElement('td');
    tdDel.appendChild(createDeleteButton(sortedObj.id))
    tr.appendChild(tdDel)
    return tr;
}
function createDeleteButton(id){
    var btn = document.createElement('input');
    btn.type = "button";
    btn.value = "Delete";
    btn.addEventListener("click", () => handleDelete(id))
    return btn
}
function changeBackgroundColor(){
    const colors = ['red', 'blue', 'green', 'yellow', 'white']
    let random = Math.floor(Math.random() * colors.length)
    document.getElementById("body").style.backgroundColor = colors[random]
}

function redirectToPortal(event){
    let token = localStorage.getItem("token");
    if (token === null){
        window.location = "http://localhost:5000/portal"
    }
}

function redirectToLogin(){
    window.location = "http://localhost:5000/login"
}

function redirectToSignUp(){
    window.location = "http://localhost:5000/sign-up"
}

function logout(){
    localStorage.removeItem('token')
    window.location = "http://localhost:5000/portal"
}