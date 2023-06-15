# PostgresDB_SQLAlchemy- Vacation Climate Analysis and Flask API Creation

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.
Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:
1.	Use the SQLAlchemy create_engine() function to connect to your Postgres database.
2.	Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
3.	Link Python to the database by creating a SQLAlchemy session.
4.	 Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
Precipitation Analysis
1.	Find the most recent date in the dataset.
2.	Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3.	Select only the "date" and "prcp" values.
4.	Load the query results into a Pandas DataFrame. Explicitly set the column names.
5.	Sort the DataFrame values by "date".
6.	Plot the results by using the DataFrame plot method, as the following image shows:

![image](https://github.com/esu75/PostgresDB_SQLAlchemy/assets/118146659/737212f1-8c60-4b44-a148-5b788ab44aed)


10.	Use Pandas to print the summary statistics for the precipitation data.
