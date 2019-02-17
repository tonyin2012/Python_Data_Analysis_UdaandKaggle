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

    def verifyinput(lst, str1):
        while str1 not in lst:
            if str1.isalpha():
                print("You didn't input a right string. ")
            else:
                print("You didn't input a string!")
            str1 = input("Try to input again:\n").lower()
        print('You chose {} to analyze!'.format(str1))
        return str1
    citylst = ['chicago', 'new york city', 'washington']
    monthlst = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    daylst = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    city = input("Choose a city to analyze：chicago, new york city, washington:\n").lower()
    city = verifyinput(citylst, city)
    month = input(
        "Choose a month or all months to analyze!\nYou can input like：all, january, february, ... , june\n").lower()
    month = verifyinput(monthlst, month)
    day = input(
        "Choose a day of week or all day to analyze!\nYou can input like：all, monday, tuesday, ... sunday\n").lower()
    day = verifyinput(daylst, day)
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    CommonMonth = df['month'].mode()[0]
    print("The most common month is:{}".format(CommonMonth))

    # TO DO: display the most common day of week
    CommonDayOfWeek = df['day_of_week'].mode()[0]
    print("The most common day of week is {}".format(CommonDayOfWeek))

    # TO DO: display the most common start hour
    CommonStartHour = df['Start Time'].dt.hour.mode()[0]
    print("The most common star hour is:{}".format(CommonStartHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    CommonStartStation = df['Start Station'].mode()[0]
    print("The most common Start Station is:{}".format(CommonStartStation))

    # TO DO: display most commonly used end station
    CommonEndStation = df['End Station'].mode()[0]
    print("The most common End Station is:{}".format(CommonEndStation))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + df['End Station']
    CommonTrip = df['Trip'].mode()[0]
    print("The most frequent Trip is:{}".format(CommonTrip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    def TimeConvert(time):
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        time = "{}h{}m{}s".format(h, m, s)
        return time
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TripTotalTime = df['Trip Duration'].sum()

    print("The total travel time is {}".format(TimeConvert(TripTotalTime)))

    # TO DO: display mean travel time

    MeanTime = df['Trip Duration'].mean()
    print("The mean travel time is {}".format(TimeConvert(MeanTime)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The user type is:\n{}".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if city == 'washington':
        print("Washington didn't have gender and birth info")
    else:
        print(df['Gender'].value_counts())
        Earliest_Birth = df['Birth Year'].min()
        Recent_Birth = df['Birth Year'].max()
        Common_Birth = df['Birth Year'].mode()[0]
        print("Earliest Birth Year is {}\nMost Recent Birth Year is {}\nMost Common Birth Year is {}.".format(Earliest_Birth,Recent_Birth,Common_Birth))


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
