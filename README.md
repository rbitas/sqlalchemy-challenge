# Sqlalchemy-challenge
homework for DataViz bootcamp
*NOTE: https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html this link was used to figure out the describe function and https://stackoverflow.com/questions/10998621/rotate-axis-text-in-matplotlib this link was used on how to rotate the text on the x- axis both of these can be found in climate.ipynb which is found in SurfsUp folder*

# Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

# Part 1: Analyze and Explore the Climate Data:

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib.

Precipitation Analysis:

Find the most recent date in the dataset.

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data

Select only the "date" and "prcp" values.

Load the query results into a Pandas DataFrame. Explicitly set the column names.

Sort the DataFrame values by "date".

Plot the results by using the DataFrame plot method

Use Pandas to print the summary statistics for the precipitation data.

Station Analysis

Design a query to calculate the total number of stations in the dataset.

Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

  List the stations and observation counts in descending order.
  Answer the following question: which station id has the greatest number of observations?

Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query

Design a query to get the previous 12 months of temperature observation (TOBS) data. 

# Part 2: Design Your Climate App:

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes
