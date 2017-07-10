from ggplot import *
from pandas import *

hr_year = pandas.read_csv(put_csv_here)
print(ggplot(hr_year, aes('yearID', 'HR')) + geom_point(color = 'red') + geom_line(color = 'red') + ggtitle('Total HRs By Year') + xlab('Year') + ylab('HR'))