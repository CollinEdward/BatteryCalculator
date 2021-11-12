 # This is kinda of a battery simulator, depending on screen brightness
 # Using this you have to know the estimated time for the battery to go down by a certain percentage by how long has passed

StartBattery = 100

EndBattery = 0

 # When the screen brigtness is at 4, it takes 17 minutes for the percentage to go down by 5

PercentageMinus = 5

Pr17MinutesPassed = 0

while StartBattery > EndBattery:
    StartBattery -= 5
    print(f"bettery percentage is {StartBattery}.")
    Pr17MinutesPassed += 1
    print(f"17 minutes has passed {Pr17MinutesPassed} times.")

if StartBattery == 0:
    print("It took ", 17 * Pr17MinutesPassed, " minutes for the battery to die while at 4 screen brightness" )