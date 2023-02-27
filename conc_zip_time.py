"""This program identifies unique zipcode and times of day in the
_cross_table_statistics function. It uses the display cross table
function to print a table that shows a table of all various combinations
in the data set. Based on user input, the program will display the
average, minimum or maximum concentration of the combinations.
"""
from enum import Enum


class Stats(Enum):
    """Establishes a value for minimum, average and maximum to be
    accessed in other functions for better code readability. """
    MIN = 0
    AVG = 1
    MAX = 2


class NoMatchingItems(Exception):
    """Create exception class when data does not match both
    descriptors
    """
    pass


class EmptyDatasetError(Exception):
    """Create exception class when no data is loaded"""
    pass


class DataSet:
    """Establish a class to create new instance attributes"""

    def __init__(self, header: str = ""):
        """Defines header and data parameter that is used in other
        functions
        """
        self._data = None
        self.header = header
        self._zips = []
        self._times = []

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, _header: str):
        if len(_header) <= 30:
            self._header = _header
        else:
            raise ValueError

    def _initialize_labels(self):
        """create a unique zip list and time list for to be used in
        making a cross table.
        """
        temp_zip = set()
        temp_time_of_day = set()

        for item in self._data:
            temp_zip.add(item[0])
            temp_time_of_day.add(item[1])

        zip_list = list(temp_zip)
        time_list = list(temp_time_of_day)
        self._zips = zip_list
        self._times = time_list

    def _cross_table_statistics(self, descriptor_one: str, descriptor_two: str):
        """Matches the zipcode and time of day with loaded data and
        prints minimum, average and maximum concentration of matched
        rows.
        """
        if self._data is None:
            raise EmptyDatasetError
        my_list = []
        for item in self._data:
            if descriptor_one == item[0] and descriptor_two == item[1]:
                my_list.append(item[2])
        if my_list:
            return min(my_list), sum(my_list) / len(my_list), max(my_list)
        else:
            raise NoMatchingItems

    def load_default_data(self):
        self._data = [("12345", "Morning", 1.1), ("94022", "Morning", 2.2),
                      ("94040", "Morning", 3.0), ("94022", "Midday", 1.0),
                      ("94040", "Morning", 1.0), ("94022", "Evening", 3.2)]
        self._initialize_labels()

    def display_cross_table(self, stat: Stats):
        """Displays a table with all combinations of zipcode and time
        of day in the loaded data. Based on user input, it will display
        show average, minimum or maximum of these combinations.
        """
        try:
            print(f"{self._times[0]:>15}{self._times[1]:>8}{self._times[2]:>8}")
            for zipcode in self._zips:
                data = []
                for time in self._times:
                    try:
                        value = self._cross_table_statistics(zipcode, time)[
                            stat.value]
                        data.append(value)
                    except NoMatchingItems:
                        data.append("N/A")
                print(f"{zipcode}{data[0]:>10}{data[1]:>8}{data[2]:>8}")
        except EmptyDatasetError:
            print("please load the data.")


def main():
    """Obtain the user's name and user's desired header."""
    my_set = DataSet()
    try:
        my_set._cross_table_statistics("12345", "Morning")
    except EmptyDatasetError:
        print("Empty data set: Pass")
    my_set.load_default_data()
    try:
        my_set._cross_table_statistics("94040", "Morning")
    except EmptyDatasetError:
        print("Empty data set: Pass")
    except NoMatchingItems:
        print("No Matching Items: Pass")

    user_name = input("What is your name? ")
    print("Greetings", user_name + ", it is a pleasure to meet you!")
    print("")
    purple_air1 = DataSet()
    while True:
        try:
            name = input("Enter Header ")
            purple_air1.header = name
            if purple_air1.header == name:
                break
        except ValueError:
            print("Invalid Header. Please enter a header less than 30 "
                  "characters long")
            continue

    menu(purple_air1)


def print_menu():
    """Gives list of items for user to choose from"""
    print("1. Print Average Particulate Concentration by Zip Code and Time")
    print("2. Print Minimum Particulate Concentration by Zip Code and Time")
    print("3. Print Maximum Particulate Concentration by Zip Code and Time")
    print("4. Adjust Zip Code Filters")
    print("5. Load Data")
    print("9. Quit")


def menu(my_dataset: DataSet):
    """Prints header based on user input. Afterwards, it will print a
    menu to obtain user's preferred choice and respond with
    various statements based on their input.
    """

    while True:
        print(f"{my_dataset.header}")
        print_menu()
        user_choice = input("Which is your choice? ")
        try:
            int_answer = int(user_choice)
            print("You chose", int_answer)
        except ValueError:
            print("Please only enter an integer")
            continue
        if int_answer == 9:
            print("Goodbye. Thank you for using the Database")
            break
        elif int_answer == 1:
            my_dataset.display_cross_table(Stats.AVG)
        elif int_answer == 2:
            my_dataset.display_cross_table(Stats.MIN)
        elif int_answer == 3:
            my_dataset.display_cross_table(Stats.MAX)
        elif int_answer == 5:
            my_dataset.load_default_data()
        elif 0 < int_answer < 6:
            print("Option", int_answer, "is not implemented yet")
        else:
            print("Option", int_answer, "is not in the menu. Please select an "
                                        "option on the menu")


if __name__ == "__main__":
    main()

"""
---Sample Run---
Empty data set: Pass
What is your name? Bryce
Greetings Bryce, it is a pleasure to meet you!

Enter Header What a fabulous program
What a fabulous program
1. Print Average Particulate Concentration by Zip Code and Time
2. Print Minimum Particulate Concentration by Zip Code and Time
3. Print Maximum Particulate Concentration by Zip Code and Time
4. Adjust Zip Code Filters
5. Load Data
9. Quit
Which is your choice? 5
You chose 5
What a fabulous program
1. Print Average Particulate Concentration by Zip Code and Time
2. Print Minimum Particulate Concentration by Zip Code and Time
3. Print Maximum Particulate Concentration by Zip Code and Time
4. Adjust Zip Code Filters
5. Load Data
9. Quit
Which is your choice? 1
You chose 1
        Evening  Midday Morning
12345       N/A     N/A     1.1
94040       N/A     N/A     2.0
94022       3.2     1.0     2.2
What a fabulous program
1. Print Average Particulate Concentration by Zip Code and Time
2. Print Minimum Particulate Concentration by Zip Code and Time
3. Print Maximum Particulate Concentration by Zip Code and Time
4. Adjust Zip Code Filters
5. Load Data
9. Quit
Which is your choice? 2
You chose 2
        Evening  Midday Morning
12345       N/A     N/A     1.1
94040       N/A     N/A     1.0
94022       3.2     1.0     2.2
What a fabulous program
1. Print Average Particulate Concentration by Zip Code and Time
2. Print Minimum Particulate Concentration by Zip Code and Time
3. Print Maximum Particulate Concentration by Zip Code and Time
4. Adjust Zip Code Filters
5. Load Data
9. Quit
Which is your choice? 3
You chose 3
        Evening  Midday Morning
12345       N/A     N/A     1.1
94040       N/A     N/A     3.0
94022       3.2     1.0     2.2
What a fabulous program
1. Print Average Particulate Concentration by Zip Code and Time
2. Print Minimum Particulate Concentration by Zip Code and Time
3. Print Maximum Particulate Concentration by Zip Code and Time
4. Adjust Zip Code Filters
5. Load Data
9. Quit
Which is your choice? 9
You chose 9
Goodbye. Thank you for using the Database

Process finished with exit code 0

"""
