from tau_emotion_bench.types import Task, Action


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
]
