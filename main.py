import os
import time

def simulate_catalog_and_stock_automation():
    # -----------------------------------------------------------------
    # E-commerce Catalog and Low-Stock Automation System
    # Designed to run smoothly on both PC and Mobile IDEs (like Pydroid 3)
    # -----------------------------------------------------------------

    catalog_database = [
        [101, "Front Brake Pads (Premium)", 45.0, 12],
        [102, "Engine Oil Filter v2", 15.5, 3],
        [103, "High-Performance Spark Plug", 8.99, 22],
        [104, "Clutch Cable - Reinforced", 29.95, 2],
        [105, "Drive Chain 120 Links", 65.0, 15]
    ]

    LOW_STOCK_THRESHOLD = 5

    print("==================================================")
    print("     E-COMMERCE AUTOMATION ENGINE STARTED        ")
    print("==================================================")
    time.sleep(1)

    while True:
        print("\n[MAIN MENU]")
        print("1. View Store Catalog & Metrics")
        print("2. Run Bulk Price/Catalog Update")
        print("3. Check and Flag Low-Stock Items")
        print("4. Exit System")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            print(f"\n{'ID':<6} | {'Product Name':<30} | {'Price':<8} | {'Stock':<6}")
            print("-" * 60)
            for item in catalog_database:
                print(f"{item[0]:<6} | {item[1]:<30} | ${item[2]:<7.2f} | {item[3]:<6}")

        elif choice == "2":
            print("\n🔄 Running Bulk Catalog Update...")
            time.sleep(1)
            try:
                percentage = float(input("Enter price adjustment percentage (e.g., 5 for +5%): "))
                factor = 1 + (percentage / 100)
                for item in catalog_database:
                    item[2] *= factor
                print(f"✔ Success: Prices adjusted by {percentage}% globally across the catalog.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid percentage number.")

        elif choice == "3":
            print("\n🔍 Analyzing store metrics for low stock...")
            time.sleep(1.2)
            low_stock_found = False
            print(f"\n⚠️  [ALERT] ITEMS BELOW THRESHOLD ({LOW_STOCK_THRESHOLD}):")
            print(f"{'Product ID':<12} | {'Product Name':<30} | {'Stock Remaining':<15}")
            print("-" * 65)
            for item in catalog_database:
                if item[3] <= LOW_STOCK_THRESHOLD:
                    print(f"{item[0]:<12} | {item[1]:<30} | {item[3]:<15}")
                    low_stock_found = True
            if not low_stock_found:
                print("✔ All items are safely stocked above the threshold limit.")
            else:
                print("\n📥 Automation Log Generated: Alert file successfully exported to backend server.")

        elif choice == "4":
            print("\nShutting down automation services cleanly. Goodbye!")
            break
        else:
            print("❌ Invalid selection. Please choose a valid menu item.")

if __name__ == "__main__":
    simulate_catalog_and_stock_automation()
      
