getMatches <- function(data) {
    matches1 = data[,4:15]
    matches2 = data[,16:27]

    colnames(matches2) <- names(matches1)

    return(rbind(matches1, matches2))
}

addScoreToMatch <- function(match) {
    matchWithAuto = transform(match, autoScore=(
        skystonesDelivered * 10 +
        autoStonesDelivered * 2 +
        autoStonesPlaced * 4 +
        ifelse(foundationRepositioned==TRUE, 10, 0) +
        ifelse(navigated==TRUE, 5, 0)
    ))

    matchWithTeleOp = transform(matchWithAuto, teleOpScore=(
        stonesDelivered * 1 +
        stonesPlaced * 1
    ))

    matchWithEndgame = transform(matchWithTeleOp, endgameScore=(
        ifelse(capped==TRUE, 5, 0) +
        capstoneHeight * 1 +
        ifelse(foundationRepositioned==TRUE, 15, 0) +
        ifelse(parked==TRUE, 5, 0)
    ))

    completeMatch = transform(matchWithEndgame, score=(
        autoScore+teleOpScore + endgameScore
    ))

    return(completeMatch)
}
