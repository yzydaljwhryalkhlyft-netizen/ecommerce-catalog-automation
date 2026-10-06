import sys
import time

class CatalogManager:
    def __init__(self):
        self.products = {
            101: {"name": "Front Brake Pads (Premium)", "price": 45.0, "stock": 12},
            102: {"name": "Engine Oil Filter v2", "price": 15.5, "stock": 3},
            103: {"name": "High-Performance Spark Plug", "price": 8.99, "stock": 22},
            104: {"name": "Clutch Cable - Reinforced", "price": 29.95, "stock": 2},
            105: {"name": "Drive Chain 120 Links", "price": 65.0, "stock": 15}
        }
        self.threshold = 5

    def display_metrics(self):
        print("\n" + "="*63)
        print(f"| {'SKU':<6} | {'Product Description':<30} | {'Price':<10} | {'Stock':<6} |")
        print("="*63)
        for sku, info in self.products.items():
            print(f"| {sku:<6} | {info['name']:<30} | ${info['price']:<9.2f} | {info['stock']:<6} |")
        print("="*63)

    def execute_bulk_update(self):
        try:
            raw_input = input("\n[INPUT] Percentage adjustment (e.g. 5 or -2.5): ").strip()
            rate = float(raw_input)
            factor = 1 + (rate / 100)
            
            for sku in self.products:
                self.products[sku]["price"] = round(self.products[sku]["price"] * factor, 2)
                
            print(f"[SUCCESS] Global price modulation applied: {rate}%")
        except ValueError:
            print("[ERROR] Micro-operation aborted: Invalid numeric format.")

    def audit_inventory_levels(self):
        print(f"\n[SCAN] Evaluating core metrics against limit ({self.threshold} units)...")
        time.sleep(0.5)
        violations = 0
        
        print("\n" + "-"*56)
        print(f"| {'SKU':<8} | {'Flagged Resource':<30} | {'Qty':<8} |")
        print("-"*56)
        
        for sku, info in self.products.items():
            if info["stock"] <= self.threshold:
                print(f"| {sku:<8} | {info['name']:<30} | {info['stock']:<8} |")
                violations += 1
                
        print("-"*56)
        if violations > 0:
            print(f"[ALERT] System logged {violations} depletion instances.")
        else:
            print("[SUCCESS] Inventory levels secure. Zero flags raised.")

def main():
    engine = CatalogManager()
    
    while True:
        print("\n::: SYSTEM CORE ENGINE :::")
        print("1) Sync Catalog View")
        print("2) Price Modification Routine")
        print("3) Run Low-Stock Diagnostics")
        print("4) Terminate Process")
        
        step = input("Execution code: ").strip()
        
        if step == "1":
            engine.display_metrics()
        elif step == "2":
            engine.execute_bulk_update()
        elif step == "3":
            engine.audit_inventory_levels()
        elif step == "4":
            print("\n[SHUTDOWN] Terminating runtime environment cleanly.")
            sys.exit(0)
        else:
            print("[WARNING] Invalid operation token.")

if __name__ == "__main__":
    main()
            
