const vType = document.querySelector("#vtype");
const repair = document.querySelector("#repair");
const message = document.querySelector("#message");
const apply = document.querySelector("#apply");
const section = document.querySelector(".home") 

function display() {
    rec_box();
    if (vType.value !== "Vehicle" && repair.value !== "Repair") {
        message.textContent = "You have selected " + vType.value + " and " + repair.value;
 
    }
    else {
        message.textContent = "";   
    }
}

function addOption(text) {
    var option = document.createElement("option");
    option.text = text;
    repair.add(option);
}

function rec_box() {
    var existingRecboxDiv = document.querySelector(".recbox");
    if (existingRecboxDiv) {
        section.removeChild(existingRecboxDiv);
    }


    const recboxDiv = document.createElement("div");
    recboxDiv.classList.add("recbox");

    const headingH3 = document.createElement("h3");
    headingH3.textContent = "Additional Recommended";

    const headingH31 = document.createElement("h3");
    headingH31.textContent = "Services";

    const ulElement = document.createElement("ul");

    const listItem1 = document.createElement("li");
    listItem1.textContent = "Related 1";
    ulElement.appendChild(listItem1);

    const listItem2 = document.createElement("li");
    listItem2.textContent = "Related 2";
    ulElement.appendChild(listItem2);

    const labelElement = document.createElement("label");
    const para = document.createElement("p");
    para.textContent = "Add: ";



    const checkboxInput = document.createElement("input");
    checkboxInput.setAttribute("type", "checkbox");
    checkboxInput.classList.add("Recom");
    labelElement.appendChild(para);
    labelElement.appendChild(checkboxInput);

    section.appendChild(recboxDiv);
    recboxDiv.appendChild(headingH3);
    recboxDiv.appendChild(headingH31);
    recboxDiv.appendChild(ulElement);
    recboxDiv.appendChild(labelElement);
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

