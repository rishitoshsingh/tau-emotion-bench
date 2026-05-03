from tau_emotionbench.types import Task, Action


TASKS = [
    Task(
        user_id='aarav.sanchez1292@example.com',
        instruction='You are assisting Aarav Sanchez, whose email is aarav.sanchez1292@example.com. You want to exchange the Hiking Boots in size 7 from his delivered order (which included a backpack, coffee maker, air purifier, and puzzle, delivered to Houston) for a new pair in size 10, because the original size was too small. You prefer the replacement boots to have the same synthetic and waterproof features as the original. You prefer to use the Mastercard ending in 5506 to cover any price difference.\n\nUse aarav.sanchez1292@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5455653'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5455653', 'item_ids': ['1262139877'], 'new_item_ids': ['1615379700'], 'payment_method_id': 'credit_card_2690859'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito (olivia.ito5204@example.com). You want to update the shipping address for your pending order—containing a black wired optical gaming mouse, a red 7 ft polyester patio umbrella with manual tilt, and a size 8 leather waterproof hiking boot—to 9975 Jefferson Avenue, Apt 472, Detroit, MI, USA 69387, because you initially planned to have it delivered there. Later, you would like to cancel the entire order because you no longer need the items. After that, you would like confirmation that the order has been successfully cancelled. You prefer the refund to be processed back to the original payment method, the credit card used for the purchase.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '9975 Jefferson Avenue', 'address2': 'Apt 472', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '69387'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5442520', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.martin5733@example.com',
        instruction='You are Lucas Martin, with email lucas.martin5733@example.com. You want to update the shipping address for your pending order—containing a black medium mountain bicycle, a clicky full-size mechanical keyboard, a white digital wall clock, and two air purifiers—from Washington, DC to your new address in Charlotte, NC (499 Broadway, Suite 351). After that, you would like to cancel the entire order because it was placed by mistake. Separately, for your delivered order that includes an espresso machine, a blue glass 500ml water bottle, a leather-strapped black-dial wristwatch, blue wireless over-ear headphones, and an 8-inch e-reader, you want to exchange the blue glass 500ml water bottle for the black stainless steel 500ml version because you prefer a more durable material. You prefer the price difference to be processed using your Mastercard ending in 9536.\n\nUse lucas.martin5733@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9318778', 'address1': '499 Broadway', 'address2': 'Suite 351', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '28205'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9318778', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3929227'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3929227', 'item_ids': ['7918497119'], 'new_item_ids': ['3453331371'], 'payment_method_id': 'credit_card_7862034'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen1851@example.com',
        instruction="You are Ava Nguyen, authenticated via email ava.nguyen1851@example.com, and you want to cancel your pending order containing a 30ml women's woody-scented perfume because you no longer need it. After that, you would like to update the shipping address for your other pending order—which includes a 50ft black vinyl garden hose and a professional-sized makeup kit for medium skin tone—to 8605 Adams Road, Suite 614, Boston, MA, USA 22243. You also prefer this new Boston address to become your default for all future orders. You used PayPal for both purchases and expect any refund from the cancellation to be returned to the same payment method.\n\nUse ava.nguyen1851@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8732376', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8732376'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2601346', 'address1': '8605 Adams Road', 'address2': 'Suite 614', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '22243'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_nguyen_4072', 'address1': '8605 Adams Road', 'address2': 'Suite 614', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '22243'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen1851@example.com',
        instruction="You are assisting Ava Nguyen (email: ava.nguyen1851@example.com). You want to cancel a pending order for a women's woody-scented 30ml perfume because it was ordered by mistake. Later, for another pending order that includes a 50ft vinyl black garden hose and a professional makeup kit for medium skin tone, you would like to update the shipping address to 123 Oak Street, Suite 100, Charlotte, NC, USA 28251. You also prefer to change the payment method to your Visa card ending in 3061 for this order. Additionally, you want to exchange the 50ft vinyl black garden hose for the 50ft latex black version because you prefer latex material for its durability and flexibility. After that, you would like to review the full catalog of available product types to explore other offerings in the store.\n\nUse ava.nguyen1851@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8732376', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8732376'}),
            Action(name='get_product_details', kwargs={'product_id': '6858788497'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2601346', 'address1': '123 Oak Street', 'address2': 'Suite 100', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '28251'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2601346', 'payment_method_id': 'credit_card_3975380'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2601346', 'item_ids': ['5206946487'], 'new_item_ids': ['4024196380'], 'payment_method_id': 'credit_card_3975380'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting Lucas Johansson (lucas.johansson7741@example.com) with his pending order placed in San Francisco. You want to first review the details of the hiking boots in the order, which are leather, waterproof, size 8. Later, you would like to update the shipping address to 943 Maple Drive, Suite 356, Chicago, IL, USA 60621, and change the payment method to the Visa card ending in 9452, preferring this card over the current Mastercard ending in 3088 for payment. After that, you would like to cancel the entire order because you no longer need the hiking boots, backpack, and jigsaw puzzle.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.johansson1233@example.com',
        instruction='You are assisting Isabella Johansson (email: isabella.johansson1233@example.com). You want to exchange the large brown memory foam Pet Bed from her delivered order for a large grey memory foam one, because she prefers the grey color over brown. You prefer any price difference to be handled using her PayPal account, which is her preferred payment method. Later, you would like to update the shipping address for her pending order to 1204 Lincoln Street, Unit 351, Las Vegas, NV, USA 48580, because the original address is no longer valid. After that, you would like to update her default address to this new Las Vegas address for future orders.\n\nUse isabella.johansson1233@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3489690'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3489690', 'item_ids': ['7381052709'], 'new_item_ids': ['2751999929'], 'payment_method_id': 'paypal_8540436'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2591905', 'address1': '1204 Lincoln Street', 'address2': 'Unit 351', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '48580'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_johansson_7408', 'address1': '1204 Lincoln Street', 'address2': 'Unit 351', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '48580'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.patel5348@example.com',
        instruction='You are assisting Yusuf Patel (yusuf.patel5348@example.com). You want to exchange the Hiking Boots from his delivered order (originally size 10, leather, not waterproof) for the same model in size 11 with waterproofing, because he needs a larger and more weather-resistant fit for outdoor use. You prefer the replacement to be the leather waterproof version in size 11, as it matches his current boots’ material while adding needed protection. You want any price difference to be covered using his gift card, as it is his preferred payment method and already used for prior purchases. Later, you will update the shipping address for a pending order containing a black 10-inch tablet to a new location in San Diego, because the original address is no longer valid. After that, you would like to update your default address to this new San Diego address for all future orders, to ensure consistent and accurate delivery. The new address is 4497 Maple Lane, Unit 78, San Diego, CA, USA 93052.\n\nUse yusuf.patel5348@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2274128'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2274128', 'item_ids': ['2185126308'], 'new_item_ids': ['6159919747'], 'payment_method_id': 'gift_card_3372949'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2236333', 'address1': '4497 Maple Lane', 'address2': 'Unit 78', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '93052'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_patel_7767', 'address1': '4497 Maple Lane', 'address2': 'Unit 78', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '93052'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.brown7817@example.com',
        instruction='You are assisting Fatima Brown (email: fatima.brown7817@example.com) with two order actions. First, you want to cancel the pending order placed in San Jose for a 30-50 lbs adjustable urethane dumbbell set because it was ordered by mistake. Second, you would like to exchange the red cycling helmet (size M, medium ventilation) from a delivered order for the same model in size S with low ventilation, as it better fits your needs. You prefer any refund or charge associated with these changes to be processed using your Visa card ending in 2364.\n\nUse fatima.brown7817@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1649831', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9045919'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9045919', 'item_ids': ['1719127154'], 'new_item_ids': ['3358616356'], 'payment_method_id': 'credit_card_1982124'}),
            Action(name='get_product_details', kwargs={'product_id': '7765186836'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen.johnson3889@example.com',
        instruction="You are assisting Chen Johnson (email: chen.johnson3889@example.com) with two requests. First, you want to cancel a pending order placed in Houston that includes a dark-toned basic makeup kit from Brand B, white wireless earbuds with 8-hour battery life, a blue fabric office chair with adjustable armrests, and a blue Bluetooth speaker with 20-hour battery life, because he no longer needs these items. Later, you would like to exchange a delivered 500-piece expert-level 'animals' jigsaw puzzle for a 1000-piece intermediate 'fantasy' themed puzzle, as he prefers a more challenging and imaginative theme. You prefer to use his PayPal account to handle any price difference for the exchange.\n\nUse chen.johnson3889@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5061109', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5797164'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5797164', 'item_ids': ['9237024510'], 'new_item_ids': ['3112842858'], 'payment_method_id': 'paypal_3742148'}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.santos9082@example.com',
        instruction='You are Ethan Santos, authenticated at ethan.santos9082@example.com. You want to change the payment method on your pending order containing a red 2-piece softshell luggage set, a black smart watch with silicone band, a blue large cycling helmet, a 2K indoor security camera, and a 7-inch black tablet from PayPal to your Mastercard ending in 9443, because you prefer to use that card for this purchase. Later, you decided you no longer need those items and would like the entire order canceled. After that, you would like to update the shipping address for your other pending order—which includes a grey medium polyester pet bed, a white wireless gaming mouse, and a red high-back leather office chair—to 416 Pine Avenue, Suite 718, Jacksonville, FL, USA 67978, and also update your default address to this new Jacksonville location for all future orders.\n\nUse ethan.santos9082@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5320242'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5320242', 'payment_method_id': 'credit_card_9784468'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5320242', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4642822', 'address1': '416 Pine Avenue', 'address2': 'Suite 718', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '67978'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_santos_6104', 'address1': '416 Pine Avenue', 'address2': 'Suite 718', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '67978'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.sanchez1556@example.com',
        instruction='You are assisting Mia Sanchez (mia.sanchez1556@example.com) with two pending orders. First, you want to cancel her order placed by mistake, which includes a white 20000mAh portable charger, a professional light-skin-tone makeup kit from Brand B, and a 60% tactile mechanical keyboard without backlight, because she no longer needs these items. Second, you would like to modify her other pending order by changing the 13-inch silver laptop with 1TB SSD and 16GB RAM to the same model but with 512GB SSD and space grey color, as she prefers the smaller storage and more modern color. After that, you will ensure any refund or additional charge is processed using her PayPal account, which is her preferred payment method for financial adjustments.\n\nUse mia.sanchez1556@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4096800', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7170967'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7170967', 'item_ids': ['5052031638'], 'new_item_ids': ['6056040996'], 'payment_method_id': 'paypal_9064553'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are assisting Fatima Wilson (email: fatima.wilson5906@example.com) with her pending order for an Office Chair and a Grill. You want to update the shipping address to 9818 Cedar Road, Floor 991, Jacksonville, FL, USA 64914, because she needs the items delivered to a new location. Later, you would like to change the payment method from the Mastercard ending in 9779 to her PayPal account, as she prefers to use PayPal for this transaction.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1443906', 'address1': '9818 Cedar Road', 'address2': 'Floor 991', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '64914'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1443906'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1443906', 'payment_method_id': 'paypal_7685859'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com) with his pending order containing hiking boots, a 13-inch black laptop with i7 processor and 32GB RAM, and a small air purifier with quiet operation. You want to update the shipping address to 8894 Park Drive, Suite 780, San Diego, CA, USA 95152, because he needs the items delivered to a new location. Later, you would like to change the payment method from the current gift card to his Mastercard ending in 3762, because he prefers to preserve the gift card balance for future use.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '8894 Park Drive', 'address2': 'Suite 780', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '95152'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen2868@example.com',
        instruction='You are Ava Nguyen, authenticated at ava.nguyen2868@example.com, and you want to update the shipping address for your pending order—containing a dumbbell set, a red Bluetooth speaker, and a red fleece jacket—to 3339 Pine Avenue, Floor 183, Chicago, IL, USA 97923, because you have relocated and need the items delivered to your new residence. Later, you would like to exchange the portable electric grill without additional features from your delivered order for a portable electric grill with a side burner, because you prefer added cooking functionality for outdoor meals. You prefer to use your Mastercard ending in 6081 for any price difference associated with the exchange.\n\nUse ava.nguyen2868@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8367380', 'address1': '3339 Pine Avenue', 'address2': 'Floor 183', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '97923'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8367380'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8668939', 'item_ids': ['1120917161'], 'new_item_ids': ['3876764226'], 'payment_method_id': 'credit_card_5683823'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.santos3158@example.com',
        instruction='You are assisting Ivan Santos (email: ivan.santos3158@example.com) with his pending order. You want to update the shipping address from the current Dallas address to 3009 Adams Road, Floor 440, Chicago, IL, USA 75736 because the original address is no longer valid. You would also like to learn more about the Office Chair in the order, which is a red mesh model with no armrests and a standard backrest, to better understand its features and available alternatives. You prefer the update to be processed promptly since the order is still pending and has not been shipped.\n\nUse ivan.santos3158@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8770097', 'address1': '3009 Adams Road', 'address2': 'Floor 440', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '75736'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8770097'}),
            Action(name='get_product_details', kwargs={'product_id': '4794339885'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed.li8414@example.com',
        instruction='You are assisting Mohamed Li (email: mohamed.li8414@example.com) with his pending order. You want to update the shipping address from the current one in Columbus, OH to 5125 Cedar Road, Unit 110, Seattle, WA, USA 46306 because it was mistakenly entered as his old address. You would like to verify the order details, which include a Mechanical Keyboard with tactile switches, white backlight, and 80% size, along with an Indoor Security Camera, a black XL cotton T-Shirt, a gold silicone-banded Smart Watch with AMOLED display, and a 20MP Digital Camera with 3x zoom. You also want to learn more about the Mechanical Keyboard product, specifically confirming it has a tactile switch type, white backlight, and 80% layout, which is currently priced at $240.97 and available for purchase.\n\nUse mohamed.li8414@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8844578', 'address1': '5125 Cedar Road', 'address2': 'Unit 110', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '46306'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8844578'}),
            Action(name='get_product_details', kwargs={'product_id': '1656367028'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li7352@example.com',
        instruction='You are assisting Sofia Li (sofia.li7352@example.com), who has a pending order currently shipping to San Antonio, TX. You want to update the shipping address for this order to 7946 Jefferson Avenue, Unit 592, Nashville, TN, USA 92075, because she has relocated and needs the delivery redirected. After updating the address, you would like to browse the full list of available product types in the store to explore future purchase options, including categories such as Air Purifier, Hiking Boots, Skateboard, Yoga Mat, and other items like Backpack, Coffee Maker, Smart Watch, and Portable Charger, to discover new products of interest.\n\nUse sofia.li7352@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8855135', 'address1': '7946 Jefferson Avenue', 'address2': 'Unit 592', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '92075'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8855135'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.lopez8943@example.com',
        instruction='You are assisting Ethan Lopez (email: ethan.lopez8943@example.com) with updating the shipping address for his pending order containing a Dumbbell Set, Espresso Machine, Coffee Maker, and Pet Bed, currently scheduled for delivery to Columbus, OH. You want to change the shipping address to 7649 Park Drive, Suite 388, Seattle, WA, USA 35250, and confirm the update was successful. After that, you would like to review the available options for the Backpack, including variations in color (such as black, green, grey, navy), size (small, medium, large), material (nylon, polyester, leather), and compartment type (laptop, camera, hydration), to evaluate it for a possible future purchase.\n\nUse ethan.lopez8943@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6779827', 'address1': '7649 Park Drive', 'address2': 'Suite 388', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '35250'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6779827'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting a customer with email yusuf.gonzalez2399@example.com who has a pending order containing a black 128GB smartphone and a ceramic 1.5-liter tea kettle. You want to update the shipping address from Los Angeles, CA to 8122 Maple Lane, Floor 521, Houston, TX, USA 61316 because it was entered incorrectly. You also prefer to change the payment method from credit card to PayPal, as the customer intended to use that method instead.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '8122 Maple Lane', 'address2': 'Floor 521', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '61316'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting Lucas Johansson (email: lucas.johansson7741@example.com) with his pending order containing hiking boots, a black small nylon backpack with a laptop compartment, and a 500-piece expert-level animal-themed jigsaw puzzle. You want to update the shipping address to 8494 Oak Avenue, Floor 489, Oklahoma City, OK, USA 40387 because he needs the order delivered to a new location. After that, you would like to change the payment method from his Mastercard ending in 3088 to his Visa ending in 9452 because he prefers to use that card for this purchase. Finally, you need to confirm the updated order details with the new address and payment method in place.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '8494 Oak Avenue', 'address2': 'Floor 489', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '40387'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.hernandez3060@example.com',
        instruction='You are Evelyn Hernandez, and your email is evelyn.hernandez3060@example.com. You want to cancel your pending electric grill order because you no longer need it. For your recent delivered order with the black-frame blue-lens polarized sunglasses, adjustable dumbbell set, and glass bookshelf, you would like to return the dumbbell set because it does not fit your workout needs, and you prefer brown-lens sunglasses over the blue-lens ones for better sun clarity and comfort. You would like the replacement sunglasses to have a black frame and polarized lenses, matching the style you received. You prefer any refund or price adjustment to be applied to your Visa card ending in 4171, which you previously authorized for such transactions. Later, you will await confirmation of the cancellation and return instructions for the dumbbell set and sunglasses exchange.\n\nUse evelyn.hernandez3060@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3482034', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9628587'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9628587', 'item_ids': ['8140269513'], 'payment_method_id': 'credit_card_3631888'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9628587', 'item_ids': ['9045948550'], 'new_item_ids': ['4358482460'], 'payment_method_id': 'credit_card_3631888'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.rossi7301@example.com',
        instruction='You are assisting a customer with email yusuf.rossi7301@example.com who wants to cancel their pending order for a black XXL cotton crew neck T-Shirt because they no longer need it. Later, they would like to return the delivered 24MP digital camera with 3x zoom and SD card storage and exchange it for a 30MP model with the same 3x zoom and SD card storage, as they prefer higher resolution while keeping the same usability and compatibility. You prefer any payment adjustment to be processed using the Mastercard ending in 2478.\n\nUse yusuf.rossi7301@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6247578', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6679257'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6679257', 'item_ids': ['5996159312'], 'payment_method_id': 'credit_card_9513926'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6679257', 'item_ids': ['5996159312'], 'new_item_ids': ['1804581713'], 'payment_method_id': 'credit_card_9513926'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.muller6448@example.com',
        instruction='You are assisting Fatima Muller (email: fatima.muller6448@example.com). You want to update the shipping address for a pending order containing a Mechanical Keyboard and a Tea Kettle to 4102 Lincoln Street, Floor 799, Las Vegas, NV, USA 12754, because the original address in Chicago is no longer valid. Later, you would like to exchange the capsule-type Espresso Machine (15 bar, 1.5L) from a delivered order for a different model that is automatic with 9 bar pressure and 2L capacity, because you prefer automatic operation and larger water capacity. You also want to return a white wireless Gaming Mouse from the same delivered order, as it does not meet your current needs. For any payment adjustments related to the exchange, you prefer to use your PayPal account ending in 5541158.\n\nUse fatima.muller6448@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9962383', 'address1': '4102 Lincoln Street', 'address2': 'Floor 799', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '12754'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9962383'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2435638', 'item_ids': ['7441167885'], 'new_item_ids': ['3709608322'], 'payment_method_id': 'paypal_5541158'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2435638', 'item_ids': ['8896479688'], 'payment_method_id': 'paypal_5541158'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.johnson2300@example.com',
        instruction='You are assisting Fatima Johnson (email: fatima.johnson2300@example.com) with two order adjustments. First, you want to update the shipping address for her pending order—which includes hiking boots, an action camera, an electric kettle, a cycling helmet, and a wristwatch—from Austin to 8123 Jackson Street, Apt 873, Houston, TX, USA 12929, because she has relocated temporarily. Later, you would like to exchange the blue v-neck polyester T-shirt (size S) from her delivered order for the same color in a crew neck cotton version in size M, because it fits better and is more comfortable, and return the remaining items from that delivered order—hiking boots, smart watch, and mechanical keyboard—because they no longer suit her needs. You prefer any refund or price difference to be processed back to her PayPal account, which is already on file.\n\nUse fatima.johnson2300@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5199551', 'address1': '8123 Jackson Street', 'address2': 'Apt 873', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '12929'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5199551'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9389413', 'item_ids': ['5047954489'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_5364164'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9389413', 'item_ids': ['4127323219', '2554056026', '6342039236'], 'payment_method_id': 'paypal_5364164'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.brown3965@example.com',
        instruction="You are assisting Harper Brown (harper.brown3965@example.com) with order adjustments. You want to cancel a pending order placed by mistake that includes a gold Smart Watch with silicone band, a glass Tea Kettle with 1-liter capacity, a woody-scented 100ml men's Perfume, a black Electric Toothbrush with rechargeable battery, and size 10 leather Hiking Boots. Later, for a delivered order received in Fort Worth, you would like to exchange the current Desk Lamp, which has medium brightness and USB power, for a new white Desk Lamp with higher brightness and the same USB power source, because you prefer brighter lighting. You also want to return the 10-inch wood-colored analog Wall Clock from the same delivered order. You prefer any payment adjustments related to these changes to be processed back to your PayPal account. You confirm both the cancellation and the exchange/return actions to proceed.\n\nUse harper.brown3965@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2273069', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1840144'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1840144', 'item_ids': ['8384507844'], 'new_item_ids': ['9083642334'], 'payment_method_id': 'paypal_2306935'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1840144', 'item_ids': ['6534134392'], 'payment_method_id': 'paypal_2306935'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.kovacs4505@example.com',
        instruction='You are assisting Sofia Kovacs (sofia.kovacs4505@example.com) with her pending order. You want to exchange the 28-inch maple skateboard with a plain design for the 28-inch bamboo skateboard with a graphic design, because she prefers the lighter bamboo material and the more expressive visual style. You prefer the price difference to be handled using her PayPal account, which is already on file. Later, you would like to update the shipping address for this order to 9268 Jefferson Avenue, Suite 37, Los Angeles, CA, USA 84743, to ensure delivery to her new location. After that, you would like her default profile address to be updated to the same Los Angeles address for future orders.\n\nUse sofia.kovacs4505@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9869592'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9869592', 'item_ids': ['3232433601'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'paypal_6840891'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9869592', 'address1': '9268 Jefferson Avenue', 'address2': 'Suite 37', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '84743'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_kovacs_7075', 'address1': '9268 Jefferson Avenue', 'address2': 'Suite 37', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '84743'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.ito2682@example.com',
        instruction='You are assisting Harper Ito (email: harper.ito2682@example.com) from Denver, CO. You want to exchange the blue cycling helmet in size S from a delivered order for a red one in size M with high ventilation, because it better fits your current gear and provides a preferred fit. You prefer the exchange to use PayPal for any price adjustment, as that was your original payment method. Later, you would like to cancel a pending order for yellow running shoes, because they are no longer needed.\n\nUse harper.ito2682@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5673917'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5673917', 'item_ids': ['1676105083'], 'new_item_ids': ['8573379326'], 'payment_method_id': 'paypal_1053133'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5673917', 'item_ids': ['1676105083'], 'payment_method_id': 'paypal_1053133'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1941216', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.silva5146@example.com',
        instruction='You are Lucas Silva, authenticated at lucas.silva5146@example.com, and you want to update the shipping address for your pending order—which includes a ceramic tea kettle, a space grey 13-inch laptop, a black portable charger, and a white wooden bookshelf—to 2181 Pine Avenue, Suite 495, Charlotte, NC, USA 89498, because you realized the original address was incorrect. You also want your default address updated to the same, to ensure future orders are delivered correctly. After that, you would like to browse available products, specifically exploring the Backpack options, because you are considering a new purchase and want to see current styles and sizes, particularly those with laptop or camera compartments in materials like nylon or polyester. Later, you decide you no longer need the original order and would like to cancel it, followed by confirmation that the cancellation was successful, so you can be assured no items will be shipped or charged further. You prefer the refund to be processed back to your Mastercard ending in 5197, which was used for the original payment.\n\nUse lucas.silva5146@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1814268', 'address1': '2181 Pine Avenue', 'address2': 'Suite 495', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '89498'}),
            Action(name='modify_user_address', kwargs={'user_id': 'lucas_silva_7435', 'address1': '2181 Pine Avenue', 'address2': 'Suite 495', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '89498'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1814268', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1814268'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.brown3965@example.com',
        instruction="You are assisting Harper Brown (email: harper.brown3965@example.com) with their pending order containing a gold Smart Watch with silicone band, a glass 1-liter Tea Kettle compatible with gas stoves, a woody-scented 100ml men's Perfume, a black Electric Toothbrush with high speed settings, and size 10 leather Hiking Boots. You want to update the shipping address from Fort Worth, TX to 3338 Oak Avenue, Suite 630, Nashville, TN, USA 23108 because the original delivery location is no longer valid. After that, you would like to switch the payment method from your Visa ending in 3356 to your PayPal account for better transaction tracking and personal budgeting. Once these updates are confirmed, you want to cancel the entire order as the items are no longer needed. Later, you would like to browse the product catalog to explore current offerings and consider new purchases based on updated needs and preferences.\n\nUse harper.brown3965@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2273069', 'address1': '3338 Oak Avenue', 'address2': 'Suite 630', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '23108'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2273069'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2273069', 'payment_method_id': 'paypal_2306935'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2273069', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting a customer who wants to cancel her pending order placed by mistake. You are to proceed with cancellation of the order containing a men's oriental-scented 100ml perfume, a glass 1.5-liter stovetop tea kettle compatible with induction, a black 1L glass electric kettle, and gray canvas sneakers in size 8. The customer, sophia.patel9841@example.com, confirms she no longer needs these items and wants the entire order canceled. You prefer the refund to be processed back to the original payment method, which is the credit card used for the purchase.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7905419', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are assisting James Martin (email: james.martin9857@example.com) with his pending order originally shipped to San Diego. You want to update the shipping address to 9831 Oak Avenue, Suite 243, Chicago, IL, USA 13249 because he has relocated temporarily. After that, you prefer to change the payment method from PayPal to his Visa card ending in 1826 for better rewards tracking. Later, you would like to review the details of the red cotton crew neck T-Shirt in size XXL, which is part of the order, to confirm its material and style before the order is finalized.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '9831 Oak Avenue', 'address2': 'Suite 243', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '13249'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3043531', 'payment_method_id': 'credit_card_7083997'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.thomas3069@example.com',
        instruction='You are Sofia Thomas, authenticated via email sofia.thomas3069@example.com. You want to update the shipping address for your pending order (containing Wireless Earbuds, Vacuum Cleaner, Electric Toothbrush, and Portable Charger) to 6675 Washington Boulevard, Floor 295, Austin, TX, USA 30995, because it was initially sent to the wrong location. Later, you will cancel this order because it was placed by mistake. Separately, you would like to exchange a red XXL cotton crew neck T-Shirt from your delivered order (shipped to Dallas) for a purple XL cotton crew neck version, because the current size is too large and you prefer the color purple. You prefer the price difference to be processed using your PayPal account. Additionally, you want to browse the full catalog of available product types to explore other items of interest, and you would like detailed information about the T-Shirt product to better understand its features and options.\n\nUse sofia.thomas3069@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7619352', 'address1': '6675 Washington Boulevard', 'address2': 'Floor 295', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '30995'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7619352', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7619352'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3388163', 'item_ids': ['9354168549'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'paypal_5334408'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.wilson5728@example.com',
        instruction='You are Mei Wilson (mei.wilson5728@example.com) and you want to cancel your pending order placed in New York because you no longer need the items. The order includes an electric portable grill with rotisserie, a professional-sized makeup kit for medium skin tone, a 31-inch bamboo graphic skateboard, black wireless earbuds with IPX7 water resistance, and a black 128GB smartphone with a 6.5-inch screen. You confirm the cancellation and prefer the refund to be returned to your gift card balance.\n\nUse mei.wilson5728@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W4498118'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4498118', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.santos8623@example.com',
        instruction="You are assisting a customer who placed a pending order for a black digital wall clock (10 inches), a silver action camera (1080p, not waterproof), and an adjustable dumbbell set (55-75 lbs, urethane material) to be shipped to Phoenix, AZ. You want to cancel the entire order because the customer no longer needs the items. You prefer the refund to be issued back to the original gift card used for purchase. The customer's email is emma.santos8623@example.com.\n\nUse emma.santos8623@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7854887'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7854887', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.santos3158@example.com',
        instruction='You are assisting Ivan Santos (email: ivan.santos3158@example.com). You want to update the shipping address for the pending order containing the red mesh Office Chair to 8146 Park Drive, Unit 548, Chicago, IL, USA 99897, because it was originally set to a Dallas address. You also want to update your default address to this Chicago address for future orders. After that, you would like to return both items from the delivered order — the black 50ft vinyl Garden Hose and the blue Wireless Earbuds — and receive a refund back to your PayPal account, as you no longer need them. Later, you changed your mind about the pending order and decided to cancel it entirely because it was placed by mistake, so you would like to cancel the order for the Office Chair before it ships.\n\nUse ivan.santos3158@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8770097', 'address1': '8146 Park Drive', 'address2': 'Unit 548', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '99897'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ivan_santos_6635', 'address1': '8146 Park Drive', 'address2': 'Unit 548', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '99897'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6893533', 'item_ids': ['5206946487', '1646531091'], 'payment_method_id': 'paypal_6151711'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6893533'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8770097', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.jackson2465@example.com',
        instruction='You are assisting Olivia Jackson (email: olivia.jackson2465@example.com). You want to update the shipping address for an order containing Hiking Boots (size 8, leather, waterproof), a Gaming Mouse, and Sneakers to 6460 Pine Avenue, Floor 294, Chicago, IL, USA 74741 because she needs it delivered to a new location. You also want to update her default address to this new Chicago address for future orders. Later, you would like to cancel her other pending order containing an Air Purifier for large rooms, white wired Headphones, and a black 7-inch 128GB Tablet because she no longer needs these items. You prefer the refund for the canceled order to be processed back to the original payment method, PayPal.\n\nUse olivia.jackson2465@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3168895'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3168895', 'address1': '6460 Pine Avenue', 'address2': 'Floor 294', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '74741'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_jackson_1219', 'address1': '6460 Pine Avenue', 'address2': 'Floor 294', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '74741'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5663445', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.khan7390@example.com',
        instruction='You are assisting Yusuf Khan (email: yusuf.khan7390@example.com). You want to review the details of a pending order placed in Dallas, which includes a 15-inch Laptop with i5 processor, 32GB RAM, 256GB SSD, and space grey color, because you need more information about this product. Later, you will cancel another pending order from the same user that contains an Electric Kettle, as you no longer need it. After that, you would like to update the shipping address for the first order (the one with the Laptop) to a new location in Las Vegas: 6628 Main Street, Suite 142, Las Vegas, NV, USA 47642. Additionally, you want to see what other product types are available in the store to explore more options.\n\nUse yusuf.khan7390@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1787190'}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3579467', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1787190', 'address1': '9928 Jackson Street', 'address2': 'Unit 607', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '86222'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are Liam Thomas, with email liam.thomas9081@example.com, and you want to first review the details of the E-Reader in your pending order, which includes a 7-inch screen, Wi-Fi connectivity, and 8GB storage, because you were initially unsure about the device specifications. Later, you decided you no longer need that order and would like to cancel it entirely because your needs have changed. After that, you would like to update the shipping address for your other pending order—containing a bamboo skateboard, a 2-piece black luggage set, and a 20000mAh blue portable charger—to 506 Madison Drive, Suite 852, Portland, OR, USA 36624, because you will be relocating and need the items delivered to your new location.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1654931'}),
            Action(name='get_product_details', kwargs={'product_id': '3801771308'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1654931', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3295833', 'address1': '506 Madison Drive', 'address2': 'Suite 852', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '36624'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.garcia1495@example.com',
        instruction='You are Sophia Garcia, and your email is sophia.garcia1495@example.com. You want to return the A4 soft cover Notebook from your delivered order that was shipped to Houston. You prefer the refund to be issued to your Mastercard ending in 5956 because that was the original payment method used for the purchase.\n\nUse sophia.garcia1495@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5777276'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5777276', 'item_ids': ['7579176349'], 'payment_method_id': 'credit_card_4147840'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.smith9157@example.com',
        instruction='You are Olivia Smith, and your email is olivia.smith9157@example.com. You want to return your delivered blue cycling helmet in size M with low ventilation and exchange it for a red one in the same size but with high ventilation, as you prefer better airflow during rides. You would like the price difference to be handled using your PayPal account, which was previously used for the original purchase.\n\nUse olivia.smith9157@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3794101'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3794101', 'item_ids': ['3339188619'], 'payment_method_id': 'paypal_2076152'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3794101', 'item_ids': ['3339188619'], 'new_item_ids': ['8573379326'], 'payment_method_id': 'paypal_2076152'}),
            Action(name='get_product_details', kwargs={'product_id': '7765186836'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.kovacs2446@example.com',
        instruction='You are assisting Harper Kovacs (email: harper.kovacs2446@example.com) with an exchange request for a delivered digital camera from their order in San Jose. You want to exchange the 30MP digital camera with 10x zoom and SD card storage for a similar model with 3x zoom but the same 30MP resolution and SD card storage, as you prefer a more compact zoom capability while maintaining image quality and storage compatibility. You would like any price difference refunded due to the lower cost of the new model. You prefer the refund to be applied back to the original payment method, which is your Visa card ending in 2080.\n\nUse harper.kovacs2446@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3065353'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3065353', 'item_ids': ['9228757377'], 'new_item_ids': ['1804581713'], 'payment_method_id': 'credit_card_7422485'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.santos7226@example.com',
        instruction='You are assisting Liam Santos (email: liam.santos7226@example.com). You want to cancel the pending order containing a red medium Cycling Helmet and a 2-liter stainless steel Tea Kettle because it was placed by mistake. Later, you would like to update the shipping address for another pending order that includes a Mechanical Keyboard and a Vacuum Cleaner to ensure it reaches the correct location. You prefer the new address to be 2577 Pine Avenue, Suite 706, Phoenix, AZ, USA 72651. You prefer the refund from the canceled order to be processed back to the original credit card used for payment.\n\nUse liam.santos7226@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6794581'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6794581', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4011814', 'address1': '2577 Pine Avenue', 'address2': 'Suite 706', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '72651'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.khan2360@example.com',
        instruction='You are Olivia Khan, and your email is olivia.khan2360@example.com. You want to update the shipping address for your pending order to 2032 Maple Lane, Floor 621, Jacksonville, FL, USA 30892 because you need it delivered to a different location. You also prefer to change the payment method from PayPal to your Mastercard ending in 2184 for better expense tracking. Later, you decided to cancel the entire order because it was placed by mistake, and you no longer need the red cotton T-shirt in size S, the black polarized sunglasses, the large memory foam pet bed, or the blue-dial metal-strap wristwatch.\n\nUse olivia.khan2360@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3840181', 'address1': '2032 Maple Lane', 'address2': 'Floor 621', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '30892'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3840181', 'payment_method_id': 'credit_card_7376788'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3840181'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3840181', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.brown3965@example.com',
        instruction='You are assisting Harper Brown (harper.brown3965@example.com) with her pending order originally shipped to Fort Worth. You want to update the shipping address to her new apartment at 3994 Pine Avenue, Apt 111, Boston, MA, because she has recently moved. After that, you prefer to change the payment method from the current credit card to PayPal for better purchase protection and easier tracking. Later, you would like to exchange the gold Smart Watch with silicone band for the same model with a leather band and AMOLED display, as you prefer a more premium and elegant look over the sporty feel of silicone. You would like any price difference to be handled using the same PayPal account, as it is your preferred payment method for this transaction.\n\nUse harper.brown3965@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2273069', 'address1': '3994 Pine Avenue', 'address2': 'Apt 111', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '49152'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2273069'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2273069', 'payment_method_id': 'paypal_2306935'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2273069', 'item_ids': ['2681513500'], 'new_item_ids': ['5694328282'], 'payment_method_id': 'paypal_2306935'}),
            Action(name='get_product_details', kwargs={'product_id': '6945232052'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting Lucas Johansson (lucas.johansson7741@example.com) with his pending order originally shipped to San Francisco. You want to update the shipping address to 5341 Adams Road, Apt 432, San Francisco, CA, USA 97958, to ensure delivery to his current location. You would like to change the payment method from the Mastercard ending in 3088 to the Visa ending in 9452 for the main transaction, as it offers better rewards for this purchase. Later, you will exchange the Hiking Boots from size 8 to size 9, both in leather and waterproof, because the original size is too tight for his needs. For any price difference resulting from the exchange, you prefer to use the Mastercard ending in 3088 to cover the adjustment.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '5341 Adams Road', 'address2': 'Apt 432', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '97958'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5073920', 'item_ids': ['2648909398'], 'new_item_ids': ['8106223139'], 'payment_method_id': 'credit_card_1814983'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.khan2146@example.com',
        instruction='You are Daiki Khan, with email daiki.khan2146@example.com, and you want to update the shipping address for your pending order—which includes a Cycling Helmet, Desk Lamp, Skateboard, and Perfume—from Charlotte, NC to 8724 Elm Street, Unit 842, Austin, TX, USA 33988 because you have moved. You also want your default address in your profile updated to the same Austin address for all future orders. Later, you would like to browse the product catalog, specifically requesting detailed information about the Laptop, because you are considering purchasing it.\n\nUse daiki.khan2146@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5861600', 'address1': '8724 Elm Street', 'address2': 'Unit 842', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '33988'}),
            Action(name='modify_user_address', kwargs={'user_id': 'daiki_khan_6856', 'address1': '8724 Elm Street', 'address2': 'Unit 842', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '33988'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.brown8893@example.com',
        instruction="You are Anya Brown (anya.brown8893@example.com). You want to update your pending order for an E-Reader and Smart Watch by changing the shipping address to 7398 Pine Avenue, Apt 947, Fort Worth, TX, USA 97649, because you've relocated within Texas. You prefer to switch the payment method from your Mastercard to your PayPal for this order, as it's your preferred digital wallet. You also want to upgrade the E-Reader from the 6-inch, 8GB model to the 8-inch, 32GB version, because you prefer a larger screen and more storage for reading and media, and you would like any price difference to be handled using your PayPal. Later, you would like to exchange the medium Pet Bed from your delivered order, changing it from fleece material in grey to memory foam in beige, because you prefer better support and a lighter color that matches your home decor. For this exchange, you prefer to use your Mastercard ending in 9625 for any price adjustment.\n\nUse anya.brown8893@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8883368', 'address1': '7398 Pine Avenue', 'address2': 'Apt 947', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '97649'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8883368', 'payment_method_id': 'paypal_5206520'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8883368', 'item_ids': ['5510402676'], 'new_item_ids': ['7609274509'], 'payment_method_id': 'paypal_5206520'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2922433'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2922433', 'item_ids': ['6857426243'], 'new_item_ids': ['3360679910'], 'payment_method_id': 'credit_card_3414703'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting Sophia Patel (sophia.patel9841@example.com). For her pending order containing a 100ml oriental men's perfume, tea kettle, electric kettle, and sneakers, you want to update the shipping address to 4466 Washington Boulevard, Apt 146, Boston, MA, USA 98607 because she has relocated temporarily. You also prefer to switch the payment method from Visa ending in 8025 to her Mastercard ending in 1639 for better rewards tracking. Additionally, you would like to change the 100ml oriental men's perfume to the 30ml version of the same scent because it's more convenient for travel. Later, for her delivered order containing a 17-inch black laptop and blue wireless earbuds, you want to return the earbuds as they don't fit well and exchange the laptop for the 15-inch space grey model with the same 32GB RAM and 1TB SSD because it's lighter and better suited for daily commutes. You prefer to use the same Mastercard ending in 1639 for any refund or additional charge associated with the exchange.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7905419', 'address1': '4466 Washington Boulevard', 'address2': 'Apt 146', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '98607'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7905419', 'payment_method_id': 'credit_card_6419343'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7905419', 'item_ids': ['5421902839'], 'new_item_ids': ['1325156478'], 'payment_method_id': 'credit_card_6419343'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2923184'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2923184', 'item_ids': ['2757705742'], 'payment_method_id': 'credit_card_6419343'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2923184', 'item_ids': ['1684786391'], 'new_item_ids': ['6017636844'], 'payment_method_id': 'credit_card_6419343'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting Fatima Li (email: fatima.li2845@example.com). You want to cancel the pending order containing a 31-inch maple graphic skateboard and a 15 bar 1.5L capsule espresso machine because it was placed by mistake. After that, you would like to browse the full range of products currently offered in the store to explore available options. Later, for your other pending order containing a wired RGB optical gaming mouse and a 13-inch i5 16GB RAM 512GB SSD space grey laptop, you would like to update the shipping address to 4783 Elm Street, Suite 32, San Francisco, CA, USA 38341, and change the payment method to PayPal for better transaction tracking.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8005719', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3510092', 'address1': '4783 Elm Street', 'address2': 'Suite 32', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '38341'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3510092', 'payment_method_id': 'paypal_6366157'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.lee3013@example.com',
        instruction='You are assisting Anya Lee (email: anya.lee3013@example.com). You want to update the shipping address for a pending order (currently to San Antonio, TX) to 7420 Elm Street, Floor 701, Columbus, OH, USA 56657, and also set this as your default address because it is your new residence. Later, for a delivered order containing a 15 bar capsule espresso machine, size 10 leather non-waterproof hiking boots, and a 1L black stainless steel kettle, you would like to exchange the espresso machine for the 19 bar capsule model because you prefer higher pressure for better extraction, exchange the hiking boots for size 9, waterproof ones because they will be more suitable for wet trails, and exchange the kettle for the 2L white glass version because you need more capacity and a more modern look. You prefer to use your PayPal account for any price differences. After that, you would like to cancel another pending order (containing a pet bed, air purifier, desk lamp, water bottle, and fleece jacket) because you no longer need the items.\n\nUse anya.lee3013@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3176007', 'address1': '7420 Elm Street', 'address2': 'Floor 701', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '56657'}),
            Action(name='modify_user_address', kwargs={'user_id': 'anya_lee_8315', 'address1': '7420 Elm Street', 'address2': 'Floor 701', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '56657'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1335809', 'item_ids': ['4875647558', '2185126308', '7602931732'], 'new_item_ids': ['6200867091', '8106223139', '4064702754'], 'payment_method_id': 'paypal_3728317'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1335809'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2989580', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.lopez3569@example.com',
        instruction='You are Ava Lopez, with email ava.lopez3569@example.com. You want to update the shipping address for your pending order (containing a skateboard, headphones, air purifier, laptop, and sunglasses) to 9626 Elm Street, Floor 608, Portland, OR, USA 29273, and also update your default address to this new Portland address because you have relocated. You would like to exchange the blue 750ml stainless steel water bottle from your delivered order (which also included a digital camera) for the red 1000ml stainless steel version because you prefer a larger capacity and different color. You prefer to use your Mastercard ending in 9677 for any applicable charges or verification related to the exchange. After initiating these changes, you would like to verify the updated details of the exchange order. Later, you decided the pending order is no longer needed, so you would like to cancel it.\n\nUse ava.lopez3569@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8327915', 'address1': '9626 Elm Street', 'address2': 'Floor 608', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '29273'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_lopez_2676', 'address1': '9626 Elm Street', 'address2': 'Floor 608', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '29273'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2941275', 'item_ids': ['7843064651'], 'new_item_ids': ['2439754078'], 'payment_method_id': 'credit_card_7772870'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2941275'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8327915', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.anderson1082@example.com',
        instruction='You are assisting Fatima Anderson (email: fatima.anderson1082@example.com), who is exploring the product catalog with a specific interest in Jigsaw Puzzles. You want to exchange the delivered 1L manual Espresso Machine for a 2L automatic model because it better suits her needs for larger capacity and ease of use. You prefer the refund for the exchange to be processed back to your PayPal account. Later, you would like to cancel the pending order containing the Sneakers, Electric Kettle, Jigsaw Puzzle, Office Chair, and Wireless Earbuds because you no longer need those items.\n\nUse fatima.anderson1082@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9183908'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9183908', 'item_ids': ['7407838442'], 'payment_method_id': 'gift_card_8070316'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9183908', 'item_ids': ['7407838442'], 'new_item_ids': ['3709608322'], 'payment_method_id': 'paypal_7697967'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6368178', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.ito2168@example.com',
        instruction='You are assisting Evelyn Ito (email: evelyn.ito2168@example.com) with her pending order originally shipped to San Diego. You want to update the shipping address to 6522 Washington Boulevard, Floor 558, Denver, CO, USA 65992, because she entered the wrong location. You prefer to switch the payment method from Visa to PayPal, and you want any price difference handled using the same PayPal account. You would like to modify the items in the order: you prefer the black large nylon backpack over the original green small leather one because you want a larger, more durable option in a different color and material; and you prefer the green Bluetooth speaker over the black one to match your style preference, while keeping the same battery life and water resistance. All changes should be applied to the same order before fulfillment.\n\nUse evelyn.ito2168@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6207110', 'address1': '6522 Washington Boulevard', 'address2': 'Floor 558', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '65992'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6207110', 'payment_method_id': 'paypal_5377635'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6207110', 'item_ids': ['7251508981', '5650803029'], 'new_item_ids': ['3928046918', '9440686670'], 'payment_method_id': 'paypal_5377635'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito (olivia.ito5204@example.com) and you have a pending order currently set to ship to Denver, CO. You want to update the shipping address to 182 Adams Road, Suite 76, Jacksonville, FL, USA 54665 because it was initially entered incorrectly. You also want to change the payment method from your Visa ending in 9182 to your PayPal account for greater convenience and security. Additionally, you would like to modify the gaming mouse in the order from the black wired version to the white wireless version because you prefer a cleaner aesthetic and the freedom of wireless connectivity.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '182 Adams Road', 'address2': 'Suite 76', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '54665'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5442520', 'item_ids': ['3330317167'], 'new_item_ids': ['8896479688'], 'payment_method_id': 'paypal_8049766'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed.lee1888@example.com',
        instruction='You are assisting a customer with email mohamed.lee1888@example.com who received a delivered order in Charlotte. You want to return one backpack because it is the wrong size and lacks the preferred compartment type — specifically, the grey medium polyester backpack with laptop compartment. Later, you would like to exchange the other backpack for a different color and functionality — preferring the navy large polyester backpack with laptop compartment over the current grey large polyester backpack with hydration compartment, as it better suits the intended use. You prefer any price difference or refund to be processed back to the Visa card ending in 4433.\n\nUse mohamed.lee1888@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7913362'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7913362', 'item_ids': ['5917587651'], 'payment_method_id': 'credit_card_8169552'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7913362', 'item_ids': ['6309044598'], 'new_item_ids': ['8084436579'], 'payment_method_id': 'credit_card_8169552'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.hernandez9440@example.com',
        instruction='You are assisting Olivia Hernandez (email: olivia.hernandez9440@example.com) with her delivered order from Seattle. You want to return the Garden Hose (25ft, green, latex) because it is no longer needed. You would like to exchange the black Wireless Earbuds (4-hour battery, not water-resistant) for the blue version with 6-hour battery life and IPX4 water resistance, as you prefer longer battery and a more vibrant color. You prefer any refund or price difference to be processed back to your Mastercard ending in 2786.\n\nUse olivia.hernandez9440@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5671546'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5671546', 'item_ids': ['3230708338'], 'payment_method_id': 'credit_card_2583849'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5671546', 'item_ids': ['4063058357'], 'new_item_ids': ['1646531091'], 'payment_method_id': 'credit_card_2583849'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are assisting Fatima Wilson (email: fatima.wilson5906@example.com) with two order actions. First, you want to cancel the pending order placed by mistake for an office chair in blue leather with fixed armrests and a gas grill with rotisserie features, both shipped to Austin. Later, you would like to initiate a return for the electric kettle from a previously delivered order in Los Angeles; the kettle is 1L capacity, made of glass, and colored silver. You prefer the refund for the returned item to be sent back to the original payment method, which was PayPal.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1443906', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7990410'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7990410', 'item_ids': ['1240311797'], 'payment_method_id': 'paypal_7685859'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.smith2338@example.com',
        instruction="You are assisting Ethan Smith (email: ethan.smith2338@example.com) with a sequence of preferences regarding his recent order. You want to update the shipping address for his pending order—which includes a white 5000mAh portable charger, an electric toothbrush, a mechanical keyboard with clicky switches and RGB backlighting, and a 24MP digital camera—to 736 Lincoln Street, Floor 207, Seattle, WA, USA 24752, because he needs it delivered to a new location. Later, you will cancel the entire order with the reason 'no longer needed', as he no longer requires the items. After that, you would like to browse the full list of available product types in the store, possibly to explore future purchase options, including categories such as air purifiers, backpacks, coffee makers, headphones, smartwatches, and others.\n\nUse ethan.smith2338@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6711349', 'address1': '736 Lincoln Street', 'address2': 'Floor 207', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '24752'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6711349'}),
            Action(name='get_product_details', kwargs={'product_id': '6942297802'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6711349', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.muller9246@example.com',
        instruction='You are yara.muller9246@example.com and want to update the shipping address for your pending order, which includes a professional-size makeup kit for light skin tone from Brand B, to 5515 Park Drive, Unit 61, San Antonio, TX, USA 62643, because the original address is incorrect. Later, you would like to cancel the entire order because it was placed by mistake. You prefer the refund to be processed back to your credit card on file.\n\nUse yara.muller9246@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5056519'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5056519', 'address1': '5515 Park Drive', 'address2': 'Unit 61', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '62643'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5056519', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.davis8164@example.com',
        instruction='You are Sofia Davis, and your email is sofia.davis8164@example.com. You have a pending order that includes a 4-piece red hardshell luggage set, a 13-inch silver laptop with i5 processor and 32GB RAM, a 1.5-liter ceramic tea kettle compatible with gas stoves, and a 1L manual espresso machine with 15 bar pressure. You want to first update the shipping address for this order to 3633 Main Street, Unit 797, San Francisco, CA, USA 81267, because you have relocated and need the delivery redirected. Later, you would like to cancel the entire order, as you no longer need these items. You prefer the refund to be processed back to the original payment method, which was a gift card.\n\nUse sofia.davis8164@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2541482'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2541482', 'address1': '3633 Main Street', 'address2': 'Unit 797', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '81267'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2541482', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.ito2682@example.com',
        instruction='You are Harper Ito, with email harper.ito2682@example.com. You want to first update the shipping address for your pending order containing yellow running shoes (size 9) to 3329 Park Drive, Apt 159, Nashville, TN, USA 36116, because you realized it was shipped to the wrong location. Later, you decided to cancel this order entirely because it was placed by mistake. After that, you would like to return the blue small cycling helmet from your delivered order, as you no longer need it, and you prefer the refund to be issued back to your PayPal account. You also want to browse the full list of available product types to explore other options, and you are particularly interested in reviewing the details of the cycling helmet product for potential future purchase, possibly in a different color or size.\n\nUse harper.ito2682@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1941216', 'address1': '3329 Park Drive', 'address2': 'Apt 159', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '36116'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1941216', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5673917'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5673917', 'item_ids': ['1676105083'], 'payment_method_id': 'paypal_1053133'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7765186836'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.gonzalez9269@example.com',
        instruction='You are assisting Aarav Gonzalez (email: aarav.gonzalez9269@example.com) with two sequential requests. First, you want to cancel the pending order placed by mistake, which includes an Electric Toothbrush in white with low speed settings and rechargeable battery, an Action Camera in silver with 5K resolution and waterproof capability, a Cycling Helmet in blue size M, and a Smart Watch with silver color, leather band, and AMOLED display, all shipped to San Antonio. You prefer the refund to be processed back to the original payment method, PayPal. After the cancellation is confirmed, you would like to browse the product catalog and view details about the Backpack product. You are interested in learning about available options such as color, size, material, and special compartments (like camera, laptop, or hydration), particularly for models in black, green, grey, or navy, and across small, medium, and large sizes.\n\nUse aarav.gonzalez9269@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6979932', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6979932'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.sanchez6218@example.com',
        instruction='You are Isabella Sanchez (isabella.sanchez6218@example.com). You want to update the shipping address for your pending order containing a bamboo 28 inch plain skateboard and a black Bluetooth speaker to 3682 Jackson Street, Unit 991, Chicago, IL, USA 33029, because you need it delivered to a new location. You also want your default address updated to this same address for future orders. Additionally, you would like to upgrade the skateboard in your order from 28 inch to 31 inch, preferring a similar bamboo construction and plain or custom design if available, because you need more deck space for stability. You prefer the price difference to be handled using your PayPal account, which was previously used for this order. Later, you would like to browse the available product types in the catalog. After that, you would like to see detailed information about the Skateboard product, including its variants, to explore other options for future purchases.\n\nUse isabella.sanchez6218@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4386313', 'address1': '3682 Jackson Street', 'address2': 'Unit 991', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '33029'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_sanchez_2068', 'address1': '3682 Jackson Street', 'address2': 'Unit 991', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '33029'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4386313', 'item_ids': ['8176740019'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'paypal_8516781'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.lopez3271@example.com',
        instruction='You are assisting Isabella Lopez (email: isabella.lopez3271@example.com) with her pending order for a red Bluetooth speaker. You want to first update the shipping address to 8890 Washington Boulevard, Unit 612, Nashville, TN, USA 79009 because the original address was incorrect. After that, you would like to change the payment method from your Mastercard ending in 4336 to your PayPal account for greater convenience. Later, you decide to cancel the entire order because it was placed by mistake. After cancellation, you would like confirmation of the current order status to ensure it has been successfully canceled and no further action is required.\n\nUse isabella.lopez3271@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4923227', 'address1': '8890 Washington Boulevard', 'address2': 'Unit 612', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '79009'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4923227', 'payment_method_id': 'paypal_1621947'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4923227', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4923227'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting Fatima Li (email: fatima.li1185@example.com). You want to update the shipping address for a pending order containing a skateboard with a graphic design and a capsule-type espresso machine to 4527 Pine Avenue, Floor 924, San Jose, CA, USA 82018, because she prefers delivery to that location. You also want to change the payment method for this order from PayPal to her Visa card ending in 1373, as she prefers to use that card for this purchase. Later, you would like to cancel another pending order that includes a wired RGB gaming mouse and a 13-inch space grey laptop with 16GB RAM and 512GB SSD, because it was placed by mistake. After that, you would like to confirm the cancellation status of that order to ensure it has been successfully cancelled.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8005719', 'address1': '4527 Pine Avenue', 'address2': 'Floor 924', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '82018'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8005719', 'payment_method_id': 'credit_card_2713802'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3510092', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3510092'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.santos8390@example.com',
        instruction='You are assisting Harper Santos, whose email is harper.santos8390@example.com. You want to first browse the available product types in the store, with a specific interest in Running Shoes. You would like to see detailed options for Running Shoes, particularly those in size 9, available in colors like white, yellow, or black, made of mesh or synthetic materials, as these align with common athletic preferences for lightweight and breathable footwear. Later, you want to update the shipping address for a pending order currently set to Charlotte, NC, to ensure it reaches your new location. You prefer the order to be shipped to 2255 Cedar Road, Unit 712, New York, NY, USA 73907, because it is your current residence. After the update, you would like confirmation that the new address has been successfully applied to avoid delivery issues.\n\nUse harper.santos8390@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6938111410'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6629830', 'address1': '2255 Cedar Road', 'address2': 'Unit 712', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '73907'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6629830'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.santos9082@example.com',
        instruction='You are assisting Ethan Santos (email: ethan.santos9082@example.com). You want to cancel the pending order containing items like a red softshell 2-piece Luggage Set and a black 7-inch Tablet because he no longer needs it. Later, you would like to update the shipping address for another pending order—currently going to Denver and containing a polyester medium grey Pet Bed, a white wireless Gaming Mouse, and a red leather Office Chair—to 7298 Cedar Road, Suite 253, Los Angeles, CA, USA 79877. At the same time, you want to change the Pet Bed in that order from the current medium polyester grey version to the medium fleece grey version because it offers a softer and more comfortable material. After that, you would like to update the customer’s default address to match the new shipping address at 7298 Cedar Road, Suite 253, Los Angeles, to ensure all future orders are delivered correctly.\n\nUse ethan.santos9082@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5320242', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5320242'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4642822', 'address1': '7298 Cedar Road', 'address2': 'Suite 253', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '79877'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_santos_6104', 'address1': '7298 Cedar Road', 'address2': 'Suite 253', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '79877'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4642822', 'item_ids': ['2405281423'], 'new_item_ids': ['6857426243'], 'payment_method_id': 'credit_card_9784468'}),
            Action(name='get_product_details', kwargs={'product_id': '2747247837'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.ahmed2006@example.com',
        instruction='You are Evelyn Ahmed, and your email is evelyn.ahmed2006@example.com. You are first interested in exploring the available product types, particularly Hiking Boots, and want to know the available sizes and materials for that product. You then want to modify your pending order by updating the shipping address to 8100 Lincoln Street, Apt 614, Columbus, OH, USA 37875 because you need the package delivered to a different location. You also want to exchange the Hiking Boots in your order, which are size 10 made of leather with waterproofing, for the same model in size 11 made of leather with waterproofing, because the original size does not fit. You prefer the larger size for better comfort during long hikes. You want any price difference to be handled using your Mastercard ending in 9838, as you prefer this payment method for adjustments. Later, you change your mind and decide to cancel the entire order because you no longer need the items.\n\nUse evelyn.ahmed2006@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1416704', 'address1': '8100 Lincoln Street', 'address2': 'Apt 614', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '37875'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1416704'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1416704', 'item_ids': ['7228247242'], 'new_item_ids': ['6159919747'], 'payment_method_id': 'credit_card_7898168'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1416704', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.martin4637@example.com',
        instruction='You are Mei Martin (mei.martin4637@example.com). You want to update the shipping address for your pending order—containing a charcoal portable grill, green small polyester backpack with camera compartment, large red mountain bicycle, and A6 hardcover notebook—from Jacksonville, FL to your new address in Columbus, OH (322 Elm Street, Suite 586). Later, you would like to exchange the office chair from your delivered order—currently a black fabric high-back chair with no armrests—for a similar black fabric chair but with fixed armrests and a standard backrest, as you prefer better arm support and find the high-back design too tall for your desk setup. You would like the price difference from the exchange to be processed via your PayPal account, as that was your original payment method. Before finalizing the exchange, you want to browse the full range of available product types to explore other potential options, and you specifically want detailed information on the office chair variants to confirm your selection is the best fit for your workspace.\n\nUse mei.martin4637@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7017301', 'address1': '322 Elm Street', 'address2': 'Suite 586', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '43133'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mei_martin_4260', 'address1': '322 Elm Street', 'address2': 'Suite 586', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '43133'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5564375', 'item_ids': ['1793929609'], 'new_item_ids': ['8426249116'], 'payment_method_id': 'paypal_2299608'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5564375', 'item_ids': ['1793929609'], 'payment_method_id': 'paypal_2299608'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7017301'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7017301', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4794339885'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.muller9246@example.com',
        instruction='You are assisting Yara Muller (email: yara.muller9246@example.com). You want to exchange the black fleece jacket in size L with full zipper, from the delivered order shipped to Phoenix, for a new variant in size XL, navy, with half zipper, because it better fits her preference for a more relaxed fit and modern style. You prefer the price difference to be handled using the Visa card ending in 6918. Later, you would like to update the shipping address for the pending order containing the professional light-skin-tone makeup kit to a new location in Phoenix: 1868 Adams Road, Floor 539, AZ, USA 35052, to ensure it reaches the correct destination. You prefer any adjustments to be processed using the same Visa card ending in 6918.\n\nUse yara.muller9246@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9384736'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9384736', 'item_ids': ['9385662952'], 'new_item_ids': ['8590708195'], 'payment_method_id': 'credit_card_3095586'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5056519', 'address1': '1868 Adams Road', 'address2': 'Floor 539', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '35052'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yara_muller_8652', 'address1': '1868 Adams Road', 'address2': 'Floor 539', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '35052'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.johnson2300@example.com',
        instruction='You are assisting Fatima Johnson (email: fatima.johnson2300@example.com). You want to exchange the blue v-neck T-Shirt in size S from her delivered order for the same style in size M, because it was received but does not fit; you prefer the replacement to maintain the v-neck style and blue color while upgrading to a cotton material if available. You prefer the $3.96 price difference to be refunded to your PayPal account used in the original purchase. Later, you would like to update the shipping address for your pending order to 3031 Park Drive, Floor 643, San Diego, CA, USA 55355, because you are relocating temporarily. After that, you would like to cancel the entire pending order, because you no longer need the hiking boots, action camera, electric kettle, cycling helmet, and wristwatch originally ordered due to changed plans.\n\nUse fatima.johnson2300@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9389413'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9389413', 'item_ids': ['5047954489'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_5364164'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5199551', 'address1': '3031 Park Drive', 'address2': 'Floor 643', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '55355'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5199551', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (yusuf.garcia2909@example.com). You want to update the shipping address for a pending order containing a grey medium polyester backpack with a laptop compartment to 3975 Jefferson Avenue, Floor 975, Austin, TX, USA 30603, because the original address in Washington, DC is no longer valid. Later, you would like to modify another pending order that includes hiking boots, a 13-inch black laptop with i7 processor, 32GB RAM, and 512GB SSD, and an air purifier, by exchanging the current laptop for a 17-inch black model with i7 processor, 32GB RAM, and 1TB SSD, because you prefer a larger screen and more storage for productivity use, and you prefer to use your PayPal account to handle any price adjustment. After that, you would like to cancel the same order entirely because you no longer need the items, including the upgraded laptop, hiking boots, and air purifier.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6885344', 'address1': '3975 Jefferson Avenue', 'address2': 'Floor 975', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '30603'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2564042', 'item_ids': ['1657832319'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.santos9082@example.com',
        instruction='You are assisting Ethan Santos (email: ethan.santos9082@example.com). You want to modify the Luggage Set in his pending order (currently a 2-piece, red, softshell set) to the 4-piece, blue, softshell version because he prefers more packing capacity and a different color. You prefer any price difference to be processed using his PayPal account. Later, you will cancel the entire order because he has decided he no longer needs these items. Separately, for another pending order containing a pet bed, gaming mouse, and office chair, you want to update the shipping address to 6283 Washington Boulevard, Floor 804, Oklahoma City, OK, USA 27468 because he has moved. After that, you would like to update his default address in the system to this new Oklahoma City address so future orders are delivered correctly.\n\nUse ethan.santos9082@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5320242'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5320242', 'item_ids': ['7160999700'], 'new_item_ids': ['8759627937'], 'payment_method_id': 'paypal_3549141'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5320242', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4642822', 'address1': '6283 Washington Boulevard', 'address2': 'Floor 804', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '27468'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_santos_6104', 'address1': '6283 Washington Boulevard', 'address2': 'Floor 804', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '27468'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.santos3158@example.com',
        instruction="You are assisting Ivan Santos (email: ivan.santos3158@example.com). You want to first modify the Office Chair in your pending order from red mesh to the blue leather version because you prefer a more elegant look and better durability. However, later you decide you no longer need the chair, so you would like to cancel the entire order instead. After that, you would like to update the shipping address for another pending order to 1569 Cedar Road, Apt 825, Chicago, IL, USA 98328 because you've moved temporarily. You also prefer to set this new address as your default for all future orders to ensure deliveries go to the correct location moving forward. You prefer refunds to be processed back to the original PayPal method used for payment.\n\nUse ivan.santos3158@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8770097'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8770097', 'item_ids': ['4274709903'], 'new_item_ids': ['4168944673'], 'payment_method_id': 'paypal_6151711'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8770097', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5183325', 'address1': '1569 Cedar Road', 'address2': 'Apt 825', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '98328'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ivan_santos_6635', 'address1': '1569 Cedar Road', 'address2': 'Apt 825', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '98328'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.sanchez6979@example.com',
        instruction='You are assisting James Sanchez (email: james.sanchez6979@example.com) with a pending order originally shipped to Chicago. You want to update the shipping address for the pending order containing an Action Camera (silver, 1080p, not waterproof) from 219 Park Avenue, Suite 437, Chicago, IL, USA 60623 to 2288 Pine Avenue, Apt 567, Denver, CO, USA 81618. Later, you will cancel this order because it is no longer needed. After that, you would like to explore the Backpack product for a potential future purchase, particularly interested in variants with a camera compartment, durable material, and in colors such as black, green, or grey. You prefer options in large size if available, and you are considering value and functionality for outdoor or travel use. You prefer the refund for the canceled order to be processed back to the original payment method, PayPal.\n\nUse james.sanchez6979@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7464385', 'address1': '2288 Pine Avenue', 'address2': 'Apt 567', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '81618'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7464385', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7464385'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.santos7683@example.com',
        instruction='You are Emma Santos, and you are updating the shipping address for your pending order. You want the order, which includes a blue leather office chair, a bamboo 31-inch custom skateboard, two 750ml water bottles (one blue plastic, one red stainless steel), and a space grey 13-inch laptop with i7 processor and 32GB RAM, to be shipped to your new office at 2876 Main Street, Suite 206, Detroit, MI, USA 53315 instead of the original San Antonio address because you recently moved your workplace. You prefer the change be made before the order is processed to ensure timely and correct delivery. You also confirm that the payment was made using a gift card and prefer that no additional charges or payment updates are needed.\n\nUse emma.santos7683@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9903153'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9903153', 'address1': '2876 Main Street', 'address2': 'Suite 206', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '53315'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.lee1693@example.com',
        instruction='You are assisting Fatima Lee (fatima.lee1693@example.com), who has a pending order currently set to ship to San Jose, CA. You want to change the shipping address for this order to 3389 Pine Avenue, Suite 683, Jacksonville, FL, USA 95899, because she needs the items delivered to her new location. Later, you will update her default address in the account settings to match this new Jacksonville address, so future orders are sent to the correct place. After that, you would like to review the Backpack product for potential future purchase, as she is interested in a durable, functional bag; the product comes in multiple colors and sizes, with options including laptop or camera compartments and materials like nylon or polyester, priced around $200.\n\nUse fatima.lee1693@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8098147'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8098147', 'address1': '3389 Pine Avenue', 'address2': 'Suite 683', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '95899'}),
            Action(name='modify_user_address', kwargs={'user_id': 'fatima_lee_3440', 'address1': '3389 Pine Avenue', 'address2': 'Suite 683', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '95899'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.rossi2645@example.com',
        instruction='You are assisting Sofia Rossi (sofia.rossi2645@example.com), whose order is still pending and currently set to ship to an outdated address. You want to update the shipping address for this order to 827 Oak Avenue, Unit 202, Seattle, WA, USA 78902, because she realized the initial address was incorrect. You also want to update her default address in profile settings to the same Seattle address for future orders. After completing the address update, you would like to explore the product catalog, specifically to view Action Cameras, because she is considering a future purchase in that category.\n\nUse sofia.rossi2645@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5918442'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5918442', 'address1': '827 Oak Avenue', 'address2': 'Unit 202', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '78902'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_rossi_8776', 'address1': '827 Oak Avenue', 'address2': 'Unit 202', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '78902'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.johnson6791@example.com',
        instruction='You are Omar Johnson, with email omar.johnson6791@example.com, and you have a pending order for a Laptop and an Indoor Security Camera currently set to ship to 349 Cedar Street, Suite 322, Denver, CO, 80266. You want to update the shipping address for this order to 8916 Madison Drive, Apt 15, Denver, CO, 92274 because you entered the wrong address initially. You also want to review the details of the Action Camera product, which offers 4K and 5K resolution options, is available in black and silver, and is waterproof in most variants, so you can consider adding it to a future order. Later, you would like to browse the full catalog of available product types—such as Backpack, Bicycle, Coffee Maker, Headphones, Smart Watch, and others—to explore what other items are offered in the store. You prefer the refund or any future payment adjustments to remain on the original gift card used for purchase.\n\nUse omar.johnson6791@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8797321', 'address1': '8916 Madison Drive', 'address2': 'Apt 15', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '92274'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8797321', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8797321'}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are assisting Fatima Wilson (email: fatima.wilson5906@example.com) with her pending order originally shipped to Austin, TX. You want to update the shipping address for her order containing a blue leather Office Chair and a large gas grill to 4549 Oak Avenue, Suite 142, Phoenix, AZ, USA 33846, so it can be redirected. Later, you will cancel the order because she no longer needs the items. You would like to confirm the order details, particularly the Office Chair with fixed armrests and standard backrest height, to ensure accuracy before cancellation. After that, you want to explore all available product types in the store catalog to consider future purchases, including options like Backpacks, Headphones, Smart Watches, and Yoga Mats, as she is interested in browsing alternatives for upcoming needs.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1443906', 'address1': '4549 Oak Avenue', 'address2': 'Suite 142', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '33846'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1443906', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1443906'}),
            Action(name='get_product_details', kwargs={'product_id': '4794339885'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.ahmed4901@example.com',
        instruction='You are assisting Mei Ahmed, whose email is mei.ahmed4901@example.com, with updating the shipping address for her pending order containing a digital camera and an espresso machine. You want to change the shipping address from her current Austin location to 8075 Jackson Street, Unit 207, San Jose, CA, USA 99187 because she provided an incorrect address at checkout and needs the items delivered to her new location. After resolving the address update, you would like to support her interest in exploring the full product catalog to discover items for future purchase, such as backpacks, laptops, or smart home devices, because she is interested in expanding her shopping beyond the current order.\n\nUse mei.ahmed4901@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2598324', 'address1': '8075 Jackson Street', 'address2': 'Unit 207', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '99187'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2598324', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2598324'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7553978', 'item_ids': ['4545791457'], 'payment_method_id': 'credit_card_5902940'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7553978', 'item_ids': ['4545791457'], 'new_item_ids': ['3098764622'], 'payment_method_id': 'credit_card_5902940'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8940227892'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.santos3158@example.com',
        instruction='You are assisting Ivan Santos (email: ivan.santos3158@example.com), who initially wanted to update the shipping address for his pending order of a red mesh office chair currently set to be delivered to Dallas, TX, to a new location. Later, he decided to cancel the order entirely because he no longer needs the chair, so you should not proceed with the address update. After cancellation, he expressed interest in browsing available products, specifically wanting to learn more about the Backpack options, such as color, size, material, and compartment type, to consider a new purchase.\n\nUse ivan.santos3158@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8770097'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8770097', 'address1': '2147 Cedar Road', 'address2': 'Apt 480', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '18965'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8770097', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen.anderson4495@example.com',
        instruction='You are assisting Chen Anderson (email: chen.anderson4495@example.com) with his pending order for sunglasses and headphones. You want to verify the details of the sunglasses in his order, which are black-framed, blue-lensed, polarized, metal-frame sunglasses, before proceeding. You would like to change the shipping address for this order to 1441 Pine Avenue, Suite 947, San Diego, CA, USA 73286, because he needs the items delivered to a new location. After that, you want to update his default address to the same San Diego address for future orders. Later, you are interested in browsing the full catalog of available product types, such as Air Purifiers, Backpacks, Coffee Makers, Headphones, Sunglasses, and others, to explore what else the store offers.\n\nUse chen.anderson4495@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1348788'}),
            Action(name='get_product_details', kwargs={'product_id': '7314138884'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1348788', 'address1': '1441 Pine Avenue', 'address2': 'Suite 947', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '73286'}),
            Action(name='modify_user_address', kwargs={'user_id': 'chen_anderson_8078', 'address1': '1441 Pine Avenue', 'address2': 'Suite 947', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '73286'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah.ito4296@example.com',
        instruction='You are assisting Noah Ito (email: noah.ito4296@example.com) with three order actions. First, you want to exchange the Cycling Helmet (currently size L, color blue, high ventilation) from your delivered order for a red one in size M with high ventilation, because it better fits your needs. You prefer to use your Mastercard ending in 1065 for any price difference. Later, you would like to update the shipping address for your pending order containing a 2000-piece animal-themed puzzle and two blue-dial wristwatches (one with silicone strap, one with metal) to 1561 Maple Lane, Floor 315, Las Vegas, NV, USA 23869, to ensure delivery to your new location. After that, you would like to cancel your other pending order containing a black Bluetooth speaker and a medium-room air purifier with quiet operation, because you no longer need these items.\n\nUse noah.ito4296@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3445693'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3445693', 'item_ids': ['2206116040'], 'new_item_ids': ['8573379326'], 'payment_method_id': 'credit_card_1620755'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4219264', 'address1': '1561 Maple Lane', 'address2': 'Floor 315', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '23869'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6729841', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.ahmed1696@example.com',
        instruction='You are Lei Ahmed, with email lei.ahmed1696@example.com, and you want to update the shipping address for your pending order—which includes a bamboo skateboard and two cycling helmets (one red medium, one black large)—from Philadelphia to 2227 Oak Avenue, Suite 151, San Jose, CA, USA 93850, because you have recently moved. After that, you would like to browse the full catalog of product types available in the store, particularly interested in outdoor and tech gear, to explore future purchase options.\n\nUse lei.ahmed1696@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9132840', 'address1': '2227 Oak Avenue', 'address2': 'Suite 151', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '93850'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.moore2816@example.com',
        instruction='You are assisting Harper Moore (email: harper.moore2816@example.com) with modifying her pending order. You want to first understand the available tea kettles to make an informed decision. After reviewing the options, you decide to change the tea kettle in the order from the current glass 1.5L induction-compatible model to a stainless steel 2L gas-compatible one, as it is more compatible with your gas stovetop and offers greater capacity. You also want to update the shipping address to a new location in Nashville. You prefer to use your Mastercard ending in 3161 for any price difference associated with the item change.\n\nUse harper.moore2816@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9832717871'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3942868'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3942868', 'item_ids': ['6454334990'], 'new_item_ids': ['4238115171'], 'payment_method_id': 'credit_card_7665260'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3942868', 'address1': '5493 Main Street', 'address2': 'Suite 925', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '32325'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.santos7226@example.com',
        instruction='You are assisting Liam Santos (liam.santos7226@example.com). You want to cancel a pending order that includes a red medium Cycling Helmet and a 2-liter stainless steel Tea Kettle because it was placed by mistake. Then, you would like to update the shipping address for another pending order containing a full-size RGB mechanical keyboard, a bagless canister vacuum cleaner, an 80% tactile white-backlit mechanical keyboard, a red small fleece jacket, and a 1000ml stainless steel red water bottle to 1303 Lincoln Street, Unit 520, Boston, MA, USA 95056, as the current Austin address is no longer valid. After handling these changes, you would like to browse the product catalog and view details for the Action Camera, possibly for use on an upcoming trip.\n\nUse liam.santos7226@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6794581', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6794581'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4011814', 'address1': '1303 Lincoln Street', 'address2': 'Unit 520', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '95056'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_santos_5468', 'address1': '1303 Lincoln Street', 'address2': 'Unit 520', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '95056'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen.ahmed5266@example.com',
        instruction='You are a customer with email chen.ahmed5266@example.com who placed a pending order containing a red large cycling helmet with high ventilation, a cordless robotic vacuum cleaner, an adjustable 55-75 lbs urethane dumbbell set, and a gold 128GB smartphone with 6GB RAM and a 6.1-inch screen. You want the shipping address for this order to be updated from Indianapolis, IN to 9771 Jefferson Avenue, Apt 523, Philadelphia, PA, USA 33170. After the update, you would like confirmation that the new address is correctly reflected in the order details.\n\nUse chen.ahmed5266@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8268544', 'address1': '9771 Jefferson Avenue', 'address2': 'Apt 523', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '33170'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8268544'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen2868@example.com',
        instruction='You are assisting Ava Nguyen (email: ava.nguyen2868@example.com) with updating the shipping address for her pending order containing a dumbbell set (55-75 lbs, iron), a red Bluetooth speaker, and a red fleece jacket (size L, half-zip). You want to change the shipping address from Los Angeles, CA to 7809 Jackson Street, Unit 956, Las Vegas, NV, USA 59649 because the original address was entered incorrectly and the order has not yet shipped.\n\nUse ava.nguyen2868@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8367380', 'address1': '7809 Jackson Street', 'address2': 'Unit 956', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '59649'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8367380'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting Ethan Thomas (email: ethan.thomas7730@example.com). You want to update the shipping address for his pending order—which includes a black silicone-band AMOLED smart watch and a gold 128GB smartphone—to 8044 Washington Boulevard, Apt 299, New York, NY, USA 31339, because he needs it delivered to a new location. You also want to update his default address to the same, to ensure future orders are sent to this address. Later, you would like to browse the available product catalog to explore what items are currently offered, including categories like air purifiers, backpacks, bicycles, coffee makers, headphones, laptops, smart home devices, and more, in preparation for future purchases.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '8044 Washington Boulevard', 'address2': 'Apt 299', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '31339'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_thomas_1791', 'address1': '8044 Washington Boulevard', 'address2': 'Apt 299', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '31339'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.santos9317@example.com',
        instruction="You are assisting Isabella Santos (email: isabella.santos9317@example.com) with her pending order containing a gold Smart Watch with a leather band and a pair of size 7 synthetic waterproof Hiking Boots. You want to update the shipping address for this order to 1877 Washington Boulevard, Apt 609, Seattle, WA, USA 20827, because it was initially set to a New York address. You also want to update her default address in profile to the same Seattle address to prevent future shipping errors. Later, if needed, you may cancel the order with the reason 'no longer needed'. After handling the address updates, you would like to explore the product catalog, specifically reviewing the Hiking Boots (product ID 7363354090), to understand available variants such as different sizes, materials, and waterproof options for potential future purchases.\n\nUse isabella.santos9317@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9527030', 'address1': '1877 Washington Boulevard', 'address2': 'Apt 609', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '20827'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_santos_1643', 'address1': '1877 Washington Boulevard', 'address2': 'Apt 609', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '20827'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9527030', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9527030'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.patel2010@example.com',
        instruction='You are assisting Evelyn Patel (email: evelyn.patel2010@example.com) with a modification to her pending order in Charlotte, NC. You want to exchange the purple XL cotton crew neck T-shirt for the black XL cotton crew neck T-shirt of the same style, as she prefers the black color over the purple. Since the order is still pending, this change is feasible. You prefer the price difference to be covered using her PayPal account, which was previously used for the original payment.\n\nUse evelyn.patel2010@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6385395'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6385395', 'item_ids': ['8124970213'], 'new_item_ids': ['2060066974'], 'payment_method_id': 'paypal_3704667'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting Ethan Thomas (email: ethan.thomas7730@example.com) with modifying his pending order placed in Columbus, OH. You want to change the Smart Watch from black to gold while keeping the same silicone band and AMOLED display, because he prefers the gold color. You would like the price difference refunded to your PayPal account, as specified. After that, you prefer the updated order to proceed with the gold Smart Watch at the adjusted cost.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8465042', 'item_ids': ['4920090458'], 'new_item_ids': ['2681513500'], 'payment_method_id': 'paypal_6982172'}),
            Action(name='get_product_details', kwargs={'product_id': '6945232052'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.thomas1454@example.com',
        instruction='You are assisting Harper Thomas (email: harper.thomas1454@example.com) with her pending order and product inquiry. You want to update the shipping address for the pending order containing a green 6mm PVC yoga mat and a black Smart Thermostat compatible with Apple HomeKit to 3023 Madison Drive, Suite 867, San Antonio, TX, USA 34157, because she needs it delivered to a new location. Later, you would like to change the payment method from the Visa ending in 5768 to the Mastercard ending in 7287, because she prefers to use that card for this purchase. After that, you are interested in browsing the available product types to explore future purchases, specifically wanting to learn more about the Action Camera model, because she is considering buying one.\n\nUse harper.thomas1454@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7425646', 'address1': '3023 Madison Drive', 'address2': 'Suite 867', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '34157'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7425646', 'payment_method_id': 'credit_card_1199336'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7425646'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.moore8091@example.com',
        instruction="You are mia.moore8091@example.com. You want to accomplish these, in order:\n1. Hi, my email is mia.moore8091@example.com. For my pending order #W3130288, please update the shipping address to: 8937 Adams Road, Floor 315, San Jose, CA, USA 26719. Also, change the payment method to my Mastercard ending in 2992.\n2. I'd like to browse your product catalog. Could you tell me what product types you offer? Then, please get the details for the Action Camera with product ID 3377618313.\n\nUse mia.moore8091@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3130288', 'address1': '8937 Adams Road', 'address2': 'Floor 315', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '26719'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3130288', 'payment_method_id': 'credit_card_2641784'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3130288'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, and your email is olivia.ito5204@example.com. You want to exchange the black wired gaming mouse in your pending order for a white wireless one because you prefer a cleaner look and wireless convenience. You prefer the refund or charge adjustment to be handled on your Visa card ending in 9182 for the small price difference. Later, you would like to update the shipping address for another pending order to 9602 Lincoln Street, Unit 324, Austin, TX, USA 93673. After that, you would like to cancel that same order because you realized it was placed by mistake.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5442520', 'item_ids': ['3330317167'], 'new_item_ids': ['8896479688'], 'payment_method_id': 'credit_card_9753331'}),
            Action(name='get_product_details', kwargs={'product_id': '5713490933'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7941031', 'address1': '9602 Lincoln Street', 'address2': 'Unit 324', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '93673'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7941031', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.kim6594@example.com',
        instruction='You are mei.kim6594@example.com, and you want to first update the shipping address for your pending order—containing an automatic espresso machine with 9 bar pressure and 1L water tank, and a 60% mechanical keyboard with linear switches and RGB backlighting—from Houston, TX to 3879 Washington Boulevard, Suite 424, Jacksonville, FL 19773 because it was intended for a different location. Later, you would like to cancel the entire order because it was placed by mistake. You prefer any refund to be returned to the original gift card used for payment.\n\nUse mei.kim6594@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3263208', 'address1': '3879 Washington Boulevard', 'address2': 'Suite 424', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '19773'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3263208', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.ito3877@example.com',
        instruction='You are Sofia Ito (sofia.ito3877@example.com) and you initially want to learn more about the black 13-inch Laptop with i7 processor, 32GB RAM, and 512GB SSD because you are considering a high-performance device for daily use. Later, you would like to return the purple v-neck polyester T-Shirt in size S from your delivered order in Philadelphia because it does not meet your style preference, and you prefer the refund to be issued back to your PayPal account. After that, you would like to cancel your pending order in Philadelphia containing a black leather-band Smart Watch and a Wi-Fi connected daylight LED bulb because you realized it was placed by mistake.\n\nUse sofia.ito3877@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5257743'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5257743', 'item_ids': ['9647292434'], 'payment_method_id': 'paypal_6882355'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1514731', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com). You want to exchange the non-waterproof 5K black Action Camera from your delivered order (shipped to Washington, DC) for the available 4K waterproof black model, because you need a camera that can be used in wet conditions. You prefer the refund for the price difference to be processed back to your PayPal account. Later, after confirming the available variants, you would like to proceed with the exchange. After that, you want to cancel your pending order (shipped to Indianapolis, IN) containing the Hiking Boots, Laptop, and Air Purifier, because you no longer need those items.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2286012'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2286012', 'item_ids': ['7523669277'], 'new_item_ids': ['6700049080'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.muller6617@example.com',
        instruction='You are assisting Ethan Muller (email: ethan.muller6617@example.com) with two main requests, followed by exploration. First, you want to cancel his pending order placed by mistake, which includes a stainless steel green 500ml water bottle, a bagged upright vacuum cleaner with pet hair removal, a glass 1-liter tea kettle for electric stoves, an automatic 19-bar espresso machine with 1.5L capacity, and a 12-inch white analog wall clock. After that, you would like to exchange the 1500-piece intermediate-level art jigsaw puzzle from his delivered order for a 1500-piece intermediate-level animals jigsaw puzzle, because he prefers the animals theme over art. You prefer to use his Visa card ending in 1399 for any price difference associated with the exchange. Later, you want to explore all available product types in the store to consider future purchases. Subsequently, you would like to see the full details of the Jigsaw Puzzle product, including all available variants by piece count, theme, and difficulty, to better understand current options.\n\nUse ethan.muller6617@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4683557', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4398027'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W4398027', 'item_ids': ['5546244844'], 'new_item_ids': ['6245746168'], 'payment_method_id': 'credit_card_5721095'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W4398027', 'item_ids': ['5546244844'], 'payment_method_id': 'credit_card_5721095'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are assisting Sophia Thomas (sophia.thomas1364@example.com) with her order requests. You want to cancel the pending order placed for a white wood bookshelf, a silver 7-inch tablet, a blue fabric office chair, and a gray leather office chair, as she no longer needs these items. Later, you would like to exchange the green 6mm PVC Yoga Mat from her delivered order for the blue 4mm PVC variant, as she prefers the thinner and differently colored mat. After that, you are interested in exploring the full range of Yoga Mat options, particularly focusing on thickness, color, and material variations to better understand available choices.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4862767', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1867876'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1867876', 'item_ids': ['7510236436'], 'new_item_ids': ['5586947715'], 'payment_method_id': 'credit_card_1034663'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4635925001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting Fatima Li (email: fatima.li1185@example.com). You want to explore the available variants for the Action Camera, which include 4K and 5K resolution models in black or silver, with waterproof options, to understand the range of features and pricing. Later, you will update the shipping address for your pending order containing a skateboard and an espresso machine to 2795 Jefferson Avenue, Apt 718, Denver, CO, USA 57764, because you need the delivery redirected to a new location. After that, you would like to exchange the current 31-inch maple deck skateboard with graphic design for a 31-inch bamboo deck skateboard with the same graphic design, as you prefer the sustainability and feel of bamboo over maple. You prefer any payment adjustment for the exchange to be handled using your PayPal account, which was previously used for the original purchase.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8005719', 'address1': '2795 Jefferson Avenue', 'address2': 'Apt 718', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '57764'}),
            Action(name='modify_user_address', kwargs={'user_id': 'fatima_li_5040', 'address1': '2795 Jefferson Avenue', 'address2': 'Apt 718', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '57764'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8005719', 'item_ids': ['5120532699'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'paypal_6366157'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.lopez8921@example.com',
        instruction='You are assisting Mason Lopez (email: mason.lopez8921@example.com). You want to learn more about the Action Camera product offered. Later, you want to update the shipping address for a pending order containing a red medium cycling helmet and a ceramic tea kettle to 6653 Main Street, Suite 278, San Francisco, CA, USA 57139, because the original address in Charlotte is no longer valid. After that, you want your default address updated to the same San Francisco address for future orders. Subsequently, you would like to modify an item in another pending order by changing the 2L glass Electric Kettle from silver to white, preferring the white version for better kitchen aesthetics while keeping the same capacity and material. You prefer any price difference to be charged to your Mastercard ending in 4629.\n\nUse mason.lopez8921@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9892169', 'address1': '6653 Main Street', 'address2': 'Suite 278', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '57139'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mason_lopez_8519', 'address1': '6653 Main Street', 'address2': 'Suite 278', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '57139'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7752859', 'item_ids': ['3015420423'], 'new_item_ids': ['4064702754'], 'payment_method_id': 'credit_card_2327218'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.brown3708@example.com',
        instruction='You are assisting aarav.brown3708@example.com, who has a pending order for a 30-50 lbs adjustable iron dumbbell set, a 750ml black glass water bottle, and a blue-dial metal-strap wristwatch. You want to update the shipping address for this order to 920 Lincoln Street, Suite 513, Los Angeles, CA, USA 45103 because the original address was incorrect. Later, you decided to cancel the entire order because it was placed by mistake, and no fulfillment has occurred yet.\n\nUse aarav.brown3708@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5065081', 'address1': '920 Lincoln Street', 'address2': 'Suite 513', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '45103'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5065081', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5065081'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting Yusuf Gonzalez (yusuf.gonzalez2399@example.com) with his pending order originally shipped to Los Angeles, CA. You want to update the shipping address to 958 Madison Drive, Unit 194, Fort Worth, TX, USA 22049 for better delivery access. You would like to change the payment method from your Mastercard ending in 9928 to PayPal for easier transaction tracking. You also want to exchange the ceramic tea kettle (1.5 liters, gas-compatible) in your order for the available glass version with the same 1.5-liter capacity and gas stovetop compatibility, as you prefer the visibility and aesthetic of glass over ceramic. Later, you would like to browse the available variants of tea kettles, particularly comparing materials, capacities, and stovetop compatibility, to make informed choices for future purchases.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '958 Madison Drive', 'address2': 'Unit 194', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '22049'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2806889', 'item_ids': ['7497340597'], 'new_item_ids': ['9647374798'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9832717871'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.brown5032@example.com',
        instruction='You are assisting Emma Brown (email: emma.brown5032@example.com) with her pending order. You want to first review the order details for the skateboard currently listed as plastic, 34 inch, plain. Then, you would like to update the shipping address to 9518 Lincoln Street, Floor 947, Philadelphia, PA, USA 77029. After that, you prefer to change the payment method from PayPal to your Visa card ending in 9135, and use this card for any price adjustment. You also want to exchange the current skateboard for a different variant: you prefer the bamboo deck, 31 inch, with a graphic design over the current one because it better suits your riding style and aesthetic preference. While these changes are being processed, you would like to browse the available product types in the catalog to explore other options. Finally, you want to see detailed information about the Skateboard product line to better understand the available choices and features.\n\nUse emma.brown5032@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6460787'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6460787', 'address1': '9518 Lincoln Street', 'address2': 'Floor 947', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '77029'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6460787', 'payment_method_id': 'credit_card_8850930'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6460787', 'item_ids': ['3098764622'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'credit_card_8850930'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are Liam Thomas, with email liam.thomas9081@example.com, and you want to browse the available products. You have a pending order containing an E-Reader with 7-inch screen and 8GB storage, and an Air Purifier designed for small rooms with ionic filter and quiet operation, originally shipped to Phoenix, AZ. You would like to change the shipping address for this order to 7051 Cedar Road, Apt 365, Houston, TX, USA 60068, because you will be traveling and prefer delivery to the new location. After updating the address, you later decide to cancel the order because your needs have changed and you no longer require the items. You would like to confirm the updated status of the order after cancellation. Finally, you want to see the details of the Action Camera product, particularly models with 4K resolution and waterproof capability, to evaluate it for a future purchase.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1654931', 'address1': '7051 Cedar Road', 'address2': 'Apt 365', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '60068'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1654931', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1654931'}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2532@example.com',
        instruction='You are yusuf.garcia2532@example.com and want to update the shipping address for your pending order containing a purple v-neck polyester T-shirt, a basic light-skin-tone makeup kit, and a green Bluetooth speaker with 10-hour battery life, currently set to ship to Indianapolis. You want the new shipping address to be 5639 Jefferson Avenue, Floor 144, Denver, CO, USA 37779 because you have moved and need the order delivered to your current location.\n\nUse yusuf.garcia2532@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7639559', 'address1': '5639 Jefferson Avenue', 'address2': 'Floor 144', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '37779'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.moore8091@example.com',
        instruction='You are Mia Moore, with email mia.moore8091@example.com, and you want to update your pending order currently shipping to San Francisco. You want the shipping address changed to 710 Sunset Drive, Suite 303, Philadelphia, PA, to align with your current location. You prefer to change the payment method from the original gift card to your Mastercard ending in 2992 for better expense tracking. You also want to exchange the gold smartwatch with silicone band and LCD display for the black one with the same features, as you prefer the more understated look. For any refund due from this change, you would like it processed to your PayPal account. Later, you would like to exchange an item from your delivered order in Philadelphia: you want to replace the blue low-speed electric toothbrush with the white high-speed model, because you prefer a faster brushing experience and a cleaner aesthetic. For any price difference in this exchange, you prefer to use your PayPal account. After that, you would like a full list of all product types available in the store, so you can explore future purchases across categories like smartwatches, electric toothbrushes, vacuum cleaners, bookshelves, backpacks, headphones, and more.\n\nUse mia.moore8091@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3130288', 'address1': '710 Sunset Drive', 'address2': 'Suite 303', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '19186'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3130288', 'payment_method_id': 'credit_card_2641784'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3130288', 'item_ids': ['2540052208'], 'new_item_ids': ['2860956907'], 'payment_method_id': 'paypal_5181300'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5544629'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5544629', 'item_ids': ['1583904702'], 'payment_method_id': 'paypal_5181300'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5544629', 'item_ids': ['1583904702'], 'new_item_ids': ['2645006275'], 'payment_method_id': 'paypal_5181300'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6945232052'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting Yusuf Gonzalez (email: yusuf.gonzalez2399@example.com) with multiple requests. First, for his pending order containing a Smartphone and a ceramic 1.5L tea kettle, you want to update the shipping address to 4268 Jackson Street, Unit 625, San Francisco, CA, USA 41833 because he prefers delivery there. You also want to change the payment method from Mastercard ending in 9928 to his PayPal account because he prefers to pay via PayPal. Additionally, you want to exchange the ceramic 1.5L tea kettle for the stainless steel 2L version because he prefers a larger, more durable kettle. Later, for his delivered order containing a blue medium cotton crew neck T-shirt, you would like to process an exchange for the black XL cotton crew neck T-shirt because he prefers the larger size and different color. After that, you would like to list all available product types to help him browse the full catalog, with a focus on T-shirt options for potential future purchases.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '4268 Jackson Street', 'address2': 'Unit 625', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '41833'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2806889', 'item_ids': ['7497340597'], 'new_item_ids': ['4238115171'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1679211'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1679211', 'item_ids': ['9612497925'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1679211', 'item_ids': ['9612497925'], 'new_item_ids': ['2060066974'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting Lucas Johansson (lucas.johansson7741@example.com). You want to update the payment method for a pending order containing hiking boots, a backpack, and a jigsaw puzzle—originally paid with a Mastercard ending in 3088—to instead use his Visa card ending in 9452, because he prefers to use that card for this purchase. Later, you would like to review the available variants of the Backpack product to understand current options, including different colors (black, green, grey, navy), sizes (small, medium, large), materials (nylon, leather, polyester), and compartment types (laptop, camera, hydration). After that, you would like to cancel another pending order containing an office chair and a tablet, because he no longer needs those items.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8379216', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.khan2360@example.com',
        instruction='You are Olivia Khan (olivia.khan2360@example.com). You want to change the payment method for your pending order—which includes a red cotton crew neck T-shirt, polarized black-brown sunglasses, a large brown memory foam pet bed, and a blue-dial metal-strap wristwatch—currently in Indianapolis, from PayPal to your Visa card ending in 9765, because you prefer using that card for this purchase. Later, you would like to explore available Laptop options, particularly interested in models with various screen sizes, processors, and storage configurations, to consider a future purchase. After reviewing those options, you decide you no longer need the original order and would like it canceled entirely.\n\nUse olivia.khan2360@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3840181'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3840181', 'payment_method_id': 'credit_card_1936578'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3840181', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting Lucas Johansson (lucas.johansson7741@example.com) with his order. You want to first verify the details of his pending order, which includes a pair of leather, waterproof hiking boots in size 8, a black nylon backpack with a laptop compartment, and a 500-piece expert-level animal-themed jigsaw puzzle. After that, you would like to update the shipping address for this order to 5561 Madison Drive, Unit 332, Chicago, IL, USA 29663, because he needs it delivered to a different location. Later, you will cancel the entire order because he no longer needs the items. You prefer the refund to be processed back to the original payment method, which was his credit card.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '5561 Madison Drive', 'address2': 'Unit 332', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '29663'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.li2787@example.com',
        instruction='You are Raj Li (email: raj.li2787@example.com) and you want to modify your pending order currently shipping to Fort Worth, TX. First, you want to update the shipping address to 552 Lincoln Street, Unit 120, Seattle, WA, USA 78006 because you are relocating. Then, you would like to change the payment method from your Visa ending in 3917 to your PayPal for better purchase protection. Additionally, you want to exchange one of the bookshelves in your order—the 5 ft black glass model—for the 5 ft white wood model because you prefer a lighter, more natural look that better matches your living room decor, and you would like any price difference charged to your PayPal. After completing these changes, you would like to browse the full catalog of available product types to explore other items you might be interested in purchasing.\n\nUse raj.li2787@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8967935', 'address1': '552 Lincoln Street', 'address2': 'Unit 120', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '78006'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8967935', 'payment_method_id': 'paypal_2028062'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8967935', 'item_ids': ['4900661478'], 'new_item_ids': ['2960542086'], 'payment_method_id': 'paypal_2028062'}),
            Action(name='get_product_details', kwargs={'product_id': '8600330539'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.rossi7301@example.com',
        instruction='You are reviewing the details of a pending order placed by yusuf.rossi7301@example.com for a black cotton crew neck T-Shirt in size XXL, currently priced at $53.27 and awaiting fulfillment at an address in Philadelphia, PA. You also want to see the full product information for this T-Shirt, including all available variants such as different colors (blue, purple, red, black), sizes (S to XXL), materials (cotton or polyester), and styles (crew neck or v-neck), along with their respective prices, to understand the full range of options available for this product.\n\nUse yusuf.rossi7301@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6247578'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva6106@example.com',
        instruction='You are assisting Omar Silva, whose email is omar.silva6106@example.com. You want to check the status of an order placed for delivery to Seattle, which includes a pair of black synthetic Running Shoes in size 9 with a rubber sole, along with a Mechanical Keyboard and an Electric Kettle. The order is currently pending. You would like detailed information about the Running Shoes, specifically the product available in size 9, black color, and synthetic material, to understand its features and options better.\n\nUse omar.silva6106@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6151519'}),
            Action(name='get_product_details', kwargs={'product_id': '6938111410'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.moore2816@example.com',
        instruction="You are assisting Harper Moore (harper.moore2816@example.com) with updates to her pending order. You want to update the shipping address to 3958 Madison Drive, Unit 984, San Jose, CA, USA 86758, because she has moved. Later, you would like to exchange the current tea kettle—made for induction stoves—for a model compatible with electric stovetops, since her stove is electric and the original will not work; you prefer the 2-liter glass electric-compatible version over the original 1.5-liter induction model. You prefer to use the Mastercard ending in 3161 for any price difference. After that, you would like to pre-authorize cancellation of the entire order if needed, citing 'ordered by mistake' as the reason, in case the changes cannot be processed or your plans change.\n\nUse harper.moore2816@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3942868', 'address1': '3958 Madison Drive', 'address2': 'Unit 984', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '86758'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3942868'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3942868', 'item_ids': ['6454334990'], 'new_item_ids': ['7292993796'], 'payment_method_id': 'credit_card_7665260'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3942868', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.kim6460@example.com',
        instruction='You are Amelia Kim, and your email is amelia.kim6460@example.com. You initially want to update the shipping address for your pending order—which includes a black desk lamp with medium brightness, a glass tea kettle with 1.5-liter capacity, a ceramic tea kettle also with 1.5-liter capacity, and a linear-switch mechanical keyboard without backlight—to 2156 Lincoln Street, Suite 522, Dallas, TX, USA 62197, because you expect to be in Dallas when the delivery arrives. Later, you change your mind and decide you no longer need the items, so you would like to cancel the entire order. You prefer the refund to be processed back to the original payment method, which was PayPal.\n\nUse amelia.kim6460@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7634667', 'address1': '2156 Lincoln Street', 'address2': 'Suite 522', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '62197'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7634667', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.jackson5798@example.com',
        instruction='You are Mia Jackson, and your email is mia.jackson5798@example.com. You want to update the shipping address for your pending order—which includes a black desk lamp, an espresso machine with 15 bar pressure and 1L capacity, and a 2L glass electric kettle—for delivery to 3863 Jefferson Avenue, Suite 105, San Francisco, CA, USA 13702, because you need it sent to a new location. You also want your default address updated to this new San Francisco address for future orders. Later, you would like to cancel another pending order—which includes a green leather backpack with a camera compartment, a ceramic tea kettle with 1.5-liter capacity, a small black cycling helmet, and blue wireless earbuds with 6-hour battery life—because you realized it was placed by mistake.\n\nUse mia.jackson5798@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7807323', 'address1': '3863 Jefferson Avenue', 'address2': 'Suite 105', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '13702'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mia_jackson_2250', 'address1': '3863 Jefferson Avenue', 'address2': 'Suite 105', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '13702'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1205816', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1205816'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.johansson1233@example.com',
        instruction='You are Isabella Johansson, with email isabella.johansson1233@example.com, and you want to update the shipping address for your pending order containing a Cycling Helmet, Garden Hose, T-Shirt, and Jigsaw Puzzle to 1517 Pine Avenue, Floor 203, Nashville, TN, USA 94348, because you have relocated. You also want to update your default address to this new Nashville address for future orders. Later, you would like to cancel your other pending order that includes an Espresso Machine, Makeup Kit, Pet Bed, and Wireless Earbuds, because you placed it by mistake. After that, you would like to learn more about the T-Shirt product available in the store, as you are considering future purchases.\n\nUse isabella.johansson1233@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8882972', 'address1': '1517 Pine Avenue', 'address2': 'Floor 203', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '94348'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_johansson_7408', 'address1': '1517 Pine Avenue', 'address2': 'Floor 203', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '94348'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6783532', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6783532'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.brown6764@example.com',
        instruction='You are assisting a customer with email isabella.brown6764@example.com regarding her pending order containing Wireless Earbuds (blue), an Indoor Security Camera (2K resolution), an LED Light Bulb (75W equivalent, daylight), and a Bluetooth Speaker (blue). You want to change the shipping address for this order to 2723 Oak Avenue, Apt 976, Nashville, TN, USA 30244, because it was initially entered incorrectly. You would like your default address to be updated to this new address for future orders. Later, after reconsidering, you decide the order is no longer needed and would like it canceled. You prefer the payment, originally made via gift card, to be refunded accordingly.\n\nUse isabella.brown6764@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7810809', 'address1': '2723 Oak Avenue', 'address2': 'Apt 976', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '30244'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_brown_4999', 'address1': '2723 Oak Avenue', 'address2': 'Apt 976', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '30244'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7810809', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are lucas.johansson7741@example.com, and you have a pending order for hiking boots in size 8, a black small nylon backpack with a laptop compartment, and a 500-piece expert-level animal-themed jigsaw puzzle. You want to update the shipping address for this order to 708 Park Drive, Unit 254, Philadelphia, PA, USA 81042, because you entered the wrong location initially. You also want your default profile address updated to the same Philadelphia address for future orders. Later, after reconsidering your purchase, you would like to cancel the entire order because you no longer need the items. You prefer the refund to be processed back to the original payment method, the credit card used for the transaction.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '708 Park Drive', 'address2': 'Unit 254', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '81042'}),
            Action(name='modify_user_address', kwargs={'user_id': 'lucas_johansson_1090', 'address1': '708 Park Drive', 'address2': 'Unit 254', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '81042'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.moore6985@example.com',
        instruction='You are Liam Moore, with email liam.moore6985@example.com, and you have both pending and delivered orders. You want to update the shipping address for your pending order, which includes an Air Purifier and a Bookshelf, to 8766 Main Street, Floor 956, Houston, TX, USA 51703, because you are relocating temporarily. You also want to update your default address to this same new address for future orders. Later, you would like to exchange the blue Wireless Earbuds with IPX4 water resistance from your delivered order for the black ones with IPX7 water resistance, because you prefer better protection against water during workouts. After that, you want to confirm the delivered status of that order and proceed with returning the Hiking Boots included in it, because they are uncomfortable for long hikes. You prefer the refund for the return to be processed to your PayPal account. Finally, you would like to browse the full catalog of available product types to explore other options, and specifically learn more about the Wireless Earbuds product, because you are interested in their features and variants.\n\nUse liam.moore6985@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3169501', 'address1': '8766 Main Street', 'address2': 'Floor 956', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '51703'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_moore_4057', 'address1': '8766 Main Street', 'address2': 'Floor 956', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '51703'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6908222', 'item_ids': ['8555936349'], 'new_item_ids': ['9580569596'], 'payment_method_id': 'paypal_4518393'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6908222'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6908222', 'item_ids': ['6595128475'], 'payment_method_id': 'paypal_4518393'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9924732112'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting Yusuf Gonzalez, whose email is yusuf.gonzalez2399@example.com. You want to update the shipping address for his pending order—which includes a black 128GB smartphone with 4GB RAM and a 1.5-liter ceramic tea kettle—from 285 Lakeview Drive, Suite 657, Los Angeles, CA 91455 to 2289 Jackson Street, Apt 116, Dallas, TX 46748, because he has relocated temporarily. You also want to update his default address to this new Dallas address for future orders. Later, after confirming the order details are correct, you would like to change the payment method from the Mastercard ending in 9928 to his PayPal account, as he prefers using PayPal for better purchase protection and easier expense tracking.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '2289 Jackson Street', 'address2': 'Apt 116', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '46748'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_gonzalez_8900', 'address1': '2289 Jackson Street', 'address2': 'Apt 116', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '46748'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.lopez3271@example.com',
        instruction='You are assisting Isabella Lopez (email: isabella.lopez3271@example.com) with her pending order for a red Bluetooth speaker with 10-hour battery life and water resistance, currently set to ship to her old address in Phoenix. You want to update the shipping address for this order to 4060 Jackson Street, Apt 68, Oklahoma City, OK, USA 39329, because she has moved. You also want to update her default address to the same Oklahoma City address for future orders. Later, you would like to change the payment method for this pending order from her Mastercard ending in 4336 to her PayPal account, because she prefers using PayPal for better rewards tracking.\n\nUse isabella.lopez3271@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4923227', 'address1': '4060 Jackson Street', 'address2': 'Apt 68', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '39329'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_lopez_6490', 'address1': '4060 Jackson Street', 'address2': 'Apt 68', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '39329'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4923227'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4923227', 'payment_method_id': 'paypal_1621947'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.ito3790@example.com',
        instruction="You are Emma Ito, authenticated with email emma.ito3790@example.com, and you have a pending order for a Water Bottle. You want to update the shipping address for this order to 1712 Lincoln Street, Unit 293, Detroit, MI, USA 56706 because you will be staying there temporarily. After that, you would like to change the payment method from PayPal to your Visa card ending in 3660 for better rewards tracking. You want confirmation of the updated order details after these changes. Later, you decide you no longer need the item, so you would like to cancel the order with the reason 'no longer needed'. Additionally, you would like to know what product types the store offers for future reference.\n\nUse emma.ito3790@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8664580', 'address1': '1712 Lincoln Street', 'address2': 'Unit 293', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '56706'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8664580', 'payment_method_id': 'credit_card_8058445'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8664580'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8664580', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.rossi1299@example.com',
        instruction='You are Amelia Rossi, authenticated with email amelia.rossi1299@example.com, and you have a pending order containing a 17-inch Laptop in space grey and a blue cotton T-Shirt. You want to change the shipping address for this order to 8828 Madison Drive, Suite 67, Philadelphia, PA, USA 37169 because you will be temporarily relocating. You also prefer to switch the payment method from the current gift card to your Visa card ending in 9402 for better purchase protection. Later, you decide to cancel the entire order because your needs changed and you no longer require the items. After that, you would like to review the details of your previous order that included an 8-inch black Tablet with 64GB storage, which was processed and shipped. Finally, you want to browse the product catalog, with a specific interest in the Laptop product line, likely considering a future purchase based on your prior interest in tech devices.\n\nUse amelia.rossi1299@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8255453', 'address1': '8828 Madison Drive', 'address2': 'Suite 67', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '37169'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8255453', 'payment_method_id': 'credit_card_6844118'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8255453', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5100317'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas4271@example.com',
        instruction='You are assisting a customer who wants to update the shipping and payment details for one of his pending orders. You want to change the shipping address to 2090 Madison Drive, Unit 269, Las Vegas, NV, USA 76891 for this order because it needs to be delivered to a new location. You also prefer to switch the payment method to your Visa card ending in 6994 for consistency with your preferred payment method. Later, you would like to cancel another pending order because you no longer need the item, and you want confirmation that the cancellation was processed successfully. After that, you are interested in exploring the product catalog, starting with a full list of available product types to understand what is offered. Subsequently, you would like detailed information about the Digital Camera, particularly models with high resolution and zoom capability, as you are considering a new purchase for photography purposes.\n\nUse liam.thomas4271@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3761872', 'address1': '2090 Madison Drive', 'address2': 'Unit 269', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '76891'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3761872', 'payment_method_id': 'credit_card_7287775'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1129578', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1129578'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8940227892'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.rossi2645@example.com',
        instruction='You are assisting Sofia Rossi (email: sofia.rossi2645@example.com) with a series of requests. First, you want to exchange the delivered bagless canister vacuum cleaner with a HEPA filter for a robotic model that specifically includes pet hair removal features, because she is looking for a more advanced and pet-friendly cleaning solution. You prefer the new model to be of the robotic type with pet hair removal capability, as it better suits her household needs. For any price difference, you prefer to use the Mastercard ending in 3357. Later, you want to update the shipping address for a pending order—currently set to Austin, TX—to 864 Jackson Street, Suite 984, Fort Worth, TX, USA 66889, because she has relocated. At the same time, you would like to change one of the Action Cameras in that order from 5K resolution to 4K resolution, preferring the 4K silver waterproof model, as it meets her recording needs while being more compatible with her editing setup. You also prefer to use the same Mastercard ending in 3357 for any adjustment related to this change. After that, you would like to browse the full list of available product types to explore other items for potential future purchases, showing interest in discovering what else the store offers across categories such as electronics, apparel, home goods, and outdoor gear.\n\nUse sofia.rossi2645@example.com for authentication.',
        actions=[
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8535951', 'item_ids': ['1304426904'], 'new_item_ids': ['4965355367'], 'payment_method_id': 'credit_card_5051208'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5918442', 'address1': '864 Jackson Street', 'address2': 'Suite 984', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '66889'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5918442', 'item_ids': ['1586641416'], 'new_item_ids': ['6117189161'], 'payment_method_id': 'credit_card_5051208'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.santos9317@example.com',
        instruction="You are Isabella Santos (email: isabella.santos9317@example.com). You want to exchange the mechanical keyboard from your delivered order (Fort Worth, TX) because you prefer linear switches and RGB backlighting over the current clicky switches and no backlighting; the replacement should be the 80% size variant with those features. You prefer to use your Mastercard ending in 4971 for any price difference. Later, you want to update the shipping address for your pending order (New York, NY) to 8699 Madison Drive, Apt 840, Detroit, MI, USA 98669; if that is not possible, you would like to cancel the order with the reason 'no longer needed'. After that, you would like to browse the full product catalog to explore available items, and then get detailed information about the product named 'Mechanical Keyboard'.\n\nUse isabella.santos9317@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1654332'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1654332', 'item_ids': ['9665000388'], 'new_item_ids': ['8484921793'], 'payment_method_id': 'credit_card_4056740'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9667707', 'address1': '8699 Madison Drive', 'address2': 'Apt 840', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '98669'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9667707', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1656367028'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.lee9297@example.com',
        instruction='You are Liam Lee, with email liam.lee9297@example.com. You want to update the shipping address for your pending order — which includes a 1.5L glass electric kettle, a green natural rubber yoga mat, and blue wireless in-ear headphones — to 6849 Elm Street, Suite 264, Houston, TX, USA 89339, because you need it delivered there instead. Later, you will cancel this order because you realized it was placed by mistake. Separately, you would like to exchange the 2000-piece animal-themed jigsaw puzzle from your delivered order for the 1000-piece fantasy-themed puzzle, as you prefer a smaller challenge with a fantasy theme over the current one. You prefer to use your Mastercard ending in 3695 for any price adjustment. After that, you would like to browse all product types in the catalog to explore more options, and then view the details of the jigsaw puzzle product to better understand available themes and piece counts.\n\nUse liam.lee9297@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2624389', 'address1': '6849 Elm Street', 'address2': 'Suite 264', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '89339'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2624389', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9710999'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9710999', 'item_ids': ['5645314103'], 'new_item_ids': ['3112842858'], 'payment_method_id': 'credit_card_5809636'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.silva6295@example.com',
        instruction='You are assisting a customer whose email is daiki.silva6295@example.com and who has a pending order for a red Bluetooth speaker with 10-hour battery life and water resistance, originally shipping to San Francisco, CA. You want to update the shipping address to 7103 Cedar Road, Apt 17, Phoenix, AZ, USA 71923, because the customer has relocated and needs the item delivered to their new location. You prefer the change to be applied immediately to ensure correct delivery.\n\nUse daiki.silva6295@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7999678', 'address1': '7103 Cedar Road', 'address2': 'Apt 17', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '71923'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7999678'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.silva6295@example.com',
        instruction='You are Daiki Silva (daiki.silva6295@example.com) and you have a pending order for a red Bluetooth speaker that you want to ensure is shipped correctly. You would like to confirm the current order details and verify that the product is available in the catalog. After that, you want to update the shipping address to your new office location at 5223 Adams Road, Suite 770, San Jose, CA, USA 94555, so the speaker is delivered to your current workplace instead of your previous address in San Francisco.\n\nUse daiki.silva6295@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7999678', 'address1': '5223 Adams Road', 'address2': 'Suite 770', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '94555'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7999678'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.muller6448@example.com',
        instruction='You are assisting Fatima (email: fatima.muller6448@example.com) with her product exploration and order adjustments. You want to first review all available product types, with specific interest in the Gaming Mouse variants. You would like to see the full range of Gaming Mouse options, particularly comparing wireless models with different sensor types and colors. You want to cancel your pending order placed in Chicago because it was made by mistake, which includes a mechanical keyboard with linear switches and a stainless steel 2-liter tea kettle. Later, you would like to exchange the white optical wireless Gaming Mouse received in your delivered order from Washington, DC, for a black laser wireless version to better match your setup, as you prefer the laser sensor and black color for aesthetic and performance reasons. You prefer any price difference to be handled using your PayPal account, which was used for the original purchase.\n\nUse fatima.muller6448@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '5713490933'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9962383', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2435638'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2435638', 'item_ids': ['8896479688'], 'new_item_ids': ['8214883393'], 'payment_method_id': 'paypal_5541158'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.nguyen1293@example.com',
        instruction='You are assisting aarav.nguyen1293@example.com, who wants to explore the Hiking Boots product line. You want to cancel a pending order placed by mistake that includes a pair of Hiking Boots made of synthetic material without waterproofing. Later, you would like to exchange a delivered pair of the same Hiking Boots (synthetic, not waterproof) for an upgraded version made of leather and waterproof, keeping the same size. You prefer the price difference to be handled using your PayPal account, as it was the original payment method used for both orders.\n\nUse aarav.nguyen1293@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2443586', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7728728'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7728728', 'item_ids': ['1437889264'], 'new_item_ids': ['3812493782'], 'payment_method_id': 'paypal_7859314'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen1851@example.com',
        instruction="You are Ava Nguyen (ava.nguyen1851@example.com). You want to cancel your pending order for a women's woody-scented 30ml perfume because you no longer need it. Later, you would like to update your other pending order containing a 50ft black vinyl garden hose and a professional makeup kit for medium skin tone to ship to a new address: 8703 Cedar Road, Apt 513, Oklahoma City, OK, USA 76781, because you are relocating temporarily. After that, you prefer to change the payment method for this order from PayPal to your Visa card ending in 3061 for better rewards and budget tracking. Finally, you would like to explore the available perfume options and pricing to consider a future purchase, particularly interested in variants across scent families, sizes, and gender categories, with current options ranging from $288.75 to $328.25.\n\nUse ava.nguyen1851@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8732376', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8732376'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2601346', 'address1': '8703 Cedar Road', 'address2': 'Apt 513', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '76781'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2601346', 'payment_method_id': 'credit_card_3975380'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6858788497'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are assisting Liam Thomas (email: liam.thomas9081@example.com). You want to cancel a pending order containing an E-Reader and an Air Purifier because he no longer needs the items. Later, you would like to update the shipping address for another pending order—containing a Skateboard, a black 2-piece softshell Luggage Set, and a blue 20000mAh Wireless Portable Charger—to 6139 Park Drive, Floor 735, Phoenix, AZ, USA 26679, and change the payment method to Visa ending in 3194. After that, you are interested in learning more about Action Cameras as potential future purchases.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1654931', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1654931'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3295833', 'address1': '6139 Park Drive', 'address2': 'Floor 735', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '26679'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3295833', 'payment_method_id': 'credit_card_3261838'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.smith2661@example.com',
        instruction='You are assisting Raj Smith (email: raj.smith2661@example.com) with a pending order for a 2L stainless steel white Electric Kettle originally shipping to Washington, DC. You want to first update the shipping address to 7803 Cedar Road, Apt 102, Boston, MA, USA 79961 because it was entered incorrectly. Later, you will request cancellation of the same order because the item is no longer needed. After that, you would like to explore all available product types in the store to understand the full catalog. Subsequently, you want to view the details of the Electric Kettle product, including its various options such as capacity, material, and color, to evaluate it for a potential future purchase.\n\nUse raj.smith2661@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8704143', 'address1': '7803 Cedar Road', 'address2': 'Apt 102', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '79961'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8704143'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8704143', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1075968781'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting a customer with two orders under the email fatima.li1185@example.com. You want to cancel the first order because it contains items you no longer need, specifically a skateboard and an espresso machine currently scheduled for delivery to Washington, DC. Later, you would like to update your second order, which includes a gaming mouse and a laptop, by changing the shipping address to a new location in Phoenix, AZ. After that, you prefer to switch the payment method from your current credit card to your PayPal account for better transaction tracking. Subsequently, you would like to exchange the 13-inch, i5, 16GB laptop in that order for the 15-inch, i9, 32GB, black model because you need more processing power and screen space for your work. You prefer the price difference to be handled using your PayPal account as the payment method.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8005719', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3510092', 'address1': '6170 Elm Street', 'address2': 'Unit 552', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '33135'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3510092', 'payment_method_id': 'paypal_6366157'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3510092', 'item_ids': ['6056040996'], 'new_item_ids': ['2913673670'], 'payment_method_id': 'paypal_6366157'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.moore8091@example.com',
        instruction='You are Mia Moore (mia.moore8091@example.com). You want to exchange the blue Electric Toothbrush with low speed and AA batteries from your delivered order for the black version with high speed and rechargeable battery, because it better suits your daily routine and charging preferences; you prefer any price difference to be handled using your PayPal account. Later, for your pending order, you would like to update the shipping address to 9675 Washington Boulevard, Unit 702, San Antonio, TX, USA 95151, because you will be relocating temporarily. After that, you prefer to change the payment method from gift card to your Mastercard ending in 2992 for better expense tracking. Subsequently, you would like to upgrade the gold Smart Watch with silicone band and LCD display to the gold version with leather band and AMOLED display, because you prefer a more premium look and advanced display; you also want the price difference from this change to be refunded to the same Mastercard.\n\nUse mia.moore8091@example.com for authentication.',
        actions=[
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5544629', 'item_ids': ['1583904702'], 'new_item_ids': ['8098621301'], 'payment_method_id': 'paypal_5181300'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3130288', 'address1': '9675 Washington Boulevard', 'address2': 'Unit 702', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '95151'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3130288', 'payment_method_id': 'credit_card_2641784'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3130288', 'item_ids': ['2540052208'], 'new_item_ids': ['5694328282'], 'payment_method_id': 'credit_card_2641784'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.brown3965@example.com',
        instruction="You are assisting Harper Brown (email: harper.brown3965@example.com) with modifying his pending order originally shipped to Fort Worth, TX. You want to exchange the non-waterproof leather Hiking Boots in size 10 for the available waterproof synthetic version in the same size, because he needs waterproof footwear for an upcoming trip. You prefer the price difference to be charged to your Visa card ending in 3356. Later, you would like the updated order to be shipped to a new address: 250 Cedar Road, Apt 689, Austin, TX, USA 19478, instead of the original Fort Worth address. After that, you want to browse the full product catalog to explore other offerings, particularly confirming the availability of items like Smart Watches, Tea Kettles, Perfume, and Electric Toothbrushes. You also want detailed information about the Hiking Boots product to verify features and options. If any of these changes cannot be completed, you would like to cancel the entire order with the reason 'ordered by mistake'.\n\nUse harper.brown3965@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2273069'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2273069', 'item_ids': ['2185126308'], 'new_item_ids': ['1615379700'], 'payment_method_id': 'credit_card_3240550'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2273069', 'address1': '250 Cedar Road', 'address2': 'Apt 689', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '19478'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2273069', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.gonzalez1317@example.com',
        instruction='You are assisting a customer who wants to update two details on their pending order containing a skateboard, notebook, and 2-piece silver luggage set. You want to change the shipping address from Fort Worth to 7884 Jackson Street, Floor 850, San Antonio, TX, USA 87994 because it is their updated location. You also want to update the payment method from the Visa ending in 4920 to the Mastercard ending in 9364, as they prefer to use that card for this purchase. These updates should be applied before the order ships.\n\nUse isabella.gonzalez1317@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1258841', 'address1': '7884 Jackson Street', 'address2': 'Floor 850', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '87994'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1258841', 'payment_method_id': 'credit_card_9878778'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.jackson2679@example.com',
        instruction='You are assisting Mia Jackson (email: mia.jackson2679@example.com). You want to update the shipping address for her pending order containing a Gaming Mouse and Hiking Boots from Philadelphia to 8997 Maple Lane, Floor 675, Seattle, WA, USA 12879, because she has relocated temporarily for work. Later, you would like to learn more about the Action Camera product, particularly its waterproof models in 4K resolution, as she is considering it for outdoor adventures. After that, you would like to see all product types available in the store to explore other potential purchases, including electronics, outdoor gear, and home essentials.\n\nUse mia.jackson2679@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1298962', 'address1': '8997 Maple Lane', 'address2': 'Floor 675', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '12879'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1298962'}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.johansson1233@example.com',
        instruction='You are assisting Isabella Johansson (isabella.johansson1233@example.com), whose pending order includes an espresso machine, a professional-sized makeup kit for medium skin tone, a large brown polyester pet bed, and blue wireless earbuds with 4-hour battery life. You want to update the shipping address for this order to 4581 Main Street, Floor 631, Houston, TX, USA 30306 because it is more convenient for delivery. Later, you would like to explore the full range of product types available in the store to discover new items of interest.\n\nUse isabella.johansson1233@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6783532', 'address1': '4581 Main Street', 'address2': 'Floor 631', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '30306'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.santos9317@example.com',
        instruction='You are assisting Isabella Santos (email: isabella.santos9317@example.com). You are first interested in learning about the available Running Shoes, particularly noting options in size 9 with mesh or synthetic materials and rubber soles for lightweight comfort and durability. Later, you want to update the shipping address for your pending order — which includes a gold Smart Watch with a leather band and a pair of size 7 synthetic hiking boots — to 6251 Park Drive, Unit 698, Las Vegas, NV, USA 12460, because you will be traveling there. You also want your default address on file updated to the same, for consistency across future orders. After that, you decide to cancel the same order because you no longer need the items, and you prefer no further fulfillment or shipment to proceed.\n\nUse isabella.santos9317@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6938111410'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9527030', 'address1': '6251 Park Drive', 'address2': 'Unit 698', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '12460'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_santos_1643', 'address1': '6251 Park Drive', 'address2': 'Unit 698', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '12460'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9527030'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9527030', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.martin4832@example.com',
        instruction='You are Sophia Martin (sophia.martin4832@example.com) and you are exploring the product catalog, particularly interested in learning about Laptops because you are considering a tech upgrade. You want to update the shipping address for your pending order—which includes a 7-inch gold tablet, a red large mountain bicycle, a portable electric grill, blue wired over-ear headphones, and a small brown fleece pet bed—to 189 Elm Street, Apt 878, San Diego, CA, USA 44124, so it can be delivered closer to your current location. You also want your default address updated to the same San Diego address for future orders, to ensure convenience and consistency. Later, you change your mind and decide to cancel the entire order because the items no longer align with your current needs, especially since you were primarily interested in a Laptop and the tablet included does not meet your requirements. You prefer the refund to be processed back to your Mastercard ending in 3292, which was used for the original purchase.\n\nUse sophia.martin4832@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1603792', 'address1': '189 Elm Street', 'address2': 'Apt 878', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '44124'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sophia_martin_8570', 'address1': '189 Elm Street', 'address2': 'Apt 878', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '44124'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1603792', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.jackson5798@example.com',
        instruction='You are Mia Jackson, and your email is mia.jackson5798@example.com. You want to update the shipping address for your pending order containing a black desk lamp, an espresso machine with 15 bar pressure and 1L capacity, and a 2L black glass electric kettle to 5479 Maple Lane, Unit 772, Houston, TX, USA 98431 because you are temporarily relocating. Later, you would like to cancel your other pending order that includes a green leather camera backpack, a ceramic tea kettle with 1.5-liter capacity, a small black cycling helmet, and blue wireless earbuds with 6-hour battery life, because you no longer need those items. You prefer the refund for the canceled order to be returned to the original payment method, which was PayPal.\n\nUse mia.jackson5798@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7807323'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7807323', 'address1': '5479 Maple Lane', 'address2': 'Unit 772', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '98431'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1205816', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.lopez8943@example.com',
        instruction="You are assisting a customer who placed a pending order for a dumbbell set, espresso machine, coffee maker, and pet bed, originally shipped to Columbus, OH. You want to update the shipping address to 4587 Elm Street, Apt 205, Boston, MA, to better suit the customer's current location. Later, you will proceed to cancel the entire order as the customer no longer needs the items. You prefer the refund to be processed back to the original gift card used for purchase.\n\nUse ethan.lopez8943@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6779827'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6779827', 'address1': '4587 Elm Street', 'address2': 'Apt 205', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '89089'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6779827', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are assisting a customer with two pending orders under the email lei.li8350@example.com. First, you want to cancel the pending laptop order because the customer no longer needs it; the order includes a space grey 17-inch laptop with i5 processor, 8GB RAM, and 1TB SSD storage. Later, you will update the shipping address for another pending order containing a 30MP digital camera, a 1L stainless steel black electric kettle, and a 14-inch black digital wall clock to 6133 Lincoln Street, Apt 203, Fort Worth, TX, USA 50085, as the items are now needed at the new location. You prefer the original payment method—PayPal—for any refund from the cancellation, and you confirm both actions are intentional.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3414433', 'address1': '6133 Lincoln Street', 'address2': 'Apt 203', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '50085'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.ahmed2006@example.com',
        instruction='You are assisting a customer with email evelyn.ahmed2006@example.com who would like to first browse the product catalog. After that, you want to update the shipping address for their pending order—currently going to Charlotte, NC—for a set of items including hiking boots, a desk lamp, a water bottle, a bookshelf, and a jigsaw puzzle, to 7761 Cedar Road, Apt 124, Houston, TX, USA 87846, because they have relocated. Later, you would like to update their default shipping address to the same Houston address so that all future orders are sent there.\n\nUse evelyn.ahmed2006@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1416704', 'address1': '7761 Cedar Road', 'address2': 'Apt 124', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '87846'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_ahmed_3960', 'address1': '7761 Cedar Road', 'address2': 'Apt 124', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '87846'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.lopez2966@example.com',
        instruction='You are Mason Lopez, and your email is mason.lopez2966@example.com. You want to cancel your pending order placed by mistake, which includes a black Smart Watch with silicone band, a black electric toothbrush, a professional-sized makeup kit for medium skin tone, a blue 6 ft sunbrella patio umbrella with auto tilt, and polarized black sunglasses with brown lenses. Later, for your delivered order containing two water bottles, you would like to return the 500ml black glass water bottle because it does not meet your durability preference. You also want to exchange the 750ml black plastic water bottle for a 500ml black stainless steel version because you prefer a more durable and lightweight option. You prefer any refund or price difference to be processed back to your PayPal account.\n\nUse mason.lopez2966@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9222585', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8185761'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8185761', 'item_ids': ['8538875209'], 'payment_method_id': 'paypal_9591556'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8185761', 'item_ids': ['7199146548'], 'new_item_ids': ['3453331371'], 'payment_method_id': 'paypal_9591556'}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.wilson6954@example.com',
        instruction='You are Mason Wilson, a customer with email mason.wilson6954@example.com, who wants to return the Digital Camera from your delivered order because it is no longer needed, and you prefer the refund to be issued back to your gift card since that was the original payment method. Later, you want to update the shipping address for your pending order—which includes a Tea Kettle, Bluetooth Speaker, Hiking Boots, and Action Camera—from Phoenix to your new location in Detroit, and you also want your default profile address updated to 9430 Pine Avenue, Floor 418, Detroit, MI, USA 77244 to ensure future orders are delivered correctly. After that, you would like to explore available products and learn more about the Laptop to evaluate it for a potential future purchase, as you are considering upgrading your current device.\n\nUse mason.wilson6954@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8161562'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8161562', 'item_ids': ['7195021808'], 'payment_method_id': 'gift_card_6767859'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4318885', 'address1': '9430 Pine Avenue', 'address2': 'Floor 418', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '77244'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mason_wilson_4597', 'address1': '9430 Pine Avenue', 'address2': 'Floor 418', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '77244'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.khan2360@example.com',
        instruction='You are Olivia Khan, and your email is olivia.khan2360@example.com. You want to update the shipping address for your pending order—containing a red cotton crew neck T-shirt in size S, polarized brown-lens black plastic sunglasses, a large brown memory foam pet bed, and a blue-dial metal-strap wristwatch—to 7747 Park Drive, Suite 232, Las Vegas, NV, USA 85281, because it was initially sent to the wrong location. After that, you would like to cancel the entire order, as you no longer need the items. You prefer the refund to be processed back to the original payment method, which was PayPal.\n\nUse olivia.khan2360@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3840181', 'address1': '7747 Park Drive', 'address2': 'Suite 232', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '85281'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3840181'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3840181', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.sanchez1292@example.com',
        instruction="You are a customer with email aarav.sanchez1292@example.com who placed a pending order for a skateboard, jigsaw puzzle, grill, headphones, and mechanical keyboard to be shipped to Houston. You want to change the shipping address for this pending order to 943 Maple Drive, Suite 356, Chicago, IL, USA 60621, and update your default address to the same for future orders. Later, you would like to cancel this order with the reason 'ordered by mistake' as you no longer need the items. Separately, you received a navy XL Fleece Jacket with full zipper in a delivered order and would like to exchange it for the black L size with full zipper because it better fits your preference. You prefer to use your Mastercard ending in 5506 for any price difference in the exchange.\n\nUse aarav.sanchez1292@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6348442', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='modify_user_address', kwargs={'user_id': 'aarav_sanchez_9729', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6348442', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4304974'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W4304974', 'item_ids': ['7528037711'], 'new_item_ids': ['9385662952'], 'payment_method_id': 'credit_card_2690859'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com), who is exploring the product catalog and has shown interest in the Backpack. You want to cancel the pending order containing the Hiking Boots, Laptop, and Air Purifier because it was placed by mistake. Later, you would like to update the shipping address for the pending order containing the grey medium polyester Backpack with a laptop compartment to 5424 Lincoln Street, Suite 411, New York, NY, USA 98918. After that, you prefer to update the default address on file to match this new New York address for future orders. You prefer the refund from the canceled order to be returned to the original gift card used for payment.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6885344', 'address1': '5424 Lincoln Street', 'address2': 'Suite 411', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '98918'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_garcia_3055', 'address1': '5424 Lincoln Street', 'address2': 'Suite 411', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '98918'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are Omar Silva (email: omar.silva4147@example.com) with a pending order currently shipping to San Diego. You want to update the shipping address to 5574 Jackson Street, Apt 958, Philadelphia, PA, USA 86934, because you will be relocating. You also prefer to change the payment method from the original gift card to your PayPal account for better transaction tracking. Later, you would like to exchange the non-waterproof 4K silver Action Camera for the 4K waterproof silver model, as you plan to use it in wet conditions and need the waterproof feature. For this exchange, you prefer the refund to be processed to your Mastercard ending in 5859. After that, you would like to cancel the entire order altogether, as you have changed your mind and no longer need the items.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9728773', 'address1': '5574 Jackson Street', 'address2': 'Apt 958', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '86934'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9728773', 'payment_method_id': 'paypal_2192303'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9728773', 'item_ids': ['9391733462'], 'new_item_ids': ['6117189161'], 'payment_method_id': 'credit_card_5322562'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.lopez3271@example.com',
        instruction='You are assisting Isabella Lopez (email: isabella.lopez3271@example.com), who has a pending order for a red Bluetooth speaker. You want to update the shipping address from Phoenix to 7576 Adams Road, Unit 536, Detroit, MI, USA 47899, so the item can be delivered to the correct location. After that, you would like to change the payment method from the Mastercard ending in 4336 to her PayPal account for better payment tracking and personal preference. Later, you intend to cancel the entire order because it was placed by mistake and is no longer needed. After cancellation, you want to verify the order status to confirm it has been successfully cancelled and no further action or charge occurs.\n\nUse isabella.lopez3271@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4923227', 'address1': '7576 Adams Road', 'address2': 'Unit 536', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '47899'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4923227', 'payment_method_id': 'paypal_1621947'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4923227', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4923227'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen1851@example.com',
        instruction="You are assisting Ava Nguyen (email: ava.nguyen1851@example.com) with her pending order for a women's woody-scented perfume (30ml). You want to update the shipping address from Charlotte, NC to 6505 Maple Lane, Apt 924, Chicago, IL, USA 43671 because it was entered incorrectly. After that, you would like to change the payment method from PayPal to her Visa card ending in 3061 for greater convenience. Later, you will decide to cancel the entire order because the item is no longer needed. After all changes, you want confirmation that the address and payment updates were processed before the cancellation, and that the final order status reflects the cancellation.\n\nUse ava.nguyen1851@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8732376', 'address1': '6505 Maple Lane', 'address2': 'Apt 924', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '43671'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8732376', 'payment_method_id': 'credit_card_3975380'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8732376', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8732376'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.khan6479@example.com',
        instruction='You are assisting Ivan Khan (email: ivan.khan6479@example.com) with his pending order originally shipped to Washington, DC, which includes a navy small nylon laptop backpack, an indoor security camera, and a silver battery-powered desk lamp. You want to first update the shipping address to 8349 Maple Lane, Floor 420, Denver, CO, USA 26985, so the package reaches his new location. Then, you would like to exchange the current backpack for a black large nylon camera backpack because it better suits his travel needs with dedicated camera storage and more space. You prefer the refund for the price difference to be processed to his PayPal account. Later, after reconsidering, you want to cancel the entire order as he has changed his mind about the purchase. After that, you would like to browse the full catalog of product types to review available backpack options and better understand the range before making future selections.\n\nUse ivan.khan6479@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5270061', 'address1': '8349 Maple Lane', 'address2': 'Floor 420', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '26985'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5270061'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5270061', 'item_ids': ['2492465580'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'paypal_7729105'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5270061', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.silva2239@example.com',
        instruction='You are Daiki Silva, and your contact email is daiki.silva2239@example.com. You want to return the green Bluetooth Speaker with 20-hour battery life and water resistance from your delivered order, as it is no longer needed, and you prefer the refund to be issued back to your PayPal account for convenience. Later, you will update the shipping address for your pending order—which includes a glass tea kettle, a stainless steel water bottle, a bagless upright vacuum with HEPA filter, wired in-ear headphones, and a 1.5L glass electric kettle—to ensure it reaches the correct location. After reviewing the delivery plan, you would like the new address to be 7084 Washington Boulevard, Suite 692, Boston, MA, USA 70779, so the package can be received at your updated residence.\n\nUse daiki.silva2239@example.com for authentication.',
        actions=[
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6564160', 'item_ids': ['2652637226'], 'payment_method_id': 'paypal_2233507'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1579160', 'address1': '7084 Washington Boulevard', 'address2': 'Suite 692', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '70779'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are Omar Silva, with email omar.silva4147@example.com, and you have a pending order containing an Action Camera with 4K resolution in silver color that is not waterproof. You want to update the shipping address to 6713 Maple Lane, Suite 385, Dallas, TX, USA 75794, because you need it delivered to a different location. You also prefer to switch the payment method from the current gift card to your Mastercard ending in 5859 for better expense tracking. Later, after reviewing the order, you realize the Action Camera was ordered by mistake, so you would like to cancel the entire order to prevent any further processing or charges.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9728773', 'address1': '6713 Maple Lane', 'address2': 'Suite 385', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '75794'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9728773', 'payment_method_id': 'credit_card_5322562'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.khan2360@example.com',
        instruction='You are Olivia Khan (email: olivia.khan2360@example.com) and you want to first review your pending order containing a red cotton crew neck T-Shirt, black polarized sunglasses, a large brown memory foam pet bed, and a blue metal-strap wristwatch, originally shipped to Indianapolis. You would like to update the shipping address to 7845 Elm Street, Suite 390, Dallas, TX, USA 85711, and change the payment method from PayPal to your Mastercard ending in 2184 for this order. Later, you decided to cancel the entire order because it was placed by mistake. After cancellation, you would like to browse the full list of available product types in the store to explore future purchase options, including categories such as T-Shirts, Sunglasses, Pet Beds, Wristwatches, Backpacks, Smartwatches, Laptops, and more.\n\nUse olivia.khan2360@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3840181'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3840181', 'address1': '7845 Elm Street', 'address2': 'Suite 390', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '85711'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3840181', 'payment_method_id': 'credit_card_7376788'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3840181', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are assisting Lei Li (email: lei.li8350@example.com) who initially wanted to check the status of her pending order containing a 17-inch space grey laptop and also explore the backpack product line, particularly models with camera or laptop compartments in various colors and materials. You want to first confirm the order is still pending and review backpack options available in sizes and colors such as black large, green small, or grey medium. Later, you would like to update the shipping address for this order to 6964 Pine Avenue, Floor 982, Las Vegas, NV, USA 26381, because she has relocated temporarily. After that, you prefer to change the payment method from PayPal to her Visa card ending in 2697 for better rewards tracking. However, subsequently, you decide the laptop is no longer needed and would like to cancel the entire order. After cancellation, you would like to browse the full range of product types currently offered in the store, including categories like Backpack, Laptop, Smart Watch, Coffee Maker, and others, to explore future purchase options.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '6964 Pine Avenue', 'address2': 'Floor 982', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '26381'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5166363', 'payment_method_id': 'credit_card_4466831'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.muller6278@example.com',
        instruction='You are daiki.muller6278@example.com. You want to check the status of your delivered order containing Hiking Boots in size 11, made of synthetic material with waterproofing, along with an Espresso Machine and a Skateboard, which was shipped to San Francisco. You also want product details for the Hiking Boots, confirming they are designed for outdoor use with durable synthetic construction. Later, you would like to change the shipping address for your pending order—which includes a 1L stainless steel electric kettle and a small beige fleece pet bed—to 943 Maple Drive, Suite 356, Chicago, IL, USA 60621, because you are relocating temporarily. After that, you want to update your default address to the same Chicago address for future orders. Subsequently, you would like to return the Hiking Boots from the delivered order because they do not fit as expected, and you prefer a refund back to your gift card for the original purchase amount.\n\nUse daiki.muller6278@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5961635'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7822344', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='modify_user_address', kwargs={'user_id': 'daiki_muller_8062', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5961635', 'item_ids': ['6546364613'], 'payment_method_id': 'gift_card_8385925'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen.lopez1681@example.com',
        instruction='You are assisting Chen Lopez (email: chen.lopez1681@example.com). You want to review the details of a delivered order that includes a 500-piece expert-level jigsaw puzzle with an animals theme, along with a blue medium cycling helmet and a large black nylon backpack with a camera compartment, all shipped to Seattle. Later, you would like to update the shipping address for a pending order containing a full-size tactile mechanical keyboard with white backlighting to 5875 Park Drive, Suite 430, Dallas, TX, USA 79491, and also update the default address to this new Dallas location. After that, you would like to return all items from the delivered order — the jigsaw puzzle, cycling helmet, and backpack — and prefer the refund to be issued back to your PayPal account.\n\nUse chen.lopez1681@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9360566'}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1790752', 'address1': '5875 Park Drive', 'address2': 'Suite 430', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '79491'}),
            Action(name='modify_user_address', kwargs={'user_id': 'chen_lopez_3345', 'address1': '5875 Park Drive', 'address2': 'Suite 430', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '79491'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9360566', 'item_ids': ['9237024510', '3339188619', '3928046918'], 'payment_method_id': 'paypal_2833385'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.rossi7301@example.com',
        instruction='You are assisting Yusuf Rossi (email: yusuf.rossi7301@example.com) with a pending order modification and product exploration. You want to update the shipping address for the pending order containing a black XXL cotton crew neck T-Shirt to 5351 Pine Avenue, Suite 506, Los Angeles, CA, USA 33812, because he is relocating and needs the package delivered to his new residence. Later, you would like to exchange the black XXL cotton crew neck T-Shirt for the purple XL cotton crew neck T-Shirt, as he prefers a smaller size and a different color that better suits his style. You prefer any payment adjustment to be processed using the Mastercard ending in 2478, as it was the original payment method. After completing these changes, you would like to review all available product types in the catalog to explore future purchase options, and specifically examine the T-Shirt product variants to understand available sizes, colors, and materials for upcoming selections.\n\nUse yusuf.rossi7301@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6247578', 'address1': '5351 Pine Avenue', 'address2': 'Suite 506', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '33812'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6247578'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6247578', 'item_ids': ['3799046073'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'credit_card_9513926'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction="You are assisting Lei Li (email: lei.li8350@example.com) with two pending orders. First, you want to update the shipping address for the pending order containing a 17-inch space grey Laptop to 4778 Adams Road, Apt 171, Los Angeles, CA, USA 33593, because the original address in San Francisco is no longer valid. Later, for another pending order that includes a Digital Camera with 3x zoom and SD card, you would like to exchange it for the same model but with 5x zoom and CF card, as it better suits the user's photography needs. You prefer to use the Visa card ending in 2697 for any price difference associated with the exchange. After that, you want to explore the full range of product types offered, to understand what other items are available. Subsequently, you would like to review the available configurations for the Laptop product, including screen size, processor, RAM, storage, and color options, to assess potential future purchases.\n\nUse lei.li8350@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '4778 Adams Road', 'address2': 'Apt 171', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '33593'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3414433', 'item_ids': ['1804581713'], 'new_item_ids': ['6384525445'], 'payment_method_id': 'credit_card_4466831'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are James Martin, with email james.martin9857@example.com, who wants to update the shipping address for a pending order containing a red XXL cotton crew neck T-Shirt, a Smart Thermostat, a Wristwatch, a Garden Hose, and a Backpack to a new location in New York. You want the shipping address updated to 1209 Oak Avenue, Suite 426, New York, NY, USA 58440 because it was originally set to your old address in San Diego. You also want your default address updated to the same New York address for future orders. After that, you would like to browse available T-Shirt options, particularly interested in variations by color, size, material, and style, so you can consider a future purchase based on current inventory with options like blue, purple, or black, in cotton or polyester, and in crew or v-neck styles.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '1209 Oak Avenue', 'address2': 'Suite 426', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '58440'}),
            Action(name='modify_user_address', kwargs={'user_id': 'james_martin_1500', 'address1': '1209 Oak Avenue', 'address2': 'Suite 426', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '58440'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.hernandez3060@example.com',
        instruction='You are assisting Evelyn Hernandez (email: evelyn.hernandez3060@example.com). You want to update the shipping address for her pending order (currently to San Diego, CA) to 5350 Pine Avenue, Suite 449, Nashville, TN, USA, 63532 because she has relocated. After that, you would like to change the grill in that order from the medium electric model with side burner to the large electric model with rotisserie, as it better suits her cooking needs. You prefer to use her Visa card ending in 4171 for any price difference. Later, you will request to cancel her other pending order (containing an 8GB e-reader with cellular, a professional light-skin-tone makeup kit, and a black high-brightness desk lamp) because she no longer needs those items.\n\nUse evelyn.hernandez3060@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3482034', 'address1': '5350 Pine Avenue', 'address2': 'Suite 449', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '63532'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3482034'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3482034', 'item_ids': ['5666020311'], 'new_item_ids': ['4404981319'], 'payment_method_id': 'credit_card_3631888'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4895606', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li5953@example.com',
        instruction='You are assisting Sofia Li (sofia.li5953@example.com) with updating the shipping address for her pending order containing wireless earbuds, two electric kettles (one 1.5L silver glass, one 1L black glass), a soft cover A6 notebook, and a pink natural rubber 6mm yoga mat). You want to change the delivery address from Philadelphia to 4382 Jackson Street, Suite 151, San Jose, CA, USA 42202 because the original location is no longer valid. You prefer the order to be shipped to the new San Jose address for timely receipt.\n\nUse sofia.li5953@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1557241', 'address1': '4382 Jackson Street', 'address2': 'Suite 151', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '42202'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are Yusuf Garcia, with email yusuf.garcia2909@example.com, and you want to cancel your pending order containing Hiking Boots, a Laptop, and an Air Purifier because you no longer need these items. Later, you would like to update the shipping address for your other pending order—which includes a grey medium polyester backpack with a laptop compartment—to 1599 Oak Avenue, Floor 571, Fort Worth, TX, USA 23658, and you prefer to switch the payment method from PayPal to your Mastercard ending in 3762 for this order. After that, you want to browse the available product types in the store, particularly focusing on the Laptop product line, and you are interested in learning more about the available configurations—such as screen size, processor, RAM, storage, and color options—to consider a future purchase.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6885344', 'address1': '1599 Oak Avenue', 'address2': 'Floor 571', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '23658'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6885344', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.wilson5728@example.com',
        instruction='You are assisting Mei Wilson (mei.wilson5728@example.com), who placed a pending order for several items including a portable electric grill with rotisserie, a makeup kit, a bamboo skateboard, wireless earbuds, and a smartphone, all shipped to New York. You want to cancel this entire order because it was placed by mistake, and you confirm proceeding with cancellation. The order was paid using a gift card, so you prefer the refund to be issued back to the original gift card. Later, you would like to learn more about the Grill product that was in the order, particularly its features and available options, to better understand what was selected and possibly consider it for a future purchase.\n\nUse mei.wilson5728@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W4498118'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4498118', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6819683148'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.gonzalez1317@example.com',
        instruction='You are assisting Isabella Gonzalez (isabella.gonzalez1317@example.com) with her pending order. You want to first update the shipping address to 7674 Maple Lane, Apt 331, New York, NY, USA 65317 because the original address in Fort Worth, TX was incorrect. Then, you would like to change the payment method to the Visa card ending in 9364 for better expense tracking. After completing these updates, you intend to cancel the entire order because it was placed by mistake. Later, you want to review the order status to confirm cancellation and also look up details of the skateboard that was part of the order—a 28-inch maple deck with a plain design—to understand the product attributes before potentially reordering in the future.\n\nUse isabella.gonzalez1317@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1258841', 'address1': '7674 Maple Lane', 'address2': 'Apt 331', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '65317'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1258841', 'payment_method_id': 'credit_card_9878778'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1258841', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1258841'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.hernandez7166@example.com',
        instruction='You are assisting Yara Hernandez (yara.hernandez7166@example.com) with modifying her delivered order from Jacksonville. You want to exchange the black Smart Watch with silicone band for the gold Smart Watch with leather band and AMOLED display, as you prefer the more elegant look and feel of the gold leather version over the sporty black silicone one. For this exchange, you prefer to use your Visa card ending in 1947 for payment handling. Later, you would like to return the silver Action Camera from the same order, as it does not meet your current needs, and you prefer the refund to be issued back to the original gift card used at purchase.\n\nUse yara.hernandez7166@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2156941'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2156941', 'item_ids': ['4920090458'], 'new_item_ids': ['5694328282'], 'payment_method_id': 'credit_card_5528301'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2156941', 'item_ids': ['1586641416'], 'payment_method_id': 'gift_card_3985012'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.brown9344@example.com',
        instruction='You are assisting Lucas Brown (email: lucas.brown9344@example.com) with modifying his delivered order. You want to exchange the 1000ml stainless steel blue water bottle for the same size and material in red, because he prefers the red color. Later, you also want to return the original blue water bottle after the exchange is processed. You prefer the refund for any price difference to be issued back to the Mastercard ending in 1276, as that was the original payment method.\n\nUse lucas.brown9344@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6239298'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6239298', 'item_ids': ['2366567022'], 'new_item_ids': ['2439754078'], 'payment_method_id': 'credit_card_2112420'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6239298', 'item_ids': ['2366567022'], 'payment_method_id': 'credit_card_2112420'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.li2787@example.com',
        instruction='You are assisting Raj (email: raj.li2787@example.com) with updates to his pending order containing a brown glass 4 ft bookshelf, a green stainless steel 750ml water bottle, a large gas grill with rotisserie, and a black glass 5 ft bookshelf, currently shipping to Fort Worth, TX. You want to update the shipping address to 1411 Cedar Road, Floor 473, San Jose, CA, USA 74584, because he needs the delivery redirected. You also want to change the payment method from the credit card ending in 3917 to his PayPal account, as he prefers to use PayPal for this transaction. Additionally, you would like to modify one of the bookshelves from the brown glass 4 ft version to the white glass 5 ft version, because he prefers the lighter color and extra height for his space. You prefer any refund or charge associated with the item change to be processed to the PayPal account.\n\nUse raj.li2787@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8967935', 'address1': '1411 Cedar Road', 'address2': 'Floor 473', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '74584'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8967935', 'payment_method_id': 'paypal_2028062'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8967935', 'item_ids': ['8649999816'], 'new_item_ids': ['8895454203'], 'payment_method_id': 'paypal_2028062'}),
            Action(name='get_product_details', kwargs={'product_id': '8600330539'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.thomas1454@example.com',
        instruction='You are assisting Harper Thomas (harper.thomas1454@example.com) with a pending order originally shipped to Houston. You want to update the shipping address to 9814 Lincoln Street, Unit 999, Detroit, MI, USA 20668, because the customer has relocated. You prefer to change the payment method to the Mastercard ending in 7287 for both the original payment and any price adjustments, as it is their preferred card. You would like to modify the Yoga Mat from green, 6mm to the blue, 4mm version because you prefer a thinner and more vibrant mat for travel. Later, you want to update the Smart Thermostat from black to the stainless steel finish to better match your kitchen appliances. You prefer the changes to be applied using the same Mastercard for any balance due.\n\nUse harper.thomas1454@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7425646', 'address1': '9814 Lincoln Street', 'address2': 'Unit 999', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '20668'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7425646', 'payment_method_id': 'credit_card_1199336'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7425646', 'item_ids': ['7510236436', '4983901480'], 'new_item_ids': ['5586947715', '9480266227'], 'payment_method_id': 'credit_card_1199336'}),
            Action(name='get_product_details', kwargs={'product_id': '4896585277'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.sanchez7626@example.com',
        instruction='You are Anya Sanchez, with email anya.sanchez7626@example.com, and you initially wanted to update the shipping address for your pending order containing a white plastic 1.5L Electric Kettle to 7342 Elm Street, Suite 213, Austin, TX, USA 37932, because it was mistakenly set to an old address in Fort Worth. Later, you decided to cancel the order entirely because you no longer needed the Electric Kettle. After the cancellation, you expressed interest in learning more about the Backpack, particularly its available colors, sizes, materials, and compartment types, to explore suitable options for potential purchase.\n\nUse anya.sanchez7626@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5402785', 'address1': '7342 Elm Street', 'address2': 'Suite 213', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '37932'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5402785'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5402785', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting Sophia Patel, whose email is sophia.patel9841@example.com. You want to first update the shipping address for her pending order—which includes a men's oriental perfume (100ml), a glass tea kettle (1.5L), a black glass electric kettle (1L), and gray canvas sneakers (size 8)—from Fort Worth, TX to 2390 Pine Avenue, Apt 391, Nashville, TN 53212, because she has relocated temporarily. You also want to change the payment method from her Visa ending in 8025 to her Mastercard ending in 1639, as she prefers to use that card for larger purchases. Later, you will request to cancel the entire order because she no longer needs the items, even after the updates. After that, you would like to explore the product catalog, specifically to review the available Laptop options, which come in various configurations including 13-inch, 15-inch, and 17-inch screen sizes, with different processors, RAM, storage, and colors, to evaluate potential future purchases.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7905419', 'address1': '2390 Pine Avenue', 'address2': 'Apt 391', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '53212'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7905419', 'payment_method_id': 'credit_card_6419343'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7905419', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.santos7683@example.com',
        instruction='You are Emma Santos (emma.santos7683@example.com). You want to update the shipping address for your pending order, which includes a blue leather office chair, a skateboard, two water bottles, and a laptop, to a new address in Nashville because you have relocated. Later, you would like to exchange the red mesh office chair from your delivered order for a black fabric high-back chair because you prefer a more supportive and darker-colored design. After that, you would like to cancel the pending order entirely because you no longer need the items due to changes in your workspace setup.\n\nUse emma.santos7683@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9903153', 'address1': '7391 Adams Road', 'address2': 'Suite 667', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '68328'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3113816', 'item_ids': ['4274709903'], 'new_item_ids': ['1793929609'], 'payment_method_id': 'credit_card_5869505'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9903153', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.thomas1454@example.com',
        instruction='You are assisting Harper Thomas (harper.thomas1454@example.com) with his pending order. You want to first update the payment method for the order to your Mastercard ending in 7287, because you prefer using that card for this purchase. You also want to change the shipping address to 4346 Park Drive, Apt 223, Portland, OR, USA 44276, as it is your current location. Later, after reviewing the product catalog and learning about the Backpack options—particularly those with laptop or camera compartments, in small or large sizes, made of nylon or polyester—you decide the original order no longer meets your needs. After that, you would like to cancel the entire order #W7425646 because you no longer require the Yoga Mat or Smart Thermostat that were included. You prefer the refund to be processed back to the original payment method unless otherwise specified.\n\nUse harper.thomas1454@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7425646'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7425646', 'payment_method_id': 'credit_card_1199336'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7425646', 'address1': '4346 Park Drive', 'address2': 'Apt 223', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '44276'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7425646', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.lopez2966@example.com',
        instruction='You are assisting a customer with email mason.lopez2966@example.com who has a pending order for a black Smart Watch with AMOLED display, a black Electric Toothbrush with high speed settings, a professional-sized Makeup Kit for medium skin tone, a 6 ft blue Patio Umbrella with auto tilt, and polarized Sunglasses with black frame and brown lenses. You want to update the shipping address for this order to 9192 Cedar Road, Floor 418, Phoenix, AZ, USA 54769, because the original address was incorrect. Later, you would like to cancel this order entirely because it was placed by mistake. You prefer the refund to be processed back to the original payment method, PayPal.\n\nUse mason.lopez2966@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9222585', 'address1': '9192 Cedar Road', 'address2': 'Floor 418', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '54769'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9222585', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9222585'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8185761', 'item_ids': ['7199146548'], 'payment_method_id': 'paypal_9591556'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8185761', 'item_ids': ['8538875209'], 'new_item_ids': ['4579334072'], 'payment_method_id': 'paypal_9591556'}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.santos8320@example.com',
        instruction='You are a customer with email aarav.santos8320@example.com who placed a pending order containing a silver 13-inch i5 laptop, a black 17-inch i7 laptop, a manual 15 bar espresso machine, a cordless bagged canister vacuum cleaner, and a black smart thermostat compatible with Google Assistant. You want to first update the shipping address for this pending order to 2052 Main Street, Apt 704, Columbus, OH, USA 44584, because it was sent to the wrong location. Later, you will cancel the entire order because it was placed by mistake. After that, you would like to review your delivered order that included two blue Bluetooth speakers, one with water resistance and one without, along with a daylight LED bulb and a 50ft black latex garden hose. For this delivered order, you want to return the blue Bluetooth speaker with water resistance (10-hour battery) because it does not meet your needs, and you prefer to exchange the other blue Bluetooth speaker (without water resistance, 10-hour battery) for a green one with 20-hour battery life because you want longer playback time. You prefer all financial transactions, including refunds and any price adjustments for the exchange, to be processed back to your PayPal account.\n\nUse aarav.santos8320@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9672333', 'address1': '2052 Main Street', 'address2': 'Apt 704', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '44584'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9672333', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8528674'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8528674', 'item_ids': ['4716977452'], 'payment_method_id': 'paypal_7664977'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8528674', 'item_ids': ['6704763132'], 'new_item_ids': ['9440686670'], 'payment_method_id': 'paypal_7664977'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.ito3790@example.com',
        instruction="You are Emma Ito, with email emma.ito3790@example.com, and you have a pending order for a stainless steel water bottle. You want to change the shipping address to 4091 Cedar Road, Floor 947, Chicago, IL, USA 92649 because you need it delivered to a new location. You also want to exchange the current blue 1000ml stainless steel water bottle for the red one of the same size and material because you prefer the color, and since the red version is slightly cheaper, you prefer the refund for the price difference to be processed back to your PayPal account. Later, you would like to know more about the store's product catalog, specifically the details of the Water Bottle product, to understand its features and options. After that, you decide you no longer need the order and would like to cancel the entire pending order.\n\nUse emma.ito3790@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8664580', 'address1': '4091 Cedar Road', 'address2': 'Floor 947', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '92649'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8664580'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8664580', 'item_ids': ['2366567022'], 'new_item_ids': ['2439754078'], 'payment_method_id': 'paypal_9995021'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8664580', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.johnson2279@example.com',
        instruction='You are Daiki Johnson, with email daiki.johnson2279@example.com, and you want to update the shipping address for your pending order (containing a glass tea kettle with 1-liter capacity) to 2560 Jefferson Avenue, Apt 31, New York, NY, USA 24164 because it is your current location. You also want your default address updated to this new New York address for future orders. Later, you would like to return the canister-style bagged vacuum cleaner designed for pet hair removal from your previously delivered order, as it is no longer needed, and you prefer the refund to be issued back to your PayPal account used for the original purchase.\n\nUse daiki.johnson2279@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1436802', 'address1': '2560 Jefferson Avenue', 'address2': 'Apt 31', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '24164'}),
            Action(name='modify_user_address', kwargs={'user_id': 'daiki_johnson_9523', 'address1': '2560 Jefferson Avenue', 'address2': 'Apt 31', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '24164'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9502127', 'item_ids': ['2872451762'], 'payment_method_id': 'paypal_2433177'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.brown8893@example.com',
        instruction='You are Anya Brown (anya.brown8893@example.com). You want to update the shipping address for your pending order (containing an E-Reader and Smart Watch) to a new address in Las Vegas because you are relocating temporarily. You prefer the new address to be 7863 Cedar Road, Apt 580, Las Vegas, NV, USA 99313. Later, you would like to change the payment method for this order from your Mastercard ending in 9625 to your PayPal account for easier expense tracking. After that, you would like to return the grey medium fleece Pet Bed from your delivered order (originally shipped to New York) because it does not match your home decor. You want each change confirmed before it is processed.\n\nUse anya.brown8893@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8883368', 'address1': '7863 Cedar Road', 'address2': 'Apt 580', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '99313'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8883368', 'payment_method_id': 'paypal_5206520'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8883368'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2922433', 'item_ids': ['6857426243'], 'payment_method_id': 'credit_card_3414703'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are Sophia Thomas (sophia.thomas1364@example.com). You want to update the shipping address for your pending order (with a bookshelf, tablet, and two office chairs) to 123 Oak Street, Suite 100, Houston, TX, USA 77001 because you will be relocating temporarily. After that, you would like to change the payment method from PayPal to your Visa card ending in 9858 for better rewards tracking. You also want to review the updated order details afterward to confirm the changes. Later, you would like to return the green 6mm PVC yoga mat from your delivered order (shipped to Dallas) and receive a refund to your Mastercard ending in 2378 because it does not meet your comfort expectations.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4862767', 'address1': '123 Oak Street', 'address2': 'Suite 100', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '77001'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4862767', 'payment_method_id': 'credit_card_7326294'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4862767'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1867876', 'item_ids': ['7510236436'], 'payment_method_id': 'credit_card_1034663'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are Omar Silva, and your email is omar.silva4147@example.com. You want to first browse the product catalog to understand what is available. Then, you would like to update the shipping address for your pending order — which includes a fantasy-themed 2000-piece jigsaw puzzle, an intermediate animal-themed 2000-piece puzzle, a brown wooden bookshelf, a silver 4K action camera, and polarized green-lens sunglasses — from San Diego to 6817 Park Drive, Suite 843, San Francisco, CA, USA 37416, because you need it delivered to a new location. Later, you would like to change the payment method for this order from a gift card to your Mastercard ending in 5859 for better personal record-keeping. After that, you decide to cancel the entire order because you no longer need the items.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9728773', 'address1': '6817 Park Drive', 'address2': 'Suite 843', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '37416'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9728773', 'payment_method_id': 'credit_card_5322562'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.moore6624@example.com',
        instruction="You are Mei Moore, with email mei.moore6624@example.com, and you want to update the shipping address for your pending order, which currently contains a pair of silver metal-frame polarized sunglasses with black lenses, a black leather-strap wristwatch, a white glass 5 ft bookshelf, and a 12-inch white analog wall clock, all originally set to ship to Los Angeles. You prefer the new shipping address to be 6374 Maple Lane, Floor 208, San Diego, CA, USA 82884, because you will be in San Diego when the order arrives. Later, you may decide to cancel the order if your plans change, and in that case, you would like it canceled with the reason 'no longer needed'. You prefer the refund, if applicable, to be processed back to the original payment method, which is your credit card.\n\nUse mei.moore6624@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2694395', 'address1': '6374 Maple Lane', 'address2': 'Floor 208', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '82884'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2694395'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2694395', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.anderson1447@example.com',
        instruction='You are assisting Fatima Anderson (email: fatima.anderson1447@example.com) with her pending order for a 31 inch plastic skateboard with a plain design. You want to update the shipping address from Jacksonville, FL to 8143 Maple Lane, Floor 353, Columbus, OH, USA 43812 because she needs it delivered to a different location. Later, you would like to cancel the order entirely because she no longer needs the skateboard. You prefer the refund to be processed back to the original payment method, PayPal.\n\nUse fatima.anderson1447@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2974929', 'address1': '8143 Maple Lane', 'address2': 'Floor 353', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '43812'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2974929'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2974929', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are assisting Omar Silva (email: omar.silva4147@example.com) with his pending order. You want to exchange the current Action Camera (4K resolution, not waterproof, silver color) for the waterproof 4K model in silver (item 6117189161), because it better suits outdoor use. You prefer the price difference refund to be processed to your PayPal account, as it was the intended payment method for adjustments. Later, you would like the shipping address for this order to be updated to 7385 Main Street, Floor 926, San Jose, CA, USA 90389, to align with your current location. After that, you would like to cancel the entire order, as you no longer need the items due to changed plans.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9728773', 'item_ids': ['9391733462'], 'new_item_ids': ['6117189161'], 'payment_method_id': 'paypal_2192303'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9728773', 'address1': '7385 Main Street', 'address2': 'Floor 926', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '90389'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas4271@example.com',
        instruction='You are Liam Thomas, with email liam.thomas4271@example.com, who initially wanted to explore the available product types in the store. You then wanted to update the shipping address for your pending order—containing a pair of black synthetic sneakers size 11, two digital cameras (one 30MP and one 20MP with 5x zoom and CF card storage), a cordless upright vacuum cleaner, and an automatic 9 bar espresso machine with 2L capacity)—from Washington, DC to 6444 Elm Street, Floor 456, San Antonio, TX, USA 68975, and also update your default address in the account to this new San Antonio location. Later, you changed your mind and decided you no longer need the order, so you would like to cancel the entire order instead. You prefer the refund to be processed back to the original payment method, which was PayPal.\n\nUse liam.thomas4271@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7471004230'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3761872'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3761872', 'address1': '6444 Elm Street', 'address2': 'Floor 456', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '68975'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_thomas_8833', 'address1': '6444 Elm Street', 'address2': 'Floor 456', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '68975'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3761872', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.lee3013@example.com',
        instruction='You are assisting Anya Lee (email: anya.lee3013@example.com) with modifying her recent orders. You want to return the Espresso Machine from her delivered order because it is no longer needed. You would like to exchange the current pair of Hiking Boots (size 10, leather, not waterproof) for a new pair in size 9, same leather material, but with waterproofing, because they will be used for wet trail conditions. You prefer the exchange and return to be processed with the price difference handled through your PayPal account. Later, you will cancel your pending order for the Headphones, Hiking Boots (size 12, synthetic, waterproof), Water Bottle, Coffee Maker, and Smart Watch because you no longer need those items. You prefer all refund or adjustment amounts to be returned to the original PayPal payment method.\n\nUse anya.lee3013@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1335809'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1335809', 'item_ids': ['4875647558'], 'payment_method_id': 'paypal_3728317'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1335809', 'item_ids': ['2185126308'], 'new_item_ids': ['8106223139'], 'payment_method_id': 'paypal_3728317'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3176007', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are assisting Fatima Wilson (email: fatima.wilson5906@example.com). You want to update the shipping address for a pending order containing a blue leather office chair and a large gas grill with rotisserie to 2266 Park Drive, Floor 543, San Antonio, TX, USA 91091, because it needs to be delivered to a different location. After that, you would like to change the payment method for this order to PayPal for better transaction tracking. Later, you would like to return the 1L silver glass electric kettle from a previous delivered order, as it is no longer needed, and you prefer the refund to be issued to your PayPal account for consistency with your preferred payment method. After making these changes, you decide to cancel the entire pending order with the office chair and grill because you no longer require the items.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1443906', 'address1': '2266 Park Drive', 'address2': 'Floor 543', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '91091'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1443906', 'payment_method_id': 'paypal_7685859'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7990410'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7990410', 'item_ids': ['1240311797'], 'payment_method_id': 'paypal_7685859'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1443906', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting a customer with email ethan.thomas7730@example.com who initially wants to update the shipping address and payment method for a pending order containing a Smart Watch and a Smartphone. You want to change the shipping address to 3857 Cedar Road, Unit 590, Charlotte, NC, USA 58392, because it is their updated preferred delivery location. You also prefer to pay using the Visa card ending in 8901 instead of the original gift card, for better purchase protection. Later, you would like to return the Pet Bed (medium, memory foam, brown) from a previously delivered order, as it is no longer needed, and request a refund to the PayPal account used for that original purchase. After that, you decide to cancel the pending order entirely because the Smart Watch and Smartphone are no longer required, despite the earlier updates.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '3857 Cedar Road', 'address2': 'Unit 590', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '58392'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'credit_card_7472558'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7764382'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['5067898160'], 'payment_method_id': 'paypal_6982172'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are assisting Liam Thomas (liam.thomas9081@example.com) with modifying his pending order and returning an item from a delivered order. You want to change the payment method for the pending order from the current Visa card to PayPal, as he prefers using PayPal for better purchase protection. You would like to upgrade the E-Reader in the same order from the 7-inch to the 8-inch screen size, keeping Wi-Fi and 8GB storage the same, because he prefers a larger display for reading comfort. Later, you will update the shipping address for this order to 1500 Oak Avenue, Unit 742, Denver, CO, USA 68391, and also set this as his default address for future orders. After that, you would like to initiate a return for the hiking boots from his delivered order, as they are not waterproof and do not meet his outdoor needs, and you prefer the refund to be issued back to his PayPal account for consistency with his preferred payment method.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1654931'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1654931', 'payment_method_id': 'paypal_3650980'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1654931', 'item_ids': ['6268080249'], 'new_item_ids': ['9494281769'], 'payment_method_id': 'paypal_3650980'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1654931', 'address1': '1500 Oak Avenue', 'address2': 'Unit 742', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '68391'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_thomas_7882', 'address1': '1500 Oak Avenue', 'address2': 'Unit 742', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '68391'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8488728', 'item_ids': ['5676696062'], 'payment_method_id': 'paypal_3650980'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction="You are Yusuf Garcia, with email yusuf.garcia2909@example.com. You want to update the shipping address for your pending order—containing hiking boots, a black 13-inch laptop with 32GB RAM, and an air purifier—from Indianapolis to 7525 Main Street, Unit 404, Oklahoma City, OK, USA 93925, because you've relocated. You also want your default address updated to this new Oklahoma City address for future orders. For your delivered order, you would like to return the black Action Camera that is not waterproof and exchange it for a black 4K waterproof model, because you need it for outdoor adventures in wet conditions. You prefer any price difference to be processed using your PayPal account. Later, you decided to cancel the pending order entirely, even after the address update, because you no longer need the items.\n\nUse yusuf.garcia2909@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '7525 Main Street', 'address2': 'Unit 404', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '93925'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_garcia_3055', 'address1': '7525 Main Street', 'address2': 'Unit 404', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '93925'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2286012', 'item_ids': ['7523669277'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2286012', 'item_ids': ['7523669277'], 'new_item_ids': ['6700049080'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.nguyen1293@example.com',
        instruction='You are assisting Aarav Nguyen (email: aarav.nguyen1293@example.com). You want to exchange the delivered blue Wireless Earbuds (with IPX4 water resistance) for the black pair with better water resistance (IPX7), because he prefers a more durable option for outdoor use. You also want to update the shipping address for the pending order to 7668 Lincoln Street, Unit 131, Jacksonville, FL, USA 84368, and set this new address as the default for future orders, as he has relocated. Later, after reviewing his needs, you would like to cancel the pending order entirely, because he no longer requires the items.\n\nUse aarav.nguyen1293@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2443586', 'address1': '7668 Lincoln Street', 'address2': 'Unit 131', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '84368'}),
            Action(name='modify_user_address', kwargs={'user_id': 'aarav_nguyen_7344', 'address1': '7668 Lincoln Street', 'address2': 'Unit 131', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '84368'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7728728', 'item_ids': ['8555936349'], 'payment_method_id': 'paypal_7859314'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7728728', 'item_ids': ['8555936349'], 'new_item_ids': ['9580569596'], 'payment_method_id': 'paypal_7859314'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2443586'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2443586', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li7352@example.com',
        instruction='You are Sofia Li (sofia.li7352@example.com) and you want to update the shipping address for your pending order—containing an Air Purifier for medium rooms, a pair of size 7 synthetic hiking boots, a 34-inch plastic skateboard, and a pink 6mm natural rubber yoga mat—to 1770 Main Street, Suite 935, Las Vegas, NV, USA 26368, because you entered the wrong address initially. You also want your default address updated to the same, to ensure future orders are delivered correctly. Later, you would like to change the payment method for this order from your Visa ending in 6791 to your Mastercard ending in 8484, as you prefer to use that card for this purchase.\n\nUse sofia.li7352@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8855135', 'address1': '1770 Main Street', 'address2': 'Suite 935', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '26368'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_li_9219', 'address1': '1770 Main Street', 'address2': 'Suite 935', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '26368'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8855135'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8855135', 'payment_method_id': 'credit_card_8105988'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.lee9368@example.com',
        instruction='You are assisting Yara Lee (email: yara.lee9368@example.com) with her pending order. You want to update the shipping address for the order to 465 Madison Drive, Apt 546, Austin, TX, USA 12351, because it was initially set to an incorrect Houston address. You also want to update your default address in the account to this new Austin address for future orders. Later, you would like to change the payment method for this order from your Mastercard ending in 5715 to your Visa card ending in 6367, as you prefer to use that card for this purchase.\n\nUse yara.lee9368@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3320020', 'address1': '465 Madison Drive', 'address2': 'Apt 546', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '12351'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yara_lee_7701', 'address1': '465 Madison Drive', 'address2': 'Apt 546', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '12351'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3320020'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3320020', 'payment_method_id': 'credit_card_6450164'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.smith9157@example.com',
        instruction="You are Olivia Smith (olivia.smith9157@example.com). You want to update the shipping address for your pending order—containing a red large mountain bicycle, a men's fresh 50ml perfume, a 31-inch bamboo skateboard, and a 30MP digital camera—to 3892 Adams Road, Floor 408, Houston, TX, USA 57508, because you initially needed it delivered there. Later, you decided you no longer need those items, so you would like to cancel the entire order. Additionally, for your delivered order containing a blue medium cycling helmet with low ventilation, you would like to exchange it for the red medium version with high ventilation, because you prefer better airflow and a different color. You prefer to use your PayPal account for any price difference associated with the exchange.\n\nUse olivia.smith9157@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1348609', 'address1': '3892 Adams Road', 'address2': 'Floor 408', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '57508'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1348609', 'reason': 'no longer needed'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3794101', 'item_ids': ['3339188619'], 'new_item_ids': ['8573379326'], 'payment_method_id': 'paypal_2076152'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are Sophia Thomas, with email sophia.thomas1364@example.com, and you want to first update the shipping address for your pending order—containing a bookshelf, tablet, and two office chairs—to 2627 Madison Drive, Floor 281, Chicago, IL, USA 72863, because it was initially set to the wrong location. Later, you intend to cancel that entire order because you no longer need the items. Separately, you would like to exchange the black large polyester backpack with a laptop compartment from your delivered order for a similar backpack that has a camera compartment and is made of nylon, because it better suits your needs for carrying photography equipment. You prefer the exchange to be processed using your Mastercard ending in 2378 for any price difference.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4862767', 'address1': '2627 Madison Drive', 'address2': 'Floor 281', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '72863'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4862767', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1867876'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1867876', 'item_ids': ['6906307980'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'credit_card_1034663'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.thomas7243@example.com',
        instruction='You are assisting mia.thomas7243@example.com with their pending order. You want to update the shipping address to 1637 Park Drive, Unit 599, New York, NY, USA 84191 because the customer has relocated temporarily. You would like to change the Hiking Boots from synthetic to leather material in size 12 while keeping the waterproof feature, as leather offers better durability for long hikes. You also want to replace the Backpack from grey nylon to green leather while maintaining the small size and laptop compartment, preferring the leather version for its professional look and longevity. You prefer any price adjustments to be handled using the PayPal account already on file.\n\nUse mia.thomas7243@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5208989', 'address1': '1637 Park Drive', 'address2': 'Unit 599', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '84191'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5208989'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5208989', 'item_ids': ['4694984344', '8054888773'], 'new_item_ids': ['8277474082', '7251508981'], 'payment_method_id': 'paypal_2977884'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting Sophia Patel, whose email is sophia.patel9841@example.com. You want to explore the available product types, with a specific interest in Running Shoes, which come in various sizes, colors, and materials such as leather or mesh, and feature EVA or rubber soles. Later, you would like to cancel your pending order placed in Fort Worth, TX, which includes a men's oriental-scented 100ml Perfume, a glass Tea Kettle with 1.5-liter capacity, a black 1L Electric Kettle, and gray size-8 canvas Sneakers, because you no longer need these items. After that, you would like to return the blue Wireless Earbuds from your delivered order for a refund, and you prefer the refund to be issued back to your original payment method, which is your Mastercard ending in 1639.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6938111410'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7905419', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2923184', 'item_ids': ['2757705742'], 'payment_method_id': 'credit_card_6419343'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.hernandez3039@example.com',
        instruction='You are assisting Sofia Hernandez (sofia.hernandez3039@example.com) with two requests in sequence. First, you want to exchange the red large v-neck cotton T-shirt from her delivered order (Seattle, delivered) for a blue medium crew neck cotton T-shirt, because the original size and style do not fit her preference. You prefer to use the Visa card ending in 7312 for any price difference associated with the exchange. Later, you will request to cancel her pending order for a portable gas grill, placed by mistake, before it ships.\n\nUse sofia.hernandez3039@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6876713'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6876713', 'item_ids': ['3234800602'], 'payment_method_id': 'credit_card_7901829'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6876713', 'item_ids': ['3234800602'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'credit_card_7901829'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3561391', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are assisting a customer with email lei.li8350@example.com regarding her pending order. You want to update the shipping address to 6180 Elm Street, Suite 823, New York, NY, USA 51576 because the original address was incorrect. You would like to change the payment method from PayPal to the Visa card ending in 2697 for both the original and any adjusted charges. You prefer to upgrade the laptop to a 17-inch model with an i7 processor, 32GB RAM, and black color over the current configuration because you want better performance and a preferred color. You want this change applied using the same Visa card for any price difference. Later, after reviewing the updated order, you decide you no longer need the laptop and would like to cancel the entire order. You confirm cancellation is intentional and complete.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '6180 Elm Street', 'address2': 'Suite 823', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '51576'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5166363', 'payment_method_id': 'credit_card_4466831'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5166363', 'item_ids': ['3334537816'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'credit_card_4466831'}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ahmed5620@example.com',
        instruction='You are Olivia Ahmed, a loyal customer with email olivia.ahmed5620@example.com, who received a delivered order in San Francisco. You want to exchange the small fleece beige Pet Bed from that order for a medium memory foam beige Pet Bed because you prefer more supportive bedding for your pet. You prefer to use your Visa card ending in 5022 for any price adjustment. Later, you would like to browse the full catalog of available product types to explore other items the store offers.\n\nUse olivia.ahmed5620@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1579621'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1579621', 'item_ids': ['4982943126'], 'payment_method_id': 'credit_card_9698900'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1579621', 'item_ids': ['4982943126'], 'new_item_ids': ['3360679910'], 'payment_method_id': 'credit_card_9698900'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2747247837'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.santos8390@example.com',
        instruction="You are assisting Harper Santos (harper.santos8390@example.com). You want to cancel the pending order that includes an electric toothbrush in white, a men's 100ml fresh-scented perfume, a large grey memory foam pet bed, a 20MP 10x zoom digital camera with CF card storage, and a 12-inch white analog wall clock, because it is no longer needed. Later, you would like to update the shipping address for another pending order—which includes polarized green-lens black sunglasses, a silver 17-inch i9 laptop with 8GB RAM and 256GB SSD, an Apple HomeKit-compatible stainless steel smart thermostat, a 30MP 10x zoom digital camera with SD card storage, and a large grey nylon backpack with a hydration compartment—from Indianapolis to 867 Main Street, Unit 530, Seattle, WA, USA 82738. You prefer the refund from the canceled order to be returned to the original PayPal method used for payment.\n\nUse harper.santos8390@example.com for authentication.",
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6629830', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6629830'}),
            Action(name='get_product_details', kwargs={'product_id': '7352963235'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4941028', 'address1': '867 Main Street', 'address2': 'Unit 530', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '82738'}),
            Action(name='modify_user_address', kwargs={'user_id': 'harper_santos_8115', 'address1': '867 Main Street', 'address2': 'Unit 530', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '82738'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.santos3158@example.com',
        instruction='You are Ivan Santos, with email ivan.santos3158@example.com, who first wanted to explore the available products, particularly Garden Hose and Wireless Earbuds. You want to update the shipping address for your pending order (with an Office Chair) to 4060 Oak Avenue, Apt 629, Los Angeles, CA, USA 93549, and also update your default address to match. Later, you would like to exchange items from your delivered order (originally shipped to Austin): you prefer the 100ft blue latex Garden Hose over the 50ft black vinyl one you received, because you need greater length and more flexible material. You also prefer the blue Wireless Earbuds with 8-hour battery life over the 6-hour version you received, to improve usage time between charges. You prefer any price difference to be handled using your PayPal account, which was used for the original purchase.\n\nUse ivan.santos3158@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6679515468'}),
            Action(name='get_product_details', kwargs={'product_id': '9924732112'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8770097', 'address1': '4060 Oak Avenue', 'address2': 'Apt 629', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '93549'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ivan_santos_6635', 'address1': '4060 Oak Avenue', 'address2': 'Apt 629', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '93549'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6893533', 'item_ids': ['5206946487', '1646531091'], 'new_item_ids': ['8481719475', '8555936349'], 'payment_method_id': 'paypal_6151711'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, with email olivia.ito5204@example.com, who first wanted to explore the product catalog, particularly Espresso Machines. You want to update the shipping address for your pending order (containing a black wired gaming mouse, a red 7 ft polyester patio umbrella, and size 8 leather hiking boots) to 272 Adams Road, Floor 127, Chicago, IL, USA 92845, because you need the items delivered to a new location. Later, you would like to change the payment method for that same pending order to PayPal, because you prefer to use that for tracking and protection. After that, you would like to return the black synthetic sneakers in size 11 from your delivered order (which also included an automatic 19 bar espresso machine), because they do not fit, and you prefer a refund back to your PayPal account for convenience and faster processing.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4354588079'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '272 Adams Road', 'address2': 'Floor 127', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '92845'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5866402'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5866402', 'item_ids': ['9727387530'], 'payment_method_id': 'paypal_8049766'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are assisting Sophia Thomas (sophia.thomas1364@example.com), who wants to learn more about the Action Camera, specifically the 4K waterproof black model, because she is considering purchasing it for outdoor use. You want to provide her with details about its features, including 4K resolution, waterproof design, and pricing around $467. Later, you will update the shipping address for her pending order containing a bookshelf, tablet, and two office chairs to 123 Oak Avenue, Suite 100, Austin, TX, USA 78701, because she has relocated within Texas. You also want to change the payment method for this order to her Visa card ending in 9858, as she prefers to consolidate payments on that card. After that, you would like to initiate a return for the black large polyester backpack from her delivered order, because it does not meet her durability expectations, and process a refund to her Mastercard ending in 2378, as that was the original payment method and she wants the credit restored there.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4862767', 'address1': '123 Oak Avenue', 'address2': 'Suite 100', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '78701'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4862767', 'payment_method_id': 'credit_card_7326294'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4862767'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1867876', 'item_ids': ['6906307980'], 'payment_method_id': 'credit_card_1034663'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.wilson1253@example.com',
        instruction='You are assisting lei.wilson1253@example.com. You are first interested in exploring the available product types, particularly the Laptop variants, to understand the options. You would like to exchange the 50ft vinyl black Garden Hose from your delivered order for the 100ft latex blue one because you need a longer and more durable hose in a different color. You also want to return the Portable Charger from the same order as it is no longer needed. You prefer any price adjustment to be processed using your Mastercard ending in 1531. Later, you would like to cancel your pending order entirely because you no longer need the items, including the Wireless Earbuds, Espresso Machine, Headphones, Smartphone, and Tablet.\n\nUse lei.wilson1253@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2905754'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2905754', 'item_ids': ['5206946487'], 'new_item_ids': ['8481719475'], 'payment_method_id': 'credit_card_3677959'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2905754', 'item_ids': ['7903094618'], 'payment_method_id': 'credit_card_3677959'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3826449', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.rossi7301@example.com',
        instruction="You are assisting Yusuf Rossi (email: yusuf.rossi7301@example.com), who first wanted to explore the store's product offerings, particularly digital cameras. You want to exchange the digital camera from his delivered order (received in Philadelphia) because he prefers a model with higher zoom capability—specifically, he wants to replace the 3x zoom camera he received with a similar 24MP model that has 5x zoom and uses CF card storage. You prefer this exchange to be processed using his Mastercard ending in 2478 for any price adjustment. Later, you will request to cancel another order placed to the same address that is still pending, because it was ordered by mistake and is no longer needed.\n\nUse yusuf.rossi7301@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8940227892'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6679257'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6679257', 'item_ids': ['5996159312'], 'new_item_ids': ['4326528037'], 'payment_method_id': 'credit_card_9513926'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6679257', 'item_ids': ['5996159312'], 'payment_method_id': 'credit_card_9513926'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4776164', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed.khan5338@example.com',
        instruction='You are assisting Mohamed Khan (email: mohamed.khan5338@example.com). You want to exchange the skateboard from your delivered order (with a graphic design, maple deck, and 34 inch length) for a new one with a bamboo deck and 31 inch length in the same graphic design, because you prefer the lighter, more flexible bamboo material and a slightly more compact size. You prefer the refund or charge for any price difference to be processed to your PayPal account. Later, for your pending order, you would like to change the black wireless earbuds with 8 hours battery life to the blue ones with 6 hours battery life, because you prefer the color and are satisfied with slightly shorter battery performance. You also want to update the shipping address to 5175 Oak Avenue, Unit 730, New York, NY, USA 29972 for this order. You prefer any price difference for this change to be handled via PayPal as well. After that, you would like to browse all available product types in the store to explore other items of interest.\n\nUse mohamed.khan5338@example.com for authentication.',
        actions=[
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W4887592', 'item_ids': ['2343503231'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'paypal_1249653'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7390432', 'item_ids': ['2499294441'], 'new_item_ids': ['1646531091'], 'payment_method_id': 'paypal_1249653'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7390432', 'address1': '5175 Oak Avenue', 'address2': 'Unit 730', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '29972'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.thomas4351@example.com',
        instruction='You are Aarav Thomas, with email aarav.thomas4351@example.com. You want to update the shipping address for your pending order containing a blue cycling helmet, a leather-strap wristwatch, and a manual espresso machine to 7471 Park Drive, Suite 15, Fort Worth, TX, USA 82827 because it was shipped to the wrong location. You also want to return the blue v-neck cotton T-shirt from your delivered order that included a 1000-piece art puzzle, as it doesn’t fit well, and you prefer the refund to be issued back to your gift card. Later, you would like to cancel another pending order that includes a black digital wall clock, a 750ml glass water bottle, a black cycling helmet, a red Bluetooth speaker, and a 1L stainless steel electric kettle because you realized it was placed by mistake.\n\nUse aarav.thomas4351@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5158064', 'address1': '7471 Park Drive', 'address2': 'Suite 15', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '82827'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5158064'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9833379', 'item_ids': ['8349118980'], 'payment_method_id': 'gift_card_6253568'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9833379', 'item_ids': ['8349118980'], 'new_item_ids': ['8349118980'], 'payment_method_id': 'gift_card_6253568'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9767156', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.johnson6791@example.com',
        instruction='You are Omar Johnson (omar.johnson6791@example.com). You want to update the shipping address for your pending order, which includes an Indoor Security Camera and a Laptop, to 7015 Park Drive, Floor 226, Dallas, TX, USA 29120, because you need it delivered to a new location. You also want to return the white small-sized Cycling Helmet from your earlier delivered order that included a Grill, Jigsaw Puzzle, and Vacuum Cleaner, and you prefer the refund to be processed to your PayPal account since that was your original payment method. Later, after updating the address, you realize you no longer need the items in the pending order, so you would like to cancel the entire pending order.\n\nUse omar.johnson6791@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8797321', 'address1': '7015 Park Drive', 'address2': 'Floor 226', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '29120'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8797321'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2809253', 'item_ids': ['1596993217'], 'payment_method_id': 'paypal_6053880'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2809253', 'item_ids': ['1596993217'], 'new_item_ids': ['1596993217'], 'payment_method_id': 'paypal_6053880'}),
            Action(name='get_product_details', kwargs={'product_id': '7765186836'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8797321', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction="You are Lei Li, with email lei.li8350@example.com, and you have a pending order for a 17-inch space grey Laptop with i5 processor, 8GB RAM, and 1TB SSD, currently set to ship to San Francisco. You want to update the shipping address to 3045 Adams Road, Apt 10, Detroit, MI, USA 72778 because you will be relocating and need the delivery redirected. After the address is successfully updated, you would like to review the updated order details to confirm the change. You are also considering canceling the order later if the item is no longer needed, with cancellation reason 'no longer needed', but only after confirming the address update. Additionally, you would like to explore purchasing a Backpack later and prefer to review product details now to compare options, particularly interested in variants with laptop or camera compartments, available in colors like black, green, or grey, and made of durable materials like nylon or polyester.\n\nUse lei.li8350@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '3045 Adams Road', 'address2': 'Apt 10', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '72778'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.silva5146@example.com',
        instruction='You are assisting Lucas Silva (lucas.silva5146@example.com) with his pending order. You want to upgrade the laptop in the order from the current 13-inch i5 model to the 15-inch i7 model with 32GB RAM and 1TB SSD, because he prefers more processing power, memory, and storage for his workflow. You prefer the refund for any price difference to be applied to the Mastercard ending in 5197. Later, you would like to update the shipping address for the entire order to 9999 Elm Street, Apt 256, Phoenix, AZ, USA 80616, to ensure delivery to his new location.\n\nUse lucas.silva5146@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1814268'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1814268', 'item_ids': ['6056040996'], 'new_item_ids': ['6017636844'], 'payment_method_id': 'credit_card_8865901'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1814268', 'address1': '9999 Elm Street', 'address2': 'Apt 256', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '80616'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.brown8893@example.com',
        instruction="You are Anya Brown (email: anya.brown8893@example.com). You want to update the shipping address for your pending order (containing an E-Reader and Smart Watch) to 773 Park Drive, Suite 900, Jacksonville, FL, USA 95331, because it needs to be delivered to a new location. You also want your default address for future orders to be updated to this same address for consistency. Later, you would like to exchange the medium grey fleece pet bed from your delivered order (which also included a Makeup Kit, Tablet, and Grill) for a similar pet bed in the same size and color but made of polyester, because you prefer the durability and easier maintenance of polyester over fleece. You prefer the price difference to be handled using your Mastercard ending in 9625. After that, you would like to cancel your other pending order (containing a Wall Clock, Desk Lamp, Dumbbell Set, and Bluetooth Speaker) with the reason 'no longer needed', as you have decided not to proceed with that purchase.\n\nUse anya.brown8893@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8883368', 'address1': '773 Park Drive', 'address2': 'Suite 900', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '95331'}),
            Action(name='modify_user_address', kwargs={'user_id': 'anya_brown_2024', 'address1': '773 Park Drive', 'address2': 'Suite 900', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '95331'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2922433'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2922433', 'item_ids': ['6857426243'], 'new_item_ids': ['2405281423'], 'payment_method_id': 'credit_card_3414703'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2922433', 'item_ids': ['6857426243'], 'payment_method_id': 'credit_card_3414703'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1170711', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com). You want to update the shipping address for a pending order containing a grey polyester backpack to 2161 Elm Street, Unit 495, Denver, CO, USA 14563, because it is the correct delivery location. You also want to update your default address to this same Denver address for future orders. Later, you would like to exchange the black Bluetooth speaker from a previously delivered order (which included an electric toothbrush, perfume, and action camera) for the red version with 10-hour battery life and water resistance, because you prefer the color and shorter battery duration with water protection. You prefer any price difference to be handled via your PayPal account. After that, you would like to cancel another pending order containing hiking boots, a black 13-inch laptop with i7 processor, and an air purifier, because you no longer need the items.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6885344', 'address1': '2161 Elm Street', 'address2': 'Unit 495', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '14563'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_garcia_3055', 'address1': '2161 Elm Street', 'address2': 'Unit 495', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '14563'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2286012'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2286012', 'item_ids': ['6455132774'], 'new_item_ids': ['7751905257'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2286012', 'item_ids': ['6455132774'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.ito7258@example.com',
        instruction='You are Sofia Ito (sofia.ito7258@example.com) and you first want to understand what product types are available, particularly the Fleece Jacket options, to make an informed choice. After receiving your delivered order in San Francisco, you would like to exchange the black Fleece Jacket (size M, full zipper) for the same style in size L because it will provide a better fit. You prefer the black, full-zip version in large over the current medium as it aligns with your comfort needs. You also prefer any price adjustment to be processed using your Visa card ending in 8566.\n\nUse sofia.ito7258@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8560156827'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6075915'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6075915', 'item_ids': ['4728397765'], 'new_item_ids': ['9385662952'], 'payment_method_id': 'credit_card_7183597'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6075915', 'item_ids': ['4728397765'], 'payment_method_id': 'credit_card_7183597'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are assisting Fatima Wilson, who has the email fatima.wilson5906@example.com. You want to update the shipping address for her pending order—which includes a blue leather Office Chair and a large gas grill with rotisserie—to 943 Maple Drive, Suite 356, Chicago, IL, USA 60621, because she needs it delivered to a new location. After that, you would like to change the payment method from her Mastercard ending in 9779 to her PayPal account, as she prefers using PayPal for this purchase. Later, you would like to browse the available options for a Backpack, as she is considering a future purchase and wants to explore the styles and features offered.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1443906'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1443906', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1443906', 'payment_method_id': 'paypal_7685859'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.patel3193@example.com',
        instruction="You are Mei Patel, with email mei.patel3193@example.com, who initially inquired about the product catalog with a specific interest in perfumes. You want to change the payment method for your pending order—containing a men's oriental 100ml perfume, an adjustable 30-50 lbs dumbbell set, a red 2-piece softshell luggage set, and a 25ft green latex garden hose—currently in Fort Worth, TX, from PayPal to your Visa card ending in 9904, because you prefer using your credit card for this purchase. Later, after the payment update, you would like to cancel the entire order as you no longer need the items.\n\nUse mei.patel3193@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_order_details', kwargs={'order_id': '#W9583042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9583042', 'payment_method_id': 'credit_card_9503061'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9583042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.lopez3271@example.com',
        instruction='You are Isabella Lopez, and your email is isabella.lopez3271@example.com. You are interested in the Bluetooth Speakers offered by the store. You have a pending order for a red Bluetooth Speaker with 10-hour battery life and water resistance, and you would like to exchange it for the green version with 20-hour battery life that is not water-resistant, as you prefer longer battery life over water resistance. Later, you would like any price difference refunded to your Mastercard ending in 4336, as that was your preferred payment method for the original purchase.\n\nUse isabella.lopez3271@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4768869376'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4923227'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4923227', 'item_ids': ['7751905257'], 'new_item_ids': ['9440686670'], 'payment_method_id': 'credit_card_8554680'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4923227', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.gonzalez9269@example.com',
        instruction='You are assisting Aarav Gonzalez (email: aarav.gonzalez9269@example.com). You want to cancel the pending order containing an Electric Toothbrush, Action Camera, Cycling Helmet, and Smart Watch because he no longer needs it. Later, for another pending order that includes a 1000ml stainless steel Water Bottle, Bluetooth Speaker, Wall Clock, Patio Umbrella, and Fleece Jacket, you would like to update the shipping address to 4138 Cedar Road, Suite 75, Jacksonville, FL, USA 78166, and also set this as the new default address. You prefer the Water Bottle in black instead of blue, keeping the same 1000ml stainless steel version, because it matches your other gear. You prefer any price difference from the color change to be handled using your PayPal account.\n\nUse aarav.gonzalez9269@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6979932'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6979932', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9160732', 'address1': '4138 Cedar Road', 'address2': 'Suite 75', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '78166'}),
            Action(name='modify_user_address', kwargs={'user_id': 'aarav_gonzalez_5113', 'address1': '4138 Cedar Road', 'address2': 'Suite 75', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '78166'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9160732', 'item_ids': ['2366567022'], 'new_item_ids': ['7661609223'], 'payment_method_id': 'paypal_6121064'}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas4271@example.com',
        instruction='You are assisting Liam Thomas (email: liam.thomas4271@example.com) with his order containing black synthetic sneakers, a digital camera, a vacuum cleaner, and an espresso machine, currently pending and originally set for delivery to Washington, DC. You want to first verify the order contents and product details for the sneakers, particularly confirming the style and fit. You would like to update the shipping address to 5263 Park Drive, Floor 843, San Diego, CA, USA 89599, because the delivery location has changed. You prefer to switch the payment method from PayPal to your Mastercard ending in 1208 for better expense tracking. Later, after reconsidering your needs, you decide to cancel the entire order because the items are no longer required.\n\nUse liam.thomas4271@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3761872'}),
            Action(name='get_product_details', kwargs={'product_id': '7471004230'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3761872', 'address1': '5263 Park Drive', 'address2': 'Floor 843', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '89599'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3761872', 'payment_method_id': 'credit_card_5089597'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3761872', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.lopez2997@example.com',
        instruction="You are assisting Raj Lopez (email: raj.lopez2997@example.com) with his order for a black stainless steel 500ml water bottle, a bamboo 31-inch graphic skateboard, and a pair of synthetic waterproof hiking boots in size 9, all currently pending shipment to 575 Chestnut Street, Suite 251, Fort Worth, TX, 76195. You want to first verify the order and product details, particularly confirming the water bottle is the 500ml stainless steel black version. Later, you would like to update the shipping address to 6072 Madison Drive, Apt 258, Columbus, OH, USA 68453, because the original delivery location is no longer valid. You also prefer to switch the payment method from the Mastercard ending in 6731308 to your PayPal account for better transaction tracking. After that, you decide the items are no longer needed, so you would like to cancel the entire order with the reason 'no longer needed'.\n\nUse raj.lopez2997@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3502364'}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3502364', 'address1': '6072 Madison Drive', 'address2': 'Apt 258', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '68453'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3502364', 'payment_method_id': 'paypal_7007375'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3502364', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction="You are assisting Lucas Johansson (email: lucas.johansson7741@example.com) with a pending order originally shipped to San Francisco. You want to update the shipping address to 7595 Madison Drive, Unit 531, Chicago, IL, USA 53562, because the delivery location has changed. After that, you would like to change the payment method to the Visa card ending in 9452 for better rewards tracking. Later, you plan to cancel the entire order because it is no longer needed. Additionally, you are interested in browsing details for the 'Action Camera' product for a potential future purchase, as it aligns with your outdoor activity interests.\n\nUse lucas.johansson7741@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '7595 Madison Drive', 'address2': 'Unit 531', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '53562'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.johansson3155@example.com',
        instruction="You are Yara Johansson, and your email is yara.johansson3155@example.com. You want to update the shipping address for your pending order—which includes a black silicone wristwatch, a blue high-back leather office chair, two jigsaw puzzles (1000 and 2000 pieces), and black wireless earbuds—from Fort Worth to 8575 Pine Avenue, Unit 631, Nashville, TN, USA 54811, because you have relocated temporarily. Later, if the order cannot be shipped to the new address, you would like to cancel it with the reason 'no longer needed'. Additionally, you would like to exchange the delivered blue cycling helmet (size S, low ventilation) for the red one of the same size and ventilation level, because you prefer the red color. You prefer to use your Mastercard ending in 5736 for any price adjustment associated with the exchange.\n\nUse yara.johansson3155@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3372648', 'address1': '8575 Pine Avenue', 'address2': 'Unit 631', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '54811'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3372648', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3372648'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9994227', 'item_ids': ['5886093635'], 'new_item_ids': ['3358616356'], 'payment_method_id': 'credit_card_4582364'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.santos7683@example.com',
        instruction='You are Emma Santos (emma.santos7683@example.com) and you want to first update the shipping address for your pending order—which includes an office chair, a skateboard, and two water bottles—to 123 Oak Street, Apt 4B, Houston, TX, USA 77001, because you initially provided the wrong address. Later, you will cancel this entire order because you placed it by mistake. Separately, for your delivered order that included a mechanical keyboard with clicky switches, you would like to exchange it for a similar 80% size model but with tactile switches and white backlight, because you prefer a smoother typing feel over the current clicky response. You prefer any refund or charge related to these actions to be processed using your Mastercard ending in 6380.\n\nUse emma.santos7683@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9903153', 'address1': '123 Oak Street', 'address2': 'Apt 4B', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '77001'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9903153', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9903153'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3113816', 'item_ids': ['4843487907'], 'new_item_ids': ['9991484137'], 'payment_method_id': 'credit_card_5869505'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.ito3790@example.com',
        instruction='You are assisting Emma Ito, whose email is emma.ito3790@example.com. You want to first review all available product types in the catalog to understand the full range of offerings. Then, for a pending order containing a 1000ml stainless steel blue water bottle, you would like to update the shipping address to 8193 Washington Boulevard, Floor 989, Portland, OR, USA 27860, to ensure delivery to the correct location. After that, you prefer to change the payment method to your Visa card ending in 3660 for consistency with your preferred payment profile. Later, after reconsidering the purchase, you decide the order is no longer needed and would like to cancel it entirely.\n\nUse emma.ito3790@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8664580', 'address1': '8193 Washington Boulevard', 'address2': 'Floor 989', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '27860'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8664580', 'payment_method_id': 'credit_card_8058445'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8664580', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.brown3965@example.com',
        instruction="You are Harper Brown, with email harper.brown3965@example.com, and you want to update the payment method for your pending order in Fort Worth from your Visa ending in 3356 to your PayPal account because you prefer using PayPal for this transaction. After that, you would like to cancel the entire order because you no longer need the items, including the gold smart watch with silicone band, glass tea kettle, men's woody perfume, black electric toothbrush, and leather hiking boots in size 10.\n\nUse harper.brown3965@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2273069'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2273069', 'payment_method_id': 'paypal_2306935'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2273069', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.patel3193@example.com',
        instruction="You are Mei Patel, with email mei.patel3193@example.com, who placed a pending order in Fort Worth, TX for a men's oriental 100ml perfume, an adjustable 30-50 lbs iron dumbbell set, a red 2-piece softshell luggage set, and a 25ft green latex garden hose. You want to change the payment method from PayPal to your Visa card ending in 9904 because you prefer using that card for this purchase. Later, you would like to cancel the entire order because it was placed by mistake. You prefer the refund to be processed back to the new payment method used, which is your Visa card ending in 9904.\n\nUse mei.patel3193@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9583042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9583042', 'payment_method_id': 'credit_card_9503061'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9583042', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are assisting Sophia Thomas (sophia.thomas1364@example.com). You want to exchange the black large polyester backpack with a laptop compartment from her delivered order for a green small one with the same features, because she prefers the smaller size and green color. Later, you will update the shipping address for her pending order to 7349 Lincoln Street, Apt 799, Charlotte, NC, USA 62134, because she needs the items delivered to a new location. After that, you would like to change the payment method on the same pending order from PayPal to her Visa card ending in 9858, because she prefers to use her credit card for this purchase.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1867876', 'item_ids': ['6906307980'], 'new_item_ids': ['3557711149'], 'payment_method_id': 'credit_card_1034663'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4862767', 'address1': '7349 Lincoln Street', 'address2': 'Apt 799', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '62134'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4862767', 'payment_method_id': 'credit_card_7326294'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.brown8893@example.com',
        instruction='You are assisting Anya Brown (email: anya.brown8893@example.com). You want to update the shipping address for a pending order containing an 8GB Wi-Fi 6-inch e-reader and a black leather-band AMOLED smart watch to 9659 Park Drive, Floor 8, San Antonio, TX, USA 67744, and also update the default address in the profile to the same address, for consistency and delivery accuracy. Later, you will cancel the same pending order because it is no longer needed. You prefer the refund to be processed back to the original payment method, the credit card used for the purchase.\n\nUse anya.brown8893@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8883368', 'address1': '9659 Park Drive', 'address2': 'Floor 8', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '67744'}),
            Action(name='modify_user_address', kwargs={'user_id': 'anya_brown_2024', 'address1': '9659 Park Drive', 'address2': 'Floor 8', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '67744'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8883368', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.muller6617@example.com',
        instruction='You are assisting Ethan Muller (email: ethan.muller6617@example.com). You want to exchange the rose gold 64GB smartphone from your delivered order (Seattle, delivered) for a black 128GB model, as you prefer more storage and a different color. You prefer the price difference to be adjusted using your Visa card ending in 1399. Later, you would like to cancel your pending order (Denver, still processing) because you realized it was placed by mistake.\n\nUse ethan.muller6617@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3155037'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3155037', 'item_ids': ['3952176596'], 'new_item_ids': ['5339029584'], 'payment_method_id': 'credit_card_5721095'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4683557', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li5953@example.com',
        instruction='You are assisting Sofia Li (sofia.li5953@example.com) with two order actions. First, you want to exchange one navy XL fleece jacket with a full zipper from her delivered order (containing an e-reader, action camera, digital camera, and two fleece jackets) for the same jacket but with a half zipper, because she prefers the half-zip style. You prefer the price adjustment to be processed using her Mastercard ending in 8609. Later, you will request to cancel her pending order placed in Philadelphia, which includes wireless earbuds, two electric kettles, a notebook, and a yoga mat, because it was placed by mistake.\n\nUse sofia.li5953@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6874763'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6874763', 'item_ids': ['7528037711'], 'new_item_ids': ['8590708195'], 'payment_method_id': 'credit_card_4046723'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1557241', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.silva5146@example.com',
        instruction='You are assisting Lucas Silva (lucas.silva5146@example.com) with a series of requests regarding his order and product exploration. First, you want to update the shipping address for his pending order—which includes a ceramic 2-liter tea kettle, a space grey 13-inch laptop with i5 processor, a black 5000mAh portable charger, and a white wooden bookshelf—from Austin to 3387 Adams Road, Apt 952, San Antonio, TX, USA 84338, and also update his default address to match, to ensure future deliveries go to the correct location. Later, you will check the order details again and proceed to cancel the order because it was placed by mistake and is no longer needed. After that, you would like to explore the product catalog, specifically reviewing the details of the Action Camera, which comes in various options including 4K and 5K resolution, waterproof and non-waterproof models, in black and silver colors, to consider a potential future purchase. You prefer the refund for the canceled order to be processed back to the original payment method, the credit card used for the purchase.\n\nUse lucas.silva5146@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1814268', 'address1': '3387 Adams Road', 'address2': 'Apt 952', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '84338'}),
            Action(name='modify_user_address', kwargs={'user_id': 'lucas_silva_7435', 'address1': '3387 Adams Road', 'address2': 'Apt 952', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '84338'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1814268'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1814268', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are Fatima Li (email: fatima.li1185@example.com) and you have two pending orders. You want to change the payment method for your order containing a Skateboard and an Espresso Machine from PayPal to your Visa card ending in 1373 because you prefer to use your credit card for this purchase. Later, you would like to update the shipping address for your order containing a Gaming Mouse and a Laptop to 4308 Washington Boulevard, Unit 840, Houston, TX, USA 78213, and you also want your default address to be updated to this new Houston address for future orders. After that, you would like to browse the product catalog and learn more about the Laptop product, particularly interested in variants with different screen sizes, processors, and storage options, as you are considering future purchases and want to understand available configurations.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8005719', 'payment_method_id': 'credit_card_2713802'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3510092', 'address1': '4308 Washington Boulevard', 'address2': 'Unit 840', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '78213'}),
            Action(name='modify_user_address', kwargs={'user_id': 'fatima_li_5040', 'address1': '4308 Washington Boulevard', 'address2': 'Unit 840', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '78213'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.ito3790@example.com',
        instruction="You are Emma Ito, with email emma.ito3790@example.com, and you have a pending order for a blue stainless steel 1000ml Water Bottle. You want to change the payment method for this order from PayPal to your Visa card ending in 3660 because you prefer using your credit card for this purchase. You also want to update the shipping address for this order to 4214 Washington Boulevard, Unit 551, Fort Worth, TX, USA 53362, and update your default address to the same, as you have moved and need all future deliveries sent to this new location. After making these changes, you would like to browse the store's full catalog of product types to explore other available items, and you specifically want to view the details of the Water Bottle you ordered to better understand its features and available variants.\n\nUse emma.ito3790@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8664580'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8664580', 'payment_method_id': 'credit_card_8058445'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8664580', 'address1': '4214 Washington Boulevard', 'address2': 'Unit 551', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '53362'}),
            Action(name='modify_user_address', kwargs={'user_id': 'emma_ito_4529', 'address1': '4214 Washington Boulevard', 'address2': 'Unit 551', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '53362'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.sanchez6360@example.com',
        instruction='You are assisting Ethan Sanchez (email: ethan.sanchez6360@example.com). You want to update the shipping address for a pending order containing an E-Reader, Water Bottle, Luggage Set, Laptop, and Grill to 3289 Jackson Street, Suite 382, Chicago, IL, USA 55494, because the original New York address is no longer valid. You also want to update your default address to this new Chicago address for future orders. For a delivered order that included a gold Smart Watch with silicone band and a Dumbbell Set with urethane coating, you would like to return the Smart Watch because it does not meet your expectations, and exchange the urethane-coated Dumbbell Set (30-50 lbs, fixed) for the same weight and type but with iron material instead, because you prefer the durability and feel of iron. You prefer any refund or charge adjustment to be processed using your PayPal account on file.\n\nUse ethan.sanchez6360@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9102111', 'address1': '3289 Jackson Street', 'address2': 'Suite 382', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '55494'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_sanchez_2952', 'address1': '3289 Jackson Street', 'address2': 'Suite 382', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '55494'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9250394', 'item_ids': ['2681513500'], 'payment_method_id': 'paypal_3574041'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9102111'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9250394', 'item_ids': ['7159180318'], 'new_item_ids': ['3333391894'], 'payment_method_id': 'paypal_3574041'}),
            Action(name='get_product_details', kwargs={'product_id': '7233192239'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are assisting James Martin (email: james.martin9857@example.com) with his pending order originally shipped to San Diego. You want to update the shipping address to 2977 Madison Drive, Suite 550, Boston, MA, USA 95650 because he has relocated temporarily. You prefer to change the payment method from PayPal to your Mastercard ending in 2067 for better rewards and expense tracking, and you want any price difference from the item exchange to be processed using the same card. You would like to exchange the red XXL cotton crew neck T-shirt for the blue M version because the original size is too large and you prefer the color blue for everyday wear. Later, after the order modifications, you would like to explore the full range of product types offered, particularly interested in reviewing all available options for the T-Shirt product to consider future purchases.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '2977 Madison Drive', 'address2': 'Suite 550', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '95650'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3043531', 'payment_method_id': 'credit_card_6932154'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3043531', 'item_ids': ['9354168549'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'credit_card_6932154'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3043531', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting Fatima Li (email: fatima.li1185@example.com) with her pending order originally shipped to Washington, DC. You want to first update the shipping address to 6468 Elm Street, Unit 141, Philadelphia, PA, USA 38822, so the package reaches her new location. Then, you prefer to change the payment method from PayPal to her Visa card ending in 1373 for better expense tracking. After that, you would like to upgrade the skateboard in the order from maple to bamboo material while keeping the same 31-inch size and graphic design, because you prefer the lighter and more sustainable bamboo deck. However, after reconsidering, you have decided to cancel the entire order as you no longer wish to proceed with the purchase. Separately, you want to explore the full range of product types available, particularly focusing on the Skateboard line, to evaluate future purchase options based on material, size, and design preferences.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8005719', 'address1': '6468 Elm Street', 'address2': 'Unit 141', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '38822'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8005719', 'payment_method_id': 'credit_card_2713802'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8005719', 'item_ids': ['5120532699'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'credit_card_2713802'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8005719', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are assisting Liam Thomas, whose email is liam.thomas9081@example.com. You want to update the shipping address for his pending order—which includes a bamboo graphic skateboard, a 2-piece black softshell luggage set, and a 20000mAh blue wireless portable charger—to 3986 Main Street, Unit 492, Chicago, IL, USA 80050, because he has relocated. After that, you would like to change the payment method from PayPal to the Visa card ending in 3194 for future charges, as it is his preferred payment option. Later, you want to exchange the 31 inch bamboo graphic skateboard for the 28 inch version with the same bamboo and graphic design, because it better suits his carrying and riding needs. You prefer the price difference from the exchange to be refunded to the original PayPal account used for purchase.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3295833', 'address1': '3986 Main Street', 'address2': 'Unit 492', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '80050'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3295833'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3295833', 'payment_method_id': 'credit_card_3261838'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3295833', 'item_ids': ['5312063289'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'paypal_3650980'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, and your email is olivia.ito5204@example.com. You want to update the shipping address for your pending order (containing a gaming mouse, patio umbrella, and hiking boots) to 3507 Park Drive, Suite 513, New York, NY, USA 31984 because you will be relocating temporarily. You would like to change the payment method from your Mastercard ending in 9182 to your PayPal account for better purchase protection and budget tracking. Additionally, you prefer a white wireless gaming mouse over the current black wired one because you want a cleaner aesthetic and a clutter-free setup on your desk. You would like all these changes confirmed before the order ships.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '3507 Park Drive', 'address2': 'Suite 513', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '31984'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5442520', 'item_ids': ['3330317167'], 'new_item_ids': ['8896479688'], 'payment_method_id': 'paypal_8049766'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.martin1284@example.com',
        instruction="You are assisting Fatima Martin (email: fatima.martin1284@example.com). You want to explore the available T-Shirt options, which include various colors (blue, purple, red, black), sizes (S to XXL), materials (cotton or polyester), and styles (crew neck or v-neck), because she is interested in browsing current offerings. Later, you would like to cancel the pending order placed in San Diego containing sunglasses with silver frames and blue non-polarized lenses, a blue leather office chair without armrests, and a 30ml men's fresh-scented perfume, because it is no longer needed. You prefer the cancellation to proceed with no replacement or refund action at this time.\n\nUse fatima.martin1284@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3376947'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3376947', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.martin4637@example.com',
        instruction='You are Mei Martin, with email mei.martin4637@example.com, and you have a pending order that includes a small green polyester backpack with a camera compartment. You want to change this backpack to a larger black nylon one with a camera compartment because you prefer more space and a durable, sleek design. You prefer to use your PayPal account for any price difference. Later, you would like to update the shipping address for this order to 9226 Adams Road, Floor 801, Jacksonville, FL, USA 39352, and also set this as your new default address for future orders. After that, you would like to browse the full list of product types offered, and then get detailed information about the Backpack product to explore options for future purchases.\n\nUse mei.martin4637@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7017301'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7017301', 'item_ids': ['9851293632'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'paypal_2299608'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7017301', 'address1': '9226 Adams Road', 'address2': 'Floor 801', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '39352'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mei_martin_4260', 'address1': '9226 Adams Road', 'address2': 'Floor 801', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '39352'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.lopez8943@example.com',
        instruction='You are Ethan Lopez, customer with email ethan.lopez8943@example.com, who has multiple pending orders. You want to modify the Dumbbell Set in one of your pending orders by switching from the adjustable version to the fixed variant, because you prefer a more stable setup while keeping the same 5-25 lbs weight range and rubber material for durability and comfort. Later, you would like to update the shipping address for a different pending order to 7604 Pine Avenue, Unit 426, San Jose, CA, USA 44416, and also update your default profile address to this new location in San Jose, because you have recently relocated and want all future deliveries to go to your new home. After that, you would like to browse the full product catalog to explore available items, and then get detailed information about the Dumbbell Set product you modified, because you are interested in understanding its full range of options and features. You prefer to use your Mastercard ending in 1020 for any price difference associated with the item change.\n\nUse ethan.lopez8943@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6779827'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6779827', 'item_ids': ['7896397433'], 'new_item_ids': ['8068777068'], 'payment_method_id': 'credit_card_9789590'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6426438', 'address1': '7604 Pine Avenue', 'address2': 'Unit 426', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '44416'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_lopez_6291', 'address1': '7604 Pine Avenue', 'address2': 'Unit 426', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '44416'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7233192239'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.thomas3069@example.com',
        instruction='You are Sofia Thomas, with email sofia.thomas3069@example.com. You want to update the shipping address for your pending order containing Wireless Earbuds, a Vacuum Cleaner, an Electric Toothbrush, and a Portable Charger to 2368 Main Street, Suite 688, Jacksonville, FL, USA 20769 because it was sent to the wrong location. You also want to return the red XXL cotton crew neck T-shirt from your delivered order because it is too large, and you prefer the refund to be processed back to your PayPal account. Later, you will cancel your other pending order that includes a bagless upright vacuum with HEPA filter and an adjustable dumbbell set because it was placed by mistake. After that, you would like to explore available T-shirt options, particularly interested in different colors, sizes, and styles such as crew neck or v-neck, made of cotton or polyester, to find a better fit and look.\n\nUse sofia.thomas3069@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7619352', 'address1': '2368 Main Street', 'address2': 'Suite 688', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '20769'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7619352'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3388163', 'item_ids': ['9354168549'], 'payment_method_id': 'paypal_5334408'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3388163', 'item_ids': ['9354168549'], 'new_item_ids': ['9354168549'], 'payment_method_id': 'paypal_5334408'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2297866', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction="You are assisting a customer who initially expressed interest in learning about Running Shoes available in the catalog. You want to provide information about the Running Shoes product line to support their browsing intent. Later, you are asked to look up the customer's pending order containing a black silicone-band Smart Watch with AMOLED display and a gold 128GB Smartphone with 4GB RAM and a 5.8-inch screen, originally shipped to Columbus, OH. You first want to update the shipping address for this order to 1804 Main Street, Suite 232, Oklahoma City, OK, USA 72081, because the customer needs it delivered to a different location. After that, you would like to cancel the entire order, as the customer no longer needs the items. The customer prefers the refund to be processed back to the original payment method, which was a gift card.\n\nUse ethan.thomas7730@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6938111410'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '8571 Park Drive', 'address2': 'Apt 309', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '83277'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.thomas3069@example.com',
        instruction='You are Sofia Thomas, with email sofia.thomas3069@example.com. You want to update the shipping address for your pending order containing wireless earbuds, a vacuum cleaner, and an electric toothbrush to 627 Main Street, Floor 972, Portland, OR, USA 36708, because it needs to be delivered to a new location. You also want your default address updated to this same new address for future orders. Later, you will cancel your other pending order that includes a bagless upright vacuum cleaner with a HEPA filter and an adjustable dumbbell set, because you no longer need those items. After that, you would like to exchange a red XXL cotton crew neck T-shirt from your delivered order for a blue M cotton crew neck T-shirt, because the original size and color do not fit your current needs. You prefer any price adjustment for the exchange to be processed using your PayPal account.\n\nUse sofia.thomas3069@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7619352', 'address1': '627 Main Street', 'address2': 'Floor 972', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '36708'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_thomas_1518', 'address1': '627 Main Street', 'address2': 'Floor 972', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '36708'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2297866', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3388163'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3388163', 'item_ids': ['9354168549'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_5334408'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah.martin8712@example.com',
        instruction='You are Noah Martin (email: noah.martin8712@example.com). You initially want to update the shipping address for your pending order (containing a Vacuum Cleaner, T-Shirt, and Laptop) to 1772 Madison Drive, Suite 505, Fort Worth, TX, USA 66442, because you have moved. You also want your default address updated to the same, for consistency across future orders. Later, you decide to cancel that pending order entirely because your needs have changed and you no longer require the items. After that, you want to check the status of your delivered order (containing a Mechanical Keyboard, Skateboard, Electric Kettle, and Wall Clock), which is confirmed delivered. You would like to exchange the 1.5L plastic Electric Kettle (currently silver) for the same model in black, because you prefer the color to match your kitchen appliances. You prefer to use your PayPal account for any price difference in the exchange.\n\nUse noah.martin8712@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7594624', 'address1': '1772 Madison Drive', 'address2': 'Suite 505', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '66442'}),
            Action(name='modify_user_address', kwargs={'user_id': 'noah_martin_5764', 'address1': '1772 Madison Drive', 'address2': 'Suite 505', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '66442'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7594624', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1971958'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1971958', 'item_ids': ['9624127908'], 'new_item_ids': ['5428723833'], 'payment_method_id': 'paypal_7383471'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.lee3013@example.com',
        instruction='You are to update the shipping address for the pending order containing Headphones (red, wired, in-ear), Hiking Boots (size 12, synthetic, waterproof), a 750ml blue stainless steel Water Bottle, a 4-cup stainless steel drip Coffee Maker with auto shutoff, and a black silicone-banded Smart Watch with AMOLED display, from San Antonio, TX to 1892 Jefferson Avenue, Floor 432, Seattle, WA, USA 53556, because the customer has relocated temporarily. After updating, you want confirmation that the address change was successfully applied. Later, you would like to initiate a return for the Hiking Boots (size 10, leather, not waterproof) from the delivered order that included an Espresso Machine and an Electric Kettle, because they do not fit properly, and you prefer a refund issued back to the original PayPal account used for the purchase.\n\nUse anya.lee3013@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3176007', 'address1': '1892 Jefferson Avenue', 'address2': 'Floor 432', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '53556'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3176007'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1335809', 'item_ids': ['2185126308'], 'payment_method_id': 'paypal_3728317'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.johansson9391@example.com',
        instruction='You are Isabella Johansson, and your email is isabella.johansson9391@example.com. You want to update the shipping address for your pending order—which includes a robotic cordless vacuum cleaner, a 20000mAh black wireless portable charger, an 8-inch e-reader, a 50ft black vinyl garden hose, and a blue fabric office chair—to 6715 Washington Boulevard, Unit 322, San Francisco, CA, USA 48731, because you need the items delivered to your new location. After updating the address, you would like confirmation that the change was successfully processed. Later, you would like to return the 31-inch plain bamboo skateboard from your delivered order, because it does not meet your expectations. You prefer the refund for the skateboard to be issued back to your PayPal account, as that was your original payment method.\n\nUse isabella.johansson9391@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2575533', 'address1': '6715 Washington Boulevard', 'address2': 'Unit 322', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '48731'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2575533'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3792453', 'item_ids': ['4293355847'], 'payment_method_id': 'paypal_3024827'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.davis6811@example.com',
        instruction='You are Mei Davis (mei.davis6811@example.com). You want to update the shipping address for your pending order containing a Gaming Mouse, Headphones, Air Purifier, Smart Thermostat, and Wireless Earbuds to 1020 Jefferson Avenue, Unit 50, Houston, TX, USA 46925, because you need it delivered to your new location. You also want your default address in your profile updated to the same, to ensure future orders go to this address. Later, you would like to return the 1000ml stainless steel blue Water Bottle from your delivered order that also included a Pet Bed, Office Chair, and Skateboard, because you no longer need it. You prefer the refund for this return to be issued back to your Mastercard ending in 1037, as it was the original payment method.\n\nUse mei.davis6811@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1267569'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1267569', 'address1': '1020 Jefferson Avenue', 'address2': 'Unit 50', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '46925'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mei_davis_8935', 'address1': '1020 Jefferson Avenue', 'address2': 'Unit 50', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '46925'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2890441', 'item_ids': ['2366567022'], 'payment_method_id': 'credit_card_1061405'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.nguyen1348@example.com',
        instruction='You are assisting Fatima Nguyen (email: fatima.nguyen1348@example.com). You want to update the shipping address for her pending order — which includes a white glass bookshelf, a black metal-band smart watch, a white desk lamp, and a 2K-resolution indoor security camera — from Columbus, Ohio to 6860 Washington Boulevard, Suite 201, Portland, OR, USA 16082, because she has moved. You also want to update her default address to this new Portland location for future orders. Later, you will initiate a return for a pair of hiking boots from her delivered order — they are size 10, made of synthetic material, and not waterproof, which was a key requirement for her outdoor use. You would like the refund for the boots to be processed back to her PayPal account, as that was the original payment method and remains her preferred option.\n\nUse fatima.nguyen1348@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8808563'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8808563', 'address1': '6860 Washington Boulevard', 'address2': 'Suite 201', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '16082'}),
            Action(name='modify_user_address', kwargs={'user_id': 'fatima_nguyen_7539', 'address1': '6860 Washington Boulevard', 'address2': 'Suite 201', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '16082'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5256976', 'item_ids': ['4127323219'], 'payment_method_id': 'paypal_2613218'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.rossi2645@example.com',
        instruction='You are assisting Sofia Rossi (email: sofia.rossi2645@example.com), who has a pending order containing a unisex oriental-scent 30ml perfume, a bamboo 31-inch graphic-design skateboard, and two silver waterproof action cameras (one 5K and one 4K resolution). You want to update the shipping address for this order from Austin, TX to 6103 Cedar Road, Suite 824, San Jose, CA, USA 90147, as the original address is no longer valid. You prefer the payment method to remain the Mastercard ending in 3357, as it was used for the original purchase.\n\nUse sofia.rossi2645@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5918442', 'address1': '6103 Cedar Road', 'address2': 'Suite 824', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '90147'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.santos9082@example.com',
        instruction='You are assisting Ethan Santos (email: ethan.santos9082@example.com) with updates to his pending order. You want to change the shipping address from San Jose, CA to 7436 Elm Street, Suite 564, Seattle, WA, because he has moved to a new apartment. Later, you would like to update the payment method from PayPal to his Mastercard ending in 9443 for better rewards, as the order has not yet been processed and payment can still be adjusted.\n\nUse ethan.santos9082@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5320242', 'address1': '7436 Elm Street', 'address2': 'Suite 564', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '63944'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5320242', 'payment_method_id': 'credit_card_9784468'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.moore1031@example.com',
        instruction='You are browsing the full catalog of product types available, including items like Dumbbell Set, Office Chair, and Espresso Machine, to explore your options. You want to update the shipping address for your pending order—currently shipping to Dallas—to a new address in New York, specifically 5893 Pine Avenue, Unit 816, New York, NY, USA 68995, because you need the items delivered to a different location. Later, you would like to change the payment method for the same order from the current gift card to your Visa card ending in 4204, as you prefer to use your credit card for this purchase and have confirmed it is linked to your account.\n\nUse daiki.moore1031@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4843514', 'address1': '5893 Pine Avenue', 'address2': 'Unit 816', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '68995'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4843514', 'payment_method_id': 'credit_card_5613268'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.silva6295@example.com',
        instruction='You are daiki.silva6295@example.com, and you have a pending order for a red Bluetooth speaker with 10-hour battery life and water resistance. You want to update the shipping address from San Francisco to 3889 Park Drive, Suite 754, Chicago, IL, USA 51840, so the item can be delivered to your new location. Later, you decide to cancel the order entirely because you no longer need the speaker. You prefer the refund to be processed back to the original gift card used for purchase.\n\nUse daiki.silva6295@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7999678', 'address1': '3889 Park Drive', 'address2': 'Suite 754', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '51840'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7999678'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7999678', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.moore4245@example.com',
        instruction='You are raj.moore4245@example.com and want to update the shipping address for your pending order (with items including a brown polyester pet bed, a red stainless steel 1000ml water bottle, a blue Bluetooth speaker, a green 6mm PVC yoga mat, and a blue cycling helmet in size L) from Washington, DC to 3943 Adams Road, Apt 559, Boston, MA, USA 41453, because you will be traveling and want the package delivered to your temporary accommodation. You would like confirmation of the updated address. Later, you will want to cancel the same order entirely because you no longer need the items. You prefer the refund to be processed back to the original payment method, which was a gift card.\n\nUse raj.moore4245@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9929926', 'address1': '3943 Adams Road', 'address2': 'Apt 559', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '41453'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9929926'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9929926', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.muller2208@example.com',
        instruction='You are Omar Muller, with email omar.muller2208@example.com, and you want to update the shipping address for your pending order—which includes a small brown fleece pet bed, a 500-piece expert-level animal-themed jigsaw puzzle, and a black 1-cup drip coffee maker with timer—from Denver, CO to 8260 Jefferson Avenue, Unit 905, Columbus, OH, USA 68284 because the original address is no longer valid. After that, you would like to cancel the entire order because you made the purchase by mistake and no longer need the items. Later, you want to explore the product catalog to consider future purchases, specifically requesting information about the Action Camera, which comes in variants with 4K or 5K resolution, waterproof or non-waterproof options, and in black or silver colors, to evaluate which model best fits your needs.\n\nUse omar.muller2208@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8343509', 'address1': '8260 Jefferson Avenue', 'address2': 'Unit 905', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '68284'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8343509', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.johnson2279@example.com',
        instruction='You are Daiki Johnson, authenticated with email daiki.johnson2279@example.com. You want to update the shipping address for your pending order—which includes a glass tea kettle with 1-liter capacity currently set to ship to Jacksonville, FL—to 2048 Washington Boulevard, Apt 142, Dallas, TX, USA 49925, because you will be relocating temporarily. Later, you would like to cancel this order entirely because you no longer need the tea kettle. Separately, you are interested in exploring the available products and would like detailed information about the Laptop product, particularly variants such as the 15-inch space grey model with i7 processor and 1TB SSD, to evaluate options for a future purchase.\n\nUse daiki.johnson2279@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1436802', 'address1': '2048 Washington Boulevard', 'address2': 'Apt 142', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '49925'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1436802', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.moore8091@example.com',
        instruction='You are assisting Mia Moore (mia.moore8091@example.com) with her order for a white glass bookshelf (3 ft), another white glass bookshelf (4 ft), a bagged upright cordless vacuum cleaner, a gold silicone-band smart watch with LCD display, and a black electric toothbrush with low speed settings and AA batteries. You want to update the shipping address for this pending order to 565 Elm Street, Apt 289, Nashville, TN, USA 35555, because it was initially set to San Francisco. You also want to update her default address to this new Nashville address for future orders. Later, you will cancel the entire order because she no longer needs the items. The original payment was made using a gift card, so you prefer the refund to be issued back to the same gift card.\n\nUse mia.moore8091@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3130288', 'address1': '565 Elm Street', 'address2': 'Apt 289', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '35555'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mia_moore_8366', 'address1': '565 Elm Street', 'address2': 'Apt 289', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '35555'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3130288'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3130288', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.smith4465@example.com',
        instruction='You are Ava Smith (email: ava.smith4465@example.com). You want to update the shipping address for your pending order containing a gold Smart Watch with metal band and LCD display from Denver, CO to 6204 Park Drive, Floor 421, Nashville, TN, USA 99341 because you need it delivered to a new location. You also want your default address updated to the same Nashville address for future orders. Later, after the address update, you decided you no longer need the item, so you would like to cancel the order. You prefer the cancellation to be processed while the order is still pending, and since payment was made with a gift card, you expect the balance to be returned to the original payment method.\n\nUse ava.smith4465@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8328622', 'address1': '6204 Park Drive', 'address2': 'Floor 421', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '99341'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_smith_1453', 'address1': '6204 Park Drive', 'address2': 'Floor 421', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '99341'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8328622'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8328622', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.santos9082@example.com',
        instruction='You are assisting a customer with email ethan.santos9082@example.com who is interested in the Action Camera product and wants to understand the available variants before making a decision. You want to know which configurations are currently in stock, particularly those with 4K or higher resolution, waterproofing, and in black or silver colors, to evaluate suitability for outdoor use. Later, you will address a separate request regarding a pending order placed in San Jose, CA, for a bundle including a red 2-piece softshell luggage set, a black silicone-banded LCD smart watch, a blue large high-ventilation cycling helmet, a 2K indoor security camera with 160-degree field of view, and a 7-inch 128GB black tablet. For this order, you would like to change the payment method from PayPal to your Mastercard ending in 9443, as you prefer to use that card for tracking and rewards purposes.\n\nUse ethan.santos9082@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5320242'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5320242', 'payment_method_id': 'credit_card_9784468'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.li2787@example.com',
        instruction='You are assisting Raj Li (email: raj.li2787@example.com) with his pending order placed in Fort Worth, TX. You first want to explore the available product types in the store to understand what is offered. Then, for your pending order containing a 4 ft brown glass bookshelf, a 5 ft black glass bookshelf, a 750ml green stainless steel water bottle, and a large gas grill with rotisserie, you want to change the payment method from your Visa card ending in 3917 to your PayPal account, because you prefer using PayPal for this purchase. Later, you decide to cancel the entire order because you no longer need the items. You prefer the refund to be processed back to the original payment method, the Visa card ending in 3917.\n\nUse raj.li2787@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8967935', 'payment_method_id': 'paypal_2028062'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8967935', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.thomas7243@example.com',
        instruction='You are assisting mia.thomas7243@example.com with her pending order containing Hiking Boots in size 12, made of synthetic material with waterproof feature, along with a grey small nylon backpack with laptop compartment and a 1500-piece intermediate art-themed jigsaw puzzle. You want to verify the product details of the Hiking Boots to ensure accuracy before proceeding. Later, you would like to change the shipping address for this order from Chicago, IL to 6331 Park Drive, Suite 111, Denver, CO, USA 98658, because the delivery location has changed. After that, you would like to update your default address to the same Denver address for future orders, to ensure consistency in shipping. You prefer the order to remain on its current payment method, which is PayPal.\n\nUse mia.thomas7243@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5208989'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5208989', 'address1': '8037 Pine Avenue', 'address2': 'Suite 367', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '59877'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mia_thomas_4629', 'address1': '8037 Pine Avenue', 'address2': 'Suite 367', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '59877'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.patel5445@example.com',
        instruction="You are assisting a customer with email yara.patel5445@example.com who has a pending order containing over-ear wired black headphones, a portable gas grill, and a silicone-strapped black-dial wristwatch. You want to update the shipping address for this order to 8141 Madison Drive, Apt 415, Denver, CO, USA 99227 because the originally provided address in Fort Worth was incorrect. Later, you would like to update the customer's default address in their profile to the same Denver address to ensure future orders are delivered correctly. You prefer the payment method remain as the gift card used in the original transaction.\n\nUse yara.patel5445@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1068289'}),
            Action(name='get_product_details', kwargs={'product_id': '6992792935'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1068289', 'address1': '8141 Madison Drive', 'address2': 'Apt 415', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '99227'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yara_patel_8545', 'address1': '8141 Madison Drive', 'address2': 'Apt 415', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '99227'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.nguyen1348@example.com',
        instruction="You are assisting Fatima Nguyen (email: fatima.nguyen1348@example.com). You want to update the shipping address for a pending order containing a white glass bookshelf, a black metal-band smart watch, a white USB desk lamp, and a 2K indoor security camera to 1811 Oak Avenue, Floor 669, Austin, TX, USA 97485, because the original Columbus, OH address is no longer valid. Later, you would like to cancel this order entirely with the reason 'no longer needed', and you want confirmation that the order status is updated to cancelled. After that, you would like to return the non-waterproof synthetic hiking boots in size 10 from a delivered order, because they do not meet your outdoor needs, and you prefer the refund to be issued back to your PayPal account. Subsequently, you want to browse the full product catalog to explore available options, and you are particularly interested in the Hiking Boots product line to compare variants such as leather versus synthetic materials, waterproof options, and different sizes.\n\nUse fatima.nguyen1348@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8808563', 'address1': '1811 Oak Avenue', 'address2': 'Floor 669', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '97485'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8808563', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8808563'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5256976', 'item_ids': ['4127323219'], 'payment_method_id': 'paypal_2613218'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.sanchez6360@example.com',
        instruction='You are Ethan Sanchez, with email ethan.sanchez6360@example.com. You want to update the shipping address for your pending order (containing an E-Reader, Water Bottle, Luggage Set, Laptop, and Grill) to 9507 Lincoln Street, Apt 34, Seattle, WA, USA 84809 because you need it delivered to a new location. Later, you will cancel that order because you placed it by mistake. After that, you would like to confirm the cancellation status. Separately, you want to return the Dumbbell Set (30-50 lbs, urethane, fixed) from your delivered order and prefer the refund to be issued back to your gift card because that was your original payment method for another order and you wish to maintain balance. Finally, you would like to explore available product types in the store and get details about the Dumbbell Set product line to consider a potential replacement, possibly preferring different weight ranges or materials such as iron or adjustable options.\n\nUse ethan.sanchez6360@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9102111', 'address1': '9507 Lincoln Street', 'address2': 'Apt 34', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '84809'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9102111', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9102111'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9250394', 'item_ids': ['7159180318'], 'payment_method_id': 'gift_card_4817478'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7233192239'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.ito8974@example.com',
        instruction='You are assisting Amelia Ito (email: amelia.ito8974@example.com) with her pending order. You want to first review the details of her order placed in Seattle, which includes a navy Fleece Jacket in size XS with a full zipper, along with a Cycling Helmet, Makeup Kit, and Digital Camera. After confirming the contents, you would like to update the shipping address to 4270 Adams Road, Floor 605, Detroit, MI, USA 37477 for better delivery access. You also prefer to switch the payment method from your Mastercard ending in 7517 to your PayPal account for this order. Later, you would like to explore the full range of product types available in the store, including categories like Air Purifier, Backpack, Coffee Maker, Electric Kettle, Espresso Machine, Gaming Mouse, Luggage Set, Mechanical Keyboard, Office Chair, Smart Watch, Tablet, Vacuum Cleaner, and Yoga Mat, to consider future purchases.\n\nUse amelia.ito8974@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3883329'}),
            Action(name='get_product_details', kwargs={'product_id': '8560156827'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3883329', 'address1': '4270 Adams Road', 'address2': 'Floor 605', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '37477'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3883329', 'payment_method_id': 'paypal_2767694'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.martin1284@example.com',
        instruction="You are assisting Fatima Martin (email: fatima.martin1284@example.com). You want to first explore the full range of available product types in the catalog to understand current offerings. Then, you want to update the shipping address for your pending order—containing a pair of silver plastic sunglasses with blue non-polarized lenses, a blue leather office chair without armrests, and a 30ml men's fresh-scented perfume—to a new location in Chicago, specifically 1565 Elm Street, Suite 272, Chicago, IL, USA 61532, to better suit your current needs. Later, after the address update, you decide to cancel the same order because your circumstances have changed and you no longer require these items. You prefer the refund to be processed back to the original payment method, the credit card ending in 6513839.\n\nUse fatima.martin1284@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3376947', 'address1': '1565 Elm Street', 'address2': 'Suite 272', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '61532'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3376947'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3376947', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.thomas7243@example.com',
        instruction='You are a customer with email mia.thomas7243@example.com who wants to first browse the product catalog. You then want to update the shipping address for your pending order—which includes a pair of size 12 synthetic waterproof hiking boots, a small grey nylon backpack with a laptop compartment, and a 1500-piece intermediate-level art-themed jigsaw puzzle—from Chicago, IL to 2078 Jackson Street, Apt 562, Charlotte, NC, USA 33787. Later, after reviewing the order status, you would like to cancel the entire order because you no longer need the items. You prefer the refund to be processed back to the original payment method, PayPal.\n\nUse mia.thomas7243@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5208989', 'address1': '2078 Jackson Street', 'address2': 'Apt 562', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '33787'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5208989'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5208989', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.lopez6910@example.com',
        instruction='You are Evelyn Lopez (email: evelyn.lopez6910@example.com). You want to update the shipping address for your pending order containing a blue cycling helmet (size S) to 4914 Adams Road, Suite 31, Philadelphia, PA, USA 82541 because you have moved and the original address in San Diego is no longer valid. You also want to explore the full range of available products in the catalog to consider future purchases, as you were curious about what other items are offered. Later, you decided to cancel your other pending order that includes white leather running shoes (size 10) and a medium electric grill with a side burner, because it was placed by mistake and you no longer need those items. You prefer any refund from the canceled order to be returned to the original payment method, which is your credit card.\n\nUse evelyn.lopez6910@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1890669', 'address1': '4914 Adams Road', 'address2': 'Suite 31', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '82541'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1890669'}),
            Action(name='get_product_details', kwargs={'product_id': '7765186836'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3007862', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.thomas3069@example.com',
        instruction='You are assisting Sofia Thomas (sofia.thomas3069@example.com) with two sequential requests. First, you want to update the shipping address for her pending order containing Wireless Earbuds, a Vacuum Cleaner, an Electric Toothbrush, and a Portable Charger to 7178 Elm Street, Unit 688, Seattle, WA, USA 77485, because she has moved. You also want her default address updated to this new Seattle address for future orders. Later, you would like to exchange the red XXL cotton crew neck T-Shirt from her delivered order—which also included a different pair of Wireless Earbuds, an Action Camera, and a Mechanical Keyboard—for a blue medium cotton crew neck T-Shirt, because the original size and color do not fit her preferences. You prefer the exchange to be processed using her PayPal account for any price adjustment, as that was her original payment method for both orders.\n\nUse sofia.thomas3069@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7619352', 'address1': '7178 Elm Street', 'address2': 'Unit 688', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '77485'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_thomas_1518', 'address1': '7178 Elm Street', 'address2': 'Unit 688', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '77485'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7619352', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3388163'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3388163', 'item_ids': ['9354168549'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_5334408'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3388163', 'item_ids': ['9354168549'], 'payment_method_id': 'paypal_5334408'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.ahmed2006@example.com',
        instruction='You are assisting Evelyn Ahmed (email: evelyn.ahmed2006@example.com). You want to update the shipping address for her pending order—containing a pair of leather, size 10, waterproof hiking boots, a black desk lamp, a 500ml black plastic water bottle, a wooden black bookshelf, and a 1000-piece beginner jigsaw puzzle—from Charlotte to 2754 Jackson Street, Floor 82, San Jose, CA, USA 40502, because she has relocated. You also want your default address updated to this new San Jose address for future orders. You are curious about the hiking boots in your order and would like confirmation that they are made of leather, sized 10, and waterproof, which aligns with your outdoor needs. Later, after considering your current situation, you decide you no longer need the items and would like the entire order canceled, as your plans have changed.\n\nUse evelyn.ahmed2006@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1416704', 'address1': '2754 Jackson Street', 'address2': 'Floor 82', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '40502'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_ahmed_3960', 'address1': '2754 Jackson Street', 'address2': 'Floor 82', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '40502'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1416704', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.thomas1454@example.com',
        instruction='You are assisting Harper Thomas (harper.thomas1454@example.com) with her pending order originally placed for a green 6mm Yoga Mat and a Smart Thermostat. You want to update the shipping address to 943 Maple Drive, Suite 356, Chicago, IL, USA 60621, because it was initially incorrect. You would like to change the payment method for the order to your Mastercard ending in 7287 for better rewards. You also prefer the blue 4mm Yoga Mat over the green 6mm one because you find the thinner, blue version more comfortable and stylish, and you want to use your Visa ending in 5768 for any price adjustment related to this exchange. Later, after reconsidering your needs, you decide to cancel the entire order because you no longer require the items. After cancellation, you want confirmation of the updated order status to ensure it has been fully canceled. You would also like to review the available options for the Yoga Mat product line to understand what variants are currently offered, particularly in terms of color, thickness, and material. After that, you want a full list of all product types available in the store so you can explore future purchases across categories such as electronics, fitness, home, and outdoor gear.\n\nUse harper.thomas1454@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7425646', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7425646', 'payment_method_id': 'credit_card_1199336'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7425646', 'item_ids': ['7510236436'], 'new_item_ids': ['5586947715'], 'payment_method_id': 'credit_card_1283450'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7425646', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7425646'}),
            Action(name='get_product_details', kwargs={'product_id': '4635925001'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.moore8091@example.com',
        instruction='You are Mia Moore (email: mia.moore8091@example.com) with a pending order containing multiple items including two bookshelves. You want to update the shipping address from San Francisco to 139 Park Drive, Floor 264, Austin, TX, USA 41280 because you need the delivery redirected. You prefer to switch the payment method from your gift card to your Mastercard ending in 2992 for better tracking and refund flexibility. You also want to upgrade one of the 3 ft white glass bookshelves to the 5 ft white glass version because you need more storage space and prefer the taller design. Later, you decide to cancel the entire order because you no longer need the items. You would like to review the details of the original order and the specific product information for the white glass bookshelf to understand what was ordered. After that, you want to browse the full list of product types available in the store to explore other options for future purchases.\n\nUse mia.moore8091@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3130288', 'address1': '139 Park Drive', 'address2': 'Floor 264', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '41280'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3130288', 'payment_method_id': 'credit_card_2641784'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3130288', 'item_ids': ['2989722512'], 'new_item_ids': ['8895454203'], 'payment_method_id': 'credit_card_2641784'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3130288', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3130288'}),
            Action(name='get_product_details', kwargs={'product_id': '8600330539'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting Fatima Li (email: fatima.li1185@example.com) with her pending order containing a skateboard and an espresso machine, originally paid with PayPal. You want to update the payment method to her Visa card ending in 1373 because she prefers to use that card for this purchase. Later, you will cancel the entire order because she no longer needs the items.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8005719', 'payment_method_id': 'credit_card_2713802'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8005719', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.gonzalez1317@example.com',
        instruction='You are assisting Isabella Gonzalez, who is reachable at isabella.gonzalez1317@example.com. You want to update the payment method for her pending order in Fort Worth from her Visa card ending in 4920 to her Mastercard ending in 9364, because she prefers to use that card for this purchase. Later, you will cancel the same order, which includes a 28-inch maple skateboard, an A4 soft-cover notebook, and a silver 2-piece hardshell luggage set, because she no longer needs the items.\n\nUse isabella.gonzalez1317@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1258841'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1258841', 'payment_method_id': 'credit_card_9878778'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1258841', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.silva3776@example.com',
        instruction='You are assisting Olivia Silva (email: olivia.silva3776@example.com) with her pending order. You want to update the shipping address from Jacksonville, FL to 6071 Washington Boulevard, Floor 825, Las Vegas, NV, USA 37278 because she needs the order delivered to a new location. Later, you would like to change the Yoga Mat in the order from the green, 6mm thick natural rubber version to the blue, 4mm thick PVC version because she prefers a thinner, more portable mat with a smoother surface. You prefer the price difference to be handled using her PayPal account, which is already on file.\n\nUse olivia.silva3776@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6940125', 'address1': '6071 Washington Boulevard', 'address2': 'Floor 825', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '37278'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6940125'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6940125', 'item_ids': ['6195938807'], 'new_item_ids': ['5586947715'], 'payment_method_id': 'paypal_9379149'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.ito3877@example.com',
        instruction='You are Sofia Ito (sofia.ito3877@example.com) with a pending order in Philadelphia. You want to update the shipping address to 2173 Lincoln Street, Unit 706, Philadelphia, PA, USA 58272, because the original address is incorrect. Later, you would like to exchange the Smart Watch with a black leather band for the gold leather band AMOLED model, as you prefer the gold finish for its more elegant look. You prefer to use your PayPal account to handle any price difference for the exchange.\n\nUse sofia.ito3877@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1514731', 'address1': '2173 Lincoln Street', 'address2': 'Unit 706', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '58272'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1514731'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1514731', 'item_ids': ['9320099340'], 'new_item_ids': ['5694328282'], 'payment_method_id': 'paypal_6882355'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li7352@example.com',
        instruction='You are Sofia Li (sofia.li7352@example.com), and you initially wanted to explore the full range of product types offered, including categories like Air Purifier, Digital Camera, Hiking Boots, and Yoga Mat, to better understand available options. You then wanted to update the shipping address for your pending order—containing an Air Purifier for medium rooms with HEPA filter, Hiking Boots in size 7 made of synthetic material, a 34-inch plastic-deck Skateboard, and a pink natural rubber Yoga Mat—to 9459 Cedar Road, Unit 383, Chicago, IL, USA 25786, because you needed it delivered to a new location. You also preferred to change the payment method for this order from your Visa card ending in 6791 to your PayPal account for greater convenience and payment flexibility. Later, you decided to cancel this entire order due to changed plans. Separately, you would like to return the Digital Camera with 24MP resolution and 3x zoom from your earlier delivered order, as it no longer fits your needs, and you prefer the refund to be issued to your Mastercard ending in 8484, the card originally used for that purchase.\n\nUse sofia.li7352@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8855135', 'address1': '9459 Cedar Road', 'address2': 'Unit 383', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '25786'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8855135', 'payment_method_id': 'paypal_8194385'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8855135', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4689314'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W4689314', 'item_ids': ['5996159312'], 'payment_method_id': 'credit_card_8105988'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are assisting Fatima Wilson (email: fatima.wilson5906@example.com). You want to update the shipping address for her pending order, which includes a blue leather office chair and a large gas grill with rotisserie, to 2315 Park Drive, Floor 214, Chicago, IL, USA 25044, because she needs it delivered to a new location. Later, you would like to change the payment method for this order to PayPal, as she prefers to use that method for this purchase. After that, you would like to return the 1L silver glass electric kettle from her earlier delivered order, because it does not meet her expectations, and you prefer the refund to be processed back to her original PayPal account for consistency with her payment preference.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1443906', 'address1': '2315 Park Drive', 'address2': 'Floor 214', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '25044'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1443906', 'payment_method_id': 'paypal_7685859'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1443906', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7990410'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7990410', 'item_ids': ['1240311797'], 'payment_method_id': 'paypal_7685859'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are assisting James Martin (email: james.martin9857@example.com). You want to update the shipping address for a pending order containing a black nylon small backpack with laptop compartment, an adjustable 5-25 lbs dumbbell set, and hiking boots size 10 to 594 Lincoln Street, Apt 794, Houston, TX, USA 74104, because he has moved. Later, you would like to cancel this same order because it was placed by mistake. After that, for another pending order containing a red cotton XXL crew neck T-shirt, a stainless steel smart thermostat compatible with Amazon Alexa, a white-dial silicone strap wristwatch, a 100ft rubber garden hose, and a green polyester small camera backpack, you prefer to change the payment method from PayPal to a Visa card ending in 1826 for better rewards.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3529525', 'address1': '594 Lincoln Street', 'address2': 'Apt 794', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '74104'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3529525', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3043531', 'payment_method_id': 'credit_card_7083997'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.patel3765@example.com',
        instruction='You are Lei Patel, with email lei.patel3765@example.com, and you want to update the shipping address for your pending order—which includes a black electric toothbrush, a 34-inch graphic skateboard, a 30-50 lbs rubber dumbbell set, and red wired in-ear headphones—from Seattle to your new address: 2061 Main Street, Unit 84, Chicago, IL, USA 83864, because you recently moved and want to ensure the order reaches the correct location. After updating the address, you would like to browse the current product catalog to explore what items are available, with the intention of considering something new to add to a future order.\n\nUse lei.patel3765@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4172216', 'address1': '2061 Main Street', 'address2': 'Unit 84', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '83864'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.gonzalez4478@example.com',
        instruction='You are assisting Liam Gonzalez (email: liam.gonzalez4478@example.com) with his pending order. You want to update the shipping address to 7748 Jefferson Avenue, Apt 997, New York, NY, USA 25763, because the original Austin address was incorrect. You also prefer to change the payment method from PayPal to your Mastercard ending in 4422 for better record-keeping and personal budget tracking. After confirming the updated order details, you would like to cancel the entire order, as it was placed by mistake and you no longer need the items, which include a black 500ml glass water bottle, a blue fabric office chair with adjustable armrests, a 2K-resolution indoor security camera with 130-degree field of view, a robotic bagless vacuum cleaner with pet hair removal, and gray leather sneakers in size 10.\n\nUse liam.gonzalez4478@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8747662', 'address1': '7748 Jefferson Avenue', 'address2': 'Apt 997', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '25763'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8747662', 'payment_method_id': 'credit_card_6341155'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8747662'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8747662', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are assisting Fatima Wilson (email: fatima.wilson5906@example.com) with her pending order containing a blue leather office chair and a large gas grill with rotisserie. You want to update the shipping address from Austin to 3030 Main Street, Suite 539, Phoenix, AZ, USA 13861, because the original address is no longer valid. After that, you would like to change the payment method from the Mastercard ending in 9779 to your PayPal account for better transaction tracking and personal budgeting. Once the updates are confirmed, you intend to cancel the entire order because you realized it was placed by mistake and you no longer need the items.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1443906', 'address1': '3030 Main Street', 'address2': 'Suite 539', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '13861'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1443906', 'payment_method_id': 'paypal_7685859'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1443906'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1443906', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are assisting Omar Silva (email: omar.silva4147@example.com) with his pending order containing a 2000-piece fantasy-themed puzzle, a 2000-piece animals-themed puzzle, a brown wooden bookshelf, a silver 4K action camera, and polarized sunglasses with black frame and green lens. You want to update the shipping address from San Diego to 7974 Lincoln Street, Floor 541, San Francisco, CA, USA 43071 because it was entered incorrectly. You also prefer to change the payment method from the gift card to your Mastercard ending in 5859 for better tracking and flexibility. Later, after making these updates, you decide to cancel the entire order because you realized it was placed by mistake and you no longer need the items.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9728773', 'address1': '7974 Lincoln Street', 'address2': 'Floor 541', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '43071'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9728773', 'payment_method_id': 'credit_card_5322562'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting a customer with email sophia.patel9841@example.com regarding her pending order. You want to first update the shipping address to 1617 Pine Avenue, Floor 942, San Jose, CA, USA 48198 for the order containing a men's oriental-scented 100ml perfume, a glass tea kettle with 1.5-liter capacity, a black 1L glass electric kettle, and gray canvas sneakers in size 8. After that, you would like to change the payment method to the Mastercard ending in 1639. Later, you decided you no longer need the items and would like to cancel the entire order.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7905419', 'address1': '1617 Pine Avenue', 'address2': 'Floor 942', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '48198'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7905419', 'payment_method_id': 'credit_card_6419343'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7905419', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.lopez6910@example.com',
        instruction='You are Evelyn Lopez, email evelyn.lopez6910@example.com, and you want to exchange the black cycling helmet (size S) from your delivered order for the red one (size S), because you prefer the red color while keeping the same fit and ventilation. You prefer to use your Mastercard ending in 8951 for any price difference. Later, you want to update the shipping address for your pending order containing a blue cycling helmet to 3788 Lincoln Street, Unit 811, San Jose, CA, USA 35235, because you need it delivered to a different location. After that, you would like to change the size 10 white running shoes in another pending order to size 8 in red, because they are for a gift and the original size was too large. You also prefer to use your Mastercard ending in 8951 for any price adjustment. Subsequently, you decide to cancel that same order because you realize it was placed by mistake and no longer wish to proceed with it.\n\nUse evelyn.lopez6910@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1890669', 'address1': '3788 Lincoln Street', 'address2': 'Unit 811', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '35235'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_lopez_5487', 'address1': '3788 Lincoln Street', 'address2': 'Unit 811', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '35235'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1355800', 'item_ids': ['5537798301'], 'new_item_ids': ['3358616356'], 'payment_method_id': 'credit_card_3566337'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3007862'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3007862', 'item_ids': ['1775591963'], 'new_item_ids': ['4153505238'], 'payment_method_id': 'credit_card_3566337'}),
            Action(name='get_product_details', kwargs={'product_id': '6938111410'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3007862', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.lopez8943@example.com',
        instruction='You are assisting Ethan Lopez (email: ethan.lopez8943@example.com). You want to update the shipping address for a pending order containing a cycling helmet, a T-shirt, hiking boots, a digital camera, and a smartphone to 3904 Adams Road, Unit 5, Chicago, IL, USA 85696, and also update your default address to this same address because you have relocated. You would like to exchange a grey medium polyester backpack with laptop compartment from a delivered order for a grey large backpack with hydration compartment, as you need more utility for outdoor use, and you prefer to use your Mastercard ending in 1020 for any price difference. After reviewing the order, you want to change the red large cotton v-neck T-shirt in the pending order to a purple XL cotton crew neck T-shirt, because you prefer the color and fit, and you prefer to use your Mastercard ending in 1020 for any price adjustment. Later, after making these changes, you decide you no longer need the items and would like to cancel the entire pending order.\n\nUse ethan.lopez8943@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8073920', 'address1': '3904 Adams Road', 'address2': 'Unit 5', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '85696'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_lopez_6291', 'address1': '3904 Adams Road', 'address2': 'Unit 5', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '85696'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8632528', 'item_ids': ['5917587651'], 'new_item_ids': ['6309044598'], 'payment_method_id': 'credit_card_9789590'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8073920'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8073920', 'item_ids': ['3234800602'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'credit_card_9789590'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8073920', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.kovacs4505@example.com',
        instruction='You are assisting Sofia Kovacs, who is authenticated via email sofia.kovacs4505@example.com. You want to return the black espresso coffee maker with a 4-cup capacity from your delivered order, preferring the refund to be issued back to your PayPal account because that was the original payment method. Later, you would like to update the shipping address for your pending order containing two skateboards (one 28-inch maple and one 34-inch plastic), polarized sunglasses with green lenses, and a 750ml black stainless steel water bottle to your new location: 8343 Park Drive, Unit 855, Houston, TX, USA 89165, as you have moved from Philadelphia. After that, you would like to cancel your other pending order that includes a black electric toothbrush with high speed settings and a white 5000mAh portable charger because it is no longer needed.\n\nUse sofia.kovacs4505@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7736983'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7736983', 'item_ids': ['5952720925'], 'payment_method_id': 'paypal_6840891'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9869592', 'address1': '8343 Park Drive', 'address2': 'Unit 855', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '89165'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5765741', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.taylor6118@example.com',
        instruction='You are assisting Yusuf Taylor (email: yusuf.taylor6118@example.com). You want to return the black Electric Toothbrush with low speed settings and the red small Cycling Helmet from your delivered order, because you changed your mind, and you prefer the refund to be issued to your original payment method, which is your Visa card ending in 4012. Later, you intended to update the shipping address for your pending order containing the white USB-powered high-brightness Desk Lamp to 938 Lincoln Street, Unit 516, Fort Worth, TX, USA 92486, because you moved. After that, you decided you no longer need the Desk Lamp, so you would like to cancel the entire pending order instead.\n\nUse yusuf.taylor6118@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5690487'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5690487', 'item_ids': ['6555827912', '3358616356'], 'payment_method_id': 'credit_card_3599838'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8268610', 'address1': '938 Lincoln Street', 'address2': 'Unit 516', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '92486'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8268610', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction='You are Ava Kovacs (email: ava.kovacs4827@example.com). You want to update the shipping address for your pending order (containing a skateboard, headphones, garden hose, and tea kettle) to 4963 Jackson Street, Floor 763, Detroit, MI, USA 33013, because you need it delivered to a new location. You also want to change the payment method for this order from your Mastercard to your PayPal, as you prefer using PayPal for this purchase. Additionally, you want to return the 28-inch plastic skateboard with a plain design from your delivered order, because it is no longer needed, and receive a refund to the original payment method. Later, after completing these changes, you decide to cancel the same pending order entirely, because you no longer need the items.\n\nUse ava.kovacs4827@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '4963 Jackson Street', 'address2': 'Floor 763', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '33013'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4184032', 'payment_method_id': 'paypal_7443913'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4184032'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6344370', 'item_ids': ['4545791457'], 'payment_method_id': 'credit_card_9699699'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4184032', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction='You are assisting Ava Kovacs (email: ava.kovacs4827@example.com) with her order preferences. You want to update the shipping address for a pending order containing a 31-inch plastic skateboard, wireless black over-ear headphones, a 50ft rubber garden hose, and a 1.5-liter ceramic tea kettle to 3158 Lincoln Street, Unit 990, Denver, CO, USA 71415, because the original Phoenix address is no longer valid. You also prefer to change the payment method for this order from your Mastercard ending in 3598 to your PayPal account for easier tracking and budgeting. Additionally, you want to return a 28-inch plastic skateboard from a delivered order, as it is the wrong size, and you prefer the refund to be issued to the original credit card used for purchase. Later, after reconsidering your needs, you decide to cancel the entire pending order (which includes the skateboard, headphones, garden hose, and tea kettle) because it is no longer required.\n\nUse ava.kovacs4827@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '3158 Lincoln Street', 'address2': 'Unit 990', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '71415'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4184032', 'payment_method_id': 'paypal_7443913'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4184032'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6344370', 'item_ids': ['4545791457'], 'payment_method_id': 'credit_card_9699699'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4184032', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are assisting James Martin (email: james.martin9857@example.com) with three sequential requests regarding his pending orders. First, you want to update the payment method for the pending order containing a red cotton crew neck T-shirt in size XXL, a stainless steel smart thermostat compatible with Amazon Alexa, a white-dial silicone-strap wristwatch, a 100ft rubber garden hose, and a small green polyester backpack with a camera compartment — currently paid for via PayPal — to instead use his Visa card ending in 1826, because he prefers this payment method for tracking and rewards. Later, you will cancel his other pending order that includes a black nylon small backpack with a laptop compartment, an adjustable 5-25 lbs iron dumbbell set, and hiking boots in size 10 made of synthetic material without waterproofing, because it was placed by mistake. After that, you would like to update the shipping address for the first order (the one with the wristwatch and garden hose) to 5816 Oak Avenue, Unit 937, San Francisco, CA, USA 18913, to ensure delivery to his new location.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3043531', 'payment_method_id': 'credit_card_7083997'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3529525', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '5816 Oak Avenue', 'address2': 'Unit 937', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '18913'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are a customer who wants to change the payment method for an order from credit card to PayPal, later decides to cancel another order due to a mistaken purchase, and subsequently wishes to update the shipping address for the first order to a new location after browsing the product catalog. You prefer to pay by PayPal for the order originally charged to credit card. You would like to cancel one order because it was placed by mistake. After that, you want to update the shipping address for the remaining order to 456 Oak Avenue, Suite 500, Los Angeles, CA, USA 90210. Your email is yusuf.gonzalez2399@example.com.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2230795', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '456 Oak Avenue', 'address2': 'Suite 500', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '90210'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, and your email is olivia.ito5204@example.com. You want to update the shipping address for your pending order—which includes a black wired gaming mouse, a red 7 ft polyester patio umbrella, and a pair of size 8 leather hiking boots—from Denver, CO to 7297 Jefferson Avenue, Apt 738, Nashville, TN, USA 79637 because you will not be at the original address when the order ships. Later, you would like to change the payment method from your Visa card ending in 9182 to your PayPal account for better purchase protection and budget tracking.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '7297 Jefferson Avenue', 'address2': 'Apt 738', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '79637'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction="You are assisting a customer with email yusuf.garcia2909@example.com who has a pending order originally shipped to Indianapolis and paid with a gift card. You want to update the shipping address to 7589 Elm Street, Floor 975, Portland, OR, USA 71726, because the customer needs the items delivered to a new location. Later, you will change the payment method from the gift card to the customer's Mastercard ending in 3762, because the customer prefers to use this card for the transaction instead of the original gift card balance.\n\nUse yusuf.garcia2909@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '7589 Elm Street', 'address2': 'Floor 975', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '71726'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.moore1031@example.com',
        instruction='You are assisting Daiki Moore, whose email is daiki.moore1031@example.com. You are updating his pending order containing a Dumbbell Set, Office Chair, and Espresso Machine. You want to change the shipping address to 4811 Lincoln Street, Apt 565, San Antonio, TX, USA 97793, because he needs the delivery at a new location. You would like to update the payment method to his Visa card ending in 4204, as he prefers to use this card instead of the gift card currently applied. You also want to exchange the current Dumbbell Set (55-75 lbs, iron, fixed) for the same weight range but in urethane and adjustable, because he prefers a more durable and customizable option. You prefer any price difference to be processed using the same Visa card. Later, you would like to browse the full catalog of product types to explore what other items are available.\n\nUse daiki.moore1031@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4843514', 'address1': '4811 Lincoln Street', 'address2': 'Apt 565', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '97793'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4843514'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4843514', 'payment_method_id': 'credit_card_5613268'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4843514', 'item_ids': ['2444431651'], 'new_item_ids': ['6130713659'], 'payment_method_id': 'credit_card_5613268'}),
            Action(name='get_product_details', kwargs={'product_id': '7233192239'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.ito8974@example.com',
        instruction='You are Amelia Ito, with email amelia.ito8974@example.com, and you have a pending order currently shipping to Seattle. You want to update the shipping address to 231 Jefferson Avenue, Unit 516, San Jose, CA, USA 61994, so the order arrives at your new location. You also want to change the payment method from your Mastercard ending in 7517 to your PayPal account for better transaction tracking and security. Additionally, you would like to exchange the Fleece Jacket in your order from size XS, navy with full zipper to the same model in size L, red with half zipper, because it better fits your needs and style preference, and you prefer any price adjustment to be processed through PayPal. After these changes are completed, you would like to browse the full list of product types available in the store to explore future purchase options.\n\nUse amelia.ito8974@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3883329', 'address1': '231 Jefferson Avenue', 'address2': 'Unit 516', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '61994'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3883329'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3883329', 'payment_method_id': 'paypal_2767694'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3883329', 'item_ids': ['8161321868'], 'new_item_ids': ['8733974883'], 'payment_method_id': 'paypal_2767694'}),
            Action(name='get_product_details', kwargs={'product_id': '8560156827'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.garcia2061@example.com',
        instruction='You are assisting Anya Garcia (anya.garcia2061@example.com) with her pending order placed in Philadelphia. You want to change the ceramic 1.5L tea kettle to the stainless steel 2L version because she prefers a larger and more durable option. You prefer the payment adjustment to be processed using your Visa card ending in 8674, as you are comfortable covering any price difference for the updated item.\n\nUse anya.garcia2061@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6436609'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6436609', 'item_ids': ['7497340597'], 'new_item_ids': ['4238115171'], 'payment_method_id': 'credit_card_8955149'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.muller6448@example.com',
        instruction='You are assisting Fatima Muller (email: fatima.muller6448@example.com) with modifying her pending order placed in Chicago. You want to change the Mechanical Keyboard from the non-backlit version to the RGB-backlit version, keeping the same 80% size and linear switches, because she prefers customizable lighting for her setup. The new variant is available and less expensive, so you prefer the price difference be refunded to the original PayPal account used for payment.\n\nUse fatima.muller6448@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9962383'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9962383', 'item_ids': ['1421289881'], 'new_item_ids': ['8484921793'], 'payment_method_id': 'paypal_5541158'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.brown3965@example.com',
        instruction="You are assisting Harper Brown (email: harper.brown3965@example.com) with their pending order originally shipped to Fort Worth, TX, containing items including a Smart Watch, Tea Kettle, Perfume, Electric Toothbrush, and Hiking Boots. You want to first update the shipping address to 9449 Jackson Street, Floor 372, Austin, TX, USA 22585, because the customer has relocated. You would like to change the payment method from Mastercard ending in 3356 to PayPal, as the customer prefers using PayPal for this transaction. You also want to exchange the hiking boots from size 10, leather, not waterproof to the same model in size 9, leather, waterproof, because the original size was too large and the customer requires waterproofing for outdoor use, and you prefer to use the Mastercard ending in 3356 for any price difference. Later, after these modifications are processed, you would like to cancel the entire order with the reason 'no longer needed', as the customer no longer requires the items.\n\nUse harper.brown3965@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2273069', 'address1': '9449 Jackson Street', 'address2': 'Floor 372', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '22585'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2273069', 'payment_method_id': 'paypal_2306935'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2273069', 'item_ids': ['2185126308'], 'new_item_ids': ['8106223139'], 'payment_method_id': 'credit_card_3240550'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2273069'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2273069', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.moore8091@example.com',
        instruction='You are assisting Mia Moore (mia.moore8091@example.com) with her pending order. You want to first review the available products in the catalog to understand current offerings. Then, you would like to update the shipping address for the order to 1422 Jackson Street, Unit 287, Portland, OR, USA 31894, because you need it delivered to a new location. You prefer to change the payment method from the original gift card to your Mastercard ending in 2992, as you want to use this card for better purchase protection and to cover any price differences. You also want to modify two bookshelves in the order: you prefer the 5 ft wood white bookshelf over the current 3 ft glass white one because you need more storage space and a sturdier material, and you prefer the 6 ft glass white bookshelf over the current 4 ft version because you have a larger wall space now. After making these updates, you later decide you no longer need the items and would like to cancel the entire order. Before cancellation, you want to verify the full order details to ensure accuracy.\n\nUse mia.moore8091@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3130288', 'address1': '1422 Jackson Street', 'address2': 'Unit 287', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '31894'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3130288', 'payment_method_id': 'credit_card_2641784'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3130288', 'item_ids': ['2989722512', '7373893106'], 'new_item_ids': ['8479046075', '1111254697'], 'payment_method_id': 'credit_card_2641784'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3130288'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3130288', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.li4862@example.com',
        instruction='You are Mason Li, and your email is mason.li4862@example.com. You want the pending order for the black Desk Lamp to be shipped to 8386 Pine Avenue, Floor 459, Nashville, TN, USA 67930 instead of the original Seattle address, because you have moved. You also want your default address in the profile updated to the same Nashville address for all future orders, to ensure correct delivery going forward.\n\nUse mason.li4862@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2392556', 'address1': '8386 Pine Avenue', 'address2': 'Floor 459', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '67930'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mason_li_6934', 'address1': '8386 Pine Avenue', 'address2': 'Floor 459', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '67930'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2392556'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.jackson5798@example.com',
        instruction='You are to update the shipping address for the pending order containing a black desk lamp, a 15 bar capsule espresso machine with 1L capacity, and a 2L glass electric kettle to 9317 Washington Boulevard, Floor 465, Las Vegas, NV, USA 95459, because the originally entered address was incorrect. You also want to update the default address in the profile to the same Las Vegas address to ensure all future orders are delivered correctly. You prefer the payment method to remain as the gift card used for this purchase.\n\nUse mia.jackson5798@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7807323', 'address1': '9317 Washington Boulevard', 'address2': 'Floor 465', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '95459'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mia_jackson_2250', 'address1': '9317 Washington Boulevard', 'address2': 'Floor 465', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '95459'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7807323'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan.smith2463@example.com',
        instruction='You are assisting Juan Smith (email: juan.smith2463@example.com) with a series of requests. First, you want to update the shipping address for a pending order containing a white 4-cup drip coffee maker with auto shutoff and a bagged upright vacuum cleaner with pet hair removal to 9835 Washington Boulevard, Suite 546, Portland, OR, USA, 52243, because he has moved. You also want this new Portland address set as his default for future orders. Later, you would like to cancel another pending order that includes a white USB desk lamp, a medium electric grill with rotisserie, and a black fabric office chair with fixed armrests, because he no longer needs those items. After that, you are interested in reviewing the available variants of the Coffee Maker product—particularly options in black, stainless steel, and different types such as drip, espresso, and French press, with capacities from 1 to 8 cups and features like timer, auto shutoff, or built-in grinder—to consider a future purchase based on style, capacity, and functionality preferences.\n\nUse juan.smith2463@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1429524'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1429524', 'address1': '9835 Washington Boulevard', 'address2': 'Suite 546', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '52243'}),
            Action(name='modify_user_address', kwargs={'user_id': 'juan_smith_5229', 'address1': '9835 Washington Boulevard', 'address2': 'Suite 546', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '52243'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7546247', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7996920482'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.nguyen1348@example.com',
        instruction="You are assisting Fatima Nguyen, whose email is fatima.nguyen1348@example.com. You want to update the shipping address for her pending order containing a white glass bookshelf, a black metal smart watch, a white desk lamp, and a 2K indoor security camera to 3728 Adams Road, Floor 63, Phoenix, AZ, USA 55739 because it was initially set to a Columbus, OH address. You also want to update her default address to this new Phoenix address for future orders. Later, you will cancel another pending order that includes a ceramic tea kettle, men's fresh-scented perfume, an 8-inch black tablet, a 1500-piece animal-themed jigsaw puzzle, and a 3-piece silver softshell luggage set, as she no longer needs these items. After that, you would like to browse the product catalog with a focus on the Action Camera, specifically wanting detailed information about its available variants, including 4K and 5K resolution models, waterproof capabilities, and color options in black and silver, because she is considering a purchase.\n\nUse fatima.nguyen1348@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8808563'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8808563', 'address1': '3728 Adams Road', 'address2': 'Floor 63', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '55739'}),
            Action(name='modify_user_address', kwargs={'user_id': 'fatima_nguyen_7539', 'address1': '3728 Adams Road', 'address2': 'Floor 63', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '55739'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2904339', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.lee9368@example.com',
        instruction='You are assisting Yara Lee (yara.lee9368@example.com), who first wanted to explore the available product types in the catalog, which include items such as Hiking Boots, Office Chair, and Mechanical Keyboard, among 50 total product types. You are now handling her request regarding her pending order containing Hiking Boots size 10, a red leather high-back Office Chair, and a full-size clicky switch Mechanical Keyboard. You want to update the shipping address from Houston to 1974 Madison Drive, Suite 420, Philadelphia, PA, USA 78696 because she needs the items delivered to a new location. Later, you will change the payment method from her Mastercard ending in 5715 to her Visa ending in 6367 because she prefers to use a different card for this purchase. You prefer the refund of the original payment to be processed back to the Mastercard ending in 5715 if needed.\n\nUse yara.lee9368@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3320020', 'address1': '1974 Madison Drive', 'address2': 'Suite 420', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '78696'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3320020', 'payment_method_id': 'credit_card_6450164'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting Sophia Patel (email: sophia.patel9841@example.com) with her pending order containing a men's oriental-scented 100ml perfume, a glass 1.5-liter induction-compatible tea kettle, a black 1L glass electric kettle, and gray canvas sneakers size 8. You want to update the shipping address from Fort Worth, TX to 1378 Cedar Road, Unit 279, Columbus, OH, USA 51435 because she needs the package delivered to a new location. Later, you would like to change the payment method from the Visa card ending in 8025 to the Mastercard ending in 1639 for better rewards tracking on this purchase.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7905419', 'address1': '1378 Cedar Road', 'address2': 'Unit 279', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '51435'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7905419', 'payment_method_id': 'credit_card_6419343'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.ito2168@example.com',
        instruction='You are Evelyn Ito, authenticated via evelyn.ito2168@example.com, and you have a pending order containing a small green leather backpack with a camera compartment and a black Bluetooth speaker with 20-hour battery life. You want to update the shipping address from San Diego to 7398 Jackson Street, Floor 604, Los Angeles, CA, USA 95449 because it was initially entered incorrectly. After updating the address, you would like to verify the order details to ensure accuracy. Later, you prefer to switch the payment method from your Visa ending in 5896 to your PayPal account for better purchase protection.\n\nUse evelyn.ito2168@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6207110', 'address1': '7398 Jackson Street', 'address2': 'Floor 604', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '95449'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6207110'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6207110', 'payment_method_id': 'paypal_5377635'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.ito3790@example.com',
        instruction='You are Emma Ito, and your email is emma.ito3790@example.com. You are interested in Water Bottles and want to understand the available options, particularly comparing color, capacity, and material. You have a pending order for a 1000ml stainless steel blue water bottle, which you initially wanted to exchange for the black 1000ml stainless steel version because you prefer the black color. You also want to update the shipping address to 8124 Jefferson Avenue, Floor 803, Boston, MA, USA 91430, as you have moved and would like the item delivered to your new location. You prefer to use your PayPal account for any price difference. Later, you changed your mind and decided you no longer need the water bottle, so you would like to cancel the entire order #W8664580.\n\nUse emma.ito3790@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8664580'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8664580', 'item_ids': ['2366567022'], 'new_item_ids': ['7661609223'], 'payment_method_id': 'paypal_9995021'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8664580', 'address1': '8124 Jefferson Avenue', 'address2': 'Floor 803', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '91430'}),
            Action(name='modify_user_address', kwargs={'user_id': 'emma_ito_4529', 'address1': '8124 Jefferson Avenue', 'address2': 'Floor 803', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '91430'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8664580', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.wilson1598@example.com',
        instruction="You are assisting a customer with email amelia.wilson1598@example.com who initially wanted to learn about available product types, showing specific interest in the Action Camera. You are then asked to modify a pending order containing a red cotton v-neck T-Shirt in size L, a silver silicone-band Smart Watch with AMOLED display, and a 1000-piece expert-level art-themed Jigsaw Puzzle. For this order, you want to exchange the red T-Shirt (size L) for a purple one in size XL because the customer prefers the color and a larger fit. Later, you are asked to update the shipping address for this order to 3768 Elm Street, Apt 71, Los Angeles, CA, USA 84037, and also update the customer's default address on file to the same, for consistency and future deliveries. After that, you are informed that the customer has changed their mind entirely and would like to cancel the order because it is no longer needed. You prefer the original payment method, PayPal, to be used for any refund processing.\n\nUse amelia.wilson1598@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3062096'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3062096', 'item_ids': ['3234800602'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'paypal_4101143'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3062096', 'address1': '3185 Oak Avenue', 'address2': 'Unit 187', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '60766'}),
            Action(name='modify_user_address', kwargs={'user_id': 'amelia_wilson_4614', 'address1': '3185 Oak Avenue', 'address2': 'Unit 187', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '60766'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3062096', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.kim8981@example.com',
        instruction='You are Omar Kim, with email omar.kim8981@example.com. You want to modify the pending order containing a white small cycling helmet by changing the color to red while keeping the same size, because you prefer the red version over the white one. You prefer to use your Mastercard ending in 9843 for any price difference associated with this change. Later, you will cancel another pending order for a blue small cotton v-neck T-shirt because you no longer need it. After that, you would like to update the shipping address for the pending order containing an espresso machine and two tablets to 8845 Jackson Street, Unit 965, Columbus, OH, USA 99241, and also update your default address to this new Columbus, OH address for future orders.\n\nUse omar.kim8981@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8557584'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8557584', 'item_ids': ['1596993217'], 'new_item_ids': ['3358616356'], 'payment_method_id': 'credit_card_3577130'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1080318', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7111824', 'address1': '3932 Elm Street', 'address2': 'Apt 695', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '68420'}),
            Action(name='modify_user_address', kwargs={'user_id': 'omar_kim_3528', 'address1': '3932 Elm Street', 'address2': 'Apt 695', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '68420'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting a customer with email ethan.thomas7730@example.com regarding their pending order. You want to first update the shipping address to a new location in San Antonio, TX, to ensure delivery to the correct place. You would like to change the Smart Watch in the order from the black model with silicone band to the gold model with leather band, as you prefer a more elegant style over the sporty look. You prefer to switch the payment method from the gift card to PayPal for better purchase protection, and if any balance is due, you want to use your Visa card ending in 8901. After initiating these changes, you later decide to cancel the entire order as you have changed your mind about the purchase.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '8145 Elm Street', 'address2': 'Suite 777', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '12156'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'paypal_6982172'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8465042', 'item_ids': ['4920090458'], 'new_item_ids': ['5694328282'], 'payment_method_id': 'credit_card_7472558'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.ito3790@example.com',
        instruction='You are Emma Ito (emma.ito3790@example.com) and you want to update your pending order for a 1000ml stainless steel water bottle. First, you want the shipping address changed to 504 Adams Road, Suite 100, Los Angeles, CA, USA 86537 because you need it delivered to a new location. Then, you would like to change the payment method from PayPal to your Visa card ending in 3660 for better expense tracking. You also prefer the black version of the 1000ml stainless steel water bottle over the blue one because you find it more stylish, and you want any price difference adjusted using the same Visa card. Later, after reviewing your needs, you realize you no longer require the item and would like to cancel the entire order.\n\nUse emma.ito3790@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8664580', 'address1': '504 Adams Road', 'address2': 'Suite 100', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '86537'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8664580', 'payment_method_id': 'credit_card_8058445'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8664580', 'item_ids': ['2366567022'], 'new_item_ids': ['7661609223'], 'payment_method_id': 'credit_card_8058445'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8664580', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.ahmed4901@example.com',
        instruction='You are Mei Ahmed, with email mei.ahmed4901@example.com, and you want to update the shipping address for your pending order containing a Digital Camera and an Espresso Machine to 8074 Jefferson Avenue, Floor 913, Charlotte, NC, USA 42939, because you will be staying there and it is more convenient for delivery. You also want to update your default address to this new Charlotte address for future orders. Later, you would like to cancel this pending order because you realized you ordered by mistake and no longer need the items. After cancellation, you would like to confirm the order status is fully cancelled. After that, you would like to browse the available product types to explore what is offered, and then get more details about the Espresso Machine, particularly interested in models with 19 bar pressure and manual or capsule types, to consider a future purchase when you are ready.\n\nUse mei.ahmed4901@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2598324', 'address1': '8074 Jefferson Avenue', 'address2': 'Floor 913', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '42939'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mei_ahmed_4909', 'address1': '8074 Jefferson Avenue', 'address2': 'Floor 913', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '42939'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2598324', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2598324'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4354588079'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.gonzalez4478@example.com',
        instruction="You are assisting Liam Gonzalez, whose email is liam.gonzalez4478@example.com. You initially want to update the shipping address for a pending order containing a black 500ml glass water bottle, a blue fabric office chair with adjustable armrests, a 2K indoor security camera with 130-degree field of view, a robotic bagless vacuum cleaner with pet hair removal, and gray leather sneakers size 10, from 647 Laurel Lane, Suite 627, Austin, TX, USA 78747 to 1130 Maple Lane, Floor 298, Columbus, OH, USA 87424, because it was entered incorrectly. You also want your default address updated to this new Columbus address for future orders. Later, you change your mind and decide to cancel the entire order instead, with the reason 'no longer needed', as you no longer require the items. After that, you would like to browse the full range of available product types to explore options for a potential new order, so you can make an informed decision based on what is offered.\n\nUse liam.gonzalez4478@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8747662', 'address1': '1130 Maple Lane', 'address2': 'Floor 298', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '87424'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_gonzalez_4265', 'address1': '1130 Maple Lane', 'address2': 'Floor 298', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '87424'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8747662', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8747662'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2985987096'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.moore8091@example.com',
        instruction='You are Mia Moore, with email mia.moore8091@example.com. You want to update the payment method for your pending order (containing a glass white bookshelf, vacuum cleaner, smart watch, and another glass white bookshelf) from a gift card to your Mastercard ending in 2992, because you prefer using your card for this purchase. Later, you would like to exchange the metal brown 6 ft bookshelf from your delivered order in Philadelphia for the wood white 5 ft version, as you prefer the wood material and smaller size for your space.\n\nUse mia.moore8091@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3130288', 'payment_method_id': 'credit_card_2641784'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5544629', 'item_ids': ['6735339143'], 'new_item_ids': ['8479046075'], 'payment_method_id': 'paypal_5181300'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting yusuf.gonzalez2399@example.com with two separate order actions. First, you want to return the blue cotton crew neck T-Shirt (size M) from a delivered order that included a Tablet, E-Reader, and Jigsaw Puzzle, because it is no longer needed; you prefer the refund to be processed back to the original PayPal account used for purchase. Later, for a separate pending order containing a black 128GB Smartphone and a ceramic 1.5-liter Tea Kettle, you would like to update the shipping address to 4900 Washington Boulevard, Apt 863, Chicago, IL, USA, 32717, to ensure delivery to the correct location, and you prefer to change the payment method from credit card to PayPal for consistency with your preferred payment method.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1679211'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1679211', 'item_ids': ['9612497925'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '4900 Washington Boulevard', 'address2': 'Apt 863', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '32717'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.gonzalez8775@example.com',
        instruction='You are assisting Mei Gonzalez (email: mei.gonzalez8775@example.com). You want to return all items from the delivered order—specifically the navy small nylon backpack with a laptop compartment and the large brown memory foam pet bed—because they are no longer needed, and you prefer a refund issued back to the original payment method, your Visa card ending in 3742. Later, for the pending order—which includes an A5 soft cover notebook, a portable gas grill with a side burner, a white wireless laser gaming mouse, a black large fleece jacket with a full zipper, and a red mesh office chair with standard backrest height—you would like to update the shipping address to 7994 Oak Avenue, Apt 386, Las Vegas, NV, USA 27395, because the items are now intended for a different location. After that, you prefer to change the payment method from PayPal to your Visa card ending in 3742 to earn rewards on the purchase.\n\nUse mei.gonzalez8775@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7303089'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7303089', 'item_ids': ['2492465580', '7381052709'], 'payment_method_id': 'credit_card_4387170'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2052757', 'address1': '6354 Park Drive', 'address2': 'Suite 839', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '50969'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2052757', 'payment_method_id': 'credit_card_4387170'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.li2787@example.com',
        instruction='You are Raj Li, with email raj.li2787@example.com, who placed a pending order containing a brown 4 ft glass bookshelf, a green 750ml stainless steel water bottle, a large gas grill with rotisserie, and a black 5 ft glass bookshelf. You want to update the shipping address for this order from 187 Broadway, Suite 268, Fort Worth, TX, USA 76184 to 3795 Adams Road, Apt 300, Fort Worth, TX, USA 63892 because it needs to be delivered to a different location. You also prefer to pay using your PayPal instead of your Visa card ending in 3917 for greater convenience and payment flexibility. Later, you decide to cancel the entire order because it was placed by mistake, and no further delivery or processing should occur.\n\nUse raj.li2787@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8967935', 'address1': '3795 Adams Road', 'address2': 'Apt 300', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '63892'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8967935'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8967935', 'payment_method_id': 'paypal_2028062'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8967935', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction="You are assisting a customer whose email is ethan.thomas7730@example.com. You initially want to update the shipping address for a pending order containing a black Smart Watch with silicone band and a gold Smartphone with 128GB storage to 2976 Oak Avenue, Suite 957, Boston, MA, USA 47836, because the original address in Columbus, OH is no longer valid. You also prefer to change the payment method from the current gift card to your Visa card ending in 8901 for better expense tracking. Later, you decide you no longer need the items in the order, so you would like to cancel the entire order with the reason 'no longer needed', as your plans have changed and the devices are no longer required.\n\nUse ethan.thomas7730@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '2976 Oak Avenue', 'address2': 'Suite 957', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '47836'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'credit_card_7472558'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.kovacs4505@example.com',
        instruction='You are Sofia Kovacs (sofia.kovacs4505@example.com). You want to change the shipping address for your pending order—which includes a skateboard and a black 750ml stainless steel water bottle—to 9557 Main Street, Suite 655, Phoenix, AZ, USA 33164, because you need it delivered to a new location. You also want to update your default address to this new Phoenix address for future orders. Later, you would like to return the black 4-cup espresso coffee maker you received, because you prefer a simpler brewing method. After that, you would like to exchange it for the black 1-cup French press from the same brand, because you prefer manual brewing over espresso. You prefer any payment adjustment to be processed using your PayPal account.\n\nUse sofia.kovacs4505@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9869592', 'address1': '9557 Main Street', 'address2': 'Suite 655', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '33164'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_kovacs_7075', 'address1': '9557 Main Street', 'address2': 'Suite 655', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '33164'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7736983'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7736983', 'item_ids': ['5952720925'], 'payment_method_id': 'paypal_6840891'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7736983', 'item_ids': ['5952720925'], 'new_item_ids': ['3020722515'], 'payment_method_id': 'paypal_6840891'}),
            Action(name='get_product_details', kwargs={'product_id': '7996920482'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.thomas3069@example.com',
        instruction='You are Sofia Thomas (sofia.thomas3069@example.com) and you want to update the shipping address for your pending order—which includes Wireless Earbuds in blue, a bagged upright Vacuum Cleaner with pet hair removal, a black Electric Toothbrush with high speed settings, and a white 5000mAh Portable Charger—for delivery to 5268 Oak Avenue, Floor 14, New York, NY, USA 78292 because you will not be at the original Dallas address. You also want to update your default shipping address in your profile to the same New York address for all future orders.\n\nUse sofia.thomas3069@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7619352', 'address1': '5268 Oak Avenue', 'address2': 'Floor 14', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '78292'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_thomas_1518', 'address1': '5268 Oak Avenue', 'address2': 'Floor 14', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '78292'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.lopez3271@example.com',
        instruction='You are assisting Isabella Lopez (isabella.lopez3271@example.com) with her pending order. You want to update the shipping address to 4726 Pine Avenue, Suite 528, Philadelphia, PA, USA 98251 because it is her current location. You prefer to change the payment method to your Visa card ending in 8902 for the order balance, as it is your preferred card for purchases. You would like to exchange the red Bluetooth speaker (10-hour battery, water resistant) for the blue one with the same specifications because you prefer the blue color. For any price difference from the exchange, you prefer to use your Mastercard ending in 4336. Later, after considering your needs, you decide to cancel the entire order because you no longer require the speaker.\n\nUse isabella.lopez3271@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4923227', 'address1': '4726 Pine Avenue', 'address2': 'Suite 528', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '98251'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4923227', 'payment_method_id': 'credit_card_8897086'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4923227'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4923227', 'item_ids': ['7751905257'], 'new_item_ids': ['4716977452'], 'payment_method_id': 'credit_card_8554680'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4923227', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.patel3193@example.com',
        instruction="You are assisting Mei Patel (mei.patel3193@example.com) with her pending order. You want to update the shipping address to 7848 Pine Avenue, Unit 637, Philadelphia, PA, USA 86945, because she has relocated. After that, you prefer to change the payment method from PayPal to your Visa card ending in 9904 for billing convenience. Subsequently, you would like to exchange the 100ml men's oriental perfume for the 30ml version of the same scent, as the smaller size better suits your needs. Finally, if any of these changes cannot be processed smoothly, you want to cancel the entire order because it will no longer be needed.\n\nUse mei.patel3193@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9583042', 'address1': '7848 Pine Avenue', 'address2': 'Unit 637', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '86945'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9583042', 'payment_method_id': 'credit_card_9503061'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9583042'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9583042', 'item_ids': ['5421902839'], 'new_item_ids': ['1325156478'], 'payment_method_id': 'credit_card_9503061'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9583042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are lucas.johansson7741@example.com and want to modify your pending order currently shipping to San Francisco, CA, by changing the delivery address to 7126 Washington Boulevard, Suite 855, Portland, OR, USA 92258, because you will be traveling there and prefer the package to arrive at your temporary location. You also want to update your default address to this new Portland address for future orders. Additionally, you want to exchange the Hiking Boots in this order from size 8 to size 9, preferring the same leather and waterproof version for a better fit, and you prefer to use your Visa card ending in 9452 for any price difference. Later, after confirming the changes, you would like to cancel your other pending order containing an Office Chair and Tablet, as you no longer need those items.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '7126 Washington Boulevard', 'address2': 'Suite 855', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '92258'}),
            Action(name='modify_user_address', kwargs={'user_id': 'lucas_johansson_1090', 'address1': '7126 Washington Boulevard', 'address2': 'Suite 855', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '92258'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5073920', 'item_ids': ['2648909398'], 'new_item_ids': ['8106223139'], 'payment_method_id': 'credit_card_1864112'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8379216', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are Omar Silva, with email omar.silva4147@example.com, and you want to cancel your pending order that includes a 2000-piece fantasy-themed jigsaw puzzle, a brown wooden bookshelf, a silver 4K action camera, polarized sunglasses with green lenses, and a 2000-piece animals-themed puzzle, because it was placed by mistake. You also want to modify your other pending order that currently has a purple XL cotton crew neck T-shirt, a silver leather-band smart watch, and a 1L manual espresso machine. For this order, you would like to update the shipping address to 1970 Jefferson Avenue, Apt 861, Detroit, MI, USA 98528, change the payment method to your Mastercard ending in 5859, and exchange the purple XL T-shirt for a blue M. Later, after these updates, you will proceed with the modified order as adjusted.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9673784', 'address1': '1970 Jefferson Avenue', 'address2': 'Apt 861', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '98528'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9673784', 'payment_method_id': 'credit_card_5322562'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9673784', 'item_ids': ['8124970213'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'credit_card_5322562'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.martin1207@example.com',
        instruction='You are Emma Martin, with email emma.martin1207@example.com. You want to update the shipping address for your pending order containing Headphones (red, wireless, on-ear) to 8703 Maple Lane, Unit 846, Houston, TX, USA 46758, because you have moved from Austin. You also want your default address updated to this new Houston address for future orders. Later, you would like to exchange the Makeup Kit (currently medium skin tone, professional size, Brand A) from your delivered order for a version with a darker skin tone, because it better matches your complexion, and you prefer the bamboo deck version of the skateboard over the maple deck for its eco-friendly material and durability. You prefer to use your PayPal account to cover any price difference for the exchange. After that, you would like to cancel your other pending order containing a Fleece Jacket, T-Shirt, Smartphone, Makeup Kit (dark), and Portable Charger, because you no longer need those items.\n\nUse emma.martin1207@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9432206', 'address1': '8703 Maple Lane', 'address2': 'Unit 846', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '46758'}),
            Action(name='modify_user_address', kwargs={'user_id': 'emma_martin_6993', 'address1': '8703 Maple Lane', 'address2': 'Unit 846', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '46758'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2800409'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2800409', 'item_ids': ['2882812427', '5120532699'], 'new_item_ids': ['1573035764', '5312063289'], 'payment_method_id': 'paypal_6129397'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5432440', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.khan6479@example.com',
        instruction="You are assisting Ivan Khan (email: ivan.khan6479@example.com). You want to update the shipping address for a pending order containing an Air Purifier and a Backpack to 9589 Oak Avenue, Unit 672, Philadelphia, PA, USA 58003, because it was originally going to an old address. You also want to update your default address to this new one to prevent future delivery issues. Later, you would like to exchange the Wireless Earbuds with 6-hour battery life (blue, IPX4 water resistance) from a delivered order for a variant with 8-hour battery life (same color and water resistance), because the current battery life is shorter than desired. You prefer the exchange refund to be processed to your PayPal account. After that, you would like to cancel another pending order containing a navy Backpack and a women's woody-scented 50ml Perfume, because it is no longer needed.\n\nUse ivan.khan6479@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7032009', 'address1': '9589 Oak Avenue', 'address2': 'Unit 672', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '58003'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ivan_khan_7475', 'address1': '9589 Oak Avenue', 'address2': 'Unit 672', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '58003'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1519594'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1519594', 'item_ids': ['1646531091'], 'new_item_ids': ['8555936349'], 'payment_method_id': 'paypal_7729105'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5782623', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.gonzalez1317@example.com',
        instruction="You are Isabella Gonzalez, and your email is isabella.gonzalez1317@example.com. You want to update the shipping address for your pending order—which includes a 28-inch maple skateboard, an A4 soft-cover notebook, and a 2-piece silver hardshell luggage set—from Fort Worth, TX to 1165 Main Street, Floor 562, Portland, OR 20211, because you need it delivered to a different location. After updating the address, you want to verify the order details to confirm the change was applied correctly. Then, you would like to change the payment method from your Visa ending in 4920 to your Mastercard ending in 9364, as you prefer to use that card for this purchase. Later, you will cancel the order with the reason 'no longer needed', as you no longer require the items.\n\nUse isabella.gonzalez1317@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1258841', 'address1': '1165 Main Street', 'address2': 'Floor 562', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '20211'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1258841'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1258841', 'payment_method_id': 'credit_card_9878778'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1258841', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction="You are Lucas Johansson, and your email is lucas.johansson7741@example.com. You have a pending order containing hiking boots, a black small nylon backpack with a laptop compartment, and a 500-piece expert-level animal-themed jigsaw puzzle. You want to update the shipping address for this order from San Francisco to 2739 Main Street, Apt 376, Portland, OR, USA 50875 because you will be traveling and need the items delivered to your temporary location. After updating the address, you would like to change the payment method from your Mastercard ending in 3088 to your Visa ending in 9452 for better rewards tracking. Later, you decide the order is no longer needed, so you would like to cancel the entire order with the reason 'no longer needed'.\n\nUse lucas.johansson7741@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '2739 Main Street', 'address2': 'Apt 376', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '50875'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction="You are lei.li8350@example.com, and you have a pending order for a space grey 17-inch laptop. You initially want to update the shipping address to 1445 Lincoln Street, Floor 165, Chicago, IL, USA 53598, because you prefer delivery to your new location. You also want to change the payment method from PayPal to your Visa card ending in 2697, as you prefer to use this card for better rewards tracking. Later, you decide to cancel the order entirely, so you would like to proceed with cancellation with the reason 'no longer needed', as the laptop is no longer required.\n\nUse lei.li8350@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '1445 Lincoln Street', 'address2': 'Floor 165', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '53598'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5166363', 'payment_method_id': 'credit_card_4466831'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.li2787@example.com',
        instruction="You are assisting a customer with email raj.li2787@example.com regarding a pending order originally shipped to Fort Worth, TX. You want to first update the shipping address to 5099 Pine Avenue, Unit 385, Fort Worth, TX, USA 91151, because the original address is no longer valid. Then, you prefer to change the payment method to PayPal for better transaction tracking and buyer protection. After completing these updates, you later decide you no longer need the order—containing a brown 4 ft glass bookshelf, a green 750ml stainless steel water bottle, a large gas grill with rotisserie, and a black 5 ft glass bookshelf—and would like to cancel it with the reason 'no longer needed'.\n\nUse raj.li2787@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8967935'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8967935', 'address1': '5099 Pine Avenue', 'address2': 'Unit 385', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '91151'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8967935', 'payment_method_id': 'paypal_2028062'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8967935', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.garcia9090@example.com',
        instruction='You are Harper Garcia, with email harper.garcia9090@example.com. You initially want to update the shipping address for your pending order containing a 4-piece red hardshell luggage set, red wired in-ear headphones, and a bagged canister vacuum cleaner to 4880 Jefferson Avenue, Apt 977, Dallas, TX, USA 19577, because you thought you would be traveling. Later, you decide to cancel that order entirely because you no longer need the items. Separately, you would like to modify the Pet Bed in your other pending order—currently a medium beige polyester version—by upgrading the material to memory foam for better comfort and support, while keeping the same size and color. You prefer the memory foam version over the polyester one for improved durability and coziness. You want to use your Visa card ending in 6583 for the small price difference. Additionally, you want to browse the full range of product types available in the store to explore other options. Finally, you would like detailed information about the Pet Bed product to better understand its features and available variants.\n\nUse harper.garcia9090@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8360923', 'address1': '4880 Jefferson Avenue', 'address2': 'Apt 977', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '19577'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8360923', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5737680'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5737680', 'item_ids': ['6499892866'], 'new_item_ids': ['3360679910'], 'payment_method_id': 'credit_card_2369458'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2747247837'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.gonzalez8775@example.com',
        instruction='You are assisting Mei Gonzalez (mei.gonzalez8775@example.com), who has a pending order containing a soft cover A5 notebook, a portable gas grill with side burner, a white wireless laser gaming mouse, a black large fleece jacket with full zipper, and a red mesh office chair without armrests. You want to change the payment method for this order from PayPal to her Mastercard ending in 3742 because she prefers using this card for tracking and rewards. After that, you would like to update the shipping address for this order to 9669 Oak Avenue, Apt 129, Nashville, TN, USA 61046, as she needs the items delivered to a new location. Subsequently, you also want to update her default address for future orders to the same Nashville address to ensure consistency in delivery going forward.\n\nUse mei.gonzalez8775@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2052757'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2052757', 'payment_method_id': 'credit_card_4387170'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2052757', 'address1': '9669 Oak Avenue', 'address2': 'Apt 129', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '61046'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mei_gonzalez_4785', 'address1': '9669 Oak Avenue', 'address2': 'Apt 129', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '61046'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction='You are assisting Ava Kovacs (email: ava.kovacs4827@example.com) with her pending order containing a skateboard, wireless over-ear headphones, a 50ft rubber garden hose, and a 1.5-liter ceramic tea kettle. You want to change the payment method from the Mastercard ending in 3598 to her PayPal account because she prefers using PayPal for this purchase. You would like the order to be shipped to 3460 Washington Boulevard, Floor 241, Los Angeles, CA, USA 45962 instead of the current Phoenix address, as it needs to go to a new location. After that, you want to update her default address to this new Los Angeles address for all future orders to ensure convenience and consistency.\n\nUse ava.kovacs4827@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W4184032'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4184032', 'payment_method_id': 'paypal_7443913'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '3460 Washington Boulevard', 'address2': 'Floor 241', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '45962'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_kovacs_3448', 'address1': '3460 Washington Boulevard', 'address2': 'Floor 241', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '45962'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.johansson9391@example.com',
        instruction="You are Isabella Johansson, and your email is isabella.johansson9391@example.com. You want to update the shipping address for your pending order—containing a robotic bagless cordless vacuum cleaner, a 20000mAh black wireless portable charger, an 8-inch Wi-Fi e-reader with 8GB storage, a 50ft black vinyl garden hose, and a blue fabric office chair with adjustable armrests—to 1230 Cedar Road, Apt 309, Jacksonville, FL, USA 50561, because you recently moved. You also want your default address updated to this new Jacksonville address for all future orders, to ensure correct delivery going forward. Later, if you decide to cancel this order, you would like it canceled with the reason 'no longer needed', in case your plans change. After that, for any exchange or return on your delivered orders, you prefer refunds or charges to be processed to your PayPal account, as it is your preferred payment method for such transactions.\n\nUse isabella.johansson9391@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2575533', 'address1': '1230 Cedar Road', 'address2': 'Apt 309', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '50561'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_johansson_2152', 'address1': '1230 Cedar Road', 'address2': 'Apt 309', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '50561'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2575533', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2575533'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3792453', 'item_ids': ['4293355847'], 'payment_method_id': 'paypal_3024827'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3792453', 'item_ids': ['4293355847'], 'new_item_ids': ['4293355847'], 'payment_method_id': 'paypal_3024827'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.kovacs6946@example.com',
        instruction='You are Harper Kovacs, with email harper.kovacs6946@example.com. You want to update the shipping address for your pending wristwatch order from San Francisco to 4649 Pine Avenue, Apt 39, Nashville, TN, USA 31934 because you have relocated. The wristwatch has a white dial and a metal strap. Later, you would like to exchange the 1L black glass electric kettle from your delivered order for a 2L white glass electric kettle because you need a larger capacity and prefer the white color. You prefer to use your PayPal account for any price adjustment. After reconsidering, you no longer need the wristwatch and would like to cancel the pending order instead of updating the address.\n\nUse harper.kovacs6946@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7775097', 'address1': '4649 Pine Avenue', 'address2': 'Apt 39', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '31934'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7775097'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5955464', 'item_ids': ['2323972008'], 'new_item_ids': ['4064702754'], 'payment_method_id': 'paypal_3246095'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5955464', 'item_ids': ['2323972008'], 'payment_method_id': 'paypal_3246095'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7775097', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.lee9368@example.com',
        instruction='You are assisting Yara Lee (email: yara.lee9368@example.com). You want to first update the shipping address for a pending order currently set to Houston to 123 Oak Avenue, Suite 100, Dallas, TX, USA 75201, because she prefers delivery to her new location. At the same time, you would like to initiate an exchange for a mechanical keyboard from a delivered order, replacing the compact 60% model with RGB backlighting and tactile switches with a full-size version that has white backlighting and tactile switches, because she prefers a larger layout with a simpler light color. You prefer the price adjustment for this exchange to be processed using your Visa card ending in 6367. Later, you decided to cancel the same pending order entirely because it was placed by mistake, so you no longer want the items in that order to be shipped or billed further.\n\nUse yara.lee9368@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3320020', 'address1': '123 Oak Avenue', 'address2': 'Suite 100', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '75201'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3320020'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1341845', 'item_ids': ['4402162122'], 'new_item_ids': ['3616838507'], 'payment_method_id': 'credit_card_6450164'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1341845', 'item_ids': ['4402162122'], 'payment_method_id': 'credit_card_6450164'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3320020', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are Liam Thomas (liam.thomas9081@example.com). You want to cancel your pending order containing an E-Reader and an Air Purifier because you no longer need the items. Later, you would like to change the shipping address for another pending order containing a Skateboard, a Luggage Set, and a Portable Charger to 5328 Main Street, Unit 556, Los Angeles, CA, USA 37899. After that, you would like your default address to be updated to this new address for all future orders. You prefer the refund from the canceled order to be returned to the original payment method, which is your Visa card ending in 3194.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1654931'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1654931', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3295833', 'address1': '5328 Main Street', 'address2': 'Unit 556', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '37899'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_thomas_7882', 'address1': '5328 Main Street', 'address2': 'Unit 556', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '37899'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.ahmed1696@example.com',
        instruction="You are assisting a customer with email lei.ahmed1696@example.com who has a pending order containing a skateboard and two cycling helmets originally shipped to Philadelphia. You want to update the shipping address for this order to 3445 Park Drive, Unit 73, Detroit, MI, USA 22375, because the customer has relocated. Later, you will cancel this order because the customer no longer needs the items. After that, you would like to explore available products, specifically the Bookshelf, to understand the options. Subsequently, you want to modify another pending order that includes a white, 5 ft glass Bookshelf and a green 500ml stainless steel water bottle. You prefer to change the Bookshelf to the wood, white, 5 ft version because it better matches the customer's home decor. You also prefer that any refund for the price difference be issued back to the Mastercard ending in 3705, which was used for the original purchase.\n\nUse lei.ahmed1696@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9132840', 'address1': '3445 Park Drive', 'address2': 'Unit 73', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '22375'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9132840', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8600330539'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6724985'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6724985', 'item_ids': ['8895454203'], 'new_item_ids': ['8479046075'], 'payment_method_id': 'credit_card_3593714'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.lee9368@example.com',
        instruction='You are assisting Yara Lee (email: yara.lee9368@example.com). You want to first learn about the available product types, with specific interest in the Mechanical Keyboard. Then, for your pending order containing a Mechanical Keyboard with clicky switches, white backlight, and full-size layout, you want to update the shipping address to 8895 Washington Boulevard, Suite 576, Las Vegas, NV, USA 48709. After that, you would like to change the payment method for this order to your Visa card ending in 6367. You also prefer to modify the current Mechanical Keyboard in the order to a different variant of the same product, though no specific replacement variant is specified. Later, you would like to return the blue Bluetooth Speaker from your delivered order, as it is no longer needed, and you prefer the refund to be issued back to your Visa card ending in 6367.\n\nUse yara.lee9368@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1656367028'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3320020', 'address1': '8895 Washington Boulevard', 'address2': 'Suite 576', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '48709'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3320020', 'payment_method_id': 'credit_card_6450164'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3320020', 'item_ids': ['6342039236'], 'new_item_ids': ['4402162122'], 'payment_method_id': 'credit_card_6450164'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1341845'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1341845', 'item_ids': ['6704763132'], 'payment_method_id': 'credit_card_6450164'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.wilson1253@example.com',
        instruction='You are Lei Wilson (email: lei.wilson1253@example.com) and you want to exchange the 15-inch Laptop with 16GB RAM and 512GB SSD in your delivered order for a 15-inch Laptop with 32GB RAM and 256GB SSD because you need more memory for performance-intensive tasks. You prefer to use your Mastercard ending in 1531 for any price difference. Later, you would like to update the shipping address for your pending order containing items like an Espresso Machine and Wireless Earbuds to a new location in Houston: 7223 Oak Avenue, Suite 701, Houston, TX, USA 15084. After that, you would like to browse the full catalog of product types available in the store to explore all offerings, including categories like Laptops, Smartphones, Espresso Machines, Headphones, and others.\n\nUse lei.wilson1253@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2905754'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2905754', 'item_ids': ['3478699712'], 'payment_method_id': 'credit_card_3677959'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2905754', 'item_ids': ['3478699712'], 'new_item_ids': ['2216662955'], 'payment_method_id': 'credit_card_3677959'}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3826449', 'address1': '7223 Oak Avenue', 'address2': 'Suite 701', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '15084'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3826449', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan.nguyen7877@example.com',
        instruction='You are assisting Juan Nguyen (email: juan.nguyen7877@example.com) with a series of requests. First, you want to exchange the Hiking Boots from his delivered order because the size 7, synthetic, non-waterproof version does not fit or meet his needs; you prefer the size 9, leather, waterproof variant for better fit and durability. You prefer any price difference to be processed using the Mastercard ending in 9548. Later, for the pending order containing the Mechanical Keyboard, you would like to change the shipping address to 123 Oak Street, Apt 4B, Denver, CO, USA 80202, and subsequently cancel the order because it was placed by mistake. After that, you would like to browse the full range of available product types in the store to explore future purchase options.\n\nUse juan.nguyen7877@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2430890'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2430890', 'item_ids': ['1437889264'], 'payment_method_id': 'credit_card_3522913'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2430890', 'item_ids': ['1437889264'], 'new_item_ids': ['8106223139'], 'payment_method_id': 'credit_card_3522913'}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9537685', 'address1': '123 Oak Street', 'address2': 'Apt 4B', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '80202'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9537685', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia, whose email is yusuf.garcia2909@example.com. You want to change the payment method for a pending order containing hiking boots, a laptop, and an air purifier from a gift card to his Mastercard ending in 3762, because he prefers to use that card for tracking and rewards. Later, you will cancel that same order because he no longer needs the items. For another pending order containing a grey, medium, polyester backpack with a laptop compartment, you would like to exchange it for the black, large, nylon version with a camera compartment, as it better suits his travel photography needs. After that, you want to update the shipping address for this backpack order to 9016 Park Drive, Apt 848, Jacksonville, FL, USA 72582, which is his new temporary residence.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6885344', 'item_ids': ['5917587651'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'paypal_7503218'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6885344', 'address1': '7277 Maple Lane', 'address2': 'Unit 997', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '92947'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.rossi1299@example.com',
        instruction='You are Amelia Rossi, and your email is amelia.rossi1299@example.com. You initially wanted to explore the product catalog to browse available items. You then decided to modify your pending order by updating the shipping address to 4843 Adams Road, Unit 912, Los Angeles, CA, USA 89047 because you prefer delivery to your new location. You prefer to change the payment method from the original gift card to your Visa card ending in 9402 for better tracking and flexibility, and you want to update the T-shirt in the order because you prefer the purple XL cotton crew neck style over the original blue medium one, as it better fits your needs. After making these changes, you realized the order was placed by mistake, so you would like to cancel the entire order.\n\nUse amelia.rossi1299@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8255453', 'address1': '4843 Adams Road', 'address2': 'Unit 912', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '89047'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8255453'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8255453', 'payment_method_id': 'credit_card_6844118'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8255453', 'item_ids': ['9612497925'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'credit_card_6844118'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8255453', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.lopez2997@example.com',
        instruction='You are assisting a customer with email raj.lopez2997@example.com who is interested in skateboards. You want to update the shipping address for their pending order to 6311 Park Drive, Unit 231, Las Vegas, NV, USA 20368, because they have relocated temporarily. You would like to change the payment method from Mastercard to PayPal for better purchase protection and easier tracking. You prefer to exchange the current skateboard in the order, which has a graphic design on a 31-inch bamboo deck, for the custom design version with the same dimensions and material, because they want a more personalized look. You prefer the price difference to be handled using the same PayPal account to streamline the transaction.\n\nUse raj.lopez2997@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3502364', 'address1': '6311 Park Drive', 'address2': 'Unit 231', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '20368'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3502364', 'payment_method_id': 'paypal_7007375'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3502364', 'item_ids': ['5312063289'], 'new_item_ids': ['6313971174'], 'payment_method_id': 'paypal_7007375'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3502364', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3502364'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting Yusuf Gonzalez (email: yusuf.gonzalez2399@example.com). For his pending order containing a black 128GB smartphone and a ceramic 1.5-liter tea kettle, you want to change the payment method from Mastercard ending in 9928 to PayPal for better transaction tracking. After that, you would like to update the shipping address to 6072 Madison Drive, Unit 499, Chicago, IL, USA 95706, as the items are now intended for a different location. Later, for his delivered order that includes a tablet, e-reader, fantasy-themed 2000-piece jigsaw puzzle, and a blue medium cotton crew neck T-shirt, you would like to exchange the blue medium T-shirt for the purple XL cotton crew neck version because it better fits his preference in both size and color, and return the jigsaw puzzle as it is no longer needed. You prefer any price difference or refund from these adjustments to be processed to the same PayPal account used for the original purchase.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '6072 Madison Drive', 'address2': 'Unit 499', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '95706'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_gonzalez_8900', 'address1': '6072 Madison Drive', 'address2': 'Unit 499', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '95706'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1679211', 'item_ids': ['9612497925'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1679211', 'item_ids': ['7127170374'], 'payment_method_id': 'paypal_3022415'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito (olivia.ito5204@example.com), and you want to update your pending order containing a gaming mouse, patio umbrella, and hiking boots shipping to Denver by changing the payment method from your Visa ending in 9182 to your PayPal account for convenience, and updating the shipping address to 5766 Adams Road, Suite 115, San Antonio, TX, USA 11457 because you have relocated. Later, you would like to exchange the black synthetic sneakers in your delivered order—which also shipped to Denver and included an espresso machine—for a pair of the same model in size 10, gray, leather, preferring this variant for better fit and style, and you want any price adjustment handled through your PayPal account. After that, you would like your default shipping address updated to 5766 Adams Road, Suite 115, San Antonio, TX, USA 11457 for all future orders to ensure consistent delivery to your new location.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '5766 Adams Road', 'address2': 'Suite 115', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '11457'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_ito_3591', 'address1': '5766 Adams Road', 'address2': 'Suite 115', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '11457'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5866402', 'item_ids': ['9727387530'], 'new_item_ids': ['2509076505'], 'payment_method_id': 'paypal_8049766'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting a customer with email ethan.thomas7730@example.com who wants to first browse the product catalog to explore available items. Then, for their pending order containing a black silicone-band AMOLED Smart Watch and a gold 128GB 4GB RAM 5.8-inch Smartphone, you want to update the shipping address from Columbus, OH to 4279 Oak Avenue, Floor 551, New York, NY, USA 75984 because the customer has relocated temporarily. After the address update, you would like to change the payment method from the current gift card to the customer’s Visa card ending in 8901 for better expense tracking. Finally, you prefer to receive confirmation of the updated order details to ensure all changes—especially the new New York address and Visa payment—have been applied correctly before the order ships.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '4279 Oak Avenue', 'address2': 'Floor 551', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '75984'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'credit_card_7472558'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.brown5032@example.com',
        instruction='You are Emma Brown, with email emma.brown5032@example.com, and you have a pending order for a skateboard. You want to update the shipping address to 9819 Oak Avenue, Suite 800, Boston, MA, USA 98029, because the original Jacksonville address is no longer valid. You also prefer to change the payment method from PayPal to your Visa card ending in 9135 for better rewards and tracking. These updates should be applied to your current pending order before fulfillment.\n\nUse emma.brown5032@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6460787', 'address1': '9819 Oak Avenue', 'address2': 'Suite 800', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '98029'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6460787', 'payment_method_id': 'credit_card_8850930'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6460787'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com) with his pending order. You want to update the shipping address to 8266 Main Street, Suite 911, Chicago, IL, USA 32760 because he needs the delivery sent to a different location. Then, you would like to change the laptop in the order from the current 13-inch black model with 512GB SSD to the 17-inch black model with 1TB SSD and i7 processor, as he prefers a larger screen and more storage for his work. You prefer the price difference to be handled using his Mastercard ending in 3762, and you want the entire order’s payment method switched from the gift card to that same Mastercard for consistency and ease of tracking.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '8266 Main Street', 'address2': 'Suite 911', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '32760'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2564042', 'item_ids': ['1657832319'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'credit_card_8405687'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.nguyen1851@example.com',
        instruction="You are assisting Ava Nguyen (email: ava.nguyen1851@example.com) with updates to her pending order. You want to change the shipping address to 848 Jackson Street, Unit 960, Columbus, OH, USA 57845, because the item is intended for her partner and needs to be delivered to a new location. You would like to exchange the current women's woody 30ml perfume for the men's fresh 50ml variant, as it better suits the recipient's preference and provides a larger size. You prefer the price difference to be handled using your Visa card ending in 3061. Later, you want to update the entire order's payment method from PayPal to the same Visa card ending in 3061 for consistency in payment tracking and personal finance management.\n\nUse ava.nguyen1851@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8732376', 'address1': '848 Jackson Street', 'address2': 'Unit 960', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '57845'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8732376'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8732376', 'payment_method_id': 'credit_card_3975380'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8732376', 'item_ids': ['8316205423'], 'new_item_ids': ['9007697085'], 'payment_method_id': 'credit_card_3975380'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction='You are assisting Sophia Patel (sophia.patel9841@example.com) with her pending order. You want to first update the shipping address to 1890 Pine Avenue, Floor 230, Phoenix, AZ, USA 41097, because the original address in Fort Worth, TX is incorrect. Then, you would like to change the payment method to your Mastercard ending in 1639 for better account management. After making these updates, you decide to cancel the entire order because it was placed by mistake. Finally, you want to confirm the current order details to ensure all changes, including the cancellation, have been processed correctly.\n\nUse sophia.patel9841@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7905419', 'address1': '1890 Pine Avenue', 'address2': 'Floor 230', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '41097'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7905419', 'payment_method_id': 'credit_card_6419343'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7905419', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.brown5032@example.com',
        instruction='You are Emma Brown, with email emma.brown5032@example.com, and you have a pending order for a 34-inch skateboard with a plastic deck and plain design. You want to update the shipping address to 8930 Oak Avenue, Floor 473, Houston, TX, USA 93733, because you need it delivered to a new location. Later, you would like to change the payment method from PayPal to your Visa card ending in 9135 for better expense tracking. After that, you decide to cancel the order entirely because it was placed by mistake.\n\nUse emma.brown5032@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6460787', 'address1': '8930 Oak Avenue', 'address2': 'Floor 473', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '93733'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6460787', 'payment_method_id': 'credit_card_8850930'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6460787', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6460787'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.lee3013@example.com',
        instruction='You are assisting Anya Lee (email: anya.lee3013@example.com). You want to browse the current product catalog. You also want to update the shipping address for your pending order—which includes headphones, hiking boots, a water bottle, a coffee maker, and a smart watch—to 116 Jackson Street, Unit 659, Houston, TX, USA 38768, because you recently moved. Later, you want to update your default shipping address to the same Houston address for future orders. After that, you would like to return the hiking boots from your delivered order—which were size 10, made of leather, and not waterproof—because they do not fit well and were less durable than expected. You prefer a refund back to your PayPal account used in the original purchase.\n\nUse anya.lee3013@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3176007', 'address1': '116 Jackson Street', 'address2': 'Unit 659', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '38768'}),
            Action(name='modify_user_address', kwargs={'user_id': 'anya_lee_8315', 'address1': '116 Jackson Street', 'address2': 'Unit 659', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '38768'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1335809', 'item_ids': ['2185126308'], 'payment_method_id': 'paypal_3728317'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.sanchez6360@example.com',
        instruction='You are assisting Ethan Sanchez (email: ethan.sanchez6360@example.com) with several requests in sequence. First, you want to browse the product catalog to explore available items. Then, you want to update the shipping address for your pending order—which includes an E-Reader, Water Bottle, Luggage Set, Laptop, and Grill—currently shipping to New York, to 6993 Lincoln Street, Suite 852, Chicago, IL, USA 42288, because you have relocated temporarily. You also want to update your default address in your profile to the same Chicago address for future orders. Later, you would like to return the Dumbbell Set (30-50 lbs, urethane, fixed) from your delivered order—which also includes a Smart Watch and Wristwatch—because it does not meet your workout needs, and you prefer a more compact set. You would like the refund issued back to your PayPal account, as that was the original payment method and you prefer refunds to go there for faster processing.\n\nUse ethan.sanchez6360@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9102111', 'address1': '6993 Lincoln Street', 'address2': 'Suite 852', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '42288'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_sanchez_2952', 'address1': '6993 Lincoln Street', 'address2': 'Suite 852', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '42288'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9250394', 'item_ids': ['7159180318'], 'payment_method_id': 'paypal_3574041'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li5731@example.com',
        instruction='You are assisting Sofia Li (sofia.li5731@example.com). You want to update the shipping address for a pending order containing wireless earbuds, a cycling helmet, and a Bluetooth speaker from Dallas to 7539 Jackson Street, Unit 544, Boston, MA, USA 32721 because the original address is incorrect. Later, for a delivered order containing a 1500-piece animals jigsaw puzzle, you would like to exchange that puzzle for a 1500-piece art puzzle because you prefer art-themed puzzles over animal-themed ones, and you prefer to use your Mastercard ending in 6193 for any price difference. After that, you also want to return the wireless on-ear headphones from the same delivered order because you no longer need them, and you prefer the refund to be issued to the same Mastercard ending in 6193. Finally, you would like to cancel the pending order altogether because you no longer need the items, making the earlier address update moot.\n\nUse sofia.li5731@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6599568', 'address1': '7539 Jackson Street', 'address2': 'Unit 544', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '32721'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sofia_li_8235', 'address1': '7539 Jackson Street', 'address2': 'Unit 544', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '32721'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9323073', 'item_ids': ['6245746168'], 'new_item_ids': ['5546244844'], 'payment_method_id': 'credit_card_8296913'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9323073'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9323073', 'item_ids': ['5788631787'], 'payment_method_id': 'credit_card_8296913'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6599568', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.lopez2966@example.com',
        instruction='You are assisting Mason Lopez (email: mason.lopez2966@example.com). You want to update the shipping address for the pending order containing a Smart Watch, Electric Toothbrush, Makeup Kit, Patio Umbrella, and Sunglasses to 259 Elm Street, Apt 853, Fort Worth, TX, USA 11700, because it has not yet shipped. You also want to update the default address for future orders to the same, for consistency in delivery. Later, you would like to exchange the 500ml glass black water bottle from the delivered order (which included two laptops, a coffee maker, and another water bottle) for a 750ml glass black water bottle, because you prefer a larger capacity while keeping the same elegant glass design. You prefer to use your PayPal account to handle any price difference for the exchange, as it was your original payment method for this order.\n\nUse mason.lopez2966@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9222585', 'address1': '259 Elm Street', 'address2': 'Apt 853', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '11700'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mason_lopez_5208', 'address1': '259 Elm Street', 'address2': 'Apt 853', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '11700'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8185761', 'item_ids': ['8538875209'], 'payment_method_id': 'paypal_9591556'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8185761', 'item_ids': ['8538875209'], 'new_item_ids': ['4579334072'], 'payment_method_id': 'paypal_9591556'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.sanchez1292@example.com',
        instruction='You are assisting Aarav Sanchez (email: aarav.sanchez1292@example.com). You want to update the shipping address for a pending order containing a skateboard, jigsaw puzzle, grill, headphones, and mechanical keyboard to 1674 Cedar Road, Unit 309, San Antonio, TX, USA 15114, because the current Houston address is no longer valid. You would like to exchange a grey small nylon backpack with laptop compartment from a delivered order for a black large nylon backpack with camera compartment, because the new backpack better fits your gear and offers more space. You prefer to use the Mastercard ending in 5506 for any price difference associated with the exchange. Later, you want to update your default shipping address to 1674 Cedar Road, Unit 309, San Antonio, TX, USA 15114 to prevent future delivery issues.\n\nUse aarav.sanchez1292@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6348442', 'address1': '1674 Cedar Road', 'address2': 'Unit 309', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '15114'}),
            Action(name='modify_user_address', kwargs={'user_id': 'aarav_sanchez_9729', 'address1': '1674 Cedar Road', 'address2': 'Unit 309', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '15114'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5455653', 'item_ids': ['8054888773'], 'payment_method_id': 'credit_card_2690859'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5455653', 'item_ids': ['8054888773'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'credit_card_2690859'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting Sophia Patel (sophia.patel9841@example.com). You want to update the shipping address for her pending order (containing a tea kettle, electric kettle, sneakers, and a 100ml oriental men's perfume) to 1602 Oak Avenue, Suite 291, Columbus, OH, USA 34342, because it was originally set to Fort Worth, TX. You prefer to change the payment method to your Mastercard ending in 1639 for any price adjustments. You also want to modify the perfume in that order from 100ml to the 30ml version of the same oriental men's scent, as it better suits your needs. Later, you decide to cancel the entire pending order because you no longer need the items. After that, you would like to verify the cancellation status. Separately, for your delivered order containing a 17-inch black laptop with i7, 32GB, and 1TB SSD, you want to exchange it for the 15-inch space grey model with the same specs (i7, 32GB, 1TB SSD), as you prefer a more portable and visually distinct device. You prefer to use the same Mastercard ending in 1639 for any price difference in the exchange.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7905419', 'address1': '1602 Oak Avenue', 'address2': 'Suite 291', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '34342'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7905419', 'payment_method_id': 'credit_card_6419343'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7905419', 'item_ids': ['5421902839'], 'new_item_ids': ['1325156478'], 'payment_method_id': 'credit_card_6419343'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7905419', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2923184', 'item_ids': ['1684786391'], 'new_item_ids': ['6017636844'], 'payment_method_id': 'credit_card_6419343'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are assisting Sophia Thomas (sophia.thomas1364@example.com). You want to update the shipping address for a pending order to 1324 Park Drive, Apt 267, Phoenix, AZ, USA 68891 because it was originally set to a different Dallas address. You prefer to change the payment method from PayPal to your Visa card ending in 9858 for this order, as you no longer wish to use PayPal. You also want to exchange one of the office chairs — specifically the blue fabric chair with adjustable armrests and standard backrest — for the black fabric chair with no armrests and high-back support, because you prefer a more supportive and minimalist design. For any price difference from this change, you prefer to use your Mastercard ending in 2378. Later, you decide to cancel the entire order because you no longer need the items. After that, you would like to exchange the green 6mm PVC yoga mat from a previously delivered order for the blue 4mm PVC yoga mat, as you prefer a thinner and more compact mat in a different color. For any refund or charge related to this exchange, you prefer to use your Mastercard ending in 2378.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4862767', 'address1': '1324 Park Drive', 'address2': 'Apt 267', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '68891'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4862767', 'payment_method_id': 'credit_card_7326294'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4862767', 'item_ids': ['8323284863'], 'new_item_ids': ['1793929609'], 'payment_method_id': 'credit_card_7326294'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4862767', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4862767'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1867876', 'item_ids': ['7510236436'], 'new_item_ids': ['5586947715'], 'payment_method_id': 'credit_card_7326294'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.santos7683@example.com',
        instruction='You are assisting emma.santos7683@example.com. You want to first view the available products. Then, for a pending order with a blue leather office chair, bamboo skateboard, two water bottles, and a space grey laptop, you want to update the shipping address to a new location in Fort Worth. After that, you no longer need the items, so you want to cancel that entire order. You would like confirmation of the cancellation by reviewing the updated order status. Separately, for a delivered order containing a red mesh office chair, you want to exchange that chair for a black fabric high-back version because you prefer a more elegant and supportive design. You prefer the price difference to be handled using your Mastercard ending in 6380.\n\nUse emma.santos7683@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9903153', 'address1': '7089 Jefferson Avenue', 'address2': 'Unit 594', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '69541'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9903153', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9903153'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3113816', 'item_ids': ['4274709903'], 'new_item_ids': ['1793929609'], 'payment_method_id': 'credit_card_5869505'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.khan2146@example.com',
        instruction='You are assisting Daiki Khan (daiki.khan2146@example.com) with two requests. First, you want to exchange the blue Bluetooth Speaker with 10-hour battery life from the delivered order for the green Bluetooth Speaker with 20-hour battery life, because it offers longer usage time and better value. You prefer the price difference to be handled using your PayPal account. Later, you would like to update the shipping address for the pending order to 3017 Park Drive, Unit 96, Houston, TX, USA 22092, to ensure delivery to your new location.\n\nUse daiki.khan2146@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5861600', 'address1': '3017 Park Drive', 'address2': 'Unit 96', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '22092'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5861600', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2329074'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2329074', 'item_ids': ['6704763132'], 'new_item_ids': ['9440686670'], 'payment_method_id': 'paypal_8879986'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are James Martin (james.martin9857@example.com). You want to review the details of your pending order placed in San Diego, which includes a red cotton crew neck T-shirt in size XXL, along with a smart thermostat, wristwatch, garden hose, and green polyester backpack. You are interested in learning more about the T-shirt item in that order. Later, you would like to update the shipping address for this order to 1946 Pine Avenue, Apt 394, New York, NY, USA 16764, to have it delivered to your new location. At the same time, you would like to browse all available product types in the store to explore other offerings. After that, you would like to cancel your other pending order—also placed from San Diego—that includes a black nylon laptop backpack, an adjustable dumbbell set, and a pair of size 10 synthetic hiking boots—because you no longer need those items. You prefer the refund for the canceled order to be processed back to your original payment method, which is PayPal.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '1946 Pine Avenue', 'address2': 'Apt 394', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '16764'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3529525', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.santos8390@example.com',
        instruction="You are assisting a customer with email harper.santos8390@example.com who has a pending order containing an Electric Toothbrush (white, high speed settings, uses AA batteries), a men's 100ml fresh-scented perfume, a large grey memory foam pet bed, a 20MP 10x zoom digital camera, and a 12-inch white analog wall clock, originally set to ship to Charlotte, NC. You want to first confirm the details of the Electric Toothbrush in this order. Later, you would like to update the shipping address to 3277 Pine Avenue, Apt 416, San Diego, CA, USA 11152, and switch the payment method from PayPal to your Visa card ending in 8643. After that, you decide to cancel the entire order because it was placed by mistake, and you no longer wish to proceed with the purchase.\n\nUse harper.santos8390@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6629830'}),
            Action(name='get_product_details', kwargs={'product_id': '7352963235'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6629830', 'address1': '3277 Pine Avenue', 'address2': 'Apt 416', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '11152'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6629830', 'payment_method_id': 'credit_card_7507679'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6629830', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are James Martin, authenticated via james.martin9857@example.com, and you want to update the shipping address for your pending order (containing a red cotton crew neck T-Shirt, a Smart Thermostat, a Wristwatch, a Garden Hose, and a Backpack) from San Diego to 2446 Jackson Street, Unit 680, Chicago, IL, USA 96402 because it was initially entered incorrectly. You also want to change the payment method from PayPal to your Mastercard ending in 2067 for greater convenience and payment tracking. Additionally, you requested details about the T-Shirt (product ID 9523456873), which is a cotton crew neck style, to confirm its attributes ahead of any potential exchange considerations in the future.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '2446 Jackson Street', 'address2': 'Unit 680', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '96402'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3043531', 'payment_method_id': 'credit_card_6932154'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction='You are assisting Ava Kovacs (email: ava.kovacs4827@example.com) with her pending order originally shipped to Phoenix. You want to update the shipping address to 9598 Maple Lane, Floor 482, San Francisco, CA, USA 70257, because she has relocated temporarily and needs the package delivered to her new location. You also want to change the payment method from Mastercard ending in 3598 to her PayPal account, as she prefers using PayPal for better purchase protection and easier expense tracking. Additionally, you would like to review the details of the Skateboard in the order, which is a 31-inch plastic-deck model with a plain design, to confirm it meets her expectations before finalizing the changes.\n\nUse ava.kovacs4827@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '9598 Maple Lane', 'address2': 'Floor 482', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '70257'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4184032', 'payment_method_id': 'paypal_7443913'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4184032'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.johansson9391@example.com',
        instruction='You are Isabella Johansson, and your email is isabella.johansson9391@example.com. You want to cancel your pending order because you no longer need the vacuum cleaner, portable charger, e-reader, garden hose, and office chair included in it. Later, you would like to exchange the skateboard you received, which is a 31-inch plain bamboo model, for a smaller 28-inch bamboo skateboard with a graphic design because you prefer a more compact size and a visually distinctive deck. Before finalizing the exchange, you want to confirm the available skateboard variants to ensure the 28-inch bamboo graphic design option is in stock and suitable. You prefer the refund for the original skateboard to be returned to the same PayPal account used for the purchase.\n\nUse isabella.johansson9391@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2575533', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2575533'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3792453', 'item_ids': ['4293355847'], 'payment_method_id': 'paypal_3024827'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3792453', 'item_ids': ['4293355847'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'paypal_3024827'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li5953@example.com',
        instruction='You are assisting Sofia Li (sofia.li5953@example.com). You want to cancel the pending order placed by mistake, which includes items like blue wireless earbuds, two glass electric kettles (1.5L silver and 1L black), a soft-cover A6 notebook, and a pink yoga mat, and is scheduled for delivery to Philadelphia. Later, you would like to exchange one fleece jacket from the delivered order — specifically the black L full-zip fleece jacket — for a red L half-zip fleece jacket, because you prefer the red color and find the current black one too plain. Before finalizing the exchange, you want to review the available options for the Fleece Jacket to confirm color, size, and style availability. You prefer to use the Mastercard ending in 8609 for any price difference associated with the exchange.\n\nUse sofia.li5953@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1557241', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6874763'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6874763', 'item_ids': ['9385662952'], 'payment_method_id': 'credit_card_4046723'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6874763', 'item_ids': ['9385662952'], 'new_item_ids': ['8733974883'], 'payment_method_id': 'credit_card_4046723'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8560156827'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting Fatima Li (email: fatima.li1185@example.com). You want to upgrade the skateboard in your pending order from a maple deck to a bamboo deck, keeping the same 31-inch size and graphic design, because you prefer the lighter and more sustainable material. You prefer the price difference to be covered using your PayPal account, as it was your selected payment method for this order. Later, you requested to update the shipping address for another pending order containing a laptop and gaming mouse from your old address in Washington, DC to your new location in San Antonio, TX (2974 Pine Avenue, Suite 383, 79190), because you no longer reside at the original address. After that, you decided you no longer need the laptop and gaming mouse and would like to cancel that entire order, as your needs have changed and you no longer require the items.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8005719', 'item_ids': ['5120532699'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'paypal_6366157'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3510092', 'address1': '2974 Pine Avenue', 'address2': 'Suite 383', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '79190'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3510092', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.lopez2966@example.com',
        instruction='You are assisting Mason Lopez (email: mason.lopez2966@example.com) with modifying and managing his pending orders. You want to change the Electric Toothbrush in the pending order containing a Smart Watch, Makeup Kit, Patio Umbrella, and Sunglasses from the black, rechargeable version to the white version that uses AA batteries, because it better suits his preference for replaceable batteries and lighter color. You prefer the price difference to be handled using the PayPal account ending in 9591556. Later, you would like to update the shipping address for another pending order containing a white wooden 5 ft bookshelf to 866 Pine Avenue, Floor 702, Fort Worth, TX, USA 69150, to ensure delivery to a new location. After that, you would like to cancel that same order because the item is no longer needed, and you prefer the refund to be processed back to the original PayPal payment method.\n\nUse mason.lopez2966@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9222585'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9222585', 'item_ids': ['8098621301'], 'new_item_ids': ['2645006275'], 'payment_method_id': 'paypal_9591556'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3130816', 'address1': '866 Pine Avenue', 'address2': 'Floor 702', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '69150'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3130816', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.lopez6910@example.com',
        instruction='You are assisting Evelyn Lopez (email: evelyn.lopez6910@example.com) with two pending orders at the same San Diego address. You want to update the cycling helmet in her pending order from blue to red, keeping the same size (S) but accepting a slight reduction in ventilation, because she prefers the red color. You prefer the change to be processed using her Mastercard ending in 8951 for any price difference. Later, you will request to cancel her other pending order that includes white leather running shoes in size 10 and a medium electric grill with a side burner, because she no longer needs those items.\n\nUse evelyn.lopez6910@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1890669'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W1890669', 'item_ids': ['1676105083'], 'new_item_ids': ['3358616356'], 'payment_method_id': 'credit_card_3566337'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3007862', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.wilson1253@example.com',
        instruction='You are assisting lei.wilson1253@example.com with their pending order placed in Jacksonville, FL. You initially want to update the Wireless Earbuds in the order from black to white, as you prefer the white color for aesthetic consistency with your other devices. For any price difference, you prefer to use your Mastercard ending in 1531. Later, you decide to cancel the entire order because you no longer need the items, including the earbuds, espresso machine, headphones, smartphone, and tablet. You would like the cancellation processed promptly and the full refund issued back to the original payment method.\n\nUse lei.wilson1253@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3826449'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3826449', 'item_ids': ['5565631513'], 'new_item_ids': ['2052249669'], 'payment_method_id': 'credit_card_3677959'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3826449', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com) with modifying his pending order that includes a laptop, hiking boots, and an air purifier, currently shipping to Indianapolis. You want to update the shipping address to 2151 Cedar Road, Floor 598, Oklahoma City, OK, USA 71273, because he needs it delivered to a different location. You prefer to change the payment method from the original gift card to his Mastercard ending in 3762 for better expense tracking. You also want to upgrade the laptop in the order from the 13-inch black model with 512GB SSD to the 15-inch space grey model with 1TB SSD, as it offers more storage and a larger screen for his work needs. Later, you will request to cancel another pending order for a grey medium polyester backpack with a laptop compartment, currently set to ship to Washington, DC, because he no longer needs it.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '2151 Cedar Road', 'address2': 'Floor 598', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '71273'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2564042', 'item_ids': ['1657832319'], 'new_item_ids': ['6017636844'], 'payment_method_id': 'credit_card_8405687'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6885344', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.martin9857@example.com',
        instruction='You are assisting James Martin (email: james.martin9857@example.com) with two pending orders. First, for his order containing a red XXL cotton crew neck T-shirt, a smart thermostat, a wristwatch, a garden hose, and a green small polyester backpack, you want to update the shipping address to 5496 Maple Lane, Floor 471, Nashville, TN, USA 27438 because he needs it delivered to a different location. You also want to change the payment method from PayPal to his Visa card ending in 1826, as he prefers to use this card for the transaction. Additionally, you would like to exchange the red XXL cotton crew neck T-shirt for a blue M cotton crew neck T-shirt, as the original size and color do not fit his needs, and use his Mastercard ending in 2067 for any price difference, since it is his preferred backup payment method. Later, you will cancel his other pending order that includes a black small nylon laptop backpack, an adjustable dumbbell set, and hiking boots, because he placed it by mistake and no longer wants those items.\n\nUse james.martin9857@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3043531', 'address1': '5496 Maple Lane', 'address2': 'Floor 471', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '27438'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3043531', 'payment_method_id': 'credit_card_7083997'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3043531', 'item_ids': ['9354168549'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'credit_card_6932154'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3043531'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3529525', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.brown8893@example.com',
        instruction='You are assisting Anya, who is reachable at anya.brown8893@example.com. You want to update the shipping address for her pending order—containing a 6-inch, 8GB Wi-Fi e-reader and a black leather-band AMOLED smart watch—from Dallas, TX to 9079 Washington Boulevard, Suite 700, Charlotte, NC, USA 74329, because she needs it delivered to a different location. After that, you would like to change the payment method from Mastercard ending in 9625 to her PayPal account, as she prefers using it for this purchase. Later, you will cancel the entire order because she has changed her mind and no longer needs the items.\n\nUse anya.brown8893@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8883368', 'address1': '9079 Washington Boulevard', 'address2': 'Suite 700', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '74329'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8883368', 'payment_method_id': 'paypal_5206520'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8883368'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8883368', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting a customer with email fatima.li1185@example.com regarding her pending order containing a 31 inch maple deck skateboard with a graphic design and a 15 bar capsule-type espresso machine with a 1.5L water tank. You want to first update the shipping address to 2542 Main Street, Suite 364, Austin, TX, USA 21535 because she needs it delivered to a different location. You also prefer to change the payment method to the Visa card ending in 1373 for better expense tracking. Later, you will cancel the entire order because she no longer needs the items, making the earlier updates obsolete.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8005719', 'address1': '2542 Main Street', 'address2': 'Suite 364', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '21535'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8005719', 'payment_method_id': 'credit_card_2713802'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8005719', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.patel2010@example.com',
        instruction='You are assisting Evelyn Patel (email: evelyn.patel2010@example.com) with her pending order. You want to exchange the purple XL cotton crew neck T-Shirt for a blue medium cotton crew neck T-Shirt because it better fits her preference in size and color. You also want to update the shipping address to 454 Park Drive, Unit 13, Seattle, WA, USA 44931, as she has relocated within the city. You prefer to use PayPal (ending in 3704667) for any price difference associated with the exchange. After these changes are completed, you would like to view all product types currently offered in the catalog to explore additional items of interest.\n\nUse evelyn.patel2010@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6385395'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6385395', 'item_ids': ['8124970213'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_3704667'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6385395', 'address1': '454 Park Drive', 'address2': 'Unit 13', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '44931'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_patel_8882', 'address1': '454 Park Drive', 'address2': 'Unit 13', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '44931'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.sanchez1556@example.com',
        instruction='You are assisting Mia Sanchez (mia.sanchez1556@example.com) with her pending order. You want to change the Makeup Kit in her order from the current light skin tone to the dark skin tone variant, keeping the same brand (Brand B) and professional size because it better matches her skin tone. You prefer to use her PayPal account to cover the price difference. You also want to update the shipping address for this order to 6237 Adams Road, Floor 384, San Antonio, TX, USA 94228, and update her default address to the same for future orders. Later, you would like to browse the product catalog to see what types of items are available, particularly interested in current offerings across all categories.\n\nUse mia.sanchez1556@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W4096800'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4096800', 'item_ids': ['7902309762'], 'new_item_ids': ['5012998807'], 'payment_method_id': 'paypal_9064553'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4096800', 'address1': '6237 Adams Road', 'address2': 'Floor 384', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '94228'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mia_sanchez_3401', 'address1': '6237 Adams Road', 'address2': 'Floor 384', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '94228'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '5149340237'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction="You are Omar Silva, with email omar.silva4147@example.com. You want to change the payment method for your pending order—containing a fantasy-themed 2000-piece jigsaw puzzle, an animal-themed 2000-piece jigsaw puzzle, a brown wooden bookshelf, a silver 4K action camera, and polarized green-lens sunglasses—from a gift card to your PayPal account, because you prefer using PayPal for better purchase protection. Later, you will cancel the order with the reason 'no longer needed', as you no longer require these items. Separately, you would like to explore the T-Shirt catalog to see available options and prices, particularly interested in variations by color, size, material, and style such as crew neck or v-neck, to evaluate potential future purchases.\n\nUse omar.silva4147@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9728773', 'payment_method_id': 'paypal_2192303'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are Fatima Li (email: fatima.li1185@example.com) and you have a pending order containing a skateboard and an espresso machine. You want to update the payment method for this order from PayPal to your Visa card ending in 1373 because you prefer to use that card for this purchase. After updating the payment, you intend to cancel the entire order because it was placed by mistake. Separately, you would like to explore the full range of product types available, with a specific interest in the espresso machine line, to understand the different options in terms of pressure, capacity, and type (manual, automatic, capsule) for future consideration.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8005719', 'payment_method_id': 'credit_card_2713802'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8005719', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4354588079'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.kovacs2446@example.com',
        instruction='You are assisting Harper Kovacs (harper.kovacs2446@example.com). You want to update the shipping address for a pending order containing two green small polyester backpacks with laptop compartments, a white 10-inch digital wall clock, a HEPA filter air purifier for medium rooms, and a 1-liter glass tea kettle to 6505 Adams Road, Suite 745, Chicago, IL, USA 20276. You also want your default address updated to this same new address because you’ve relocated. Later, you would like to exchange a 30MP digital camera with 10x zoom and SD card storage, which was delivered in a previous order, for a model with 3x zoom and the same resolution and storage type, because you prefer a more compact and lightweight camera for everyday use. You prefer the refund for the price difference to be issued back to your Visa card ending in 2080, which was used for the original purchase.\n\nUse harper.kovacs2446@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9093821', 'address1': '6505 Adams Road', 'address2': 'Suite 745', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '20276'}),
            Action(name='modify_user_address', kwargs={'user_id': 'harper_kovacs_8617', 'address1': '6505 Adams Road', 'address2': 'Suite 745', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '20276'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9093821', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3065353'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3065353', 'item_ids': ['9228757377'], 'new_item_ids': ['1804581713'], 'payment_method_id': 'credit_card_7422485'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.moore2450@example.com',
        instruction='You are Ava Moore (ava.moore2450@example.com). You initially wanted to update the shipping address for your pending order containing a silver 8-inch tablet, a blue 25ft vinyl garden hose, and a black large polyester backpack to 5875 Park Drive, Suite 683, Jacksonville, FL, USA 86292, and also update your default address to this location. Later, you decided to cancel that pending order because it was no longer needed. After that, you would like to exchange the skateboard from your delivered order — which currently has a graphic design on a 34-inch plastic deck — for the same size and material model but with a plain design, because you prefer a more minimalist look. You prefer to use your PayPal account for any price difference associated with the exchange.\n\nUse ava.moore2450@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8331214', 'address1': '5875 Park Drive', 'address2': 'Suite 683', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '86292'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_moore_4814', 'address1': '5875 Park Drive', 'address2': 'Suite 683', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '86292'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8331214', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8331214'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8495163', 'item_ids': ['5489028872'], 'new_item_ids': ['3098764622'], 'payment_method_id': 'paypal_7478252'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.kovacs6466@example.com',
        instruction="You are assisting Mason Kovacs (email: mason.kovacs6466@example.com). You want to modify the pending order that includes polarized metal sunglasses with a black frame and green lenses, exchanging them for the same style with a silver frame and black lenses because you prefer the latter look. You also want to update the shipping address to 1308 Oak Avenue, Apt 563, Los Angeles, CA, USA 99763, as the delivery location has changed. You prefer to use your Mastercard ending in 4608 for any price difference. Later, you decide to cancel the entire order because you no longer need the items. After cancellation, you would like to explore the store's product catalog, specifically viewing details about backpacks, as you are considering a future purchase for everyday use.\n\nUse mason.kovacs6466@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6030855'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6030855', 'item_ids': ['2177260429'], 'new_item_ids': ['2198125883'], 'payment_method_id': 'credit_card_4314033'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6030855', 'address1': '1308 Oak Avenue', 'address2': 'Apt 563', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '99763'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6030855', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.patel3402@example.com',
        instruction='You are assisting daiki.patel3402@example.com, who first wanted to explore the available product types, particularly the Bookshelf options. You want to exchange the delivered 3 ft white glass Bookshelf for the 5 ft white glass version from the same product line, as the larger size better fits their space. You prefer the same material and color for consistency in their living room. Later, you would like the price difference to be processed using your PayPal account, as it was the original payment method and offers convenient transaction handling.\n\nUse daiki.patel3402@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8600330539'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3135192'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3135192', 'item_ids': ['2989722512'], 'payment_method_id': 'paypal_1009053'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3135192', 'item_ids': ['2989722512'], 'new_item_ids': ['8895454203'], 'payment_method_id': 'paypal_1009053'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.lopez2997@example.com',
        instruction='You are Raj Lopez, with email raj.lopez2997@example.com. You want to update the shipping address for your pending order—which includes a stainless steel black 500ml water bottle, a bamboo 31-inch graphic skateboard, and synthetic size 9 waterproof hiking boots—to 8916 Adams Road, Apt 811, Austin, TX, USA 61731, because it was shipped to an old address. You also want your default address updated to this new one for future orders. After that, you would like to cancel this order because it was placed by mistake. Later, you want to review your other pending order containing a black small polyester crew neck T-shirt and a bagless canister vacuum cleaner with pet hair removal. You prefer to change the payment method for this order to your PayPal account. Then, you would like to exchange the black small polyester T-shirt for a blue medium cotton crew neck T-shirt, as you prefer cotton over polyester and a larger size in a different color, and you want any price difference handled through the same PayPal payment. After that, you would like to browse the full range of product types offered, particularly focusing on T-Shirts, to better understand available styles, materials, and options for future purchases.\n\nUse raj.lopez2997@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3502364', 'address1': '8916 Adams Road', 'address2': 'Apt 811', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '61731'}),
            Action(name='modify_user_address', kwargs={'user_id': 'raj_lopez_5873', 'address1': '8916 Adams Road', 'address2': 'Apt 811', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '61731'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3502364', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7162915'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7162915', 'payment_method_id': 'paypal_7007375'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7162915', 'item_ids': ['1176194968'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_7007375'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.smith9157@example.com',
        instruction="You are Olivia Smith, with email olivia.smith9157@example.com. You want to update the shipping address for your pending order, which includes a red large mountain bicycle, men's fresh-scent 50ml perfume, a 31-inch bamboo custom-design skateboard, and a 30MP 5x zoom digital camera, to 1220 Adams Road, Apt 329, Philadelphia, PA, USA 53054 because you need it delivered to a new location. Later, you would like to exchange the blue medium cycling helmet from your delivered order for the same model in red, size medium, with high ventilation, because you prefer the color and improved airflow. You prefer any price difference for the exchange to be handled using your PayPal account.\n\nUse olivia.smith9157@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1348609', 'address1': '1220 Adams Road', 'address2': 'Apt 329', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '53054'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3794101', 'item_ids': ['3339188619'], 'new_item_ids': ['8573379326'], 'payment_method_id': 'paypal_2076152'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.hernandez3039@example.com',
        instruction="You are assisting Sofia Hernandez (sofia.hernandez3039@example.com). You want to update the shipping address for her pending portable gas grill order from Seattle, WA to 123 Oak Avenue, Apt 5, Portland, OR, USA 97201 because she needs it delivered to a new location. If the address cannot be changed, you would like to cancel the order with the reason 'ordered by mistake'. Separately, for her delivered order containing a red large v-neck cotton T-shirt, you would like to exchange it for a blue medium crew neck cotton T-shirt because the original did not fit and she prefers the crew neck style in a smaller size. You prefer to use her Visa card ending in 7312 for any price difference associated with the exchange.\n\nUse sofia.hernandez3039@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3561391', 'address1': '123 Oak Avenue', 'address2': 'Apt 5', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '97201'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3561391', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6876713'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6876713', 'item_ids': ['3234800602'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'credit_card_7901829'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com) with his pending order. You want to confirm the shipping address as 690 Broadway, Suite 737, Indianapolis, IN, USA 46226, which is already correctly listed, to ensure delivery accuracy. You would like to change the payment method from the current gift card to your Mastercard ending in 3762, because you prefer using your card for better purchase tracking and warranty support. Later, you want to review the product details of the Backpack (product ID: 2524789262), particularly interested in variants with a laptop or camera compartment, available in colors like black, green, or grey, and in sizes ranging from small to large, to evaluate a future purchase based on material preference (nylon, leather, or polyester) and functional needs.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '690 Broadway', 'address2': 'Suite 737', 'city': 'Indianapolis', 'state': 'IN', 'country': 'USA', 'zip': '46226'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.patel3193@example.com',
        instruction="You are Mei Patel, authenticated via mei.patel3193@example.com, and you have a pending order currently set to ship to Fort Worth, TX. You want to update the shipping address to a new location in Charlotte, NC (9744 Maple Lane, Unit 64) because you will not be available to receive the package at the original address. You also prefer to change the payment method from PayPal to your Visa card ending in 9904 for better rewards and spending tracking. After these updates, you would like to review the items in your order, which include a men's oriental 100ml perfume, a 2-piece red softshell luggage set, an adjustable 30-50 lbs iron dumbbell set, and a 25ft green latex garden hose. Subsequently, you want to see the available options for the Perfume product to consider potential future purchases, particularly interested in variants with different scent families (such as fresh or woody), sizes (including 30ml and 50ml), and gender-specific versions, while noting that the current item in your order is the oriental 100ml men's version.\n\nUse mei.patel3193@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9583042', 'address1': '9744 Maple Lane', 'address2': 'Unit 64', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '46280'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9583042', 'payment_method_id': 'credit_card_9503061'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9583042'}),
            Action(name='get_product_details', kwargs={'product_id': '6858788497'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella.sanchez6218@example.com',
        instruction='You are assisting Isabella Sanchez (email: isabella.sanchez6218@example.com). You want to modify the skateboard in her pending order (containing a bamboo 28-inch plain design skateboard and a black Bluetooth speaker) from the plain design to the graphic design version because she prefers a more visually striking look. Later, you will update the shipping address for this order to 1692 Pine Avenue, Floor 324, Denver, CO, USA 40897, and also update her default address to the same location for future convenience. After that, you would like to exchange the black leather band smart watch in her delivered order (shipped to New York) for the gold leather band version with LCD display because she prefers a more elegant and premium appearance. You prefer any price difference to be handled using her PayPal account, which she has used for previous purchases. Finally, you want to browse all available product types in the store to explore future purchase options.\n\nUse isabella.sanchez6218@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4386313', 'address1': '1692 Pine Avenue', 'address2': 'Floor 324', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '40897'}),
            Action(name='modify_user_address', kwargs={'user_id': 'isabella_sanchez_2068', 'address1': '1692 Pine Avenue', 'address2': 'Floor 324', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '40897'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4386313', 'item_ids': ['8176740019'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'paypal_8516781'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1713682'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1713682', 'item_ids': ['1007724142'], 'new_item_ids': ['9408160950'], 'payment_method_id': 'paypal_8516781'}),
            Action(name='get_product_details', kwargs={'product_id': '6945232052'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.kim8981@example.com',
        instruction='You are Omar Kim, authenticated via email omar.kim8981@example.com, and you want to check the status of your pending order that includes a 500-piece beginner-level art-themed jigsaw puzzle, a white small cycling helmet, two tea kettles (one glass 1-liter and one ceramic 1.5-liter), and a navy small nylon backpack. You would like to review the details of the jigsaw puzzle to confirm its theme and difficulty level before proceeding. After reviewing, you want to update the shipping address for this pending order to a new location in New York City, specifically to 871 Maple Lane, Unit 924, New York, NY, USA 73131, to ensure delivery to your current residence. Later, you would like to browse the full catalog of available product types, including items like backpacks, cycling helmets, tea kettles, puzzles, e-readers, smartwatches, and luggage sets, to explore options for future purchases.\n\nUse omar.kim8981@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8557584'}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8557584', 'address1': '871 Maple Lane', 'address2': 'Unit 924', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '73131'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.nguyen5072@example.com',
        instruction='You are Mia Nguyen, and your email is mia.nguyen5072@example.com. You want to review the current status and contents of your pending order, which includes a 1000-piece expert-level animal-themed jigsaw puzzle, a 2K-resolution indoor security camera with Ethernet connectivity, and black wireless earbuds with IPX7 water resistance and 6-hour battery life, because you are confirming what was ordered. You also want to learn more about the jigsaw puzzle product, specifically the 1000-piece animal-themed expert version, to understand its features and available alternatives in the product line. Later, you would like to update the shipping address for this order to 6126 Maple Lane, Suite 33, Philadelphia, PA, USA 23750, so it can be delivered to a different location. After that, you would like to cancel your other pending order containing a silver 10-inch tablet with 128GB storage, a black 3-piece softshell luggage set, black synthetic sneakers in size 6, and a red large cycling helmet with high ventilation, because you no longer need those items. Finally, you would like to see a list of all product types currently available in the catalog to explore what other items you might be interested in purchasing in the future.\n\nUse mia.nguyen5072@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W4657527'}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4657527', 'address1': '6126 Maple Lane', 'address2': 'Suite 33', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '23750'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7259788', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.li4862@example.com',
        instruction='You are Mason Li, with email mason.li4862@example.com, who initially wants to browse the product catalog and update the shipping address for a pending order containing a black Desk Lamp to 7537 Park Drive, Apt 265, Los Angeles, CA, USA 67943, because it no longer matches his current location; you also want to update your default address to the same for future orders. Additionally, you would like to return the Skateboard from a delivered order because it does not suit your needs, and you prefer the refund to be issued back to your gift card for future use. Later, you decide to cancel the pending Desk Lamp order because you no longer need it, and you would like confirmation of the cancellation. After that, you want to explore details of the Action Camera product, particularly models with 4K resolution and waterproof features, to evaluate it for a potential future purchase.\n\nUse mason.li4862@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2392556', 'address1': '7537 Park Drive', 'address2': 'Apt 265', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '67943'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mason_li_6934', 'address1': '7537 Park Drive', 'address2': 'Apt 265', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '67943'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8998368', 'item_ids': ['9594745976'], 'payment_method_id': 'gift_card_6486968'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2392556', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2392556'}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason.kovacs6466@example.com',
        instruction='You are assisting a customer with email mason.kovacs6466@example.com who first wanted to explore the available product types, particularly T-Shirts, to understand the catalog offerings. You want to confirm that T-Shirts are available for future consideration. Later, you would like to update the shipping address for a pending order—currently shipping to Seattle—for an order containing polarized black-framed sunglasses with green lenses and a black Bluetooth speaker. You prefer the new address to be 3433 Maple Lane, Floor 860, Las Vegas, NV, USA 57426, to ensure delivery to the correct location. You prefer the payment method remains the same, as the original purchase was made with a credit card.\n\nUse mason.kovacs6466@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6030855', 'address1': '3433 Maple Lane', 'address2': 'Floor 860', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '57426'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting Yusuf Gonzalez (email: yusuf.gonzalez2399@example.com). You want to first update the shipping address for his pending order (currently in Los Angeles) to 4241 Elm Street, Unit 353, Nashville, TN, USA 46176, so it reaches his new location. You also want to change the payment method for this order to PayPal, as you prefer that for tracking and refund control. Additionally, you would like to exchange the ceramic 1.5-liter tea kettle in the order for the stainless steel 2-liter version, as it better suits your stovetop and capacity needs, and you prefer any price difference to be refunded to your PayPal account. Later, you decided you no longer need the updated order and would like to cancel it entirely. After cancellation, you want to confirm the order status to ensure it has been fully canceled. Subsequently, you would like to initiate a return for the blue cotton T-shirt (size M) from your earlier delivered order, as it doesn’t fit your needs, and you prefer the refund to be processed back to your PayPal account for consistency and faster access.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '4241 Elm Street', 'address2': 'Unit 353', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '46176'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2806889', 'item_ids': ['7497340597'], 'new_item_ids': ['4238115171'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2806889', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1679211', 'item_ids': ['9612497925'], 'payment_method_id': 'paypal_3022415'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction="You are Olivia Ito, with email olivia.ito5204@example.com. You want to update the shipping address for your pending order (with a gaming mouse, patio umbrella, and hiking boots) to 3295 Jefferson Avenue, Apt 173, Boston, MA, USA 28145, because you've moved temporarily for work. You would like to change the payment method from your Visa ending in 9182 to your PayPal, as you prefer using it for online purchases. You also prefer the white wireless gaming mouse over the black wired one currently in the order, because you want a cleaner look and wireless convenience, and you agree to pay any price difference via PayPal. Later, you will cancel another pending order (for a wristwatch and backpack) because you placed it by mistake. After that, you would like to return the black sneakers from your delivered order (which also included an espresso machine) and receive a refund to your gift card, as they don’t fit and you’d like to save the credit for future use.\n\nUse olivia.ito5204@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '3295 Jefferson Avenue', 'address2': 'Apt 173', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '28145'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5442520', 'item_ids': ['3330317167'], 'new_item_ids': ['8896479688'], 'payment_method_id': 'paypal_8049766'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7941031', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5866402'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5866402', 'item_ids': ['9727387530'], 'payment_method_id': 'gift_card_7794233'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito (olivia.ito5204@example.com) and you have a pending order currently set for delivery to Denver, CO. You want to change the payment method from credit card to PayPal because you prefer using PayPal for online purchases. You also want to exchange the black wired gaming mouse in your order for the white wireless version because you prefer a wireless setup and a lighter color that matches your desk setup. You are interested in learning more about the Gaming Mouse product, particularly its available configurations, to ensure the white wireless model meets your needs. Later, you would like to update the shipping address for this order to 2858 Maple Lane, Floor 934, Nashville, TN, 98316, and also update your default address to the same location because you have relocated. After these updates, you would like to cancel the entire order because you no longer need the items, including the updated mouse and other contents such as the patio umbrella and hiking boots.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5442520'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5442520', 'item_ids': ['3330317167'], 'new_item_ids': ['8896479688'], 'payment_method_id': 'paypal_8049766'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '5713490933'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '2858 Maple Lane', 'address2': 'Floor 934', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '98316'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_ito_3591', 'address1': '2858 Maple Lane', 'address2': 'Floor 934', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '98316'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5442520', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.khan2360@example.com',
        instruction='You are assisting Olivia Khan (email: olivia.khan2360@example.com) with her pending order. You want to change the payment method from PayPal to her Mastercard ending in 2184 because she prefers using her card for this purchase. You also want to exchange the red small cotton crew neck T-Shirt for a blue medium cotton crew neck T-Shirt of the same product because the original size and color no longer suit her needs. You would like to review the available options for the T-Shirt product to understand the full range of styles and colors. Later, you want to update the shipping address for the order to 1918 Oak Avenue, Apt 530, Austin, TX, USA 46495, and also update her default address to this new location in Austin for future orders. After that, you would like to cancel the entire order because she no longer needs the items.\n\nUse olivia.khan2360@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3840181'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3840181', 'payment_method_id': 'credit_card_7376788'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3840181', 'item_ids': ['3542102174'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'credit_card_7376788'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3840181', 'address1': '3724 Washington Boulevard', 'address2': 'Suite 499', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '76510'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_khan_9030', 'address1': '3724 Washington Boulevard', 'address2': 'Suite 499', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '76510'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3840181', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.lee9368@example.com',
        instruction='You are Yara Lee (email: yara.lee9368@example.com). You want to return the blue Bluetooth Speaker with 10-hour battery life and no water resistance from your delivered order, because you no longer need it. You prefer the refund to be issued to your Visa card ending in 6367. Later, you want to update the shipping address for your pending order — which includes a red leather high-back office chair, hiking boots, and a full-size mechanical keyboard — to 5454 Washington Boulevard, Apt 694, Columbus, OH, USA 19529. You also want to change the payment method for that pending order to your Visa card ending in 6367. After that, you would like to browse all available product types in the catalog to explore other offerings.\n\nUse yara.lee9368@example.com for authentication.',
        actions=[
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1341845', 'item_ids': ['6704763132'], 'payment_method_id': 'credit_card_6450164'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3320020', 'address1': '5454 Washington Boulevard', 'address2': 'Apt 694', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '19529'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3320020', 'payment_method_id': 'credit_card_6450164'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.ahmed1696@example.com',
        instruction="You are assisting a customer with email lei.ahmed1696@example.com who has a pending order in Philadelphia. You want to first modify the large black cycling helmet with low ventilation to a smaller size S in red with low ventilation, because it may not fit properly, and you prefer to use the Mastercard ending in 3705 for any price difference. Later, you will cancel the entire order because you've changed your mind and no longer need the items.\n\nUse lei.ahmed1696@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9132840'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9132840', 'item_ids': ['6048672633'], 'new_item_ids': ['3358616356'], 'payment_method_id': 'credit_card_3593714'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9132840', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.moore2816@example.com',
        instruction='You are assisting a customer who placed a pending order in Phoenix for a glass 1.5L induction-compatible tea kettle and prefers stainless steel over glass for durability and aesthetics. You want to modify the current item to the stainless steel 1.5L induction-compatible version because it better matches their kitchenware preferences and is compatible with their induction stove. You prefer any price adjustment to be processed using the Mastercard ending in 3161. Later, after the modification, you decided you no longer need the item and would like to cancel the entire order.\n\nUse harper.moore2816@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W3942868'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3942868', 'item_ids': ['6454334990'], 'new_item_ids': ['3738831434'], 'payment_method_id': 'credit_card_7665260'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3942868', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction='You are Ava Kovacs, email ava.kovacs4827@example.com, and you want to exchange your delivered 28-inch plastic plain-design skateboard for a 28-inch bamboo deck skateboard with a graphic design because you prefer a more eco-friendly material and a visually distinctive style. You prefer the price difference to be handled using your Mastercard ending in 3598. Later, you want to update the shipping address for your pending order to 3681 Lincoln Street, Unit 455, Houston, TX, USA 46637, and also update your default account address to this new Houston address for future orders. After that, you would like to cancel your pending order because you no longer need the items.\n\nUse ava.kovacs4827@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6344370'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6344370', 'item_ids': ['4545791457'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'credit_card_9699699'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '3681 Lincoln Street', 'address2': 'Unit 455', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '46637'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_kovacs_3448', 'address1': '3681 Lincoln Street', 'address2': 'Unit 455', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '46637'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4184032', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction='You are assisting Yusuf Gonzalez (email: yusuf.gonzalez2399@example.com). You want to exchange the blue medium cotton crew neck T-shirt from your delivered order (which included a tablet, e-reader, puzzle, and the T-shirt) for a purple XL cotton crew neck T-shirt, because you prefer the larger size and different color. You prefer the price difference to be handled using your PayPal account. Later, you want to update the shipping address for your pending order (containing a smartphone and tea kettle) from Los Angeles to 7748 Oak Avenue, Apt 945, Charlotte, NC, USA 66301, because it was originally set to an old address. You also want to update your default address to this new one for future orders. After that, you would like to cancel your other pending order (which includes a bookshelf, LED bulb, tablet, and sunglasses) because you no longer need it.\n\nUse yusuf.gonzalez2399@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1679211'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1679211', 'item_ids': ['9612497925'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'paypal_3022415'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2806889', 'address1': '7748 Oak Avenue', 'address2': 'Apt 945', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '66301'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_gonzalez_8900', 'address1': '7748 Oak Avenue', 'address2': 'Apt 945', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '66301'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2230795', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.taylor6118@example.com',
        instruction='You are Yusuf Taylor, and your email is yusuf.taylor6118@example.com. You want to update the shipping address for your pending order, which includes a white glass bookshelf and a pink yoga mat, to 943 Maple Drive, Suite 356, Chicago, IL, USA 60621, because it was originally set to a different location. You would also like to exchange the red cycling helmet in size S from your delivered order for the same model in size M, color red, which has higher ventilation, because it fits better and meets your comfort needs. You prefer any price difference to be processed using your Visa card ending in 4012. Later, you are interested in learning more about the Backpack product for a potential future purchase. After that, you would like to cancel another pending order containing a white USB desk lamp because it was placed by mistake.\n\nUse yusuf.taylor6118@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2702727', 'address1': '943 Maple Drive', 'address2': 'Suite 356', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '60621'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2702727'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5690487', 'item_ids': ['3358616356'], 'new_item_ids': ['8573379326'], 'payment_method_id': 'credit_card_3599838'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5690487', 'item_ids': ['3358616356'], 'payment_method_id': 'credit_card_3599838'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8268610', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.ito3790@example.com',
        instruction='You are Emma Ito, with email emma.ito3790@example.com, and you want to update your pending order for a 1000ml stainless steel water bottle. You prefer to change the payment method from PayPal to your Visa card ending in 3660 because you want to use a different funding source. You also want the shipping address for this order updated to 500 Adams Road, Floor 511, Detroit, MI, USA 95144, to ensure delivery to your new location. After that, you would like your default account address updated to the same Detroit address for consistency across future orders. Finally, you prefer to swap the water bottle color from blue to black, keeping the same 1000ml stainless steel version, because you prefer the black finish, and you want any price difference to be handled using the same Visa card ending in 3660.\n\nUse emma.ito3790@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8664580'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8664580', 'payment_method_id': 'credit_card_8058445'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8664580', 'address1': '500 Adams Road', 'address2': 'Floor 511', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '95144'}),
            Action(name='modify_user_address', kwargs={'user_id': 'emma_ito_4529', 'address1': '500 Adams Road', 'address2': 'Floor 511', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '95144'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8664580', 'item_ids': ['2366567022'], 'new_item_ids': ['7661609223'], 'payment_method_id': 'credit_card_8058445'}),
            Action(name='get_product_details', kwargs={'product_id': '8310926033'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting Lucas Johansson (lucas.johansson7741@example.com) with modifications to his pending order. You want to change the payment method from Mastercard ending in 3088 to Visa ending in 9452 for better card rewards. You would like the shipping address updated to 8664 Madison Drive, Unit 373, Portland, OR, USA 93608, as it is more convenient for delivery. You prefer to exchange the small black nylon backpack with a laptop compartment for the large black nylon backpack with a camera compartment because it offers more space and better organization for travel gear. After that, you would like to update your default shipping address to 8664 Madison Drive, Unit 373, Portland, OR, USA 93608 for all future orders to ensure consistency and convenience.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '8664 Madison Drive', 'address2': 'Unit 373', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '93608'}),
            Action(name='modify_user_address', kwargs={'user_id': 'lucas_johansson_1090', 'address1': '8664 Madison Drive', 'address2': 'Unit 373', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '93608'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5073920', 'item_ids': ['7824298782'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'credit_card_1864112'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.ito2168@example.com',
        instruction='You are assisting Evelyn Ito (email: evelyn.ito2168@example.com), who has a pending order containing a green leather small backpack with a camera compartment and a black Bluetooth speaker with 20 hours of battery life. You want to update the shipping address for this order from San Diego, California to 4693 Adams Road, Unit 283, San Antonio, Texas, because she needs it delivered to a new location. Later, you would like to change the payment method from her Visa card ending in 5896 to her PayPal account for greater convenience. After that, you plan to cancel the entire order because she no longer needs the items. Additionally, you want to review all available product types in the store to explore future purchase options, as she is interested in browsing the full catalog.\n\nUse evelyn.ito2168@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6207110', 'address1': '4693 Adams Road', 'address2': 'Unit 283', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '62407'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6207110', 'payment_method_id': 'paypal_5377635'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6207110', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6207110'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting a customer with email yusuf.garcia2909@example.com regarding their pending order containing Hiking Boots, a Laptop, and an Air Purifier, originally shipped to Indianapolis. You want to update the shipping address to 404 Pine Avenue, Floor 874, New York, NY, USA 71261, because the original address is incorrect. You also want to change the payment method from a gift card to your Mastercard ending in 3762 for better expense tracking. After making these updates, you decide to cancel the entire order because it was placed by mistake. You would like to verify the final order details to confirm that all changes, including cancellation, have been correctly processed. Later, you want to browse the full catalog to see all available product types for future shopping reference. After that, you would like detailed information about the Laptop product, particularly interested in models with 13-inch to 17-inch screens, i5 to i9 processors, 8GB to 32GB RAM, and various storage and color options, to evaluate potential future purchases.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '404 Pine Avenue', 'address2': 'Floor 874', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '71261'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are Lei Li, with email lei.li8350@example.com. You want to exchange the black electric toothbrush from your delivered order for a white one, because you prefer the color white over black. You prefer the refund or charge for any price difference to be applied to your Visa ending in 2697. Later, you want to update the shipping address for your pending laptop order to 6851 Pine Avenue, Floor 687, Philadelphia, PA, USA 49448, because you have relocated temporarily. You also want to change the payment method for this order from PayPal to your Visa ending in 2697, because you prefer to consolidate payments on your credit card. After that, you would like to cancel your other pending order containing a digital camera, electric kettle, and wall clock, because you no longer need the items.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6289770'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6289770', 'item_ids': ['8098621301'], 'new_item_ids': ['2645006275'], 'payment_method_id': 'credit_card_4466831'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '6851 Pine Avenue', 'address2': 'Floor 687', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '49448'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5166363', 'payment_method_id': 'credit_card_4466831'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3414433', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.sanchez1479@example.com',
        instruction='You are assisting a customer with email daiki.sanchez1479@example.com who has a pending order. You want to update the shipping address for this order to 5632 Washington Boulevard, Unit 16, Portland, OR, USA 36916, because it was initially entered incorrectly. You also want to update your default address to the same, to ensure future orders are delivered correctly. Later, you would like to change the Action Camera in the order from silver to black, while keeping the same 4K resolution and waterproof features, because you prefer the black color for aesthetic reasons. You prefer the price difference to be refunded and the adjustment processed using your Visa card ending in 6593.\n\nUse daiki.sanchez1479@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9348897', 'address1': '5632 Washington Boulevard', 'address2': 'Unit 16', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '36916'}),
            Action(name='modify_user_address', kwargs={'user_id': 'daiki_sanchez_3253', 'address1': '5632 Washington Boulevard', 'address2': 'Unit 16', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '36916'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9348897', 'item_ids': ['6117189161'], 'new_item_ids': ['6700049080'], 'payment_method_id': 'credit_card_8853416'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.garcia9090@example.com',
        instruction='You are Harper Garcia (harper.garcia9090@example.com) and you want to update the shipping address for your pending order to 8641 Washington Boulevard, Unit 996, Houston, TX, USA 28800 because it was initially set to an outdated address. You also want your default address for future orders to be updated to this new address for consistency. Additionally, you would like to change the red hardshell 4-piece Luggage Set in your order to the blue softshell 4-piece version because you prefer the softshell material and blue color, and you prefer the price difference to be charged to your Visa card ending in 6583.\n\nUse harper.garcia9090@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8360923', 'address1': '8641 Washington Boulevard', 'address2': 'Unit 996', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '28800'}),
            Action(name='modify_user_address', kwargs={'user_id': 'harper_garcia_5438', 'address1': '8641 Washington Boulevard', 'address2': 'Unit 996', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '28800'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8360923', 'item_ids': ['9956648681'], 'new_item_ids': ['8759627937'], 'payment_method_id': 'credit_card_2369458'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.sanchez2046@example.com',
        instruction='You are assisting Raj Sanchez (email: raj.sanchez2046@example.com). You want to update the shipping address for a pending order containing an Indoor Security Camera and an Air Purifier to 9030 Adams Road, Unit 156, San Jose, CA, USA 45769, and also update your default address to this new location, because you have relocated. Later, for a delivered order containing a red on-ear wireless Headphones and a Jigsaw Puzzle, you would like to return the Jigsaw Puzzle because it does not suit your preferences, and exchange the red on-ear wireless Headphones for the over-ear black wireless model because you prefer a more comfortable fit and a sleeker color. You prefer to use your Mastercard ending in 2130 for any refund or price difference associated with these changes.\n\nUse raj.sanchez2046@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4566809', 'address1': '9030 Adams Road', 'address2': 'Unit 156', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '45769'}),
            Action(name='modify_user_address', kwargs={'user_id': 'raj_sanchez_2970', 'address1': '9030 Adams Road', 'address2': 'Unit 156', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '45769'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7736708', 'item_ids': ['1096508426'], 'payment_method_id': 'credit_card_3362387'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7736708', 'item_ids': ['3104857380'], 'new_item_ids': ['7493556126'], 'payment_method_id': 'credit_card_3362387'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7736708'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4566809', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.hernandez9440@example.com',
        instruction='You are Olivia Hernandez, and your email is olivia.hernandez9440@example.com. You want the pending order containing sunglasses and a makeup kit to be shipped to 4864 Main Street, Unit 389, New York, NY, USA 79388, because you have moved from Washington, DC. You also want your default profile address updated to this New York address for future orders. Later, you would like to return the garden hose from your delivered order, because it does not meet your expectations. You also want to exchange the black wireless earbuds with 4-hour battery life for the blue model with 6-hour battery life, because you prefer longer battery performance and a different color. You prefer any refund or price difference from the exchange to be applied back to your Mastercard ending in 2786.\n\nUse olivia.hernandez9440@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6811468', 'address1': '4864 Main Street', 'address2': 'Unit 389', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '79388'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_hernandez_5066', 'address1': '4864 Main Street', 'address2': 'Unit 389', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '79388'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W5671546', 'item_ids': ['3230708338'], 'payment_method_id': 'credit_card_2583849'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5671546', 'item_ids': ['4063058357'], 'new_item_ids': ['1646531091'], 'payment_method_id': 'credit_card_2583849'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6811468'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6811468', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.smith2338@example.com',
        instruction="You are to update the shipping address for the pending order containing a Portable Charger, Electric Toothbrush, Mechanical Keyboard, and Digital Camera from New York to 1412 Park Drive, Suite 209, San Francisco, CA, USA 36100 because the customer needs it delivered to a new location. You also want to update the default address in the customer's profile to the same San Francisco address for all future orders to ensure consistency in delivery. You prefer to keep PayPal as the payment method for this and future transactions.\n\nUse ethan.smith2338@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6711349', 'address1': '1412 Park Drive', 'address2': 'Suite 209', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '36100'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ethan_smith_9087', 'address1': '1412 Park Drive', 'address2': 'Suite 209', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '36100'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.moore2450@example.com',
        instruction='You are Ava Moore, authenticated via ava.moore2450@example.com, and you want to update the shipping address for your pending order containing a silver 8-inch tablet with 128GB storage, a blue 25ft vinyl garden hose, and a large black polyester backpack to 5127 Oak Avenue, Suite 173, Seattle, WA, USA 86660 because it was mistakenly sent to New York. You also want your default address updated to this Seattle address for future orders. After that, you would like to cancel this order entirely because it was placed by mistake.\n\nUse ava.moore2450@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8331214', 'address1': '5127 Oak Avenue', 'address2': 'Suite 173', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '86660'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_moore_4814', 'address1': '5127 Oak Avenue', 'address2': 'Suite 173', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '86660'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8331214', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8331214'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8495163', 'item_ids': ['5489028872'], 'new_item_ids': ['3098764622'], 'payment_method_id': 'paypal_7478252'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8495163', 'item_ids': ['5489028872'], 'payment_method_id': 'paypal_7478252'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.kovacs2446@example.com',
        instruction='You are assisting Harper Kovacs (email: harper.kovacs2446@example.com) with two order actions. First, you want to update the shipping address for a pending order containing a green polyester backpack with laptop compartment, a white 10-inch digital wall clock, a HEPA air purifier with smart sensors, and a 1-liter glass tea kettle to 7910 Washington Boulevard, Suite 627, Denver, CO, USA 60742. After that, you would like to cancel the entire order because it was placed by mistake. Later, you would like to exchange a delivered 30MP digital camera with 10x zoom and SD card storage for a similar model with 30MP resolution, 5x zoom, and CF card storage, as it better suits your needs. You prefer to use your Visa card ending in 2080 for the exchange transaction.\n\nUse harper.kovacs2446@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9093821', 'address1': '7910 Washington Boulevard', 'address2': 'Suite 627', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '60742'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9093821', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3065353'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3065353', 'item_ids': ['9228757377'], 'new_item_ids': ['6384525445'], 'payment_method_id': 'credit_card_7422485'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting Ethan Thomas (email: ethan.thomas7730@example.com). You want to update the shipping address for a pending order containing a Smart Watch and Smartphone to a new address in Houston, TX, USA. After that, you would like to cancel the order entirely because it is no longer needed. Separately, for a delivered order that included a Laptop, you want to exchange the current 17-inch Laptop with i5 processor, 8GB RAM, and 1TB SSD in space grey for a different 17-inch model with i7 processor, 32GB RAM, 1TB SSD, and black color, which is available and slightly lower in price. You prefer the exchange to be processed using your PayPal account for any financial adjustments, and the replacement should be shipped to your original address in Chicago, IL, USA.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '3016 Main Street', 'address2': 'Floor 368', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '87802'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7764382'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['3334537816'], 'payment_method_id': 'paypal_6982172'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['3334537816'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'paypal_6982172'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav.santos2789@example.com',
        instruction='You are Aarav Santos, with email aarav.santos2789@example.com. You want to update your pending order (with items including Hiking Boots, a Coffee Maker, Wireless Earbuds, and a Makeup Kit) by changing the shipping address to 6482 Park Drive, Floor 118, Portland, OR, USA 15955, and you want this address also set as your default. You prefer the Hiking Boots in size 9 instead of size 8 because the original size does not fit, and you would like any price difference handled using your Visa ending in 1747. Later, you decided to cancel this order because it was placed by mistake, and you would like confirmation that the cancellation was successful. After that, for your delivered order (which included a Mechanical Keyboard, Perfume, Dumbbell Set, Smartphone, and Indoor Security Camera), you want to return the Mechanical Keyboard because it does not meet your needs, and you prefer the refund to be issued back to your Visa ending in 1747. Finally, you would like to browse the available product types and see the full range of Hiking Boots options, including sizes, materials, and waterproof features, to consider future purchases that better match your outdoor activity needs.\n\nUse aarav.santos2789@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6111820', 'address1': '6482 Park Drive', 'address2': 'Floor 118', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '15955'}),
            Action(name='modify_user_address', kwargs={'user_id': 'aarav_santos_4279', 'address1': '6482 Park Drive', 'address2': 'Floor 118', 'city': 'Portland', 'state': 'OR', 'country': 'USA', 'zip': '15955'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6111820', 'item_ids': ['2648909398'], 'new_item_ids': ['8106223139'], 'payment_method_id': 'credit_card_3816099'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6111820', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6111820'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8309293', 'item_ids': ['8484921793'], 'payment_method_id': 'credit_card_3816099'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7363354090'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.ito8974@example.com',
        instruction="You are Amelia Ito, and your email is amelia.ito8974@example.com. You initially want to update the shipping address for your pending order (with a Fleece Jacket, Cycling Helmet, Makeup Kit, and Digital Camera) to 2436 Madison Drive, Suite 820, Nashville, TN, USA 18234, and also update your default address to match, because you've moved temporarily. You also want to change the Fleece Jacket in that order from size XS, color navy, to size L, color black, with full zipper, because it didn't fit and you prefer a more visible color, using your Mastercard ending in 7517 for any price difference. Later, you decide to cancel that entire pending order because you placed it by mistake and no longer need the items. After that, you would like to return the Hiking Boots from your previously delivered order (which also included a Bluetooth Speaker, Coffee Maker, and Bicycle) and have the refund issued back to your Mastercard ending in 7517, because the boots are uncomfortable and not waterproof as you had hoped. Finally, you want to browse the full product catalog to explore what other items are available, because you're interested in discovering new products that better suit your needs.\n\nUse amelia.ito8974@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3883329', 'address1': '2436 Madison Drive', 'address2': 'Suite 820', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '18234'}),
            Action(name='modify_user_address', kwargs={'user_id': 'amelia_ito_8772', 'address1': '2436 Madison Drive', 'address2': 'Suite 820', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '18234'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3883329', 'item_ids': ['8161321868'], 'new_item_ids': ['9385662952'], 'payment_method_id': 'credit_card_1016162'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3883329', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3883329'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3733909', 'item_ids': ['6595128475'], 'payment_method_id': 'credit_card_1016162'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '8560156827'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting Ethan Thomas (email: ethan.thomas7730@example.com). You want to exchange the 17-inch, i5, 8GB RAM, 1TB SSD, space grey laptop from his delivered order (items include a pet bed, mechanical keyboard, and security camera, delivered to Chicago) for a 17-inch, i7, 32GB RAM, 1TB SSD, black laptop, because he prefers higher performance and a different color. You prefer any price difference to be handled using his PayPal account. Later, you would like to change the payment method on his pending order (containing a black silicone-band smartwatch and a gold 128GB smartphone, shipping to Columbus) from a gift card to his Visa card ending in 8901, because he wants to preserve the remaining gift card balance for future use.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7764382'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['3334537816'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'paypal_6982172'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'credit_card_7472558'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting Ethan Thomas (email: ethan.thomas7730@example.com). For his delivered order containing a 17-inch Laptop with i5 processor, 8GB RAM, and space grey color, along with a medium brown memory foam Pet Bed, you want to initiate an exchange of the laptop for the 17-inch model with i7 processor, 32GB RAM, 1TB SSD, and black color, and return the pet bed. You prefer the refund for the returned items to be issued back to his gift card, and for any price difference in the exchange, you prefer to use his Visa card ending in 8901. Later, for his pending order containing a black silicone-banded Smart Watch and a gold 128GB Smartphone, you would like to update the shipping address to 6199 Madison Drive, Apt 136, Charlotte, NC, USA 98540, and switch the payment method from the current gift card to his PayPal account.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7764382'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['5067898160'], 'payment_method_id': 'gift_card_2519457'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['3334537816'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'credit_card_7472558'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '6199 Madison Drive', 'address2': 'Apt 136', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '98540'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'paypal_6982172'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.thomas9081@example.com',
        instruction='You are Liam Thomas, and your email is liam.thomas9081@example.com. You want to return the hiking boots from your delivered order because they are not waterproof, and you prefer a full refund back to your original payment method, which is PayPal. Later, you would like to update the shipping address for your pending order to 3660 Jackson Street, Floor 465, Oklahoma City, OK, USA 72569. You also prefer to change the payment method for that pending order to PayPal. Additionally, you intended to exchange the E-Reader in that order for a version with 16GB storage, but since it is not currently available, no item change will be made at this time.\n\nUse liam.thomas9081@example.com for authentication.',
        actions=[
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8488728', 'item_ids': ['5676696062'], 'payment_method_id': 'paypal_3650980'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1654931', 'address1': '3660 Jackson Street', 'address2': 'Floor 465', 'city': 'Oklahoma City', 'state': 'OK', 'country': 'USA', 'zip': '72569'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1654931', 'payment_method_id': 'paypal_3650980'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.wilson5906@example.com',
        instruction='You are Fatima Wilson, with email fatima.wilson5906@example.com, who first wants to review the available products. You have a pending order containing a blue leather office chair with fixed armrests and a large gas grill with rotisserie feature, originally set to ship to Austin, TX. You want to change the shipping address for this order to 4061 Park Drive, Suite 481, Fort Worth, TX, USA 34611, because you need the items delivered to your new location. You also prefer to update the payment method from your Mastercard ending in 9779 to your PayPal account for better transaction tracking and security.\n\nUse fatima.wilson5906@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1443906', 'address1': '4061 Park Drive', 'address2': 'Suite 481', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '34611'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1443906'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W1443906', 'payment_method_id': 'paypal_7685859'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting a customer with email yusuf.garcia2909@example.com who wants to first browse the product catalog. Then, for their pending order containing hiking boots in size 11, a 13-inch black laptop with i7 processor, and an air purifier for small rooms, you want to update the shipping address to 8778 Cedar Road, Apt 211, Dallas, TX, USA 45549 because they have relocated. After that, you would like to change the payment method from a gift card to their Mastercard ending in 3762 because they prefer to use their credit card for this purchase.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '8778 Cedar Road', 'address2': 'Apt 211', 'city': 'Dallas', 'state': 'TX', 'country': 'USA', 'zip': '45549'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are assisting a customer with email lei.li8350@example.com who is browsing available products and has a pending order for a 17-inch Laptop in space grey with 8GB RAM, 1TB SSD, and i5 processor. You want to update the shipping address for this order to 570 Madison Drive, Apt 807, Jacksonville, FL, USA 64564, because the customer has relocated. After that, you would like to change the payment method from PayPal to a Visa card ending in 2697 for better expense tracking. Later, you intend to cancel the order entirely because the customer no longer needs the Laptop. After cancellation, you would like to verify the order details and obtain more information about the Laptop product, including its available configurations and pricing, to consider future purchases.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '570 Madison Drive', 'address2': 'Apt 807', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '64564'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5166363', 'payment_method_id': 'credit_card_4466831'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.moore1031@example.com',
        instruction='You are Daiki Moore, and your email is daiki.moore1031@example.com. You want to update the shipping address for your pending order—which includes a Dumbbell Set, a red mesh Office Chair, and a 19 bar capsule-type Espresso Machine with 1L water tank—to 7859 Madison Drive, Unit 494, Detroit, MI, USA 52197, because you realized the original address in Dallas was incorrect. You also prefer to switch the payment method from gift card to your Visa card ending in 4204, as you want to preserve gift card balance for future use. Later, you would like to verify the details of this order and specifically review the specifications of the Espresso Machine you ordered, to ensure it meets your expectations for home use.\n\nUse daiki.moore1031@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4843514', 'address1': '7859 Madison Drive', 'address2': 'Unit 494', 'city': 'Detroit', 'state': 'MI', 'country': 'USA', 'zip': '52197'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W4843514', 'payment_method_id': 'credit_card_5613268'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4843514', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4843514'}),
            Action(name='get_product_details', kwargs={'product_id': '4354588079'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.thomas1454@example.com',
        instruction='You are unable to verify the identity of the user with email harper.thomas1454@example.com as no matching account was found. Therefore, no actions can be taken regarding order modifications, address updates, cancellations, or product inquiries.\n\nUse harper.thomas1454@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7425646'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W7425646', 'payment_method_id': 'credit_card_1199336'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7425646', 'address1': '9106 Lincoln Street', 'address2': 'Unit 543', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '33925'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7425646', 'reason': 'ordered by mistake'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4896585277'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.kovacs5369@example.com',
        instruction='You are Evelyn Kovacs (evelyn.kovacs5369@example.com). You want to update the shipping address for your pending order to 4315 Oak Avenue, Unit 373, Houston, TX, USA 95145 because it is more convenient for delivery. You also want to exchange the 1-liter glass tea kettle in that order for the 1.5-liter version because you prefer a larger capacity for daily use. You prefer to use your PayPal account for any price difference. Later, you would like to exchange the 20MP, 10x zoom digital camera from your delivered order for the 30MP, 10x zoom model because you need higher resolution for photography, and you prefer to use PayPal for any adjustment. After that, you would like to cancel your other pending order because it was placed by mistake.\n\nUse evelyn.kovacs5369@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5694685', 'address1': '4315 Oak Avenue', 'address2': 'Unit 373', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '95145'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_kovacs_6742', 'address1': '4315 Oak Avenue', 'address2': 'Unit 373', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '95145'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5694685', 'item_ids': ['3909406921'], 'new_item_ids': ['9647374798'], 'payment_method_id': 'paypal_7732922'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2768683'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2768683', 'item_ids': ['7583936705'], 'payment_method_id': 'paypal_7732922'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2768683', 'item_ids': ['7583936705'], 'new_item_ids': ['9228757377'], 'payment_method_id': 'paypal_7732922'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7398274', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.hernandez3060@example.com',
        instruction="You are Evelyn Hernandez, and your email is evelyn.hernandez3060@example.com. You want to update the shipping address for your pending grill order to 1766 Park Drive, Suite 782, Las Vegas, NV, USA 10181, because you've relocated temporarily. You also want this new address to become your default address for future orders. Additionally, you would like to upgrade the grill in this order from the medium electric model with a side burner to the large electric grill with rotisserie, because you plan to host larger gatherings and need more cooking capacity. You prefer to use your Visa card ending in 4171 for any price difference. Later, you would like to exchange the sunglasses from your delivered order—originally with a black metal frame, blue polarized lenses—for a new pair with a silver plastic frame and blue non-polarized lenses, because you prefer a lighter, more casual style that’s easier to maintain. You also prefer to use the same Visa card for any additional cost. After that, you would like to cancel your other pending order, which includes an e-reader, makeup kit, and desk lamp, because you no longer need these items due to changed plans.\n\nUse evelyn.hernandez3060@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3482034', 'address1': '1766 Park Drive', 'address2': 'Suite 782', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '10181'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_hernandez_1701', 'address1': '1766 Park Drive', 'address2': 'Suite 782', 'city': 'Las Vegas', 'state': 'NV', 'country': 'USA', 'zip': '10181'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W3482034', 'item_ids': ['5666020311'], 'new_item_ids': ['4404981319'], 'payment_method_id': 'credit_card_3631888'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9628587'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W9628587', 'item_ids': ['9045948550'], 'payment_method_id': 'credit_card_3631888'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9628587', 'item_ids': ['9045948550'], 'new_item_ids': ['4329558751'], 'payment_method_id': 'credit_card_3631888'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4895606', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.kovacs2446@example.com',
        instruction="You are assisting Harper Kovacs (email: harper.kovacs2446@example.com) with several requests. First, you want to browse the store's product catalog to explore available items. Next, for the pending order containing a green small polyester backpack with laptop compartment, a white 10-inch digital wall clock, a HEPA filter air purifier for medium rooms, and a 1-liter glass tea kettle, you want to update the shipping address to 3515 Lincoln Street, Unit 249, Jacksonville, FL, USA 17766 because the original San Jose address is no longer valid. If the address change cannot be processed, you would like to cancel the order with the reason 'ordered by mistake'. Additionally, you want to check the status of the delivered order that included a 30MP digital camera with 10x zoom and SD card storage, and you would like to initiate a return for that camera because it is no longer needed. You prefer the refund to be issued back to the original payment method, which is the Visa card ending in 2080.\n\nUse harper.kovacs2446@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9093821', 'address1': '3515 Lincoln Street', 'address2': 'Unit 249', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '17766'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9093821', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3065353'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3065353', 'item_ids': ['9228757377'], 'payment_method_id': 'credit_card_7422485'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.jackson4654@example.com',
        instruction="You are assisting Yusuf Jackson (email: yusuf.jackson4654@example.com). You want to first explore all product types the store offers to understand the full catalog. Then, for your pending order containing a gold Smartphone (128GB, 4GB RAM) and a gold Smart Watch with silicone band, you want to update the shipping address from Seattle to 727 Oak Avenue, Apt 382, Denver, CO, USA 49592, because you now prefer delivery to Denver. Later, you decide to cancel this order altogether, citing 'ordered by mistake' as the reason, because you no longer need the items. After cancellation, you would like to confirm the order status to ensure it has been fully canceled. Separately, for your delivered order that included a large brown polyester Pet Bed, you would like to return that item because it does not suit your pet's needs, and you prefer the refund to be applied to your gift card balance for future use.\n\nUse yusuf.jackson4654@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2087737', 'address1': '727 Oak Avenue', 'address2': 'Apt 382', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '49592'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2087737', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2087737'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7128968', 'item_ids': ['7729002517'], 'payment_method_id': 'gift_card_7037673'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.li1185@example.com',
        instruction='You are assisting Fatima Li (email: fatima.li1185@example.com). You want to update the shipping address for her pending order, which includes a skateboard and an espresso machine, to 3086 Washington Boulevard, Unit 987, Boston, MA, USA 36578, because she has moved temporarily for work. You also want her default address to be updated to this new Boston address for future orders. Later, you would like to modify the skateboard in the same pending order, switching from the maple deck version to the bamboo deck version (same 31-inch length and graphic design), because she prefers the sustainability and lighter weight of bamboo. You prefer to use her PayPal account to handle any price difference for the skateboard upgrade, as it was the original payment method used for the order.\n\nUse fatima.li1185@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8005719', 'address1': '3086 Washington Boulevard', 'address2': 'Unit 987', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '36578'}),
            Action(name='modify_user_address', kwargs={'user_id': 'fatima_li_5040', 'address1': '3086 Washington Boulevard', 'address2': 'Unit 987', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '36578'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8005719'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8005719', 'item_ids': ['5120532699'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'paypal_6366157'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.ito8974@example.com',
        instruction='You are Amelia Ito (email: amelia.ito8974@example.com) and you want to update the shipping address for your pending order—currently at 798 Hickory Lane, Suite 353, Seattle, WA—to 896 Maple Lane, Floor 257, Chicago, IL, USA 92536, and also set this new address as your default for future orders because it is your current residence. After the update, you would like to review the details of the Fleece Jacket in your order, which is a navy-colored, full-zip jacket in size XS, to confirm its style and fit. Later, after reviewing the item, you have decided to cancel the entire order because you no longer need the items, including the jacket, helmet, makeup kit, and camera. You prefer the refund to be processed back to the original payment method, which is your credit card.\n\nUse amelia.ito8974@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3883329', 'address1': '896 Maple Lane', 'address2': 'Floor 257', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '92536'}),
            Action(name='modify_user_address', kwargs={'user_id': 'amelia_ito_8772', 'address1': '896 Maple Lane', 'address2': 'Floor 257', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '92536'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3883329'}),
            Action(name='get_product_details', kwargs={'product_id': '8560156827'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3883329', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.li8523@example.com',
        instruction="You are Liam Li, and your email is liam.li8523@example.com. You want to update the shipping address for your pending order—currently shipping to Charlotte, NC—for the urethane-coated fixed dumbbell set (30–50 lbs) to 1720 Washington Boulevard, Apt 4, Chicago, IL, USA 96639, and you also want your default address updated to the same address because it's your correct and current location. After that, you would like to verify the details of this order and the product to confirm what was purchased. Later, after reviewing, you would like to cancel the pending order entirely because you no longer need the dumbbell set. You prefer the refund to be processed back to the original payment method, which was the gift card used for the purchase.\n\nUse liam.li8523@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1130240', 'address1': '1720 Washington Boulevard', 'address2': 'Apt 4', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '96639'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_li_8526', 'address1': '1720 Washington Boulevard', 'address2': 'Apt 4', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '96639'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1130240'}),
            Action(name='get_product_details', kwargs={'product_id': '7233192239'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1130240', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah.martin8712@example.com',
        instruction="You are Noah Martin (email: noah.martin8712@example.com). You want to update the shipping address for your pending order—containing a bagless upright vacuum cleaner with HEPA filter, a blue cotton v-neck t-shirt in size S, and a space grey 15-inch laptop with i5 processor and 32GB RAM—to 5230 Park Drive, Unit 977, Seattle, WA, USA 65187 because you need it delivered there. Later, you will cancel the entire order because you no longer need the items. Separately, for your delivered order containing a full-size mechanical keyboard with clicky switches and white backlight, a plastic 31-inch skateboard, a 1.5L silver electric kettle, and a 10-inch wood-colored analog wall clock, you would like to return only the mechanical keyboard because you don't need it anymore. You prefer the refund for the return to be issued back to your PayPal account, as that was your original payment method.\n\nUse noah.martin8712@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7594624', 'address1': '5230 Park Drive', 'address2': 'Unit 977', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '65187'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7594624', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1971958'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1971958', 'item_ids': ['6342039236'], 'payment_method_id': 'paypal_7383471'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.martin9430@example.com',
        instruction='You are assisting Lucas Martin (lucas.martin9430@example.com) with two order actions. First, for his pending order containing a black silicone-band smart watch, a white glass bookshelf, a 2000-piece beginner-level jigsaw puzzle, a red cotton crew neck T-shirt, and a 30MP digital camera, you want to update the shipping address to 6603 Washington Boulevard, Suite 132, New York, NY, USA 99082, because it was originally set to Austin. After that, you would like to cancel the entire order because it was placed by mistake. Later, for his delivered order containing a black plastic 750ml water bottle, you would like to initiate a return of the item and request a refund to his Mastercard ending in 8198, as he no longer needs it.\n\nUse lucas.martin9430@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5502903', 'address1': '6603 Washington Boulevard', 'address2': 'Suite 132', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '99082'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5502903', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4998173'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W4998173', 'item_ids': ['7199146548'], 'payment_method_id': 'credit_card_2325059'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are Omar Silva (email: omar.silva4147@example.com). You want to cancel your pending order containing a fantasy-themed 2000-piece jigsaw puzzle, a brown wooden bookshelf, a silver non-waterproof 4K action camera, polarized green-lens sunglasses, and an animals-themed 2000-piece puzzle because you no longer need these items. Later, you would like to modify another pending order that includes a purple XL cotton crew neck T-Shirt, a silver leather-band smart watch, and a 1L manual espresso machine. For this order, you want to update the shipping address to 6091 Cedar Road, Floor 9, New York, NY, USA 10236. You also prefer to change the payment method from gift card to PayPal, and you would like to exchange the purple XL T-Shirt for the blue M cotton crew neck T-Shirt, with any price difference covered using your PayPal. After that, you would like to browse the full catalog of available product types to explore other options, with a specific interest in T-Shirts.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9728773', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9673784', 'address1': '6091 Cedar Road', 'address2': 'Floor 9', 'city': 'New York', 'state': 'NY', 'country': 'USA', 'zip': '10236'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9673784', 'payment_method_id': 'paypal_2192303'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9673784', 'item_ids': ['8124970213'], 'new_item_ids': ['9612497925'], 'payment_method_id': 'paypal_2192303'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com). You want to cancel a pending order that includes hiking boots, a laptop, and an air purifier, originally shipped to Indianapolis, because he no longer needs the items. Later, you would like to modify another pending order for a grey medium polyester backpack with a laptop compartment, currently shipped to Washington, DC: you want to update the shipping address to 1207 Adams Road, Unit 139, Nashville, TN, USA 15101, change the payment method from PayPal to the Mastercard ending in 3762, and exchange the medium backpack for a large one in the same color and material if possible, or otherwise prefer a large grey polyester backpack with a hydration or laptop compartment. After that, you would like to browse all available product types in the catalog to explore options, and then view detailed information about the Backpack product to understand its variants and features.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W6885344', 'address1': '1207 Adams Road', 'address2': 'Unit 139', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '15101'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W6885344', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W6885344', 'item_ids': ['5917587651'], 'new_item_ids': ['6309044598'], 'payment_method_id': 'credit_card_8405687'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah.ito4296@example.com',
        instruction='You are assisting a customer with email noah.ito4296@example.com who is reviewing available product types and specifically interested in wristwatches. You want to inform them about the full range of product categories offered, with a focus on the Wristwatch variants. You would like to update their pending order placed in Seattle by replacing the wristwatch with a metal strap and blue dial with the available leather-strap black-dial version, as you prefer a more classic and comfortable style over the current sporty metal design. You prefer the price difference to be handled using your Mastercard ending in 1065, as previously authorized for this order.\n\nUse noah.ito4296@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6066914160'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4219264'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4219264', 'item_ids': ['9112290483'], 'new_item_ids': ['9949163720'], 'payment_method_id': 'credit_card_1620755'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.anderson9999@example.com',
        instruction='You are assisting a customer with email omar.anderson9999@example.com who initially inquired about coffee makers, lamps, and hiking gear. You want to modify their pending order placed in Phoenix by replacing the 4-cup black espresso coffee maker with timer with a 4-cup stainless steel drip coffee maker with auto shutoff, as you prefer the auto shutoff feature and stainless steel finish over the current espresso model with timer. You prefer to use your PayPal account for any price adjustment associated with this change.\n\nUse omar.anderson9999@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7996920482'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2091016', 'item_ids': ['5952720925'], 'new_item_ids': ['3039787582'], 'payment_method_id': 'paypal_2055565'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.gonzalez2399@example.com',
        instruction="You are assisting Yusuf Gonzalez, whose email is yusuf.gonzalez2399@example.com. You want to update the payment method for a pending order containing a black 128GB smartphone and a ceramic tea kettle from a Mastercard ending in 9928 to his PayPal account, as he prefers using PayPal for this transaction. If the payment update is not possible, you would like the order canceled with the reason 'ordered by mistake'. Later, for another pending order that includes a gold 128GB tablet, bookshelf, LED light bulb, and sunglasses, you want to change the shipping address to 9388 Oak Avenue, Unit 910, Austin, TX, USA 62197, and update the default address to match, as he has relocated. After that, you would like to modify the tablet in this order from the gold 128GB model to the silver 64GB version, which is less expensive, and you prefer any refund for the price difference to be returned to the same PayPal account used for the original purchase.\n\nUse yusuf.gonzalez2399@example.com for authentication.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2806889'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2806889', 'payment_method_id': 'paypal_3022415'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2806889', 'reason': 'ordered by mistake'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2230795', 'address1': '9388 Oak Avenue', 'address2': 'Unit 910', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '62197'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yusuf_gonzalez_8900', 'address1': '9388 Oak Avenue', 'address2': 'Unit 910', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '62197'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2230795', 'item_ids': ['6948061616'], 'new_item_ids': ['2106335193'], 'payment_method_id': 'paypal_3022415'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.sanchez2046@example.com',
        instruction='You are assisting a customer with email raj.sanchez2046@example.com who is interested in Air Purifiers. You want to modify the Air Purifier in their pending order for San Diego by upgrading it to a model with a HEPA filter and quiet operation, because they prefer better air filtration and quieter performance. The new variant is suitable for medium-sized rooms and is available for upgrade. You prefer to use your Mastercard ending in 2130 for any price difference associated with this change.\n\nUse raj.sanchez2046@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_order_details', kwargs={'order_id': '#W4566809'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4566809', 'item_ids': ['5826601160'], 'new_item_ids': ['3076708684'], 'payment_method_id': 'credit_card_3362387'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.santos3158@example.com',
        instruction='You are Ivan Santos (ivan.santos3158@example.com). You want to update the shipping address for your pending Office Chair order to 1903 Madison Drive, Suite 298, Seattle, WA, USA 47970 because you accidentally entered an old address. You also want this new address to become your default for future orders to avoid similar issues. Later, you would like to exchange the blue Wireless Earbuds with 6-hour battery life from your recent delivery for the same model in blue but with 8-hour battery life, as the current battery life does not meet your needs. You prefer the price difference to be handled via your PayPal account, which was used for the original purchase, for faster and more convenient processing.\n\nUse ivan.santos3158@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8770097', 'address1': '1903 Madison Drive', 'address2': 'Suite 298', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '47970'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ivan_santos_6635', 'address1': '1903 Madison Drive', 'address2': 'Suite 298', 'city': 'Seattle', 'state': 'WA', 'country': 'USA', 'zip': '47970'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6893533', 'item_ids': ['1646531091'], 'new_item_ids': ['8555936349'], 'payment_method_id': 'paypal_6151711'}),
            Action(name='get_product_details', kwargs={'product_id': '9924732112'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.wilson1598@example.com',
        instruction="You are Amelia Wilson, with email amelia.wilson1598@example.com. You want to update the shipping address for your pending order (containing a red cotton v-neck T-shirt, a silver silicone-band smart watch, and a 1000-piece art-themed puzzle) to 3835 Oak Avenue, Apt 266, Philadelphia, PA, USA 57612 because you've moved temporarily. You also want your default address updated to this new Philadelphia address for future orders. Later, you would like to exchange the 5-25 lbs iron adjustable dumbbell set from your delivered order (which also included a 1000-piece art-themed puzzle) for the 30-50 lbs iron adjustable set because you need heavier weights for your strength training. You prefer the price difference to be handled using your PayPal account, which was used for a previous payment.\n\nUse amelia.wilson1598@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3062096', 'address1': '3835 Oak Avenue', 'address2': 'Apt 266', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '57612'}),
            Action(name='modify_user_address', kwargs={'user_id': 'amelia_wilson_4614', 'address1': '3835 Oak Avenue', 'address2': 'Apt 266', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '57612'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9077205', 'item_ids': ['3877338112'], 'new_item_ids': ['6245231688'], 'payment_method_id': 'paypal_4101143'}),
            Action(name='get_product_details', kwargs={'product_id': '7233192239'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava.kovacs4827@example.com',
        instruction='You are Ava Kovacs (email: ava.kovacs4827@example.com). You want to update the shipping address for your pending order, which includes a skateboard, headphones, garden hose, and tea kettle, to 4781 Madison Drive, Unit 412, Columbus, OH, USA 96055, because you have moved. You also want to update your default address to this new Columbus address for future orders. After reviewing all product types and skateboard variants, you would like to exchange the plain plastic 28 inch skateboard from your delivered order for the bamboo 28 inch skateboard with a graphic design, because you prefer a more eco-friendly material and a more stylish appearance. You prefer to use your Mastercard ending in 3598 for any price difference. Later, you decide to cancel your pending order entirely because you no longer need the items.\n\nUse ava.kovacs4827@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4184032', 'address1': '4781 Madison Drive', 'address2': 'Unit 412', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '96055'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ava_kovacs_3448', 'address1': '4781 Madison Drive', 'address2': 'Unit 412', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '96055'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6344370', 'item_ids': ['4545791457'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'credit_card_9699699'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4184032', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma.martin1207@example.com',
        instruction='You are Emma Martin (email: emma.martin1207@example.com) and you want to update the shipping address for your pending order — which includes a navy XL half-zip fleece jacket, a red XXL cotton crew neck t-shirt, a gold 128GB smartphone, a professional dark-skin-tone makeup kit, and a 20000mAh black wireless portable charger — to 3269 Madison Drive, Floor 533, Austin, TX, USA 73749 because it was initially sent to the wrong location. You also want your default address updated to the same because you prefer consistency across your account. Later, you would like to cancel the entire order because you no longer need the items. After that, you would like confirmation that the cancellation was successful and the order status is no longer pending.\n\nUse emma.martin1207@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5432440', 'address1': '3269 Madison Drive', 'address2': 'Floor 533', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '73749'}),
            Action(name='modify_user_address', kwargs={'user_id': 'emma_martin_6993', 'address1': '3269 Madison Drive', 'address2': 'Floor 533', 'city': 'Austin', 'state': 'TX', 'country': 'USA', 'zip': '73749'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5432440', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5432440'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed.khan5338@example.com',
        instruction='You are assisting a customer with email mohamed.khan5338@example.com who has a pending order for Wireless Earbuds in black and an Electric Toothbrush in white. You want to change the shipping address for this order to 6020 Cedar Road, Apt 642, Denver, CO, USA 85552, because the original address was incorrect. You also want to update the default shipping address to this new Denver address for all future orders. After that, you would like to cancel the pending order because it was placed by mistake. Finally, you want confirmation that the order has been successfully canceled and is no longer active.\n\nUse mohamed.khan5338@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7390432', 'address1': '6020 Cedar Road', 'address2': 'Apt 642', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '85552'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mohamed_khan_3010', 'address1': '6020 Cedar Road', 'address2': 'Apt 642', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '85552'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7390432', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7390432'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.gonzalez8775@example.com',
        instruction='You are assisting Mei Gonzalez (mei.gonzalez8775@example.com) with two order updates. First, for her pending order containing a portable gas grill with side burner, a black fleece jacket in size L, a white wireless gaming mouse, an A5 soft-cover notebook, and a red mesh office chair, you want to update the shipping address to 1296 Main Street, Floor 185, Los Angeles, CA, USA 25508 because she has relocated temporarily. You also want to change the payment method from PayPal to her Visa card ending in 3742 for better expense tracking. Later, for her delivered order that included a navy small nylon backpack with a laptop compartment and a large memory foam pet bed, you would like to return the backpack and exchange it for a black large nylon backpack with a camera compartment instead, because she needs more specialized storage for her photography gear. You prefer the price difference to be handled using her original payment method, which was her credit card.\n\nUse mei.gonzalez8775@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2052757', 'address1': '1296 Main Street', 'address2': 'Floor 185', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '25508'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2052757', 'payment_method_id': 'credit_card_4387170'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7303089'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W7303089', 'item_ids': ['2492465580'], 'payment_method_id': 'credit_card_4387170'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7303089', 'item_ids': ['2492465580'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'credit_card_4387170'}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya.brown8893@example.com',
        instruction='You are Anya Brown (anya.brown8893@example.com). You want to update the shipping address for your pending order (containing an E-Reader and a Smart Watch) to 3806 Lincoln Street, Apt 76, Denver, CO, USA 10515 because it was initially sent to the wrong location. After that, you would like to change the payment method for this order from Mastercard to PayPal for your preferred payment convenience. Later, you would like to return the medium grey fleece Pet Bed from your delivered order (shipped to New York) because you no longer need it, and you prefer the refund to be issued back to your original payment method.\n\nUse anya.brown8893@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8883368', 'address1': '3806 Lincoln Street', 'address2': 'Apt 76', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '10515'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8883368', 'payment_method_id': 'paypal_5206520'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8883368'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W2922433', 'item_ids': ['6857426243'], 'payment_method_id': 'credit_card_3414703'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2922433', 'item_ids': ['6857426243'], 'new_item_ids': ['6857426243'], 'payment_method_id': 'credit_card_3414703'}),
            Action(name='get_product_details', kwargs={'product_id': '2747247837'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, and your email is olivia.ito5204@example.com. You want to update the shipping address for your pending order—which includes a black wired gaming mouse, a red 7 ft polyester patio umbrella, and a size 8 leather hiking boot—to 7518 Main Street, Suite 175, Nashville, TN, USA 65632, because you will be staying there and the original Denver address is no longer valid. After that, you would like to change the payment method from your Visa card ending in 9182 to your PayPal account for better spending tracking. Later, you decide to cancel the entire order because you realized you no longer need these items and made the purchase by mistake.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '7518 Main Street', 'address2': 'Suite 175', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '65632'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5442520', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj.li2787@example.com',
        instruction='You are assisting a customer who wants to update their pending order originally shipped to Fort Worth, TX. You want to change the shipping address to 5302 Adams Road, Apt 86, Fort Worth, TX, USA 11341, because the original address is incorrect. Later, you would like to switch the payment method from the Visa card ending in 3917 to PayPal, as the customer prefers to use that for this transaction. After that, you would like to cancel the entire order because it was placed by mistake, and no longer wish to proceed with the purchase of the glass bookshelves, green stainless steel water bottle, or large gas grill.\n\nUse raj.li2787@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8967935', 'address1': '5302 Adams Road', 'address2': 'Apt 86', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '11341'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8967935', 'payment_method_id': 'paypal_2028062'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8967935', 'reason': 'ordered by mistake'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting lucas.johansson7741@example.com with two pending orders. For the first order containing hiking boots, a black small nylon backpack with a laptop compartment, and a 500-piece animal-themed jigsaw puzzle, you want to change the payment method to the Visa card ending in 9452 and then cancel the order because the items are no longer needed. Later, for the second pending order containing a gray fabric high-back office chair without armrests and a black 10-inch tablet with 32GB storage, you would like to update the shipping address to 4448 Jackson Street, Apt 256, Jacksonville, FL, USA 58248, and also update the default address to the same, to ensure future orders are delivered correctly.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8379216', 'address1': '4448 Jackson Street', 'address2': 'Apt 256', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '58248'}),
            Action(name='modify_user_address', kwargs={'user_id': 'lucas_johansson_1090', 'address1': '4448 Jackson Street', 'address2': 'Apt 256', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '58248'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting Yusuf Garcia (email: yusuf.garcia2909@example.com), who has a pending order containing Hiking Boots, a Laptop, and an Air Purifier, originally shipping to Indianapolis. You want to update the shipping address for this order to 5690 Jefferson Avenue, Apt 188, San Diego, CA, because the delivery location has changed. You also prefer to change the payment method from a gift card to your Mastercard ending in 3762 for better expense tracking. Later, you decide to cancel the same order entirely because the items are no longer needed. After the cancellation, you would like to explore the product catalog to discover available options, starting with a full list of product types. Subsequently, you are interested in learning more about the Backpack, particularly its available colors, sizes, materials, and compartment types, to evaluate suitability for future purchase.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '5690 Jefferson Avenue', 'address2': 'Apt 188', 'city': 'San Diego', 'state': 'CA', 'country': 'USA', 'zip': '28511'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'credit_card_8405687'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2564042', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.ahmed4901@example.com',
        instruction='You are assisting Mei Ahmed (email: mei.ahmed4901@example.com). You want to exchange the 28-inch skateboard with a plain plastic deck from the delivered order for a new 28-inch skateboard with a bamboo deck and graphic design, because you prefer the look and material of bamboo with a more stylish appearance. You prefer any price difference to be handled using your Mastercard ending in 9375. Later, you would like to update the shipping address for your pending order to 4527 Washington Boulevard, Floor 439, Los Angeles, CA, USA 73754, because you have relocated and need the items delivered to your new location. After that, you would like your default address to be updated to the same Los Angeles address for all future orders.\n\nUse mei.ahmed4901@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7553978'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7553978', 'item_ids': ['4545791457'], 'new_item_ids': ['6843647669'], 'payment_method_id': 'credit_card_5902940'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2598324', 'address1': '4527 Washington Boulevard', 'address2': 'Floor 439', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '73754'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mei_ahmed_4909', 'address1': '4527 Washington Boulevard', 'address2': 'Floor 439', 'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'zip': '73754'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li7352@example.com',
        instruction='You are Sofia Li (sofia.li7352@example.com) and you have a pending order that you initially want to modify. You want to update the shipping address to 7228 Jackson Street, Unit 875, Charlotte, NC, USA 13147 because it is your current location. You prefer to change the payment method from your Visa ending in 6791 to your Mastercard ending in 8484 for better rewards. You also want to exchange the 34-inch plastic deck skateboard with a plain design for a 34-inch bamboo deck with a graphic design because you prefer a more eco-friendly and stylish option, and you want any price difference applied to your Mastercard ending in 8484. After that, you would like to return the digital camera from your delivered order and receive a refund to your Mastercard ending in 8484 because it does not meet your needs. Later, after considering your needs, you decide to cancel the entire pending order #W8855135 because you no longer require the items.\n\nUse sofia.li7352@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8855135', 'address1': '7228 Jackson Street', 'address2': 'Unit 875', 'city': 'Charlotte', 'state': 'NC', 'country': 'USA', 'zip': '13147'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8855135', 'payment_method_id': 'credit_card_8105988'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8855135', 'item_ids': ['3098764622'], 'new_item_ids': ['3541421151'], 'payment_method_id': 'credit_card_8105988'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8855135'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W4689314', 'item_ids': ['5996159312'], 'payment_method_id': 'credit_card_8105988'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8855135', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are Lei Li, with email lei.li8350@example.com, who initially wanted to update the shipping address for a pending laptop order to 3999 Pine Avenue, Unit 863, San Francisco, CA, USA 54850, because it needed to be delivered to a different location. You wanted to change the payment method to your Visa card ending in 2697 for better rewards and control. You also preferred to upgrade the laptop from the i5/8GB configuration to a more powerful i7/32GB model in black, using the same Visa for any additional cost, because you needed higher performance. You requested confirmation of the updated order details to ensure all changes were applied correctly. Additionally, you wanted to return the black electric toothbrush from a previously delivered order, choosing a refund to your Visa ending in 2697 for consistency in payment handling. Later, after these changes were processed, you decided to cancel the entire pending laptop order because you no longer needed the device.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '3999 Pine Avenue', 'address2': 'Unit 863', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '54850'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5166363', 'payment_method_id': 'credit_card_4466831'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5166363', 'item_ids': ['3334537816'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'credit_card_4466831'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6289770', 'item_ids': ['8098621301'], 'payment_method_id': 'credit_card_4466831'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5166363', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.patel3193@example.com',
        instruction="You are assisting Mei Patel (mei.patel3193@example.com), who explored the available perfume variants and decided to make changes to two of her pending orders. You want to cancel her first order because it was placed by mistake. That order includes a 30ml women's woody perfume, among other items. Later, for her second order containing a 100ml men's oriental perfume, you would like to exchange the perfume for the smaller 30ml men's oriental version because she prefers a more compact size. You prefer the refund for the price difference to be processed back to her PayPal account, as that was the original payment method. After that, you would like to update the shipping address for this second order to 4357 Adams Road, Floor 725, San Diego, CA, USA 98763.\n\nUse mei.patel3193@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '6858788497'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4082615', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9583042'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9583042', 'item_ids': ['5421902839'], 'new_item_ids': ['1325156478'], 'payment_method_id': 'paypal_4768213'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9583042', 'address1': '992 Cedar Road', 'address2': 'Unit 254', 'city': 'Fort Worth', 'state': 'TX', 'country': 'USA', 'zip': '61575'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf.garcia2909@example.com',
        instruction='You are assisting a customer with email yusuf.garcia2909@example.com who has a pending order containing a black 13-inch laptop with 512GB SSD. You want to verify the order details and product specifications to ensure accuracy. You would like to update the shipping address to 8812 Washington Boulevard, Apt 332, Boston, MA, USA 36856, because the original address in Indianapolis is no longer valid. You prefer to switch the payment method from the current gift card to your PayPal account for better transaction tracking. You also want to exchange the current laptop for a model with a 15-inch screen and 1TB SSD in space grey, because you prefer a larger display and more storage capacity. Since the new laptop is less expensive, you would like the price difference refunded to your Mastercard ending in 3762 for consistency with your preferred refund method.\n\nUse yusuf.garcia2909@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2564042'}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W2564042', 'address1': '8812 Washington Boulevard', 'address2': 'Apt 332', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '36856'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W2564042', 'payment_method_id': 'paypal_7503218'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2564042', 'item_ids': ['1657832319'], 'new_item_ids': ['6017636844'], 'payment_method_id': 'credit_card_8405687'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.rossi1299@example.com',
        instruction='You are Amelia Rossi, and your email is amelia.rossi1299@example.com. You want to update the shipping address for your pending order to 1304 Washington Boulevard, Unit 382, Phoenix, AZ, USA 36170 because you need the package delivered to a different location. You would like to exchange the blue medium cotton crew neck T-Shirt in your order for a purple XL cotton crew neck T-Shirt because the original size and color do not fit your preference. You prefer to pay using your Visa card ending in 9402 instead of the gift card currently applied, as you would like to preserve the gift card balance for future use.\n\nUse amelia.rossi1299@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8255453'}),
            Action(name='get_product_details', kwargs={'product_id': '9523456873'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8255453', 'address1': '1304 Washington Boulevard', 'address2': 'Unit 382', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '36170'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8255453', 'payment_method_id': 'credit_card_6844118'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8255453', 'item_ids': ['9612497925'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'credit_card_6844118'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan.khan6479@example.com',
        instruction='You are assisting Ivan Khan (email: ivan.khan6479@example.com) with updating his shipping and profile address for a pending order containing a navy nylon small laptop Backpack, an Indoor Security Camera, and a Desk Lamp. You want to change the shipping address for this order from Washington, DC to 6980 Main Street, Apt 318, Nashville, TN, USA 96702 because it was entered incorrectly. Later, you will update his default profile address to the same Nashville address to ensure future orders are delivered correctly. After that, you would like to explore the product catalog, specifically reviewing the available variants of the Backpack he ordered, so he can understand the different color, size, material, and compartment options available for this product, such as black or green, large or small, nylon or polyester, and camera or hydration compartments, to inform potential future purchases.\n\nUse ivan.khan6479@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5270061', 'address1': '6980 Main Street', 'address2': 'Apt 318', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '96702'}),
            Action(name='modify_user_address', kwargs={'user_id': 'ivan_khan_7475', 'address1': '6980 Main Street', 'address2': 'Apt 318', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '96702'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5270061'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5270061', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '2524789262'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam.li8523@example.com',
        instruction="You are Liam Li, with email liam.li8523@example.com, and you want to update the shipping address for your pending order (currently shipping a Dumbbell Set) to 2552 Jefferson Avenue, Suite 142, Chicago, IL, USA 53127, because you need it delivered to your new location. You also want your default address updated to this Chicago address for future orders. Later, you would like to return the gold Smart Watch with leather band from your delivered order, because it doesn't match your style preference, and you want the refund processed to your PayPal account. After that, you would like to exchange it for the black Smart Watch with silicone band, because you prefer a more durable and understated look, and you prefer to use your PayPal for any price difference.\n\nUse liam.li8523@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1130240', 'address1': '2552 Jefferson Avenue', 'address2': 'Suite 142', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '53127'}),
            Action(name='modify_user_address', kwargs={'user_id': 'liam_li_8526', 'address1': '2552 Jefferson Avenue', 'address2': 'Suite 142', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '53127'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8838515'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8838515', 'item_ids': ['9408160950'], 'payment_method_id': 'paypal_9619477'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W8838515', 'item_ids': ['9408160950'], 'new_item_ids': ['2860956907'], 'payment_method_id': 'paypal_9619477'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei.davis6811@example.com',
        instruction='You are Mei Davis (mei.davis6811@example.com). You want to cancel your pending order placed in Denver because you no longer need the items, which include a white wireless gaming mouse, black wireless over-ear headphones, a medium-room HEPA air purifier with night mode, a stainless steel smart thermostat compatible with Amazon Alexa, and black wireless earbuds with 6-hour battery life and IPX7 water resistance. Later, you would like to exchange the blue 1000ml stainless steel water bottle from your delivered order for the black version of the same size and material, as you prefer the black color for style reasons. You prefer to use your Mastercard ending in 1037 for any price adjustment related to the exchange. After that, you would like to receive a full list of all product types available in the store to explore more options for future purchases.\n\nUse mei.davis6811@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1267569', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2890441'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W2890441', 'item_ids': ['2366567022'], 'new_item_ids': ['7661609223'], 'payment_method_id': 'credit_card_1061405'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.anderson1447@example.com',
        instruction='You are assisting Fatima Anderson (email: fatima.anderson1447@example.com). You want to exchange the skateboard in her smaller pending order (currently plastic, 31 inch, plain) for a 31-inch bamboo deck with a graphic design, because she prefers the eco-friendly material and visual style. You prefer the price difference to be covered using her PayPal account, which was previously used for this order. Later, for her larger pending order containing wireless earbuds, headphones, and a digital camera, you would like to update the shipping address to 8517 Pine Avenue, Unit 883, Denver, CO, USA 86047, to redirect delivery to a new location. After that, you would like to cancel the entire order, as she no longer needs the items. After handling these changes, you would like to receive a list of all current product types available in the catalog to explore future purchases, with a particular interest in outdoor and tech accessories.\n\nUse fatima.anderson1447@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2974929'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W2974929', 'item_ids': ['3877188862'], 'new_item_ids': ['5312063289'], 'payment_method_id': 'paypal_7916550'}),
            Action(name='get_product_details', kwargs={'product_id': '1968349452'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4514908', 'address1': '8517 Pine Avenue', 'address2': 'Unit 883', 'city': 'Denver', 'state': 'CO', 'country': 'USA', 'zip': '86047'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W4514908', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia.jackson5798@example.com',
        instruction='You are Mia Jackson, with email mia.jackson5798@example.com, and you want to modify the Desk Lamp in your pending order to the high brightness version while keeping it black and powered by AC adapter, because you prefer brighter lighting for your workspace; the price difference should be covered using your PayPal account. Later, you would like to update the shipping address for your second pending order to a new location in Houston, Texas, but then decided to cancel this entire order instead, as your needs have changed. After that, you would like to know what product types are currently available in the catalog for future consideration, so you can explore new items that match your lifestyle and home setup.\n\nUse mia.jackson5798@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7807323'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7807323', 'item_ids': ['5320792178'], 'new_item_ids': ['7624783998'], 'payment_method_id': 'paypal_2031016'}),
            Action(name='get_product_details', kwargs={'product_id': '6817146515'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W1205816', 'address1': '8332 Lincoln Street', 'address2': 'Suite 475', 'city': 'Houston', 'state': 'TX', 'country': 'USA', 'zip': '73999'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W1205816', 'reason': 'no longer needed'}),
            Action(name='list_all_product_types', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.thomas1364@example.com',
        instruction='You are assisting Sophia Thomas (sophia.thomas1364@example.com). You want to change the shipping address for a pending order containing a bookshelf, tablet, and two office chairs from Dallas, TX to 1334 Elm Street, Apt 167, Phoenix, AZ, USA 52204 because it needs to be delivered to a new location. Later, you would like to update your default address to this new Phoenix address for future orders. After that, you would like to exchange a black, large, polyester backpack with a laptop compartment (from a delivered order) for a black, large, nylon backpack with a camera compartment because you prefer more durable material and a compartment suited for camera gear. You prefer the price difference to be processed using your Visa card ending in 9858.\n\nUse sophia.thomas1364@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4862767', 'address1': '1334 Elm Street', 'address2': 'Apt 167', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '52204'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sophia_thomas_5301', 'address1': '1334 Elm Street', 'address2': 'Apt 167', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '52204'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1867876', 'item_ids': ['6906307980'], 'new_item_ids': ['3928046918'], 'payment_method_id': 'credit_card_7326294'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn.hernandez3060@example.com',
        instruction='You are Evelyn Hernandez, and your email is evelyn.hernandez3060@example.com. You want to change the shipping address for your pending grill order from San Diego to 7691 Pine Avenue, Apt 220, San Francisco, CA, USA 21802, because you have moved. You also want your default address updated to this new San Francisco address for future orders. Later, you would like to exchange the sunglasses from your delivered order that have blue lenses and a metal frame for the same model with green lenses and a plastic frame, because you prefer the look and feel of green lenses with a lighter frame. You prefer to use your Visa card ending in 4171 for any price difference associated with the exchange.\n\nUse evelyn.hernandez3060@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3482034', 'address1': '7691 Pine Avenue', 'address2': 'Apt 220', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '21802'}),
            Action(name='modify_user_address', kwargs={'user_id': 'evelyn_hernandez_1701', 'address1': '7691 Pine Avenue', 'address2': 'Apt 220', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '21802'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W9628587', 'item_ids': ['9045948550'], 'new_item_ids': ['4548300368'], 'payment_method_id': 'credit_card_3631888'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.silva4147@example.com',
        instruction='You are assisting Omar Silva (email: omar.silva4147@example.com) with his pending order. You want to update the shipping address to 9585 Maple Lane, Unit 623, Columbus, OH, USA 96221, because he needs the items delivered to a new location. Later, you would like to change the payment method from the original gift card to his Mastercard ending in 5859, as he prefers to use this card for better purchase protection. After that, you would like to exchange the current 4K silver Action Camera (not waterproof) for the available 4K silver waterproof model, because he plans to use it in wet conditions and needs the waterproof feature. You prefer the price difference to be handled using the same Mastercard for any additional charge or refund.\n\nUse omar.silva4147@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9728773', 'address1': '9585 Maple Lane', 'address2': 'Unit 623', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '96221'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9728773'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W9728773', 'payment_method_id': 'credit_card_5322562'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9728773', 'item_ids': ['9391733462'], 'new_item_ids': ['6117189161'], 'payment_method_id': 'credit_card_5322562'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei.li8350@example.com',
        instruction='You are Lei Li (email: lei.li8350@example.com). You want to update the shipping address for your pending Laptop order to 2454 Oak Avenue, Unit 533, San Antonio, TX, USA 81612 because you need it delivered to a new location. Later, you would like to return the black Electric Toothbrush from your delivered order because it does not meet your expectations. After that, you would like to exchange the current plastic blue 750ml Water Bottle for a stainless steel blue 750ml version because you prefer a more durable and insulated material. You prefer any refund or charge related to these changes to be processed using your Visa card ending in 2697.\n\nUse lei.li8350@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5166363', 'address1': '2454 Oak Avenue', 'address2': 'Unit 533', 'city': 'San Antonio', 'state': 'TX', 'country': 'USA', 'zip': '81612'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5166363'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W6289770', 'item_ids': ['8098621301'], 'payment_method_id': 'credit_card_4466831'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W6289770', 'item_ids': ['6974536207'], 'new_item_ids': ['7843064651'], 'payment_method_id': 'credit_card_4466831'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia.patel9841@example.com',
        instruction="You are assisting Sophia Patel (email: sophia.patel9841@example.com) with her order requests. You want to change the shipping address for her pending order—which includes a men's oriental-scented 100ml perfume, a glass 1.5-liter induction-compatible tea kettle, a black 1L glass electric kettle, and gray size 8 canvas sneakers—from Fort Worth, TX to 1236 Jefferson Avenue, Floor 53, Phoenix, AZ, USA 10261, because she has moved. You also want your default address updated to this new Phoenix address for future orders. Later, after reconsidering, you would like to cancel the entire order because you no longer need the items. You prefer the refund to be processed back to the original payment method, which is the Visa card ending in 8025.\n\nUse sophia.patel9841@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7905419', 'address1': '1236 Jefferson Avenue', 'address2': 'Floor 53', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '10261'}),
            Action(name='modify_user_address', kwargs={'user_id': 'sophia_patel_6833', 'address1': '1236 Jefferson Avenue', 'address2': 'Floor 53', 'city': 'Phoenix', 'state': 'AZ', 'country': 'USA', 'zip': '10261'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W7905419', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7905419'}),
            Action(name='get_product_details', kwargs={'product_id': '6858788497'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.silva2443@example.com',
        instruction='You are Yara Silva (email: yara.silva2443@example.com) and you want to update the shipping address for your pending order containing an Electric Kettle, Wristwatch, and Bookshelf to 8273 Washington Boulevard, Unit 949, Jacksonville, FL, USA 12615 because you need it delivered to a new location. You also want your default address updated to match this new address for future orders. While this is being processed, you would like to know what product types are available in the catalog to explore other options. Later, you decided to cancel your other pending order containing an Air Purifier, Backpack, Water Bottle, and Tablet because you no longer need those items, and you would like confirmation that the cancellation was successful. After that, you would like detailed information about the Action Camera product, particularly its available variants, to consider a potential future purchase.\n\nUse yara.silva2443@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9810810', 'address1': '8273 Washington Boulevard', 'address2': 'Unit 949', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '12615'}),
            Action(name='modify_user_address', kwargs={'user_id': 'yara_silva_7567', 'address1': '8273 Washington Boulevard', 'address2': 'Unit 949', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '12615'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9034102', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9034102'}),
            Action(name='get_product_details', kwargs={'product_id': '3377618313'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed.li8414@example.com',
        instruction="You are a returning customer with email mohamed.li8414@example.com who initially wants to browse the product catalog. You want to update the shipping address for your pending order—containing a mechanical keyboard, security camera, T-shirt, smart watch, and digital camera—to a new address in Chicago because you've relocated. You also want your default address updated to the same Chicago address for future orders. Later, you decide to cancel that pending order because you no longer need the items. After cancellation, you would like to return the 50ft black latex garden hose from a previously delivered order, as it no longer fits your needs. You prefer the refund for the returned item to be issued back to your PayPal account, which is your primary payment method.\n\nUse mohamed.li8414@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8844578', 'address1': '2670 Main Street', 'address2': 'Suite 381', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '22730'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mohamed_li_1979', 'address1': '2670 Main Street', 'address2': 'Suite 381', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '22730'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8844578', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8844578'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W8864622', 'item_ids': ['4024196380'], 'payment_method_id': 'paypal_6045911'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia.ito8974@example.com',
        instruction='You are assisting Amelia Ito, whose email is amelia.ito8974@example.com. You want to update the shipping address for her pending order—which includes a Fleece Jacket, Cycling Helmet, Makeup Kit, and Digital Camera—to 7432 Maple Lane, Apt 756, Columbus, OH, USA 98163, because she needs it delivered to a new location. You also want to update her default address in profile to this new Columbus address for future orders. Later, you will cancel the same pending order because she no longer needs the items. After that, you would like to return the Bluetooth Speaker from her previously delivered order to receive a refund, as she no longer uses it. You prefer the refund to be issued back to her Mastercard ending in 7517, which was the original payment method.\n\nUse amelia.ito8974@example.com for authentication.',
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3883329', 'address1': '7432 Maple Lane', 'address2': 'Apt 756', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '98163'}),
            Action(name='modify_user_address', kwargs={'user_id': 'amelia_ito_8772', 'address1': '7432 Maple Lane', 'address2': 'Apt 756', 'city': 'Columbus', 'state': 'OH', 'country': 'USA', 'zip': '98163'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3883329', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3883329'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3733909', 'item_ids': ['5650803029'], 'payment_method_id': 'credit_card_1016162'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas.johansson7741@example.com',
        instruction='You are assisting lucas.johansson7741@example.com with his pending order containing Hiking Boots in size 8, a black small nylon backpack with a laptop compartment, and a 500-piece expert-level animal-themed jigsaw puzzle. You want to update the shipping address to 3139 Cedar Road, Apt 292, Jacksonville, FL, USA 11322 because it is his current location. You would like to change the payment method from the current card to his Visa ending in 9452 for better rewards tracking. You prefer to update the Hiking Boots from size 8 to size 9 in leather with waterproofing, as it better fits his needs. Later, you would like to cancel the entire order because he no longer requires the items.\n\nUse lucas.johansson7741@example.com for authentication.',
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5073920'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5073920', 'address1': '3139 Cedar Road', 'address2': 'Apt 292', 'city': 'Jacksonville', 'state': 'FL', 'country': 'USA', 'zip': '11322'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5073920', 'payment_method_id': 'credit_card_1864112'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W5073920', 'item_ids': ['2648909398'], 'new_item_ids': ['8106223139'], 'payment_method_id': 'credit_card_1864112'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W5073920', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan.thomas7730@example.com',
        instruction='You are assisting Ethan Thomas (email: ethan.thomas7730@example.com). You want to update the shipping address for a pending order containing a black silicone-band Smart Watch and a gold 128GB Smartphone to 437 Adams Road, Unit 516, Nashville, TN, USA 30356, because it needs to be delivered to a different location. After that, you would like to change the payment method for this order to your Visa ending in 8901, as you prefer to use this card for tracking and rewards. Later, you intend to cancel this order entirely because it was placed by mistake. Simultaneously, you want to exchange the 17-inch space grey Laptop with i5 processor and 8GB RAM from a delivered order for a 17-inch black Laptop with i7 processor and 32GB RAM, because you need more processing power and memory for professional work. You prefer the price adjustment for this exchange to be handled through your PayPal account, as it was the original payment method and offers buyer protection. Additionally, you would like to review all available variants of the Laptop product to confirm your exchange choice is optimal, ensuring you select the best configuration for your needs.\n\nUse ethan.thomas7730@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8465042', 'address1': '437 Adams Road', 'address2': 'Unit 516', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '30356'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8465042', 'payment_method_id': 'credit_card_7472558'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8465042', 'reason': 'ordered by mistake'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W7764382', 'item_ids': ['3334537816'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'paypal_6982172'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8465042'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '4760268021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.ito5204@example.com',
        instruction='You are Olivia Ito, authenticated with email olivia.ito5204@example.com, and you have a pending order containing a black wired gaming mouse, a red 7 ft polyester patio umbrella with manual tilt, and leather hiking boots in size 8. You want to update the shipping address for this pending order to 3207 Lincoln Street, Floor 173, Boston, MA, USA 11326 because you will be relocating temporarily. After that, you would like to change the payment method for this order from credit card to PayPal, as you prefer to consolidate payments through that account. Later, you want to exchange the black synthetic sneakers in size 11 from your delivered order (which also included an automatic 19 bar espresso machine) for the same model in size 10, but in gray leather, because the original size is too large and you prefer the look and feel of the gray leather version. You prefer any price difference to be processed using your PayPal account. Additionally, you would like to know more about the sneakers product line, particularly the model you ordered, to explore other available options and understand its features better.\n\nUse olivia.ito5204@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W5442520', 'address1': '3207 Lincoln Street', 'address2': 'Floor 173', 'city': 'Boston', 'state': 'MA', 'country': 'USA', 'zip': '11326'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W5442520', 'payment_method_id': 'paypal_8049766'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5866402'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W5866402', 'item_ids': ['9727387530'], 'new_item_ids': ['2509076505'], 'payment_method_id': 'paypal_8049766'}),
            Action(name='list_all_product_types', kwargs={}),
            Action(name='get_product_details', kwargs={'product_id': '7471004230'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima.anderson1447@example.com',
        instruction='You are assisting Fatima Anderson (email: fatima.anderson1447@example.com). You want to cancel a pending skateboard order because she no longer needs it. The skateboard is 31 inch with a plain design and plastic deck. Later, for another pending order containing blue wireless earbuds with 4-hour battery life, headphones, and a digital camera, you would like to change the shipping address to 2999 Jackson Street, Unit 818, Nashville, TN, USA 70372, and update the default address to match. You also want to upgrade the wireless earbuds to a version with longer battery life (6 hours) while keeping the blue color, as it better suits her usage needs. You prefer any price difference to be handled using her PayPal account, which is her preferred payment method for refunds and adjustments.\n\nUse fatima.anderson1447@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W2974929', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2974929'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W4514908', 'address1': '2999 Jackson Street', 'address2': 'Unit 818', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '70372'}),
            Action(name='modify_user_address', kwargs={'user_id': 'fatima_anderson_2157', 'address1': '2999 Jackson Street', 'address2': 'Unit 818', 'city': 'Nashville', 'state': 'TN', 'country': 'USA', 'zip': '70372'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W4514908', 'item_ids': ['2757705742'], 'new_item_ids': ['1646531091'], 'payment_method_id': 'paypal_7916550'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia.silva3776@example.com',
        instruction='You are Olivia Silva, authenticated with email olivia.silva3776@example.com. You want to cancel your pending order containing the green natural rubber Yoga Mat because you no longer need it. For your other pending order containing a navy polyester backpack, manual 9 bar espresso machine, rose gold 64GB smartphone, white analog wall clock, and white wireless earbuds, you want to update the shipping address to 745 Maple Lane, Unit 749, Philadelphia, PA, USA 74442, and you prefer the black 128GB smartphone over the current rose gold 64GB version for a better fit with your device ecosystem. After that, you would like your default address to be updated to the new Philadelphia address for future orders. You prefer any payment adjustment, including the minor refund from the smartphone price difference, to be processed back to your PayPal account.\n\nUse olivia.silva3776@example.com for authentication.',
        actions=[
            Action(name='cancel_pending_order', kwargs={'order_id': '#W6940125', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6940125'}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W7613749', 'address1': '745 Maple Lane', 'address2': 'Unit 749', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '74442'}),
            Action(name='modify_user_address', kwargs={'user_id': 'olivia_silva_7273', 'address1': '745 Maple Lane', 'address2': 'Unit 749', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '74442'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W7613749', 'item_ids': ['5311660992'], 'new_item_ids': ['1507389580'], 'payment_method_id': 'paypal_9379149'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia.li7352@example.com',
        instruction="You are Sofia Li, with email sofia.li7352@example.com. For your pending order containing an Air Purifier, Hiking Boots, Skateboard, and Yoga Mat, you want to update the shipping address to 7056 Lincoln Street, Floor 966, San Jose, CA, USA 74160 because it needs to be delivered to a new location. You also want to change the payment method from your Visa card ending in 6791 to your PayPal account for greater convenience. If these changes cannot be made, you would like the order canceled with the reason 'no longer needed'. Separately, for your delivered order containing a 500-piece art-themed Jigsaw Puzzle and a Bicycle, you want to return the puzzle because you prefer a more challenging fantasy-themed design, and you would like to exchange it for the 1000-piece fantasy-themed puzzle. You prefer to use your Mastercard ending in 8484 for any refund or additional charge associated with the exchange.\n\nUse sofia.li7352@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8855135', 'address1': '7056 Lincoln Street', 'address2': 'Floor 966', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '74160'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W8855135', 'payment_method_id': 'paypal_8194385'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8855135', 'reason': 'no longer needed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W3916020'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W3916020', 'item_ids': ['4068787148'], 'payment_method_id': 'credit_card_8105988'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W3916020', 'item_ids': ['4068787148'], 'new_item_ids': ['3112842858'], 'payment_method_id': 'credit_card_8105988'}),
            Action(name='get_product_details', kwargs={'product_id': '1808611083'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara.lee9368@example.com',
        instruction="You are assisting Yara Lee (email: yara.lee9368@example.com). You want to update the shipping address for a pending order containing Hiking Boots, a red leather Office Chair, and a Mechanical Keyboard to 5742 Jackson Street, Unit 674, Philadelphia, PA, USA 49835, because the original address in Houston is incorrect. You would like to change the payment method for this order to your Visa card ending in 6367 for consistency with your preferred payment method. If any issues arise during this update, you are prepared to cancel the order with the reason 'ordered by mistake'. Later, you would like to exchange a Mechanical Keyboard from a delivered order — originally with tactile switches, RGB backlight, and 60% size — for a variant with clicky switches, no backlight, and full size, because you prefer a louder typing feedback and a more complete layout without lighting effects. You prefer to use the same Visa card ending in 6367 for any price adjustment related to the exchange.\n\nUse yara.lee9368@example.com for authentication.",
        actions=[
            Action(name='list_all_product_types', kwargs={}),
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W3320020', 'address1': '5742 Jackson Street', 'address2': 'Unit 674', 'city': 'Philadelphia', 'state': 'PA', 'country': 'USA', 'zip': '49835'}),
            Action(name='modify_pending_order_payment', kwargs={'order_id': '#W3320020', 'payment_method_id': 'credit_card_6450164'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W3320020', 'reason': 'ordered by mistake'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1341845'}),
            Action(name='return_delivered_order_items', kwargs={'order_id': '#W1341845', 'item_ids': ['4402162122'], 'payment_method_id': 'credit_card_6450164'}),
            Action(name='exchange_delivered_order_items', kwargs={'order_id': '#W1341845', 'item_ids': ['4402162122'], 'new_item_ids': ['7706410293'], 'payment_method_id': 'credit_card_6450164'}),
            Action(name='get_product_details', kwargs={'product_id': '1656367028'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki.sanchez1479@example.com',
        instruction='You are Daiki Sanchez, and your email is daiki.sanchez1479@example.com. You want to update the shipping address for your pending order—currently going to Denver—to 5423 Main Street, Suite 461, San Jose, CA, USA 52535, because it was entered incorrectly. You also want your default address updated to this new San Jose address for future orders. After that, you would like to change the Action Camera in your order from silver to black, keeping the same 4K resolution and waterproof feature, because you prefer the black color. You prefer to use your Visa card ending in 6593 for any price difference. Later, after considering the changes, you have decided you no longer need the items and would like to cancel the entire order.\n\nUse daiki.sanchez1479@example.com for authentication.',
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W9348897', 'address1': '5423 Main Street', 'address2': 'Suite 461', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '52535'}),
            Action(name='modify_user_address', kwargs={'user_id': 'daiki_sanchez_3253', 'address1': '5423 Main Street', 'address2': 'Suite 461', 'city': 'San Jose', 'state': 'CA', 'country': 'USA', 'zip': '52535'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9348897'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W9348897', 'item_ids': ['6117189161'], 'new_item_ids': ['6700049080'], 'payment_method_id': 'credit_card_8853416'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W9348897', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed.li8414@example.com',
        instruction="You are assisting Mohamed Li (mohamed.li8414@example.com) with his pending order. You want to change the shipping address for the order from Columbus, OH to 5476 Adams Road, Unit 146, Chicago, IL, USA 83203, because it was entered incorrectly. You also want to update your default address to this new Chicago address for future orders. You would like to exchange the black XL cotton crew neck T-shirt in the order for the purple XL version because you prefer the color purple over black. Later, after considering the changes, you have decided to cancel the entire order as you've changed your mind about the purchase. You prefer the refund to be issued back to the original payment method, which was PayPal.\n\nUse mohamed.li8414@example.com for authentication.",
        actions=[
            Action(name='modify_pending_order_address', kwargs={'order_id': '#W8844578', 'address1': '5476 Adams Road', 'address2': 'Unit 146', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '83203'}),
            Action(name='modify_user_address', kwargs={'user_id': 'mohamed_li_1979', 'address1': '5476 Adams Road', 'address2': 'Unit 146', 'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'zip': '83203'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8844578'}),
            Action(name='modify_pending_order_items', kwargs={'order_id': '#W8844578', 'item_ids': ['2060066974'], 'new_item_ids': ['8124970213'], 'payment_method_id': 'paypal_6045911'}),
            Action(name='cancel_pending_order', kwargs={'order_id': '#W8844578', 'reason': 'no longer needed'}),
        ],
        outputs=[],
    ),
]
