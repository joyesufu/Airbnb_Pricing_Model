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

After examining the data, we noticed that there was an extensive amount of outliers that affected that data, especially when it came to the average price of an Airbnb listing. These outliers were not included in the model because most of these price outliers are located in Manhattan, NY where Airbnb prices are significantly higher to the point only those in the top 3%-5% could afford it. Another noticeable outlier was the number of bedrooms for each Airbnb listing. Based on the graph below, the price of an Airbnb decreases significantly after to bedrooms, which we thought was odd. For instance, the price drops drastically for an 11 bedroom Airbnb, but then skyrockets when the number of bedrooms reaches 14. Due to the fact that almost all Airbnbs will not have that many rooms, we deemed it necessary not to include anything over 10 bedrooms in the model.


Dataframe(from Jupyter Notebook):

![dataframe](./images/Outlier_Removal.PNG)


Average Price and Bedrooms Graph:

![bedrooms](./images/AveragePrice_and_Bedrooms.PNG)

<a name="flask"></a>
### Flask Application

<a name="airbnb_html"></a>
### Airbnb Home Page

For the creation of the the web page we designed a layout that matched Airbnb's company colors, which was completed through bootstrap. Different tabs were created at the top left corner of the page to take viewers of the page directly to the location on the web page of the selected tab. Under this, there is little slideshow of pictures to add more professionalism, and beneath that are the pictures of the creators of this project. As a viewer works their way down the page they will see a brief description about the project along with the methodology, analysis, visuals, model, and features used. To give a viewer a more interactive experience at the very bottom of the page there is a section labeled "Try It", which allows the viewer to select certain features they would like for an Airbnb to have and after doing so a predictive price is generated based on the features choosen.


![web1](./images/Web_Page_1.PNG)


![web2](./images/Web_Page_2.PNG)


![web3](./images/Web_Page_3.PNG)


<a name="scatter_plot"></a>
### Scatter Plot

The scatter plot below displays the relationship between Airbnb prices and the number of reviews. Based on the plot, it could be assumed that the more expensive a property is listed for the less reviews it will have. A reason for this is that more expensive properties tend to price out the majority of the population because most people could not afford them, therefore there will be less reviews because only a small percentage of people can give a valid review. Another noticable feature of the plot is the color range which shows any reviews less than 20 as a light purple color and any reviews over 20 as a dark pink color.

![scatter](./images/Scatter_Plot.PNG)

<a name="box_plot"></a>
### Box Plot

<a name="heat_map"></a>
### Heat Map

<a name="conc"></a>
### Conclusion
