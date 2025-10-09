def add_time(start, duration, start_day=None):
    # Parse start time
    time, period = start.split()
    start_hour, start_min = map(int, time.split(':'))
    
    # Convert to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Parse duration
    dur_hour, dur_min = map(int, duration.split(':'))
    
    # Calculate total minutes
    total_min = start_min + dur_min
    extra_hour = total_min // 60
    final_min = total_min % 60
    
    # Calculate total hours and days
    total_hour = start_hour + dur_hour + extra_hour
    days_later = total_hour // 24
    final_hour = total_hour % 24
    
    # Convert back to 12-hour format
    if final_hour == 0:
        display_hour = 12
        period = 'AM'
    elif final_hour == 12:
        display_hour = 12
        period = 'PM'
    elif final_hour > 12:
        display_hour = final_hour - 12
        period = 'PM'
    else:
        display_hour = final_hour
        period = 'AM'
    
    # Format time
    new_time = f"{display_hour}:{final_min:02d} {period}"
    
    # Handle day of week
    if start_day:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_index = days.index(start_day.lower())
        final_index = (start_index + days_later) % 7
        new_time += f", {days[final_index].capitalize()}"
    
    # Handle days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time