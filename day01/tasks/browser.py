browser_name = input("Enter browser name:")
valid_browser_names = ["chrome", "firefox", "edge", "opera", "safari"]

if browser_name in valid_browser_names:
    if browser_name == "chrome":
        print("Chrome Browser is selected")
    elif browser_name == "firefox":
        print("Firefox Browser is selected")
    elif browser_name == "opera":
        print("Firefox Browser is selected")
    elif browser_name == "safari":
        print("Firefox Browser is selected")
    else:
        print("Edge Browser is selected")
else:
    print("Invalid Browser Name")

