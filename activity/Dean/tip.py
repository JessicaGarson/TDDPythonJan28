tipdict = {"Excellent": .20,
           "Great": .15,
           "Good": .10,
           "Poor": .05,
           "Terrible": 0 }
def calculateTip(amount, rating):
    
    if rating in tipdict:
        tipamount =  float(amount) * tipdict[rating]
        return tipamount
    else:
        return f"Enter one of the following: {list(tipdict.keys())}"
    
if __name__ == "__main__":
    amount = input("Enter bill amount: ")
    rating = input(f"Tip scale\n{list(tipdict.keys())}\n\nEnter the type of tip you'd like to leave: ")
    print(calculateTip(amount, rating))
