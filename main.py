from dataset import df
print("""
"Hello! 👋 Welcome to AutoSherpa. I'm here to help you find your perfect used car. How can I assist you today?"
      
1️⃣ 🚗 Browse Used Cars
2️⃣ 💰 Get Car Valuation 
3️⃣ 📞 Contact Our Team
4️⃣  About us

select one option         
""")
customer_number=int(input())

if customer_number==1:
    print("""
I'd love to help you find the perfect car.

Please select your budget range:
1️⃣ Under ₹3Lakhs
2️⃣ ₹3-5 Lakhs  
3️⃣ above ₹5 Lakhs


Please select your budget range:(select the option)
    """)
    number=int(input())

    if number ==1:
        print(
        """
Not Bad! under ₹3 Lakhs gives you only few options.Now, what type of car do you prefer?
        """)
        value_df=df[df['Purchase Price']<=300000]
        # result2="model - "+value_df['Model'] +"   Variant - "+ value_df['Variant']
        # result2=value_df['Model']
        result2=value_df['Model'].drop_duplicates().reset_index(drop=True)
        
        dict={}
        for i in range(min(5, len(result2))): 
            dict[i + 1] = value_df['Model'].iloc[i]
            print(f"{i+1} - {result2.iloc[i]}")

        # print("""select an option from the above shown """)
        # model_number=int(input())
        # print(f"Perfect! {dict[model_number]} are very popular for families.") 
        print("select the brand:")
        choose_model=int(input())-1
        selected_model=result2[choose_model]
        filtered_df = value_df[value_df['Model'] == selected_model]
        print(f"\nAvailable variants for model '{selected_model}':")
        for idx, row in enumerate(filtered_df.itertuples(), 1):
            print(f"{idx} - Variant: {row.Variant}")

        variant_choice = int(input("Select an option from the above shown: ")) - 1
        selected_variant = filtered_df.iloc[variant_choice]['Variant']

        print(f"\nPerfect! {selected_model} - {selected_variant} is a very popular choice for families.")


    elif number==2:
        print(
        """
Good Choice! between ₹3-5 Lakhs gives you excellent options.Now, what type of car do you prefer?

        """)
        value_df=df[(df['Purchase Price']>300000) &( df['Purchase Price']<=500000) ]
        # result2="model - "+value_df['Model'] +"   Variant - "+ value_df['Variant']
        result2=value_df['Model'].drop_duplicates().reset_index(drop=True)
        dict={}
        print("""choose the brand from respective model  """)
        for i in range(len(result2)): 
            dict[i + 1] = value_df['Model'].iloc[i]
            print(f"{i+1} - {result2.iloc[i]}")
        
        print("select the brand:")
        choose_model=int(input())-1
        selected_model=result2[choose_model]
        filtered_df = value_df[value_df['Model'] == selected_model]
        # print(f"\nAvailable variants/brands for model '{selected_model}':")
        # for i, row in filtered_df.iterrows():
        #     print(f"{i+1} - {row['Variant']}")



        # print("""select an option from the above shown """)
        # model_number=int(input())
        # print(f"Perfect! {dict[model_number]} are very popular for families.") 
        print(f"\nAvailable variants for model '{selected_model}':")
        for idx, row in enumerate(filtered_df.itertuples(), 1):
            print(f"{idx} - Variant: {row.Variant}")

        variant_choice = int(input("Select an option from the above shown: ")) - 1
        selected_variant = filtered_df.iloc[variant_choice]['Variant']

        print(f"\nPerfect! {selected_model} - {selected_variant} is a very popular choice for families.")
        

    elif number==3:
        print(
        """
Great Choice! Above 5 Lakhs gives you many options.
Now, what type of car do you prefer?

        """)
        value_df=df[df['Purchase Price']>500000]
        # result2=value_df['Model'] 
        result2=value_df['Model'].drop_duplicates().reset_index(drop=True)

        dict={}
        for i in range(min(5, len(result2))): 
            dict[i + 1] = value_df['Model'].iloc[i]
            print(f"{i+1} - {result2.iloc[i]}")

        print("select the brand:")
        choose_model=int(input())-1
        selected_model=result2[choose_model]
        filtered_df = value_df[value_df['Model'] == selected_model]
        print(f"\nAvailable variants for model '{selected_model}':")
        for idx, row in enumerate(filtered_df.itertuples(), 1):
            print(f"{idx} - Variant: {row.Variant}")

        variant_choice = int(input("Select an option from the above shown: ")) - 1
        selected_variant = filtered_df.iloc[variant_choice]['Variant']

        print(f"\nPerfect! {selected_model} - {selected_variant} is a very popular choice for families.")
        # print("""select an option from the above shown """)
        # model_number=int(input())
        # print(f"Perfect! {dict[model_number]} are very popular for families.") 


