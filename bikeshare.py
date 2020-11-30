import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def choice (choice):
    """Asks user to proceed with the program or to terminate

    #Returns:
    #'Proceeding the program...'  - if user enters 1
    #'Good Bye!'                  - if user enters 0
    #'Invalid Entry, Try Again!'  - if user enters value different than (0) or (1)
    #"""

    while True:
        print()
        print("'* press (1) to continue, or (0) to terminate')")
        choice = input()

        if choice == '1':
            msg= "proceeding the program..."
            print(msg)
            break

        elif choice == '0':
            print("\nGood Bye!\n")
            quit()

        else:
            print("\nInvalid Entry, Try Again!\n")
            continue

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print()
    print('________________________')
    print('CITY            | Number|'.upper())
    print('________________________|')
    print('chicago         |1      |'.title())
    print('new york city   |2      |'.title())
    print('washington      |3      |'.title())
    print('________________________|')


    city=''

    while True:
        city = int(input('* Kindly choose the city number to investigate further:').strip())

        if city==1:
            print()
            print('You have chosen {}'.format(list(CITY_DATA.keys())[0].title())) # Display the dictionary key index 0 = Chicago, return as list
            city="chicago"
            choice(city)
            print()
            break
        elif city==2:
            print()
            print('You have chosen {}'.format(list(CITY_DATA.keys())[1].title())) # Display the dictionary key index 1 = new york city, return as list
            city="new york city"
            choice(city)
            print()
            break
        elif city==3:
            print()
            print('You have chosen {}'.format(list(CITY_DATA.keys())[2].title())) # Display the dictionary key index 2 = washington, return as list
            city="washington"
            choice(city)
            print()
            break
        else:
            print()
            print('you have entered a worng value, retry:')
            print()
            continue


   # TO DO: get user input for month (all, january, february, ... , june)

    print()
    print()
    print('________________________')
    print('Month           | Number|'.upper())
    print('________________________|')
    print('January         |1      |'.title())
    print('February        |2      |'.title())
    print('March           |3      |'.title())
    print('April           |4      |'.title())
    print('May             |5      |'.title())
    print('June            |6      |'.title())
    print('All             |7      |'.title())
    print('________________________|')
    print()

    months_list = ['january', 'february', 'march', 'april', 'may', 'june']
    month=''
    # Checking if the user input included within the month_list list.
    while True:
        month = int(input('* Kindly choose the month number to investigate further:').strip())
        if 1 <= month <= 6:
            print('You have chosen', months_list[month - 1].title()) #Displaying the value stored inside the month_list index
            month=str(months_list[month - 1].lower()) # Assigning the month_list index value into the month var. Retruning value as string
            choice(month)
            break
        elif month==7:
            print()
            print('* You have chosen to invistigate all months:')
            print('_____________________________________________________________________________________________________________________________')
            print('|',str(months_list),'|')  # Display the full month list to the user. reurn it as a str
            print('_____________________________________________________________________________________________________________________________')
            month='all' # Assigning the string 'all' into var month, if user choose 7 (All cities as a filter)
            choice(month)
            break
        else:
            print()
            print('you have entered a worng value, retry:')
            print()
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print()
    print()
    print('________________________')
    print('Day             | Number|'.upper())
    print('________________________')
    print('monday          |1      |'.title())
    print('tuesday         |2      |'.title())
    print('wednesday       |3      |'.title())
    print('thursday        |4      |'.title())
    print('friday          |5      |'.title())
    print('saturday        |6      |'.title())
    print('sunday          |7      |'.title())
    print('all             |8      |'.title())
    print('________________________|')
    print()

    day_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday'] # Creating var day_list. Assigning a list with days of the week

    while True:
        day = int(input('* Kindly choose the day number to investigate further:').strip()) #asking the user to choose a numerical value
        if 1 <= day <= 7:
            print('You have chosen', day_list[day - 1].title()) #Displaying the day by accessing the day_list index
            day=str(day_list[day - 1].lower())
            choice(day)
            break
        elif day==8:
            print()
            print('* You have chosen to invistigate all days:')
            print('_____________________________________________________________________________________________________________________________')
            print('|',str(day_list),'|') # Displaying the full day_list. Return as string
            print('_____________________________________________________________________________________________________________________________')
            day='all' # if user choose 8 (all days), assign the str value 'all' into the day var
            choice(day)
            break
        else:
            print('you have entered a worng value, retry:')
            print()
            continue



    return city ,month,day


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
    df['Start Time']= pd.to_datetime(df['Start Time']) # Converting the 'Start Time' Column into datetime object
    df['End Time']= pd.to_datetime(df['End Time']) # Converting the 'End Time' column into datatime object
    df['month']=df['Start Time'].dt.month_name() # Creating new column 'month' and store the converted Start Time values
    df['day']=df['Start Time'].dt.day_name() # Creating new column 'day' and store the converted Start Time values
    print(df['month'])
    # Giving values to the new day column
    #. capitalize since the values stores are starting with capital letters
    if day != 'all' :
        df = df[df['day'] == day.capitalize()]

    if month != 'all' :
        df = df[df['month'] == month.capitalize()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_common_month = df['month'].mode()[0]
    print()
    print('The most common month is:{}'.format(most_common_month))
    print('-'*40)

    # TO DO: display the most common day of week

    most_common_day = df['day'].mode()[0]
    print()
    print('The most common month is:{}'.format(most_common_day))
    print('-'*40)

    # TO DO: display the most common start hour

    most_common_starthour= df['Start Time'].dt.hour.mode()[0]
    print()
    print('The most common start hour is:{}'.format(most_common_starthour))
    print('-'*40)
    print()
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_ss = df['Start Station'].mode()[0]
    print()
    print('The most common Start Station is:{}'.format(most_common_ss))
    print('-'*40)

    # TO DO: display most commonly used end station
    most_common_es = df['End Station'].mode()[0]
    print()
    print('The most common End Station is:{}'.format(most_common_es))
    print('-'*40)

    # TO DO: display most frequent combination of start station and end station trip by using the mode() method on the column index
    df['Trip_Comp']= df['Start Station']+'' +df['End Station']
    trip_comp=df['Trip_Comp'].mode()[0]
    print('The most frequest combination of Start and End station is:{}'.format(trip_comp))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time by using the sum() method

    total_travel_time = df['Trip Duration'].sum()
    print()
    print('The total travel time is:{}'.format(total_travel_time))
    print('-'*40)

    # TO DO: display mean travel time by using the .mean() method

    mean_travel_time = df['Trip Duration'].mean()
    print()
    print('The mean travel time is:{}'.format(mean_travel_time))
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('-'*40)
    user_type=df['User Type'].value_counts()
    print(user_type)
    print('-'*40)

    # TO DO: Display counts of gender by using the value_counts method
    # Handling the Washington exception by using using try, except

    try:
        df['Gender']
        gender_type=df['Gender'].value_counts()
        print(gender_type)
    except:
        pass

    print('-'*40)

    # TO DO: Display earliest, most recent, and most common year of birth
    # Handling the Washington exception by using using try, except

    try:
        df['Birth Year']
        earliest_birth=int(df['Birth Year'].min())
        print()
        print('The earliest year of birth is:{}'.format(earliest_birth))
        print('-'*40)
    except:
        pass

    try:
        df['Birth Year']
        recent_birth=int(df['Birth Year'].max())
        print()
        print('The recent year of birth is:{}'.format(int(recent_birth)))
        print('-'*40)
    except:
        pass

    try:
        df['Birth Year']
        common_birth=int(df['Birth Year'].mode())
        print()
        print('The common year of birth is:{}'.format(common_birth))
        print('-'*40)
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #Asking the user if intersted in seeing the raw data, show 5 in each dispaly
        #checking the user input and exiting the loop if the condition is not met

        raw_data=input('Do you want to see the raw data??').lower().strip()
        while(raw_data=='yes'):
            start=0
            end=5
            temp=df[start:end]
            print(temp)
            start += 5 #increment the start var by 5 on each loop
            end += 5    #increment the start var by 5 on each loop
            raw_data=input('Do you want to see more raw data? Enter yes or no').lower().strip()

        #Asking the user to terminate or restart the program. Yes for restart, no terminate
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
