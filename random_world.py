import random


# returns a random phone number
def generate_random_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"


# returns a list of random phone numbers. the number of phone numbers is passed in as a parameter
def generate_list_random_phone_numbers(number_of_phone_numbers):
    phone_numbers = []
    for i in range(number_of_phone_numbers):
        phone_numbers.append(generate_random_phone_number())
    return phone_numbers


# returns a random date
def generate_random_date():
    return f"{random.randint(1, 12)}/{random.randint(1, 28)}/{random.randint(1900, 2020)}"


# returns a list of random dates. the number of dates is passed in as a parameter
def generate_list_random_dates(number_of_dates):
    dates = []
    for i in range(number_of_dates):
        dates.append(generate_random_date())
    return dates


# returns a random address from a list of street names, street types, cities, states and zip codes
def generate_random_address():
    with open("streets.txt", "r") as f:
        streets = f.read().splitlines()
    with open("street_types.txt", "r") as f:
        street_types = f.read().splitlines()
    with open("cities.txt", "r") as f:
        cities = f.read().splitlines()
    with open("states.txt", "r") as f:
        states = f.read().splitlines()
    with open("zipcodes.txt", "r") as f:
        zipcodes = f.read().splitlines()
    street = streets[random.randint(0, len(streets)-1)]
    street_type = street_types[random.randint(0, len(street_types)-1)]
    city = cities[random.randint(0, len(cities)-1)]
    state = states[random.randint(0, len(states)-1)]
    zipcode = zipcodes[random.randint(0, len(zipcodes)-1)]
    return f"{street} {street_type}, {city}, {state} {zipcode}"


# returns a list of random addresses. the number of addresses is passed in as a parameter
def generate_list_random_addresses(number_of_addresses):
    addresses = []
    for i in range(number_of_addresses):
        addresses.append(generate_random_address())
    return addresses


# returns a random word from a words text document
def generate_random_word():
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    return words[random.randint(0, len(words)-1)]


# generates list of random words. the number of words is passed in as a parameter
def generate_list_random_words(number_of_words):
    words = []
    for i in range(number_of_words):
        words.append(generate_random_word())
    return words


# generates random sentence of words from a text document. the number of words in the sentence is
# passed in as a parameter
def generate_random_sentence(number_of_words):
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    sentence = ""
    for i in range(number_of_words):
        if i == 0:
            sentence += words[random.randint(0, len(words)-1)].capitalize() + " "
        else:
            sentence += words[random.randint(0, len(words)-1)] + " "
    return f"{sentence[:-1]}."


# generates a random list od sentences of random length. the number of sentences is passed in as a parameter
def generate_random_list_sentences(number_of_sentences):
    sentences = []
    for i in range(number_of_sentences):
        sentences.append(generate_random_sentence(random.randint(5, 15)))
    return sentences


# generates a random full name from a list of first names and a list of last names
def generate_random_name():
    with open("firstnames.txt", "r") as f:
        firstnames = f.read().splitlines()
    with open("lastnames.txt", "r") as f:
        lastnames = f.read().splitlines()
    return f"{firstnames[random.randint(0, len(firstnames)-1)]} {lastnames[random.randint(0, len(lastnames)-1)]}"


# generates a list of random names. the number of names is passed in as a parameter
def generate_list_random_names(number_of_names):
    names = []
    for i in range(number_of_names):
        names.append(generate_random_name())
    return names


# generates a random email address from a list of first names, last names and domains. returns a list of email
# addresses and the full name of the person the email address belongs to """
def generate_random_email():
    with open("firstnames.txt", "r") as f:
        firstnames = f.read().splitlines()
    with open("lastnames.txt", "r") as f:
        lastnames = f.read().splitlines()
    with open("domains.txt", "r") as f:
        domains = f.read().splitlines()
    firstname = firstnames[random.randint(0, len(firstnames)-1)]
    lastname = lastnames[random.randint(0, len(lastnames)-1)]
    domain = domains[random.randint(0, len(domains)-1)]
    return f"{firstname}.{lastname}@{domain}", f"{firstname} {lastname}"


# generates a random job title from a list of job titles
def generate_random_job_title():
    with open("job_titles.txt", "r") as f:
        job_titles = f.read().splitlines()
    return job_titles[random.randint(0, len(job_titles)-1)]


# generates a list of random job titles. the number of job titles is passed in as a parameter
def generate_list_random_job_titles(number_of_job_titles):
    job_titles = []
    for i in range(number_of_job_titles):
        job_titles.append(generate_random_job_title())
    return job_titles


# generates random user profile. returns a dictionary with the user's name, email address, phone number, address,
# date of birth and job title
def generate_random_user_profile():
    email, name = generate_random_email()
    phone_number = generate_random_phone_number()
    address = generate_random_address()
    date_of_birth = generate_random_date()
    job_title = generate_random_job_title()
    return {"name": name, "email": email, "phone_number": phone_number, "address": address,
            "date_of_birth": date_of_birth, "job_title": job_title}


# generates a list of random user profiles. the number of profiles is passed in as a parameter
def generate_list_random_user_profiles(number_of_profiles):
    profiles = []
    for i in range(number_of_profiles):
        profiles.append(generate_random_user_profile())
    return profiles

