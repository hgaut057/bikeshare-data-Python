import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHi There! Here, we will explore some of the US bikeshare data. Let\'s get started shall we?')
    # get user input for city (chicago, new york city, washington).


    while True:
        city = input("\To get started, please type in the name of the city would you like to filter for? (New York City, Chicago or Washington?)\n")
        city = city.title()
        if city not in ('Chicago', 'New York City', 'Washington'):
            print("I don't understand. Please Try again.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nWhich month would you like to filter for? (January, February, March, April, May, June or type 'all')\n")
        month = month.title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("Invalid Response. Try again.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Are you looking to filter through a specfic day? If yes, please select one of the following days, otherwise please select 'all':( Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all').\n")
        day = day.title()
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("Invalid day. Try again.")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # loading data file into the DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filtering by month if available
    if month != 'all':
   	 	# using the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filtering by month to create the new DataFrame
        df = df[df['month'] == month]

        # filtering by day of week if available
    if day != 'all':
        # filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]
    print('The Most Common Month:', popular_month)


    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('The Most Common day:', popular_day)



    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('The Most Commonly used start station:', Start_Station)


    # display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe Most Commonly used end station:', End_Station)


    # display most frequent combination of start station and end station trip

    Combine_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe Most Commonly used pair of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    Total_Travel_Time = df['Trip Duration'].sum()
    print('The Total travel time:', Total_Travel_Time/86400, " Days")


    # display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types_count = df['User Type'].value_counts()
    #print(user_types)
    print('User Counts:\n', user_types_count)

    # Display counts of gender

    try:
      gender_count = df['Gender'].value_counts()
      print('\nGender Counts:\n', gender_count)
    except KeyError:
      print("\nGender Counts:\nNo data available.")

    # Display earliest, most recent, and most common year of birth

    try:
      Earliest_Birth_Year = df['Birth Year'].min()
      print('\nEarliest Birth Year:', Earliest_Birth_Year)
    except KeyError:
      print("\nEarliest Birth Year:\nNo data available.")

    try:
      Most_Recent_Birth_Year = df['Birth Year'].max()
      print('\nMost Recent Birth Year:', Most_Recent_Birth_Year)
    except KeyError:
      print("\nMost Recent Birth Year:\nNo data available.")

    try:
      Most_Common_Birth_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Birth Year:', Most_Common_Birth_Year)
    except KeyError:
      print("\nMost Common Birth Year:\nNo data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    user_input = raw_input('Do you want to see the raw data? Please enter yes or no.\n')
    line_number = 0
    
    while 1 == 1:
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = raw_input('\nDo you want to see more of the raw data? Enter yes or no.\n')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
