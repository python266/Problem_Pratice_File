def photo_sizer(l, w, h):
    if l > w or l > h:
        print("UPLOAD ANOTHER")
    elif w == h:
        print("ACCEPTED")
    elif l < w or l < h:
        print("CROP IT")
if __name__ == '__main__':
    photo_sizer(l=180, w=640, h=480)
    photo_sizer(l=180, w=120, h=300)
    photo_sizer(l=180, w=180, h=180)