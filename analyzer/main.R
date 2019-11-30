library(tidyverse)

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

averageTeamResults = aggregate(autoScore ~ teamNum, matchesWithJustScores, mean)
averageTeamResults$teleOpScore = aggregate(teleOpScore ~ teamNum, matchesWithJustScores, mean)[,2]
averageTeamResults$endgameScore = aggregate(endgameScore ~ teamNum, matchesWithJustScores, mean)[,2]
averageTeamResults$score = aggregate(score ~ teamNum, matchesWithJustScores, mean)[,2]

ggplot(averageTeamResults, aes(
                               x = autoScore,
                               y = (teleOpScore),
                               color=endgameScore)) +
    geom_text(aes(label = averageTeamResults$teamNum), size = 3)
#    labs(title = "Score TL;DR",
#         caption = "Autonomous Score vs TeleOp and Endgame Score",
#         x = "TeleOp + Endgame Score",
#         y = "Autonomous Score")
   
#color = stonesDelivered)) +
#                    alpha = climbRate)) + 
#  labs(title = "Scale Robot Exploration", 
#       caption = "Data collected by FRC 1712", 
#       x = "Mean total cubes per match", 
#       y = "Mean scale cubes per match",
#       color = "Do they have a two-cube scale auto?") 

