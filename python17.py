action = "buy"
match action:
    case "buy":
        print("order crypto buy")
    case "sell":
        print("crypto sell hogi")
    case _:
        print("sell and buy wrong")
        