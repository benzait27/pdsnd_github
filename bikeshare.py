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
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    print('Would you like to see data for Chicago, New York City or Washington ?')
    city_list = ["Chicago","New York City","Washington"]
    city = input()
    
    # In case the user does not enter the correct word
    while city.title() not in city_list : 
            city =  input("Please enter one of the following answers: 'Chicago','New York City','Washington'")
    
    # TO DO: get user input for time filter (all, january, february, ... , june)
    time_filter_list = ["Month","Day","Both","None"]
    time_filter = input('Would you like to filter data by month, day, both or not at all? type none for no time filter')
    
    # In case the user does not enter the correct word
    while time_filter.title() not in time_filter_list :
        time_filter = input("Please enter one of the following answers: 'Month','Day','Both','None'")

    # Initialise variable    
    month = 'None'
    day = 'None'
    
    # Get user input for month (january, february, ... , june)
    if time_filter.title() in ['Both','Month'] :
        month_filter_list = ["January", "February","March","April","May", "June"] 
        month = input('which month ? January, February , March, April, May or June')
        
        # In case the user does not enter the correct word    
        while month.title() not in month_filter_list :
            month = input("Please enter one of the following answers: 'January', 'February','March','April','May', 'June'")
    
   # Get user input for day of week (monday, tuesday, ... sunday)
    if time_filter.title() in ['Both','Day'] :
        day_filter_list = ['1','2','3','4','5','6','7']
        day = input('which day ? please type your response as an integer (e.g., 1=Sunday)')
        
        # In case the user does not enter the correct word       
        while day not in day_filter_list :
            day = input("Please enter one of the following answers: '1','2','3','4','5','6','7'")
    
    
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.title()])
    
    # here to get the original dataframe, we need it when we display the rows
    df_original = pd.read_csv(CITY_DATA[city.title()])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month.title() != 'None':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month.title()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'None':
        # filter by day of week to create the new dataframe
        days =  ['1','2','3','4','5','6','7']
        day = (days.index(day) + 6 ) % 7
        df = df[df['day_of_week'] == day]

    return df , df_original


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    # Display the most common month
    df['month'] = df['Start Time'].dt.month
    
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('\nThe most popular month for traveling is:',popular_month)
    
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    # Display the most day of week
    start_time = time.time()
    
    # extract day from the Start Time column to create an day of week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # find the most popular day
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day for traveling is:',popular_day)
    
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    # Display the most common start hour
    start_time = time.time()
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour for traveling is',popular_hour)
 
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    # find the most popular Start Station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most popular Start Station for traveling is:', popular_start_station)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    start_time = time.time()
    # Display most commonly used end station
    # find the most popular end Station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most popular End Station for traveling is:',popular_end_station)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    start_time = time.time()
    # Display most frequent combination of start station and end station trip
    df["Combination Station"] = "("+df["Start Station"]+")" +" and  ("+ df["End Station"] +")"
    popular_combination_station = df['Combination Station'].mode()[0]
    print('\nThe most popular combination station for traveling is:',popular_combination_station)

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    
    # Calculate the total duration 
    df['total duration'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    total_duration = df['total duration'].sum()
    print('\nThe total travel time is:',total_duration)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    start_time = time.time()
    # Display mean travel time
    mean_travel_time = total_duration / df['total duration'].count() 
    print('\nThe average time spent on each trip is:', pd.Timedelta(mean_travel_time, unit='ns'))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nThe breakdonw of users is:\n',df['User Type'].value_counts())
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    start_time = time.time()
    # Display counts of gender
    if 'Gender' in df :
        print('\nThe breakdonw of gender is:\n',df['Gender'].value_counts())
    
    #In case there is no "Gender" column. 
    else:
        print('\nThe breakdonw of gender is:')
        print('No gender data to share\n')
    
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    start_time = time.time()    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df :
        print('\nThe most earliest year of birth is:',df['Birth Year'].min())
        print('\nThe most recent year of birth is:',df['Birth Year'].max())
        print('\nThe most common  year of birth is:',df['Birth Year'].mode()[0])
    #In case there is no "Birth Year" column. 
    else:
        print('The most earliest year of birth is:')
        print('No birth year data to share\n')
        
        print('The most recent year of birth is:')
        print('No birth year data to share\n')
        
        print('The most common year of birth is:')
        print('No birth year data to share')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_rows(df):
    
    """Displays rows of bikeshare trips."""
    
    print("Would you like to view individual trip data ? type 'Yes' or 'No'")
    response = input()
    first_row = 0
    last_rows = 5
    number_of_rows = len(df.index)
    
    # In case the user does not enter the correct word
    while response.title() not in ['Yes','No']:
           print("Please enter one of the following answers: 'Yes','No'")
           response =  input()
      
    # Display the 5 rows until the user enter 'No'
    while response.title() == 'Yes' :
        
        #To avoid end of data 
        if last_rows > number_of_rows:
           last_rows = number_of_rows 
        
        print(df.iloc[first_row:last_rows,:])
        first_row = last_rows
        last_rows += 5
        print("Would you like to view individual trip data ? type 'Yes' or 'No'")
        response = input()
        # In case the user does not enter the correct word
        while response.title() not in ['Yes','No']:
            print("Please enter one of the following answers: 'Yes','No'")
            response =  input()    

            
def main():
    while True:
        city, month, day = get_filters()
        df, df_original = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df_original)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        # In case the user does not enter the correct word
        while restart.title() not in ['Yes','No']:
            print("Please enter one of the following answers: 'Yes','No'")
            restart =  input()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
