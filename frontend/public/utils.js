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