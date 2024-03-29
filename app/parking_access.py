from app.utils import get_formated_datetime

# Constantes
PERCENT_CONVERSION_VALUE = 100
HOUR_IN_SECONDS = 3600
MINUTES_IN_HOUR = 60
FRACTIONS_PER_HOUR = 4
MAX_DAYTIME_HOURS = 9
FRACTION_IN_MINUTES = 15


class ParkingAccess:
  
    def get_price_by_time(self, parking_access: dict, parking_lot: object):
          checkin = get_formated_datetime(date=parking_access.get('checkin'))
          checkout = get_formated_datetime(date=parking_access.get('checkout'))

          if checkin >= get_formated_datetime(date=parking_lot.daily_overnight_initial_hour
          ) and checkout <= get_formated_datetime(date=parking_lot.daily_overnight_end_hour):
              return parking_lot.daily_value_daytime*(parking_lot.daily_value_overnight/PERCENT_CONVERSION_VALUE)
          
          total_seconds = (checkout-checkin).seconds
          hours = int(total_seconds/HOUR_IN_SECONDS)

          if hours >= MAX_DAYTIME_HOURS:
              return parking_lot.daily_value_daytime

          minutes = int((total_seconds - (hours*HOUR_IN_SECONDS))/MINUTES_IN_HOUR)
          hours_value = int(hours*((FRACTIONS_PER_HOUR*parking_lot.fraction_value)*(1 - (parking_lot.fulltime_value/PERCENT_CONVERSION_VALUE))))
          minutes_value = int(minutes/FRACTION_IN_MINUTES)*parking_lot.fraction_value

          return hours_value+minutes_value