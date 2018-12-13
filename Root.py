#Sylvester Amponsah 10/7/2018

import re
import datetime

file = open('test1.txt', "r")

#this method takes the extracted times from names with trips, performs
# subtraction to get trip duration then converts the result to seconds and saves
# them in an array. I used arrays here for their easy access using their indices
# since I will be looping through multiple arrays in a later method to construct strings
# for each Driver
def timeOperation(drivenTime2):
    durationArray = []
    for x in range(0, len(drivenTime2)-1, 2):
        #converts string objects in the array into time objects
        time2 = datetime.datetime.strptime(drivenTime2[x], '%H:%M')
        time3 = datetime.datetime.strptime(drivenTime2[x+1], '%H:%M')
        #calculates time dureation and converts to seconds
        durationInSeconds = (time3 - time2).total_seconds()
        durationArray.append(durationInSeconds)
    return durationArray

#this method sorts the dictionary using their key, which is the total miles traveled
#I used sorted here which collects the list iterable it receives into a list and sort the list using timsort with O(NlogN) complexity worst case
def sortDictResult(dicts):
    sorted_dicts = sorted(dicts.items(), key = lambda t: t[0], reverse = True)
    for key in sorted_dicts:
         keyy = str(key)
         beg = keyy.index('\'')
         end = keyy.index(')')
         print(keyy[beg+1:end-1])

#For this simple case, this brute force approach works but for a large set of data this method would be highly inefficient
# O(n^2) worst case time complexity performance
def duplicity(driverNames):
    duplicateIndex = []
    for i in range(len(driverNames)):
        for j in range(i+1, len(driverNames)):
            if driverNames[i] == driverNames[j]:
                duplicateIndex.append(i)
                duplicateIndex.append(j)
                return duplicateIndex

#this method takes care of names that appear in the Driver command but do not register trips
def peopleWithZeroMiles(sample, driverNames):
    uniq = []
    something = []
    for item in sample:
        if item not in driverNames:
            uniq.append(item)
            return uniq

#Arrays serves best as function parameters for the sort of manipulations performed on the data
#However the data is stored in a dictionary to reduce time complexity of sorting later on
def calOperation(allNames, drivenMiles, drivenTimes):
    difference = len(allNames)-len(drivenMiles)
    #takes care of names that registered no trips
    drivenMiles+=[0]*difference
    #tempTime stores the result of the time operations (seconds) in an array
    tempTime = timeOperation(drivenTimes)
    #corresponding times to names with no trips, 3600 to avoid to avoid division by zero integer, this works since corresponding milages have already been set to zero
    tempTime+=[3600]*difference
    #duplicateIndex stores the index of duplicate items
    duplicateIndex = duplicity(allNames)
    #if there are duplicates, we add the relevant data to the second dupliated item and pop the index of the first duplicated item
    dicts = {}
    if duplicateIndex != None:
        drivenMiles[duplicateIndex[1]] += drivenMiles[duplicateIndex[0]]
        tempTime[duplicateIndex[1]] += tempTime[duplicateIndex[0]]
        tempTime.pop(duplicateIndex[0])
        allNames.pop(duplicateIndex[0])
        drivenMiles.pop(duplicateIndex[0])
        #loop goes through the arrays and assemble the data in the required format
        for j in range(len(tempTime)):
            durationInSeconds = tempTime[j]
            drivenMilesPerPerson = drivenMiles[j]
            name = allNames[j]
            durationInHours = durationInSeconds / 3600
            mph = int(drivenMilesPerPerson/durationInHours)
            totalMileDriven = int(mph * durationInHours)
            #conditional statement assings 0 to mph's less than 5 or greater than 100 and reduces their orginial dictionary key for sorting later on
            if mph > 5 and mph < 100:
                dicts[totalMileDriven] = str(name) + ": " + str(totalMileDriven) + " miles @ " + str(mph) + " mph"
            else:
            #what happens to the key of average mph greater than 100? for sorting purposes
                totalMileDriven = 5-j
                dicts[totalMileDriven] = str(name) + ": " + str(0) + " miles"
    else:#if there are no duplicated items
        for i in range(len(tempTime)):
            durationInSeconds = tempTime[i]
            drivenMilesPerPerson = drivenMiles[i]
            name = allNames[i]
            durationInHours = durationInSeconds / 3600
            mph = int(drivenMilesPerPerson/durationInHours)
            totalMileDriven = int(mph * durationInHours)
            if mph > 5 and mph < 100:
                dicts[totalMileDriven] = str(name) + ": " + str(totalMileDriven) + " miles @ " + str(mph) + " mph"
            else:
                #what happens to the key of average mph greater than 100? for sorting purposes
                totalMileDriven = 5-i
                dicts[totalMileDriven] = str(name) + ": " + str(0) + " miles"
    return dicts

#lineOperation method extracts relevant data (Names, milages, and times) from the input file and stores them in a separate array.
#Since sortDictResult doesn't have a return, lineOperation has to go in the print statement for the output to be on console 
def lineOperation(file):
    namesArray = []
    milesArray = []
    timesArray = []
    zeroMilesNames = []

    for line in file:

        names = re.compile(r'[A-Za-z]{2,25}||\s[A-Za-z]{2,25}')
        namm = line.split('Trip')
        driverNammes = names.findall(str(namm))
        zeroMilesNames.append(driverNammes[4])
        sample = zeroMilesNames[0:int(len(zeroMilesNames)/2)]

        if 'Trip' in line:
            #python literal expression is used to specifically select time, milage, and name data
            times = re.compile(r'\d+:\d+')
            miles = re.compile(r'\d+\.\d+')

            nam = line.split('\rTrip')

            num = line.split()

            drivenTimes = times.findall(str(num))
            drivenMiles = miles.findall(str(num))
            driverNames = names.findall(str(nam))
            namesArray.append(driverNames[4])
            milesArray.append(float(drivenMiles[0]))
            timesArray.append(drivenTimes[0])
            timesArray.append(drivenTimes[1])
            #the array of values are then passed onto calOperation which returns a dictionary
    uniqNames = peopleWithZeroMiles(sample, namesArray)
    #add names with trips to names without trips
    allNames = namesArray + ([], uniqNames)[uniqNames != None]
    dicts = calOperation(allNames, milesArray, timesArray)

    #The returned dictionary values are then sorted and pinted on the console
    return str(sortDictResult(dicts))

print(lineOperation(file))
file.close()
