def convert_age(age):
    days_in_year = 365.25  
    hours_in_day = 24
    
    age_in_days = age * days_in_year
    age_in_hours = age_in_days * hours_in_day
    
    return age_in_days, age_in_hours

age_to_convert = 45
days_lived, hours_lived = convert_age(age_to_convert)

print(f"A person aged {age_to_convert} years has lived for approximately:")
print(f"{days_lived:.2f} days")
print(f"{hours_lived:.2f} hours")
