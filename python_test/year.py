s = str(input("Write an American date: (MM/DD/YY): "))


def date_converter(s):
    mm = s[0] + s[1]
    dd = s[3] + s[4]
    yy = s[6] + s[7]
    ds = '-'

    swe_date = str('20'+yy+ds+mm+ds+dd)
    print(swe_date)

    return mm, dd, yy,  swe_date


date_converter(s)
