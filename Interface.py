import gradio as gr
import random

# Real-looking random names for donors
donor_names = [
    "Alice", "Aisha", "Omkar", "Bhavesh", "Anjali", "Ravi", "Priya", "Siddharth", "Neha", 
    "Karan", "Sonal", "Rahul", "Rohit", "Sneha", "Aman", "Meera", "Farhan", "Isha", 
    "Kabir", "Rhea", "Jai", "Rekha", "Vishal", "Parvati", "Sameer", "Simran", "Deepak", 
    "Arjun", "Nikita", "Manish", "Kavita", "Pooja", "Kunal", "Ritika", "Harsh", "Yash", 
    "Aarti", "Shweta", "Raj", "Tina", "Raghav", "Gauri", "Tejas", "Vikas", "Ishaan"
]

# Define blood groups and locations
blood_groups = ["A+", "B+", "O+", "O-", "AB-", "A-", "B-"]
locations = ["Pune", "Mumbai", "Nagpur", "Nashik", "Delhi"]

# Generate random donor data with real-looking names and fake numbers
donors = []
for location in locations:
    for blood_group in blood_groups:
        for i in range(10):  
            donors.append({
                "name": random.choice(donor_names),
                "bloodGroup": blood_group,
                "phone": f"+91 {random.randint(7000000000, 9999999999)}",  # for creating fake numbers
                "location": location
            })

# Function to search for donors based on blood group and location
def search_donor(blood_group, location):
    found_donors = [donor for donor in donors if donor['bloodGroup'] == blood_group and donor['location'].lower() == location.lower()]
    
    if found_donors:
        result = "\n".join(f"Name: {donor['name']}, Phone: {donor['phone']}" for donor in found_donors)
        return result
    else:
        return "No donor found for the given blood group and location."

# Define Gradio interface
with gr.Blocks() as interface:
    gr.Markdown("<h1 style='text-align: center; color: red;'>Blood Bank Management System</h1>")
    
    blood_group_input = gr.Dropdown(label="Select Blood Group", choices=blood_groups, value="A+")
    location_input = gr.Dropdown(label="Select Location", choices=locations, value="Mumbai")
    
    output = gr.Textbox(label="Donors Found", lines=10, placeholder="Search results will appear here...")
    
    # Button to search
    search_button = gr.Button("Search Donor")
    
    # Button function
    search_button.click(fn=search_donor, inputs=[blood_group_input, location_input], outputs=output)

# Launching the interface
interface.launch()
