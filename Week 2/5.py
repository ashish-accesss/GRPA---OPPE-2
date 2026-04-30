# main_dish = input()
# time_of_day = int(input())
# has_voucher =   ...
# is_card_payment = ...

# if main_dish == "panner tikka":
#     cost = 250
#     elif main_dissh == "butter chikcen":
#         cost == 240
#     elif main_dish = "masal dosa":
#         cost = 200
#     else: # if main dish is invalid print invalid dish and exit the code.
#       print("Invalid main dish")
#       exit() 

#     if time_of_day >= 12 and time_of_day =< 15:
#         total_cost = (1 - 0.15) * cost

#     eles
#         total_cost = cost

#     if has_voucher
#         total_cost =* 0.9  # Apply voucher discount

#     if is_card_payment  # service charge for card payments
#         service_charge = 0.05 * total_cost
#         total_cost =+ servcie_charge

#     print(f"{total_cost:.02f}")
main_dish = input().lower().strip()
time_of_day=int(input())
has_voucher=input().strip() =="True"
is_card_payment=input().strip() =="True"

if main_dish=="paneer tikka":
    cost = 250
elif main_dish=="butter chicken":
    cost = 240
elif main_dish=="masala dosa":
    cost = 200
else:
    print("Invalid main dish")
if 12 <= time_of_day <= 15:
    cost -= cost*0.15
if has_voucher:
    cost -= cost*0.10
if is_card_payment:
    cost += cost*0.05
print(f"{cost:.2f}")
