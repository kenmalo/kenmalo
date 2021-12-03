state_capitals = {"Washington" :"Olympia","Oregon":"salem", "California":"Sacramento" }
#print(len(state_capitals))
#print(state_capitals["Washington"])
state_capitals["Washington"] = "Aberdeen"
state_capitals["Texas"] = "Austin"
del state_capitals["California"]
#state_capitals.pop("Oregon")
print(state_capitals)
removed_capital = state_capitals.pop("Oregon")
print(removed_capital)