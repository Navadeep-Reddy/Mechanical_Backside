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
        newOption.text = "Faulty Chain Sprocket";

        var newOption1 = document.createElement("option");
        newOption1.text = "Engine Oil Replacement";

        var newOption2 = document.createElement("option");
        newOption2.text = "Puncture";

        var newOption3 = document.createElement("option");
        newOption3.text = "Tire Alignment";


        repair.add(newOption);
        repair.add(newOption1);
        repair.add(newOption2);
        repair.add(newOption3);
        repair.add(newOption4);
    }

    else if (vType.value === "Bicycle") {
        var newOption = document.createElement("option");
        newOption.text = "Chain adjustment";

        var newOption1 = document.createElement("option");
        newOption1.text = "Brake Disc Replacement";

        var newOption2 = document.createElement("option");
        newOption2.text = "Puncture";

        var newOption3 = document.createElement("option");
        newOption3.text = "Tire Alignment";

        var newOption4 = document.createElement("option");
        newOption4.text = "Horn Replacement";

        var newOption5 = document.createElement("option");
        newOption5.text = "Seat Tightening";

        repair.add(newOption);
        repair.add(newOption1);
        repair.add(newOption2);
        repair.add(newOption3);
        repair.add(newOption4);
        repair.add(newOption5);
    }

    else if(vType.value === "Car"){
        var newOption = document.createElement("option");
        newOption.text = "Engine Maintenance";

        var newOption1 = document.createElement("option");
        newOption1.text = "Battery Checkup";

        var newOption2 = document.createElement("option");
        newOption2.text = "Tire Checkup";

        var newOption3 = document.createElement("option");
        newOption3.text = "Brackets";

        var newOption4 = document.createElement("option");
        newOption4.text = "Detailing";

        var newOption5 = document.createElement("option");
        newOption5.text = "Coolant Refill";

        repair.add(newOption);
        repair.add(newOption1);
        repair.add(newOption2);
        repair.add(newOption3);
        repair.add(newOption4);
        repair.add(newOption5);

    }

});



