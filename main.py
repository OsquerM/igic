#Variables 
cleanPrice = 1
def run(price_with_igic: float, igic: float) -> float:
    # TODO
    global  cleanPrice
    cleanPrice = price_with_igic - (price_with_igic * igic / 100) 
    return cleanPrice


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(cleanPrice)