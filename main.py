import pywhatkit

# Send a WhatsApp Message to a Contact at 12:00 AM
pywhatkit.sendwhatmsg("+919876543210", "Happy Birthday", 0, 0)

# Send a WhatsApp Message to a Group (Friends) at 09:30 AM
pywhatkit.sendwhatmsg_to_group("Friends", "Hey All!", 9, 30)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("Friends", "Images/Hello.png", "Hello")
