# Project_4

## Background:

You probably have heard many success stories regarding people making a substantial amount of money posting their properties on Airbnb. To test the accuracy of these claims a machine learning model has been created to test whether or not the prices that are listed for Airbnbs are properly priced. Some of the property types that are being analyzed include: homes, apartments, hotels, etc. For this project different features will be analyzed to see whether or not they have either a positive, negative, or no affect on the price of the listing. New York City will be the topic of this particular project. The source of the data used for this project comes from Inside Airbnb.

## Technologies:

Python, Pandas, Sklearn, Matplotlib, Jupyter Notebook, HTML, CSS, Tableau 

## Contributors:

Ellen Grove, Joshua Yesufu, Anne Pizzini, Zach Meader

## Data Source:

New York City Airbnb data compiled using Inside Airbnb from

http://insideairbnb.com/get-the-data/

## Table of Contents:

1. [ Outlier Removal. ](#outlier)
2. [ Flask Application. ](#flask)
3. [ Airbnb Home Page/HTML. ](#airbnb_html)
4. [ Scatter Plot. ](#scatter_plot)
5. [ Box Plot. ](#box_plot)
6. [ Heat Map. ](#heat_map)
7. [ Conclusion. ](#conc)

<a name="outlier"></a>
### Outlier Removal

After examining the data, we noticed that there was an extensive amount of outliers that affected that data, especially when it came to the average price of an Airbnb listing. These outliers were not included in the model because most of these price outliers are located in Manhattan, NY where Airbnb prices are significantly higher to the point only those in the top 3%-5% could afford it. Another noticeable outlier was the number of bedrooms for each Airbnb listing. Based on the graph below, the price of an Airbnb decreases significantly after to bedrooms, which we thought was odd. For instance, the price drops drastically for an 11 bedroom Airbnb, but skyrockets to a price that is unaffordable to most people. Due to the fact that almost all Airbnbs will not have that many rooms, we deemed it necessary not to include anything over 10 bedrooms in the model.


Dataframe(from Jupyter Notebook)

![dataframe](./images/Outlier_Removal.PNG)


Average Price and Bedrooms Graph

![bedrooms](./images/AveragePrice_and_Bedrooms.PNG)

<a name="flask"></a>
### Flask Application

<a name="airbnb_html"></a>
### Airbnb Home Page

<a name="scatter_plot"></a>
### Scatter Plot

<a name="box_plot"></a>
### Box Plot

<a name="heat_map"></a>
### Heat Map

<a name="conc"></a>
### Conclusion
