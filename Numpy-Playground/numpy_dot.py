## Numpy Dot Function

# Import Numpy 
from pandas import DataFrame, Series
from numpy import dot

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
            'Netherlands', 'Germany', 'Switzerland', 'Belarus',
            'Austria', 'France', 'Poland', 'China', 'Korea', 
            'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
            'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
            'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

def numpy_dot(countries,gold,silver,bronze):
    medals = [gold, silver, bronze]
    points = [4,2,1]
    medal_points = dot(points,medals)
    olympic_points_df = DataFrame({'country_name' : Series(countries),'points': Series(medal_points)})
    
    return olympic_points_df

print(numpy_dot(countries,gold,silver,bronze))