# we need to print the images of the selected car by the user//
    print("""
what would you like to do next ?
1️⃣ Get detailed specifications
2️⃣ See more pictures  
3️⃣ Check financing options
4️⃣ Schedule test drive
5️⃣ See other cars from my list
6️⃣ Get best price quote

Select 1-6:
    """)
    test_drive_number=int(input())
    if test_drive_number==4:
        print(f"""
Perfect! Let's arrange your {selected_model} test drive.

when would you prefer the test drive?

1️⃣ Today 
2️⃣ Tomorrow  
3️⃣ This weekend 

Pick your preferred option:
        """)
        date_number=int(input())
        day_dict={
            1:"Today",
            2:"Tomorrow",
            3:" This weekend"
        }
        print(f"Excellent! {day_dict[date_number]} is perfect.")


        print("Please provide your details:")

        print("📝 Your Name: [Please type]")
        name=input()

        print("📱 Phone Number: [Please type] ")
        number=int(input())

        print("\nDo you have a valid driving license?")
        print("1️⃣ Yes")
        print("2️⃣ No")
        license_number = int(input("Enter 1 or 2: "))

        if license_number == 2:
            print("""
        🚫 We're sorry!

        Unfortunately, a valid driving license is mandatory to take a test drive.

        Please feel free to explore other options or reach out to our team for further assistance. We're always here to help! 😊
        """)
            exit()  # or return if you're in a function
        else:
            license_status = "Yes"

        # Ask about number of people joining
        print("\nHow many people will join the test drive?")
        print("1️⃣ Just me")
        print("2️⃣ 2 people")
        print("3️⃣ 3-4 people")
        print("4️⃣ More than 4")
        people_number = int(input("Enter your choice: "))

        people_dict = {
            1: "Just me",
            2: "2 people",
            3: "3-4 people",
            4: "More than 4"
        }
        people_joining = people_dict.get(people_number, "Unknown")

        print(f"Thank you {name}! ✅ Your test drive is confirmed:")

#         print(f"""
# 🚗 **TEST DRIVE CONFIRMED**
# 👤 Name: {name}  
# 📱 Phone: {number}
# ✅ License: {license_status}
# 👥 People joining: {people_joining}
# 🚗 Car: {selected_model} - {selected_variant} – ₹{filtered_df['Purchase Price'].iloc[variant_choice]:,}
# 📅 Date: {day_dict[date_number]}  
# ⏰ Time: 10:00 AM - 12:00 PM
# """)


#         print("""
# 📍 **Showroom Location:**
# AutoDeals, Maruti Division, MG Road, Bangalore
    
# What should we prepare for your visit?

# 1️⃣ Just the test drive
# 2️⃣ Test drive + financing discussion
# 3️⃣ Test drive + other car options  
# 4️⃣ Everything (complete car buying consultation)

# Choose 1-4:"

#         """)
#         details_number=int(input())
#         print(f"""
# Perfect! We'll prepare everything for your complete car buying experience.
    

# ✅ **TOMORROW'S AGENDA:**
# 🚗 {selected_model} test drive
# 💰 Financing options discussion  
# 🔄 Trade-in evaluation (if applicable)
# 📋 Complete documentation guidance
# 🎯 Best price negotiation
# 📊 Insurance & warranty options

# Our executive Suresh will handle your complete requirements.

# **BRING TOMORROW:**
# ✅ Valid Driving License
# ✅ Any ID Proof
# ✅ Current car documents (if trade-in)

# **WEATHER UPDATE:**
# We have covered parking and AC showroom for your comfort!

# Looking forward to helping you find your perfect {selected_model} tomorrow! 

# Have a great day! 👋

# *You can reply anytime if you have questions before tomorrow's visit.*"

#         """)
        # After confirming test drive and printing confirmation...

