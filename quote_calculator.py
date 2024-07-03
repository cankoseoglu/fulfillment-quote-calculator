# quote_calculator.py

# Define variables
sku_count = int(input("Depoya gönderilecek SKU adeti: "))
item_count = int(input("Depoya gönderilecek toplam adet: "))
product_size = input("Ürün boyutu (küçük/orta/büyük): ")
average_order_value = float(input("Ortalama sipariş tutarı (TL): "))
average_items_per_order = int(input("Ortalama sipariş başına ürün adeti: "))
value_added_services_cost = float(input("Katma değerli servis ücreti (TL): "))
minimum_invoice_amount = float(input("Minimum fatura bedeli (TL): "))

# Calculate mal kabul cost
base_cost_per_sku = 5  # Example value, adjust as needed
base_cost_per_item = 0.1  # Example value, adjust as needed
mal_kabul_cost = sku_count * base_cost_per_sku + item_count * base_cost_per_item

# Calculate stoklama ücreti
if product_size == 'küçük':
    storage_fee_per_m3 = 5  # Example value
elif product_size == 'orta':
    storage_fee_per_m3 = 7  # Example value
else:  # 'büyük'
    storage_fee_per_m3 = 10  # Example value
storage_cost = storage_fee_per_m3 * 30  # Assuming 1 cubic meter and 30 days

# Calculate sipariş karşılama ücreti
if average_order_value < 100:
    order_fulfillment_cost = 0
elif average_order_value < 500:
    order_fulfillment_cost = 20  # Example value
else:
    order_fulfillment_cost = 50  # Example value

# Calculate ürün toplama ücreti
picking_cost = average_items_per_order * 2  # Example calculation, adjust as needed

# Sum up all costs
total_cost = (
    mal_kabul_cost +
    storage_cost +
    value_added_services_cost +
    order_fulfillment_cost +
    picking_cost
)

# Ensure minimum invoice amount
if total_cost < minimum_invoice_amount:
    total_cost = minimum_invoice_amount + (minimum_invoice_amount * 0.1)  # 10% increase over the minimum

print(f"Toplam Teklif Tutarı: {total_cost} TL")
