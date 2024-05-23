const vType = document.querySelector("#vtype");
const repair = document.querySelector("#repair");
const message = document.querySelector("#message");
const apply = document.querySelector("#apply");

function display()
{
    if (vType.value != "Vehicle" && repair.value!= "Repair") message.textContent = "You have selected " + vType.value + " and " + repair.value;
};

repair.addEventListener("change", display);
vType.addEventListener("change", display);

vType.addEventListener("change", function(){
    repair.innerHTML = "";

    if (vType.value === "Motorcycle") {
        var newOption = document.createElement("option");
        newOption.text = "Tire Repair";

        var newOption1 = document.createElement("option");
        newOption1.text = "Gear Adjustment";

        var newOption2 = document.createElement("option");
        newOption2.text = "Brake Checkup";

        var newOption3 = document.createElement("option");
        newOption3.text = "Chain Maintenance";

        var newOption4 = document.createElement("option");
        newOption4.text = "Suspension";

        var newOption5 = document.createElement("option");
        newOption5.text = "Drivetrain";

        var newOption6 = document.createElement("option");
        newOption6.text = "Engine Checkup";


        repair.add(newOption);
        repair.add(newOption1);
        repair.add(newOption2);
        repair.add(newOption3);
        repair.add(newOption4);
        repair.add(newOption5);
        repair.add(newOption6);
    }


    else if (vType.value === "Bicycle") {
        var newOption = document.createElement("option");
        newOption.text = "Tire Puncture";

        var newOption1 = document.createElement("option");
        newOption1.text = "Brake Adjustment";

        var newOption2 = document.createElement("option");
        newOption2.text = "Frame";

        var newOption3 = document.createElement("option");
        newOption3.text = "Suspension";

        repair.add(newOption);
        repair.add(newOption1);
        repair.add(newOption2);
        repair.add(newOption3);

    }

    else if(vType.value === "Car"){
        var newOption = document.createElement("option");
        newOption.text = "Brake Checkup";

        var newOption1 = document.createElement("option");
        newOption1.text = "Suspension";

        var newOption2 = document.createElement("option");
        newOption2.text = "Tire Checkup";

        var newOption3 = document.createElement("option");
        newOption3.text = "Fuel Injector";

        var newOption4 = document.createElement("option");
        newOption4.text = "Transmission";

        var newOption5 = document.createElement("option");
        newOption5.text = "Drivetrain";

        repair.add(newOption);
        repair.add(newOption1);
        repair.add(newOption2);
        repair.add(newOption3);
        repair.add(newOption4);
        repair.add(newOption5);

    }

});



