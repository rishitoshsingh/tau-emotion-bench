from tau_emotion_bench.types import Task, Action


TASKS = [
    Task(
        user_id='mia.jackson2679@example.com',
        instruction='You are Mia Jackson, authenticated via mia.jackson2679@example.com, and you want to first understand the range of product types available in the catalog. You are then looking to update the shipping address for your pending order containing a Gaming Mouse and a pair of size 7 Hiking Boots to a new location in Denver. You prefer the new address to be 3420 Jackson Street, Unit 269, Denver, CO, USA 58293 because you have relocated temporarily. Later, you would like to cancel your other pending order that includes an Air Purifier, a leather medium green Backpack with a camera compartment, and a bagged cordless Vacuum Cleaner, because you ordered it by mistake and no longer need the items. You prefer any refund to be returned to the original payment method, PayPal.\n\nUse mia.jackson2679@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1298962', 'address1': '3420 Jackson Street', 'address2': 'Unit 269', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '58293'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8411016', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.santos2789@example.com',
        instruction='You are a customer with the email aarav.santos2789@example.com who has a pending order and a delivered order, both shipped to Phoenix. You want to cancel the pending order because it was placed by mistake. Later, you would like to exchange the mechanical keyboard from your delivered order, which currently has an 80% size layout with RGB backlight and linear switches, for the same model but in a more compact 60% size layout, also with RGB backlight and linear switches, because you prefer a smaller footprint for your workspace. You prefer to use your Visa card ending in 1747 for any price adjustment associated with the exchange.\n\nUse aarav.santos2789@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6111820', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8309293'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8309293', 'item_ids': ['8484921793'], 'new_item_ids': ['7867398203'], 'payment_method_id': 'credit_card_3816099'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.kim1995@example.com',
        instruction='You are James Kim, authenticated with email james.kim1995@example.com, and you want to learn about the T-Shirt product available in various colors like blue, purple, red, and black, in sizes from S to XXL, made of cotton or polyester, with crew neck or v-neck styles, priced around $47–$54. Later, you would like to update the shipping address for your pending order—which includes a Backpack, Electric Kettle, Espresso Machine, Air Purifier, and Electric Toothbrush—currently set to San Antonio, TX, to a new address in San Francisco, CA. You prefer the change because you are relocating temporarily and want the delivery sent to your new location. You prefer the order to remain on the original payment method, PayPal.\n\nUse james.kim1995@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9154975', 'address1': '1658 Cedar Road', 'address2': 'Suite 542', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '49528'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.hernandez8836@example.com',
        instruction='You are assisting Yusuf Hernandez (email: yusuf.hernandez8836@example.com) with his pending order currently shipping to Denver. You want to update the shipping address to 9069 Adams Road, Unit 212, Los Angeles, CA, USA 38750 because he has relocated temporarily. Later, you would like to exchange the black wired gaming mouse for the white wireless model, as he prefers a cleaner aesthetic and the convenience of wireless connectivity. You prefer the price difference to be handled using his PayPal account, which was previously used for the original payment.\n\nUse yusuf.hernandez8836@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2166301', 'address1': '9069 Adams Road', 'address2': 'Unit 212', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '38750'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2166301'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2166301', 'item_ids': ['3330317167'], 'new_item_ids': ['8896479688'], 'payment_method_id': 'paypal_7529813'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.wilson6954@example.com',
        instruction='You are assisting Mason Wilson, who is authenticated via mason.wilson6954@example.com. You want to return the Digital Camera from a delivered order placed in Indianapolis. The camera has a 30MP resolution, 5x zoom, and uses SD card storage. You prefer to return this item and have the refund issued back to the original gift card used for purchase.\n\nUse mason.wilson6954@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8161562'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8161562', 'item_ids': ['7195021808'], 'payment_method_id': 'gift_card_6767859'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.thomas1454@example.com',
        instruction='You are assisting a customer with email harper.thomas1454@example.com who has a pending order in Houston containing a green PVC yoga mat (6mm thickness) and a black Smart Thermostat compatible with Apple HomeKit. You want to update the payment method for this order from the Visa card ending in 5768 to the Mastercard ending in 7287, as the customer prefers to use this card for the purchase.\n\nUse harper.thomas1454@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7425646'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7425646', 'payment_method_id': 'credit_card_1199336'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.gonzalez4478@example.com',
        instruction='You are assisting Liam Gonzalez (email: liam.gonzalez4478@example.com) with his pending order. You want to update the shipping address to 4230 Cedar Road, Apt 849, Denver, CO, USA 81272 because he needs the delivery redirected. You prefer to change the payment method to your Mastercard ending in 4422 for better rewards and tracking. You also want to exchange the 500ml glass black Water Bottle for the 750ml stainless steel black one because you prefer a larger, more durable option. You are interested in learning more about available Water Bottle options, particularly those with stainless steel material, larger capacity, and black color, to understand future purchase possibilities. After these modifications are processed, you would like to cancel the entire order because you no longer need the items.\n\nUse liam.gonzalez4478@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8747662'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8747662', 'address1': '4230 Cedar Road', 'address2': 'Apt 849', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '81272'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8747662', 'payment_method_id': 'credit_card_6341155'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8747662', 'item_ids': ['8538875209'], 'new_item_ids': ['3453331371'], 'payment_method_id': 'credit_card_6341155'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8747662', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.silva2443@example.com',
        instruction='You are Yara Silva, with email yara.silva2443@example.com. You want to update the shipping address for your pending order containing an Electric Kettle, Wristwatch, and Bookshelf to 6715 Park Drive, Suite 118, Oklahoma City, OK, USA 49262, because you need it delivered to a new location. You also want to update your default address to this same address for future orders. Later, you would like to return the blue Cycling Helmet (size L) from your delivered order that also included a Dumbbell Set and Vacuum Cleaner, because it does not fit well, and you prefer the refund to be applied back to your gift card. After that, you would like to cancel your other pending order containing an Air Purifier, Backpack, Water Bottle, and Tablet, because you no longer need those items. Finally, you want to browse the available product types and learn more about the T-Shirt product for potential future purchase, because you are considering adding casual wear to your wardrobe.\n\nUse yara.silva2443@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9810810'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9810810', 'address1': '6715 Park Drive', 'address2': 'Suite 118', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '49262'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yara_silva_7567', 'address1': '6715 Park Drive', 'address2': 'Suite 118', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '49262'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3964602', 'item_ids': ['7907773809'], 'payment_method_id': 'gift_card_7252880'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9034102', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.muller4197@example.com',
        instruction='You are Omar Muller, with email omar.muller4197@example.com, and you want to update the shipping address for a pending order containing a jigsaw puzzle and a notebook to 9007 Madison Drive, Floor 93, Fort Worth, TX, USA 36068 because it is your new location, and you also want this address set as your default for future orders. Later, you would like to return the white stainless steel 2L electric kettle from a delivered order because you no longer need it, and you prefer the refund to be issued back to the original gift card used for purchase. After that, you intend to cancel another pending order that includes a glass bookshelf, a blue glass water bottle, a black 10-inch tablet, and a black plastic 1.5L electric kettle because it was placed by mistake. Finally, you are interested in browsing the product catalog and would like to see detailed information about the Laptop product to evaluate it for a potential future purchase.\n\nUse omar.muller4197@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7044833'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7044833', 'address1': '9007 Madison Drive', 'address2': 'Floor 93', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '36068'}),
            Action(name='modify_user_address', kwargs={'user_id': 'omar_muller_7891', 'address1': '9007 Madison Drive', 'address2': 'Floor 93', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '36068'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6573840', 'item_ids': ['4458619711'], 'payment_method_id': 'gift_card_3689412'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9474165', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.lopez2997@example.com',
        instruction='You are Raj Lopez, authenticated at raj.lopez2997@example.com. You want to cancel your pending order containing a black 500ml stainless steel water bottle, a bamboo 31-inch graphic skateboard, and synthetic waterproof size 9 hiking boots because it was placed by mistake. After that, you would like to update your other pending order: first, change the shipping address to 7024 Oak Avenue, Suite 191, Charlotte, NC, USA 72643. Then, you prefer to switch the payment method from your Mastercard ending in 6731308 to PayPal. Finally, you want to exchange the black small polyester crew neck T-Shirt in that order for a blue medium cotton crew neck T-Shirt because you prefer the larger size, different color, and more breathable material.\n\nUse raj.lopez2997@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3502364', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3502364'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7162915', 'address1': '7024 Oak Avenue', 'address2': 'Suite 191', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '72643'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7162915', 'payment_method_id': 'paypal_7007375'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7162915', 'item_ids': ['1176194968'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_7007375'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.ito8974@example.com',
        instruction='You are Amelia Ito, with email amelia.ito8974@example.com. For your delivered order containing items shipped to Columbus, you want to return the Hiking Boots because they are not waterproof and made of synthetic material, and you would like to exchange the 2-cup black espresso coffee maker for a 4-cup stainless steel drip coffee maker with auto shutoff because you prefer a larger capacity and simpler brewing style. You prefer any refund or charge to be processed to your Mastercard ending in 7517. Later, you would like to update the shipping address for your pending order—currently going to Seattle—to 8797 Madison Drive, Unit 130, Las Vegas, NV, USA 33488, to ensure delivery at your new location. After that, you would like to browse the full list of product types available in the store to explore other items of interest.\n\nUse amelia.ito8974@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3733909'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3733909', 'item_ids': ['6595128475'], 'payment_method_id': 'credit_card_1016162'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3733909', 'item_ids': ['9862136885'], 'new_item_ids': ['3039787582'], 'payment_method_id': 'credit_card_1016162'}),
            Action(name='get_product_details', kwargs={'product_id': '7996920482'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3883329', 'address1': '8797 Madison Drive', 'address2': 'Unit 130', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '33488'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3883329', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are assisting James Martin (james.martin9857@example.com). You want to cancel a pending order that includes a red XXL cotton T-shirt, a Smart Thermostat compatible with Amazon Alexa, a white-dial silicone-strap wristwatch, a 100ft rubber garden hose, and a green small polyester backpack with a camera compartment, because he no longer needs these items. Later, you would like to modify another pending order that currently includes a black small nylon laptop backpack, a 5-25 lbs adjustable iron dumbbell set, and size 10 synthetic hiking boots. You want to update the shipping address for this order to 676 Park Drive, Suite 502, San Diego, CA, USA 90382, and also set this as the new default address. You prefer to exchange the black small nylon laptop backpack for the grey small nylon laptop backpack because you prefer the color grey over black, and you would like the price difference charged to your Mastercard ending in 2067.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3043531', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3529525', 'address1': '676 Park Drive', 'address2': 'Suite 502', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '90382'}),
            Action(name='modify_user_address', kwargs={'user_id': 'james_martin_1500', 'address1': '676 Park Drive', 'address2': 'Suite 502', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '90382'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3529525', 'item_ids': ['7824298782'], 'new_item_ids': ['8054888773'], 'payment_method_id': 'credit_card_6932154'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.kovacs4505@example.com',
        instruction='You are Sofia Kovacs (sofia.kovacs4505@example.com). You want to cancel your pending order containing an electric toothbrush and a portable charger because you no longer need those items. Later, you would like to modify another pending order by replacing the 28-inch skateboard with a maple deck and plain design with the 28-inch version that has a bamboo deck and graphic design, because you prefer a more eco-friendly material and a bolder look. After that, you would like the shipping address for this modified order to be updated to 1780 Maple Lane, Floor 496, Chicago, IL, USA 72691, as you will be relocating. You prefer any price difference from the change to be handled through your PayPal account, which was used for the original purchase.\n\nUse sofia.kovacs4505@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5765741', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5765741'}),
            Action(name='get_product_details', kwargs={'product_id': '7352963235'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9869592', 'address1': '1780 Maple Lane', 'address2': 'Floor 496', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '72691'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_kovacs_7075', 'address1': '546 Lakeview Drive', 'address2': 'Suite 491', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '19049'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9869592', 'item_ids': ['3232433601'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'paypal_6840891'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are assisting Lei Li (email: lei.li8350@example.com) with her order and product exploration preferences. You want to first update the shipping address for her pending order (containing a space grey 17-inch i5 Laptop) to 6188 Jackson Street, Apt 933, Jacksonville, FL, USA 75226, because she has relocated temporarily. You also want to change the payment method from PayPal to her Visa card ending in 2697 for both the original charge and any price adjustments, as she prefers using that card for tech purchases. Additionally, you want to upgrade the laptop to a black 17-inch model with an i7 processor and 32GB RAM, which is more powerful for her work needs. Later, you will cancel this entire order because she has changed her mind and no longer needs the laptop immediately. After that, you would like to explore the full product catalog, starting with all available Laptop variants, to compare configurations, prices, and features for a future purchase decision.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '6188 Jackson Street', 'address2': 'Apt 933', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '75226'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5166363', 'payment_method_id': 'credit_card_4466831'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5166363', 'item_ids': ['3334537816'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'credit_card_4466831'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.brown8893@example.com',
        instruction='You are Anya Brown (anya.brown8893@example.com). You want to exchange the delivered Pet Bed (medium, fleece, grey) for a new one with memory foam and beige color because you prefer better support and a lighter color. You prefer the price difference to be handled using your Mastercard ending in 9625. Later, you will cancel your pending order containing the E-Reader and Smart Watch because you no longer need them. After that, you would like to update the shipping address for your other pending order (which includes a Wall Clock, Desk Lamp, Dumbbell Set, and Bluetooth Speaker) to 7246 Park Drive, Unit 508, San Francisco, CA, USA 33474, and change the payment method for this order to your PayPal account.\n\nUse anya.brown8893@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2922433'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2922433', 'item_ids': ['6857426243'], 'new_item_ids': ['3360679910'], 'payment_method_id': 'credit_card_3414703'}),
            Action(name='get_product_details', kwargs={'product_id': '2747247837'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8883368', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1170711', 'address1': '7246 Park Drive', 'address2': 'Unit 508', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '33474'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1170711', 'payment_method_id': 'paypal_5206520'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.nguyen5072@example.com',
        instruction='You are Mia Nguyen, with email mia.nguyen5072@example.com, who is exploring the product catalog and wants to learn about the Action Camera, particularly its 4K waterproof variants in black and silver. You want to cancel your pending order containing a Tablet, Luggage Set, Sneakers, and a Cycling Helmet because it was placed by mistake. Later, you would like to exchange the black Wireless Earbuds with 6-hour battery life in another pending order for the blue variant with the same 6-hour battery life, as you prefer the blue color. After that, you would like the shipping address for this order to be updated to 3580 Park Drive, Unit 921, San Jose, CA, USA 58763. Finally, you want your default address to be updated to this new San Jose address for all future orders, as it is your current residence. You prefer to keep using PayPal for payments.\n\nUse mia.nguyen5072@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7259788', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7259788'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4657527', 'item_ids': ['5565631513'], 'new_item_ids': ['1646531091'], 'payment_method_id': 'paypal_3722088'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4657527', 'address1': '3580 Park Drive', 'address2': 'Unit 921', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '58763'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mia_nguyen_6399', 'address1': '3580 Park Drive', 'address2': 'Unit 921', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '58763'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.thomas1454@example.com',
        instruction='You are assisting Harper Thomas (email: harper.thomas1454@example.com), who is interested in Action Cameras and has a pending order containing a Yoga Mat and a Smart Thermostat. You want to change the payment method for this order from your Visa ending in 5768 to your Mastercard ending in 7287 because you prefer using that card for this purchase. You also want to exchange the green Yoga Mat for a blue one, as you prefer the blue color over green. Later, you would like to update the shipping address for this order to 6961 Park Drive, Floor 658, San Francisco, CA, USA 48442, to ensure it is delivered to the correct location. After that, you would like to update your default address to the same San Francisco address for future orders.\n\nUse harper.thomas1454@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7425646'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7425646', 'payment_method_id': 'credit_card_1199336'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7425646', 'item_ids': ['7510236436'], 'new_item_ids': ['5586947715'], 'payment_method_id': 'credit_card_1199336'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7425646', 'address1': '6961 Park Drive', 'address2': 'Floor 658', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '48442'}),
            Action(name='modify_user_address', kwargs={'user_id': 'harper_thomas_9402', 'address1': '6961 Park Drive', 'address2': 'Floor 658', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '48442'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction='You are Ava Kovacs, authenticated at ava.kovacs4827@example.com, and you have a pending order that includes a skateboard with a plastic deck, 31-inch length, and plain design. You want to first review the details of this skateboard to confirm its specifications. Later, you would like to update the shipping address to a new location in Dallas and prefer to switch the payment method from your Mastercard to your PayPal account for better transaction tracking. After that, you decide to cancel the entire order because you no longer need the items.\n\nUse ava.kovacs4827@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W4184032'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '6145 Jefferson Avenue', 'address2': 'Suite 84', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '27594'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4184032', 'payment_method_id': 'paypal_7443913'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4184032', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.ahmed8540@example.com',
        instruction="You are assisting Liam Ahmed (email: liam.ahmed8540@example.com) with his order preferences. You want to update the shipping address for his pending order containing a glass 2-liter tea kettle, white size-9 running shoes, a black large cycling helmet, and two dumbbell sets (one adjustable 30-50 lbs, one fixed 55-75 lbs) from the original San Diego address to 7101 Park Drive, Unit 144, San Diego, CA, USA 45100, to ensure delivery to his current location. Later, you would like to explore available options for the Backpack product, particularly interested in variants with camera, hydration, or laptop compartments, in various colors like black, green, grey, or navy, and sizes from small to large, made of nylon, polyester, or leather, to consider adding one to a future order. After that, you would like to cancel the entire order with the reason 'no longer needed', as the items are no longer required. You prefer the refund to be processed back to the original payment method, which was a gift card.\n\nUse liam.ahmed8540@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7534214'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7534214', 'address1': '7101 Park Drive', 'address2': 'Unit 144', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '45100'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7534214', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.johnson7869@example.com',
        instruction='You are assisting James Johnson (email: james.johnson7869@example.com). You want to first explore the available options for the Action Camera product. After reviewing them, you would like to modify the pending order containing an Action Camera, a wristwatch, and a 2000-piece jigsaw puzzle, currently shipping to Chicago. You prefer to change the shipping address to 8284 Jackson Street, Apt 491, Portland, OR, USA 51335. You also want to upgrade the Action Camera from the 1080p model to the 4K model in black, as you prefer higher resolution video capability. You prefer to use your Visa card ending in 2429 for any price adjustment associated with this change.\n\nUse james.johnson7869@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1006327', 'address1': '8284 Jackson Street', 'address2': 'Apt 491', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '51335'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1006327'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1006327', 'item_ids': ['5925362855'], 'new_item_ids': ['6700049080'], 'payment_method_id': 'credit_card_4998749'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.hernandez1120@example.com',
        instruction='You are Ivan Hernandez, with email ivan.hernandez1120@example.com, and you have a pending order currently shipping to Dallas. You want to update the shipping address for this order to 2271 Elm Street, Suite 51, Dallas, TX, USA 48684, to ensure delivery to your updated suite. Later, you would like to return the silver Desk Lamp with low brightness from a previously delivered order, as it does not suit your workspace, and you prefer the refund to be issued back to your gift card for future use. After resolving these logistics, you are interested in exploring the product catalog and would like to see all available product types. Subsequently, you want detailed information about the Laptop model, particularly interested in configurations with space grey color and 15-inch screen size, to evaluate options for a future purchase.\n\nUse ivan.hernandez1120@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4284542', 'address1': '2271 Elm Street', 'address2': 'Suite 51', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '48684'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4284542'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5838674', 'item_ids': ['7453605304'], 'payment_method_id': 'gift_card_9368765'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.santos9317@example.com',
        instruction='You are assisting Isabella Santos (email: isabella.santos9317@example.com), who wants to cancel her pending order containing a gold Smart Watch with a leather band and waterproof synthetic Hiking Boots in size 7 because she no longer needs them. Later, you will update the shipping address for another pending order—which includes a professional dark-skin-tone Makeup Kit, an 8-inch Wi-Fi E-Reader with 32GB storage, and white mesh Running Shoes in size 9—to 5911 Cedar Road, Floor 143, New York, NY, USA 13648, and also update her default address in the system to this new location. After that, you would like to provide her with an overview of the available E-Reader options in the catalog, which include various models differing by screen size (6-inch, 7-inch, or 8-inch), connectivity (Wi-Fi or Wi-Fi + Cellular), and storage (8GB or 32GB). You prefer any refunds from cancellations to be returned to the original credit card used for purchase.\n\nUse isabella.santos9317@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9527030', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9527030'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9667707', 'address1': '5911 Cedar Road', 'address2': 'Floor 143', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '13648'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_santos_1643', 'address1': '5911 Cedar Road', 'address2': 'Floor 143', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '13648'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3801771308'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.kim1995@example.com',
        instruction="You are james.kim1995@example.com. You want to check the details of your pending order containing a black small nylon backpack with a laptop compartment, along with an electric kettle, espresso machine, air purifier, and electric toothbrush. You would like to update the shipping address for this order to 3728 Pine Avenue, Suite 203, San Diego, CA, USA 49188, because you are relocating temporarily. After that, you want your default profile address updated to the same San Diego address for future orders. Later, you decide you no longer need the items, so you would like to cancel the entire order with the reason 'no longer needed'. You prefer the refund to be processed back to the original payment method, which is PayPal.\n\nUse james.kim1995@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9154975'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9154975', 'address1': '3728 Pine Avenue', 'address2': 'Suite 203', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '49188'}),
            Action(name='modify_user_address', kwargs={'user_id': 'james_kim_7213', 'address1': '3728 Pine Avenue', 'address2': 'Suite 203', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '49188'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9154975', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.lopez2997@example.com',
        instruction='You are Raj Lopez (email: raj.lopez2997@example.com) and you want to cancel your pending order that includes a black stainless steel 500ml water bottle, a bamboo 31-inch graphic skateboard, and a pair of size 9 synthetic waterproof hiking boots, because you no longer need these items. After cancellation, you want to explore the full range of available product types in the store to consider future purchases. Later, you would like to update your other pending order—which contains a black polyester small crew neck T-shirt and a bagless canister vacuum cleaner with pet hair removal—from the original Fort Worth address to 123 Oak Avenue, Suite 100, Austin, TX, USA 78701, because you have relocated temporarily. You also prefer to switch the payment method for this order from your Mastercard ending in 3803 to your PayPal account for better purchase protection and budget tracking.\n\nUse raj.lopez2997@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3502364', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3502364'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7162915', 'address1': '123 Oak Avenue', 'address2': 'Suite 100', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '78701'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7162915', 'payment_method_id': 'paypal_7007375'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.smith3991@example.com',
        instruction='You are Emma Smith (emma.smith3991@example.com) with two pending orders. You want to update the shipping address for your laptop order to 7692 Jackson Street, Floor 614, San Diego, CA, USA 52025 because you will be relocating and need the delivery redirected. You also want to know what product types are available in the store to explore future purchases. Later, for your other pending order containing an Action Camera, you would like to exchange the 1080p silver model for the 4K black version because you prefer higher resolution and a more durable finish, and you prefer the price difference to be refunded to your PayPal account.\n\nUse emma.smith3991@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2417020', 'address1': '7692 Jackson Street', 'address2': 'Floor 614', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '52025'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2417020', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3614011'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3614011', 'item_ids': ['5436236388'], 'new_item_ids': ['6700049080'], 'payment_method_id': 'paypal_6228291'}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction="You are Liam Thomas, and your email is liam.thomas9081@example.com. You want to update your pending order currently shipping to Phoenix by changing the delivery address to 9217 Lincoln Street, Suite 637, Dallas, TX, USA 42342, because you've relocated temporarily. You also prefer to switch the payment method for this order to PayPal for better purchase protection. Additionally, you would like to upgrade the 7-inch E-Reader in this order to the 8-inch version for easier reading, and you prefer to pay the small price difference using your Visa card ending in 3194. Later, you want to explore the full range of available products, so you would like to browse a complete list of all product types offered, and then see detailed information about the E-Reader model to consider future purchases. After that, you would like to cancel another pending order that includes a bamboo skateboard, a black 2-piece luggage set, and a blue 20000mAh portable charger, because your travel plans have changed and you no longer need these items. Finally, you would like to return the leather hiking boots from your delivered order because they are not waterproof and don't meet your outdoor needs, and you prefer to receive the refund back to your PayPal account for consistency with the original payment method.\n\nUse liam.thomas9081@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1654931', 'address1': '9217 Lincoln Street', 'address2': 'Suite 637', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '42342'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1654931', 'payment_method_id': 'paypal_3650980'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1654931', 'item_ids': ['6268080249'], 'new_item_ids': ['9494281769'], 'payment_method_id': 'credit_card_3261838'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3801771308'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3295833', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8488728'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8488728', 'item_ids': ['5676696062'], 'payment_method_id': 'paypal_3650980'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen1851@example.com',
        instruction="You are Ava Nguyen (ava.nguyen1851@example.com). You want to change the payment method on your pending order containing a women's woody 30ml perfume from PayPal to your Visa card ending in 3061 because you prefer using that card for this purchase. Later, you will cancel that order because you no longer need the perfume. Separately, for your other pending order containing a 50ft black vinyl garden hose and a professional makeup kit for medium skin tone, you want to update the shipping address to 689 Adams Road, Apt 213, Las Vegas, NV, USA 38117, and also update your default account address to this new Las Vegas location for future orders. You would like to upgrade the garden hose in that order from the 50ft vinyl black model to the 50ft black latex version because you prefer latex for its flexibility and durability. After that, you want to review the full list of product types available in the store to explore other items for potential future purchases.\n\nUse ava.nguyen1851@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8732376'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8732376', 'payment_method_id': 'credit_card_3975380'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8732376', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2601346', 'address1': '689 Adams Road', 'address2': 'Apt 213', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '38117'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_nguyen_4072', 'address1': '689 Adams Road', 'address2': 'Apt 213', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '38117'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2601346', 'item_ids': ['5206946487'], 'new_item_ids': ['4024196380'], 'payment_method_id': 'paypal_3180577'}),
            Action(name='get_product_details', kwargs={'product_id': '6679515468'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.martin5733@example.com',
        instruction='You are assisting Lucas, whose email is lucas.martin5733@example.com. You want to cancel a pending order placed by mistake, which includes a black medium mountain bicycle and other items, because it is no longer needed. Later, you would like to exchange a blue 500ml glass water bottle from a delivered order in Charlotte for a green one of the same size and material, because the green color is preferred. You prefer the refund from the canceled order and exchange to be issued back to the Mastercard ending in 9536.\n\nUse lucas.martin5733@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9318778', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3929227'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3929227', 'item_ids': ['7918497119'], 'new_item_ids': ['5758737025'], 'payment_method_id': 'credit_card_7862034'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.khan2360@example.com',
        instruction='You are Olivia Khan (olivia.khan2360@example.com), and want to loop for some smartphones. Then you want to update the shipping address for your pending order—which includes a red cotton crew neck T-shirt in size S, polarized brown-lens black plastic sunglasses, a large brown memory foam pet bed, and a blue-dial metal-strap wristwatch—from 146 Cedar Street, Suite 863, Indianapolis, IN, 46290 to 1460 Washington Boulevard, Suite 917, New York, NY, 73245. You also want your default address for future orders updated to this new New York address, as you have relocated and need all current and future deliveries sent to your new location.\n\nUse olivia.khan2360@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3840181', 'address1': '1460 Washington Boulevard', 'address2': 'Suite 917', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '73245'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_khan_9030', 'address1': '1460 Washington Boulevard', 'address2': 'Suite 917', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '73245'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.nguyen1293@example.com',
        instruction='You are assisting aarav.nguyen1293@example.com with a pending order that includes a 60% mechanical keyboard with clicky switches and RGB backlighting, a pair of size 7 synthetic hiking boots without waterproofing, and a 25ft green vinyl garden hose. You want to update the shipping address for this order to 4737 Park Drive, Floor 916, Charlotte, NC, USA 71756, as the original Dallas address was incorrect. After updating the address, you would like to cancel the entire order because the items are no longer needed. You prefer the refund to be processed back to the original payment method, which is PayPal.\n\nUse aarav.nguyen1293@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2443586', 'address1': '4737 Park Drive', 'address2': 'Floor 916', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '71756'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2443586'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2443586', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.wilson8748@example.com',
        instruction='You are Evelyn Wilson, and your email is evelyn.wilson8748@example.com. You want to update the shipping address for your pending order—which includes a digital wall clock, a gold 128GB tablet, a HEPA air purifier for large rooms, and a robotic vacuum cleaner—to 9182 Main Street, Unit 564, Denver, CO, USA 21497, because your current address in Seattle is outdated. You also want your default address updated to the same Denver address for future orders. Later, you would like to return the red medium-sized cycling helmet with high ventilation from your recently delivered order, as it is no longer needed, and you prefer to receive a refund back to the original gift card used for the purchase.\n\nUse evelyn.wilson8748@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7381650', 'address1': '9182 Main Street', 'address2': 'Unit 564', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '21497'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_wilson_8460', 'address1': '9182 Main Street', 'address2': 'Unit 564', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '21497'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6392164', 'item_ids': ['8573379326'], 'payment_method_id': 'gift_card_8931217'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.rossi2645@example.com',
        instruction='You are Sofia Rossi (sofia.rossi2645@example.com). You want to update the shipping address for a pending order containing a perfume, skateboard, and two action cameras to 326 Adams Road, Unit 485, Portland, OR, USA 78651 because you need it delivered to a new location. Later, you would like to exchange the delivered canister, bagless vacuum cleaner with HEPA filter for a similar canister, bagless model that includes pet hair removal functionality because it performs better for your household needs. You prefer the price difference to be processed using your Mastercard ending in 3357. After that, you would like to cancel another pending order that includes a makeup kit, espresso coffee maker, tablet, and red leather office chair because it was purchased by mistake.\n\nUse sofia.rossi2645@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5918442', 'address1': '326 Adams Road', 'address2': 'Unit 485', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '78651'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5918442'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8535951', 'item_ids': ['1304426904'], 'new_item_ids': ['7958300294'], 'payment_method_id': 'credit_card_5051208'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5500815', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.muller6448@example.com',
        instruction='You are assisting a customer, fatima.muller6448@example.com, who has a pending order currently shipping to Chicago. You want to update the shipping address for this order to 3865 Cedar Road, Floor 204, New York, NY, USA 57824, because the recipient plans to receive it at a new location. Later, you would like to cancel the entire order because the customer no longer needs the items—a mechanical keyboard with linear switches and no backlight, and a stainless steel 2-liter tea kettle compatible with gas stovetops—after deciding against setting up a new home office. You prefer the refund to be processed back to the original payment method, PayPal.\n\nUse fatima.muller6448@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9962383', 'address1': '3865 Cedar Road', 'address2': 'Floor 204', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '57824'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9962383', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9962383'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.gonzalez8775@example.com',
        instruction='You are Mei Gonzalez, with email mei.gonzalez8775@example.com, and you want to update the shipping address for your pending order—containing a soft cover A5 notebook, a portable gas grill with side burner, a white wireless laser gaming mouse, a black large fleece jacket, and a red mesh office chair—to 6642 Washington Boulevard, Floor 394, Philadelphia, PA, USA 36715, in case the order has already been processed. Later, you would like to cancel the entire order because you no longer need these items. After that, you would like to see all available product types in the catalog for future reference, so you can explore what options are currently offered.\n\nUse mei.gonzalez8775@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2052757', 'address1': '6642 Washington Boulevard', 'address2': 'Floor 394', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '36715'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2052757', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2052757'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.lopez3569@example.com',
        instruction='You are Ava Lopez, and your email is ava.lopez3569@example.com. You want to update the shipping address for your pending order—which includes a bamboo 34-inch custom-design skateboard, white wired on-ear headphones, a medium-room HEPA air purifier with night mode, a black 17-inch i7 laptop with 32GB RAM and 1TB SSD, and polarized brown-lens black plastic sunglasses—to 5574 Washington Boulevard, Unit 496, Boston, MA, USA 85558, because the original address was incorrect. Later, you decided you no longer need the items and would like to cancel the entire order. Since the order was paid using a gift card, you prefer any refund to be returned to the same gift card.\n\nUse ava.lopez3569@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8327915', 'address1': '5574 Washington Boulevard', 'address2': 'Unit 496', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '85558'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8327915'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8327915', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, and your email is olivia.ito5204@example.com. You have a pending order that includes a black wired optical gaming mouse, a red 7 ft polyester patio umbrella with manual tilt, and a size 8 leather waterproof hiking boot. You want to update the shipping address to 3221 Washington Boulevard, Apt 164, Detroit, MI, USA 30476 because the original Denver address is no longer valid. You also prefer to switch the payment method from your Visa ending in 9182 to your PayPal account for better purchase protection. Later, you would like to review the full details of this order to confirm the changes. After that, you want to see the product details for the gaming mouse you ordered—specifically the black, wired, optical model—to understand its features and verify it meets your gaming setup needs.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '3221 Washington Boulevard', 'address2': 'Apt 164', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '30476'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
            Action(name='get_product_details', kwargs={'product_id': '5713490933'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.kim1995@example.com',
        instruction='You are assisting James Kim (james.kim1995@example.com) with several order modifications. You want to first explore the full range of product types available in the catalog to understand what items are offered. Then, you want to update the shipping address for a pending order containing a black nylon small backpack, a 1L glass electric kettle, an espresso machine, an air purifier, and an electric toothbrush from San Antonio, TX to 3856 Washington Boulevard, Unit 544, Las Vegas, NV, USA 31664. Later, you would like to modify another pending order that includes hiking boots (size 10, synthetic, non-waterproof), a wristwatch, and a mechanical keyboard by exchanging the current hiking boots for a waterproof version in the same size and material, preferring the upgraded functionality for outdoor use, and you prefer to use your PayPal account to cover any price difference. After that, you would like to cancel the first order (originally intended for San Antonio and updated to Las Vegas) because you no longer need the items.\n\nUse james.kim1995@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9154975', 'address1': '3856 Washington Boulevard', 'address2': 'Unit 544', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '31664'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3289292'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3289292', 'item_ids': ['4127323219'], 'new_item_ids': ['1615379700'], 'payment_method_id': 'paypal_8963303'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9154975', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.johnson2279@example.com',
        instruction='You are Daiki Johnson, and your email is daiki.johnson2279@example.com. You want to update the shipping address for your pending order containing a 1-liter glass tea kettle with gas stovetop compatibility to 9478 Cedar Road, Apt 344, Fort Worth, TX, USA 84924, because you realized the original address was incorrect. Later, you would like to cancel the order entirely because you made the purchase by mistake. After that, you are interested in learning more about the Backpack product, particularly variants with a camera or laptop compartment, made from nylon or polyester, in sizes ranging from small to large, as you are considering a future purchase.\n\nUse daiki.johnson2279@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1436802', 'address1': '9478 Cedar Road', 'address2': 'Apt 344', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '84924'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1436802', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1436802'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are assisting Liam Thomas (email: liam.thomas9081@example.com). You want to exchange the non-waterproof hiking boots (size 11, leather) from the delivered order to the same style in waterproof version because they were not suitable for wet conditions. You prefer the waterproof model in the same size and material for better outdoor performance. You prefer the price difference to be handled using your PayPal account. Later, you would like to update the shipping address for your pending order (which includes a bamboo skateboard, 2-piece black luggage set, and a 20000mAh blue portable charger) to 5478 Lincoln Street, Unit 335, Phoenix, AZ, USA 54341. After that, you would like to cancel that same pending order because it was placed by mistake.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8488728'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8488728', 'item_ids': ['5676696062'], 'new_item_ids': ['6159919747'], 'payment_method_id': 'paypal_3650980'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3295833', 'address1': '5478 Lincoln Street', 'address2': 'Unit 335', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '54341'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3295833', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting Lucas Johansson (lucas.johansson7741@example.com), who has a pending order currently shipping to San Francisco, CA. You want to update the shipping address to 2427 Park Drive, Suite 446, Fort Worth, TX, USA 87364, because he will be relocating. You also want to exchange the small black nylon backpack with a laptop compartment for a large black nylon backpack with a camera compartment, because he prefers more space and dedicated camera storage for travel photography. You authorize any price adjustment to be processed using your Visa card ending in 9452, noting the replacement item is slightly lower in price. Later, after considering the changes, you decide to cancel the entire order because your plans have changed and you no longer need the items.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '2427 Park Drive', 'address2': 'Suite 446', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '87364'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5073920', 'item_ids': ['7824298782'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'credit_card_1864112'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting a customer with email yusuf.gonzalez2399@example.com who has a pending order originally shipped to Los Angeles. You want to first update the shipping address to a new location in Phoenix because the customer expected to receive the items there. Later, you will cancel the entire order because the customer no longer needs the Smartphone and Tea Kettle. Before canceling, you would like to review the order contents and understand the features of the ceramic 1.5-liter Tea Kettle compatible with gas stovetops, which was part of the order. After cancellation, you are interested in browsing all available product types in the catalog to explore future purchase options, particularly items like Air Purifiers, Coffee Makers, or Smart Home devices. You prefer the refund to be issued back to the original payment method, which is the credit card used for the purchase.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '7955 Elm Street', 'address2': 'Floor 161', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '64365'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2806889', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
            Action(name='get_product_details', kwargs={'product_id': '9832717871'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are Liam Thomas, and your email is liam.thomas9081@example.com. You want to update the shipping address for your pending order containing an E-Reader and Air Purifier to 1708 Oak Avenue, Apt 659, San Diego, CA, USA 55276, because you recently moved. You also want your default account address updated to this new San Diego address for future orders. After that, you would like to cancel the pending order because you realized it was placed by mistake. Later, you would like to exchange your delivered Hiking Boots (size 11, leather, non-waterproof) for a waterproof version, because you need them for wet trail conditions. You prefer the refund for the cancelled order to be returned to the original payment method, which is your Visa card ending in 3194.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1654931', 'address1': '1708 Oak Avenue', 'address2': 'Apt 659', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '55276'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_thomas_7882', 'address1': '1708 Oak Avenue', 'address2': 'Apt 659', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '55276'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1654931', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1654931'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8488728', 'item_ids': ['5676696062'], 'new_item_ids': ['6159919747'], 'payment_method_id': 'paypal_3650980'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.sanchez1292@example.com',
        instruction='You are Aarav Sanchez, authenticated at aarav.sanchez1292@example.com, and you want to update the shipping address for your pending order (which includes a skateboard, jigsaw puzzle, grill, headphones, and mechanical keyboard) from Houston to 1209 Pine Avenue, Floor 6, Denver, CO, USA 92161 because you entered the wrong address initially. You also want your default address in the system updated to the same Denver address to ensure all future orders are delivered correctly.\n\nUse aarav.sanchez1292@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6348442', 'address1': '1209 Pine Avenue', 'address2': 'Floor 6', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '92161'}),
            Action(name='modify_user_address', kwargs={'user_id': 'aarav_sanchez_9729', 'address1': '1209 Pine Avenue', 'address2': 'Floor 6', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '92161'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are Yusuf Garcia, with email yusuf.garcia2909@example.com, and you have an order in Indianapolis for hiking boots size 11, a 13-inch black laptop with i7 processor and 32GB RAM, and an air purifier for small rooms. You want to know the status of this order. You initially paid using a gift card, but you would like to update the payment method for this order. You prefer to pay using your Mastercard ending in 3762 instead, as you want to preserve the remaining gift card balance for future purchases.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li7352@example.com',
        instruction='You are Sofia Li (sofia.li7352@example.com) and you want to update the shipping address for your pending order—containing an Air Purifier for medium rooms, a pair of size 7 synthetic hiking boots, a 34-inch plastic skateboard, and a 6mm pink natural rubber yoga mat—to 9528 Madison Drive, Unit 651, Nashville, TN, USA 95135 because you initially entered the wrong address. You also want to change the payment method from your Visa card ending in 6791 to your PayPal account for greater convenience and payment flexibility.\n\nUse sofia.li7352@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8855135', 'address1': '9528 Madison Drive', 'address2': 'Unit 651', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '95135'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8855135', 'payment_method_id': 'paypal_8194385'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com). You want to return the black Electric Toothbrush with rechargeable battery from a delivered order that included a Bluetooth Speaker, Perfume, and Action Camera, because it is no longer needed. You prefer the refund to be processed to your PayPal account for convenience. Later, for a pending order containing a size 11 leather waterproof Hiking Boot, a Laptop, and an Air Purifier, you want to update the shipping address to 9239 Jefferson Avenue, Suite 451, Jacksonville, FL, USA 18704, to ensure delivery to your new location. After that, you would like to change the payment method from gift card to your Mastercard ending in 3762 for better expense tracking. Subsequently, you want to exchange the current Hiking Boots for the size 12 version with the same leather and waterproof features, charging any price difference to the same Mastercard. Finally, you decide to cancel the entire pending order as your needs have changed. After resolving these order matters, you would like to review all available product types in the catalog to explore future purchase options.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2286012'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2286012', 'item_ids': ['8098621301'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '9239 Jefferson Avenue', 'address2': 'Suite 451', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '18704'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2564042', 'item_ids': ['6159919747'], 'new_item_ids': ['8277474082'], 'payment_method_id': 'credit_card_8405687'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.gonzalez8775@example.com',
        instruction='You are Mei Gonzalez, with email mei.gonzalez8775@example.com, and you want to exchange the navy small backpack from your delivered order for a black large backpack with a laptop compartment because you prefer the larger size and darker color for daily use. You would like the price difference to be handled using your PayPal account. Later, you would like to update the shipping address for your pending order to 5779 Cedar Road, Suite 610, Austin, TX, USA 34399, and change the payment method to your Visa card ending in 3742 for consistency with your preferred payment method. After that, you would like to cancel the entire pending order as you no longer need the items. Finally, you would like to see a list of all product types currently available in the catalog to explore other options.\n\nUse mei.gonzalez8775@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7303089'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7303089', 'item_ids': ['2492465580'], 'new_item_ids': ['8054888773'], 'payment_method_id': 'paypal_2568958'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2052757', 'address1': '5779 Cedar Road', 'address2': 'Suite 610', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '34399'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2052757', 'payment_method_id': 'credit_card_4387170'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2052757', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are Fatima Li (email: fatima.li1185@example.com) and help with your pending order. You want to update the shipping address to 1122 Elm Street, Apt 355, San Antonio, TX, USA 93112 because she prefers delivery to that location. Then, you would like to change the payment method from PayPal to her Mastercard ending in 1531 for greater convenience. After that, you prefer to exchange the current skateboard with a maple deck for the bamboo deck version, keeping the same 31-inch length and graphic design, because she prefers the sustainability and lighter weight of bamboo. Later, you decide to cancel the entire order because she no longer needs the items. Before finalizing the cancellation, you would like to explore the available skateboard options in the catalog to understand what other styles and materials are offered, particularly those with bamboo decks and similar dimensions, for future orders.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8005719', 'address1': '1122 Elm Street', 'address2': 'Apt 355', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '93112'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8005719', 'payment_method_id': 'credit_card_2713802'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8005719', 'item_ids': ['5120532699'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'credit_card_2713802'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8005719', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.kovacs6946@example.com',
        instruction='You are a customer with email harper.kovacs6946@example.com who initially wants to explore the product catalog, particularly Electric Kettles. Then you want to update the shipping address for a pending Wristwatch order to a new location in Boston because the customer plans to be there soon. Later, you will cancel this order entirely because it was placed by mistake. After that, you would like to manage a delivered order by returning one 1L black glass Electric Kettle because it is smaller than needed. You prefer to exchange a 2L silver glass Electric Kettle for a 2L white glass model because you prefer the white color for kitchen aesthetics. You prefer any financial adjustments to be handled using the PayPal account already on file, as it was used for the original purchase.\n\nUse harper.kovacs6946@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1075968781'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7775097', 'address1': '2224 Main Street', 'address2': 'Apt 932', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '21014'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7775097', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5955464'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5955464', 'item_ids': ['2323972008'], 'payment_method_id': 'paypal_3246095'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5955464', 'item_ids': ['3015420423'], 'new_item_ids': ['4064702754'], 'payment_method_id': 'paypal_3246095'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are assisting James Martin (james.martin9857@example.com) with his pending order. You want to update the shipping address to 1662 Maple Lane, Unit 30, Philadelphia, PA, USA 54862 because he needs it delivered to a new location. You would like to change the payment method from PayPal to your Mastercard ending in 2067 for better expense tracking. You also prefer to exchange the green small polyester backpack with camera compartment for the black large nylon one with camera compartment because it better suits your needs in terms of size, color, and material. Later, after considering the changes, you decide the order is no longer necessary and would like to cancel the entire order.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '1662 Maple Lane', 'address2': 'Unit 30', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '54862'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3043531', 'payment_method_id': 'credit_card_6932154'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3043531', 'item_ids': ['9851293632'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'credit_card_7083997'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3043531', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction="You are assisting Ava Kovacs (email: ava.kovacs4827@example.com) with her pending order containing a skateboard with a plain design and plastic deck, wireless black over-ear headphones, a 50ft rubber garden hose in green, and a ceramic tea kettle with 1.5-liter capacity. You want to update the shipping address to 918 Adams Road, Floor 310, Detroit, MI, USA 96021 because the original Phoenix address is no longer valid. After that, you would like to change the payment method from Mastercard to PayPal for better transaction tracking. You also reserve the option to cancel the order later with the reason 'no longer needed' if circumstances change. After handling these order modifications, you would like to browse all available product types in the catalog to explore future purchase options, including items like air purifiers, espresso machines, smartwatches, and yoga mats.\n\nUse ava.kovacs4827@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '918 Adams Road', 'address2': 'Floor 310', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '96021'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4184032', 'payment_method_id': 'paypal_7443913'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4184032', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4184032'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.lee9297@example.com',
        instruction='You are Liam Lee, authenticated by the email liam.lee9297@example.com. You are initially interested in learning about the Backpack product, particularly its available styles and features, to understand if it fits your needs for outdoor use. Later, you want to update the shipping address for your pending order—containing an Electric Kettle, a Yoga Mat, and Headphones—to 7211 Washington Boulevard, Unit 528, San Diego, CA, USA 45583, because you will be traveling and prefer delivery to that location. You also want your default address updated to this new San Diego address for future orders. However, after making these changes, you realize the order was placed by mistake, so you later decide to cancel the entire pending order. You prefer the refund to be issued back to your Mastercard ending in 3695, which was used for the original purchase.\n\nUse liam.lee9297@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2624389'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2624389', 'address1': '7211 Washington Boulevard', 'address2': 'Unit 528', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '45583'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_lee_5696', 'address1': '7211 Washington Boulevard', 'address2': 'Unit 528', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '45583'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2624389', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are Ethan Thomas, and your email is ethan.thomas7730@example.com. You want to update the payment method for your pending order (containing a black Smart Watch with silicone band and a gold Smartphone) from a gift card to your Visa card ending in 8901, because you prefer using your credit card for tracking and rewards. You also want to change the Smart Watch display from AMOLED to LCD while keeping the black color and silicone band, because you prefer lower power consumption and glare reduction in bright environments, and you want any price difference handled using the same Visa card. Later, you would like to update the shipping address for this pending order to 3645 Washington Boulevard, Apt 242, Portland, OR, USA 36575, and also set this as your default address, to ensure future deliveries go to your new residence. After that, you would like to return the brown medium memory foam Pet Bed from your delivered order (which also included a clicky mechanical keyboard, a 4K indoor security camera, and a space grey laptop), because it does not match your home decor, and you prefer a refund to your PayPal account for ease of use and quick access to funds.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'credit_card_7472558'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8465042', 'item_ids': ['4920090458'], 'new_item_ids': ['2860956907'], 'payment_method_id': 'credit_card_7472558'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '3645 Washington Boulevard', 'address2': 'Apt 242', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '36575'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_thomas_1791', 'address1': '3645 Washington Boulevard', 'address2': 'Apt 242', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '36575'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['5067898160'], 'payment_method_id': 'paypal_6982172'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen1851@example.com',
        instruction="You are assisting Ava Nguyen (email: ava.nguyen1851@example.com) with her pending order originally containing a women's woody 30ml perfume. You want to update the shipping address to 2013 Madison Drive, Suite 669, San Antonio, TX, USA 97273, because she prefers delivery to this new location. After that, you would like to change the payment method to the Visa card ending in 3061 for her convenience. You also prefer to exchange the current women's version of the woody-scented 30ml perfume for the men's version of the same size and scent family, as it better suits the intended recipient. Later, after considering the changes, you decide to cancel the entire order because she no longer needs the item.\n\nUse ava.nguyen1851@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8732376', 'address1': '2013 Madison Drive', 'address2': 'Suite 669', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '97273'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8732376', 'payment_method_id': 'credit_card_3975380'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8732376', 'item_ids': ['8316205423'], 'new_item_ids': ['5081446110'], 'payment_method_id': 'credit_card_3975380'}),
            Action(name='get_product_details', kwargs={'product_id': '6858788497'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8732376'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8732376', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, with email olivia.ito5204@example.com. You are managing several orders and account preferences. First, for your pending order containing a black wired Gaming Mouse, Patio Umbrella, and Hiking Boots, you want to change the payment method from credit card to PayPal and replace the black wired Gaming Mouse with the white wireless version, because you prefer a cleaner aesthetic and wireless convenience; you want any price difference handled via PayPal. Later, you want to update the shipping address for this order to 8404 Cedar Road, Unit 866, Los Angeles, CA, USA 34341, and also set this as your new default address for future orders. For your delivered order containing a 19 bar automatic espresso machine and black sneakers, you would like to exchange the current espresso machine for the 19 bar, 2L, manual type because you prefer more control over brewing, and return the sneakers because they don’t fit; you prefer any refund or additional charge to be processed to your PayPal account. After that, you would like to cancel your other pending order containing a white-dial leather-strap wristwatch and a grey medium backpack, because you no longer need those items.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5442520', 'item_ids': ['3330317167'], 'new_item_ids': ['8896479688'], 'payment_method_id': 'paypal_8049766'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '8404 Cedar Road', 'address2': 'Unit 866', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '34341'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_ito_3591', 'address1': '8404 Cedar Road', 'address2': 'Unit 866', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '34341'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5866402', 'item_ids': ['6242772310'], 'new_item_ids': ['3379843752'], 'payment_method_id': 'paypal_8049766'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5866402', 'item_ids': ['9727387530'], 'payment_method_id': 'paypal_8049766'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7941031', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan.lopez7539@example.com',
        instruction='You are Juan Lopez (email: juan.lopez7539@example.com) and want assistant with your pending order. You want to update the shipping address to 4119 Park Drive, Suite 575, Fort Worth, TX, USA 46066 because the original address was incorrect. After updating the address, you would like to cancel the entire order because the items — a blue medium cycling helmet with low ventilation, a 50ft green vinyl garden hose, and a 2L automatic espresso machine with 9 bar pressure — are no longer needed. You prefer the refund to be processed back to the original payment method, PayPal, which was used for the purchase.\n\nUse juan.lopez7539@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3386832', 'address1': '4119 Park Drive', 'address2': 'Suite 575', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '46066'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3386832', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3386832'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.moore4245@example.com',
        instruction='You are customer with email raj.moore4245@example.com who first wants to browse the full range of product types available in the store catalog. You are to provide a complete list of product categories to support your browsing. Later, for your pending order containing a brown polyester pet bed (small), a red stainless steel 1000ml water bottle, a blue Bluetooth speaker with 10-hour battery life, a green 6mm PVC yoga mat, and a blue cycling helmet (size L), you are to update the shipping address from Washington, DC to 9056 Washington Boulevard, Suite 252, Nashville, TN, USA 56951, as the delivery location has changed. After that, you are to cancel the entire order, as you have decided the items are no longer needed and no longer wishes to proceed with the purchase, despite the prior address update.\n\nUse raj.moore4245@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9929926', 'address1': '9056 Washington Boulevard', 'address2': 'Suite 252', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '56951'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9929926', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.li2787@example.com',
        instruction='You are assisting a customer with email raj.li2787@example.com who has a pending order. You want to update the payment method to PayPal for convenience. You would like to exchange the black glass 5 ft bookshelf for the white wood 5 ft bookshelf because you prefer a more natural and lighter look that better matches your living room decor. You also want to update the shipping address to 4615 Washington Boulevard, Unit 991, Denver, CO, USA 90428, as the item is now intended for a different location. Later, after considering your needs, you decide to cancel the entire order because you no longer require the items.\n\nUse raj.li2787@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8967935'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8967935', 'payment_method_id': 'paypal_2028062'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8967935', 'item_ids': ['4900661478'], 'new_item_ids': ['8479046075'], 'payment_method_id': 'paypal_2028062'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8967935', 'address1': '4615 Washington Boulevard', 'address2': 'Unit 991', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '90428'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8967935', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.ahmed1696@example.com',
        instruction='You are assisting Lei Ahmed (email: lei.ahmed1696@example.com) with her pending order. You want to first update the shipping address to 4980 Jefferson Avenue, Suite 71, Philadelphia, PA, USA 85530 because she prefers delivery to this location. Then, you would like to change one of the cycling helmets from black L size with low ventilation to the white L size with medium ventilation because she prefers the color and ventilation level for better comfort and visibility. You prefer any price adjustment to be processed using her Mastercard ending in 3705. Later, you will cancel the entire order because she no longer needs the items, making the earlier updates moot, but the cancellation takes precedence as her final decision.\n\nUse lei.ahmed1696@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9132840', 'address1': '4980 Jefferson Avenue', 'address2': 'Suite 71', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '85530'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9132840'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9132840', 'item_ids': ['6048672633'], 'new_item_ids': ['6697922351'], 'payment_method_id': 'credit_card_3593714'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9132840', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.kim6594@example.com',
        instruction='You are assisting a customer with email mei.kim6594@example.com who placed a pending order for an espresso machine and a mechanical keyboard. You want to cancel the entire order because it was placed by mistake. You prefer the refund to be returned to the original payment method, which is the gift card used for the purchase. After cancellation, you would like confirmation that the gift card balance has been restored.\n\nUse mei.kim6594@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3263208', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3263208'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.santos1752@example.com',
        instruction='You are a customer with email omar.santos1752@example.com who placed a pending order for a robotic vacuum cleaner with pet hair removal, two navy XL fleece jackets (one with full zipper, one with half), and a black nylon backpack with a hydration compartment. You want to update the shipping address to 2559 Elm Street, Floor 21, Austin, TX, USA 26976 because the original address in Fort Worth was incorrect. Later, you would like to cancel the entire order because it was placed by mistake, even after the address update, and you no longer wish to proceed with the purchase. You prefer the refund to be issued back to the original gift card used for payment.\n\nUse omar.santos1752@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9121070', 'address1': '2559 Elm Street', 'address2': 'Floor 21', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '26976'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9121070', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are assisting Sophia Thomas (sophia.thomas1364@example.com) with her retail requests. You want to update the shipping address for her pending order—which includes a white wooden bookshelf, a 7-inch silver tablet, a blue fabric office chair, and a gray leather high-back office chair—currently shipping to Dallas, TX, to a new address: 3208 Lincoln Street, Apt 647, New York, NY, USA 35428, because she has relocated. You also prefer to change the payment method from PayPal to your Visa card ending in 9858 for better expense tracking. Later, you would like to explore the product catalog, specifically learning about backpacks, and review available options such as camera-ready or laptop-compartment styles in various colors, sizes, and materials. After browsing, you decide to cancel the same pending order because you no longer need the items.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4862767', 'address1': '3208 Lincoln Street', 'address2': 'Apt 647', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '35428'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4862767', 'payment_method_id': 'credit_card_7326294'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4862767'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4862767', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.brown5032@example.com',
        instruction='You are assisting Emma Brown (emma.brown5032@example.com) with her pending order. You want to first update the shipping address to 4958 Lincoln Street, Suite 612, San Jose, CA, USA 21054, because it needs to be delivered to a new location. Then, you would like to change the payment method from PayPal to your Visa card ending in 9135 for better expense tracking. After that, you prefer to exchange the current skateboard (plastic, 34 inch, plain) for a more durable bamboo deck with a 31 inch length and graphic design, as it better suits your style and riding preference, and you want any price difference applied to the same Visa card. Later, you decide to cancel the entire order as you no longer need the skateboard.\n\nUse emma.brown5032@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6460787', 'address1': '4958 Lincoln Street', 'address2': 'Suite 612', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '21054'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6460787', 'payment_method_id': 'credit_card_8850930'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6460787', 'item_ids': ['3098764622'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'credit_card_8850930'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6460787', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6460787'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.kovacs4296@example.com',
        instruction="You are Mei Kovacs (mei.kovacs4296@example.com), who first wanted to explore the full range of product types offered before updating the shipping address for your pending order containing a black 20000mAh wireless portable charger, a large electric grill with rotisserie, a silver 1.5L plastic electric kettle, a 1000-piece beginner animal-themed jigsaw puzzle, and a 25ft blue vinyl garden hose, currently shipping to Columbus, OH. Based on these you will make informed decisions after few days. After browsing, you would have updated the shipping address for this order to 4177 Main Street, Unit 991, Phoenix, AZ, USA 61021, had she not changed her mind. After reconsidering, you now need to cancel this order with the reason 'no longer needed', as you no longer requires these items. After cancellation, you would like to confirm the updated order status to ensure it reflects the cancellation accurately. You prefer the refund to be processed back to the original payment method, which was a gift card.\n\nUse mei.kovacs4296@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8193638', 'address1': '4177 Main Street', 'address2': 'Unit 991', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '61021'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8193638', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8193638'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.li8523@example.com',
        instruction='You are Liam Li (email: liam.li8523@example.com) and need help with a pending order. You want to first update the Dumbbell Set from the 30-50 lbs urethane fixed version to the 55-75 lbs iron fixed version because he prefers a heavier, more durable set for his workouts. You prefer the price difference to be covered using his PayPal account. Later, you would like to update the shipping address to 7322 Cedar Road, Suite 25, Houston, TX, USA 37992, to align with his current residence. After that, you would like to cancel the entire order because you realized the purchase was made by mistake and no longer needs the equipment.\n\nUse liam.li8523@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1130240'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1130240', 'item_ids': ['7159180318'], 'new_item_ids': ['2444431651'], 'payment_method_id': 'paypal_9619477'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1130240', 'address1': '7322 Cedar Road', 'address2': 'Suite 25', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '37992'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1130240', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen2868@example.com',
        instruction='You are Ava Nguyen (email: ava.nguyen2868@example.com) and want help with your pending order. You want to update the shipping address to 9774 Elm Street, Apt 475, Las Vegas, NV, USA 17972 because you moved. You also want to exchange the red fleece jacket with half zipper (size L) for the black fleece jacket with full zipper in the same size because it better suits your preference for style and functionality. You prefer to use the Mastercard ending in 6081 for any price difference. Later, you will decide to cancel the entire order because you no longer need the items.\n\nUse ava.nguyen2868@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8367380', 'address1': '9774 Elm Street', 'address2': 'Apt 475', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '17972'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8367380'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8367380', 'item_ids': ['8733974883'], 'new_item_ids': ['9385662952'], 'payment_method_id': 'credit_card_5683823'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8367380', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.muller6617@example.com',
        instruction="You are assisting a customer who placed a pending order for several household items and has decided to cancel the entire order because they no longer need the items. The order includes a 500ml stainless steel green water bottle, an upright bagged vacuum cleaner with pet hair removal, a 1-liter glass tea kettle compatible with electric stoves, a 19-bar automatic espresso machine with a 1.5L water tank, and a 12-inch white analog wall clock, all shipped to Denver, CO. You want to cancel this entire order. Before finalizing the cancellation, you reviewed the water bottle's product details to confirm its specifications—specifically noting it is a 500ml stainless steel green model—and decided no replacement or exchange is needed. You prefer the refund to be processed back to the original payment method, which is the credit card used for the purchase. After that, you would like confirmation that the cancellation has been completed and the refund initiated.\n\nUse ethan.muller6617@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4683557', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4683557'}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting Ethan Thomas (email: ethan.thomas7730@example.com). You want to cancel a pending order placed by mistake that includes a black Smart Watch with a silicone band and AMOLED display, and a gold Smartphone with 128GB storage and a 5.8-inch screen, shipping to Columbus. Later, you would like to return the medium brown memory foam Pet Bed from a delivered order that shipped to Chicago, because it is no longer needed. You prefer the refund for the returned item to be processed back to the original payment method, which is PayPal.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['5067898160'], 'payment_method_id': 'paypal_6982172'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah.hernandez4161@example.com',
        instruction='You are assisting a customer with email noah.hernandez4161@example.com who has a pending order originally shipping to Chicago. You want to update the shipping address for the order to 6299 Jackson Street, Unit 161, Los Angeles, CA, USA 88932, as the recipient is now in Los Angeles. Later, you would like to cancel the entire order because the customer no longer needs the 7-inch e-reader with Wi-Fi + Cellular connectivity and 8GB storage. You prefer the refund to be processed back to the original payment method, which was a gift card.\n\nUse noah.hernandez4161@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3897284', 'address1': '6299 Jackson Street', 'address2': 'Unit 161', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '88932'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3897284', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.kim8981@example.com',
        instruction='You are assisting Omar Kim (email: omar.kim8981@example.com) with his pending order. You want to update the payment method to his Mastercard ending in 9843 because he prefers using his card over the original gift card. Then, you would like to change the cycling helmet from white to black in the same size (S) because he prefers the black color. After that, you want to update the shipping address to 296 Lincoln Street, Floor 606, San Diego, CA, USA 72869, as the original Jacksonville address is no longer valid. Later, you will cancel the entire order because he has decided he no longer needs the items.\n\nUse omar.kim8981@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8557584'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8557584', 'payment_method_id': 'credit_card_3577130'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8557584', 'item_ids': ['1596993217'], 'new_item_ids': ['5537798301'], 'payment_method_id': 'credit_card_3577130'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8557584', 'address1': '296 Lincoln Street', 'address2': 'Floor 606', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '72869'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8557584', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),
]
