import matplotlib.pyplot as plt # visulization library , which is used to plot thr graph
X = [1, 2, 3, 4]
Y = [5, 6, 7, 8]
plt.plot(X, Y)
#plt.show()

#functions in matplotlib
# title - xlabel - y label - legend
movies = ['don','par hera pheri','3 idiots','pk']
revenue = [100, 150, 200, 250]
year = [2006, 2000, 2009, 2014]
plt.plot(year, revenue)
plt.title('Revenue of movies')
plt.xlabel('Year')
plt.ylabel('Revenue in crores')
#plt.show()


#multiple dataset on line plot
oscar_movies = ['don','par hera pheri','3 idiots','pk']
revenue = [100, 150, 200, 250]
year = [2006, 2000, 2009, 2014]
non_oscar_movies = ["sura","bahubali","emoji","love express"]
revenue_ns =[200,110,190,260]
plt.plot(year,revenue)
plt.plot(year,revenue_ns)
plt.show()