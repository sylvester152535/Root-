import unittest
import  Root
#Sylvester Amponsah   10/7/2018
class TestRoot(unittest.TestCase):

    def setUp(self):
            self.testArray = ['Dan', 'Bob', 'Alex', 'Zellinger', 'Dan']
            self.testArray1 = ['Dan', 'Bob', 'Bob', 'Zellinger', 'Dan']
            self.testArray2 = ['Dan', 'Bob', 'Bob', 'Zellinger', 'Dan', 'Bob']
            self.dict = {41:"Alex: 41 miles @ 33 mph", 38: "Dan: 38 miles @ 4 mph", 0:"Bob: 0 miles" }
            self.timesAA = ['07:15','07:45','06:12','06:32','12:01','13:16']
            self.names = ['Dan', 'Dan', 'Alex','Bob']
            self.miles = [17.3, 21.8, 42.0]
            self.times = ['07:15', '07:45', '06:12', '06:32','12:01', '13:16']
            self.dict1 = {41:"Alex: 41 miles @ 33 mph",  3:"Bob: 0 miles", 38: "Dan: 38 miles @ 46 mph",  }

    def tearDown(self):
        pass

    #this method takes the extracted string format times in the file, calculates durations and converts time to
    def test_timeOperation(self):
        result = Root.timeOperation(self.timesAA)
        self.assertEqual(result, [1800.0,1200.0,4500.0])

    #sorts the stored data in the dictionary and prints each line
    #sortDictResult has no return statement so it returns None
    def test_sortDictResult(self):
        self.assertIsNone(Root.sortDictResult(self.dict))

    ## Checks and return index of duplicated items. This simple brute force approach only works for one duplication
    ## A more robust method for a large dataset will be introduced in the readme file
    def test_duplicity(self):
        self.assertEqual(Root.duplicity(self.testArray), [0,4])
        self.assertNotEqual(Root.duplicity(self.testArray2), [0,4,1,2,5])

    #this method tests names from the Driver command that registered no trips
    def test_peopleWithZeroMiles(self):
        self.assertEqual(Root.peopleWithZeroMiles(self.testArray, self.testArray1), ['Alex'])
    #takes name, miles, and time array inputs and return a dictionary
    def test_calOperation(self):
        self.assertEqual(Root.calOperation(self.names, self.miles, self.times), self.dict1)
    #takes file as input and returns a sorted dictionary
    def test_lineOperation(self):
        file = open('test1.txt', "r")
        #linebyline = "Alex: 41 miles @ 34 mph", "Dan: 39 miles @ 47 mph", "Bob: 0 miles"
        self.assertEqual(Root.lineOperation(file), 'None')


if __name__ == '__main__':
    unittest.main()
