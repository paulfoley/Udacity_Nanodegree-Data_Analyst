# Exploring Reddit Data

# Import Library
library(ggplot2)

# Load Data Set
reddit <- read.csv('reddit.csv')

# Explore Reddit Users Employment Status
table(reddit$employment.status)

# Summary of Reddit Users
summary(reddit)

# Age of Reddit Users
levels(reddit$age.range)
qplot(data = reddit, x = age.range)

# Income of Reddit Users
levels(reddit$income.range)
qplot(data = reddit, x = income.range)

# Settings Levels of Ordered Factors Solution
reddit$age.range <- factor(reddit$age.range, levels = c('Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65 or Above'), ordered = T)
reddit$income.range <- factor(reddit$income.range, levels = c("Under $20,000", "$20,000 - $29,999", "$30,000 - $39,999", "$40,000 - $49,999", "$50,000 - $69,999", "$70,000 - $99,999", "$100,000 - $149,999", "$150,000 or more"), ordered = T)

# Plot Age of Reddit Users - Ordered
qplot(data = reddit, x = age.range)

# Plot Income of Reddit Users - Ordered
qplot(data = reddit, x = income.range)
