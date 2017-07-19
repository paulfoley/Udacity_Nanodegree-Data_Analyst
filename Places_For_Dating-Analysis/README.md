# Best Places for Dating

## Summary

A common problem amongst my friends is finding a significant other. I have girlfriend, so I am set, but I’m always willing to play cupid with my friends, male or female.

As a real-life example, I have a friend, that lives in Manhattan NY; For the analysis we’ll call her by the fake name Alexa (for privacy purposes). She complains New York, is the worst place in the world to date men because there are too MANY WOMEN, and and the competition makes dating hard. 

Then on the other hand I have a friend that lives in San Jose CA: We'll call him by the fake name Alex (again for privacy purposes). He complains that San Jose is the worst place in the world to date women, because there seems to be an overwhelming amount of tech dudes in the city and that makes competition hard.

## Analysis Design
So, let’s help out our friends Alexa and Alex find their one true love, using data! We’re going to maximize their chances for success by finding their optimal location to date. 

Let’s start with Alexa. To do this we’re going to focus on areas that have a high ratio of single men.

First, let’s find the states that have the most men:

![MAP – Men Single Ratio By State](https://public.tableau.com/shared/TQ24WQNTF?:display_count=yes)

The chart is clear! Women should move to Alaska, where there is the highest ratio of single men, 19.32% to be exact, that’ll increase their odds!

O wait… Alexa is telling me that she’s not moving to Alaska just to find a husband, apparently, it’s too cold and far away from family. It’s back to the drawing board. The next best option is finding places in the continental US that have high single male ratios.

I got an idea! Next let’s plot a bar graph of single men by area. 

[Bar Chart – Men Ratio By Area]

Great news! There are some areas that have 90%+ single men, that’s great odds! I’m going to recommend Alexa move to Little America WY, a small town of 68 people in the middle of nowhere.

O wait… Alexa is telling me that she’s not moving to a small town in the middle of nowhere just to find a husband. 

From talking a little more to Alexa, it sounds like there are certain criteria to move to an area. The first of which is the area needs to be a small city or larger. Which for our purposes we will consider 500,000+ people. Denver, where I currently live is around 650,000 people and is amazing!

Also, from what Alexa tells me, it sounds like age range is important to her, she’ll only date men between 25 to 40. So, let’s change our search criteria a little bit to weed out the single college people, and the single elderly people. (Side note I have nothing against people aged 40+, it’s just Alexa is really picky and I think that’s part of her dating problem, but that’s a different analysis)

We’re going to need a new metric – percent men single between the ages of 25 and 40.  I created this using Tableau’s Create Field functionality. Now our target areas are cities, and we have a specific age range. Let’s replot! 

[Bar Chart – Top Cities For Single Men]
 
Great! So, the choice is clear San Francisco CA, Manhattan NY, and Seattle WA. These are the best places for a girl to be single.

O wait… we’re kind of back where we started... the whole reason we started this was to find a place for Alexa, who lives in Manhattan NY, to move to… and now we’re recommending she stay in the same place.

We forgot to add in a crucial data point, gender ratio. There’s been a bunch of really great articles written about how gender ratio messes up dating. To keep the thesis really simple, human heterosexual marriage and coupling is (usually) 1 to 1. So, in areas where there are uneven gender ratios, say 54% to 46%, for every 100 people there’s at-least 8 people left un-paired, which ends up driving a higher single %age.

So, to help Alexa out, let’s add in a filter of male ratio that is 50% or greater:

[Bar Chart – Top Cities for Single Men]

AND BOOM! The city of choice for single women to find a mate are San Francisco CA, Seattle WA, and San Jose CA. It looks like a move to the west coast is needed!

Now let’s do the same exact steps with Alex. His criteria is a city as well, dating age range of 18 to 34, and a gender ratio of women 52%+. Here’s the plot we got:

[Bar Chart – Women Single Ratio By City]

It looks like Alex needs to move to Manhattan NY, Baltimore MD, or Bronx NY!

That ends our analysis for this project, using Tableau’s charts we can quickly find the best cities for our single friends to live and date in… thanks Tableau!

Resources

The data for this analysis was donated by the kind people at Towncharts.com. They were nice enough to provide a csv file of population data that was already pre-cleaned which let us get right to the analysis. Thank you Towncharts!
