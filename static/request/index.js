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
apply.addEventListener("click", function(){
    message.textContent = "Your Order Has Been Noted";
});

