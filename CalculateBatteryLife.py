 # This is kinda of a battery simulator, depending on screen brightness
 # Using this you have to know the estimated time for the battery to go down by a certain percentage by how long has passed

StartBattery = 100

EndBattery = 0

 # When the screen brigtness is at 4, it takes 17 minutes for the percentage to go down by 5

PercentageMinus = 5
# set the value for 0 so it can count the times that 17 minutes has been passed to add up all minutes at the end
Pr17MinutesPassed = 0

# While the starting battery is higher then what your end battery goal is, it will keep going down. 
while StartBattery > EndBattery:
    # Here knowing what the battey goes down by the certain minute, gets taken away from the start battery.
    StartBattery -= 5
    print(f"bettery percentage is {StartBattery}.")
    # For this specific test where after 17 minutes the battery goes down by 5 procent at 4 % brightness -
    # It adds 1 time to every 17 minutes that has passed so it can tell how long it took the computer to loose all battery.
    Pr17MinutesPassed += 1 
    print(f"17 minutes has passed {Pr17MinutesPassed} times.")

# Checks start battery for value 0, so it can stop and add everything together.
if StartBattery == 0:
    print("It took ", 17 * Pr17MinutesPassed, " minutes for the battery to die while at 4 screen brightness" )