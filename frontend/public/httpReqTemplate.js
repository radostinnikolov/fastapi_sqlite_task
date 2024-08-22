async function httpRequest(url, httpMethod, data=undefined) {
    let token = localStorage.getItem("token");
    try {
        let config = {
            method: httpMethod,
            headers: {
                'Content-Type': 'application/json'
            }
        }
        
        if (httpMethod === "POST"){
            config.body = JSON.stringify(data) 
        };
        if (token !== null){
            config.headers["Authorization"] = `Bearer ${token}`
        }
        
        const response = await fetch(url, config);
        if (response.ok) {
            const result = await response.json();
            return result
        } else {
            alert('Failed: ' + response.statusText);
        }
        
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

async function httpLoginRequest(url, httpMethod, data) {
    try {
        let config = {
            method: httpMethod,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: data
        }
        const response = await fetch(url, config, data);
        if (response.ok) {
            const result = await response.json();
            localStorage.setItem("token", result.access_token)
            alert("Success!");
            window.location = "http://localhost:5000/"
        } else {
            alert('Failed: ' + response.statusText);
        }
        
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

