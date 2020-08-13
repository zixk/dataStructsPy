
    # Clock hands
    # Write a function that returns the acute angle between two clock hands, with two integers for the number of hours and number of minutes.
    # E.g. For 3:00, the acute angle would be 90°. For 6:00, it would be 180°.

def clockHands(hour, minute):
    hour_hand = 360*hour/12
    minute_hand = 360*minute/60
    angle_between_hands = abs(hour_hand-minute_hand)
    print(min(angle_between_hands, 360-angle_between_hands))
if __name__ == "__main__":
    clockHands(6,42)