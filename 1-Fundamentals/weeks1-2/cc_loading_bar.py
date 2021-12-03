for amount_loaded in range(0, 100 +5, 5):
    print(amount_loaded)
    if amount_loaded == 25:
        print("1/4 of the way")
    elif amount_loaded==50:
        print("1/2 of the way")
    elif amount_loaded ==75:
        print("3/4 of the way")
    elif amount_loaded == 100:
        print("loading complete")
    