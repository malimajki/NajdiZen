from datetime import timedelta, datetime

monday_start = '12:00'
monday_start = datetime.strptime(monday_start, "%H:%M")
monday_end = '06:00'
monday_end = datetime.strptime(monday_end, "%H:%M")
pausa_od = '12:00'
pausa_od = datetime.strptime(pausa_od, "%H:%M")
pausa_do = '13:00'
pausa_do = datetime.strptime(pausa_do, "%H:%M")


slot_duration = 30

slots = []

while monday_start < monday_end:
    if monday_start >= pausa_od and monday_start <= pausa_do:
        pass
    else:
        slots.append(monday_start.strftime("%H:%M"))
    monday_start = monday_start + timedelta(minutes=slot_duration)
print (slots)