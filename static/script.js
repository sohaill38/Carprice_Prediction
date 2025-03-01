
function validateForm(event) {
    var inputs = event.target.getElementsByTagName("input");
    var selects = event.target.getElementsByTagName("select");
    var isValid = true;

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value === "") {
            isValid = false;
            break;
        }
    }

    if (isValid) {
        for (var j = 0; j < selects.length; j++) {
            if (selects[j].value === "") {
                isValid = false;
                break;
            }
        }
    }

    if (!isValid) {
        alert("Please fill in all the fields.");
        event.preventDefault();
    }
}
