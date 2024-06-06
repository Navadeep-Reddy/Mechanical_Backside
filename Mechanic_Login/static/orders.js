document.addEventListener('DOMContentLoaded', function() {
    const orderList = document.querySelector('.order-list tbody');
    const orderUrl = document.querySelector('.order-list').dataset.orderUrl;

    async function addOrders() {
        const list = await User_Details();
        console.log(list);
        list.forEach(item => {
            addOrder(item[0], item[1], item[2], item[3], item[4], item[5]);
        });
    }

    addOrders();

    function addOrder(customerName, vehicle, service, registrationNo, date, emergency) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${customerName}</td>
            <td>${vehicle}</td>
            <td>${service}</td>
            <td>${registrationNo}</td>
            <td>${date}</td>
            <td>${emergency}</td>
            <td class="center-button">
                <div class="order-actions">
                    <form action="${orderUrl}" method="POST">
                        <input type="hidden" name="customer_name" value="${customerName}">
                        <input type="hidden" name="vehicle" value="${vehicle}">
                        <input type="hidden" name="service" value="${service}">
                        <input type="hidden" name="registration_no" value="${registrationNo}">
                        <input type="hidden" name="date" value="${date}">
                        <button type="submit" class="completed">Completed</button>
                    </form>
                </div>
            </td>
        `;
        orderList.appendChild(row);
    }

    let list = User_Details();
    console.log(list);
    for(let i = 0; i < list.length; i++)
    {
        addOrder(list[i]);
    }
});

async function User_Details(){
    const response = await fetch("/get_jobs", {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    });

    data = await response.json();
    return data;
};
