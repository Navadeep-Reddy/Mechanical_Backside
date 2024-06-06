document.addEventListener('DOMContentLoaded', function() {
    const orderList = document.querySelector('.order-list tbody');
    const orderUrl = document.querySelector('.order-list').dataset.orderUrl;

    function addOrder(customerName, vehicle, service, registrationNo, date) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${customerName}</td>
            <td>${vehicle}</td>
            <td>${service}</td>
            <td>${registrationNo}</td>
            <td>${date}</td>
            <td class="center-button">
                <div class="order-actions">
                    <form action="${orderUrl}" method="POST">
                        <button type="submit" class="completed">Completed</button>
                    </form>
                </div>
            </td>
        `;
        orderList.appendChild(row);
    }

    // Add orders
    addOrder('Newbie', 'Motorcycle', 'Puncture', 'TN2332', '2024-05-27');
    addOrder('Newbie', 'Bicycle', 'Tire Alignment', 'TN3785', '2024-05-28');
    addOrder('Navadeep', 'Motorcycle', 'Engine Oil Replacement', 'AP7892', '2024-05-21');
    addOrder('Update', 'Car', 'Transmission, Engine Maintenance, Fuel Injector, Drivetrain', '-', '2024-05-10');
    addOrder('Update', 'Car', 'Tire Checkup', '-', '2024-05-11');
    addOrder('Update', 'Car', 'Tire Checkup, Brake Checkup, Fuel Injector', '-', '2024-05-12');
    addOrder('Update', 'Bicycle', 'Tire Puncture, Wheel Checkup, Tube Replacement', '-', '2024-05-13');
    addOrder('Update', 'Bicycle', 'Suspension', '-', '2024-05-14');
    addOrder('Navadeep1', 'Car', 'Fuel Injector', 'TN8439', '2024-05-06');
    addOrder('Navadeep1', 'Bicycle', 'Frame, Headset Adjustment, Wheel Checkup, Lubrication, Suspension', 'TN98348', '2024-05-03');
    addOrder('Navadeep1', 'Empty', 'Empty', '-', '-');
});
