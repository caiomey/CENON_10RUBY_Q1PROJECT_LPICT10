from pyscript import document, display
from js import alert

def create_order(e):
    # Get quantity values
    item1 = int(document.getElementById("item1").value)
    item2 = int(document.getElementById("item2").value)
    item3 = int(document.getElementById("item3").value)
    item4 = int(document.getElementById("item4").value)
    item5 = int(document.getElementById("item5").value)
    item6 = int(document.getElementById("item6").value)
    item7 = int(document.getElementById("item7").value)

    # Prices
    price1 = 100
    price2 = 60
    price3 = 160
    price4 = 20
    price5 = 30
    price6 = 120
    price7 = 140

    # Calculate total
    total = (item1*price1 + item2*price2 + item3*price3 +
             item4*price4 + item5*price5 + item6*price6 + item7*price7)

    # Customer details
    customer_name = document.getElementById("customer").value
    customer_address = document.getElementById("address").value
    contact_number = document.getElementById("contact_number").value

    # Create summary
    summary_text = "<h5>Order Summary:</h5>"
    items = [("Carbonara", item1), ("Garlic Bread", item2), ("Caesar Salad", item3),
             ("Iced Tea", item4), ("Sparkling Water", item5),
             ("Pancakes", item6), ("Rice with Chicken", item7)]
    
    for name, qty in items:
        if qty > 0:
            summary_text += f"{name}: {qty}<br>"

    summary_text += f"<strong>Total: ₱{total}</strong>"

    # Display results
    document.getElementById("summary").innerHTML = summary_text
    alert("✅ Order Successful!")
    document.getElementById("success_message").innerHTML = "✅ Order Successful!"
