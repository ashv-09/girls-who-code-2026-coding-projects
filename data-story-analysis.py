# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
# print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# plt.scatter(lwd["year"],lwd["ED_litt_p"],color="cyan")
plt.title("Percent of Women Who are Literate over Time")
plt.xlabel("Year")
plt.ylabel("Women who are literate (%)")
plt.ylim(0,110)
plt.show()


listOfCountries = lwd["country_name"].unique()
# print(util.vformat_list(listOfCountries))


oneCountryBooleanList = lwd["country_name"] == "Senegal"
# print(oneCountryBooleanList)


oneCountryData = lwd.loc[oneCountryBooleanList]
# print(oneCountryData)


plt.scatter(x="year", y="ED_litt_p", data=oneCountryData)
plt.ylim(0,110)
plt.show()


# Story -----------------------------------------------------

print("\n\n")
print("Setting: \n")
print("My country is located on the continent of Africa and has a population of 19.4 million people as of 2026. \n")
print("Africa is known to generally have lower literacy rates in comparison to the rest of the world due to colonization, imperialism, lack of resources, and possibly geographical reasons. \n")
print("Africa as a continent has improved in terms of their exposure to the outside world and intra-continent development with increasing education opportunities, urbanization, technological advancement, and gender rights advocacy. \n")

input("Press return to continue. \n")


print("Characters: \n")
print("My data represents the literacy of women in Senegal from 1990 to 2020. \n")
print("Historically, women have always been restricted to the same opportunities and rights that men are presented with. In Africa, this trend has generally been more severe. Because of this, women literacy rates have taken longer to rise in this country compared to a country like the United States or a European country. \n")
print("Existing gender and familial norms, such as women being the main caretaker and domestic supporter of a household, may have also led women to consider the opportunity of education to be of less importance than those responsibilities. \n")

input("Press return to continue. \n")

print("Context: \n")
print("In the data from the graph, there is a sudden visible decrease in the literacy rates of women in Senegal from 1997 to 2005. Further research revealed that the reason for the literacy rates to remain low during these times may have been caused by geographical isolation, low retention in schools, and language barriers since a lot of programs were French missionary style. \n")
print("Another reason for the decrease in literacy is dependence on external funding (and the volatility of it) and budget cuts within the country. \n")
print("Gender norms continued to play a dominant role in the subject of women literacy, with girls often being pulled out of school to help with domestic and agricultural work. \n\n")

print("Research Question: How have changes in access to education affected women's literacy rates in Senegal from 1990 to 2020?")
