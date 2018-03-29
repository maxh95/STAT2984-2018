# Assignment 4
# Introduction to numpy and visualization
# Due at 8am on March 29, 2018
import numpy as np
import sys
import matplotlib.pyplot as plt


# Question 1: (5 points)

#The column names are Name, Year, Max.Wind.Speed(kts), Central.Pressure(mb), Category

# All of the columns contain integers except for Name which contains strings

#wind speed and year are not missing any values, name is missing many and annotated as -----, pressure and category are
#missing some values and appear as blanks

# I replace the missing data points with -1 so that later on I can remove the index of the elements that correspond
# to the missing data

# some sort of regional break down would be nice to include, such as pacific or atlantic ocean in order to more easily
# see how hurricanes vary by location, granted one could look this information up but it would be nice if included



# Question 2: (5 points)

def read_data(file):
    # create an empty list to append a list of values for each key to
    name_list = []
    year_list = []
    maxwind_list = []
    pressure_list = []
    category_list = []

    #reads in the data
    datum = open(file, 'r').readlines()

    #gets the keys and removes unnecessary elements at the end
    datum[0] = datum[0][0:len(datum[0])-1]
    header = datum[0].split('\t')

    data_dict = {}
    # makes sure the end of of a list is not removed if there is no category for the storm
    lastLine = False
    for line in datum[1:]:
        if line[len(line)-1] == '\n':
            line = line[0:len(line)-1]
        else:
            lastLine = True
        value = [line for line in line.split('\t')]

        #appends a list for each column of data to the keys
        name = value[0]
        year = value[1]
        wind = value[2]
        pressure = value[3]

        # if the category is blank, append an empty string. helps deal with null values later
        if len(value) is 4:
            value.append("")
        category = value[4]

        #formats data
        name = name.strip()
        year = year.strip()
        pressure = pressure.strip()
        category = category.strip()

        # deals with missing values for each list and appends a float if the value is missing
        if name != "-----":
            name_list.append(name)
        if pressure != "":
            pressure_list.append(float(pressure))
        else:
            pressure_list.append(-1)
        if year != "":
            year_list.append(float(year))
        if category != "":
            category_list.append(float(category))
        else:
            category_list.append(-1)
        if wind != "":
            maxwind_list.append(float(wind))
        else:
           maxwind_list.append(-1)

    # makes the dictionary by assigning each relative list to its key
    data_dict['name'] = name_list
    data_dict['year'] = year_list
    data_dict['wind'] = maxwind_list
    data_dict['pressure'] = pressure_list
    data_dict['category'] = category_list

    return data_dict

filename = "hurricanes-2015.txt"
data = read_data(filename)



# Question 3: (10 points)
# create a function called 'summarize_data' to summarize the data
def summarize_data(data_in, columns_in, verbose = False):
    # for loop so I can calculate summary stats for multiple columns
    for column in columns_in:
        #make a numpy array to use numpy functions as a float
        data_np = np.array(data_in[column]).astype(np.float)
        a = np.mean(data_np)
        b = min(data_np)
        c = max(data_np)
        d = np.std(data_np)

        if verbose:
            print "Mean:", a
            print "Minimum:", b
            print "Maximum:", c
            print "Standard Deviation:", d
            if column == 'wind':
                print 'Max.Wind.Speed(kts)'
            elif column == 'pressure':
                print 'Central.Pressure(mb)'
            else:
                print 'Category'
            print "----------------------"
    # return values
    return a, b, c, d

columns=['wind','pressure','category']
data_summary = summarize_data(data, columns, verbose = True)



# Question 3: (10 points)
# create a boxplot of the maximum wind speed grouped by category
category_datas = data['category']
pressure_datas = data['pressure']

# make dictionary
dict_by_category = {}
# go through set of categories
for cat in set(data['category']):
    # create a new key for hurricane category
    dict_by_category[cat] = []

# for each windspeed
for i, win in enumerate(data['wind']):
    # append the windspeed to the dictionary by category of the storm
    dict_by_category[data['category'][i]].append(win)

# create an empty list to add data
data_empty = []
labels = []
for wind in sorted(dict_by_category, reverse=True):
    labels.append(str(wind) + ' Wind')
    data_empty.append(dict_by_category[wind])
#print data_empty[0:5]

# draw a boxplot displaying the windspeed (y-axis) and storm category (x-axis)

# create figure object
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(7, 8))
wind_category_boxplot = axes.boxplot(data_empty[0:5], vert=True, patch_artist=True)

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(data_empty[0:5]))], xticklabels=labels)

