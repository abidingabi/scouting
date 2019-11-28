var qr0;

function calculate() {
    var schema = genSchema();
    let score1 = getScore(schema.team1);
    let score2 = getScore(schema.team2);

    document.getElementById("score1").innerHTML = score1;
    document.getElementById("score2").innerHTML = score2;
    document.getElementById("score").innerHTML = score1+score2+schema.tallestSkyscraper*2;

    console.log(schema);

    var qrc = qrcodegen.QrCode;
    qr0 = qrc.encodeText(JSON.stringify(schema), qrc.Ecc.MEDIUM);
    qr0.drawCanvas(3, 1, document.getElementById("qrcode"));
}

function save() {
    var schema = genSchema()

    localStorage.setItem(schema.matchNum+schema.allianceColor, JSON.stringify(schema))
}

function genSchema() {
    return {
        matchNum: document.getElementById('matchnum').value,
        allianceColor: document.getElementById("alliancecolor").options[document.getElementById("alliancecolor").selectedIndex].value,
        tallestSkyscraper: document.getElementById("tallestskyscraperheight").value,
        team1: {
            num: document.getElementById('team1').value,
            auto: {
                skystonesDelivered: document.getElementById('skystonesdelivered1').value,
                stonesDelivered: document.getElementById('autostonesdelivered1').value,
                stonesPlaced: document.getElementById('autostonesplaced1').checked,
                foundationRepositioned: document.getElementById('repositioned1').checked,
                navigated: document.getElementById('navigated1').checked
            },
            teleOp: {
                stonesDelivered: document.getElementById('stonesdelivered1').value,
                stonesPlaced: document.getElementById('stonesplaced1').value
            },
            endgame: {
                capped: document.getElementById('capped1').checked,
                capstoneHeight: document.getElementById("capstoneheight1").value,
                foundationMoved: document.getElementById("foundationmoved1").checked,
                parked: document.getElementById("parked1").checked
            }
        },
        team2: {
            num: document.getElementById('team2').value,
            auto: {
                skystonesDelivered: document.getElementById('skystonesdelivered2').value,
                stonesDelivered: document.getElementById('autostonesdelivered2').value,
                stonesPlaced: document.getElementById('autostonesplaced2').checked,
                foundationRepositioned: document.getElementById('repositioned2').checked,
                navigated: document.getElementById('navigated2').checked
            },
            teleOp: {
                stonesDelivered: document.getElementById('stonesdelivered2').value,
                stonesPlaced: document.getElementById('stonesplaced2').value
            },
            endgame: {
                capped: document.getElementById('capped2').checked,
                capstoneHeight: document.getElementById("capstoneheight2").value,
                foundationMoved: document.getElementById("foundationmoved2").checked,
                parked: document.getElementById("parked2").checked
            }
        }
    }
}

function getScore(team) {
    var score = 0;

    score += team.auto.skystonesDelivered * 10
    score += team.auto.stonesDelivered * 2
    score += team.auto.stonesPlaced * 4
    if (team.auto.foundationRepositioned) {
        score += 10
    }
    if (team.auto.navigated) {
        score += 5
    }

    score += team.teleOp.stonesDelivered * 1
    score += team.teleOp.stonesPlaced * 1

    if (team.endgame.capped) {
        score += 5
    }
    score += team.endgame.capstoneHeight * 1
    if (team.endgame.foundationMoved) {
        score += 15
    }
    if (team.endgame.parked) {
        score += 5
    }

    return score;
}