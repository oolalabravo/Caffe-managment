from fpdf import FPDF
from datetime import datetime
import os

menu = {
    1: {"name": "Cappuccino", "price": 120},
    2: {"name": "Espresso", "price": 100},
    3: {"name": "Latte", "price": 130},
    4: {"name": "Cheesecake", "price": 150},
    5: {"name": "Brownie", "price": 80}
}
name =[]#order name
quan=[]#order quantities
total=[]#Total of indivisual order
cus_name=''#customer name
ttl=0#whole order total
price=[]#price of orders indivisual


def generate_invoice(customer_name, order_name, quant, price, total):
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()

    # Add DejaVuSans font (regular and bold)
    pdf.add_font('DejaVu', '', r'C:\Users\Bhavya\Desktop\DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', r'C:\Users\Bhavya\Desktop\DejaVuSans-Bold.ttf', uni=True)

    # Set the font to DejaVu regular for company name
    pdf.set_font('DejaVu', 'B', 16)  # Bold for the title
    pdf.cell(200, 10, text="Bombay Caffe House", ln=True, align='C')

    # Add Invoice Date
    pdf.set_font('DejaVu', '', 12)
    invoice_date = datetime.now().strftime('%d-%m-%Y')
    pdf.cell(200, 10, text=f"Date: {invoice_date}", ln=True, align='C')

    pdf.ln(10)  # Add a line break

    # Customer Details
    pdf.cell(200, 10, text=f"Customer Name: {customer_name}", ln=True)

    pdf.ln(5)  # Add a line break

    # Invoice Table Header
    pdf.set_font("DejaVu", 'B', 12)
    pdf.cell(50, 10, text="Product Name", border=1)
    pdf.cell(40, 10, text="Quantity", border=1)
    pdf.cell(40, 10, text="Price (₹)", border=1)
    pdf.cell(50, 10, text="Total (₹)", border=1)
    pdf.ln()

    # Reset font for table content
    pdf.set_font("DejaVu", '', 12)

    # Invoice Table Content for Multiple Orders
    grand_total = 0
    for i in range(len(order_name)):
        pdf.cell(50, 10, text=order_name[i], border=1)
        pdf.cell(40, 10, text=str(quant[i]), border=1)
        pdf.cell(40, 10, text=f"₹{price[i]}", border=1)  # Individual price
        pdf.cell(50, 10, text=f"₹{total[i]}", border=1)  # Total for the item
        pdf.ln()
        grand_total += total[i]

    pdf.ln(10)  # Add a line break

    # **Grand Total Block**
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(200, 10, text="-------------------------", ln=True, align='C')  # Separator line
    pdf.cell(200, 10, text=f"Grand Total: ₹{grand_total}", ln=True, align='C')
    pdf.cell(200, 10, text="-------------------------", ln=True, align='C')  # Separator line

    pdf.ln(10)  # Add a line break

    # Define the path where the invoice will be saved
    filename = f"invoice_{customer_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    output_path = os.path.join(r"F:\computer project\Cafe management", filename)

    # Check if the directory exists, if not, create it
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the PDF to the specified path
    pdf.output(output_path)
    print(f"Invoice generated successfully as '{output_path}'")
    
    op=input('Y/N Give Us Feedback: ')
    op.lower()
    if(op=='y'):
        feedback()
    else:
        print('Thanks For Visiting Us')
    reset_order_data()



def take_order():
    global cus_name
    global name
    global quan
    global total
    global ttl


    display_menu()
    cus_name=input('Please Enter Your Name: ')
    while True:
        item_id = int(input("Enter item number to add to order (0 to finish): "))
        if item_id == 0:
            if len(total)>0:
                for i in range(len(total)):
                    ttl+=total[i]

            break
        if item_id in menu:
            qty=int(input(f"Enter quantity for {menu[item_id]['name']}: "))
            name.append(menu[item_id]['name'])
            pri=int(menu[item_id]['price'])
            price.append(pri)
            t=qty*pri
            total.append(t)
            quan.append(qty)




def view_orders():
    if not name:
        print("📭 No active orders.")
        return
    print("\n📦 Current Orders 📦")
    for i in range(len(name)):
        print(f'Name: {name[i]} | Quantity {quan[i]} | Amount: {total[i]}')

    print("🧾 Order Summary 🧾")
    print(ttl)


def display_menu():
    print("\n📋 MENU 📋")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ₹{item['price']}")
    print()


def reset_order_data():
    global name, quan, total, price, ttl
    name.clear()
    quan.clear()
    total.clear()
    price.clear()
    ttl = 0

def feedback():
    print("\n📝 We Value Your Feedback 📝")
    customer_feedback = input("Please share your feedback: ")
    print("\nThank you for your feedback! 😊")
    print('Thanks For Visiting Us')
    
    with open(r"F:\computer project\Cafe management\feedback.txt", "a") as file:
        file.write(f"{datetime.now()} - {cus_name}: {customer_feedback}\n")


def main_menu():
    print("\n🎉 Welcome to the Café Management System 🎉")
    while True:
        
        print("1. Display Menu")
        print("2. Take Order")
        print("3. View Orders")
        print("4. Calculate Bill")
        #print("5. Give Us Feedback")
        print("5. Exit")


        choice = int(input("Select an option: "))
        if choice == 1:
            display_menu()
        elif choice == 2:
            take_order()
        elif choice == 3:
            view_orders()
        
        elif choice == 4:
            generate_invoice(cus_name,name,quan,price,total)
        
       # '''elif choice == 5:
           # feedback()'''
        elif choice == 5:
            print("👋 Exiting the system. Have a great day!")
            break
        else:
            print("❌ Invalid option. Please try again.")


# Runs the Café Management System
main_menu()