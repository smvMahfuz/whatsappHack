import pywhatkit as pwk

try:
    # pwk.sendwhatmsg_to_group("Family", "Hey Guys! How's everybody?", 20, 27)
    # pwk.sendwhats_image("Family", "Media/image.png", "Hi")
    pwk.sendwhatmsg("+8801727577709", "Hi Mr Ripon, Good morning?", 6, 18)
    # # pwk.sendwhatmsg("+8801786948601", "Hi Mr sagor", 20,7)
    # # pwk.sendwhatmsg("+8801727577709", "Hello", 20, 18)
    # # print("Message Sent!")
    pwk.sendwhats_image("+8801727577709", "media/image.jpeg")


except:
    print("Error in sending the message")
