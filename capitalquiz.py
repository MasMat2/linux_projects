import random

state_capital = {'Alabama' : ('AL', 'Montgomery'), 'Alaska' : ('AK', 'Juneau'), 'Arizona' : ('AZ', 'Phoenix'), 'Arkansas' : ('AR', 'Little Rock'), 'California' : ('CA', 'Sacramento'), 'Colorado' : ('CO', 'Denver'), 'Connecticut' : ('CT', 'Hartford'), 'Delaware' : ('DE', 'Dover'), 'Florida' : ('FL', 'Tallahassee'), 'Georgia' : ('GA', 'Atlanta'), 'Hawaii' : ('HI', 'Honolulu'), 'Idaho' : ('ID', 'Boise'), 'Illinois' : ('IL', 'Springfield'), 'Indiana' : ('IN', 'Indianapolis'), 'Iowa' : ('IA', 'Des Moines'), 'Kansas' : ('KS', 'Topeka'), 'Kentucky' : ('KY', 'Frankfort'), 'Louisiana' : ('LA', 'Baton Rouge'), 'Maine' : ('ME', 'Augusta'), 'Maryland' : ('MD', 'Annapolis'), 'Massachusetts' : ('MA', 'Boston'), 'Michigan' : ('MI', 'Lansing'), 'Minnesota' : ('MN', 'Saint Paul'), 'Mississippi' : ('MS', 'Jackson'), 'Missouri' : ('MO', 'Jefferson City'), 'Montana' : ('MT', 'Helena'), 'Nebraska' : ('NE', 'Lincoln'), 'Nevada' : ('NV', 'Carson City'), 'New Hampshire' : ('NH', 'Concord'), 'New Jersey' : ('NJ', 'Trenton'), 'New Mexico' : ('NM', 'Santa Fe'), 'New York' : ('NY', 'Albany'), 'North Carolina' : ('NC', 'Raleigh'), 'North Dakota' : ('ND', 'Bismarck'), 'Ohio' : ('OH', 'Columbus'), 'Oklahoma' : ('OK', 'Oklahoma City'), 'Oregon' : ('OR', 'Salem'), 'Pennsylvania' : ('PA', 'Harrisburg'), 'Rhode Island' : ('RI', 'Providence'), 'South Carolina' : ('SC', 'Columbia'), 'South Dakota' : ('SD', 'Pierre'), 'Tennessee' : ('TN', 'Nashville'), 'Texas' : ('TX', 'Austin'), 'Utah' : ('UT', 'Salt Lake City'), 'Vermont' : ('VT', 'Montpelier'), 'Virginia' : ('VA', 'Richmond'), 'Washington' : ('WA', 'Olympia'), 'West Virginia' : ('WV', 'Charleston'), 'Wisconsin' : ('WI', 'Madison'), 'Wyoming' : ('WY', 'Cheyenne')}
points = 0
finish = ['q','f','e','quit','finish','end']


while True:
    state = random.choice(list(state_capital))
    question = 0

    if question == 0:
        print()
        print('What is the capital of %s?' %(state))
        answer = input('-').lower()

        if answer in finish:
            break
        elif answer == state_capital[state][1].lower():
            print('Correct!')
        else:
            print('The correct answer is: %s' % (state_capital[state][1]))
