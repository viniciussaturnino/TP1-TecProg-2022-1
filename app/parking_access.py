from datetime import datetime


class ParkingAccess:
  
  def get_price_by_time(self, parking_access: dict, parking_lot: object):
        checkin = datetime.strptime(parking_access.get('checkin'), "%H:%M:%S")
        checkout = datetime.strptime(parking_access.get('checkout'), "%H:%M:%S")

        if checkin >= datetime.strptime(parking_lot.daily_overnight_initial_hour, "%H:%M:%S"
        ) and checkout <= datetime.strptime(parking_lot.daily_overnight_end_hour, "%H:%M:%S"):
            return parking_lot.daily_value_daytime*(parking_lot.daily_value_overnight/100)
        
        total_seconds = (checkout-checkin).seconds
        hours = int(total_seconds/3600)

        if hours >= 9:
            return parking_lot.daily_value_daytime

        minutes = int((total_seconds - (hours*3600))/60)
        hours_value = int(hours*((4*parking_lot.fraction_value)*(1 - (parking_lot.fulltime_value/100))))
        minutes_value = int(minutes/15)*parking_lot.fraction_value

        return hours_value+minutes_value