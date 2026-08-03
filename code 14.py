def calculate_gst_exclusive(base_price, gst_rate):
    """
    Calculates GST when the price does NOT include tax yet.
    Formula: GST Amount = (Base Price * GST Rate) / 100
    """
    gst_amount = (base_price * gst_rate) / 100
    total_price = base_price + gst_amount
    
    return gst_amount, total_price

def calculate_gst_inclusive(total_price, gst_rate):
    """
    Calculates the base price and tax when the price ALREADY includes tax.
    Formula: Base Price = (Total Price * 100) / (100 + GST Rate)
    """
    base_price = (total_price * 100) / (100 + gst_rate)
    gst_amount = total_price - base_price
    
    return gst_amount, base_price

# ==========================================
# --- Example 1: Adding GST (Exclusive) ---
# ==========================================
print("--- 1. Adding GST to a Base Price ---")
price_before_tax = 1000  # Let's say ₹1000
rate = 18                # 18% GST

tax_added, final_bill = calculate_gst_exclusive(price_before_tax, rate)

print(f"Base Price: ₹{price_before_tax:.2f}")
print(f"GST Rate: {rate}%")
print(f"GST Amount: ₹{tax_added:.2f}")
print(f"Total Bill: ₹{final_bill:.2f}\n")

# ==========================================
# --- Example 2: Extracting GST (Inclusive) ---
# ==========================================
print("--- 2. Extracting GST from a Total Price ---")
mrp = 1180               # Let's say the sticker price is ₹1180
rate = 18                # 18% GST

tax_included, original_price = calculate_gst_inclusive(mrp, rate)

print(f"Total Price (MRP): ₹{mrp:.2f}")
print(f"GST Rate: {rate}%")
print(f"Original Base Price: ₹{original_price:.2f}")
print(f"GST Amount Included: ₹{tax_included:.2f}")