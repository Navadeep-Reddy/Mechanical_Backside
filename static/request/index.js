const vType = document.querySelector("#vtype");
const repair = document.querySelector("#repair");
const message = document.querySelector("#message");
const apply = document.querySelector("#apply");
const section = document.querySelector(".home");
let new_repairs = [];

function display() {
    if (vType.value !== "Vehicle" && repair.value !== "Repair") {
        message.textContent = "You have selected " + vType.value + " and " + repair.value;
        getRelatedRepairs(vType.value, repair.value);
    } else {
        message.textContent = "";
    }
}

function addOption(text) {
    const option = document.createElement("option");
    option.text = text;
    option.value = text;
    repair.add(option);
}

function rec_box(relatedRepairs = []) {
    // Remove existing recbox if it exists
    let existingRecboxDiv = document.querySelector(".recbox");
    if (existingRecboxDiv) {
        section.removeChild(existingRecboxDiv);
    }

    // Create new recbox
    const recboxDiv = document.createElement("div");
    recboxDiv.classList.add("recbox");

    const headingH3 = document.createElement("h3");
    headingH3.textContent = "Additional Recommended Services";

    const ulElement = document.createElement("ul");

    relatedRepairs.forEach(repair => {
        const listItem = document.createElement("li");
        listItem.textContent = repair;
        ulElement.appendChild(listItem);
    });

    const labelElement = document.createElement("label");
    labelElement.textContent = "Add: ";

    const checkboxInput = document.createElement("input");
    checkboxInput.setAttribute("type", "checkbox");
    checkboxInput.classList.add("Recom");
    labelElement.appendChild(checkboxInput);

    recboxDiv.appendChild(headingH3);
    recboxDiv.appendChild(ulElement);
    recboxDiv.appendChild(labelElement);

    section.appendChild(recboxDiv);

    // Add event listener for checkbox input after it is added to the DOM
    checkboxInput.addEventListener("click", function() {
        let selectedOption = repair.options[repair.selectedIndex];
        let updatedText = selectedOption.text;
        new_repairs.forEach(repairItem => {
            if (!updatedText.includes(repairItem)) {
                updatedText = updatedText + ", " + repairItem;
            }
        });
        selectedOption.text = updatedText;
        selectedOption.value = updatedText;
    });
}

function getRelatedRepairs(vehicleType, repairType) {
    fetch('/get_related_repairs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            vehicle_type: vehicleType,
            repair_type: repairType
        })
    })
    .then(response => response.json())
    .then(data => {
        new_repairs = data;
        rec_box(data);
    })
    .catch(error => console.error('Error:', error));
}

repair.addEventListener("change", display);

vType.addEventListener("change", function () {
    repair.innerHTML = '<option disabled selected value="Repair">Repair</option>';

    switch (vType.value) {
        case "Motorcycle":
            addOption("Tire Repair");
            addOption("Gear Adjustment");
            addOption("Brake Checkup");
            addOption("Chain Maintenance");
            addOption("Suspension");
            addOption("Drivetrain");
            addOption("Engine Checkup");
            break;

        case "Bicycle":
            addOption("Tire Puncture");
            addOption("Brake Adjustment");
            addOption("Frame");
            addOption("Suspension");
            break;

        case "Car":
            addOption("Brake Checkup");
            addOption("Suspension");
            addOption("Tire Checkup");
            addOption("Fuel Injector");
            addOption("Transmission");
            addOption("Drivetrain");
            break;

        default:
            break;
    }
});
