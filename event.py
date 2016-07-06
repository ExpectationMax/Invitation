
thisevent = Event()

thisevent.title = "Strange german word with exclamation mark"
thisevent.description = "Much text"

thisevent.creator = Person("Max Horn", date(2016,7,16))
thisevent.trigger = lambda creator: ((creator.days_since_birth % 365.25) < 1)

# For christoph
thisevent.eventtype = "Party"

# check weather conditions
if weather == "Sunny" or weather == "Nice" or weather == "Awesome":
    thisevent.location = "Neckarwiese"
else:
    thisevent.location = "Dr.-Emil-König-Str. 3, 69214 Eppelheim"

# add minimum supply for a party
thisevent.supplies.append("crate of beer")
thisevent.supplies.append("cutlery")
thisevent.supplies.append("plates from the mensa")
thisevent.supplies.append("very basic food supply")
thisevent.supplies.append("brownies")

# conditional supplies
if thisevent.location == "Neckarwiese":
    grill = Supply("grill")
    grill.comment = "Does anybody know from who I could lend one?"
    thisevent.supplies.append(grill)
    thisevent.supplies.append("limited no. of blankets for lying around")

thisevent.giftRequired = False
thisevent.bring.append("Whatever you need to be happy")

if you.needAlcohol:
    thisevent.bring.append("Alcohol")

if you.needSupply:
    thisevent.bring.append("Your own supply")

if you.isAttending(thisevent):
    me.increaseHappiness()
