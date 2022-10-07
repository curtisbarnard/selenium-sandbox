from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.select_place_to_go('Tokyo')
    # below will only select dates within the two panes that get open, TODO figure out how to select future dates
    bot.select_dates('2022-10-15', '2022-10-30')
    bot.select_guest(2)
    bot.search()
    bot.apply_filters()