# Step 10: Test Drive Location
        print(f"\nThank you {name}! Your details are noted. Where would you like to take the test drive?")
        print("1️⃣ Pick up from our showroom")
        print("2️⃣ We bring the car to your location")
        print("3️⃣ Meet at a nearby landmark")
        print("4️⃣ At your office (if weekend is suitable)")

        location_choice = int(input("Enter your choice (1-4): "))

        location_dict = {
            1: "Our Showroom",
            2: "Your Location",
            3: "Nearby Landmark",
            4: "Your Office"
        }
        location_text = location_dict.get(location_choice, "Our Showroom")

        # Step 11: Final Confirmation
        print(f"""
Perfect! Here's your test drive confirmation:

🚗 **TEST DRIVE CONFIRMED**
👤 Name: {name}
📱 Phone: {number}
✅ License: {license_status}
👥 People joining: {people_joining}
🚗 Car: {selected_model} - {selected_variant} – ₹{filtered_df['Purchase Price'].iloc[variant_choice]:,}
📅 Date: {day_dict[date_number]}
⏰ Time: 10:00 AM - 12:00 PM
📍 Location: {location_text}

        """)

        if location_choice == 1:
            print("""🏢 Showroom Address: AutoDeals, Maruti Division, MG Road, Bangalore
        🚗 Free parking available""")
        elif location_choice == 4:
            print("""🏢 We'll confirm if weekend is suitable for your office visit.""")

        print("""
What to bring:
✅ Valid driving license
✅ Any photo ID

What else can I help you with?
1️⃣ Get directions to showroom
2️⃣ Know what documents to bring
3️⃣ See other cars too
4️⃣ Get financing information
5️⃣ Talk to our sales executive
6️⃣ All set, see you Saturday! 👋
        """)

        next_step = int(input("Select an option (1-6): "))

        # Step 12: Final Thank You & Follow-up
        if next_step == 6:
            print(f"""
Wonderful {name}! 👋
Your {day_dict[date_number]} test drive is all confirmed. Our executive Suresh will call you a day before to confirm directions and answer any questions.
📞 Need help before then? Call us: +91-9876543210 WhatsApp: This number

Quick reminder: We'll also have financing options ready if you like the car during your test drive!
Looking forward to seeing you {day_dict[date_number]} morning!
Have a great day! 😊
        """)
        else:
            # You can add further handling for other options here if needed.
            print("Thanks for your response! We'll assist you with that shortly.")

if customer_number==2:
    print("""
Welcome to Car Valuation !! 

Let’s value your car. First, what’s the Car Make (Designed by)?
1️⃣ Maruti
2️⃣ Hyundai
3️⃣ Renault   

Select from 1-3:          
    """)
    make_number = int(input())

    if make_number == 1:
        result_df = df[df['Make'] == "Maruthi"]
        print("And choose the model from below:")
        model_dict = {}
        for i in range(min(5, len(result_df))):
            model_name = result_df["Model"].iloc[i]
            model_dict[i + 1] = model_name
            print(f"{i+1} - {model_name}")

        model_chosed = int(input("Enter your model choice number: "))
        selected_model = model_dict[model_chosed]

        print("Can you choose the variant in that model?")
        variant_df = result_df[result_df["Model"] == selected_model]
        for i, variant in enumerate(variant_df["Variant"].unique(), 1):
            print(f"{i} - {variant}")

    elif make_number == 2:
        result_df = df[df['Make'] == "Hyundai"]
        print("And choose the model from below:")
        model_dict = {}
        for i in range(min(5, len(result_df))):
            model_name = result_df["Model"].iloc[i]
            model_dict[i + 1] = model_name
            print(f"{i+1} - {model_name}")

        model_chosed = int(input("Enter your model choice number: "))
        selected_model = model_dict[model_chosed]

        print("Can you choose the variant in that model?")
        variant_df = result_df[result_df["Model"] == selected_model]
        for i, variant in enumerate(variant_df["Variant"].unique(), 1):
            print(f"{i} - {variant}")

    elif make_number == 3:
        result_df = df[df['Make'] == "Renault"]
        print("And choose the model from below:")
        model_dict = {}
        for i in range(min(5, len(result_df))):
            model_name = result_df["Model"].iloc[i]
            model_dict[i + 1] = model_name
            print(f"{i+1} - {model_name}")

        model_chosed = int(input("\nEnter your model choice number: "))
        selected_model = model_dict[model_chosed]

        print("Can you choose the variant in that model?")
        variant_df = result_df[result_df["Model"] == selected_model]
        for i, variant in enumerate(variant_df["Variant"].unique(), 1):
            print(f"{i} - {variant}")

        variant_choices = list(variant_df["Variant"].unique())

        variant_number = int(input("Enter your variant choice number: \n"))
        selected_variant = variant_choices[variant_number - 1]
        price_df = variant_df[variant_df["Variant"] == selected_variant]
        prices = price_df["Estimated Selling Price"].tolist()


        if len(prices) == 1:
            estimated_price = prices[0]
        else:
            estimated_price = sum(prices) / len(prices)

        print(f"\nYour {selected_model} {selected_variant} is valued at approximately ₹{estimated_price:,.0f}\n")

