import pandas
from ggplot import *

hr_by_team = pandas.read_csv(hr_by_team_year_sf_la_csv)
gg = ggplot(hr_by_team, aes('yearID', 'HR', color = 'teamID')) + geom_point() + geom_line() + ggtitle('Total HRs By Year') + xlab('Year') + ylab('HR')