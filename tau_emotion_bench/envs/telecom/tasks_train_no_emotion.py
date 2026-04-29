from tau_emotion_bench.types import Task, Action


TASKS = [
    Task(
        user_id='reese.clark7888@email.com',
        instruction='You are reese.clark7888@email.com. You want to first review the details of your Cable Internet 500MB service because you are considering discontinuing it. After reviewing, you would like to cancel the service to reduce monthly expenses. You prefer to pay off your outstanding balance of $31.62 using your credit card today to bring your account current. After that, you would like to receive updated billing information to confirm the service removal and payment have been successfully processed and reflected in your account.\n\nUse reese.clark7888@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_cable_500mb'}),
            Action(name='manage_service', kwargs={'customer_id': 'reese_clark_1767', 'action': 'remove', 'service_id': 'internet_cable_500mb'}),
            Action(name='record_payment', kwargs={'customer_id': 'reese_clark_1767', 'amount': 31.62, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_clark_1767'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.white8837@email.com',
        instruction='You are Jamie White (jamie.white8837@email.com). You want to pay the outstanding balance of $68.71 using a credit card because the last payment was marked as late and you want to avoid further fees. If any issues occur during payment processing, you would like a high-priority billing support ticket created to ensure prompt resolution. You are experiencing no service on your Samsung Galaxy A54, which is your primary mobile device, so you need troubleshooting assistance to restore connectivity. Later, you would like to add the Unlimited Mobile Plan to your account because it better fits your usage needs, and you want it associated with your Samsung Galaxy A54. After that, you prefer to update your billing preferences to paperless and enable auto-pay with a quarterly billing cycle for better payment control and to reduce late fees, as your current setup does not include auto-pay or paperless billing.\n\nUse jamie.white8837@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'jamie_white_7985', 'amount': 68.71, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'jamie_white_7985', 'category': 'billing', 'priority': 'high'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy A54'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'no_service'}),
            Action(name='manage_billing', kwargs={'customer_id': 'jamie_white_7985', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'jamie_white_7985', 'action': 'add', 'service_id': 'mobile_unlimited', 'devices_ids': ['1']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.thomas5669@email.com',
        instruction="You are alex.thomas5669@email.com. You want to pay the outstanding balance of $89.19 using a credit card because the last payment was marked as late and you want to bring the account current. After that, you would like troubleshooting assistance for your Samsung Galaxy A54 because it is experiencing no service, and as a Samsung user, you rely on your mobile device for daily communication. Later, you want to update your billing preferences by enabling paperless billing and auto-pay with your credit card to avoid future late fees, and switch to a quarterly billing cycle for better budget alignment. You also want a full list of your current services—Basic Mobile Plan, Cable Internet 500MB, and Premium TV Package—to review what you're paying for.\n\nUse alex.thomas5669@email.com for authentication.",
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'alex_thomas_7404', 'amount': 89.19, 'method': 'credit_card', 'date': '2025-04-05'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_thomas_7404', 'category': 'billing'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy A54'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'no_service'}),
            Action(name='manage_billing', kwargs={'customer_id': 'alex_thomas_7404', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'alex_thomas_7404', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.allen2290@email.com',
        instruction="You are Taylor Allen (taylor.allen2290@email.com). You want to know the specifications of your iPhone SE (3rd gen) because you are assessing its performance. Since the device is experiencing battery drain, you would like troubleshooting guidance to extend battery life for daily use. You prefer Apple devices and are using the iPhone SE (3rd gen) on the mobile_basic plan. Later, you would like a full list of your active services—Unlimited Basic Mobile, Fiber Internet 1 Gbps, Premium TV Package, and Home Security—so you can review what you're currently paying for. You prefer to keep billing communications paperless and would like to maintain monthly billing, but you are not currently enrolled in auto-pay.\n\nUse taylor.allen2290@email.com for authentication.",
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone SE (3rd gen)'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'taylor_allen_9648', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.hall1782@email.com',
        instruction='You are taylor.hall1782@email.com. You want to review the details of your iPhone 15 Pro because you are experiencing persistent battery drain issues. Since the device is an Apple phone, you prefer manufacturer-specific troubleshooting, so you would like steps to address the battery drain, including restarting the device, reducing screen brightness, and closing background apps. After that, you would like a complete list of your current services to understand your account setup, which includes the Unlimited Mobile Plan and Cable Internet 500MB service.\n\nUse taylor.hall1782@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'taylor_hall_4351', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='skyler.patel6110@email.com',
        instruction='You are Skyler Patel (skyler.patel6110@email.com). You want to update your billing preferences by disabling auto-pay because you prefer to manually review charges each cycle, while keeping paperless billing enabled for convenience and environmental reasons. You would like to switch your billing cycle to annual to reduce the frequency of payments and better align with your budgeting schedule. Later, you intend to pay off your current balance of $100.42 using your credit card on October 5, 2025, to avoid further late fees. Additionally, you would like information about your Basic Mobile Plan, which provides essential mobile service with a monthly cost of $35.00, to better understand your current coverage and usage limits.\n\nUse skyler.patel6110@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'skyler_patel_6435', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'annual'}),
            Action(name='record_payment', kwargs={'customer_id': 'skyler_patel_6435', 'amount': 100.42, 'method': 'credit_card', 'date': '2025-10-05'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'skyler_patel_6435'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_basic'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='cameron.jackson0534@email.com',
        instruction='You are cameron_jackson_3391, with email cameron.jackson0534@email.com. You want to update your billing preferences to disable paperless billing because you prefer receiving physical statements, and to disable auto-pay so you can manage payments manually. You would like to switch to a quarterly billing cycle for better alignment with your personal budgeting schedule. You also want to pay your current outstanding balance of $137.05 today, September 18, 2025, using your credit card to clear the balance promptly and avoid further late fees. After that, you would like to review your full billing details to verify the changes and ensure accuracy. Additionally, you would like information about your Premium TV Package (tv_premium), which costs $95.00 per month, to confirm its features and value as part of your current service lineup.\n\nUse cameron.jackson0534@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'cameron_jackson_3391', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'cameron_jackson_3391', 'amount': 137.05, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'cameron_jackson_3391'}),
            Action(name='get_service_details', kwargs={'service_id': 'tv_premium'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.lewis2167@email.com',
        instruction="You are Morgan Lewis (morgan.lewis2167@email.com). Your iPhone 13, an Apple device, is experiencing no service issues, so you want troubleshooting assistance to restore connectivity and maintain reliable mobile access. You also want to review your current services, which include the Unlimited Mobile Plan and Fiber Internet 1 Gbps, to ensure they meet your needs. Later, you would like to learn more about the Unlimited Mobile Plan because you are considering your service options. After that, you prefer to update your billing preferences to paperless with auto-pay enabled on a monthly cycle for better account management and payment reliability. Finally, you intend to pay your outstanding balance of $124.97 using a credit card on today's date to clear any overdue charges and avoid late fees.\n\nUse morgan.lewis2167@email.com for authentication.",
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 13'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'morgan_lewis_4303', 'category': 'mobile'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 13', 'issue': 'no_service'}),
            Action(name='manage_service', kwargs={'customer_id': 'morgan_lewis_4303', 'action': 'list'}),
            Action(name='record_payment', kwargs={'customer_id': 'morgan_lewis_4303', 'amount': 124.97, 'method': 'credit_card', 'date': '2025-09-20'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'morgan_lewis_4303'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='manage_billing', kwargs={'customer_id': 'morgan_lewis_4303', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.thomas4598@email.com',
        instruction='You are rowan_thomas_1718, with email rowan.thomas4598@email.com. You want to disable paperless billing because you prefer receiving physical copies by mail, disable auto-pay to regain manual control over payments, and switch to a quarterly billing cycle for better budget alignment. You would like a full list of your current services to review your plan lineup. Since your Apple iPhone 13 is experiencing battery drain that disrupts daily use, you prefer troubleshooting guidance focused on power-saving adjustments. After reviewing the steps, you would like to create a support ticket for the device issue with medium priority to ensure it is tracked for resolution.\n\nUse rowan.thomas4598@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_thomas_1718', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'rowan_thomas_1718', 'action': 'list'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 13', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_thomas_1718', 'category': 'device', 'priority': 'medium'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.martinez2139@email.com',
        instruction='You are Taylor Martinez (taylor.martinez2139@email.com). You want to update your billing preferences to disable paperless billing because you prefer receiving physical statements, disable auto-pay for greater control over payment timing, and switch to a quarterly billing cycle to align with your budgeting schedule. You would like to remove the Basic TV Package from your services as it is no longer needed. You are experiencing battery drain on your Apple iPhone 15 Pro, which affects daily usability, so you need troubleshooting guidance. Later, you would like a support ticket created for this device issue with category device to ensure it is tracked and resolved.\n\nUse taylor.martinez2139@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'taylor_martinez_7052', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'taylor_martinez_7052', 'action': 'remove', 'service_id': 'tv_basic'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'taylor_martinez_7052', 'category': 'device'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.walker6369@email.com',
        instruction='You are taylor_walker_0047, a senior customer on the Senior Mobile Plan. You want troubleshooting for battery drain issues because your iPhone 14, an Apple device, is losing charge too quickly during the day. You would like confirmation that the senior discount has been applied to your plan, reducing the price from $45.00 to $40.00, so you can verify your billing accuracy. You prefer Apple devices, and your iPhone 14 is essential for daily communication. Later, you would like to add a WiFi 6 Router to improve home network performance, as your current Standard WiFi Router is outdated. After that, you want a new high-priority support ticket created for device issues because the existing connectivity problems are disruptive. Subsequently, you would like the existing ticket TICKET00006 to be updated to status in_progress and urgent priority because it has not been addressed promptly despite its importance. You also prefer to update your billing preferences to paperless billing and quarterly billing for better organization and cost tracking, and you want to disable auto-pay for greater control over payments. Finally, you would like to make a $50.00 payment using credit card on 2025-09-25 and confirm your updated billing details to ensure the transaction is recorded correctly.\n\nUse taylor.walker6369@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'taylor_walker_0047', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00006'}),
            Action(name='add_device', kwargs={'customer_id': 'taylor_walker_0047', 'device_name': 'WiFi 6 Router'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'taylor_walker_0047', 'category': 'device', 'priority': 'high'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00006', 'status': 'in_progress', 'priority': 'urgent'}),
            Action(name='manage_billing', kwargs={'customer_id': 'taylor_walker_0047', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'taylor_walker_0047'}),
            Action(name='record_payment', kwargs={'customer_id': 'taylor_walker_0047', 'amount': 50.0, 'method': 'credit_card', 'date': '2025-09-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.wilson5045@email.com',
        instruction='You are rowan.wilson5045@email.com. You want to know the price of a $45.00 plan with the senior discount applied, which would be $40.00, because you are eligible for the discount and want to understand your potential savings. You would like to review your current billing details because you have an outstanding balance of $106.77 that you plan to settle. You prefer to pay the balance of $106.77 using credit card on 2025-10-20 to avoid further late fees and bring your account current. You are experiencing battery drain on your iPhone 13, which is affecting daily usability, so you want troubleshooting guidance for this issue. You prefer Apple devices, specifically the iPhone 13, as it is your current device and important for communication. You would like a high-priority support ticket created for the battery drain issue because the device is essential for your daily activities and the problem is persistent.\n\nUse rowan.wilson5045@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_wilson_1058'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_wilson_1058', 'amount': 106.77, 'method': 'credit_card', 'date': '2025-10-20'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_wilson_1058', 'category': 'device', 'priority': 'high'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 13', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 13'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.garcia2823@email.com',
        instruction="You are sam_garcia_2071, customer email sam.garcia2823@email.com. You want to understand how the senior discount would apply to a $45.00 plan because you're exploring cost-saving options, and the discounted rate would be $40.00. You would like to review your current billing details to verify charges, as your account had an outstanding balance of $132.21. You prefer to pay this balance of $132.21 today using a credit card to clear the dues promptly, and the payment has been successfully applied, bringing your current balance to $0.00. You want to report a billing concern by creating a support ticket, so a medium-priority billing ticket (TICKET241) has been created for follow-up. You need help with your Samsung Galaxy S23 because it is experiencing battery drain issues that affect daily usability, so you would like troubleshooting guidance. You also want to know the specifications of your device because you're assessing its performance capabilities, and the device is a Samsung-manufactured mobile phone, model Galaxy S23. You prefer Samsung devices for their familiarity and ecosystem integration.\n\nUse sam.garcia2823@email.com for authentication.",
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_garcia_2071'}),
            Action(name='record_payment', kwargs={'customer_id': 'sam_garcia_2071', 'amount': 132.21, 'method': 'credit_card', 'date': '2025-10-25'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_garcia_2071', 'category': 'billing', 'priority': 'medium'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy S23'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.anderson3172@email.com',
        instruction="You are sam_anderson_2306, and you want to know the specifications of your iPhone 15 Pro because you are experiencing issues with its performance and connectivity. You prefer Apple devices, specifically the iPhone 15 Pro model, as it is your primary mobile phone. After learning the device details, you would like a support ticket to be created to address the ongoing device issue, as reliable phone functionality is important for staying connected. The ticket has been created under the 'device' category with medium priority.\n\nUse sam.anderson3172@email.com for authentication.",
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_anderson_2306', 'category': 'device'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.jackson1136@email.com',
        instruction='You are Avery Jackson (avery.jackson1136@email.com). You want to learn about the Fiber Internet 1GB service because you are considering upgrading from your current cable internet plan to achieve faster and more reliable speeds. You also want details about the WiFi 6 Router, manufactured by TechCorp, because it is already in your account and you need to confirm its compatibility with the fiber service. You would like a high-priority support ticket created for ongoing internet connectivity issues because the problem is disrupting your home network and requires urgent attention.\n\nUse avery.jackson1136@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'avery_jackson_3269', 'category': 'internet', 'priority': 'high'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='skyler.martinez8026@email.com',
        instruction='You are skyler_martinez_2372. You want to know the details of the Fiber Internet 1GB plan because you are evaluating your current service; it costs $80.00 per month and provides high-speed fiber internet. You also want information about the WiFi 6 Router because you are considering upgrading your current networking equipment; it is a TechCorp model designed for high-performance home networks. Since you are currently experiencing internet connectivity issues, you would like a support ticket created under the internet category to resolve the problem; a ticket (TICKET241) has been opened for this issue.\n\nUse skyler.martinez8026@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'skyler_martinez_2372', 'category': 'internet'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jordan.king3586@email.com',
        instruction='You are jordan_king_4419, a senior customer on the Senior Mobile Plan. You want to add an iPhone 14 to your account because you recently acquired the device and need it activated for service. After adding it, you would like troubleshooting for battery drain issues because the phone loses charge quickly during daily use. You prefer Apple devices, specifically the iPhone 14 model. Later, you want to learn about the Unlimited Mobile Plan and its pricing, and you specifically want to know your senior-discounted rate of $40.00 based on a $45.00 base price for better cost comparison. After that, you would like to review your current services, which include the Senior Mobile Plan, Fiber Internet 1GB, and Basic TV Package. Subsequently, you want to update your billing preferences to enable paperless billing for convenience, turn on auto-pay for payment reliability, and set your billing cycle to monthly to align with your budgeting habits, as these settings give you better control and reduce manual effort.\n\nUse jordan.king3586@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'jordan_king_4419', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'jordan_king_4419'}),
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'jordan_king_4419', 'action': 'list'}),
            Action(name='manage_billing', kwargs={'customer_id': 'jordan_king_4419', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.hall3747@email.com',
        instruction='You are morgan_hall_1459, a senior customer on the Senior Mobile Plan. You want to add an iPhone 13 to your account because you recently acquired the device and need it connected to your service. Since the iPhone 13 is made by Apple, you prefer Apple devices for their ecosystem compatibility. After adding it, you experience battery drain issues, so you would like troubleshooting guidance to improve battery life and avoid frequent charging. You are also interested in the Unlimited Mobile Plan for potential future use, and you want to know its price with the senior discount applied. The Senior Mobile Plan currently costs $45.00, and with the $5 senior discount, it would be $40.00, which helps you maintain affordable service. You want to explore all available services to understand your options, and after review, you decide to add the Basic TV Package to expand your home entertainment. Finally, you would like to confirm your billing preferences: you prefer paperless billing and auto-pay enabled for convenience and environmental reasons, and you want to keep your billing cycle as monthly to align with your budgeting habits.\n\nUse morgan.hall3747@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'morgan_hall_1459', 'device_name': 'iPhone 13'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 13'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 13', 'issue': 'battery_drain'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'morgan_hall_1459'}),
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'morgan_hall_1459', 'action': 'add', 'service_id': 'tv_basic'}),
            Action(name='manage_billing', kwargs={'customer_id': 'morgan_hall_1459', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.lee1419@email.com',
        instruction='You are Emerson Lee (emerson.lee1419@email.com). You want to pay your outstanding balance of $85.81 by credit card on 2025-09-18 because the last payment was marked as late and you want to clear the balance. After that, you would like to update your billing preferences to enable auto-pay and maintain paperless billing with a monthly billing cycle for better payment control and to avoid future late fees. You prefer auto-pay with credit card as your payment method to ensure timely payments. Subsequently, you want a billing support ticket created with medium priority to confirm that all changes were processed correctly and to have a record of the updates.\n\nUse emerson.lee1419@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'emerson_lee_1092'}),
            Action(name='record_payment', kwargs={'customer_id': 'emerson_lee_1092', 'amount': 85.81, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='manage_billing', kwargs={'customer_id': 'emerson_lee_1092', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'emerson_lee_1092', 'category': 'billing', 'priority': 'medium'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jordan.brown7942@email.com',
        instruction='You are jordan_brown_1927, and your email is jordan.brown7942@email.com. You own an iPhone 15 Pro and are experiencing no service, so you would like troubleshooting steps to resolve connectivity issues because the device is essential for daily communication. Since the issue persists, you want a support ticket created in the device category to formally log the problem and ensure follow-up. You prefer Apple devices for their ecosystem integration and reliability, and you would like the issue resolved promptly to restore full functionality.\n\nUse jordan.brown7942@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'jordan_brown_1927', 'category': 'device'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'no_service'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='casey.jackson8903@email.com',
        instruction="You are casey.jackson8903@email.com. You own an iPhone 15 Pro and are experiencing no service, so you would like troubleshooting guidance because the device is unusable without connectivity. You prefer Apple devices, specifically the iPhone 15 Pro, which is your primary mobile phone. After reviewing initial troubleshooting steps, you want a high-priority support ticket created to ensure rapid resolution, as this issue is impacting your daily communication. A support ticket (TICKET241) has been opened in category 'device' with high priority to investigate the no-service issue further.\n\nUse casey.jackson8903@email.com for authentication.",
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'casey_jackson_6078', 'category': 'device', 'priority': 'high'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'no_service'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='skyler.clark8545@email.com',
        instruction='You are Skyler Clark (skyler_clark_3608). You want to pay off your current outstanding balance of $151.91 today, September 18, 2025, using your credit card because you prefer to keep your account in good standing. After that, you would like to learn more about the Premium TV Package since you are considering adding it to your services. Later, you would like to open a support ticket for billing concerns with medium priority because you want clarity and resolution on recent charges, including a late fee that may need review.\n\nUse skyler.clark8545@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'skyler_clark_3608', 'amount': 151.91, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'skyler_clark_3608'}),
            Action(name='get_service_details', kwargs={'service_id': 'tv_premium'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'skyler_clark_3608', 'category': 'billing', 'priority': 'medium'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.patel6952@email.com',
        instruction='You are Avery Patel (avery.patel6952@email.com). You want to clear your outstanding balance of $194.81 by making a payment with your credit card on 2025-09-18 because you prefer to keep your account in good standing. After that, you would like to learn more about the Fiber Internet 1GB service as a potential upgrade from your current Cable Internet 500MB plan, since you are experiencing connectivity concerns. You also want to open an internet-related support ticket with medium priority to address these ongoing connectivity issues, as reliable internet is important for your household use.\n\nUse avery.patel6952@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'avery_patel_1556', 'amount': 194.81, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'avery_patel_1556'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'avery_patel_1556', 'category': 'internet', 'priority': 'medium'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jordan.jackson2540@email.com',
        instruction='You are jordan_jackson_5473 (jordan.jackson2540@email.com). You want to first review all available services in the catalog to understand your options for potential upgrades or changes, particularly interested in higher-speed internet and expanded TV packages. After that, you would like to see a list of services currently active on your account, which include the Unlimited Mobile Plan, Cable Internet 100MB, Basic TV Package, and Home Security System, so you can compare them against available offerings. Finally, you want to check your billing details, including your current balance of $0.00, recent payment of $232.01 on 2025-09-21, and monthly charges totaling $232.01, to ensure accuracy and evaluate cost-saving opportunities. You prefer to keep auto-pay disabled for now to maintain manual control over payments.\n\nUse jordan.jackson2540@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'jordan_jackson_5473', 'action': 'list'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'jordan_jackson_5473'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='drew.thomas8153@email.com',
        instruction='You are drew_thomas_8834, a senior customer with email drew.thomas8153@email.com. You want to remove the Fiber Internet 1GB service from your account because you no longer need home internet. This change reduces your monthly charges and simplifies your services to only the mobile_senior plan, which fits your usage as a senior user who primarily relies on mobile connectivity.\n\nUse drew.thomas8153@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'drew_thomas_8834', 'action': 'remove', 'service_id': 'internet_fiber_1gb'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'drew_thomas_8834'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.wilson5381@email.com',
        instruction='You are Harper Wilson (harper.wilson5381@email.com). You want to make a payment of $89.84 using your credit card for September 18, 2025, to clear your current balance, because you prefer to keep your account up to date. You would like to add the Unlimited Mobile Plan to your account for better data access and service quality, as your current mobile_basic plan has limitations. You prefer Apple devices, specifically the iPhone 13, which you currently use. However, it has been experiencing battery drain issues, so you want troubleshooting guidance to improve battery life and avoid frequent charging. You would like to receive the plan details and device specifications to better understand your services and device capabilities.\n\nUse harper.wilson5381@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'harper_wilson_5062', 'amount': 89.84, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'harper_wilson_5062'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 13'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 13', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'harper_wilson_5062', 'action': 'add', 'service_id': 'mobile_unlimited'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.martinez5108@email.com',
        instruction='You are rowan_martinez_8235. You want to update your billing preferences to enable paperless billing for environmental and convenience reasons, disable auto-pay because you prefer manual control over payments, and switch to a quarterly billing cycle to better align with your budgeting schedule. After that, you would like to update your open support ticket TICKET00072 to resolved status with urgent priority because the issue has been addressed but requires immediate closure confirmation. You also want troubleshooting for battery drain issues on your Apple iPhone SE (3rd gen) because the device loses charge quickly during daily use. Finally, you would like to remove the Basic Mobile Plan from your account as it no longer meets your usage needs.\n\nUse rowan.martinez5108@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_martinez_8235', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_martinez_8235'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_martinez_8235', 'category': 'billing'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00072'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00072', 'status': 'resolved', 'priority': 'urgent'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'rowan_martinez_8235', 'action': 'remove', 'service_id': 'mobile_basic'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_basic'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.hall2588@email.com',
        instruction='You are alex.hall2588@email.com. You want to remove the Unlimited Mobile Plan from your account because you are reevaluating your mobile needs. Before proceeding, you would like to understand the plan details and the specifications of your iPhone 13, as it is currently associated with the mobile service and you want to ensure compatibility and feature understanding. You prefer Apple devices, and the iPhone 13 is your current mobile phone, so knowing its capabilities matters for your decision-making.\n\nUse alex.hall2588@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'alex_hall_3010', 'action': 'remove', 'service_id': 'mobile_unlimited'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_hall_3010'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 13'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.king7459@email.com',
        instruction='You are sam_king_1289 (sam.king7459@email.com). You want to remove the Fiber Internet 1GB service from your account because you are downsizing your home services. Before proceeding, you would like to review your current billing details to understand the impact on your monthly charges. You also want to learn more about the Fiber Internet 1GB service you are canceling, including its speed and reliability, and about the Basic WiFi Router currently provided with it, since you plan to either return it or replace it with a newer model after cancellation.\n\nUse sam.king7459@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'sam_king_1289', 'action': 'remove', 'service_id': 'internet_fiber_1gb'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_king_1289'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='riley.allen8517@email.com',
        instruction="You are Riley Allen. You want to know your discounted rate for the Senior Mobile Plan because you're eligible for the senior discount, and the original price of $45.00 should be reduced by $5 to $40.00. You also want to review your current billing details for accuracy and personal record. Later, you would like to add the Sports TV Package to your services for access to live sports, and you need a support ticket created with medium priority to address an issue with your account settings. After that, you would like to learn more about the Sports TV Package, including its features and channel lineup, to ensure it meets your viewing needs. You also want detailed information about your Google Pixel 8, which is made by Google, to confirm its compatibility with the new service and understand its capabilities.\n\nUse riley.allen8517@email.com for authentication.",
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'riley_allen_6154'}),
            Action(name='manage_service', kwargs={'customer_id': 'riley_allen_6154', 'action': 'add', 'service_id': 'tv_sports_package'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'riley_allen_6154', 'category': 'account', 'priority': 'medium'}),
            Action(name='get_service_details', kwargs={'service_id': 'tv_sports_package'}),
            Action(name='get_device_details', kwargs={'device_name': 'Google Pixel 8'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.anderson8510@email.com',
        instruction="You are Elliot Anderson, email elliot.anderson8510@email.com, a senior customer on the mobile_senior plan. You want to know your discounted mobile plan price because you are eligible for the senior discount, and the plan's original $45.00 rate should reflect a $5 reduction, resulting in a $40.00 monthly cost. You also want your full billing details because you are reviewing your current charges and payment history, which shows a $0.00 balance and a recent payment of $242.51. Later, you would like a list of all services on your account to understand what you are currently subscribed to, which includes the Fiber Internet 1GB and Premium TV services. At the same time, you want to file a support ticket for your account with medium priority because you have general account-related questions that need attention. After that, you would like detailed information about your Fiber Internet 1GB service because you are interested in your internet speed and service features, and you also want specifications for the Enterprise Router because you believe it is part of your service bundle, even though your account currently includes a Standard WiFi Router instead.\n\nUse elliot.anderson8510@email.com for authentication.",
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'elliot_anderson_6407'}),
            Action(name='manage_service', kwargs={'customer_id': 'elliot_anderson_6407', 'action': 'list'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_anderson_6407', 'category': 'account', 'priority': 'medium'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'Enterprise Router'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson2185@email.com',
        instruction='You are Quinn Wilson (quinn_wilson_7642). You want to upgrade your internet service by adding the Fiber Internet 1GB plan because it offers faster speeds and better reliability than your current 100 Mbps cable connection. You would like to confirm the service details—Fiber Internet 1GB, $80.00 per month—and proceed with adding it to your account. After the upgrade, you expect improved performance for streaming, video calls, and multiple connected devices at home.\n\nUse quinn.wilson2185@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_wilson_7642', 'action': 'add', 'service_id': 'internet_fiber_1gb'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.lee2299@email.com',
        instruction='You are Alex Lee (alex.lee2299@email.com), a senior customer on the Senior Mobile Plan. You want to know the discounted price of your mobile service because you are eligible for the senior discount, and the calculation shows it reduces the $45.00 original price to $40.00. You would like to review your current billing details to understand your monthly charges and payment history, which show a current balance of $0.00 and consistent auto-pay usage. Although your billing preferences are already set to paperless billing and auto-pay with a monthly cycle, you prefer to confirm these settings for accuracy and control. You want a list of all active services on your account—Senior Mobile Plan, Cable Internet 500MB, Basic TV Package, and Home Security System—to verify what you currently use. Later, you would like to see the full list of available services in the catalog, including options like Fiber Internet, Premium TV, and Business Mobile, for future reference and potential upgrades.\n\nUse alex.lee2299@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_lee_6742'}),
            Action(name='manage_billing', kwargs={'customer_id': 'alex_lee_6742', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='manage_service', kwargs={'customer_id': 'alex_lee_6742', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.garcia6852@email.com',
        instruction='You are reese_garcia_3039, a senior customer on the Senior Mobile Plan. You want to know your discounted monthly rate because you qualify for the senior discount, and the plan price of $45.00 should reflect a $5 reduction, resulting in a final cost of $40.00. You also want to review your current billing details to understand your charges and payment history. You would like to update your billing preferences to enable auto-pay with your credit card and maintain paperless billing on a monthly cycle for better convenience and payment security. You want to confirm your current services—Senior Mobile Plan, Cable Internet 500MB, and Premium TV Package—to ensure accuracy. Later, you would like to explore other available services in the catalog, such as Fiber Internet 1GB or the Basic Mobile Plan, to evaluate potential future upgrades or changes based on your usage needs and value preferences.\n\nUse reese.garcia6852@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_garcia_3039'}),
            Action(name='manage_billing', kwargs={'customer_id': 'reese_garcia_3039', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='manage_service', kwargs={'customer_id': 'reese_garcia_3039', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.garcia2823@email.com',
        instruction='You are sam_garcia_2071. You want to remove the Home Security System service from your account because you are looking to simplify your telecom package. After that, you would like to update your billing preferences to disable auto-pay and switch to a quarterly billing cycle for better payment control. Later, you will make a payment of $132.21 using your credit card to clear your outstanding balance.\n\nUse sam.garcia2823@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'sam_garcia_2071', 'action': 'remove', 'service_id': 'home_security'}),
            Action(name='manage_billing', kwargs={'customer_id': 'sam_garcia_2071', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'sam_garcia_2071', 'amount': 132.21, 'method': 'credit_card', 'date': '2025-10-28'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.young6478@email.com',
        instruction="You are Jamie Young (jamie_young_6769), a residential customer in Mountain View, CA. You want to remove the Unlimited Mobile Plan from your account to reduce monthly expenses, as you are streamlining your services. You would like to update your billing preferences to enable auto-pay for payment convenience, keep paperless billing for environmental and digital access reasons, and switch to a quarterly billing cycle for better alignment with your financial planning. After that, you intend to make a one-time payment of $48.11 using your credit card on today's date to clear your outstanding balance, ensuring your account remains in good standing.\n\nUse jamie.young6478@email.com for authentication.",
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'jamie_young_6769', 'action': 'remove', 'service_id': 'mobile_unlimited'}),
            Action(name='manage_billing', kwargs={'customer_id': 'jamie_young_6769', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'jamie_young_6769', 'amount': 48.11, 'method': 'credit_card', 'date': '2025-10-05'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='riley.martinez9267@email.com',
        instruction='You are Riley Martinez (riley.martinez9267@email.com). You want to update your billing preferences by disabling paperless billing because you prefer receiving physical statements, disabling auto-pay for greater control over payment timing, and switching to a quarterly billing cycle to better align with your budgeting schedule. You also want to remove the Premium TV Package service to reduce monthly expenses. Additionally, your Samsung Galaxy S23 mobile phone has no service, so you need troubleshooting guidance because it is currently unusable for calls and data. Later, you would like to create a high-priority support ticket for the device issue since the phone is critical for daily communication. After that, you want to add a Conference Phone System to your account for business use in meetings, and you prefer Polycom devices for reliability in professional settings, specifically the Trio-8800 model. You also want detailed specifications of the Conference Phone System to confirm it meets your office requirements.\n\nUse riley.martinez9267@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'riley_martinez_5241', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'riley_martinez_5241', 'action': 'remove', 'service_id': 'tv_premium'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'no_service'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'riley_martinez_5241', 'category': 'device', 'priority': 'high'}),
            Action(name='add_device', kwargs={'customer_id': 'riley_martinez_5241', 'device_name': 'Conference Phone System'}),
            Action(name='get_device_details', kwargs={'device_name': 'Conference Phone System'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='riley.patel5861@email.com',
        instruction='You are Riley Patel (riley.patel5861@email.com). You want to update your billing preferences to enable auto-pay and switch to a quarterly billing cycle while continuing paperless billing because you prefer automated, less frequent payments and want to reduce physical mail. You also want to cancel your Basic Mobile Plan as it no longer meets your usage needs. Your Samsung Galaxy S23 is currently experiencing no service, so you need troubleshooting assistance because it is your primary device and essential for daily communication. Later, you would like to add a new iPhone 15 Pro to your account because you prefer Apple devices for their ecosystem integration, and the iPhone 15 Pro offers advanced features you rely on. You prefer the iPhone 15 Pro, but would accept another current-generation iPhone if unavailable. After adding the device, you would like a high-priority support ticket created to report ongoing device issues since timely resolution is important for your connectivity needs. Finally, you would like to verify the specifications of the iPhone 15 Pro before setup to ensure compatibility and optimal performance.\n\nUse riley.patel5861@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'riley_patel_6045', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'riley_patel_6045', 'action': 'remove', 'service_id': 'mobile_basic'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'no_service'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'riley_patel_6045', 'category': 'device', 'priority': 'high'}),
            Action(name='add_device', kwargs={'customer_id': 'riley_patel_6045', 'device_name': 'iPhone 15 Pro'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.walker6369@email.com',
        instruction='You are taylor_walker_0047, a senior customer on the Senior Mobile Plan. You want to confirm your discounted monthly rate of $40.00 because you qualify for the senior discount, which reduces the original $45.00 rate by $5.00. You would like to verify the details of your current Cable Internet 500MB service, which costs $55.00 per month, because you are considering removing it. You prefer to remove this internet service from your account to simplify your billing and reduce expenses. After that, you would like to explore all available services so you can evaluate better options, particularly interested in potentially switching to Fiber Internet 500MB at $60.00/month or keeping a lower-cost alternative, because you value reliable internet but also want to maintain affordability in retirement.\n\nUse taylor.walker6369@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_cable_500mb'}),
            Action(name='manage_service', kwargs={'customer_id': 'taylor_walker_0047', 'action': 'remove', 'service_id': 'internet_cable_500mb'}),
            Action(name='get_services', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.garcia6112@email.com',
        instruction="You are Morgan Garcia (morgan.garcia6112@email.com), a senior customer currently on the Senior Mobile Plan. You want to know your discounted monthly rate, which is $40.00 after applying the senior discount to the original $45.00 price, because you want to confirm your eligible savings. You would like to learn about the Unlimited Mobile Plan, priced at $85.00 per month, because you are exploring higher-tier mobile options. You want a list of your current services—Senior Mobile Plan, Cable Internet 100MB, and Premium TV Package—because you want to understand what you're currently paying for. Finally, you would like to see all available services in the catalog, including fiber internet, family and business mobile plans, and additional TV and security options, because you are considering potential upgrades or changes to your current package.\n\nUse morgan.garcia6112@email.com for authentication.",
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='manage_service', kwargs={'customer_id': 'morgan_garcia_8324', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='parker.clark7951@email.com',
        instruction='You are parker.clark7951@email.com. You want to check the status of your open support ticket TICKET00118 because you are experiencing ongoing service concerns. You also want to review your billing details to understand your current charges, especially related to your Cable Internet 500MB service, which you rely on for home connectivity. You are interested in the specifications of the iPhone 15 Pro, manufactured by Apple, as a potential device upgrade due to its advanced features, even though you currently use other Apple and Android devices. Since your current internet service is not fiber and speeds may be limited, you would like a new support ticket created for internet performance issues with medium priority if further troubleshooting is needed, to improve reliability for daily use. You prefer to pay by bank transfer with auto-pay enabled and paperless billing, as reflected in your current preferences.\n\nUse parker.clark7951@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00118'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'parker_clark_0821'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'parker_clark_0821', 'category': 'internet', 'priority': 'medium'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.anderson8524@email.com',
        instruction="You are Elliot Anderson, customer elliot.anderson8524@email.com. You want to open a billing-related support ticket and review your current billing details because you have a concern about your account. You would like information about your Unlimited Mobile Plan to better understand your monthly charges, which are currently auto-paid via credit card. Later, you would like assistance with your iPhone 15 Pro, which is experiencing battery drain issues. You prefer Apple devices and specifically the iPhone 15 Pro model. You want troubleshooting steps for the battery issue, verification of the device's specifications, and to have the device added to your account for service association.\n\nUse elliot.anderson8524@email.com for authentication.",
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_anderson_3546', 'category': 'billing'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'elliot_anderson_3546'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='add_device', kwargs={'customer_id': 'elliot_anderson_3546', 'device_name': 'iPhone 15 Pro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='skyler.white6855@email.com',
        instruction='You are Skyler White (skyler_white_1594), a business customer with an existing mobile business plan. You want to create a support ticket for your mobile service with medium priority because you are experiencing service issues. You would also like to review your current billing details to understand your charges, and you are interested in learning more about the Unlimited Mobile Plan for potential comparison, as it offers a simpler individual plan structure at $85/month. Later, you report that your iPhone 15 Pro is experiencing slow speeds, which affects your daily productivity. You prefer Apple devices and specifically use the iPhone 15 Pro, so you would like troubleshooting steps to resolve the speed issue. You also want to confirm the device specifications, which are for an Apple iPhone 15 Pro, to ensure compatibility and performance expectations. Although the device is already registered on your account, you wish to ensure it is properly associated with your service for support purposes.\n\nUse skyler.white6855@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'skyler_white_1594', 'category': 'mobile', 'priority': 'medium'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'skyler_white_1594'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'slow_speeds'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='add_device', kwargs={'customer_id': 'skyler_white_1594', 'device_name': 'iPhone 15 Pro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.lee1419@email.com',
        instruction='You are Emerson Lee (emerson_lee_1092), a residential customer in Austin, TX. You want to remove the Fiber Internet 500MB internet plan because you are looking to reduce costs or switch providers. You would like to update your billing preferences to enable paperless billing and auto-pay for convenience and environmental reasons, and change your billing cycle to quarterly to better align with your financial planning. You are also interested in understanding the cost of the Fiber Internet 500MB plan, which is $60.00 per month, and what it would be with the senior discount applied, which would reduce it to $55.00, though you are not currently on the senior plan.\n\nUse emerson.lee1419@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'emerson_lee_1092', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'emerson_lee_1092', 'action': 'remove', 'service_id': 'internet_fiber_500mb'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_500mb'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.clark0162@email.com',
        instruction='You are emerson_clark_1026, email emerson.clark0162@email.com. You want to remove the Premium TV Package to reduce monthly expenses. You would like to update your billing preferences to enable paperless billing and auto-pay with an annual billing cycle for greater convenience and better cost tracking. You also want confirmation that your Senior Mobile Plan is correctly discounted to $40.00 per month with the senior discount, as you are a senior customer and expect this benefit to be applied. You prefer the Senior Mobile Plan for its affordability and suitability to your usage needs.\n\nUse emerson.clark0162@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'emerson_clark_1026', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'annual'}),
            Action(name='manage_service', kwargs={'customer_id': 'emerson_clark_1026', 'action': 'remove', 'service_id': 'tv_premium'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.hall6556@email.com',
        instruction="You are Morgan Hall (morgan.hall6556@email.com), a residential customer in Chicago. You want to upgrade your internet service to Fiber Internet 1GB because your current 500mb plan no longer meets your household's streaming and work-from-home needs. Alongside this, you would like to add a new iPhone 15 Pro to your account, as you prefer Apple devices for their ecosystem integration and long-term reliability. Later, you would like to update your open support ticket (TICKET00156), changing its status to resolved and escalating the priority to urgent, because the issue has been fixed but requires immediate confirmation and closure for billing and service accuracy.\n\nUse morgan.hall6556@email.com for authentication.",
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='manage_service', kwargs={'customer_id': 'morgan_hall_4954', 'action': 'add', 'service_id': 'internet_fiber_1gb'}),
            Action(name='add_device', kwargs={'customer_id': 'morgan_hall_4954', 'device_name': 'iPhone 15 Pro'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00156'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00156', 'status': 'resolved', 'priority': 'urgent'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'morgan_hall_4954', 'category': 'internet'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'morgan_hall_4954'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.jackson9491@email.com',
        instruction='You are Jamie Jackson (jamie.jackson9491@email.com). You want to learn about the Unlimited Mobile Plan and review your current billing details because you are evaluating your service options and costs. Your current services include the Family Plan - 4 Lines, Cable Internet 100MB, and Basic TV Package, with a monthly bill of $267.38 paid via bank transfer, and you prefer paperless billing. You would like to list all your devices and troubleshoot the battery drain on your Apple iPhone 15 because it is affecting daily usability, and you rely on the device for communication. After that, you want to see all available services to explore potential upgrades or changes. You are also interested in how the senior discount applies to a $45.00 plan, which would reduce the cost to $40.00, indicating a possible interest in switching to the Senior Mobile Plan for cost savings, though you have not yet requested the change.\n\nUse jamie.jackson9491@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'jamie_jackson_7919'}),
            Action(name='manage_service', kwargs={'customer_id': 'jamie_jackson_7919', 'action': 'list'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15', 'issue': 'battery_drain'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.allen7082@email.com',
        instruction='You are Quinn Allen (quinn.allen7082@email.com). You want to understand the details of the Fiber Internet 1GB plan because you are considering upgrading from your current Cable Internet 100MB service. You also want to review your current billing details to ensure accuracy and maintain control over your monthly expenses. Later, you would like to remove your Cable Internet 100MB service as it no longer meets your speed needs. At the same time, you are experiencing battery drain issues with your Apple iPhone 15 Pro, which you rely on daily, so you would like troubleshooting guidance to improve its performance. After that, you want to see the full list of available services to explore better options across mobile, internet, TV, and security. Finally, since you qualify for senior benefits, you would like to know the discounted price of a $45.00 service, which becomes $40.00 with the senior discount, to evaluate potential savings on eligible plans like the Senior Mobile Plan. You prefer to pay by bank transfer as it is your current and trusted payment method.\n\nUse quinn.allen7082@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_allen_6441'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_allen_6441', 'action': 'remove', 'service_id': 'internet_cable_100mb'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.lewis7779@email.com',
        instruction='You are reese_lewis_4991, and your Apple iPhone SE (3rd gen) is experiencing battery drain issues, so you want troubleshooting steps to resolve the problem because the device battery does not last through the day. You would like a high-priority support ticket created for this device issue since initial troubleshooting did not fix the problem. Later, you want the ticket escalated to urgent priority and marked as in_progress to ensure faster resolution because the phone is essential for daily communication.\n\nUse reese.lewis7779@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'reese_lewis_4991', 'category': 'device', 'priority': 'high'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET241', 'status': 'in_progress', 'priority': 'urgent'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.harris4268@email.com',
        instruction='You are Jamie Harris (jamie.harris4268@email.com). You want to troubleshoot battery drain on your Samsung Galaxy A54 because the device is losing charge too quickly during normal use. You prefer Samsung devices and specifically the Galaxy A54 model, which is your primary mobile phone. You would like a new support ticket created for this device issue to ensure it is formally tracked. Later, you want to update your existing support ticket (TICKET00167) by changing its status to in_progress and priority to urgent, because the issue it covers has become more time-sensitive and requires immediate attention from the support team.\n\nUse jamie.harris4268@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'jamie_harris_3456', 'category': 'device'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00167', 'status': 'in_progress', 'priority': 'urgent'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.wilson2953@email.com',
        instruction='You are Reese Wilson (reese_wilson_1963). You want to add a Samsung Galaxy S23 to your account because you recently acquired the device and need it activated for service. Since the device is made by Samsung, you prefer Samsung phones for their feature integration. After adding it, you are experiencing slow speeds on the Samsung Galaxy S23 and would like troubleshooting because the performance is below expectations for your internet usage. You would like to open a support ticket for this internet issue and escalate it to high priority since reliable connectivity is important for daily use. You also want to review the specifications of the Samsung Galaxy S23 to confirm compatibility and features. Additionally, you would like to retrieve your current billing details to verify charges. Later, you want to update your billing preferences by disabling paperless billing and auto-pay because you prefer to manually review invoices and control payment timing, and you would like to switch to a quarterly billing cycle for better budget alignment. After that, you would like to make a $50.00 payment using your credit card on September 20, 2025, to reduce your balance proactively.\n\nUse reese.wilson2953@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'reese_wilson_1963', 'device_name': 'Samsung Galaxy S23'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'slow_speeds'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy S23'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'reese_wilson_1963', 'category': 'internet'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_wilson_1963'}),
            Action(name='manage_billing', kwargs={'customer_id': 'reese_wilson_1963', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'reese_wilson_1963', 'amount': 50.0, 'method': 'credit_card', 'date': '2025-09-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.young8645@email.com',
        instruction='You are Jamie Young (jamie_young_2580). You want to remove the Fiber Internet 1GB service from your account because you are switching providers, and you prefer no further charges or equipment recovery issues. After that, you would like a support ticket created in the internet category to formally document the service discontinuation and ensure a clear record of the termination request.\n\nUse jamie.young8645@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'jamie_young_2580', 'action': 'remove', 'service_id': 'internet_fiber_1gb'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'jamie_young_2580', 'category': 'internet'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.allen0067@email.com',
        instruction='You are Taylor Allen (taylor.allen0067@email.com), a senior customer with the Senior Mobile Plan. You want troubleshooting for your iPhone 14 because it is experiencing battery drain, and you need the device details since it is your primary mobile phone. You prefer Apple devices, specifically the iPhone 14 model, as it is currently your main device. Later, you would like to know what the Senior Mobile Plan includes and confirm its price after the senior discount, because you want to verify your billing accuracy. The plan originally costs $45.00, and after applying the $5 senior discount, you would like confirmation that the correct discounted price of $40.00 is reflected in your account.\n\nUse taylor.allen0067@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.garcia9940@email.com',
        instruction='You are Elliot Garcia (elliot_garcia_0237). You want to make a $54.12 payment using your credit card today to clear your outstanding balance because you prefer to keep your account in good standing. After that, you would like a billing support ticket created to dispute part of the charges, initially set to medium priority, because you noticed an unexpected late fee on your bill. Later, you escalate the ticket to urgent priority and change its status to in_progress because you need immediate resolution due to an upcoming payment cycle and want to ensure the disputed amount is reviewed promptly.\n\nUse elliot.garcia9940@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'elliot_garcia_0237', 'amount': 54.12, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_garcia_0237', 'category': 'billing', 'priority': 'medium'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET241', 'status': 'in_progress', 'priority': 'urgent'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET241'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.brown9199@email.com',
        instruction='You are taylor_brown_9301, with email taylor.brown9199@email.com. You want to review all available telecom services because you are confirming your current options as a senior customer. You would like to see the details of your current plan, the Senior Mobile Plan, because you want to understand its features and confirm it is correctly applied to your account. You also want to verify the discounted price of the plan, which should reflect a $5 senior discount applied to the original $45.00 monthly rate, resulting in a final charge of $40.00, so you can ensure billing accuracy.\n\nUse taylor.brown9199@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.white0148@email.com',
        instruction='You are sam_white_4704. You want to review all available telecom services to understand your options. You specifically want details about the Senior Mobile Plan because you are eligible for the senior discount. You would like the final price of the plan after applying the $5 senior discount, which results in a cost of $40.00 per month, to confirm your affordable and suitable mobile service as a senior customer.\n\nUse sam.white0148@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.garcia0789@email.com',
        instruction='You are Quinn Garcia (quinn.garcia0789@email.com), a senior customer on the Senior Mobile Plan. Your iPhone 14 is experiencing battery drain issues, so you want troubleshooting guidance because the device loses power too quickly during daily use. You would like to keep your current service as it fits your usage and budget. You prefer Apple devices, specifically the iPhone 14, which is already on your account and linked to your mobile service. You would like to review your current billing details for clarity. You want to update your billing preferences to enable paperless billing (already active) and switch to auto-pay with a credit card for better payment control, and you prefer a monthly billing cycle to match your budgeting habits. You would like to make a nominal $0.00 payment today using a credit card to test the new auto-pay setup. You are interested in the senior discount applied to your plan, which reduces your monthly Senior Mobile Plan cost from $45.00 to $40.00, and you value this discount for its affordability.\n\nUse quinn.garcia0789@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'quinn_garcia_3466', 'category': 'device', 'priority': 'medium'}),
            Action(name='add_device', kwargs={'customer_id': 'quinn_garcia_3466', 'device_name': 'iPhone 14'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_garcia_3466', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_garcia_3466'}),
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_garcia_3466', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='record_payment', kwargs={'customer_id': 'quinn_garcia_3466', 'amount': 0.0, 'method': 'credit_card', 'date': '2025-10-25'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00208'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00208', 'status': 'resolved', 'priority': 'low'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='cameron.martinez5331@email.com',
        instruction='You are cameron_martinez_6591. You want to verify the details of your iPhone 15 Pro because you need to confirm it is properly registered on your account. You would like to formally add the iPhone 15 Pro to your account to ensure service continuity, as it is your primary mobile device. You prefer Apple devices, specifically the iPhone 15 Pro model, for compatibility with your existing ecosystem. Later, you would like troubleshooting for slow speeds on the iPhone 15 Pro because the performance issue is affecting your daily usage, especially while streaming and browsing on the Unlimited Mobile Plan.\n\nUse cameron.martinez5331@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='add_device', kwargs={'customer_id': 'cameron_martinez_6591', 'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'slow_speeds'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.hall6379@email.com',
        instruction='You are reese_hall_9712, a business customer using Apple devices, with a preference for iPhones including the iPhone 15 Pro. You want to know the details of your iPhone 15 Pro because you are experiencing service issues with it. You would like to create a new support ticket for the device issue with category device since the phone is critical for business operations. Later, you want to modify existing ticket TICKET00094 by changing its status to in_progress and priority to urgent because the issue is time-sensitive and requires immediate attention. You also want to check the current status of ticket TICKET00094 to confirm the update was applied. You prefer to review your billing details to ensure accuracy and because you are considering service additions. You are interested in the Premium TV Package and would like to know its details before adding it to your account. You are currently experiencing no_service on your iPhone 15 Pro, which disrupts connectivity, so you need troubleshooting guidance. You would like to add the Premium TV Package to your account to expand home entertainment options. You inquired about the senior discount pricing on a $45.00 service, which would cost $40.00 with the discount, even though you are not on the senior plan, to understand potential savings.\n\nUse reese.hall6379@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'reese_hall_9712', 'category': 'device'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00094', 'status': 'in_progress', 'priority': 'urgent'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00094'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_hall_9712'}),
            Action(name='get_service_details', kwargs={'service_id': 'tv_premium'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'no_service'}),
            Action(name='manage_service', kwargs={'customer_id': 'reese_hall_9712', 'action': 'add', 'service_id': 'tv_premium'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='taylor.anderson5864@email.com',
        instruction="You are Taylor Anderson (taylor.anderson5864@email.com). You own an iPhone 12, an Apple mobile phone, and are experiencing significant battery drain, so you would like troubleshooting guidance to resolve the issue quickly. After reviewing the steps, you want a support ticket created under the 'device' category because the problem persists and requires technical follow-up. You prefer Apple devices for their ecosystem integration and reliability. You would like the ticket escalated if the issue is not resolved within 48 hours, as the phone is essential for daily communication.\n\nUse taylor.anderson5864@email.com for authentication.",
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 12', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 12'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'taylor_anderson_1691', 'category': 'device'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.jackson3662@email.com',
        instruction='You are elliot_jackson_3919. You own an Apple iPhone 15 Pro and are experiencing unusually fast battery drain, so you would like troubleshooting assistance to identify and resolve the issue because the device is not lasting through the day despite normal usage.\n\nUse elliot.jackson3662@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kendall.lee2343@email.com',
        instruction='You are kendall_lee_9814 (email: kendall.lee2343@email.com). You want to first verify your current billing details because you plan to pay off your outstanding balance today. After confirming the balance of $72.36, which includes a late fee, you would like to make a one-time payment of $72.36 using your credit card to clear the balance immediately and avoid further charges. You prefer this method because you are not currently enrolled in auto-pay and want to maintain control over your payment timing.\n\nUse kendall.lee2343@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'kendall_lee_9814'}),
            Action(name='record_payment', kwargs={'customer_id': 'kendall_lee_9814', 'amount': 72.36, 'method': 'credit_card', 'date': '2025-09-18'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.garcia2286@email.com',
        instruction='You are rowan_garcia_8718. You want to learn about the Fiber Internet 1GB service and the WiFi 6 Router to determine compatibility with your current setup, as you are considering upgrading your home network performance. After reviewing, you would like to add the WiFi 6 Router to your account because it offers better speed and coverage for your fiber connection. You prefer devices from TechCorp due to their reliability, and specifically the WiFi6-Pro model for its advanced networking features. Later, you would like to pay your outstanding balance of $56.19 using your credit card on 2025-09-18 because the last payment was marked as late and you want to avoid further fees. After that, you would like to open a high-priority support ticket regarding recent billing charges because you noticed unexpected late fees and want clarification promptly.\n\nUse rowan.garcia2286@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
            Action(name='add_device', kwargs={'customer_id': 'rowan_garcia_8718', 'device_name': 'WiFi 6 Router'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_garcia_8718'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_garcia_8718', 'amount': 56.19, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_garcia_8718', 'category': 'billing', 'priority': 'high'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='casey.clark0465@email.com',
        instruction='You are Casey Clark (casey.clark0465@email.com). You want to upgrade your internet service to Fiber Internet 1GB because you need faster and more reliable connectivity for household usage. You are interested in the technical and pricing details of this service, which costs $80.00 per month. You prefer networking equipment from TechCorp and specifically want the WiFi 6 Router (model WiFi6-Pro) to support your new internet service, but it is already on your account and currently associated with your existing cable internet. Later, you would like to pay off your outstanding balance of $37.10 using your credit card on 2025-09-18 to bring your account current, which has been successfully applied. After that, you would like to create a billing support ticket (TICKET241) to inquire about recent charges, including a late fee, so you can understand your billing history and prevent future issues. You prefer to pay by credit card and keep paperless billing enabled.\n\nUse casey.clark0465@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
            Action(name='add_device', kwargs={'customer_id': 'casey_clark_6698', 'device_name': 'WiFi 6 Router'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'casey_clark_6698'}),
            Action(name='record_payment', kwargs={'customer_id': 'casey_clark_6698', 'amount': 37.1, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'casey_clark_6698', 'category': 'billing'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='parker.lee0757@email.com',
        instruction='You are Parker Lee (parker_lee_9680). You want to review your billing details because you are verifying your current charges and payment history. After that, you would like to create a new support ticket with medium priority regarding a billing inquiry since you have questions about your monthly charges. Later, you want to update your existing ticket TICKET00133 to in_progress status and high priority because the issue has become more urgent. You would like to know the details of the Unlimited Mobile Plan to better understand your current mobile service. You prefer Apple devices and specifically the iPhone 15 Pro model, so you would like troubleshooting steps for battery drain issues because the device loses charge quickly during daily use. You are on a senior plan and would like to know the discounted price for a $45.00 service, which after the $5 senior discount is $40.00, to confirm the accuracy of your billing.\n\nUse parker.lee0757@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'parker_lee_9680'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'parker_lee_9680', 'category': 'billing', 'priority': 'medium'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00133', 'status': 'in_progress', 'priority': 'high'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.anderson5696@email.com',
        instruction='You are Harper Anderson (harper.anderson5696@email.com), a business customer with services including Fiber Internet 2GB and a 10-line mobile business plan. You want to review your current billing details because you are assessing your monthly expenses, which total $894.38, paid via invoice on a monthly cycle. You would like to create a new support ticket for slow internet speeds affecting your Standard WiFi Router, a TechCorp networking device, because it is underperforming for your business needs. After that, you want to escalate your existing open ticket (TICKET00160) to high priority for faster resolution, as the current low priority is delaying support. You are also interested in understanding potential savings through the senior discount program and would like to know that a $45.00 plan would be reduced to $40.00 with the $5 senior discount, though you are not currently applying it to any service.\n\nUse harper.anderson5696@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'harper_anderson_9931'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'harper_anderson_9931', 'category': 'internet', 'priority': 'medium'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00160', 'status': 'open', 'priority': 'high'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_2gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'Standard WiFi Router'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Standard WiFi Router', 'issue': 'slow_speeds'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.garcia2286@email.com',
        instruction="You are Rowan Garcia (rowan.garcia2286@email.com), a residential customer in Chicago. You want to review the details of your Family Plan - 4 Lines mobile service because you're confirming your current plan coverage. You also want to update your open support ticket (TICKET00183) to resolved status with low priority since the issue has been addressed. After that, you would like to see all available services to explore potential upgrades, and then confirm your current services to ensure everything is accurate. You prefer to update your billing preferences by enabling paperless billing and auto-pay for convenience, and switching to a quarterly billing cycle to better align with your financial planning. Finally, you intend to make a one-time payment of $56.19 using your credit card to clear your outstanding balance and avoid future late fees.\n\nUse rowan.garcia2286@email.com for authentication.",
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_family_4lines'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00183'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00183', 'status': 'resolved', 'priority': 'low'}),
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'rowan_garcia_8718', 'action': 'list'}),
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_garcia_8718', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_garcia_8718', 'amount': 56.19, 'method': 'credit_card', 'date': '2025-09-18'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.brown6471@email.com',
        instruction='You are Sam Brown (sam.brown6471@email.com), a residential customer since 2020. You want to know the details of your Unlimited Mobile Plan because you are reviewing your current services. You would like to review all your current services to ensure they meet your needs. You prefer to update your billing preferences to paperless billing with no auto-pay and a monthly billing cycle for better control over your payments. Later, you would like to pay your outstanding balance of $59.79 using your credit card on September 25, 2025, to clear the late fee and avoid further charges.\n\nUse sam.brown6471@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00197'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00197', 'status': 'in_progress', 'priority': 'high'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_brown_5625', 'category': 'billing', 'priority': 'medium'}),
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'sam_brown_5625', 'action': 'list'}),
            Action(name='manage_billing', kwargs={'customer_id': 'sam_brown_5625', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'monthly'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_brown_5625'}),
            Action(name='record_payment', kwargs={'customer_id': 'sam_brown_5625', 'amount': 59.79, 'method': 'credit_card', 'date': '2025-09-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson4865@email.com',
        instruction='You are quinn_wilson_4735, with email quinn.wilson4865@email.com. You want to check the status of your open support ticket TICKET00214, which is currently low priority, because you are following up on an ongoing issue. You also want to review your billing details to understand your current charges and payment setup. You would like to remove the Cable Internet 100MB service from your account to simplify your plan and reduce costs, as you no longer need the service. Later, you would like to update your billing preferences to enable paperless billing for convenience, keep auto-pay enabled with your credit card for reliability, and switch to an annual billing cycle to better manage your payments and reduce billing frequency.\n\nUse quinn.wilson4865@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00214'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_wilson_4735'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_wilson_4735', 'action': 'remove', 'service_id': 'internet_cable_100mb'}),
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_wilson_4735', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'annual'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.nguyen0038@email.com',
        instruction='You are emerson_nguyen_6383, a senior customer on the mobile_senior plan, and you want to confirm your monthly rate with the senior discount applied because you value transparency in billing; the $45.00 plan is reduced to $40.00 with the discount. After that, you would like to update your billing preferences to enable paperless billing and auto-pay, and switch to an annual billing cycle because you prefer a streamlined, low-maintenance payment process that reduces administrative effort and ensures timely payments.\n\nUse emerson.nguyen0038@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'emerson_nguyen_6383'}),
            Action(name='manage_billing', kwargs={'customer_id': 'emerson_nguyen_6383', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'annual'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.martinez9975@email.com',
        instruction='You are rowan_martinez_5186, a senior customer on the Senior Mobile Plan. You want to confirm the discounted price of your mobile service, which is $40.00 after applying the senior discount to the original $45.00 rate, because you want to verify your current plan cost. You would like to keep paperless billing and auto-pay enabled for convenience and environmental reasons. Later, you want to change your billing cycle to quarterly for better budget management, and you requested your current billing details to verify the accuracy of your account settings.\n\nUse rowan.martinez9975@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_martinez_5186'}),
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_martinez_5186', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kendall.lee5449@email.com',
        instruction='You are kendall.lee5449@email.com. You want to make a payment of $119.45 using your credit card because you have an outstanding balance that includes a late fee, and you are experiencing billing issues, so you would like to open a support ticket for billing to resolve the matter. Later, you would like to update your billing preferences by enabling auto-pay and switching to a quarterly billing cycle for better financial planning, while keeping paperless billing enabled as you prefer digital records. After that, you would like to confirm the discounted price of your Senior Mobile Plan, which you use as a senior customer, and the rate should reflect the $5 senior discount, resulting in a $40.00 monthly charge instead of $45.00.\n\nUse kendall.lee5449@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'kendall_lee_0640', 'amount': 119.45, 'method': 'credit_card', 'date': '2025-10-22'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'kendall_lee_0640', 'category': 'billing'}),
            Action(name='manage_billing', kwargs={'customer_id': 'kendall_lee_0640', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'kendall_lee_0640'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.king0580@email.com',
        instruction='You are alex_king_8257 (email alex.king0580@email.com). You want to make a payment of $92.56 via credit card on September 18, 2025, to clear your current balance because recent late fees were charged due to missed payments. You also want to create a support ticket in the billing category to address the recurring late fees and prevent future occurrences. After that, you would like to update your billing preferences to enable auto-pay and switch to a quarterly billing cycle to ensure timely payments and avoid late fees, while keeping paperless billing enabled for convenience. Later, you are interested in upgrading to the Unlimited Mobile Plan, which costs $85.00 per month, and you would like to know the discounted price of $80.00 with the senior discount applied because it offers better value and fits your usage needs.\n\nUse alex.king0580@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'alex_king_8257', 'amount': 92.56, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_king_8257', 'category': 'billing'}),
            Action(name='manage_billing', kwargs={'customer_id': 'alex_king_8257', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_king_8257'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '85.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='parker.young1167@email.com',
        instruction='You are parker_young_5701. You want to check the specifications of your iPhone 15 Pro because you need to confirm its compatibility before adding it to your account. The device is an Apple smartphone, model iPhone 15 Pro, in the mobile_phone category. After reviewing the details, you would like to add the iPhone 15 Pro to your account for service activation so you can begin using it on the network.\n\nUse parker.young1167@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='add_device', kwargs={'customer_id': 'parker_young_5701', 'device_name': 'iPhone 15 Pro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.allen2350@email.com',
        instruction="You are Alex Allen (alex.allen2350@email.com). You want to add your new iPhone 15 Pro to your account because it's your preferred device for mobile service, and you need it activated for seamless connectivity. You prefer Apple devices, specifically the iPhone 15 Pro, for its performance and integration with your existing setup. After that, you would like to create a support ticket for device setup assistance to ensure the new phone is properly configured. You want to upgrade your internet service from cable to the Fiber Internet 1GB plan because you need faster and more reliable speeds for streaming and remote work. You would like to add this service to your account and confirm the change. Later, you want to update your billing preferences to enable auto-pay and switch to a quarterly billing cycle for better payment management and convenience. You prefer to pay by bank transfer and want auto-pay enabled with this method to avoid missed payments. Finally, you would like to review your updated billing details to confirm all changes have been applied correctly.\n\nUse alex.allen2350@email.com for authentication.",
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_allen_3726', 'category': 'device', 'priority': 'medium'}),
            Action(name='add_device', kwargs={'customer_id': 'alex_allen_3726', 'device_name': 'iPhone 15 Pro'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='manage_billing', kwargs={'customer_id': 'alex_allen_3726', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'alex_allen_3726', 'action': 'add', 'service_id': 'internet_fiber_1gb'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_allen_3726'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='drew.walker9273@email.com',
        instruction="You are drew_walker_7967. You want to add your new WiFi 6 Router to your account because you recently upgraded your home network and need it registered for service. After that, you would like to create a support ticket for your device issue since you're experiencing connectivity problems and need technical assistance. You are interested in the Fiber Internet 1GB plan and would like to learn more about it because you're considering upgrading from your current 100 Mbps cable internet for faster and more reliable speeds. You want to review your current services to understand what you're currently paying for and ensure accuracy. You also want to see your full billing details to verify your payment history and charges. Later, you would like to update your billing preferences: you prefer paperless billing for environmental and convenience reasons, you want to disable auto-pay to have more control over payment timing, and you would like to switch to a quarterly billing cycle to better manage your cash flow.\n\nUse drew.walker9273@email.com for authentication.",
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'drew_walker_7967', 'category': 'device'}),
            Action(name='add_device', kwargs={'customer_id': 'drew_walker_7967', 'device_name': 'WiFi 6 Router'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='manage_billing', kwargs={'customer_id': 'drew_walker_7967', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'drew_walker_7967', 'action': 'list'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'drew_walker_7967'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.white5781@email.com',
        instruction="You are reese.white5781@email.com. You want to check the status of your open support ticket (TICKET00029) because you need an update on an ongoing issue. You also want to review your billing details to confirm your current charges and payment method, as you prefer to keep your account in good standing. After that, you would like to learn more about upgrading to the Fiber Internet 1GB service because your current 500MB plan may not meet your household's usage needs. You prefer faster speeds for streaming and remote work. Later, you want to see the full list of available services to compare all options and evaluate potential bundles or cost-saving alternatives, ensuring you have the best value for your needs. You prefer to keep auto-pay enabled with your credit card for convenience and reliability.\n\nUse reese.white5781@email.com for authentication.",
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00029'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_white_1093'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_services', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson5782@email.com',
        instruction='You are Quinn Wilson (quinn.wilson5782@email.com), a business customer with the Business Mobile - 10 Lines and Fiber Internet 2 Gbps services. You want to check and escalate your open support ticket TICKET00076 to high priority because the issue is urgent and affecting business operations. After that, you would like to update your billing preferences to enable paperless billing and auto-pay with a monthly billing cycle to ensure timely payments and reduce administrative overhead, as your previous invoice payments have been late. You prefer auto-pay with your existing credit method for consistency. Later, you need assistance with battery drain issues on your iPhone 15 Pro, which you use for business communication, so you would like troubleshooting steps and device details. You prefer Apple devices for their integration and reliability, and specifically use the iPhone 15 Pro for its performance and features.\n\nUse quinn.wilson5782@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_business_10lines'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00076'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00076', 'status': 'open', 'priority': 'high'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'quinn_wilson_5555', 'category': 'billing', 'priority': 'medium'}),
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_wilson_5555', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_wilson_5555', 'action': 'list'}),
            Action(name='get_senior_discount', kwargs={'original_price': '450.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_wilson_5555'}),
            Action(name='add_device', kwargs={'customer_id': 'quinn_wilson_5555', 'device_name': 'iPhone 15 Pro'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='casey.clark0465@email.com',
        instruction='You are Casey Clark (casey.clark0465@email.com). You want to remove the Basic TV Package from your account because you no longer use it and wish to reduce monthly expenses. You would like to add a new Samsung Galaxy S23 to your account, preferring Samsung devices for their camera quality and user interface, with the Galaxy S23 as your preferred model. You prefer to pay off your current balance of $37.10 using a credit card on October 18, 2025, to clear outstanding charges and avoid late fees. After that, you would like a support ticket created for billing-related concerns with medium priority to address recent late fee issues and ensure payment processing is accurate.\n\nUse casey.clark0465@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'casey_clark_6698', 'action': 'remove', 'service_id': 'tv_basic'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'casey_clark_6698'}),
            Action(name='record_payment', kwargs={'customer_id': 'casey_clark_6698', 'amount': 37.1, 'method': 'credit_card', 'date': '2025-10-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'casey_clark_6698', 'category': 'billing', 'priority': 'medium'}),
            Action(name='add_device', kwargs={'customer_id': 'casey_clark_6698', 'device_name': 'Samsung Galaxy S23'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy S23'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.wright6177@email.com',
        instruction='You are jamie.wright6177@email.com. You want to open a high-priority support ticket in the device category because your iPhone 15 has no service and you need urgent assistance. You would like troubleshooting steps for the connectivity issue so you can attempt to restore service immediately. You want to review your current services to confirm your business plan includes the mobile, internet, and phone services you rely on. You prefer Apple devices, and you would like to confirm the iPhone 15 is properly recognized and associated with your account for correct service mapping and support eligibility.\n\nUse jamie.wright6177@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'jamie_wright_6803', 'category': 'device', 'priority': 'high'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15', 'issue': 'no_service'}),
            Action(name='manage_service', kwargs={'customer_id': 'jamie_wright_6803', 'action': 'list'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15'}),
            Action(name='add_device', kwargs={'customer_id': 'jamie_wright_6803', 'device_name': 'iPhone 15'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.thomas5669@email.com',
        instruction='You are Alex Thomas (alex.thomas5669@email.com), a residential customer in Austin, TX. You want to review your current services—Basic Mobile Plan, Cable Internet 500MB, and Premium TV Package—and check your billing details because you have an outstanding balance of $89.19 that you plan to pay. You would like to make a payment of $89.19 using your credit card on 2025-10-05 to clear the balance and avoid further late fees, as your last payment was marked late. You are interested in exploring all available services to evaluate potential upgrades or additions. You would like to create a support ticket for your mobile service because your Samsung Galaxy A54, a Samsung mobile phone, is experiencing significant battery drain that affects daily usability, and troubleshooting steps like restarting and adjusting settings have not resolved the issue. Later, you would like to update your billing preferences to enable paperless billing and auto-pay with your credit card to ensure timely payments and reduce physical clutter, while keeping your billing cycle as monthly for consistency with your budgeting.\n\nUse alex.thomas5669@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'alex_thomas_7404', 'action': 'list'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_thomas_7404'}),
            Action(name='record_payment', kwargs={'customer_id': 'alex_thomas_7404', 'amount': 89.19, 'method': 'credit_card', 'date': '2025-10-05'}),
            Action(name='get_services', kwargs={}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_thomas_7404', 'category': 'mobile'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'battery_drain'}),
            Action(name='manage_billing', kwargs={'customer_id': 'alex_thomas_7404', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.martinez9975@email.com',
        instruction='You are rowan_martinez_5186. You want to learn about the Fiber Internet 1GB service because you are considering upgrading from your current internet plan. You would like to update your billing preferences to enable paperless billing for environmental and convenience reasons, disable auto-pay to have more control over payment timing, and switch to a quarterly billing cycle to better align with your budgeting schedule. After that, you would like to create a support ticket in the billing category with medium priority to discuss your billing changes, and you also want to review your current billing details to verify your account status and charges.\n\nUse rowan.martinez9975@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_martinez_5186', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_martinez_5186', 'category': 'billing', 'priority': 'medium'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_martinez_5186'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.nguyen8363@email.com',
        instruction='You are Avery Nguyen (avery_nguyen_2530). You want to review the Unlimited Mobile Plan because you are considering upgrading your current mobile service for better data benefits. After reviewing, you would like to update your billing preferences to enable paperless billing and auto-pay with your credit card, and switch to a monthly billing cycle for better alignment with your budgeting schedule. Later, you would like to create a support ticket for a billing-related concern to ensure any discrepancies are formally tracked. After that, you would like a full summary of your current billing details, including payment history and monthly charges, to verify your account status and confirm the changes were applied correctly.\n\nUse avery.nguyen8363@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='manage_billing', kwargs={'customer_id': 'avery_nguyen_2530', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'avery_nguyen_2530', 'category': 'billing'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'avery_nguyen_2530'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='riley.walker3176@email.com',
        instruction="You are riley.walker3176@email.com. You want to check the specifications of your iPhone 12 because you are experiencing a 'no service' issue and need to understand the device context before proceeding. You would like to create a new support ticket for the device issue with high priority since the phone is currently unusable for calls and data. After that, you want to update your existing ticket TICKET00098 to status 'in_progress' and priority 'high' because it has been pending longer than expected, and you would like to confirm its latest status to ensure it is being actively handled. You prefer Apple devices, so you would like to add an iPhone 15 Pro to your account as a replacement. You also want to upgrade your mobile service by adding the Unlimited Mobile Plan for $85.00 per month to ensure full data and calling coverage on all devices. Finally, you need troubleshooting support for your iPhone 12's connectivity problem because it has no service despite being in a covered area, and you want to rule out user-side issues before replacement.\n\nUse riley.walker3176@email.com for authentication.",
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 12'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'riley_walker_3495', 'category': 'device', 'priority': 'high'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00098', 'status': 'in_progress', 'priority': 'high'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00098'}),
            Action(name='manage_service', kwargs={'customer_id': 'riley_walker_3495', 'action': 'add', 'service_id': 'mobile_unlimited'}),
            Action(name='add_device', kwargs={'customer_id': 'riley_walker_3495', 'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 12', 'issue': 'no_service'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.martinez2652@email.com',
        instruction='You are Jamie Martinez (jamie.martinez2652@email.com). You want to review the details of your Apple iPhone 15 Pro because you are experiencing battery drain issues and need to understand the device specifications. You also have an open support ticket (TICKET00128) currently at medium priority, and you would like to escalate it to urgent priority because the device issue is affecting daily use. Later, you would like to see a list of your current services—Unlimited Mobile Plan, Cable Internet 100MB, and Basic TV Package—for account review. After that, you want to add a Samsung Galaxy A54 to your account because you prefer Samsung devices for secondary phones, and this model fits your budget and usage needs. You also want troubleshooting guidance for battery drain on your iPhone 15 Pro because the device is losing charge quickly despite minimal use, and you rely on it for communication and daily tasks.\n\nUse jamie.martinez2652@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'jamie_martinez_3329', 'category': 'device', 'priority': 'medium'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00128', 'status': 'open', 'priority': 'urgent'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00128'}),
            Action(name='manage_service', kwargs={'customer_id': 'jamie_martinez_3329', 'action': 'list'}),
            Action(name='add_device', kwargs={'customer_id': 'jamie_martinez_3329', 'device_name': 'Samsung Galaxy A54'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.garcia5456@email.com',
        instruction='You are morgan_garcia_0855. You prefer Apple devices, so you would like to add an iPhone 14 to your account because it fits your preference for reliable, supported smartphones from a trusted brand.\n\nUse morgan.garcia5456@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'morgan_garcia_0855', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'morgan_garcia_0855', 'category': 'device'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'morgan_garcia_0855'}),
            Action(name='manage_service', kwargs={'customer_id': 'morgan_garcia_0855', 'action': 'list'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.wilson8581@email.com',
        instruction='You are Avery Wilson (avery.wilson8581@email.com). You want to add an iPhone 14 to your account because you recently acquired the device and need it connected to your mobile service. You prefer Apple devices, specifically the iPhone 14 model, for compatibility with your existing ecosystem. You would like to know the device specifications to understand its capabilities and ensure it meets your usage needs. You are experiencing issues with the iPhone 14, so you want a support ticket created under the device category to get technical assistance. You would like the ticket to be processed promptly to minimize disruption. You want to add the Premium TV Package to your services to access expanded entertainment content, especially premium channels and on-demand programming. You would like to review your current billing details to understand your monthly charges and payment history, ensuring transparency and control over your account. You are inquiring about the senior discount application on a $45.00 plan, which would reduce the cost to $40.00, to explore potential savings, though your current plan does not reflect senior eligibility based on your account details.\n\nUse avery.wilson8581@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'avery_wilson_0002', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'avery_wilson_0002', 'category': 'device'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'avery_wilson_0002'}),
            Action(name='manage_service', kwargs={'customer_id': 'avery_wilson_0002', 'action': 'add', 'service_id': 'tv_premium'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='casey.garcia9145@email.com',
        instruction='You are Casey Garcia (casey.garcia9145@email.com). You want to verify that your support ticket TICKET00142 is still open, which it is, with medium priority, because you need confirmation that your service issue is being addressed. You would like to review your current billing details, including your $0.00 balance and recent payment history, to ensure accuracy before making changes. After that, you prefer to update your billing preferences to enable auto-pay for convenience and to avoid missed payments, switch from paperless to paper billing because you prefer physical copies for record-keeping, and change your billing cycle to quarterly to better manage your cash flow.\n\nUse casey.garcia9145@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00142'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'casey_garcia_5886'}),
            Action(name='manage_billing', kwargs={'customer_id': 'casey_garcia_5886', 'paperless': False, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
        ],
        outputs=[],
    ),
]
