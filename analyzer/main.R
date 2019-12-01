library(tidyverse)
library(rmarkdown)

source("util.R")

args = commandArgs(trailingOnly=TRUE)

if (length(args) == 1 && args[1]=="test") {
    data <- read.csv("fake_match_results.csv")
} else {
    data <- read.csv("match_results.csv")
}

matchesWithoutScore = getMatches(data)

matches = addScoreToMatch(matchesWithoutScore)

#print("Scores Overall:")
#print(summary(matches[13:16]))

matchesWithJustScores <- matches[c(1, 13:16)]

averageTeamResults = aggregate(autoScore ~ teamNum, matches, mean)
averageTeamResults$teleOpScore = aggregate(teleOpScore ~ teamNum, matches, mean)[,2]
averageTeamResults$endgameScore = aggregate(endgameScore ~ teamNum, matches, mean)[,2]
averageTeamResults$score = aggregate(score ~ teamNum, matches, mean)[,2]
averageTeamResults$autoStonesDelivered = aggregate(autoStonesDelivered ~ teamNum, matches, mean)[,2]
averageTeamResults$stonesDelivered = aggregate(stonesDelivered ~ teamNum, matches, mean)[,2]
averageTeamResults$autoStonesPlaced = aggregate(autoStonesPlaced ~ teamNum, matches, mean)[,2]
averageTeamResults$stonesPlaced = aggregate(stonesPlaced ~ teamNum, matches, mean)[,2]

ggplot(averageTeamResults, aes(
                               x = autoScore,
                               y = teleOpScore,
                               color=endgameScore)) +
    geom_text(aes(label = averageTeamResults$teamNum), size = 3) +
    labs(title = "Scores",
         x = "TeleOp Score",
         y = "Autonomous Score",
         color = "End Game Score")

ggplot(averageTeamResults, aes(
                               x = autoStonesDelivered,
                               y = autoStonesPlaced)) +
    geom_text(aes(label = averageTeamResults$teamNum), size = 3) +
    labs(title = "Auto Stones",
         x = "Auto Stones Delivered",
         y = "Auto Stones Placed")


ggplot(averageTeamResults, aes(
                               x = stonesPlaced,
                               y = stonesDelivered)) +
    geom_text(aes(label = averageTeamResults$teamNum), size = 3) +
    labs(title = "TeleOp Stones",
         x = "Stones Delivered",
         y = "Stones Placed")
