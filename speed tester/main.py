import speedtest as st

def speed_test():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download Speed in Mbps: ", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload Speed in Mbps: ", up_speed)

    ping = test.results.ping
    print("ping: ", ping)

speed_test()