# add y-axis label
axes.set_ylabel('Max.Wind.Speed(kts)')
plt.title('Maximum Windspeed Grouped by Category', fontsize = 15)
#remove box from outside
axes.spines['top'].set_visible(False)
axes.spines['bottom'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['left'].set_visible(False)
# darker colors for more sever storms
colors = ['black', 'midnightblue', 'steelblue', 'lightsteelblue', 'whitesmoke']
for patch, color in zip(wind_category_boxplot['boxes'], colors):
    patch.set_facecolor(color)
axes.annotate('Outlier', xy=(3, 90)) #xytext=(3, 88), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()



# Question 4: (15 points)
# summarize the relationship between wind speed and central pressure

wind_data = data['wind']
pressure_data = data['pressure']

# removes the index in the list of pressure/wind data where there are missing pressure values
index = 0
while index < len(pressure_data):
    if pressure_data[index] < 0 or wind_data[index] < 0:
        pressure_data.pop(index)
        wind_data.pop(index)
    index = index + 1

#calculates correlation
correlation = np.corrcoef(pressure_data, wind_data)
print 'The Correlation between Central Pressure and Windspeed in our hurricane data is:', correlation[1]

#finds line of best fit through the data to add to plot
best_fit = np.polyfit(pressure_data, wind_data, 1)
line_for_graph = np.poly1d(best_fit)

#adds title labels and other features including the actual plot
plt.title('Relationship Between Hurricane Windspeed and Pressure', fontsize = 16)
plt.xlabel('Central.Pressure(mb)', fontsize = 16)
plt.ylabel('Max.Wind.Speed(kts)', fontsize = 16)
fig, line = plt.plot(pressure_data , wind_data, '.', pressure_data, line_for_graph(pressure_data), '-', c = 'midnightblue')
plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
line.set_color('red')
plt.show()



# Question 5: (15 points)
# Create a hypothesis to be tested over time.
# HYPOTHESIS: as category increases windspeed increases

category_info = data['category']
# removes the index in the list of category/wind data where there are missing pressure values. This following
# code makes sure the dimensions of the variables are the same in order to calculate correlation
ind = 0
while ind < len(category_info):
     if category_info[ind] < 0 or wind_data[ind] < 0:
        category_info.pop(ind)
        #wind_data.pop(ind)
     ind = ind + 1
category_resized = category_info.pop(-1)
hypothesis_correlation = np.corrcoef(wind_data, category_info)
print 'The Correlation between Storm Category and Windspeed in our hurricane data is:', hypothesis_correlation[1]

#calculates line of best fit
line_fit = np.polyfit(pressure_data, wind_data, 1)
linefit = np.poly1d(best_fit)

#adds title labels and other features including the actual plot
plt.title('Relationship Between Hurricane Windspeed and Storm Category', fontsize = 16)
plt.xlabel('Storm Category', fontsize = 16)
plt.ylabel('Max.Wind.Speed(kts)', fontsize = 16)
fig, line = plt.plot(category_info, wind_data, '.', category_info, linefit(category_info), '-', c = 'steelblue')
plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
line.set_color('orange')
plt.show()



# Question 6: (15 points extra credit + 10 points if selected winner)

dict_by_categ = {}
# go through set of categories
for cat in set(data['category']):
    # create a new key for hurricane category
    dict_by_categ[cat] = []

# for each pressure
for i, p in enumerate(data['pressure']):
    # append the pressure to the dictionary by category of the storm
    dict_by_categ[data['category'][i]].append(p)

# create an empty list to add data
press_empty = []
labelss = []
for press in sorted(dict_by_categ, reverse=True):
    labelss.append(str(press) + 'Pressure')
    press_empty.append(dict_by_categ[press])
#print press_empty[0:5]

figure, axs = plt.subplots(nrows=1, ncols=1, figsize=(9, 10))
pressure_category_boxplot = axs.boxplot(press_empty[0:5], vert=True, patch_artist=True)

# add x-tick labels
plt.setp(axs, xticks=[y+1 for y in range(len(press_empty[0:5]))], xticklabels=labels)

# add y-axis label
axs.set_ylabel('Central Pressure(mb)')
plt.title('Central Pressure Grouped by Category', fontsize = 15)
#remove box from outside
axs.spines['top'].set_visible(False)
axs.spines['bottom'].set_visible(False)
axs.spines['right'].set_visible(False)
axs.spines['left'].set_visible(False)
# darker colors for more severe storms
colors = ['black', 'midnightblue', 'steelblue', 'lightsteelblue', 'whitesmoke']
for patch, color in zip(pressure_category_boxplot['boxes'], colors):
    patch.set_facecolor(color)
#axs.annotate('Outlier', xy=(3, 90)) #xytext=(3, 88), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()


# From question four we learned that there is a negative relationship between hurricane windspeed and central pressure.
# In question three the boxplot showed that as category increased so did windspeed. To provide further evidence
# for the relationship observed, a boxplot of pressure grouped by category should show the opposite tren.

