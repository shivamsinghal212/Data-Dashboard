# Data-Dashboard
This is a dashboard integrated with datatables and highcharts for visualization of data.

**Instructions to run application:**
**Use Virtualenv**
1. pip install django **(Django>2.0)**
2. python manage.py makemigrations **(Output: No changes detected)**
3. python manage.py migrate 
4. python manage.py loaddata fixtures.json **(Load data into database)**
5. python manage.py runserver

**Features:**
1. You can use the legend on the graph to switch between "Intensity, relevance and Likelihood"
2. Data is displayed in the form of tables below the graph.
3. One property can be selected at once between **Sector, Topic, Region, Pestle, Year **

**Upcoming Features:**
1. Click on the node in the graph to get it details.
2. Removal of "Go" button to make it more dynamic.
3. Improved UI

![alt text](https://github.com/shivamsinghal212/Data-Dashboard/blob/master/dashboard.PNG)

