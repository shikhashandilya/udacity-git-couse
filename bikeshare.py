import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city name:").lower()
    while city not in CITY_DATA.keys():
        city = input("Please select from provided options (chicago/new york city/washington):").lower()     

    # TO DO: get user input for month (all, january, february, ... , june)
    mon = ['all','january', 'february', 'march', 'april', 'may', 'june']
    month = input("Enter month:").lower()
    while month not in mon:
         month = input("Enter any month from january to june or all:").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week: ").lower()
    while day not in ['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input("Enter day of week(mon-sun) or all: ").lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    # extract month and day of week from Start Time to create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    
    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
    #filter by month to create new dataframe
    df = df[df['month'] == month]   

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("Most common month is:", common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("Most common day of week is:", common_day_of_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print("Most common start hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displaying statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).count().idxmax()
    print("Most frequest combination of start station and end station is {} & {} ".format(most_common_start_and_end_stations[0][0],most_common_start_and_end_stations[0][1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60.0
    print("Total travel time in hours is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60.0
    print("Mean travel time in hours is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    #Washington data does not have Gender and Birth Year columns.
    if city != 'washington':
    
        # TO DO: Display counts of gender
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("Earliest year of birth is:",df['Birth Year'].min())
        print("Most recent year of birth is:",df['Birth Year'].max())
        print("Most common year of birth is:",df['Birth Year'].value_counts().idxmax())
        
    else:
        print("Washington data does not have Gender and Birth Year columns.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    row = 0
    while True:
        view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no\n') 
        if view_data.lower() == 'yes':
            print(df.iloc[row : row+5])
            row = row + 5
        elif view_data.lower() == 'no':
            break
        else:
            print("Invalid input. Please try again")
   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart your search? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
