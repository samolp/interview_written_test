import random
import datetime


def generate_data():
    # Randomly pickup from predefined data
    first_name = ['Alice', 'Ben', 'Charles', 'David', 'Emily']
    last_name = ['Chan', 'Wong', 'Lee', 'Ng', 'Lam']
    name = random.choice(first_name) + ' ' + random.choice(last_name)

    gender = random.choice(['M', 'F'])

    dob = datetime.datetime(random.randint(1900,2020), random.randint(1,12), random.randint(1,31) )
    dob = dob.strftime('%d/%m/%Y')

    phone = str(random.randint(10000000, 99999999))

    email_client = ['yahoo.com', 'gmail.com']
    email = name.replace(' ', '') + '@' + random.choice(email_client)

    building = ['A', 'B', 'C']
    road = ['D', 'E', 'F']
    district = ['Wan Chai', 'Central', 'Causeway Bay']
    address = random.choice(building) + ' Building\n' + \
              random.choice(road) + ' Road, ' + random.choice(district)

    person = {
        'name': name,
        'gender': gender,
        'dateOfBirth': dob,
        'phoneNumber': phone,
        'email': email,
        'address': address

    }

    return person
