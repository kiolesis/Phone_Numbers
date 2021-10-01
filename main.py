import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Wpisz numer telefonu z numerem kraju:")
mobileNo = phonenumbers.parse(mobileNo)

# Strefa czasowa
print(timezone.time_zones_for_number(mobileNo))

# Informacje o przekaźniku telefonu
print(carrier.name_for_number(mobileNo, "en"))

# Informacje o regionie
print(geocoder.description_for_number(mobileNo, "en"))

# Ważność numeru
print("Ważność numeru telefonu: ", phonenumbers.is_valid_number(mobileNo))

# Możliwości numeru
print("Sprawdzenie możliwoście numeru", phonenumbers.is_possible_number(mobileNo))
