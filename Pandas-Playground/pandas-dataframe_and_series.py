from pandas import DataFrame, Series
from numpy import mean

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
            'Netherlands', 'Germany', 'Switzerland', 'Belarus',
            'Austria', 'France', 'Poland', 'China', 'Korea', 
            'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
            'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
            'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts = {'country_name':countries,
                        'gold': Series(gold),
                        'silver': Series(silver),
                        'bronze': Series(bronze)} 

# Functions 
def avg_medal_count(olympic_medal_counts):
    # Returns averages for medal count
    df = DataFrame(olympic_medal_counts)
    avg_bronze_at_least_one_gold = mean(df['bronze'][df['gold']>=1])
    avg_medal_count = df[['gold','silver','bronze']].apply(mean)
    
    return (avg_medal_count, avg_bronze_at_least_one_gold)

print(avg_medal_count(olympic_medal_counts))