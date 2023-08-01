## My Pay

## Entitlements

Base = input("Base Pay: $")
BAH = input("BAH: $")
BAS = input("BAS: $")

## Deductions

Fed = input("Federal Taxes: $")
SS = input("FICA - Social Security: $")
Med = input("FICA - Medicare: $")
SGLI = input("SGLI: $")
State = input("State Taxes: $")
FSGLI = input("Family SGLI: $")
RTSP = input("Roth TSP: $")
TOT_Ent = [Base, BAH, BAS]
print(sum(TOT_Ent))
    
TOT_Ded = eval(sum(Fed + SS + Med + SGLI + State + FSGLI + RTSP)

   print("Total entitlement $", TOT_Ent)


## EOM = input("End of month pay: $")

## Allotments

## TRI = input("TRICARE dental: $")

## Summary
## TOT_Tax = eval((100*Fed)/TOT_Ent)
## Living = eval((100*(TOT_Ent-TOT_Ded))/TOT_Ent)



## M_M_P = input("Mid month pay: $")
