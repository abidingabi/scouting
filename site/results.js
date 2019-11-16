function render() {
    let a = allStorage();

    if (a.length == 0) {
        alert("You have no scouting data, go back to scoring to add data");
    }

    var index;

    for (index = a.length-1; index >= 0; --index) {
        let previousHTML = document.getElementById("results").innerHTML;
        document.getElementById("results").innerHTML = previousHTML + "<b>Match " + JSON.parse(a[index]).matchNum + " - " + JSON.parse(a[index]).allianceColor + ":</b><br>" + "<canvas id=\"qrcode"+index+"\"></canvas><br>";
    }

    for (index = a.length-1; index >= 0; --index) {
        qrcodegen.QrCode.encodeText(
            a[index], qrcodegen.QrCode.Ecc.MEDIUM
        ).drawCanvas(3, 1, document.getElementById("qrcode"+index));
    }
}

function reset() {
    if(confirm("Are you sure you want to reset ALL YOUR SCOUTING DATA")) {
        localStorage.clear();
    }
}

function allStorage() {
    var values = [],
        keys = Object.keys(localStorage),
        i = keys.length;

    while ( i-- ) {
        values.push( localStorage.getItem(keys[i]) );
    }

    return values;
}