function Delete_Performance(input_id, csrfToken) {
    
    if (confirm("Are you sure you want to delete this performance?")) {
        fetch('/delete_performance/' + input_id + '/', {
            
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-CSRFToken': csrfToken
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            window.location.reload();
        })
        .catch(error => {
            console.error(error);
            console.log(error.response);
        });
    }
}
