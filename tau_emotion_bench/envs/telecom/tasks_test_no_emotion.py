from tau_emotion_bench.types import Task, Action


TASKS = [
    Task(
        user_id='alex.wilson0710@email.com',
        instruction='You are Alex Wilson (alex_wilson_8557). You want to add the Sports TV Package to your services because you are interested in expanded sports content. You checked your billing details and confirmed an outstanding balance of $163.98, so you prefer to make a full payment on 2025-09-19 using your credit card to bring your account current. You also want to add a new mobile device to your account, and you prefer Samsung devices, specifically the Galaxy S23, for its performance and compatibility with your existing plan. After adding it, you would like to confirm its details for your records. Finally, you would like to create a support ticket in the mobile category with medium priority to address ongoing connectivity concerns, ensuring your service reliability is improved.\n\nUse alex.wilson0710@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'alex_wilson_8557', 'action': 'add', 'service_id': 'tv_sports_package'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_wilson_8557'}),
            Action(name='record_payment', kwargs={'customer_id': 'alex_wilson_8557', 'amount': 163.98, 'method': 'credit_card', 'date': '2025-09-19'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_wilson_8557', 'category': 'mobile', 'priority': 'medium'}),
            Action(name='add_device', kwargs={'customer_id': 'alex_wilson_8557', 'device_name': 'Samsung Galaxy S23'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy S23'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.lewis1592@email.com',
        instruction='You are Morgan Lewis (morgan.lewis1592@email.com). You are experiencing no service on your iPhone 15 Pro, so you want troubleshooting because the device is essential for daily communication. You prefer Apple devices, specifically the iPhone 15 Pro, and would like a support ticket created for ongoing assistance since the issue persists after basic steps. Later, you would like to pay your outstanding balance of $106.76 by credit card to clear your account on 2025-10-25. After that, you prefer to enable auto-pay for convenience while keeping paperless billing and the monthly billing cycle to maintain control and reduce manual effort.\n\nUse morgan.lewis1592@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'morgan_lewis_7010', 'category': 'mobile'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'no_service'}),
            Action(name='manage_service', kwargs={'customer_id': 'morgan_lewis_7010', 'action': 'list'}),
            Action(name='record_payment', kwargs={'customer_id': 'morgan_lewis_7010', 'amount': 106.76, 'method': 'credit_card', 'date': '2025-10-25'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'morgan_lewis_7010'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='manage_billing', kwargs={'customer_id': 'morgan_lewis_7010', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.clark7888@email.com',
        instruction='You are reese_clark_1767, authenticated via email reese.clark7888@email.com. You want to add a new mobile phone to your account, preferring Apple devices, specifically the iPhone 14, because you are expanding your device options. You would like to add the Unlimited Mobile Plan to support this new device, as mobile_basic plan does not meet your growing usage needs. You want to review your billing details because your current balance is $31.62, and you prefer to keep your account in good standing. You would like to update your billing preferences to enable auto-pay with credit card and maintain paperless billing for convenience and reliability. You prefer to make a payment of $31.62 using credit card on 2025-10-18 to clear your outstanding balance and avoid late fees. After that, you would like to create a support ticket for your device issues with medium priority because your Samsung Galaxy A54 is currently experiencing no service, which affects your connectivity. You also want troubleshooting assistance for the Samsung Galaxy A54 because it is your primary mobile device and losing service disrupts your daily communication.\n\nUse reese.clark7888@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'reese_clark_1767', 'device_name': 'iPhone 14'}),
            Action(name='manage_service', kwargs={'customer_id': 'reese_clark_1767', 'action': 'add', 'service_id': 'mobile_unlimited'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_clark_1767'}),
            Action(name='manage_billing', kwargs={'customer_id': 'reese_clark_1767', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='record_payment', kwargs={'customer_id': 'reese_clark_1767', 'amount': 31.62, 'method': 'credit_card', 'date': '2025-10-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'reese_clark_1767', 'category': 'device', 'priority': 'medium'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy A54'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'no_service'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.harris2506@email.com',
        instruction='You are reese_harris_9472, with email reese.harris2506@email.com. You want to check your billing details because you noticed an outstanding balance of $122.11. You prefer to pay this balance immediately using your credit card for faster processing, even though your default method is bank transfer, to avoid any further late fees. You would like to pay $122.11 using your credit card on 2025-09-18, bringing your current balance to $0.00.\n\nUse reese.harris2506@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_harris_9472'}),
            Action(name='record_payment', kwargs={'customer_id': 'reese_harris_9472', 'amount': 122.11, 'method': 'credit_card', 'date': '2025-09-18'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.clark2808@email.com',
        instruction='You are morgan_clark_6566, authenticated via email morgan.clark2808@email.com. You want to review the details of your Unlimited Mobile Plan because you are verifying your current service commitment. After that, you would like to update your billing preferences to enable auto-pay for payment convenience and to avoid late fees, switch to a quarterly billing cycle for better alignment with your financial planning, and disable paperless billing because you prefer receiving physical bills in the mail.\n\nUse morgan.clark2808@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='manage_billing', kwargs={'customer_id': 'morgan_clark_6566', 'paperless': False, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.garcia5456@email.com',
        instruction='You are morgan_garcia_0855. You would like to add your iPhone 14 to your account because you recently acquired the device and want it associated with your service. Since you prefer Apple devices, the iPhone 14 is your chosen model for seamless integration with your existing ecosystem. After that, you would like to see a list of all services currently on your account—specifically Unlimited Mobile Plan, Cable Internet 100MB, and Basic TV Package—to review your current subscriptions and ensure everything is accurate.\n\nUse morgan.garcia5456@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'morgan_garcia_0855', 'device_name': 'iPhone 14'}),
            Action(name='manage_service', kwargs={'customer_id': 'morgan_garcia_0855', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.harris2015@email.com',
        instruction='You are Quinn Harris (quinn.harris2015@email.com). You want to know the specifications of your Google Pixel 8 because you are reviewing your device capabilities. You prefer devices from Google, and specifically the Pixel 8 model, as it is your current phone. You would like to understand the pricing of the Senior Mobile Plan, which is $45.00 monthly, and after applying the $5 senior discount, you would pay $40.00, because you are evaluating more affordable plan options. You also want to review your current billing details and the features of your Basic Mobile Plan, which costs $35.00 per month, to better understand your service usage and expenses. Later, you would like to see all available services to explore potential upgrades or changes. After that, you want to confirm your current services—Basic Mobile Plan and Cable Internet 500 Mbps—to ensure accuracy. Finally, you would like to make a one-time payment of $39.57 using your credit card on 2025-09-25 to clear your outstanding balance, because you prefer to keep your account in good standing and avoid late fees.\n\nUse quinn.harris2015@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'Google Pixel 8'}),
            Action(name='add_device', kwargs={'customer_id': 'quinn_harris_9291', 'device_name': 'Google Pixel 8'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_harris_9291'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_basic'}),
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_harris_9291', 'action': 'list'}),
            Action(name='record_payment', kwargs={'customer_id': 'quinn_harris_9291', 'amount': 39.57, 'method': 'credit_card', 'date': '2025-09-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.thomas5669@email.com',
        instruction='You are Alex Thomas (alex.thomas5669@email.com). You want to pay off your outstanding balance of $89.19 using your credit card on 2025-09-18 because you want to clear your account arrears and avoid further late fees. After that, you would like to add a new WiFi 6 Router to your account for better home connectivity, with a preference for TechCorp devices to ensure compatibility with your existing network setup. Later, you want to understand the details of the Senior Mobile Plan and how the senior discount affects pricing, as the plan costs $45.00 monthly and reduces to $40.00 with the senior discount, which could help you save on mobile service if you switch.\n\nUse alex.thomas5669@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'alex_thomas_7404', 'amount': 89.19, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_thomas_7404'}),
            Action(name='manage_service', kwargs={'customer_id': 'alex_thomas_7404', 'action': 'list'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
            Action(name='add_device', kwargs={'customer_id': 'alex_thomas_7404', 'device_name': 'WiFi 6 Router'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kendall.nguyen7757@email.com',
        instruction='You are kendall_nguyen_8834, with email kendall.nguyen7757@email.com. You want to add the Unlimited Mobile Plan for $85.00 per month to your account because it offers better data and calling features compared to Basic Mobile Plan.\n\nUse kendall.nguyen7757@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='manage_service', kwargs={'customer_id': 'kendall_nguyen_8834', 'action': 'add', 'service_id': 'mobile_unlimited'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.martinez8921@email.com',
        instruction='You are jamie_martinez_9584, with email jamie.martinez8921@email.com. You want to add your iPhone 14 to your account because you recently acquired the device and need it registered for service. Since the device is made by Apple, you prefer to keep your devices within the Apple ecosystem for seamless integration. You would like the specifications of the iPhone 14 verified to ensure compatibility and correct service provisioning. Later, you want a support ticket created for the device registration process with medium priority, as this ensures timely handling without immediate urgency, and the ticket has been logged as TICKET241.\n\nUse jamie.martinez8921@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'jamie_martinez_9584', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'jamie_martinez_9584', 'category': 'device', 'priority': 'medium'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson2185@email.com',
        instruction='You are quinn.wilson2185@email.com. You want to update your billing preferences by enabling paperless billing and auto-pay to reduce manual effort and ensure timely payments, and you prefer switching to a quarterly billing cycle for better alignment with your financial planning. After that, you would like to remove the Basic TV Package from your account because you no longer use it. Later, you need troubleshooting for battery drain issues on your iPhone 15 Pro, which you rely on daily, and you prefer Apple devices for their ecosystem integration and user experience.\n\nUse quinn.wilson2185@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_wilson_7642', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_wilson_7642', 'action': 'remove', 'service_id': 'tv_basic'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.martinez1803@email.com',
        instruction='You are Sam Martinez (sam_martinez_3845) with email sam.martinez1803@email.com. You want to check the status of your open support ticket TICKET00131 because you are awaiting resolution on a prior issue. You would like to review your current billing details, including your $0.00 balance and monthly charges of $276.07, to ensure accuracy and maintain control over your expenses. You want to know about Fiber Internet 1GB service, and compare it to your current 500 Mbps cable plan. You prefer Apple devices and specifically use an iPhone 15 Pro, so you would like to confirm its specifications due to ongoing battery drain issues affecting your daily usage. After reviewing these details, you would like to create a new support ticket in the billing category to address a concern about recent charges, as you value clear and transparent billing communication.\n\nUse sam.martinez1803@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00131'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_martinez_3845'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_martinez_3845', 'category': 'billing'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.nguyen0038@email.com',
        instruction='You are Emerson Nguyen (emerson.nguyen0038@email.com). You want to update your billing preferences to enable paperless billing and auto-pay with your credit card, and switch to a quarterly billing cycle for better financial planning and convenience. You would also like a list of your current services, which include the Senior Mobile Plan, Cable Internet 100MB, and Premium TV Package, so you can review them. Later, you would like to add your new Samsung Galaxy S23 to your account because you recently acquired it and need it registered. Since the device is experiencing slow speeds, you would like troubleshooting assistance to improve performance. After that, you want to pay off your outstanding balance of $158.60 using your credit card to bring your account current and avoid late fees on 2025-09-18.\n\nUse emerson.nguyen0038@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'emerson_nguyen_6383', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'emerson_nguyen_6383', 'action': 'list'}),
            Action(name='add_device', kwargs={'customer_id': 'emerson_nguyen_6383', 'device_name': 'Samsung Galaxy S23'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'slow_speeds'}),
            Action(name='record_payment', kwargs={'customer_id': 'emerson_nguyen_6383', 'amount': 158.6, 'method': 'credit_card', 'date': '2025-09-18'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kendall.lee5449@email.com',
        instruction='You are kendall_lee_0640, a senior customer on the Senior Mobile Plan. You want troubleshooting for your Samsung Galaxy A54 because it is experiencing battery drain, which affects daily usability and want to create a support ticket of medium priority. You prefer Samsung devices for their familiarity and ease of use, and this model is your primary phone for communication so you want to add one more Samsung A54. Later, you would like to update your billing preferences to enable auto-pay with your credit card to avoid late fees, while keeping paperless billing and a monthly cycle for consistency and convenience. You also want to pay your outstanding balance of $119.45 as of September 18, 2025, to bring your account current. Additionally, you would like confirmation that your Senior Mobile Plan at $45.00 receives the applicable senior discount. After that, you want your new support ticket TICKET241 to be updated to status in_progress with high priority because the device issue is urgent and ongoing.\n\nUse kendall.lee5449@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy A54'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'kendall_lee_0640', 'category': 'device', 'priority': 'medium'}),
            Action(name='add_device', kwargs={'customer_id': 'kendall_lee_0640', 'device_name': 'Samsung Galaxy A54'}),
            Action(name='manage_service', kwargs={'customer_id': 'kendall_lee_0640', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_billing_details', kwargs={'customer_id': 'kendall_lee_0640'}),
            Action(name='manage_billing', kwargs={'customer_id': 'kendall_lee_0640', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='record_payment', kwargs={'customer_id': 'kendall_lee_0640', 'amount': 119.45, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET241'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET241', 'status': 'in_progress', 'priority': 'high'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='riley.patel8159@email.com',
        instruction="You are Riley Patel (riley.patel8159@email.com). You want to create a support ticket for a device issue because you're experiencing problems and need technical assistance. You would like to add your Samsung Galaxy S23 to your account because it's your preferred device and you want it connected to your service. You prefer Samsung devices, specifically the Galaxy S23 model, for their performance and integration with your existing setup. You want to list your current services—Unlimited Mobile Plan, Cable Internet 100MB, and Home Security System—to understand what you're currently using, and you would like to explore other available services to consider potential upgrades or additions. You want to review your billing details to ensure accuracy and transparency. After that, you would like to update your billing preferences to paperless billing for environmental and convenience reasons, enable auto-pay with your credit card to avoid missed payments, and set your billing cycle to monthly to align with your budgeting habits.\n\nUse riley.patel8159@email.com for authentication.",
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'riley_patel_6640', 'category': 'device'}),
            Action(name='add_device', kwargs={'customer_id': 'riley_patel_6640', 'device_name': 'Samsung Galaxy S23'}),
            Action(name='manage_service', kwargs={'customer_id': 'riley_patel_6640', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_billing_details', kwargs={'customer_id': 'riley_patel_6640'}),
            Action(name='manage_billing', kwargs={'customer_id': 'riley_patel_6640', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.lee9322@email.com',
        instruction='You are Rowan Lee (rowan_lee_8557). You want to remove the Fiber Internet 500MB internet service from your account because you are simplifying your services and no longer need home internet. After that, you would like to review your billing details and pay the current outstanding balance of $52.44 using bank transfer on 2025-09-18 to bring your account current. You also want to explore all available services to understand what options are offered. You would like to report a battery drain issue with your Apple iPhone SE (3rd gen) by creating a support ticket, as the device is losing charge too quickly during normal use. Later, you would like to update your billing preferences: you prefer paperless billing and enabling auto-pay for convenience and reliability, and you want to switch to a quarterly billing cycle to better manage your payments.\n\nUse rowan.lee9322@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'rowan_lee_8557', 'action': 'remove', 'service_id': 'internet_fiber_500mb'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_lee_8557'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_lee_8557', 'amount': 52.44, 'method': 'bank_transfer', 'date': '2025-09-18'}),
            Action(name='get_services', kwargs={}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_lee_8557', 'category': 'device', 'priority': 'medium'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'battery_drain'}),
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_lee_8557', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.brown6471@email.com',
        instruction="You are sam_brown_5625 (email: sam.brown6471@email.com). You want to review the Unlimited Mobile Plan details and apply a $5 senior discount because you qualify for the senior benefit, reducing the monthly cost from $85.00 to $80.00. You would like to see your current billing details to verify your account status. You plan to pay off your outstanding balance of $59.79 using credit card on 2025-10-10 because you want to clear past-due charges. After that, you want to create a billing support ticket for follow-up to ensure the payment is properly reflected. You would like to explore all available services to understand your options. You want to list your current services to review what you're using. You are experiencing no service on your iPhone 15, so you need troubleshooting guidance because the device isn't connecting to the network. You want to know the device details of the iPhone 15 because you're confirming it's an Apple device before adding it. You would like to add the iPhone 15 to your account. Later, you want to update your billing preferences to paperless and enable auto-pay with credit card for convenience and reliability. You prefer a quarterly billing cycle to reduce the frequency of payments and better align with your budgeting schedule.\n\nUse sam.brown6471@email.com for authentication.",
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_senior_discount', kwargs={'original_price': '85.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_brown_5625'}),
            Action(name='record_payment', kwargs={'customer_id': 'sam_brown_5625', 'amount': 59.79, 'method': 'credit_card', 'date': '2025-10-10'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_brown_5625', 'category': 'billing'}),
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'sam_brown_5625', 'action': 'list'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15', 'issue': 'no_service'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15'}),
            Action(name='add_device', kwargs={'customer_id': 'sam_brown_5625', 'device_name': 'iPhone 15'}),
            Action(name='manage_billing', kwargs={'customer_id': 'sam_brown_5625', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.white6990@email.com',
        instruction='You are reese_white_4727, with email reese.white6990@email.com. You want to review all available telecom services and plans to evaluate your options, including mobile, internet, TV, phone, and security offerings, so you can make an informed decision about potential service changes or additions.\n\nUse reese.white6990@email.com for authentication.',
        actions=[
            Action(name='get_services', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.wilson0710@email.com',
        instruction='You are Alex Wilson (alex_wilson_8557), a residential customer since 2018. You want to pay your current outstanding balance of $163.98 today, September 28, 2025, using your credit card because you prefer to keep your account in good standing. You also want to remove your Fiber Internet 1GB service because it has been consistently delivering slow speeds despite troubleshooting. Before proceeding, you requested details about the service and your WiFi 6 Router to make an informed decision. You would like troubleshooting guidance for the router because the slow speeds are affecting your home internet experience. You prefer TechCorp as the manufacturer of your networking equipment, and specifically the WiFi6-Pro model, but you are considering discontinuing it due to performance issues in future.\n\nUse alex.wilson0710@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'alex_wilson_8557', 'amount': 163.98, 'method': 'credit_card', 'date': '2025-09-28'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_wilson_8557'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'WiFi 6 Router', 'issue': 'slow_speeds'}),
            Action(name='manage_service', kwargs={'customer_id': 'alex_wilson_8557', 'action': 'remove', 'service_id': 'internet_fiber_1gb'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kendall.white6804@email.com',
        instruction='You are kendall_white_9831. You want to add an iPhone 15 Pro to your account because you prefer Apple devices for their ecosystem integration and this model supports your usage needs. You are experiencing battery drain issues with the device, so you would like troubleshooting guidance to resolve performance problems that affect daily usability. You want to review your current billing details to ensure accuracy and transparency in your monthly charges. You would like a support ticket created for the ongoing device issue so it can be formally tracked and addressed, and you prefer medium priority since the device is important but not mission-critical. You also want to manage your telecom services to optimize your plan, starting with your current Basic Mobile Plan, Cable Internet 500MB, and Basic TV Package, with the possibility of upgrading for better value or performance in future. You will not make any changes today.\n\nUse kendall.white6804@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'kendall_white_9831', 'action': 'list'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'kendall_white_9831'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'kendall_white_9831', 'category': 'device', 'priority': 'medium'}),
            Action(name='add_device', kwargs={'customer_id': 'kendall_white_9831', 'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='riley.jackson5759@email.com',
        instruction='You are Riley Jackson (riley.jackson5759@email.com). You want to verify the details of your iPhone 15 Pro because you need to confirm its specifications are correctly recorded in your account. You prefer Apple devices, and specifically the iPhone 15 Pro model, as it aligns with your current device ecosystem, so you want to add one more to your account. Later, you want troubleshooting guidance for the ongoing battery drain issue because the phone loses charge quickly during work hours, impacting productivity; the steps should include restarting the device, adjusting brightness, and closing background apps.\n\nUse riley.jackson5759@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='add_device', kwargs={'customer_id': 'riley_jackson_7148', 'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.walker5879@email.com',
        instruction='You are Emerson Walker (emerson.walker5879@email.com). You want to add your new iPhone 14 to your account for full service integration. Since the device is experiencing significant battery drain, you would like troubleshooting guidance because the battery does not last through your workday. You prefer Apple devices for their ecosystem compatibility, and specifically the iPhone 14 for its performance. After reviewing initial steps, you would like a support ticket created in the device category to formally track the issue and ensure resolution, as this phone is critical for business communications.\n\nUse emerson.walker5879@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'emerson_walker_8800', 'device_name': 'iPhone 14'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'emerson_walker_8800', 'category': 'device'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='parker.lee0757@email.com',
        instruction='You are Parker Lee (parker.lee0757@email.com). You want to understand the features and pricing of the Fiber Internet 1GB service because you are considering upgrading from your current 100 Mbps cable plan for faster and more reliable speeds. Later, you would like to escalate the priority of your open support ticket (TICKET00132) to urgent because you are experiencing ongoing internet connectivity issues that are disrupting your daily activities.\n\nUse parker.lee0757@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00132'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00132', 'status': 'open', 'priority': 'urgent'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.harris2506@email.com',
        instruction='You are reese.harris2506@email.com. You own an Apple iPhone 15 and are experiencing significant battery drain, so you want troubleshooting assistance to restore normal device performance. Since the issue persists, you would like a support ticket created for your Unlimited Mobile Plan with high priority because reliable mobile service is essential. Later, you intend to pay off your outstanding balance of $122.11 using your credit card on September 28, 2025, to avoid further late fees and maintain account standing.\n\nUse reese.harris2506@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'reese_harris_9472', 'category': 'mobile', 'priority': 'high'}),
            Action(name='record_payment', kwargs={'customer_id': 'reese_harris_9472', 'amount': 122.11, 'method': 'credit_card', 'date': '2025-09-28'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.garcia9940@email.com',
        instruction='You are elliot_garcia_0237. You want to check your billing details because you noticed an outstanding balance of $54.12 that needs to be resolved. You would like to pay off the full balance of $54.12 using your credit card on 2025-09-18 to bring your account current and avoid further late fees. After that, you would like a support ticket opened for billing concerns with medium priority because you have experienced recurring billing discrepancies and late fee charges despite timely payments. Additionally, you need troubleshooting assistance for your iPhone 15 Pro, which is experiencing battery drain issues; you prefer Apple devices and this model specifically, but the rapid battery depletion is disrupting your daily use and requires resolution.\n\nUse elliot.garcia9940@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'elliot_garcia_0237'}),
            Action(name='record_payment', kwargs={'customer_id': 'elliot_garcia_0237', 'amount': 54.12, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_garcia_0237', 'category': 'billing', 'priority': 'medium'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.clark9299@email.com',
        instruction='You are Quinn Clark (quinn.clark9299@email.com), a senior customer experiencing battery drain on your Samsung Galaxy A54, which is your primary mobile device and essential for daily communication. You want troubleshooting guidance for the battery issue because the phone does not last through the day. If troubleshooting fails, you would like a support ticket opened for the device issue to ensure resolution. You want to add one more Samsung A54 as you prefer Samsung devices, specifically the Galaxy A54, and rely on it for connectivity. Later, you would like to review all available services to understand potential upgrades or changes, followed by specific details about your current Senior Mobile Plan to confirm its benefits. You also want to update your billing preferences to switch from a monthly to a quarterly billing cycle for better alignment with your pension schedule, while keeping paperless billing and auto-pay enabled for convenience and reliability. After that, you would like a list of all services currently on your account to verify your subscriptions. You want the senior discount applied to your Senior Mobile Plan, which reduces the $45.00 monthly cost to $40.00, because you are eligible and want to ensure accurate billing. Finally, you would like to review your full billing details, including current balance, payment history, and charges, to maintain financial oversight and confirm all settings are correct. You prefer to pay by credit card and have autopay enabled for seamless service continuity.\n\nUse quinn.clark9299@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'quinn_clark_3458', 'category': 'device'}),
            Action(name='add_device', kwargs={'customer_id': 'quinn_clark_3458', 'device_name': 'Samsung Galaxy A54'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_clark_3458', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_clark_3458', 'action': 'list'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_clark_3458'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.wilson5839@email.com',
        instruction='You are elliot.wilson5839@email.com. You own an Apple iPhone 15, which is your primary mobile device, and you are experiencing no service connectivity, making the phone unusable for calls and data. Because the issue persists and affects daily communication, you want troubleshooting guidance to resolve the connectivity problem. After that, you would like a support ticket created under the device category to formally track and escalate the issue for technical investigation, ensuring a permanent fix is provided.\n\nUse elliot.wilson5839@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_wilson_6565', 'category': 'device'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15', 'issue': 'no_service'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.wilson8581@email.com',
        instruction='You are Avery Wilson (avery.wilson8581@email.com). You want to disable paperless billing and auto-pay because you prefer receiving physical bills and managing payments manually. You would like to change your billing cycle to quarterly for better alignment with your personal budgeting schedule. Additionally, you want to remove your Cable Internet 100MB service since you are switching to a new internet provider, making this service no longer necessary.\n\nUse avery.wilson8581@email.com for authentication.',
        actions=[
            Action(name='manage_billing', kwargs={'customer_id': 'avery_wilson_0002', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'avery_wilson_0002', 'action': 'remove', 'service_id': 'internet_cable_100mb'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='riley.patel8159@email.com',
        instruction='You are riley.patel8159@email.com. You want to check the status of your open support ticket TICKET00150, which is currently at medium priority, and you would like it escalated to urgent because the issue requires immediate attention. After that, you would like a new support ticket created for your iPhone SE (3rd gen) with high priority since the device is experiencing persistent battery drain that affects daily usability. You prefer Apple devices and specifically the iPhone SE model, so maintaining continuity with your preferred brand and device is important. You need troubleshooting guidance for the battery drain, which includes restarting the device, reducing screen brightness, and closing background apps, as a temporary measure while the ticket is processed. Later, you would like a full list of your current services—Unlimited Mobile Plan, Cable Internet 100MB, and Home Security System—for review to ensure all active services align with your needs.\n\nUse riley.patel8159@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00150'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00150', 'status': 'open', 'priority': 'urgent'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'riley_patel_6640', 'category': 'device', 'priority': 'high'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'riley_patel_6640', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='casey.lee1335@email.com',
        instruction='You are Casey Lee (casey.lee1335@email.com). You want to learn about the Fiber Internet 1GB service because you are upgrading from cable internet for faster and more reliable speeds. You would like to switch your billing to quarterly cycle, and you prefer to disable both paperless billing and auto-pay so you can review each bill manually and maintain control over payment timing. You want to add the Fiber Internet 1GB service to your account to benefit from gigabit speeds. You prefer Samsung devices, so you would like to add a Samsung 65" Smart TV to your account for a seamless brand-integrated home entertainment experience. Since you are experiencing slow internet speeds during the transition, you would like to create a support ticket in the internet category to resolve performance issues promptly.\n\nUse casey.lee1335@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_1gb'}),
            Action(name='manage_billing', kwargs={'customer_id': 'casey_lee_7980', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'casey_lee_7980', 'action': 'add', 'service_id': 'internet_fiber_1gb'}),
            Action(name='add_device', kwargs={'customer_id': 'casey_lee_7980', 'device_name': 'Samsung 65" Smart TV'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'casey_lee_7980', 'category': 'internet'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.white6161@email.com',
        instruction='You are Quinn White (quinn.white6161@email.com). You are experiencing battery drain on your iPhone 14, which you rely on for business communications, so you would like troubleshooting steps to resolve the issue and restore reliable daily use. The suggested steps are: restart the device, reduce screen brightness, and close background apps.\n\nUse quinn.white6161@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson2185@email.com',
        instruction='You are quinn_wilson_7642. You own an Apple iPhone 15 Pro, and you are experiencing significant battery drain that disrupts daily usage, so you would like troubleshooting assistance to resolve the issue.\n\nUse quinn.wilson2185@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.anderson8510@email.com',
        instruction='You are elliot.anderson8510@email.com. You want to remove the Premium TV Package because you no longer use it and want to reduce monthly expenses. You would like to update your billing preferences to paperless and enable auto-pay with a quarterly billing cycle for better financial planning and environmental sustainability. You want to create a support ticket for mobile service issues because you are experiencing connectivity problems. After creating the ticket, you would like to check its status and escalate the priority to high since the issue is affecting your daily communication. You want to confirm the senior discount on the Senior Mobile Plan because you qualify for reduced pricing as a senior customer. You would like to review the full details of the Senior Mobile Plan to ensure it continues to meet your needs. You are experiencing battery drain on your Samsung Galaxy A54, so you would like troubleshooting guidance because the device does not last through the day; you prefer Samsung devices for their reliability and familiarity, and this model is your primary phone for staying in touch with family.\n\nUse elliot.anderson8510@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'elliot_anderson_6407', 'action': 'remove', 'service_id': 'tv_premium'}),
            Action(name='manage_billing', kwargs={'customer_id': 'elliot_anderson_6407', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_anderson_6407', 'category': 'mobile'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'elliot_anderson_6407'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET241'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET241', 'status': 'open', 'priority': 'high'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy A54'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson5782@email.com',
        instruction='You are Quinn Wilson (quinn.wilson5782@email.com), a business customer with an outstanding balance of $152.22. You want to add a WiFi 6 Router to your account. You prefer networking equipment from TechCorp, and specifically the WiFi6-Pro model, to support high-speed connectivity. You would also like a support ticket created for ongoing slow internet speeds affecting your Standard WiFi Router, as reliable performance is critical for daily operations. After that, you want to update your billing preferences to paperless and enable auto-pay with a monthly billing cycle to streamline account management and avoid late fees. You prefer to pay by credit card and intend to apply a payment of $152.22 on October 5, 2025, to clear your current balance. Later, you would like to review the details of your newly added WiFi 6 Router to confirm its specifications. You also want troubleshooting steps for the Standard WiFi Router regarding slow speeds to attempt resolution before further escalation. Finally, you would like a list of all active services on your account, including the Fiber Internet 2GB and Business Mobile - 10 Lines plans, to verify your current service setup.\n\nUse quinn.wilson5782@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'quinn_wilson_5555', 'device_name': 'WiFi 6 Router'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'quinn_wilson_5555', 'category': 'device', 'priority': 'medium'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_wilson_5555'}),
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_wilson_5555', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='record_payment', kwargs={'customer_id': 'quinn_wilson_5555', 'amount': 152.22, 'method': 'credit_card', 'date': '2025-10-05'}),
            Action(name='get_device_details', kwargs={'device_name': 'WiFi 6 Router'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Standard WiFi Router', 'issue': 'slow_speeds'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_wilson_5555', 'action': 'list'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_2gb'}),
            Action(name='get_services', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson5782@email.com',
        instruction='You are Quinn Wilson (quinn_wilson_5555), a business customer with an existing Standard WiFi Router on your account that you want confirmed and retained. You want to remove your Fiber Internet 2GB service because you are looking to reduce costs. You are interested in the Senior Mobile Plan at $40.00 per month after the senior discount is applied to the original $45.00 price, as it offers a more budget-friendly option. You own an iPhone 15 Pro made by Apple, and it is experiencing significant battery drain, so you would like troubleshooting guidance to resolve performance issues that affect daily productivity. Since the problem persists, you want to create a new support ticket for the iPhone 15 Pro battery issue and escalate your existing ticket (TICKET00076) to high priority because it has remained unresolved at low priority. You also want to confirm the updated details of ticket TICKET00076 afterward. You would like to review the details of your mobile_business_10lines service to understand your current business plan. You prefer to update your billing preferences to paperless billing for environmental and convenience reasons, disable auto-pay to maintain manual control, and set your billing cycle to monthly for consistency. Finally, you intend to pay your current balance of $152.22 using bank transfer on 2025-10-22 to ensure timely settlement and avoid further late fees.\n\nUse quinn.wilson5782@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'Standard WiFi Router'}),
            Action(name='add_device', kwargs={'customer_id': 'quinn_wilson_5555', 'device_name': 'Standard WiFi Router'}),
            Action(name='manage_service', kwargs={'customer_id': 'quinn_wilson_5555', 'action': 'remove', 'service_id': 'internet_fiber_2gb'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_wilson_5555'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'quinn_wilson_5555', 'category': 'device', 'priority': 'medium'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00076', 'status': 'open', 'priority': 'high'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00076'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_business_10lines'}),
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_wilson_5555', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'monthly'}),
            Action(name='record_payment', kwargs={'customer_id': 'quinn_wilson_5555', 'amount': 152.22, 'method': 'bank_transfer', 'date': '2025-10-22'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.anderson0433@email.com',
        instruction="You are alex_anderson_8285, with email alex.anderson0433@email.com. You want to first review all available services because you're considering potential upgrades or changes to your current plan. You would like detailed information about your current Unlimited Mobile Plan to understand its features and value. Since your Apple iPhone 15 Pro is experiencing battery drain that disrupts daily use, you need troubleshooting guidance to resolve the issue quickly. Later, you would like to add a Standard WiFi Router to your account to improve home network coverage, as your current Enterprise Router may not be optimized for whole-home signal distribution. After that, you want to create a new support ticket for ongoing device issues with high priority because the mobile device problems are affecting your connectivity and productivity. Subsequently, you would like to update your existing ticket TICKET00012 to in_progress status with high priority because you want to ensure the issue is actively being addressed and not left pending.\n\nUse alex.anderson0433@email.com for authentication.",
        actions=[
            Action(name='get_services', kwargs={}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='add_device', kwargs={'customer_id': 'alex_anderson_8285', 'device_name': 'Standard WiFi Router'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_anderson_8285', 'category': 'device', 'priority': 'high'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00012', 'status': 'in_progress', 'priority': 'high'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='quinn.wilson5782@email.com',
        instruction='You are Quinn Wilson (quinn.wilson5782@email.com), a business customer with the mobile_business_10lines and internet_fiber_2gb services. You want to verify the specifications of your iPhone 15 Pro because you are experiencing issues with the device and need to confirm its details before proceeding. You would like to create a support ticket for the iPhone 15 Pro to report a device issue, as it is critical for your business operations. Later, you want to check the status of your existing support ticket TICKET00076, which is currently open with low priority, because you need faster resolution due to ongoing performance problems. You also want to review your billing details and see that your current balance is $152.22, with paperless billing and auto-pay disabled and a monthly billing cycle. After reviewing, you prefer to update your billing preferences to enable paperless billing and auto-pay with a quarterly billing cycle for better financial tracking and to avoid late fees, as your previous payment was marked late. Finally, you would like to make a payment of $152.22 today (2025-10-05) using your credit card to clear the outstanding balance and bring your account current.\n\nUse quinn.wilson5782@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'quinn_wilson_5555', 'category': 'device'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00076'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'quinn_wilson_5555'}),
            Action(name='manage_billing', kwargs={'customer_id': 'quinn_wilson_5555', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'quinn_wilson_5555', 'amount': 152.22, 'method': 'credit_card', 'date': '2025-10-05'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.wilson2953@email.com',
        instruction='You are reese_wilson_1963, authenticated via email reese.wilson2953@email.com. You want to add your new iPhone 14 to your account because you recently purchased it and need it activated for service. You prefer Apple devices, specifically the iPhone 14 model, for compatibility with your existing ecosystem. After adding the device, you would like to open a support ticket for assistance with device setup issues because you are experiencing difficulties during initial configuration. The ticket (TICKET241) has been created under the device category with medium priority. You also want to verify the device specifications in the system to ensure accurate registration and support eligibility.\n\nUse reese.wilson2953@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'reese_wilson_1963', 'category': 'device'}),
            Action(name='add_device', kwargs={'customer_id': 'reese_wilson_1963', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.wilson0710@email.com',
        instruction='You are Alex Wilson (alex.wilson0710@email.com). You want to open a medium-priority billing support ticket because you are experiencing discrepancies on your recent bill and need formal documentation. After that, you would like to review your billing details to understand the charges, especially the late fee and HD cable box rental. You prefer to pay the outstanding balance of $163.98 by credit card on September 18, 2025 that is today, to resolve the overdue amount and avoid further fees, and you want confirmation that your balance is now zero.\n\nUse alex.wilson0710@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_wilson_8557', 'category': 'billing', 'priority': 'medium'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'alex_wilson_8557'}),
            Action(name='record_payment', kwargs={'customer_id': 'alex_wilson_8557', 'amount': 163.98, 'method': 'credit_card', 'date': '2025-09-18'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper.wilson5381@email.com',
        instruction='You are Harper Wilson (harper_wilson_5062). You want to check the status of your open support ticket TICKET00231, which is currently open with medium priority, and review your billing details because you noticed a late payment and a current balance of $89.84. After reviewing, you would like to remove the Basic TV Package from your services because you no longer use it, and you prefer to update your billing preferences to disable auto-pay and paperless billing for greater control over payments, switching to a quarterly billing cycle to better align with your personal budgeting schedule. You prefer to make payments manually by credit card.\n\nUse harper.wilson5381@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00231'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'harper_wilson_5062'}),
            Action(name='manage_service', kwargs={'customer_id': 'harper_wilson_5062', 'action': 'remove', 'service_id': 'tv_basic'}),
            Action(name='manage_billing', kwargs={'customer_id': 'harper_wilson_5062', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.garcia4034@email.com',
        instruction='You are Alex Garcia (alex.garcia4034@email.com). You want to add an iPhone 14 to your account because you recently acquired the device. You prefer Apple devices, specifically the iPhone 14 model, for compatibility with your existing ecosystem. After adding the device, you would like troubleshooting guidance for battery drain issues because the phone loses charge quickly during daily use. You also want a full list of your current services—Unlimited Mobile Plan, Cable Internet 500MB, Premium TV Package, and Home Security System—to review your monthly charges and service lineup.\n\nUse alex.garcia4034@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'alex_garcia_1945', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'alex_garcia_1945', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.allen8122@email.com',
        instruction='You are Emerson Allen (emerson_allen_8604). You want to check the status of your open support ticket TICKET00014 because you need confirmation that your issue is being handled. After that, you would like to update your billing preferences to disable paperless billing and auto-pay, while keeping the billing cycle monthly, because you prefer receiving physical bills and want manual control over payments. You are on the Senior Mobile Plan, which originally costs $45.00, and you would like to confirm the discounted price after applying the senior discount, which is $40.00, to ensure accurate and reduced monthly charges.\n\nUse emerson.allen8122@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00014'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'emerson_allen_8604'}),
            Action(name='manage_service', kwargs={'customer_id': 'emerson_allen_8604', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='manage_billing', kwargs={'customer_id': 'emerson_allen_8604', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'monthly'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.walker8488@email.com',
        instruction="You are Rowan Walker (rowan_walker_5808), a residential customer in Phoenix, AZ. You want to review the details of your Unlimited Mobile Plan because you're evaluating your current service package. You have an open support ticket (TICKET00081) with medium priority, and you would like to escalate it to urgent priority because the issue is time-sensitive. After that, you would like to create a new support ticket for a device issue to address ongoing concerns with your new phone. You prefer Apple devices, so you recently acquired an iPhone 14 and want it added to your account. You are experiencing battery drain on the iPhone 14, so you need troubleshooting guidance because the device does not last through the day. You would like to change your billing preferences to quarterly billing with paperless billing and auto-pay disabled because you prefer manual control over your payments and receive statements digitally. You also want to review your current services, which include Unlimited Mobile Plan, Cable Internet 500 Mbps, and Premium TV, to assess potential adjustments. You inquired about the senior discount, which reduces a $45.00 plan to $40.00, possibly for a family member, even though you are not on the senior plan.\n\nUse rowan.walker8488@email.com for authentication.",
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00081'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00081', 'status': 'open', 'priority': 'urgent'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_walker_5808', 'category': 'device', 'priority': 'high'}),
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_walker_5808', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='manage_service', kwargs={'customer_id': 'rowan_walker_5808', 'action': 'list'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_walker_5808'}),
            Action(name='add_device', kwargs={'customer_id': 'rowan_walker_5808', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.lewis1592@email.com',
        instruction='You are Morgan Lewis (morgan.lewis1592@email.com). You want to remove the Fiber Internet 500MB plan from your account because you are simplifying your services. You would like to add a new mobile device to your account, preferring Samsung as the manufacturer. Specifically, you want to add a Samsung Galaxy A54 to your account for expanded device use. Your iPhone 15 Pro is experiencing battery drain, so you need troubleshooting guidance to extend battery life through basic steps like restarting the device, reducing brightness, and closing background apps. You also want to create a support ticket for the iPhone 15 Pro battery issue with medium priority since the problem persists and affects daily usability. Later, you would like to review your billing details to understand your current charges and payment history. You also want to know the discounted price of your Senior Mobile Plan, which you pay as a senior customer, and it should reflect the $5 discount bringing the monthly cost to $40.00. After that, you would like to pay off your outstanding balance of $106.76 using your credit card on October 15, 2025, to avoid late fees and maintain account in good standing.\n\nUse morgan.lewis1592@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'morgan_lewis_7010', 'action': 'remove', 'service_id': 'internet_fiber_500mb'}),
            Action(name='add_device', kwargs={'customer_id': 'morgan_lewis_7010', 'device_name': 'Samsung Galaxy A54'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'morgan_lewis_7010', 'category': 'device', 'priority': 'medium'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'morgan_lewis_7010'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='record_payment', kwargs={'customer_id': 'morgan_lewis_7010', 'amount': 106.76, 'method': 'credit_card', 'date': '2025-10-15'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.lee9322@email.com',
        instruction='You are rowan.lee9322@email.com. You are on the Senior Mobile Plan, which costs $45.00, and you want to confirm that the senior discount of $5.00 is applied, resulting in a final price of $40.00, to ensure you are receiving the correct senior benefit. You also want to review the details of your Fiber Internet 500MB service, which costs $60.00, because you are considering removing it to reduce monthly expenses. You have an outstanding balance of $52.44 that includes a $25 late fee, and you want to pay it off using bank transfer today (2025-10-26) to clear your account. You would like a support ticket created for the late fee dispute because you believe it was applied in error and want it reviewed. After payment, you would like to update your billing preferences to enable paperless billing and auto-pay with bank transfer to avoid future late fees and ensure convenience, while keeping your billing cycle monthly. You are experiencing battery drain on your iPhone SE (3rd gen), a device made by Apple, and you need troubleshooting steps because the battery does not last through the day, affecting your daily usage.\n\nUse rowan.lee9322@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'internet_fiber_500mb'}),
            Action(name='manage_service', kwargs={'customer_id': 'rowan_lee_8557', 'action': 'remove', 'service_id': 'internet_fiber_500mb'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_lee_8557', 'amount': 52.44, 'method': 'bank_transfer', 'date': '2025-10-26'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_lee_8557', 'category': 'billing', 'priority': 'medium'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_lee_8557'}),
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_lee_8557', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone SE (3rd gen)'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.anderson3172@email.com',
        instruction='You are sam.anderson3172@email.com. You want to troubleshoot the iPhone 15 Pro because it is experiencing battery drain issues that affect daily usability. You would like to review your current services, which include the Unlimited Mobile Plan and Cable Internet 500MB, to understand your account setup. You also want to check your billing details for accuracy. Later, you would like to update your billing preferences by disabling paperless billing and auto-pay to gain more control over your statements and payments, and switch to a quarterly billing cycle for better budget alignment. Subsequently, you want to create a high-priority support ticket for the ongoing device issues because the problem persists and requires urgent attention. Finally, you would like to add a new mobile device to your account, preferring Samsung as the manufacturer, specifically the Galaxy S23, and confirm its specifications are correctly recorded in the system.\n\nUse sam.anderson3172@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'sam_anderson_2306', 'action': 'list'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_anderson_2306'}),
            Action(name='manage_billing', kwargs={'customer_id': 'sam_anderson_2306', 'paperless': False, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_anderson_2306', 'category': 'device', 'priority': 'high'}),
            Action(name='add_device', kwargs={'customer_id': 'sam_anderson_2306', 'device_name': 'Samsung Galaxy S23'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy S23'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.martinez0944@email.com',
        instruction='You are Avery Martinez (avery.martinez0944@email.com). You are on the Senior Mobile Plan, which normally costs $45.00 per month, and you want to apply the senior discount because it reduces your monthly cost to $40.00, providing a more affordable rate for your mobile service. You would like to know more about the Senior Mobile Plan because it is tailored for seniors with simplified features and pricing. You prefer Samsung devices, so you would like to add a Samsung Galaxy S23 to your account because it is a reliable, up-to-date smartphone that meets your usage needs. After adding the device, you want to review your billing situation because you have ongoing concerns about payment processing. You create a billing support ticket with medium priority because you want ongoing issues to be tracked and addressed. You review your billing details to verify your charges and payment history. Later, you update your billing preferences by disabling auto-pay because you prefer manual control over payments, while keeping paperless billing enabled for convenience and maintaining the monthly billing cycle for consistency.\n\nUse avery.martinez0944@email.com for authentication.',
        actions=[
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy S23'}),
            Action(name='add_device', kwargs={'customer_id': 'avery_martinez_8709', 'device_name': 'Samsung Galaxy S23'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'avery_martinez_8709', 'category': 'billing', 'priority': 'medium'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'avery_martinez_8709'}),
            Action(name='manage_billing', kwargs={'customer_id': 'avery_martinez_8709', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'monthly'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.clark7888@email.com',
        instruction='You are reese.clark7888@email.com. You want to check the status of your support ticket TICKET00024. You would like to review your current billing information, including your balance of $31.62 and monthly charges, because you noticed a late payment of $74.32 was applied and you want to understand any potential fees or impacts related to the ongoing support issue.\n\nUse reese.clark7888@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00024'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_clark_1767'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.martinez1803@email.com',
        instruction="You are sam_martinez_3845. You want to check the status of your open support ticket TICKET00131, which is currently open with medium priority, because you need an update on an ongoing issue. After that, you would like to create a new support ticket for a billing inquiry because you have questions about your charges, and you prefer this ticket to be tracked separately. Later, you want to escalate the priority of your existing ticket TICKET00131 from medium to high due to increased urgency, as the issue is now impacting your ability to use essential services.\n\nUse sam.martinez1803@email.com for authentication.",
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00131'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_martinez_3845'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_martinez_3845', 'category': 'billing', 'priority': 'medium'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00131', 'status': 'open', 'priority': 'high'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kendall.lee2343@email.com',
        instruction='You are kendall_lee_9814, customer email kendall.lee2343@email.com. You want to make a payment of $72.36 on 2025-09-18 using your credit card because you have an outstanding balance that needs to be cleared. After that, you would like to review your updated billing details to confirm the payment was applied successfully. You also want to create a new support ticket for a billing inquiry with high priority because the issue requires prompt attention. Later, you would like to update the existing ticket TICKET00163 to urgent priority and mark it as in_progress to reflect its current status and ensure it receives immediate handling. Finally, you would like to retrieve the latest details of ticket TICKET00163 to verify that the changes were made correctly.\n\nUse kendall.lee2343@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'kendall_lee_9814', 'amount': 72.36, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'kendall_lee_9814'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'kendall_lee_9814', 'category': 'billing', 'priority': 'high'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00163', 'status': 'in_progress', 'priority': 'urgent'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00163'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.garcia2286@email.com',
        instruction='You are Rowan Garcia (rowan.garcia2286@email.com). You want to add your Samsung Galaxy A54 to your account because it is a device you are actively using. You would like to review the details of the Family Plan - 4 Lines service to understand your current mobile offering. You are interested in the senior discount on a $45.00 plan, which would reduce the cost by $5, because you are evaluating affordability for supplementary services. Later, you intend to pay off your outstanding balance of $56.19 using bank transfer on 2025-10-18 to bring your account current. You would like troubleshooting assistance for slow speeds on your Samsung Galaxy A54 because the device is experiencing performance issues that affect usability. You prefer Samsung devices, specifically the Galaxy A54 model, for your mobile needs. You want to create a new high-priority support ticket for the slow speeds issue because it is impacting your daily connectivity. After that, you would like to check the status of your existing ticket TICKET00183, and update it to urgent priority to ensure the issue receives immediate attention and closure.\n\nUse rowan.garcia2286@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'rowan_garcia_8718', 'device_name': 'Samsung Galaxy A54'}),
            Action(name='manage_service', kwargs={'customer_id': 'rowan_garcia_8718', 'action': 'list'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_family_4lines'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_garcia_8718', 'amount': 56.19, 'method': 'bank_transfer', 'date': '2025-10-18'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_garcia_8718'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_garcia_8718', 'category': 'device', 'priority': 'high'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'slow_speeds'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy A54'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00183'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00183', 'status': 'open', 'priority': 'urgent'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='morgan.garcia6112@email.com',
        instruction='You are morgan_garcia_8324, customer email morgan.garcia6112@email.com. You want to remove the Premium TV Package from your services because you no longer use it. You would like to add your Samsung Galaxy A54 to your account, as it is your preferred device. You prefer Samsung phones for their reliability and ease of use. You need troubleshooting for battery drain issues on the device because it does not last through the day. You want to create a support ticket for your TV service to report ongoing issues. You are on the Senior Mobile Plan and want to understand your senior discount, which reduces your monthly mobile charge from $45.00 to $40.00. You would like to update your billing preferences to disable paperless billing, enable auto-pay with credit card, and switch to quarterly billing for better payment management. After that, you intend to make a payment of $188.40 today (2025-09-28) using your credit card to clear your outstanding balance.\n\nUse morgan.garcia6112@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'morgan_garcia_8324', 'action': 'remove', 'service_id': 'tv_premium'}),
            Action(name='add_device', kwargs={'customer_id': 'morgan_garcia_8324', 'device_name': 'Samsung Galaxy A54'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy A54'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy A54', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'morgan_garcia_8324', 'category': 'tv'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'morgan_garcia_8324'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_senior'}),
            Action(name='manage_billing', kwargs={'customer_id': 'morgan_garcia_8324', 'paperless': False, 'auto_pay': True, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'morgan_garcia_8324', 'amount': 188.4, 'method': 'credit_card', 'date': '2025-09-28'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.brown9335@email.com',
        instruction='You are rowan_brown_8285, email rowan.brown9335@email.com. You want to remove the Fiber Internet 500MB plan because you are downsizing your services. You would like to add a Samsung 65" Smart TV to your account for enhanced home entertainment. You prefer Samsung devices, specifically the Galaxy S23, but are experiencing battery drain issues, so you want troubleshooting guidance to extend device usability. You would like a high-priority support ticket created for your mobile service due to ongoing connectivity concerns. You want to review your current billing details to understand your charges and payment history. You are eligible for the senior discount, so you would like to know that a $45.00 plan would cost $40.00 with the discount applied. You are interested in the Unlimited Mobile Plan and would like its details for comparison. You prefer to update your billing preferences to paperless billing and enable auto-pay with a monthly billing cycle for better control and convenience. You would like to make a payment of $22.04 today, September 25, 2025, using your credit card to clear your current balance.\n\nUse rowan.brown9335@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'rowan_brown_8285', 'action': 'remove', 'service_id': 'internet_fiber_500mb'}),
            Action(name='add_device', kwargs={'customer_id': 'rowan_brown_8285', 'device_name': 'Samsung 65" Smart TV'}),
            Action(name='get_device_details', kwargs={'device_name': 'Samsung Galaxy S23'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'battery_drain'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_brown_8285', 'category': 'mobile', 'priority': 'high'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_brown_8285'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='manage_billing', kwargs={'customer_id': 'rowan_brown_8285', 'paperless': True, 'auto_pay': True, 'billing_cycle': 'monthly'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_brown_8285', 'amount': 22.04, 'method': 'credit_card', 'date': '2025-09-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.anderson8524@email.com',
        instruction='You are elliot_anderson_3546, and your Apple iPhone SE (3rd gen) is experiencing persistent no-service connectivity issues, so you want troubleshooting assistance to restore reliable mobile access. Since the device is essential for daily communication and the issue has been ongoing, you would like a high-priority support ticket created for this device issue to ensure prompt investigation and resolution.\n\nUse elliot.anderson8524@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_anderson_3546', 'category': 'device', 'priority': 'high'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'no_service'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='parker.jackson7798@email.com',
        instruction='You are parker_jackson_1593, with email parker.jackson7798@email.com. You want to remove your Fiber Internet 1GB service because you are moving to a new location. Before cancellation, you would like a support ticket created in the internet category to document ongoing connectivity issues so the technical team can troubleshoot the problem.\n\nUse parker.jackson7798@email.com for authentication.',
        actions=[
            Action(name='manage_service', kwargs={'customer_id': 'parker_jackson_1593', 'action': 'remove', 'service_id': 'internet_fiber_1gb'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'parker_jackson_1593', 'category': 'internet'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kendall.garcia9053@email.com',
        instruction='You are kendall.garcia9053@email.com. You want to pay off your current outstanding balance of $33.09 using your credit card because you prefer to keep your account in good standing. After that, you would like to know the price of the Senior Mobile Plan with the senior discount applied, which is $40.00 per month, because you are evaluating a potential plan change to better suit your needs and budget as a senior customer.\n\nUse kendall.garcia9053@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'kendall_garcia_2616'}),
            Action(name='record_payment', kwargs={'customer_id': 'kendall_garcia_2616', 'amount': 33.09, 'method': 'credit_card', 'date': '2025-10-25'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.clark7888@email.com',
        instruction='You are reese.clark7888@email.com. You want to review your billing details and pay your current balance of $31.62 with your credit card because you prefer to keep your account in good standing and avoid late fees. After that, you would like to know the discounted price for the senior mobile plan, which is $40.00 after applying the $5 senior discount from the original $45.00 rate, because you are interested in cost-saving options that match your eligibility.\n\nUse reese.clark7888@email.com for authentication.',
        actions=[
            Action(name='get_billing_details', kwargs={'customer_id': 'reese_clark_1767'}),
            Action(name='record_payment', kwargs={'customer_id': 'reese_clark_1767', 'amount': 31.62, 'method': 'credit_card', 'date': '2025-09-18'}),
            Action(name='get_services', kwargs={}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.garcia2286@email.com',
        instruction='You are Rowan Garcia (rowan.garcia2286@email.com). You own an Apple iPhone 13 that is experiencing battery drain, so you would like troubleshooting guidance to resolve the issue quickly. You want to create a new support ticket for the iPhone 13 with high priority because the device is essential for daily communication. Later, you would like to escalate your existing ticket (TICKET00183) to urgent priority and in_progress status because it has been delayed and requires immediate attention. After that, you would like to pay off your outstanding balance of $56.19 using a credit card on September 20, 2025, to avoid further late fees and ensure your account remains in good standing.\n\nUse rowan.garcia2286@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 13', 'issue': 'battery_drain'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 13'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_garcia_8718', 'category': 'device', 'priority': 'high'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00183', 'status': 'in_progress', 'priority': 'urgent'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00183'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_garcia_8718'}),
            Action(name='record_payment', kwargs={'customer_id': 'rowan_garcia_8718', 'amount': 56.19, 'method': 'credit_card', 'date': '2025-09-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emerson.walker5879@email.com',
        instruction='You are emerson_walker_8800, customer emerson.walker5879@email.com. You want to pay off your outstanding balance of $103.75 using your credit card on 2025-10-15 because you prefer to clear your balance proactively despite being on auto-pay with invoice billing. After that, you would like to create a support ticket for your billing issue with medium priority since your last payment was marked as late and you want to resolve any discrepancies. You also inquired about the Unlimited Mobile Plan to evaluate a potential change from your current business plan, and you are interested in the senior discount, which would reduce a $45.00 plan to $40.00, as you are age-eligible and seeking cost-effective options. You prefer Apple devices, specifically the iPhone 15 Pro, because it aligns with your current device ecosystem, but you are experiencing battery drain issues with it, so you would like troubleshooting guidance to maintain productivity. You also want to list all services on your account to review your current business services: Unlimited Business Mobile (10 lines), 2 Gbps Fiber Internet, and Business Phone System.\n\nUse emerson.walker5879@email.com for authentication.',
        actions=[
            Action(name='record_payment', kwargs={'customer_id': 'emerson_walker_8800', 'amount': 103.75, 'method': 'credit_card', 'date': '2025-10-15'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'emerson_walker_8800', 'category': 'billing', 'priority': 'medium'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET00076', 'status': 'in_progress', 'priority': 'high'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_senior_discount', kwargs={'original_price': '45.00'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'emerson_walker_8800'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
            Action(name='manage_service', kwargs={'customer_id': 'emerson_walker_8800', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elliot.anderson8524@email.com',
        instruction="You are elliot.anderson8524@email.com. You own an iPhone SE (3rd gen), an Apple device, and are experiencing no service on it, which disrupts your ability to stay connected. You would like troubleshooting assistance for the no service issue because basic steps haven't resolved the problem. Additionally, you want a support ticket created to formally investigate the device connectivity issue, so the problem can be tracked and resolved with technical support.\n\nUse elliot.anderson8524@email.com for authentication.",
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone SE (3rd gen)'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'no_service'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'elliot_anderson_3546', 'category': 'device'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.thomas9611@email.com',
        instruction='You are alex_thomas_0806, and your email is alex.thomas9611@email.com. You want troubleshooting for your iPhone SE (3rd gen) because it has no service despite being an Apple device known for reliable connectivity. After attempting troubleshooting steps, you would like a support ticket created under the device category since the issue persists and requires further technical investigation. You prefer the ticket to be assigned medium priority as the device is important for daily communication but not currently impacting other services.\n\nUse alex.thomas9611@email.com for authentication.',
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone SE (3rd gen)'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone SE (3rd gen)', 'issue': 'no_service'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_thomas_0806', 'category': 'device'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.jackson1136@email.com',
        instruction='You are avery_jackson_3269, and your Samsung Galaxy S23 is experiencing slow speeds, so you would like troubleshooting because the device is not performing reliably on your current internet connection, but you will not escalate it. You prefer Samsung devices for their reliability and familiarity, and the Galaxy S23 is your primary phone for daily use. You also want a full list of your current services—Unlimited Mobile Plan, Cable Internet 500 Mbps, and Basic TV Package—because you are reviewing your account for potential changes. Later, you would like detailed information about the Unlimited Mobile Plan, including its $85.00 monthly cost and features, because you want to confirm it still meets your usage needs.\n\nUse avery.jackson1136@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'slow_speeds'}),
            Action(name='manage_service', kwargs={'customer_id': 'avery_jackson_3269', 'action': 'list'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.jackson9868@email.com',
        instruction="You are sam_jackson_0641, and your email is sam.jackson9868@email.com. You own an iPhone 13, a mobile phone made by Apple, which is currently experiencing no service. You want troubleshooting steps for the no service issue because the device is not connecting to the network despite being functional otherwise. After that, you would like a support ticket created under the 'device' category to formally escalate the issue and ensure it is tracked by technical support. You prefer the ticket to be assigned medium priority since the issue affects daily communication but does not involve a complete device failure.\n\nUse sam.jackson9868@email.com for authentication.",
        actions=[
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 13'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_jackson_0641', 'category': 'device'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 13', 'issue': 'no_service'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='alex.nguyen7479@email.com',
        instruction="You are alex_nguyen_5938. You want to know the details of the Unlimited Mobile Plan because you are considering your service options, and you would like a list of your current services to understand what you're currently subscribed to. You are experiencing no_service issues with your iPhone 14, which is an Apple device you rely on daily, so you need troubleshooting guidance to restore connectivity. Since the issue persists, you would like a support ticket created in the device category with high priority to ensure prompt resolution, as reliable mobile service is critical for your business operations.\n\nUse alex.nguyen7479@email.com for authentication.",
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='get_services', kwargs={}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'alex_nguyen_5938', 'category': 'device', 'priority': 'high'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'no_service'}),
            Action(name='manage_service', kwargs={'customer_id': 'alex_nguyen_5938', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sam.patel3366@email.com',
        instruction='You are Sam Patel (sam.patel3366@email.com). You want to create a high-priority billing support ticket and later, you would like to escalate it to urgent priority because the issue requires immediate attention. After that, you would like to review your current services — Family Plan - 4 Lines, Cable Internet 100MB, and Premium TV Package — and explore other available service options to ensure you have the best fit. You prefer to update your billing preferences to quarterly billing with paperless statements and no auto-pay for better control over payments. You plan to make a payment of $336.40 using your credit card on 2025-10-01 to maintain account balance. You prefer Apple devices and specifically want to add your new iPhone 15 Pro to your account because it is your primary phone. Since the device is experiencing battery drain issues that affect daily usability, you would like troubleshooting guidance to resolve the problem quickly.\n\nUse sam.patel3366@email.com for authentication.',
        actions=[
            Action(name='create_support_ticket', kwargs={'customer_id': 'sam_patel_9254', 'category': 'billing', 'priority': 'high'}),
            Action(name='modify_support_ticket', kwargs={'ticket_id': 'TICKET241', 'status': 'in_progress', 'priority': 'urgent'}),
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET241'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'sam_patel_9254'}),
            Action(name='get_services', kwargs={}),
            Action(name='manage_service', kwargs={'customer_id': 'sam_patel_9254', 'action': 'list'}),
            Action(name='manage_billing', kwargs={'customer_id': 'sam_patel_9254', 'paperless': True, 'auto_pay': False, 'billing_cycle': 'quarterly'}),
            Action(name='record_payment', kwargs={'customer_id': 'sam_patel_9254', 'amount': 336.4, 'method': 'credit_card', 'date': '2025-10-01'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='add_device', kwargs={'customer_id': 'sam_patel_9254', 'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rowan.allen2136@email.com',
        instruction='You are rowan.allen2136@email.com. You want to check the status of your open support ticket TICKET00069, which is currently open with low priority, because you are following up on an ongoing issue. You also want to review your billing details, including your current $0.00 balance and next bill date of 2025-10-28, and list all services on your account—Unlimited Mobile Plan, Fiber Internet 1GB, Basic TV Package, and Home Security System—because you are verifying your account activity. Later, you would like to address a new issue with your iPhone 15 Pro, which is experiencing no service despite being an Apple device known for reliable connectivity, so you prefer troubleshooting steps such as restarting the device and resetting network settings. After that, you would like a new support ticket (TICKET241) created under the device category because the issue persists after basic fixes.\n\nUse rowan.allen2136@email.com for authentication.',
        actions=[
            Action(name='get_support_ticket_details', kwargs={'ticket_id': 'TICKET00069'}),
            Action(name='get_billing_details', kwargs={'customer_id': 'rowan_allen_6535'}),
            Action(name='manage_service', kwargs={'customer_id': 'rowan_allen_6535', 'action': 'list'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 15 Pro'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 15 Pro', 'issue': 'no_service'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'rowan_allen_6535', 'category': 'device'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='drew.lee7641@email.com',
        instruction='You are Drew Lee (drew.lee7641@email.com). You want to add your iPhone 14 to your account because you recently acquired it and expect it to be active on your mobile service. After that, you would like to review the details of the Unlimited Mobile Plan to understand its features and pricing, as you are considering switching to it for better value. Subsequently, you want to create a support ticket in the mobile category to report ongoing connectivity issues. Your iPhone 14 is currently experiencing no service, which disrupts your daily communication, so you prefer troubleshooting guidance to resolve the issue quickly. Finally, you would like a list of your current services to better understand your account setup and ensure all devices are properly linked. You prefer Apple devices, specifically the iPhone 14, for their ecosystem compatibility and user experience.\n\nUse drew.lee7641@email.com for authentication.',
        actions=[
            Action(name='add_device', kwargs={'customer_id': 'drew_lee_3775', 'device_name': 'iPhone 14'}),
            Action(name='get_device_details', kwargs={'device_name': 'iPhone 14'}),
            Action(name='get_service_details', kwargs={'service_id': 'mobile_unlimited'}),
            Action(name='create_support_ticket', kwargs={'customer_id': 'drew_lee_3775', 'category': 'mobile'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'iPhone 14', 'issue': 'no_service'}),
            Action(name='manage_service', kwargs={'customer_id': 'drew_lee_3775', 'action': 'list'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='casey.jackson8903@email.com',
        instruction='You are Casey Jackson (casey.jackson8903@email.com), a residential customer in Chicago. You want to know the details of your Cable Internet 500MB service because you are experiencing slow speeds and want to verify your current plan. You also want troubleshooting steps for your WiFi 6 Router, which is the primary networking device for your home and is currently underperforming. You prefer TechCorp as the manufacturer for your networking equipment, and you would like guidance on restarting the router, checking connections, and running a speed test to resolve the issue promptly.\n\nUse casey.jackson8903@email.com for authentication.',
        actions=[
            Action(name='get_service_details', kwargs={'service_id': 'internet_cable_500mb'}),
            Action(name='troubleshoot_device', kwargs={'device_name': 'WiFi 6 Router', 'issue': 'slow_speeds'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.jackson1136@email.com',
        instruction='You are avery_jackson_3269 (avery.jackson1136@email.com). You are experiencing slow internet speeds on your Samsung Galaxy S23, which is affecting your mobile usage, so you would like troubleshooting support to identify and resolve the performance issue.\n\nUse avery.jackson1136@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'slow_speeds'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='reese.young7173@email.com',
        instruction='You are reese_young_3890. You are experiencing rapid battery drain on your Samsung Galaxy S23 smartphone, which is affecting daily usability. You would like troubleshooting assistance to resolve the issue because basic functionality is being disrupted. Since Samsung devices are your preferred brand for mobile phones, you expect support tailored to this model. You want steps to address the battery drain, including restarting the device, reducing screen brightness, and closing background apps.\n\nUse reese.young7173@email.com for authentication.',
        actions=[
            Action(name='troubleshoot_device', kwargs={'device_name': 'Samsung Galaxy S23', 'issue': 'battery_drain'}),
        ],
        outputs=[],
    ),
]
