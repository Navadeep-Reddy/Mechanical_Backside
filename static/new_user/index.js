warningEl = document.querySelector("#warning");
userEl = document.querySelector("#user-el");
passEl = document.querySelector("#pass-el");
repassEl = document.querySelector("#repass-el");
buttonEl = document.querySelector("#button-el");

buttonEl.addEventListener("click", function(event){

    if (userEl.value.trim() == "") {
        event.preventDefault();
        warningEl.innerText = "Username is empty";
    }

    else if (passEl.value.trim() == "" && repassEl.value == "" )
        {
            event.preventDefault()
            warningEl.innerText = "Empty Password!";
        }

    else {
        if (passEl.value !== repassEl.value){
            event.preventDefault();
            warningEl.innerText = "Passwords do not match";

        }

        else warningEl.innerText = ""; 
    }
});
