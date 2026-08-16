# riverton baseline data with jobs included
industries = {
    "ironforge_steel": {
        "emissions": 50000, 
        "mac": 120, 
        "flight_risk": 85,
        "jobs": 12000
    },
    "riverton_power": {
        "emissions": 35000, 
        "mac": 65, 
        "flight_risk": 100,
        "jobs": 2500
    },
    "nanolink_systems": {
        "emissions": 15000, 
        "mac": 30, 
        "flight_risk": 200,
        "jobs": 8000
    }
}

def simulate_market(carbon_price):
    print(f"--- testing carbon price: ${carbon_price} per ton ---")
    
    total_emissions_reduced = 0
    total_jobs_lost = 0
    total_revenue = 0
    
    for name, data in industries.items():
        # check if the price forces them to relocate (carbon leakage)
        if carbon_price >= data["flight_risk"]:
            print(f"{name}: relocates (price >= flight risk) -> jobs lost")
            total_jobs_lost += data["jobs"]
            
        # check if the price is high enough to force them to upgrade tech
        elif carbon_price >= data["mac"]:
            print(f"{name}: reduces emissions! (price >= mac) -> less pollution")
            total_emissions_reduced += data["emissions"]
            
        # if the price is too low, they just buy credits and keep polluting
        else:
            print(f"{name}: buys credits (price < mac) -> keeps polluting")
            total_revenue += data["emissions"] * carbon_price
            
    # print the final calculated stats for this price point
    print(f"results for ${carbon_price} carbon price:")
    print(f"   - emissions reduced: {total_emissions_reduced:,} tons")
    print(f"   - government revenue: ${total_revenue:,}")
    print(f"   - jobs lost to carbon leakage: {total_jobs_lost:,}\n\n")

# test scenarios based on the scarcity scale
simulate_market(20)
simulate_market(30)
simulate_market(40)
simulate_market(50)
simulate_market(60)
simulate_market(70)
simulate_market(80)
simulate_market(90)