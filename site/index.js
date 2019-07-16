var qr0;

function calculate() {
    var schema = genSchema();
    let score1 = getScore(schema.team1);
    let score2 = getScore(schema.team2);

    document.getElementById("score1").innerHTML = score1;
    document.getElementById("score2").innerHTML = score2;
    document.getElementById("score").innerHTML = score1+score2;

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
        matchNum: document.getElementById('matchNum').value,
        allianceColor: document.querySelector('input[name="allianceColor"]:checked').value,
        team1: {
            num: document.getElementById('team1').value,
            auto: {
                land: document.getElementById('land1').checked,
                sample: document.getElementById('sample1').checked,
                claim: document.getElementById('claim1').checked,
                park: document.getElementById('park1').checked,
            },
            teleOp: {
                cargoHoldMinerals: document.getElementById('cargoHoldMinerals1').value,
                depotHoldMinerals: document.getElementById('depotHoldMinerals1').value,
            },
            endgame: {
                endgameState: document.querySelector('input[name="endgameState1"]:checked').value
            }
        },
        team2: {
            num: document.getElementById('team2').value,
            auto: {
                land: document.getElementById('land2').checked,
                sample: document.getElementById('sample2').checked,
                claim: document.getElementById('claim2').checked,
                park: document.getElementById('park2').checked,
            },
            teleOp: {
                cargoHoldMinerals: document.getElementById('cargoHoldMinerals2').value,
                depotHoldMinerals: document.getElementById('depotHoldMinerals2').value,
            },
            endgame: {
                endgameState: document.querySelector('input[name="endgameState2"]:checked').value
            }
        }
    }
}

function getScore(team) {
    var score = 0;
    
    if (team.auto.land) {
        score += 30;
    }
    if (team.auto.sample) {
        score += 25;
    }
    if (team.auto.claim) {
        score += 15;
    }
    if (team.auto.park) {
        score += 10;
    }

    score += team.teleOp.cargoHoldMinerals * 5
    score += team.teleOp.depotHoldMinerals * 2

    switch (team.endgame.endgameState) {
        case "hang":
            score += 50;
            break
        case "partialPark":
            score += 15;
            break;
        case "fullPark":
            score += 25;
            break;
    }

    return score;
}