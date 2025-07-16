print('Welcome to our funding platform')

loan = int (input('How much would you like to loan? '))

rate = int (input('What annual rate are you comfortable with? '))

duration = int (input('What duration in years are you comfortable with? '))

monthly_rate = (rate / 100) / 12
 
monthly_duration = duration * 12 

print('Your monthly interest rate is ', monthly_duration)

mortgage = loan * (monthly_rate*(1 + monthly_rate)**monthly_duration) / ((1 + monthly_rate)**monthly_duration - 1)

print('Your monthly mortgage payment is ', mortgage, 'thank you! ')








