def findAngle(hour: int, minute: int):
    hour %= 12  # normalize to 0-11

    angle_h = (hour * 360) // 12  # angle of just hour
    # minute/(total minutes in clock) * 360Deg
    # add adjustment of movement due to minutes.
    angle_h += (minute * 360) // (12 * 60)

    # Minute angle
    # Minute/<total minutes in face of clock> * 360Deg
    angle_m = (minute * 360) // 60

    # Get angle diff
    angle = abs(angle_h-angle_m)

    if angle > 180:
        angle = 360 - angle

    return angle


angle = findAngle(1, 45)
print(angle)
