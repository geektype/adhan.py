import adhan

c = adhan.Client(
        latitude = 51.89105733691326,
        longitude =   -0.4304007575461619,
)

print(c.get_day())
