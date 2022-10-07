from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.select_place_to_go(input("What city would you like to travel to?"))
        # below will only select dates within the two panes that get open, TODO figure out how to select future dates
        bot.select_dates('2022-11-15', '2022-11-30')
        bot.select_guest(int(input("How many adults?")))
        bot.search()
        bot.apply_filters()
        bot.refresh()
        bot.report_results()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from the terminal \n'
            'Please add your Selenium Drivers to the PATH variable \n'
            'Windows Command Line: \n'
            '   set PATH=%PATH%;C:/Users/Curtis/Documents/seleniumdrivers/ \n'
            '   Replace the forward slashes with back slashes above \n \n'
            'Git BASH Terminal: \n'
            ' PATH=$PATH:/C/Users/Curtis/Documents/seleniumdrivers/'
        )
    else:
        raise
