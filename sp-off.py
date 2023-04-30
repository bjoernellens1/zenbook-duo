from screenpad import screenpad

if __name__ == "__main__":
    sp = screenpad()
    if sp.get_brightness(sp.sp_brightness_path) != 0:
        sp.set_brightness(0)
    else:
        sp.set_brightness(30)