import time
import numpy as np
import pandas as pd

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington).

    while True:
        city = input("Name of the city to analyze (chicago, new york city, washington) >> ").lower()
        if city in CITY_DATA:
            break
        else :
            print("Invalid City")

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Name of the month to analyze (all, january, february, ... , june) >> ").lower()
        if month in months:
            break
        else :
            print("Invalid Month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Name of the day to analyze (all, monday, tuesday, ... sunday) >> ").lower()
        if day in days:
            break
        else :
            print("Invalid Day")

    print("-" * 40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        if isinstance(month, str):
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        day = day.capitalize()
        df = df[df['day'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    if df.empty:
        print("The DataFrame is empty. No data to analyze.")
        return {}

    # TO DO: Display the most common month

    best_month = df['month'].mode()[0]
    print(f"Best month is : {best_month}")

    # TO DO: Display the most common day of week

    best_day = df['day'].mode()[0]
    print(f"Best day is : {best_day}")

    # TO DO: Display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    best_hour = df['hour'].mode()[0]
    print(f"Best hour is : {best_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

    return {
        'best_month': best_month,
        'best_day': best_day,
        'best_hour': best_hour
    }


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: Display most commonly used start station

    best_start_station = df['Start Station'].mode()[0]
    print(f"Best Start Station is : {best_start_station}")

    # TO DO: Display most commonly used end station

    best_end_station = df['End Station'].mode()[0]
    print(f"Best End Station is : {best_end_station}")

    # TO DO: Display most frequent combination of start station and end station trip

    df['Start End Station'] = df['Start Station'] + " AND " + df['End Station']
    best_start_end_station = df['Start End Station'].mode()[0]
    print(f" Best Start End Station is : {best_start_end_station}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

    return {
        'best_start_station': best_start_station,
        'best_end_station': best_end_station,
        'best_start_end_station': best_start_end_station
    }

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: Display total travel time

    total_duration_s = df['Trip Duration'].sum()
    total_duration_m = df['Trip Duration'].sum()/60
    total_duration_h = df['Trip Duration'].sum()/3600
    print(f"Total Duration is : {total_duration_s:.2f} s / {total_duration_m:.2f} min / {total_duration_h:.2f} h")    

    # TO DO: Display mean travel time

    mean_duration_s = df['Trip Duration'].mean()
    mean_duration_m = df['Trip Duration'].mean()/60
    mean_duration_h = df['Trip Duration'].mean()/3600
    print(f"Total Duration is : {mean_duration_s:.2f} s / {mean_duration_m:.2f} min / {mean_duration_h:.2f} h") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

    return {
        'Trip Duration': total_duration_s,
        'Mean Duration': mean_duration_s
    }

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
   
    """print(df['User Type'].unique())"""

    if 'User Type' not in df.columns:
        print("No Data")
    else:
        Subscriber = df['User Type'].str.count('Subscriber').sum()
        Customer = df['User Type'].str.count('Customer').sum()
        Dependent = df['User Type'].str.count('Dependent').sum()
        print(f"Counts of user types is : Subscriber = {Subscriber:.0f} / Customer = {Customer:.0f} / Dependent = {Dependent:.0f}")

    # TO DO: Display counts of gender

    """print(df['Gender'].unique())"""

    if 'Gender' not in df.columns:
        print("No Data")
    else:
        Male = df['Gender'].str.count('Male').sum()
        Female = df['Gender'].str.count('Female').sum()
        print(f"Counts of user types is : Female = {Female:.0f} And Male = {Male:.0f}")

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' not in df.columns:
        print("No Data")
    else:
        most_earliest = df['Birth Year'].min()
        print(f"Most Earliest is : {most_earliest:.0f}")

        most_recent = df['Birth Year'].max()
        print(f"Most Recent is : {most_recent:.0f}")

        most_common_year = df['Birth Year'].mode()[0]
        print(f"Most Common Year is : {most_common_year:.0f}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break

if __name__ == "__main__":
    main()