import pandas as pd
import numpy as np

# Replaced (England, Scotland, Wales, N.Ireland) with UK
data = pd.read_csv("filtered-openipf-2022-11-26-2.csv", low_memory=False) # All Raw + 3lift + international fed (IPF,African,Asian,EPF,FESUPO,NAPF,ORPF,Commonwealth)

countryList = ['USA', 'Sweden', 'India', 'New Zealand', 'Australia',
        'Canada', 'Sri Lanka', 'South Africa', 'Nauru',
        'Trinidad and Tobago', 'Guyana', 'Ireland', 'UK', 'Peru', 'Colombia',
        'Costa Rica', 'US Virgin Islands', 'Puerto Rico', 'Mexico', 'Uruguay',
        'Ecuador', 'Chile', 'Argentina', 'Austria', 'Russia', 'Germany', 'Slovenia',
        'Brazil', 'Philippines', 'Taiwan', 'Japan', 'Poland', 'Iran',
        'Kazakhstan', 'UAE', 'Lebanon', 'Mongolia', 'Singapore', 'Uzbekistan',
        'Morocco', 'Algeria', 'Egypt', 'Libya', 'France', 'Finland', 'Georgia', 'Spain',
        'Hungary', 'Belarus', 'Czechia', 'Netherlands', 'Estonia', 'Slovakia',
        'Denmark', 'Latvia', 'Lithuania', 'Romania', 'Norway', 'Belgium', 'Iceland',
        'Italy', 'Bulgaria', 'Ukraine', 'Switzerland', 'Turkey'] # countries with => 30 data points

searchColumns = ['Squat1Kg','Squat2Kg','Squat3Kg',
                'Bench1Kg','Bench2Kg','Bench3Kg',
                'Deadlift1Kg','Deadlift2Kg','Deadlift3Kg']

def countMadeLifts(country):
    totalMadeLifts = 0
    unreportedCount = 0
    countryData = data[(data['Country'] == country)]
    for lifter in countryData.index:
        lifterMadeLifts = 0
        for column in searchColumns:
            if (countryData[column][lifter] > 0):
                lifterMadeLifts += 1
        if lifterMadeLifts == 0:
            unreportedCount += 1
        totalMadeLifts += lifterMadeLifts
    lifters = len(countryData.index) - unreportedCount
    return (round(totalMadeLifts / lifters, 2), lifters)

dict = {country : countMadeLifts(country) for country in countryList} # create dictionary
dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])} # sort dictionary

for country in dict:
    print(country, dict[country])
