async function httpRequest(url, httpMethod, data=undefined) {
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