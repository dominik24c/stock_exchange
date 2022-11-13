//
// const getCookie = (name) => {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//         const values = cookies[i].split("=");
//         const key = values[0];
//         const value = values[1];
//         if (key === name) {
//             return value;
//         }
//     }
//     return null;
// }

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const renderRows = () => {
    const csrftoken = getCookie('csrftoken');
    fetch(`${window.location.origin}/stock-exchange/data`, {
        mode: 'same-origin',
        headers: {'X-CSRFToken': csrftoken},
    })
        .then((response) => {
            // console.log(response);
            return response.json();
        })
        .then((data) => {
            // console.log(data);
            const tbody = document.querySelector('div#stock-exchange > table > tbody');
            tbody.innerHTML = '';
            if (data && data.stock_exchange) {
                data.stock_exchange.forEach(item => {
                    const row = document.createElement('tr');
                    const items = [item.name, item.exchange, item.rate_change, item.rate_change_percent,
                        item.number_of_transaction, item.turnover, item.opening, item.min, item.max, item.updated_at]
                    items.forEach(value => {
                        const td = document.createElement('td')
                        td.innerHTML = value;
                        row.append(td);
                    })
                    tbody.append(row);
                })
            }
        });
}

renderRows();
setInterval(renderRows, 5 * 60 * 1000);
