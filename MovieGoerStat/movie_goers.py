##basic stats from SY2005

import pandas as pd

movie_goers = pd.read_csv("MovieGoerData.csv")
cairns_movie_goers = movie_goers.loc[movie_goers['Location'] == 'Cairns']
townsville_movie_goers = movie_goers.loc[movie_goers['Location'] == 'Townsville']


average_salary = movie_goers['Salary Per Annum'].mean()
print(f' The median salary for all movie goers is {average_salary}')

median_salary = movie_goers['Salary Per Annum'].median()
print(f' The median salary for all movie goers is {median_salary}')

std_deviation_salary = movie_goers['Salary Per Annum'].std()
print(f' The standard deviation for all movie goers salary is {std_deviation_salary}')

##geni_coefficient