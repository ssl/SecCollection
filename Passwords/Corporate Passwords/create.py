years = list(range(2016, 2026))
seasons = ["Spring", "Summer", "Autumn", "Winter"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
special_event = "Christmas"

variations = []

for year in years:
    for season in seasons:
        variation = season + str(year)
        variations.extend([variation, variation.lower(), variation + "!"])
    for month in months:
        variation = month + str(year)
        variations.extend([variation, variation.lower(), variation + "!"])
    variation = special_event + str(year)
    variations.extend([variation, variation.lower(), variation + "!"])

for v in variations:
    print(v)
