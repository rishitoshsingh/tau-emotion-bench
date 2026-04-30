from tau_emotion_bench.types import Task, Action


TASKS = [
    Task(
        user_id='noah_nguyen_6566',
        instruction='You are Noah Nguyen, user ID noah_nguyen_6566, and you hold reservation M9OL3W for a round-trip economy journey from DTW to SEA with return via JFK. You want to cancel the entire reservation due to a change in plans. You also want to update the passenger list by removing Sophia Lopez and adding Juan Ito, as the traveler composition has changed. Additionally, you want to rebook the outbound portion of your trip on the same date, 2024-05-19, with a morning flight from DTW to PHX (HAT097) followed by a late evening connecting flight from PHX to SEA (HAT045), both in economy class. You prefer these specific flights to better align with your revised schedule. You would like any fare difference to be charged to your credit card ending in 7345, which is already on file.\n\nUse noah_nguyen_6566 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'M9OL3W'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'M9OL3W'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'M9OL3W', 'passengers': [{'first_name': 'Noah', 'last_name': 'Nguyen', 'dob': '1968-03-04'}, {'first_name': 'Raj', 'last_name': 'Sanchez', 'dob': '1977-10-03'}, {'first_name': 'Juan', 'last_name': 'Ito', 'dob': '1998-10-21'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'M9OL3W', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT097', 'date': '2024-05-19'}, {'flight_number': 'HAT045', 'date': '2024-05-19'}, {'flight_number': 'HAT276', 'date': '2024-05-23'}, {'flight_number': 'HAT212', 'date': '2024-05-24'}], 'payment_id': 'credit_card_5771887'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_lopez_2532',
        instruction="You are to first cancel the existing reservation FPJKQM for a business-class one-way trip from PHX to LAX on 2024-05-20, as the traveler's plans have changed. Then, you want to book a new one-way economy flight from PHX to LAS on 2024-05-16 for two passengers: Noah Lopez and Evelyn Lee, because they need to travel earlier to LAS. You prefer the morning flight, specifically around 09:00 AM, as it is the only available option on that date and aligns with typical early travel plans. After booking, you would like to add one checked bag to the reservation, setting total_baggages and nonfree_baggages both to 1, because luggage is needed for the trip. You prefer to use the credit card ending in 5999 for both the new booking and the baggage fee, as it is the card on file and the user's preferred payment method.\n\nUse noah_lopez_2532 for authentication.",
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'FPJKQM'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_lopez_2532', 'origin': 'PHX', 'destination': 'LAS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT173', 'date': '2024-05-16'}], 'passengers': [{'first_name': 'Noah', 'last_name': 'Lopez', 'dob': '1954-09-07'}, {'first_name': 'Evelyn', 'last_name': 'Lee', 'dob': '1950-04-04'}], 'payment_methods': [{'payment_id': 'credit_card_3623927', 'amount': 332}, {'payment_id': 'credit_card_3623927', 'amount': 50}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'HATHAT', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3623927'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_rossi_1651',
        instruction='You are assisting Amelia Rossi (user_id: amelia_rossi_1651) with two travel requests. First, you want to book a new one-way flight from JFK to IAH on 2024-05-20 in economy class for two passengers: Raj Johnson (DOB 1973-08-10) and Sofia Davis (DOB 1982-12-27), preferring flight HAT279 which departs in the late morning (around 11:00 AM), because it is the only available economy flight on that date matching the requested route and time. You prefer to pay using the credit card ending in 7564 (payment_id credit_card_4240750). Later, you would like to update the passenger names on existing reservation MZLGZ8, which is a round-trip from JFK to IAH with a return to JFK, by changing the passengers from Noah Ahmed and Yusuf Smith to Raj Johnson and Sofia Davis, ensuring their correct dates of birth are reflected, while keeping the passenger count at two, so the reservation aligns with the updated travelers.\n\nUse amelia_rossi_1651 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'amelia_rossi_1651', 'origin': 'JFK', 'destination': 'IAH', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT279', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Raj', 'last_name': 'Johnson', 'dob': '1973-08-10'}, {'first_name': 'Sofia', 'last_name': 'Davis', 'dob': '1982-12-27'}], 'payment_methods': [{'payment_id': 'credit_card_4240750', 'amount': 330}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'MZLGZ8', 'passengers': [{'first_name': 'Raj', 'last_name': 'Johnson', 'dob': '1973-08-10'}, {'first_name': 'Sofia', 'last_name': 'Davis', 'dob': '1982-12-27'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_jackson_9549',
        instruction='You are Daiki Jackson (user_id: daiki_jackson_9549) and you want to explore flight options from San Francisco (SFO) to Houston (IAH) on 2024-05-20 for yourself and your saved passengers (Aarav Thomas and Amelia Martin). You would like to compare both direct and one-stop flight options to evaluate schedules and prices. However, only direct flights are available on this route and date. You prefer two direct flight options: one in the afternoon around 16:00 and one in the late evening around 23:00, both on 2024-05-20. You want to see pricing and seat availability in economy and business class for these flights, as you are considering comfort and cost. You prefer to use your Mastercard ending in 2563 for any booking, if needed.\n\nUse daiki_jackson_9549 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'IAH', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_ito_2309',
        instruction='You are assisting Harper Ito (harper_ito_2309) in searching for flight options from DTW to MIA on 2024-05-20. You want to first check for direct flights, but since none are available, you would like to explore one-stop itineraries. You prefer a connecting flight from DTW to MIA on 2024-05-20 with a connection via JFK, departing DTW in the early morning and arriving in MIA by evening, as this is the only viable option that reaches the destination on the requested date.\n\nUse harper_ito_2309 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'DTW', 'destination': 'MIA', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'MIA', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei_anderson_2319',
        instruction='You are Lei Anderson, and you want to book a one-way flight from Atlanta to Chicago on 2024-05-20 in the morning for three passengers, including Mason Johansson, in economy class, because you have planned a new trip. You prefer to pay using your Visa card ending in 5481. Later, you would like to upgrade your existing round-trip reservation from New York (JFK) to Newark (EWR) via Miami and Houston on 2024-05-16 and 2024-05-26 from economy to business class for both legs of the journey, for a more comfortable experience, and you prefer to use the same Visa card ending in 5481 for any fare difference. After that, you would like to cancel your other round-trip reservation from Atlanta to Houston on 2024-05-28 and returning on 2024-05-29, and receive a refund to your Visa card ending in 5481, as you are finalizing your travel plans.\n\nUse lei_anderson_2319 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'lei_anderson_2319', 'origin': 'ATL', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT227', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lei', 'last_name': 'Anderson', 'dob': '1990-09-11'}, {'first_name': 'Noah', 'last_name': 'Johnson', 'dob': '1985-04-18'}, {'first_name': 'Mason', 'last_name': 'Johansson', 'dob': '1993-07-13'}], 'payment_methods': [{'payment_id': 'credit_card_4526808', 'amount': 315}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'OK5IEN'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'OK5IEN', 'cabin': 'business', 'flights': [{'flight_number': 'HAT014', 'date': '2024-05-16'}, {'flight_number': 'HAT192', 'date': '2024-05-16'}, {'flight_number': 'HAT166', 'date': '2024-05-26'}, {'flight_number': 'HAT068', 'date': '2024-05-26'}], 'payment_id': 'credit_card_4526808'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'OK5IEN', 'passengers': [{'first_name': 'Lei', 'last_name': 'Anderson', 'dob': '1990-09-11'}, {'first_name': 'Olivia', 'last_name': 'Li', 'dob': '1972-03-12'}]}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'KFSKBR'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava_lopez_9068',
        instruction='You are assisting Ava Lopez (user_id: ava_lopez_9068) with multiple travel requests. First, you want to book a one-way one-stop flight from PHX to SFO on 2024-05-20 for passenger Lei Johansson (DOB: 1986-06-10), consisting of HAT156 from PHX to SEA departing at 07:00 AM and HAT258 from SEA to SFO departing at 5:00 PM, both in economy class, with one total baggage (no non-free baggage) and no insurance. You prefer to charge this booking to the credit card ending in 8178. Second, you want to update the passenger name on existing reservation 7ABORJ from Ava Lopez to Lei Johansson (DOB: 1986-06-10), as the trip is now for Lei instead of Ava. Third, you want to check for any direct flights from ATL to EWR on 2024-05-22 to evaluate options, with the intent to cancel the current connecting reservation (7ABORJ) if a suitable direct flight is available; however, no direct flights were found, so the current connecting itinerary remains under review for cancellation.\n\nUse ava_lopez_9068 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'PHX', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ava_lopez_9068', 'origin': 'PHX', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT156', 'date': '2024-05-20'}, {'flight_number': 'HAT258', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lei', 'last_name': 'Johansson', 'dob': '1986-06-10'}], 'payment_methods': [{'payment_id': 'credit_card_3688120', 'amount': 293}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '7ABORJ', 'passengers': [{'first_name': 'Lei', 'last_name': 'Johansson', 'dob': '1986-06-10'}]}),
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'EWR', 'date': '2024-05-22'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'VE1ZC3'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'VE1ZC3'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_kovacs_8102',
        instruction='You are Raj Kovacs, and you want to book a one-stop economy flight from Philadelphia to Boston on May 20, 2024, for yourself and Mason Sanchez, with the first leg from PHL to CLT (flight HAT243) departing around midnight and the second leg from CLT to BOS (flight HAT287) departing in the morning, because these flights are available and match your requested routing. You prefer to pay using your Mastercard ending in 5274. You also want to update your existing reservation I4ZX6J by replacing passenger Amelia Wilson with Emma Kovacs, as she is no longer traveling. Later, you would like to explore direct flight options from Philadelphia to Boston on May 20, 2024, to assess faster alternatives, but none are currently offered by the airline. After that, you would like to cancel your business class one-way reservation O8IHB3 for a flight from Philadelphia to San Francisco on May 26, 2024, because you no longer need the trip.\n\nUse raj_kovacs_8102 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'PHL', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'raj_kovacs_8102', 'origin': 'PHL', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT243', 'date': '2024-05-20'}, {'flight_number': 'HAT287', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Raj', 'last_name': 'Kovacs', 'dob': '1981-05-20'}, {'first_name': 'Mason', 'last_name': 'Sanchez', 'dob': '1976-05-16'}], 'payment_methods': [{'payment_id': 'credit_card_7320675', 'amount': 754}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'I4ZX6J', 'passengers': [{'first_name': 'Raj', 'last_name': 'Kovacs', 'dob': '1981-05-20'}, {'first_name': 'Emma', 'last_name': 'Kovacs', 'dob': '1999-01-12'}, {'first_name': 'Noah', 'last_name': 'Wilson', 'dob': '1997-07-28'}]}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHL', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'O8IHB3'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'O8IHB3'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia_ahmed_9069',
        instruction='You are Sofia Ahmed, and you want to cancel your existing one-way reservation L2TMRS from JFK to EWR via IAH on 2024-05-26 in economy class because you have changed your travel plans. You would like to book a new one-way direct flight from JFK to SFO on 2024-05-20 for yourself and Omar Patel, preferring an afternoon flight (flight HAT023, departing around 14:00) in economy class, with 2 total checked bags included and no travel insurance, because you want a more convenient direct route. You prefer to pay using your credit card ending in 9744 for this new booking. Later, you want to review the details of your other reservation RGWRKS, which is a round-trip from SEA to LGA with connections on 2024-05-26 and 2024-05-28 for three passengers (Sofia Ahmed, Emma Li, and Omar Patel), and you would like to explore direct flight options from SEA to LGA on 2024-05-26; however, you should be informed that no direct flights are currently available on that route and date.\n\nUse sofia_ahmed_9069 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'L2TMRS'}),
            Action(name='book_reservation', kwargs={'user_id': 'sofia_ahmed_9069', 'origin': 'JFK', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Sofia', 'last_name': 'Ahmed', 'dob': '1970-07-20'}, {'first_name': 'Omar', 'last_name': 'Patel', 'dob': '1993-11-05'}], 'payment_methods': [{'payment_id': 'credit_card_1236431', 'amount': 382}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RGWRKS'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SEA', 'destination': 'LGA', 'date': '2024-05-26'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_li_2415',
        instruction='You are to cancel the existing one-way business class reservation NUCNX0 from IAH to PHL on 2024-05-16 for Amelia Li, Lucas Kim, and Amelia Santos, as the trip is no longer needed. Later, you would like to book a new one-way economy flight from IAH to JFK on 2024-05-20 for the same three passengers, preferring the early morning flight option (HAT025, departing at 04:00) since it is the only available direct economy flight on that date and aligns with a preferred early departure. You prefer to use the credit card ending in 4846 on file for payment, with total_baggages=1, nonfree_baggages=0, and no insurance. After that, you want to review the details of your existing round-trip basic economy reservation ZZF2YA from EWR to BOS on 2024-05-19, and explore available direct flight options on that route for potential rebooking, but note that no direct flights are currently available between EWR and BOS on that date, so any alternative would require a connection.\n\nUse amelia_li_2415 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'NUCNX0'}),
            Action(name='book_reservation', kwargs={'user_id': 'amelia_li_2415', 'origin': 'IAH', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT068', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Amelia', 'last_name': 'Li', 'dob': '1964-10-15'}, {'first_name': 'Lucas', 'last_name': 'Kim', 'dob': '1990-10-15'}, {'first_name': 'Amelia', 'last_name': 'Santos', 'dob': '1950-03-26'}], 'payment_methods': [{'payment_id': 'credit_card_1605369', 'amount': 519}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'ZZF2YA'}),
            Action(name='search_direct_flight', kwargs={'origin': 'EWR', 'destination': 'BOS', 'date': '2024-05-19'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_patel_1917',
        instruction='You are assisting Daiki Patel (user_id: daiki_patel_1917) who had his business class flight from SFO to PHL (reservation 0W60LB) cancelled and would like to receive a compensation certificate for the inconvenience. After that, you will help him rebook his trip on a new flight from SFO to PHL in business class on 2024-05-20. You prefer the early morning flight HAT042, which departs at 06:00, as it aligns with his original travel plans and offers available business class seating. The rebooking should be charged to his credit card ending in 1765, which is already on file and was used for the original purchase.\n\nUse daiki_patel_1917 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'daiki_patel_1917', 'amount': 100}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '0W60LB'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '0W60LB', 'cabin': 'business', 'flights': [{'flight_number': 'HAT042', 'date': '2024-05-20'}], 'payment_id': 'credit_card_4327297'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia_kim_8433',
        instruction='You are Sofia Kim, and you initially wanted to review your round-trip business class reservation 5ZV1XV from CLT to MCO on 2024-05-28, which involves a one-stop itinerary via BOS (HAT064 and HAT145), and you also wanted to explore alternative one-stop flight options for the same route and date. However, you later decided to cancel this reservation because you prefer a direct flight from CLT to MCO on 2024-05-28 for greater convenience. After checking, you found no direct flights are available on that route and date, so your updated preference is to proceed with cancellation and await notification for any future direct flight options. Additionally, you experienced a delay on a prior flight (HAT154 from LAS to MCO on 2024-05-13, part of reservation 89W3AO), and you would like to request a compensation certificate for that disruption.\n\nUse sofia_kim_8433 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '5ZV1XV'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'MCO', 'date': '2024-05-28'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '5ZV1XV'}),
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'MCO', 'date': '2024-05-28'}),
            Action(name='send_certificate', kwargs={'user_id': 'sofia_kim_8433', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf_martin_3470',
        instruction='You are assisting Yusuf Martin with his upcoming one-way business-class trip from JFK to LAX via MIA on 2024-05-22 under reservation BBVDO9. You want to correct the last name of passenger Yusuf Muller (DOB 1956-05-06) to Martin, as it currently does not match his legal name. After that, you would like to add one checked bag to the reservation, increasing the total to two checked bags with one being paid, because the current baggage allowance does not meet travel needs. You prefer the baggage fee to be charged to your saved Mastercard ending in 6182, as it is your preferred payment method on file.\n\nUse yusuf_martin_3470 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'BBVDO9'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'BBVDO9', 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Martin', 'dob': '1964-02-24'}, {'first_name': 'Yusuf', 'last_name': 'Martin', 'dob': '1956-05-06'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'BBVDO9', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_9067289'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_khan_4151',
        instruction='You are updating reservation RRMXPX for a one-way business class trip from MIA to PHX via LAS on 2024-05-27 and 2024-05-28. You want to change the passenger from Mei Brown to your saved passenger Raj Lopez (DOB 1953-05-18), because he is the intended traveler. You would like to increase the total checked baggage from 2 to 3, adding 1 paid bag, because additional luggage is needed for the trip. You prefer the bag fee to be charged to your Mastercard ending in 3445, as it is your preferred payment method on file.\n\nUse isabella_khan_4151 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RRMXPX'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'RRMXPX', 'passengers': [{'first_name': 'Raj', 'last_name': 'Lopez', 'dob': '1953-05-18'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'RRMXPX', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_4651498'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_lee_7603',
        instruction='You are assisting Daiki Lee (daiki_lee_7603), who had a business class one-way flight from LAS to PHX on 2024-05-11 (flight HAT244) under reservation PMZURQ, which was cancelled. You want to request a compensation certificate for the inconvenience caused by the cancellation, as a goodwill gesture for the disrupted travel plans. Later, you would like to formally cancel the reservation PMZURQ to confirm the refund process, even though the flight has already been cancelled, and you prefer the refund to be returned to the original payment method, which was a gift card ending in 3421731.\n\nUse daiki_lee_7603 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'daiki_lee_7603', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'PMZURQ'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'PMZURQ'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_lee_7603',
        instruction='You are to cancel the existing reservation PMZURQ for Daiki Lee, which was a business class one-way flight from LAS to PHX on 2024-05-11, as it has been cancelled by the airline. You would like to explore rebooking options and prefer a one-stop business class flight from LAS to PHX on 2024-05-20, with a departure in the early morning or later time window, given the availability of multiple connecting options. Later, you will request a compensation certificate due to the inconvenience caused by the cancellation of your original flight.\n\nUse daiki_lee_7603 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'PMZURQ'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'PMZURQ'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'daiki_lee_7603', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_davis_4420',
        instruction='You are updating reservation ZQVILE for a one-way trip from PHX to DFW. First, you want to change the passenger from Olivia Johnson to Anya Jackson, as she is the intended traveler. Then, you would like to add one checked bag, bringing the total to two bags with one being paid, to accommodate additional luggage. After that, you prefer to upgrade the entire itinerary to business class on both flights: the flight from PHX to SEA on 2024-05-24 and the connecting flight from SEA to DFW on 2024-05-25, to ensure a more comfortable travel experience. You prefer all additional charges for the bag and fare difference to be billed to your Mastercard ending in 3597, which is already on file.\n\nUse ethan_davis_4420 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'ZQVILE'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'ZQVILE', 'passengers': [{'first_name': 'Anya', 'last_name': 'Jackson', 'dob': '1987-05-06'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'ZQVILE', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_9585625'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'ZQVILE', 'cabin': 'business', 'flights': [{'flight_number': 'HAT045', 'date': '2024-05-24'}, {'flight_number': 'HAT113', 'date': '2024-05-25'}], 'payment_id': 'credit_card_9585625'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia_anderson_8651',
        instruction='You are Olivia Anderson, and you want to cancel your round-trip reservation GHHGOB from LGA to LGA via PHL and CLT because your plans have changed, and you prefer the refund to be processed to your Mastercard ending in 4016. Later, you would like to book a new one-way flight from LGA to PHX on 2024-05-20 for passenger Olivia Anderson in economy class, preferring the late evening flight (HAT002) departing at 9:00 PM, and you prefer to pay using your Mastercard ending in 4016. After that, you want to upgrade the MSP to MCO leg of reservation FUQR5E (flight HAT036) on 2024-05-17 from economy to business class for passenger Anya Davis, also using your Mastercard ending in 4016 for the fare difference.\n\nUse olivia_anderson_8651 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'GHHGOB'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GHHGOB'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LGA', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'olivia_anderson_8651', 'origin': 'LGA', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT002', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Olivia', 'last_name': 'Anderson', 'dob': '1960-08-19'}], 'payment_methods': [{'payment_id': 'credit_card_6349270', 'amount': 175}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'FUQR5E', 'cabin': 'business', 'flights': [{'flight_number': 'HAT036', 'date': '2024-05-17'}], 'payment_id': 'credit_card_6349270'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_nguyen_6691',
        instruction='You are to assist Chen Nguyen and Sophia Patel with their respective requests in sequence. First, you want to book a one-way business class flight from Atlanta to New York on 2024-05-20 for two passengers: Chen Nguyen and Aarav Taylor, preferring an afternoon departure because that is the only available direct business flight on that date. You prefer to pay using your Visa card ending in 6205. Later, you want to update your existing reservation 5PQ0HT for the outbound journey from Atlanta to Denver via Las Vegas on 2024-05-24, keeping the same flights (HAT178 and HAT162) in business class, but updating the passenger list to remove Anya Santos and add Mei Silva (DOB 1967-05-12) due to a change in travel plans. After that, you are to assist Sophia Patel, who had her one-way flight from New York to Seattle on 2024-05-11 cancelled, and she would like to receive a compensation certificate as restitution for the disruption.\n\nUse chen_nguyen_6691 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'chen_nguyen_6691', 'origin': 'ATL', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT233', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Chen', 'last_name': 'Nguyen', 'dob': '1973-09-23'}, {'first_name': 'Aarav', 'last_name': 'Taylor', 'dob': '1980-05-19'}], 'payment_methods': [{'payment_id': 'credit_card_9491838', 'amount': 756}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '5PQ0HT', 'cabin': 'business', 'flights': [{'flight_number': 'HAT178', 'date': '2024-05-24'}, {'flight_number': 'HAT162', 'date': '2024-05-24'}, {'flight_number': 'HAT046', 'date': '2024-05-28'}, {'flight_number': 'HAT177', 'date': '2024-05-28'}], 'payment_id': 'credit_card_9491838'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '5PQ0HT', 'passengers': [{'first_name': 'Chen', 'last_name': 'Nguyen', 'dob': '1973-09-23'}, {'first_name': 'Aarav', 'last_name': 'Taylor', 'dob': '1980-05-19'}, {'first_name': 'Mei', 'last_name': 'Silva', 'dob': '1967-05-12'}]}),
            Action(name='send_certificate', kwargs={'user_id': 'sophia_patel_6859', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_lee_6144',
        instruction='You are assisting Daiki Lee with multiple travel requests. First, you want to confirm a one-way one-stop flight from PHL to PHX on 2024-05-20 for one passenger in economy class, departing in the late afternoon from PHL and connecting in the evening via LGA, as this fits the planned travel schedule. You prefer to pay using the Visa card ending in 9734, which is your preferred payment method. Later, you would like to cancel your existing one-way economy reservation from PHL to SFO on 2024-05-18, as you are reconsidering your travel plans. After cancellation, you want to search for direct flight options from PHL to SFO on the same date (2024-05-18) to explore potentially more convenient alternatives. Additionally, you need to update the passenger on your one-way business class reservation from MCO to BOS on 2024-05-27, changing the name from Daiki Lee to Raj Muller (DOB 1967-10-16), as the trip is now being taken by a colleague.\n\nUse daiki_lee_6144 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'PHL', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_lee_6144', 'origin': 'PHL', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT135', 'date': '2024-05-20'}, {'flight_number': 'HAT150', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Lee', 'dob': '1976-10-08'}], 'payment_methods': [{'payment_id': 'credit_card_6198952', 'amount': 322}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'IIHXDG'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHL', 'destination': 'SFO', 'date': '2024-05-18'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'COVE6R'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'COVE6R', 'passengers': [{'first_name': 'Raj', 'last_name': 'Muller', 'dob': '1967-10-16'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_silva_9265',
        instruction='You are Mohamed Silva, and you have a reservation (K1NW8N) for a round-trip basic economy flight from JFK to SFO with a connection in SEA for three passengers: Mohamed Silva, Raj Sanchez, and Liam Wilson. You want to cancel this entire reservation because you are reconsidering your travel plans, and it is within the 24-hour window for cancellation. Later, you would like to explore rebooking a one-stop return flight from SFO to JFK on 2024-05-28. You prefer an early morning departure from SFO, specifically the connecting option arriving at LGA (New York) via PHX, as it serves the same metropolitan area as JFK and is the only viable one-stop option available on that date.\n\nUse mohamed_silva_9265 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'K1NW8N'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'K1NW8N'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'JFK', 'date': '2024-05-28'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma_martin_8571',
        instruction='You are Emma Martin, traveling with passenger Lei Hernandez, and you want to verify your existing one-way reservation 1JR46H from DTW to BOS on 2024-05-20 with a connection via CLT, booked in economy class. You would also like to explore alternative one-stop flight options from DTW to BOS on the same date, possibly considering a change for better timing or convenience. However, after searching, no direct one-stop flight options from DTW to BOS on 2024-05-20 are available; all alternative itineraries connect through PHX, JFK, or MSP and do not reach BOS. Therefore, you prefer to keep your current reservation unless a suitable one-stop DTW-to-BOS option becomes available.\n\nUse emma_martin_8571 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '1JR46H'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'BOS', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia_silva_7557',
        instruction='You are assisting Sophia Silva (user_id: sophia_silva_7557) with her travel changes. You want to book a one-way, one-stop flight from MSP to CLT on 2024-05-20 for passenger Yara Silva, with the first leg from MSP to DTW on flight HAT248 departing at 05:00 and the second leg from DTW to CLT on flight HAT053 departing at 16:00, both in economy class, with one checked bag, because she has changed her destination from EWR to CLT. You prefer to pay using the credit card ending in 7238. After that, you want to cancel the original round-trip basic economy reservation NM1VX1 from MSP to EWR, because it is no longer needed. Later, you would like to search for direct flights from MSP to DTW on 2024-05-22, possibly for future travel consideration, and you note that flight HAT248 is available that day departing at 05:00.\n\nUse sophia_silva_7557 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'MSP', 'destination': 'CLT', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'sophia_silva_7557', 'origin': 'MSP', 'destination': 'CLT', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT248', 'date': '2024-05-20'}, {'flight_number': 'HAT053', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yara', 'last_name': 'Silva', 'dob': '1972-06-16'}], 'payment_methods': [{'payment_id': 'credit_card_4196779', 'amount': 267}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'NM1VX1'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MSP', 'destination': 'DTW', 'date': '2024-05-22'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_nguyen_6045',
        instruction='You are assisting Ethan Nguyen (user_id: ethan_nguyen_6045) with updating his travel plans. You want to book a one-way connecting flight from LGA to SFO on 2024-05-20, with a stop in PHX, for one passenger (Ethan Nguyen), in economy class, departing LGA early morning (HAT245 at 00:00) and connecting in PHX to SFO in the afternoon (HAT159 at 14:00), with one total baggage and no insurance, charged to his saved Visa card ending in 3303. After that, you would like to cancel his original round-trip reservation L1QGWV (LGA to PHL on 2024-05-28 and return) and request a refund to the same credit card. Subsequently, you want to explore available direct flight options from LGA to PHL on 2024-05-28, particularly those in the early morning (around 03:00) and morning (around 08:00), to assess potential rebooking alternatives.\n\nUse ethan_nguyen_6045 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ethan_nguyen_6045', 'origin': 'LGA', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT245', 'date': '2024-05-20'}, {'flight_number': 'HAT159', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ethan', 'last_name': 'Nguyen', 'dob': '1970-04-28'}], 'payment_methods': [{'payment_id': 'credit_card_8005628', 'amount': 284}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'L1QGWV'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-28'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_moore_8640',
        instruction='You are updating reservation VCAM3D for Raj Moore (DOB 1966-02-02) to change the first flight from LAS to PHX on 2024-05-28 from the early morning departure to a morning flight, specifically HAT244 departing at 10:00 AM, while keeping the connecting flight HAT073 from PHX to DTW on the same day in business class. You want both flights to remain in business class because of comfort and work needs during travel. You also want to increase the total checked bags to two, with one additional paid bag, because you need extra luggage for your trip. Any fare difference should be charged to your credit card ending in 8131, which is already on file. Finally, you would like confirmation that all passenger details are correctly recorded as Raj Moore.\n\nUse raj_moore_8640 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'VCAM3D'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'VCAM3D', 'cabin': 'business', 'flights': [{'flight_number': 'HAT244', 'date': '2024-05-28'}, {'flight_number': 'HAT073', 'date': '2024-05-28'}], 'payment_id': 'credit_card_8507667'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'VCAM3D', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_8507667'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'VCAM3D', 'passengers': [{'first_name': 'Raj', 'last_name': 'Moore', 'dob': '1966-02-02'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_nguyen_4239',
        instruction='You are assisting Isabella Nguyen (DOB: 1976-12-13) with updating her reservation 66NJCE for travel on 2024-05-28. You want to upgrade both flight segments to business class: first, the early morning flight from Philadelphia (PHL) to Charlotte (CLT) (HAT269), because she prefers a more comfortable cabin for the start of her journey; and later, the late evening flight from Charlotte (CLT) to Newark (EWR) (HAT157), to ensure comfort on the final leg. You would like to add one checked bag, resulting in two total bags (one paid), to accommodate her travel needs. You prefer to use her Visa card ending in 5063 for any applicable charges. You also want to confirm her passenger details are correctly recorded as Isabella Nguyen with the date of birth 1976-12-13.\n\nUse isabella_nguyen_4239 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '66NJCE'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '66NJCE', 'cabin': 'business', 'flights': [{'flight_number': 'HAT269', 'date': '2024-05-28'}, {'flight_number': 'HAT157', 'date': '2024-05-28'}], 'payment_id': 'credit_card_8035954'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '66NJCE', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_8035954'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '66NJCE', 'passengers': [{'first_name': 'Isabella', 'last_name': 'Nguyen', 'dob': '1976-12-13'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_brown_3623',
        instruction="You are Mohamed Brown (user_id: mohamed_brown_3623) and you want to cancel your existing round-trip business class reservation UEMRO5 from SEA to DFW because your travel plans have changed. After that, you would like to book a one-way economy flight from SEA to SFO on 2024-05-20 for two passengers, Fatima Gonzalez and Ava Kovács, preferring flight HAT258 which departs in the evening. You prefer to pay using your Mastercard ending in 3777. Later, you realized there is a typo in the passenger name and you would like to update Ava Kovacs' last name to 'Kovács' to ensure accurate travel documentation.\n\nUse mohamed_brown_3623 for authentication.",
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'UEMRO5'}),
            Action(name='book_reservation', kwargs={'user_id': 'mohamed_brown_3623', 'origin': 'SEA', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT258', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Fatima', 'last_name': 'Gonzalez', 'dob': '1953-07-22'}, {'first_name': 'Ava', 'last_name': 'Kovacs', 'dob': '1977-06-11'}], 'payment_methods': [{'payment_id': 'credit_card_8077450', 'amount': 342}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'HATHAT', 'passengers': [{'first_name': 'Fatima', 'last_name': 'Gonzalez', 'dob': '1953-07-22'}, {'first_name': 'Ava', 'last_name': 'Kovács', 'dob': '1977-06-11'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_rossi_4078',
        instruction='You are assisting Evelyn Rossi, a gold member, who wants to upgrade her existing round-trip economy reservation (7SISHT) from SFO to LAX on 2024-05-19 to business class, as she initially intended to book a new one-way business flight on the same route and date but decided to modify her current booking instead. You want to use her Mastercard ending in 8752 for any additional charges. Later, you will cancel her other reservation (EZGELT) for a one-way business flight from MIA to LAS on 2024-05-21, as she no longer needs it. After that, you would like to request a compensation certificate for the cancellation of reservation EZGELT, since the flight was cancelled by the airline and she is entitled to compensation under her membership benefits.\n\nUse evelyn_rossi_4078 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'LAX', 'date': '2024-05-19'}),
            Action(name='book_reservation', kwargs={'user_id': 'evelyn_rossi_4078', 'origin': 'SFO', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT257', 'date': '2024-05-19'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Rossi', 'dob': '1997-11-08'}], 'payment_methods': [{'payment_id': 'credit_card_2355067', 'amount': 405}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '7SISHT'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'EZGELT'}),
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_rossi_4078', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_hernandez_5188',
        instruction='You are to first cancel the round-trip business class reservation from LAX to SFO (confirmation code 35V5SM) for Yusuf Lee because Mohamed Hernandez needs to change his plans, and process a refund to the original payment method, the credit card ending in 7393. Later, you are to book a one-way economy class flight from LAX to ORD on 2024-05-20 for Evelyn Rossi, as this route better suits the updated travel needs. You prefer the overnight flight departing LAX around 02:00 AM and arriving in ORD by 06:00 AM, specifically flight HAT103, because it is the only available economy seat on that date and aligns with the requested timing. You prefer to pay the $126 fare using the same credit card ending in 7393, with no checked bags and no travel insurance.\n\nUse mohamed_hernandez_5188 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '35V5SM'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAX', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mohamed_hernandez_5188', 'origin': 'LAX', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT103', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Rossi', 'dob': '1972-09-13'}], 'payment_methods': [{'payment_id': 'credit_card_5417084', 'amount': 126}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_martin_2396',
        instruction='You are assisting Ethan Martin with the cancellation of his round-trip economy reservation from LGA to BOS via CLT on May 27–28, 2024. You want to cancel reservation GXWCPN and have the refund processed back to the original payment method, which is the credit card ending in 57, because it was the card used for the initial purchase. Later, you would like to request a compensation certificate as a goodwill gesture for the inconvenience caused by the need to cancel the trip.\n\nUse ethan_martin_2396 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GXWCPN'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'GXWCPN'}),
            Action(name='send_certificate', kwargs={'user_id': 'ethan_martin_2396', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav_brown_5556',
        instruction='You are Aarav Brown, user aarav_brown_5556, who wants to cancel your one-way business class reservation 00GMVN for the flight from SFO to SEA on 2024-05-21 because your plans have changed. You are eligible for cancellation as per airline policy for business class bookings. After the cancellation, you would like to receive a compensation certificate for the inconvenience, as compensation of $100 per passenger is standard for canceled flights.\n\nUse aarav_brown_5556 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '00GMVN'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '00GMVN'}),
            Action(name='send_certificate', kwargs={'user_id': 'aarav_brown_5556', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_lee_6144',
        instruction='You are assisting Daiki Lee (user_id: daiki_lee_6144) with updating his reservation COVE6R. You want to change his one-way business class flight from MCO to BOS from 2024-05-27 to 2024-05-28, because he needs to delay his trip by one day. You prefer an early morning flight on 2024-05-28 for the updated travel date, as reflected by the selection of the available business class option. You prefer to use the credit card ending in 9734 for any fare difference associated with the change.\n\nUse daiki_lee_6144 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'COVE6R'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'COVE6R', 'cabin': 'business', 'flights': [{'flight_number': 'HAT028', 'date': '2024-05-28'}], 'payment_id': 'credit_card_6198952'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_silva_5208',
        instruction='You are Evelyn Silva (user_id: evelyn_silva_5208) managing reservation 90WDMA for two passengers, Fatima Anderson and Fatima Davis. You want to upgrade both segments of the one-way trip from PHX to LAX via SFO on 2024-05-21 from economy to business class. The first segment is flight HAT283 (PHX-SFO), departing in the evening, and the second is flight HAT257 (SFO-LAX), also departing in the evening. You prefer both passengers to be upgraded on these flights because business class offers greater comfort for the journey. You prefer to use your credit card ending in 5642 (payment_id: credit_card_1638882) to cover any fare difference, as it is already on file and convenient for payment.\n\nUse evelyn_silva_5208 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '90WDMA'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '90WDMA', 'cabin': 'business', 'flights': [{'flight_number': 'HAT283', 'date': '2024-05-21'}, {'flight_number': 'HAT257', 'date': '2024-05-21'}], 'payment_id': 'credit_card_1638882'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james_santos_9046',
        instruction="You are James Santos, and you want to update your reservation 5GAZGX for a business trip from IAH to SEA. You prefer to change the departure flight to HAT112 on 2024-05-26 from IAH to LAS and the connecting flight to HAT047 on 2024-05-27 from LAS to SEA, keeping both in business class, because you need to move the trip one day earlier. You also want to add one additional checked bag, making a total of two bags (one paid), to accommodate extra luggage for the trip. You prefer to use your Mastercard ending in 2536 for any additional charges. Later, you want to cancel your return basic economy reservation MWJZ87 due to schedule conflicts. After that, you would like to book a new one-way business class flight HAT207 from IAH to EWR on 2024-05-20 for two passengers: James Santos and Liam Kim, with one checked bag (no paid bags) and no insurance, because it's a separate short trip. You prefer to use your Visa ending in 5993 for this new booking. Finally, since your flight was cancelled, you would like to receive a compensation certificate as reimbursement.\n\nUse james_santos_9046 for authentication.",
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '5GAZGX'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '5GAZGX', 'cabin': 'business', 'flights': [{'flight_number': 'HAT112', 'date': '2024-05-26'}, {'flight_number': 'HAT047', 'date': '2024-05-27'}], 'payment_id': 'credit_card_3365978'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '5GAZGX', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3365978'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'MWJZ87'}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'james_santos_9046', 'origin': 'IAH', 'destination': 'EWR', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT207', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'James', 'last_name': 'Santos', 'dob': '1956-12-09'}, {'first_name': 'Liam', 'last_name': 'Kim', 'dob': '1997-12-04'}], 'payment_methods': [{'payment_id': 'credit_card_6899560', 'amount': 408}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'james_santos_9046', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason_johansson_5154',
        instruction='You are Mason Johansson, a regular customer, and you want to update your original reservation RB9S17 to a new travel date. You would like to cancel your existing reservation for the CLT to DEN flight on 2024-05-28 and instead book a new one-way business class flight for one passenger from CLT to DEN on 2024-05-20, specifically on flight HAT262, which departs in the afternoon at 13:00, because it is the only direct flight available on that date. You prefer to use your credit card ending in 1242 for the new booking and any fare difference. Later, you also want to explore flight options from CLT to DEN on 2024-05-20 to compare, including both direct and one-stop flights; however, only the direct flight HAT262 is available, as no connecting options reach DEN on that date.\n\nUse mason_johansson_5154 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RB9S17'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'RB9S17', 'cabin': 'business', 'flights': [{'flight_number': 'HAT262', 'date': '2024-05-20'}], 'payment_id': 'credit_card_3358561'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'RB9S17'}),
            Action(name='book_reservation', kwargs={'user_id': 'mason_johansson_5154', 'origin': 'CLT', 'destination': 'DEN', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT262', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mason', 'last_name': 'Johansson', 'dob': '1955-01-07'}], 'payment_methods': [{'payment_id': 'credit_card_3358561', 'amount': 466}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'DEN', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'DEN', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_johnson_3148',
        instruction='You are Fatima Johnson (fatima_johnson_3148), a silver member planning a trip from Dallas (DFW) to Newark (EWR) on May 20, 2024. You want to explore available flight options to make an informed decision, valuing flexibility and convenience. You would like to see all direct and one-stop flight options from DFW to EWR on that date. After reviewing, you find there is only one viable flight: a direct evening flight from DFW to EWR on May 20, 2024, departing in the late afternoon and arriving in the evening. You prefer this direct flight option for its convenience and schedule alignment. No valid one-stop flights are available to EWR on this date, so your focus remains on evaluating this single direct flight before making a booking decision.\n\nUse fatima_johnson_3148 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'DFW', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DFW', 'destination': 'EWR', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_ito_2309',
        instruction='You are Harper Ito (harper_ito_2309) and you want to compare direct and one-stop flight options from JFK to ORD on 2024-05-20. You prefer a direct flight on 2024-05-20 departing late evening (around 00:00) as it aligns with your travel plans and avoids layovers. Since no one-stop flights are available from JFK to ORD on that date, you would like to proceed with reviewing the direct flight option for your trip.\n\nUse harper_ito_2309 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'ORD', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_moore_8640',
        instruction='You are Raj Moore (DOB: 1966-02-02) and you want to book a new one-way economy flight from LAS to DTW on 2024-05-20 with a connection in PHX, departing early in the morning, because you found a suitable itinerary using flight HAT284 (LAS→PHX) and HAT265 (PHX→DTW) and prefer this timing for convenience. You want one free baggage included and no travel insurance, and you prefer to pay using your Visa card ending in 8131. Later, you want to update your existing reservation VCAM3D for a one-way business class trip from LAS to DTW on 2024-05-28 to confirm the flights as HAT284 and HAT073, ensuring continuity with your preferred routing. After that, you would like to increase the total baggage allowance to 2 on VCAM3D, with one additional paid baggage, and charge the fee to the same Visa card ending in 8131, to accommodate your travel needs. Finally, you want to review the updated details of reservation VCAM3D to confirm all changes were applied correctly.\n\nUse raj_moore_8640 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'raj_moore_8640', 'origin': 'LAS', 'destination': 'DTW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT284', 'date': '2024-05-20'}, {'flight_number': 'HAT265', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Raj', 'last_name': 'Moore', 'dob': '1966-02-02'}], 'payment_methods': [{'payment_id': 'credit_card_8507667', 'amount': 346}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'VCAM3D', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_8507667'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'VCAM3D', 'cabin': 'business', 'flights': [{'flight_number': 'HAT284', 'date': '2024-05-28'}, {'flight_number': 'HAT073', 'date': '2024-05-28'}], 'payment_id': 'credit_card_8507667'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'VCAM3D'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_hernandez_8403',
        instruction='You are assisting Amelia Hernandez, who wants to book a one-way economy flight from IAH to SFO on 2024-05-20 for herself and Raj Lopez, departing in the morning (flight HAT072 at 09:00), because she has updated her travel plans. She would like to include one checked bag at no additional cost, as it is within her allowance, and prefers to pay using her Mastercard ending in 3785. Later, she wants to cancel her existing round-trip reservation 5JR4XX from IAH to CLT, which includes connecting flights via EWR, due to this change in plans. After that, she would like to update her reservation GKW825 for the one-way trip from PHX to BOS on 2024-05-26 to add two checked bags for the travelers on the booking, with both bags charged to her Mastercard ending in 3785, as she needs to accommodate additional luggage for the trip.\n\nUse amelia_hernandez_8403 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'amelia_hernandez_8403', 'origin': 'IAH', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT072', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Amelia', 'last_name': 'Hernandez', 'dob': '1968-11-28'}, {'first_name': 'Raj', 'last_name': 'Lopez', 'dob': '1963-09-13'}], 'payment_methods': [{'payment_id': 'credit_card_2756027', 'amount': 200}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '5JR4XX'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'GKW825'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'GKW825', 'total_baggages': 2, 'nonfree_baggages': 2, 'payment_id': 'credit_card_2756027'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_martin_3083',
        instruction='You are assisting Noah Martin (user_id: noah_martin_3083) who wants to book a one-way flight from BOS to MCO on 2024-05-20 for himself and passenger Lei Lopez in economy class, preferring an early morning flight based on available options. You want to include one checked bag using the free allowance and pay with the Visa card ending in 2091 on file. Later, you would like to cancel the existing round-trip basic economy reservation KLA174 from BOS to DTW due to changed plans, with refund issued to the same credit card. After that, you would like to add one checked bag to the business class round-trip reservation DS6NDE for passenger Raj Muller traveling from LAX to ATL, paying the $30 fee using the same Visa card ending in 2091.\n\nUse noah_martin_3083 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_martin_3083', 'origin': 'BOS', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT013', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Noah', 'last_name': 'Martin', 'dob': '1995-02-28'}, {'first_name': 'Lei', 'last_name': 'Lopez', 'dob': '1955-01-26'}], 'payment_methods': [{'payment_id': 'credit_card_7670221', 'amount': 200}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'KLA174'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'DS6NDE', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_7670221'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_rossi_9391',
        instruction='You are assisting Lucas Rossi, who is traveling with Lucas Anderson, Chen Ahmed, and Juan Sanchez. You want to explore available one-stop flight options from DTW to LAS on 2024-05-26 to evaluate suitable alternatives before making changes, as the current itinerary involves an overnight departure. Later, you would like to cancel the existing reservation FDEBWQ, which includes a round-trip in basic economy with a connection in PHX, because suitable alternatives are being considered. After that, you would like a full refund processed to the Mastercard ending in 7352, as this payment method is on file and the reservation is covered by travel insurance.\n\nUse lucas_rossi_9391 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'LAS', 'date': '2024-05-26'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'FDEBWQ'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_thomas_8641',
        instruction='You are assisting Harper Thomas, a silver member, who is adjusting travel plans. You want to explore one-way travel options to the West Coast, specifically by searching for direct flights from Boston to Seattle on 2024-05-22. After identifying available options, you would like to cancel the existing round-trip reservation TV8G38 from Boston to Denver via Miami and returning via Charlotte, as the new plans make the original trip unnecessary. You prefer the refund to be issued to the original Mastercard ending in 2008, which was used for the booking.\n\nUse harper_thomas_8641 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'SEA', 'date': '2024-05-22'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'TV8G38'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia_brown_9485',
        instruction='You are to first cancel the existing reservation GAST7Q for Sofia Brown, which is a business class one-way flight from CLT to BOS on 2024-05-21, because she no longer wishes to travel to Boston. After that, you are to book a new one-stop journey from CLT to LAX in business class for Sofia Brown (DOB: 1968-12-25), with the first flight departing CLT for EWR on 2024-05-22 in the late evening (around 11:00 PM) on flight HAT157, followed by a connecting flight from EWR to LAX on 2024-05-23 in the early morning (around 7:00 AM) on flight HAT041. You prefer to book both flights in business class for 1 passenger, with 1 total baggage (none paid), and without travel insurance. You prefer to use the credit card ending in 5332048 for payment, as it is your saved card on file.\n\nUse sofia_brown_9485 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GAST7Q'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'LAX', 'date': '2024-05-22'}),
            Action(name='book_reservation', kwargs={'user_id': 'sofia_brown_9485', 'origin': 'CLT', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT157', 'date': '2024-05-22'}, {'flight_number': 'HAT041', 'date': '2024-05-23'}], 'passengers': [{'first_name': 'Sofia', 'last_name': 'Brown', 'dob': '1968-12-25'}], 'payment_methods': [{'payment_id': 'credit_card_5332048', 'amount': 845}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are Ivan Taylor (ivan_taylor_6615) and you want a compensation certificate because your flight HAT052 from ATL to LAS on 2024-05-08 was cancelled. Later, you would like to book a one-way flight from ATL to LGA on 2024-05-20 in economy class for two passengers, Ivan Taylor and Aarav Kim, with two checked bags (both free), no insurance, and you prefer to pay using your credit card ending in 1656. After that, you want to update your existing reservation PK9XO8 by adding one additional checked bag (making a total of three, with one paid) and changing your SFO-to-IAH flight on 2024-05-24 from the original departure to a later one at 23:00 (flight HAT082), keeping business class, and you prefer to use your credit card ending in 1656 for any fare difference.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'ATL', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT110', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Aarav', 'last_name': 'Kim', 'dob': '1962-10-28'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 336}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'PK9XO8'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'PK9XO8', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_1885633'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'PK9XO8', 'cabin': 'business', 'flights': [{'flight_number': 'HAT034', 'date': '2024-05-24'}, {'flight_number': 'HAT082', 'date': '2024-05-24'}, {'flight_number': 'HAT072', 'date': '2024-05-27'}, {'flight_number': 'HAT273', 'date': '2024-05-27'}], 'payment_id': 'credit_card_1885633'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma_johansson_6252',
        instruction='You are to cancel the reservation 3AU451 for Emma Johansson, which includes a one-way basic economy flight from CLT to MSP via DTW on 2024-05-19, because the trip has been decided to be cancelled. You want the refund to be issued to the original payment method, which is the Visa card ending in 4149, as this was the card used for booking and is the preferred method for reimbursement.\n\nUse emma_johansson_6252 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '3AU451'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '3AU451'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei_hernandez_9827',
        instruction='You are Mei Hernandez (mei_hernandez_9827) and you want to cancel your one-way economy reservation 672VDE from LAX to PHL via ORD on 2024-05-17, which includes insurance, because you no longer wish to travel on that date. After cancellation, you would like to search for alternative flights from LAX to PHL on 2024-05-18, starting with one-stop itineraries; however, no such connecting flights are available to PHL on that date. You also checked for direct flights from LAX to PHL on 2024-05-18, but there are no direct options. Due to the inconvenience of the original flight not being available on your preferred date and no alternatives existing, you would like to receive a goodwill compensation certificate.\n\nUse mei_hernandez_9827 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '672VDE'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '672VDE'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAX', 'destination': 'PHL', 'date': '2024-05-18'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAX', 'destination': 'PHL', 'date': '2024-05-18'}),
            Action(name='send_certificate', kwargs={'user_id': 'mei_hernandez_9827', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_lee_2325',
        instruction='You are Evelyn Lee, user ID evelyn_lee_2325, and you want to cancel your business class one-way reservation 4WEVK0 from PHX to SFO on 2024-05-22 for yourself and Daiki Anderson due to an emergency. After cancellation, you would like to explore rebooking options, preferring a direct flight from PHX to SFO on the same date, specifically in business class. Since HAT032 departs at 11:00 and is the only business class option available, you prefer a morning flight on 2024-05-22. You also want to check one-stop options in case no direct business class flights were available, but none connect to SFO. Later, you would like to receive a compensation certificate for the inconvenience caused by the cancellation.\n\nUse evelyn_lee_2325 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '4WEVK0'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '4WEVK0'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHX', 'destination': 'SFO', 'date': '2024-05-22'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'PHX', 'destination': 'SFO', 'date': '2024-05-22'}),
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_lee_2325', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_lee_2325',
        instruction='You are Evelyn Lee, and you want to change the cabin class from business to economy for your reservation 4WEVK0 for the flight from PHX to SFO on 2024-05-22, which departs in the evening, for both yourself and passenger Daiki Anderson, due to personal preference. You prefer to use your Visa card ending in 7370 for any fare adjustments associated with this change.\n\nUse evelyn_lee_2325 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '4WEVK0'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '4WEVK0', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT009', 'date': '2024-05-22'}], 'payment_id': 'credit_card_5787244'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHX', 'destination': 'SFO', 'date': '2024-05-22'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'PHX', 'destination': 'SFO', 'date': '2024-05-22'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan_moore_4540',
        instruction='You are Juan Moore, a gold member, traveling with Isabella Silva, and you want to verify your current reservation 2NULCR for a business class one-way flight from DFW to ATL on 2024-05-22. You are also interested in comparing available direct flight options on the same route and date to evaluate alternatives. You would like to consider a business class flight from DFW to ATL on 2024-05-22, particularly the evening option departing around 20:00, as an alternative to your current early morning flight.\n\nUse juan_moore_4540 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '2NULCR'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DFW', 'destination': 'ATL', 'date': '2024-05-22'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_ito_2309',
        instruction='You are assisting Harper Ito (harper_ito_2309) with their one-way reservation MCO2H9 for three passengers—Harper Ito, Yara Jackson, and Evelyn Davis—traveling from DTW to MIA via JFK on 2024-05-17 in economy class. You want to first retrieve the full details of the existing reservation to understand the current itinerary. After that, you would like to compare it with alternative flight options, specifically direct flights from DTW to JFK on the same date. You prefer a direct flight from DTW to JFK on 2024-05-17 in the afternoon, such as the available option departing around 16:00, to evaluate timing and pricing alternatives for the first leg of the journey.\n\nUse harper_ito_2309 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'MCO2H9'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DTW', 'destination': 'JFK', 'date': '2024-05-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction='You are to first cancel the existing business class round-trip reservation from DEN to LAS due to a schedule conflict. Then, you want to book a new one-way economy flight from DEN to MIA for passenger Yusuf Ahmed on 2024-05-20, preferring an early morning departure as offered by flight HAT255. You prefer to use your saved Visa card ending in 1892 for the booking. After confirmation, you would like to add one checked baggage to the reservation, charging the fee to the same card.\n\nUse noah_khan_8166 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'Y1ZIDC'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_khan_8166', 'origin': 'DEN', 'destination': 'MIA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT255', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}], 'payment_methods': [{'payment_id': 'credit_card_3240482', 'amount': 139}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'Y1ZIDC'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'Y1ZIDC', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3240482'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_li_1258',
        instruction='You are to first cancel the existing basic economy one-way reservation TOVYFC for Harper Li and Sofia Thomas from LGA to PHL on 2024-05-23, which is eligible for cancellation due to insurance coverage. Then, you want to book a new one-way economy flight from LGA to PHX on 2024-05-20 for the same two passengers, preferring the late evening flight HAT002 departing at 21:00, as it aligns with their requested flight number and travel plans. You prefer this booking to be charged to the Mastercard ending in 8455, which is on file. After that, you would like to update reservation X53YKA to add one checked bag, setting total_baggages and nonfree_baggages both to 1, and you prefer this charge to also be applied to the same Mastercard ending in 8455 for consistency in payment method.\n\nUse harper_li_1258 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'TOVYFC'}),
            Action(name='book_reservation', kwargs={'user_id': 'harper_li_1258', 'origin': 'LGA', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT002', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Harper', 'last_name': 'Li', 'dob': '1970-10-19'}, {'first_name': 'Sofia', 'last_name': 'Thomas', 'dob': '1953-03-01'}], 'payment_methods': [{'payment_id': 'credit_card_2007333', 'amount': 350}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'X53YKA'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'X53YKA', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_2007333'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_khan_4151',
        instruction='You are assisting Isabella Khan (isabella_khan_4151), who had her business class one-way flight from CLT to LGA on 2024-05-09 (reservation 8POIJI) cancelled. You want to request a compensation certificate for the cancellation, as this is standard policy for disrupted travel. Later, you will update the passenger list on reservation 8POIJI by replacing Raj Lopez with Emma White, while keeping Isabella Khan and Ivan Nguyen as the other two passengers, to reflect the correct traveler information. After that, you would like to search for new direct flight options from CLT to LGA on 2024-05-20 for rebooking. You prefer a direct business class flight on that date, and since only one direct option is available, you are interested in the early morning flight departing around 02:00 AM, which aligns with the available HAT024 service. You prefer to use the Mastercard ending in 3445 on file for any additional payments, if needed.\n\nUse isabella_khan_4151 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'isabella_khan_4151', 'amount': 300}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '8POIJI'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '8POIJI', 'passengers': [{'first_name': 'Isabella', 'last_name': 'Khan', 'dob': '1954-07-18'}, {'first_name': 'Ivan', 'last_name': 'Nguyen', 'dob': '1952-05-06'}, {'first_name': 'Emma', 'last_name': 'White', 'dob': '1990-04-10'}]}),
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'LGA', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_hernandez_5188',
        instruction='You are to first cancel the existing round-trip business reservation 35V5SM from LAX to SFO because the travel plans have changed. Then, you want to book a one-way economy flight from LAX to ORD on 2024-05-20 for passenger Evelyn Rossi, as she is traveling for work and needs a confirmed seat. You prefer flight HAT104 because it was specifically requested and has available economy seating. You want to include one total checked bag with no additional insurance, and you prefer to pay using your Mastercard ending in 7393. After that, you would like to explore flight options for another potential trip from LAX to ORD on 2024-05-25, specifically comparing direct flights (such as the early morning flight around 02:00 AM or the evening flight around 8:00 PM) versus one-stop itineraries, to evaluate timing and convenience for future planning.\n\nUse mohamed_hernandez_5188 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '35V5SM'}),
            Action(name='book_reservation', kwargs={'user_id': 'mohamed_hernandez_5188', 'origin': 'LAX', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT104', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Rossi', 'dob': '1972-09-13'}], 'payment_methods': [{'payment_id': 'credit_card_5417084', 'amount': 162}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAX', 'destination': 'ORD', 'date': '2024-05-25'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAX', 'destination': 'ORD', 'date': '2024-05-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan_muller_6989',
        instruction='You are Juan Muller, and you want to first verify your previous reservation TPN0ET, which was a one-way basic economy flight from ORD to PHX via DTW on 2024-05-12 for yourself and Sophia Muller. After that, you would like to explore new travel options from ORD to IAH on 2024-05-20. You want to consider both direct and one-stop flight options for this new trip. For direct flights, you prefer either an overnight departure around 00:00 or a morning departure around 09:00. You are also interested in one-stop options via connecting airports such as DTW or ATL, with flexible timing, to compare total travel time and cost. You prefer to use your Visa card ending in 5805 for any new bookings.\n\nUse juan_muller_6989 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'TPN0ET'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ORD', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'ORD', 'destination': 'IAH', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_johnson_1294',
        instruction='You are Daiki Johnson, user daiki_johnson_1294, with a current round-trip reservation OQU7IJ for travel from IAH to DTW on 2024-05-23 via ORD. You want to explore alternative flight options for the outbound journey from IAH to DTW on 2024-05-23, specifically comparing direct and one-stop itineraries for better convenience. After checking availability, you would like to consider a one-stop option departing IAH in the early morning (around 01:00 AM) and arriving at DTW by late evening (around 11:00 PM), as no direct flights are available on this route. You prefer to remain in economy class and are comparing pricing and timing for potential rebooking.\n\nUse daiki_johnson_1294 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'OQU7IJ'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'DTW', 'date': '2024-05-23'}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'DTW', 'date': '2024-05-23'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei_rossi_4874',
        instruction='You are Lei Rossi, and you want a compensation certificate for the cancelled flight on reservation 15EN70 from CLT to LGA on 2024-05-04, which affected you and passenger Isabella Jackson. Later, you would like to book a one-way flight from CLT to LGA on 2024-05-20 for two passengers, Lei Rossi and Liam Brown, in economy class, preferring an early morning departure around 02:00 AM as offered by flight HAT024. You prefer to pay using your Visa card ending in 7279. After that, you would like to cancel your active reservation H0HHXO for a one-way flight from IAH to EWR on 2024-05-28 in basic economy, which includes insurance and is booked for passengers Lei Rossi and Liam Brown, and you prefer the refund to be issued back to your Visa card ending in 7279.\n\nUse lei_rossi_4874 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'lei_rossi_4874', 'amount': 200}),
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'lei_rossi_4874', 'origin': 'CLT', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT024', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lei', 'last_name': 'Rossi', 'dob': '1986-11-21'}, {'first_name': 'Isabella', 'last_name': 'Jackson', 'dob': '2000-09-09'}], 'payment_methods': [{'payment_id': 'credit_card_9623492', 'amount': 360}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'H0HHXO'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are assisting Ivan Taylor (user_id: ivan_taylor_6615) with rebooking a flight for himself and Ivan Jackson after the cancellation of reservation 06K2QN (originally ATL to LAS on 2024-05-08). You want to book a direct flight from ATL to LAS on 2024-05-20 for two passengers in the basic economy cabin, with a preference for a late evening departure. There is only one viable direct flight (HAT281) departing at 22:00, so you prefer that option. Later, you would like to request a compensation certificate due to the prior flight cancellation, as per airline policy for disrupted travel.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_garcia_6211',
        instruction='You are assisting Evelyn Garcia (evelyn_garcia_6211), who had her previous flight HAT195 from IAH to EWR on 2024-05-11 cancelled under reservation 5264D4, which included two passengers: Evelyn Garcia and Mei Lee. You want to rebook a flight from IAH to SFO for both passengers on 2024-05-20. After checking, there are no direct or connecting flights available from IAH to SFO on that date. Later, you would like to request a compensation certificate worth $200 for the inconvenience caused by the cancellation of the original flight.\n\nUse evelyn_garcia_6211 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_garcia_6211', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james_li_5992',
        instruction='You are James Li, a regular customer, and you want to book a one-way flight from DFW to SEA on 2024-05-20 for yourself and your colleague Raj Davis. You prefer the morning flight, specifically flight HAT038 departing at 06:00 AM, in economy class, because it aligns with your travel plans. You prefer to pay using your saved Mastercard ending in 5020. Later, you also want to update the passenger details on your existing reservation HJ63VG for the one-way trip from LAS to ORD on 2024-05-21 by changing the passenger name from Lucas Jackson to Seb Smith, as Seb will now be traveling instead.\n\nUse james_li_5992 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'DFW', 'destination': 'SEA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'james_li_5992', 'origin': 'DFW', 'destination': 'SEA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT038', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'James', 'last_name': 'Li', 'dob': '1983-07-04'}, {'first_name': 'Raj', 'last_name': 'Davis', 'dob': '1951-06-23'}], 'payment_methods': [{'payment_id': 'credit_card_8972239', 'amount': 384}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'HJ63VG', 'passengers': [{'first_name': 'Raj', 'last_name': 'Davis', 'dob': '1951-06-23'}, {'first_name': 'Seb', 'last_name': 'Smith', 'dob': '1997-03-01'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_ito_2309',
        instruction='You are Harper Ito, contacting support on behalf of three passengers: Harper Ito, Yara Jackson, and Evelyn Davis. You want to cancel your existing one-way economy reservation MCO2H9 for the flight from DTW to MIA on 2024-05-17 due to a schedule conflict. After that, you would like to search for one-stop flight options from DTW to MIA on 2024-05-20, preferably with a daytime departure from DTW and reasonable connection times, to accommodate your revised travel plans. You prefer to keep the same cabin class (economy) and passenger group for any new booking.\n\nUse harper_ito_2309 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'MCO2H9'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'MIA', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav_jackson_2879',
        instruction='You are Aarav Jackson, account holder for reservation QQ69B9, and you want to cancel the business class one-way flight for passenger Isabella Wilson from ORD to IAH on 2024-05-18 because of changed travel plans. After that, you would like to search for one-stop flight options from ORD to SFO on 2024-05-20; however, no such connecting flights to SFO are available on that date in the current schedule.\n\nUse aarav_jackson_2879 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'QQ69B9'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ORD', 'destination': 'SFO', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia_martin_3924',
        instruction='You are Olivia Martin (DOB 1979-11-04), and you want to cancel your round-trip reservation DVONGW from DEN to JFK in economy class due to a schedule conflict. After that, you would like to book a new one-way flight from DEN to DFW on 2024-05-20 in economy class for two passengers: Olivia Martin and Yusuf Jackson, specifically on flight HAT246, which departs in the afternoon, and you prefer to pay using your Visa card ending in 7324. You also want to update your existing reservation H0MVIE for a one-way flight from CLT to BOS on 2024-05-20 to flight HAT287, which departs in the morning, keeping the same cabin class, and you prefer any fare difference to be charged to the same Visa card ending in 7324. Later, you would like to correct the passenger name on reservation H0MVIE from Olivia Martin to Olivia Smith (same DOB), and add one checked baggage, with the baggage fee also charged to your Visa card ending in 7324. Additionally, since your original reservation DVONGW was canceled, you would like to receive a compensation certificate as a travel voucher for future use.\n\nUse olivia_martin_3924 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'DVONGW'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DEN', 'destination': 'DFW', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'olivia_martin_3924', 'origin': 'DEN', 'destination': 'DFW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT246', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Olivia', 'last_name': 'Martin', 'dob': '1979-11-04'}, {'first_name': 'Yusuf', 'last_name': 'Jackson', 'dob': '1995-08-10'}], 'payment_methods': [{'payment_id': 'credit_card_1048722', 'amount': 214}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'H0MVIE', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT287', 'date': '2024-05-20'}], 'payment_id': 'credit_card_1048722'}),
            Action(name='send_certificate', kwargs={'user_id': 'olivia_martin_3924', 'amount': 100}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'H0MVIE'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'H0MVIE', 'passengers': [{'first_name': 'Olivia', 'last_name': 'Smith', 'dob': '1979-11-04'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'H0MVIE', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_1048722'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_rossi_9280',
        instruction="You are Lucas Rossi, and you want to book a one-way flight from EWR to MSP on 2024-05-20 for two passengers, yourself and Isabella Hernandez, in economy class, specifically flight HAT208, which is an overnight flight, because you prefer that timing and it matches your schedule. You want to use your Mastercard ending in 7523 for payment and include one total baggage with no non-free charges, without purchasing insurance. After booking, you would like to update the passenger list to correct a typo by changing 'Isabella Hernandez' to 'Isabella Rossi' while keeping her date of birth unchanged, to ensure her travel documents are accurate. Later, you would like to cancel your existing round-trip reservation RF9ICL from EWR to SFO because you no longer need the trip, and you prefer the refund to be issued back to the same Mastercard ending in 7523 since it was the original payment method and the reservation is fully refundable due to travel insurance.\n\nUse lucas_rossi_9280 for authentication.",
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'EWR', 'destination': 'MSP', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'lucas_rossi_9280', 'origin': 'EWR', 'destination': 'MSP', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT208', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lucas', 'last_name': 'Rossi', 'dob': '1981-10-17'}, {'first_name': 'Isabella', 'last_name': 'Hernandez', 'dob': '1998-08-06'}], 'payment_methods': [{'payment_id': 'credit_card_1106772', 'amount': 352}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'MH743C', 'passengers': [{'first_name': 'Lucas', 'last_name': 'Rossi', 'dob': '1981-10-17'}, {'first_name': 'Isabella', 'last_name': 'Rossi', 'dob': '1998-08-06'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RF9ICL'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'RF9ICL'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_ito_2309',
        instruction='You are Harper Ito, a gold member, booking a one-way economy flight from DTW to MSP on 2024-05-20 for yourself and two companions, Yara Jackson and Evelyn Davis, because of changed travel plans. You prefer a flight in the afternoon, as flight HAT254 departs around 15:00, and you want to include 3 total bags with no charge and no insurance. You prefer to pay using your credit card ending in 7986. Later, you would like to cancel your original reservation N76PP0 for the business-class one-way flight from JFK to ORD on 2024-05-27, as those plans have been revised, and you prefer the refund to be issued back to your credit card ending in 7986.\n\nUse harper_ito_2309 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'DTW', 'destination': 'MSP', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'MSP', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'harper_ito_2309', 'origin': 'DTW', 'destination': 'MSP', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT254', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Harper', 'last_name': 'Ito', 'dob': '1984-03-23'}, {'first_name': 'Yara', 'last_name': 'Jackson', 'dob': '1997-05-05'}, {'first_name': 'Evelyn', 'last_name': 'Davis', 'dob': '1957-02-07'}], 'payment_methods': [{'payment_id': 'credit_card_1330512', 'amount': 303}], 'total_baggages': 3, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'MCO2H9', 'passengers': [{'first_name': 'Harper', 'last_name': 'Ito', 'dob': '1984-03-23'}, {'first_name': 'Yara', 'last_name': 'Jackson', 'dob': '1997-05-05'}, {'first_name': 'Evelyn', 'last_name': 'Davis', 'dob': '1957-02-07'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'N76PP0'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'N76PP0'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_sanchez_5251',
        instruction="You are assisting Anya Sanchez (user_id: anya_sanchez_5251) with a request following the cancellation of her business class flight from DFW to LAX on 2024-05-12 (reservation KDNMCS). You want to request a compensation certificate for the inconvenience caused by the cancellation. Later, you would like to explore new flight options from DFW to LAX on 2024-05-16. You prefer a one-stop itinerary if necessary, and the only available option is flight HAT170 departing DFW at 03:00 AM and arriving in LAX at 06:00 AM. You are open to booking this flight if it aligns with the passenger's schedule.\n\nUse anya_sanchez_5251 for authentication.",
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'anya_sanchez_5251', 'amount': 100}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DFW', 'destination': 'LAX', 'date': '2024-05-16'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DFW', 'destination': 'LAX', 'date': '2024-05-16'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_rossi_9652',
        instruction='You are to cancel the one-way economy reservation BVO68R for Fatima Rossi, Yara Kovacs, and Mei Moore from SFO to DEN via PHL on 2024-05-20, as plans have changed. After cancellation, you would like to explore rebooking options for a direct flight from SFO to PHX on the same date; however, no direct flights are currently available on that route and date. You prefer to be notified if any SFO to PHX flights become available for booking on 2024-05-20, and you would like to consider economy class options if they appear.\n\nUse fatima_rossi_9652 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'BVO68R'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'PHX', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_gonzalez_7490',
        instruction='You are Raj Gonzalez, and you want to cancel your existing basic economy one-way reservation QFIIFC from BOS to JFK via SEA on 2024-05-28, which is eligible for cancellation due to insurance coverage. You would like the refund processed back to your Mastercard ending in 9177. After that, you would like to explore direct flight options from BOS to MCO on 2024-05-20 in economy or business class. You prefer a flight departing either between 04:00 and 04:30 or between 23:00 and 23:30, as these are the available direct options to Orlando.\n\nUse raj_gonzalez_7490 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'QFIIFC'}),
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'MCO', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_thomas_9373',
        instruction="You are assisting Lucas Thomas (lucas_thomas_9373) with his travel requests. You want to search for one-stop flight options from MIA to JFK on 2024-05-20 because he was exploring alternative travel plans. Later, you will process the cancellation of reservation MIC7D1, which was for a business class one-way flight from MIA to JFK on 2024-05-10 for passenger Amelia Nguyen, because the flight (HAT292) was cancelled. After that, you would like to issue a compensation certificate for $100 because the flight disruption entitles the passenger to compensation under the airline's policy.\n\nUse lucas_thomas_9373 for authentication.",
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'MIA', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MIA', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'MIC7D1'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'MIC7D1'}),
            Action(name='send_certificate', kwargs={'user_id': 'lucas_thomas_9373', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_thomas_8641',
        instruction='You are Harper Thomas (harper_thomas_8641), and you want to review your existing round-trip business class reservation TV8G38 from BOS to DEN via MIA on 2024-05-20. You are considering rebooking to a simpler itinerary and would prefer direct flights if available over one-stop options on the same route and date. You would like to book a new one-way economy flight from BOS to MCO on 2024-05-20, specifically the evening flight (departing at 19:00), for passenger Harper Thomas (DOB 1991-03-20), with 1 checked bag and no insurance, and you prefer to pay using your credit card ending in 2008. After that, you would like to receive a compensation certificate due to the inconvenience caused by the change in travel plans. Later, you want to cancel your original reservation TV8G38 and have the refund processed back to the same credit card ending in 2008.\n\nUse harper_thomas_8641 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'TV8G38'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'BOS', 'destination': 'DEN', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'harper_thomas_8641', 'origin': 'BOS', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT013', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Harper', 'last_name': 'Thomas', 'dob': '1991-03-20'}], 'payment_methods': [{'payment_id': 'credit_card_5794036', 'amount': 100}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'harper_thomas_8641', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'TV8G38'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_sanchez_3298',
        instruction='You are assisting Chen Sanchez (user_id: chen_sanchez_3298) with canceling their existing round-trip business class reservation WNVCCD from SFO to JFK due to changed plans. After cancellation, you want to find flight options for a new trip on 2024-05-20. First, you would like a direct flight from SFO to PHL on 2024-05-20 in the early morning, as there is one available option (flight HAT074 at 05:00 AM). Later, you will explore one-stop itineraries from SFO to LGA on the same date; however, no such connecting flights are currently available. The passengers on the original reservation are Yara Patel and Liam Kovacs, and their details should be carried forward if rebooking. You prefer to use the payment method on file for any new bookings.\n\nUse chen_sanchez_3298 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'WNVCCD'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'PHL', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_khan_5280',
        instruction='You are to cancel the entire reservation 5J5H6S for Amelia Khan and Olivia Khan, which includes a one-way journey from MCO to SFO via PHX on May 16 and 17, 2024, because their travel plans have changed. You want the cancellation processed promptly since no flights have been taken and the reservation is eligible for a full refund. You prefer the refund to be issued back to the original payment method, which was a gift card, as this ensures proper recovery of funds used for the booking.\n\nUse amelia_khan_5280 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '5J5H6S'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '5J5H6S'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_nguyen_6045',
        instruction='You are assisting Ethan Nguyen with his travel plans. You want to book a direct flight from LGA to PHL on 2024-05-20 in economy class for one passenger (Ethan Nguyen), preferring an early morning departure around 03:00 AM, as flight HAT029 is available and fits his schedule. You prefer to pay using his Visa card ending in 3303. After that, you would like to cancel reservation L1QGWV, which is a round-trip from LGA to PHL, and request a refund to the same card, as the outbound leg was rescheduled and the return is no longer needed. You also want to request a compensation certificate for the delay experienced on reservation UDIGI7, where the first leg (HAT272 from LGA to CLT) was delayed on 2024-05-15, causing travel disruption. Later, you would like to explore one-stop flight options from LGA to PHL on 2024-05-21 for future planning, particularly interested in overnight or early morning connections, such as those involving a stop in CLT or PHX, to evaluate alternative travel times.\n\nUse ethan_nguyen_6045 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ethan_nguyen_6045', 'origin': 'LGA', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT029', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Smith', 'dob': '1953-07-21'}], 'payment_methods': [{'payment_id': 'credit_card_8005628', 'amount': 135}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'L1QGWV'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'L1QGWV'}),
            Action(name='send_certificate', kwargs={'user_id': 'ethan_nguyen_6045', 'amount': 50}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-21'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam_lee_5870',
        instruction='You are assisting Liam Lee, who initially wanted to search for one-stop flights from JFK to LAX on 2024-05-20, but due to unavailability, shifted focus to direct flights on the same route. When no direct flights to LAX were found, you want to book a direct alternative: a flight from JFK to SFO on 2024-05-20 for three passengers—Liam Lee, Raj Hernandez, and Sofia Jackson—in economy class. The preferred flight departs in the afternoon, as flight HAT023 is scheduled to leave JFK around 14:00. You prefer to include one checked bag for the group and decline travel insurance. You want to use the credit card ending in 8261 for payment, as it is the preferred method on file.\n\nUse liam_lee_5870 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'liam_lee_5870', 'origin': 'JFK', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Liam', 'last_name': 'Lee', 'dob': '1972-11-06'}, {'first_name': 'Raj', 'last_name': 'Hernandez', 'dob': '1964-07-10'}, {'first_name': 'Sofia', 'last_name': 'Jackson', 'dob': '1964-10-10'}], 'payment_methods': [{'payment_id': 'credit_card_1015550', 'amount': 573}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_ahmed_2248',
        instruction='You are Fatima Ahmed, and you want to cancel your existing round-trip reservation from CLT to IAH (reservation GIVSHB) due to a change in plans. You would like to book a new one-way flight from CLT to BOS on 2024-05-29 for two passengers, Mohamed Johansson and Lucas Kovacs, in economy class, specifically flight HAT216 which departs early in the morning, because it fits your revised travel schedule. You prefer to pay using your credit card ending in 7228 (credit_card_2531738) for this new booking. Later, you would like to receive a compensation certificate for the inconvenience caused by the cancellation of reservation GIVSHB. After that, you want to update your existing reservation LKCF2D to change your itinerary: you prefer to fly from JFK to SEA on 2024-05-18 on flight HAT083, followed by a connecting flight from SEA to DFW on the same day via flight HAT221, both in economy class, to better align with your updated schedule, and you would like any fare difference charged to your credit card ending in 5667 (credit_card_2531738).\n\nUse fatima_ahmed_2248 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GIVSHB'}),
            Action(name='book_reservation', kwargs={'user_id': 'fatima_ahmed_2248', 'origin': 'CLT', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT216', 'date': '2024-05-29'}], 'passengers': [{'first_name': 'Mohamed', 'last_name': 'Johansson', 'dob': '1996-08-19'}, {'first_name': 'Lucas', 'last_name': 'Kovacs', 'dob': '1957-10-27'}], 'payment_methods': [{'payment_id': 'credit_card_2531738', 'amount': 368}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'fatima_ahmed_2248', 'amount': 200}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'LKCF2D'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'LKCF2D', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT083', 'date': '2024-05-18'}, {'flight_number': 'HAT221', 'date': '2024-05-18'}], 'payment_id': 'credit_card_2531738'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei_rossi_4874',
        instruction='You are assisting Lei Rossi, who wants to book a new one-way flight for herself and her companion Liam Brown from IAH to SFO on 2024-05-20 in economy class with no checked bags and no insurance, preferring the early morning flight (HAT180) due to schedule alignment. You prefer to use her Visa card ending in 7279 for payment. After that, you want to cancel her existing reservation H0HHXO for a one-way basic economy flight from IAH to EWR on 2024-05-28, which includes insurance and is eligible for cancellation, and you need the details of that reservation for record-keeping. Later, you would like to explore one-stop flight options from IAH to EWR on 2024-05-28 for future travel planning. Additionally, you are requesting compensation for a previously cancelled flight under reservation 15EN70, which involved two passengers and qualifies for a travel certificate.\n\nUse lei_rossi_4874 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'lei_rossi_4874', 'origin': 'IAH', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT180', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lei', 'last_name': 'Rossi', 'dob': '1986-11-21'}, {'first_name': 'Liam', 'last_name': 'Brown', 'dob': '2000-01-10'}], 'payment_methods': [{'payment_id': 'credit_card_9623492', 'amount': 248}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'H0HHXO'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'H0HHXO'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'EWR', 'date': '2024-05-28'}),
            Action(name='send_certificate', kwargs={'user_id': 'lei_rossi_4874', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_hernandez_5188',
        instruction='You are Mohamed Hernandez, managing reservation 35V5SM for a business class round-trip from LAX to SFO, with the outbound flight on 2024-05-24. You want to review the details of your current booking, which includes passenger Yusuf Lee on flight HAT155 departing LAX in the evening. You would like to compare this option with other available flights on the same route and date to evaluate alternatives. You are interested in seeing both direct and one-stop flight options from LAX to SFO on 2024-05-24, particularly noting departure times, cabin availability, and pricing, so you can decide whether to keep your current reservation or change it. Since HAT155 is the only direct flight available on that date, you are open to reviewing one-stop itineraries that may offer better timing or value, even though they involve a connection.\n\nUse mohamed_hernandez_5188 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '35V5SM'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAX', 'destination': 'SFO', 'date': '2024-05-24'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAX', 'destination': 'SFO', 'date': '2024-05-24'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction="You are assisting Ivan Taylor (user_id: ivan_taylor_6615) with two requests. First, you want to update reservation AMZ5SS for Ivan Taylor, Liam Wilson, and Sophia Sanchez to change their itinerary from JFK to DFW via ATL on 2024-05-18 to instead fly from JFK to IAH on HAT279 and then from IAH to LAS on HAT286, both on 2024-05-18, while keeping the cabin in business class. This change is preferred because it aligns with the customer's updated travel plans. You prefer the flight from JFK to IAH in the morning (departing at 11:00) and the connecting flight from IAH to LAS in the late evening (departing at 22:00), both on the same day. You prefer to charge any fare difference to the credit card ending in 1656, which is on file. Later, you would like to request a compensation certificate for $200 due to the cancellation of reservation 06K2QN, which affected two passengers (Ivan Taylor and Ivan Jackson) on a previously booked one-way flight from ATL to LAS on 2024-05-08.\n\nUse ivan_taylor_6615 for authentication.",
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'AMZ5SS'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'AMZ5SS', 'cabin': 'business', 'flights': [{'flight_number': 'HAT279', 'date': '2024-05-18'}, {'flight_number': 'HAT286', 'date': '2024-05-18'}], 'payment_id': 'credit_card_1885633'}),
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia_santos_2092',
        instruction='You are Mia Santos, and you want to reconfirm your business class round-trip reservation AHVHPP for peace of mind, specifically flight HAT284 from LAS to PHX on 2024-05-26 and return flight HAT173 from PHX to LAS on 2024-05-29, with both flights remaining unchanged. You prefer this update to be processed using your credit card ending in 2705 for any potential charges. Later, you would like to request a compensation certificate for the delays experienced on your basic economy round-trip reservation 4NXSCL, which included delayed flights HAT240 (DTW to JFK), HAT136 (JFK to ATL) on 2024-05-15, and HAT020 (ORD to DTW) on 2024-05-20, as these disruptions affected your travel plans.\n\nUse mia_santos_2092 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'AHVHPP'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'AHVHPP', 'cabin': 'business', 'flights': [{'flight_number': 'HAT284', 'date': '2024-05-26'}, {'flight_number': 'HAT173', 'date': '2024-05-29'}], 'payment_id': 'credit_card_5606648'}),
            Action(name='send_certificate', kwargs={'user_id': 'mia_santos_2092', 'amount': 50}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james_santos_9046',
        instruction="You are assisting James Santos and Mei Lopez with three sequential requests. First, you want to book a one-way flight from JFK to SFO on 2024-05-20 in the afternoon for two passengers, Sofia Johnson and Isabella Khan, in economy class, with 2 total baggage items included at no extra cost, because these are his companions and he prefers to use his Visa ending in 5993 for payment. Later, you will process a request for Mei Lopez to receive a compensation certificate because her business class one-way reservation J6IHJ0 from JFK to CLT was cancelled. After that, you would like to update James Santos's existing reservation 5GAZGX by correcting the passenger name from Ethan Johansson to Ethan Johnson (DOB 1989-01-12) and adding one checked bag, increasing total_baggages to 2 with one paid bag, because he wants accurate passenger details and additional luggage for the trip, and he prefers to charge the bag fee to his Visa ending in 5993.\n\nUse james_santos_9046 for authentication.",
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'james_santos_9046', 'origin': 'JFK', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Sofia', 'last_name': 'Johnson', 'dob': '1959-07-16'}, {'first_name': 'Isabella', 'last_name': 'Khan', 'dob': '1964-03-10'}], 'payment_methods': [{'payment_id': 'credit_card_6899560', 'amount': 382}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'mei_lopez_9471', 'amount': 100}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '5GAZGX'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '5GAZGX', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_6899560'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '5GAZGX', 'passengers': [{'first_name': 'James', 'last_name': 'Santos', 'dob': '1956-12-09'}, {'first_name': 'Ethan', 'last_name': 'Johnson', 'dob': '1989-01-12'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_anderson_9682',
        instruction='You are Isabella Anderson, and you want to book a direct evening flight from CLT to DTW on 2024-05-20 for yourself and Lei Kim because you found flight HAT167 available and suitable for your schedule. You prefer to book it in economy class and pay using your Visa card ending in 7228, which is on file. Later, you would like to upgrade your existing round-trip reservation from CLT to ORD (with connections via PHL and DEN) to business class for all flights on 2024-05-18 (outbound) and 2024-05-26 (return), using the same payment method, to ensure comfort on this leg of your travel. After that, you want to cancel your earlier business class one-way reservation I5QZWG from LAX to CLT, as your plans have changed. Subsequently, you would like to explore one-stop flight options from LAX to CLT on 2024-05-21, as you are now considering alternative routing for that segment of your trip.\n\nUse isabella_anderson_9682 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'isabella_anderson_9682', 'origin': 'CLT', 'destination': 'DTW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT167', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Isabella', 'last_name': 'Anderson', 'dob': '1967-09-24'}, {'first_name': 'Lei', 'last_name': 'Kim', 'dob': '1979-03-16'}], 'payment_methods': [{'payment_id': 'credit_card_3277516', 'amount': 332}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'U898WZ', 'cabin': 'business', 'flights': [{'flight_number': 'HAT205', 'date': '2024-05-18'}, {'flight_number': 'HAT197', 'date': '2024-05-18'}, {'flight_number': 'HAT238', 'date': '2024-05-26'}, {'flight_number': 'HAT143', 'date': '2024-05-26'}], 'payment_id': 'credit_card_3277516'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'I5QZWG'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAX', 'destination': 'CLT', 'date': '2024-05-21'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma_taylor_2700',
        instruction='You are Emma Taylor, and you want to explore one-stop flight options from CLT to PHL on 2024-05-26 to find a better departure time, but no viable same-day connecting flights are available. Later, you would like to upgrade the cabin class for your return flight from PHL to CLT on 2024-05-27 (flight HAT016) from economy to business class for all three passengers—Emma Taylor, Harper Patel, and Raj Jackson—because you prefer more comfort on the return leg. You prefer to use your Mastercard ending in 4384 for any additional charges associated with the upgrade.\n\nUse emma_taylor_2700 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'PHL', 'date': '2024-05-26'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'PHL', 'date': '2024-05-26'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'G6YKB9'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'G6YKB9', 'cabin': 'business', 'flights': [{'flight_number': 'HAT205', 'date': '2024-05-26'}, {'flight_number': 'HAT016', 'date': '2024-05-27'}], 'payment_id': 'credit_card_5778461'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_wilson_5739',
        instruction='You are Mohamed Wilson (mohamed_wilson_5739) with reservation 5EU2LL, and you want to change your outbound journey from JFK to DFW on 2024-05-26 to fly via Seattle instead of Atlanta. You prefer a one-stop business class itinerary on that date, departing JFK early morning on flight HAT083 to SEA, followed by an afternoon connection on flight HAT037 from SEA to DFW, because it aligns with your revised travel plans. You want to keep the original return flights HAT222 and HAT021 on 2024-05-30 in business class. You prefer any fare difference to be charged to your credit card ending in 1211, as it is your preferred payment method on file.\n\nUse mohamed_wilson_5739 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'DFW', 'date': '2024-05-26'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'DFW', 'date': '2024-05-26'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '5EU2LL'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '5EU2LL', 'cabin': 'business', 'flights': [{'flight_number': 'HAT083', 'date': '2024-05-26'}, {'flight_number': 'HAT037', 'date': '2024-05-26'}, {'flight_number': 'HAT222', 'date': '2024-05-30'}, {'flight_number': 'HAT021', 'date': '2024-05-30'}], 'payment_id': 'credit_card_7921410'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf_kovacs_9564',
        instruction='You are Yusuf Kovacs, and you want to cancel your existing one-way economy reservation ZS5PID from BOS to DTW via CLT on 2024-05-17 due to a change in plans. After that, you would like to search for alternative travel options from BOS to DTW on 2024-05-20. You prefer a direct flight on that date; however, if no direct flights are available, you are open to one-stop itineraries. Based on current availability, there are no direct or connecting flights from BOS to DTW on 2024-05-20, so no suitable alternatives are currently bookable.\n\nUse yusuf_kovacs_9564 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'ZS5PID'}),
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'BOS', 'destination': 'DTW', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_li_2415',
        instruction='You are Amelia Li (amelia_li_2415) and you want to cancel your reservation NUCNX0 for a one-way business-class trip from IAH to PHL via ORD on 2024-05-16 because your plans have changed, and you prefer a full refund to your Visa card ending in 4846. After that, you would like to explore new travel options and want to book a direct business-class flight from IAH to JFK on 2024-05-20. You prefer an early morning flight, as the only available direct business option departs around 06:00 AM. You also requested to check one-stop itineraries on the same route and date in case of better times or pricing, but no viable one-stop flights from IAH to JFK were found.\n\nUse amelia_li_2415 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'NUCNX0'}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'JFK', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei_thomas_8446',
        instruction='You are to assist Mei Thomas in rebooking her trip due to a schedule conflict. You want to book a round-trip in business class from LAS to IAH on 2024-05-20 for two passengers: Fatima Patel and Sofia Brown, with a one-stop itinerary via PHX, because she found a viable connection that better fits her schedule. The outbound should be a morning flight from LAS to PHX (HAT242, departing 11:00) connecting to a mid-afternoon flight from PHX to IAH (HAT152, departing 15:00), both on 2024-05-20, to ensure a feasible connection with sufficient layover. After booking, you will update the passenger list to replace Sofia Brown with Mei Thomas, as the name was entered incorrectly. Then, you would like to confirm the updated flights are in business class and process any fare difference using the same credit card ending in 4779, which is her preferred payment method. Finally, you need to cancel the original reservation W4QNKQ, as it is no longer needed following the successful rebooking.\n\nUse mei_thomas_8446 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mei_thomas_8446', 'origin': 'LAS', 'destination': 'IAH', 'flight_type': 'round_trip', 'cabin': 'business', 'flights': [{'flight_number': 'HAT284', 'date': '2024-05-20'}, {'flight_number': 'HAT152', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Fatima', 'last_name': 'Patel', 'dob': '1953-12-13'}, {'first_name': 'Sofia', 'last_name': 'Brown', 'dob': '1988-09-02'}], 'payment_methods': [{'payment_id': 'credit_card_6784407', 'amount': 1712}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'W4QNKQ', 'passengers': [{'first_name': 'Fatima', 'last_name': 'Patel', 'dob': '1953-12-13'}, {'first_name': 'Mei', 'last_name': 'Thomas', 'dob': '1973-05-06'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'W4QNKQ', 'cabin': 'business', 'flights': [{'flight_number': 'HAT284', 'date': '2024-05-19'}, {'flight_number': 'HAT226', 'date': '2024-05-19'}, {'flight_number': 'HAT002', 'date': '2024-05-21'}, {'flight_number': 'HAT173', 'date': '2024-05-22'}], 'payment_id': 'credit_card_6784407'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'W4QNKQ'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'W4QNKQ'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_khan_4151',
        instruction='You are Isabella Khan, user_id isabella_khan_4151, and you want a compensation certificate for the cancelled business class flight from CLT to LGA on 2024-05-09 (reservation 8POIJI), as it disrupted your original travel plans. Later, you would like to book a new economy flight from CLT to LGA on 2024-05-20 for three passengers—Isabella Khan, Ivan Nguyen, and Raj Lopez—preferring the evening flight (HAT087 departing at 17:00) because it is the only available option on that date and aligns with your rebooking request, and you prefer to pay using your saved credit card ending in 3445 with 3 checked bags included and no insurance. After that, you would like to cancel your upcoming business class reservation RRMXPX for Mei Brown on the multi-leg trip from MIA to PHX on 2024-05-27 and 2024-05-28, and you prefer the refund to be issued back to the same credit card ending in 3445.\n\nUse isabella_khan_4151 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'isabella_khan_4151', 'amount': 300}),
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'isabella_khan_4151', 'origin': 'CLT', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT087', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Isabella', 'last_name': 'Khan', 'dob': '1954-07-18'}, {'first_name': 'Ivan', 'last_name': 'Nguyen', 'dob': '1952-05-06'}, {'first_name': 'Raj', 'last_name': 'Lopez', 'dob': '1953-05-18'}], 'payment_methods': [{'payment_id': 'credit_card_4651498', 'amount': 588}], 'total_baggages': 3, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RRMXPX'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'RRMXPX'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_thomas_9373',
        instruction='You are Lucas Thomas, and you want a compensation certificate for the cancelled MIA to JFK flight on 2024-05-10 (reservation MIC7D1) due to the inconvenience caused. Later, you would like to cancel your upcoming one-way economy reservation NYHIHA from MIA to DTW via ORD on 2024-05-23–24, which includes two passengers (Lucas Thomas and Daiki Ahmed) and is eligible for cancellation with insurance, and you prefer the refund to be issued back to your Mastercard ending in 9916.\n\nUse lucas_thomas_9373 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'lucas_thomas_9373', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'NYHIHA'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_li_4016',
        instruction='You are assisting Ethan Li (ethan_li_4016), a gold member, with multiple travel requests. First, you want to book a one-way economy flight from JFK to ATL on 2024-05-20, specifically flight HAT057 departing in the early morning, for one passenger, and charge it to his Visa card ending in 5735. Later, you need to cancel his existing round-trip reservation QE1WXY from JFK to SFO due to a schedule conflict. After that, for his one-way reservation 9WQ9ND from DFW to BOS on 2024-05-24, you would like to update the passenger list by removing Juan Silva and adding Ivan Kovacs, who is a saved passenger, and add one checked bag to the reservation, charging the baggage fee to the same Visa card ending in 5735. Finally, you would like to request a compensation certificate for a recent flight delay he experienced, as he is entitled to recognition for the inconvenience.\n\nUse ethan_li_4016 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'ATL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ethan_li_4016', 'origin': 'JFK', 'destination': 'ATL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT057', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ethan', 'last_name': 'Li', 'dob': '1979-02-28'}], 'payment_methods': [{'payment_id': 'credit_card_3129816', 'amount': 141}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'QE1WXY'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'QE1WXY'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '9WQ9ND', 'passengers': [{'first_name': 'Ethan', 'last_name': 'Li', 'dob': '1979-02-28'}, {'first_name': 'Ivan', 'last_name': 'Kovacs', 'dob': '1996-09-18'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '9WQ9ND', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3129816'}),
            Action(name='send_certificate', kwargs={'user_id': 'ethan_li_4016', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar_ahmed_3737',
        instruction='You are Omar Ahmed (omar_ahmed_3737) and you want to search for and book a direct one-way flight from BOS to MCO on 2024-05-20 for yourself and Mohamed Sanchez. You would like to book flight HAT145 departing in the afternoon (at 16:00) in economy class for two passengers, and you prefer to pay using your Visa card ending in 4348. After that, you want to update your existing reservation 5XUJ32 (BOS to DFW on 2024-05-11, business class) to different flights on the same route and date, using the same card for any fare difference. Later, you decide to cancel reservation 5XUJ32 instead of updating it. Before the cancellation, you would like to correct the passenger name from Mohamed Sanchez to Mohamed Smith (DOB 1979-02-27) and add one checked bag to the reservation, increasing total_baggages to 5 and nonfree_baggages to 1, with the fee charged to your Visa card ending in 4348. After the cancellation, you would like to receive a compensation certificate as reimbursement for the cancelled trip.\n\nUse omar_ahmed_3737 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'omar_ahmed_3737', 'origin': 'BOS', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT145', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Omar', 'last_name': 'Ahmed', 'dob': '1985-04-26'}, {'first_name': 'Mohamed', 'last_name': 'Sanchez', 'dob': '1979-02-27'}], 'payment_methods': [{'payment_id': 'credit_card_1333905', 'amount': 320}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '5XUJ32', 'cabin': 'business', 'flights': [{'flight_number': 'HAT006', 'date': '2024-05-11'}, {'flight_number': 'HAT117', 'date': '2024-05-11'}], 'payment_id': 'credit_card_1333905'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '5XUJ32'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '5XUJ32'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '5XUJ32', 'passengers': [{'first_name': 'Omar', 'last_name': 'Ahmed', 'dob': '1985-04-26'}, {'first_name': 'Mohamed', 'last_name': 'Smith', 'dob': '1979-02-27'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '5XUJ32', 'total_baggages': 5, 'nonfree_baggages': 1, 'payment_id': 'credit_card_1333905'}),
            Action(name='send_certificate', kwargs={'user_id': 'omar_ahmed_3737', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_moore_2190',
        instruction='You are Mohamed Moore, a regular customer, traveling with your companion Lucas Jackson on a one-way trip from Newark (EWR) to Los Angeles (LAX) on 2024-05-20. You want to book a direct morning economy flight, specifically HAT041, because it fits your preferred departure time and route. You are booking for two passengers and initially request one checked bag. After booking, you would like to update your reservation to include a second checked bag, making one bag non-free, because you need additional luggage. You prefer to pay for both the initial booking and the additional baggage fee using your Mastercard ending in 4721, which is already on file.\n\nUse mohamed_moore_2190 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'EWR', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mohamed_moore_2190', 'origin': 'EWR', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT041', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mohamed', 'last_name': 'Moore', 'dob': '1995-06-06'}, {'first_name': 'Lucas', 'last_name': 'Jackson', 'dob': '1989-06-28'}], 'payment_methods': [{'payment_id': 'credit_card_6369550', 'amount': 392}, {'payment_id': 'credit_card_6369550', 'amount': 50}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'HATHAT', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_6369550'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf_gonzalez_6436',
        instruction='You are Yusuf Gonzalez, and you want to book a one-way flight from PHL to LGA on 2024-05-20 for yourself and Mohamed Wilson in economy class, with no checked bags, no insurance, and payment using your Visa card ending in 6613, because you are rebooking new travel plans. Later, you want to cancel your existing one-way reservation USJI8D from ATL to LAX for Mohamed Wilson and Lei Hernandez due to changed plans, and you would like a compensation certificate issued as a result of this cancellation. After that, you want to confirm the business class upgrade on your round-trip reservation DOBSMB from PHL to DEN and back, keeping the same flights HAT076 on 2024-05-23 and HAT158 on 2024-05-25 for yourself and Isabella Garcia, with any fare difference charged to your Visa card ending in 6613, because you prefer enhanced comfort for this trip.\n\nUse yusuf_gonzalez_6436 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'PHL', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'yusuf_gonzalez_6436', 'origin': 'PHL', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT096', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mohamed', 'last_name': 'Wilson', 'dob': '1981-11-04'}, {'first_name': 'Lei', 'last_name': 'Hernandez', 'dob': '1961-08-16'}], 'payment_methods': [{'payment_id': 'credit_card_8843042', 'amount': 344}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'USJI8D'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'DOBSMB', 'cabin': 'business', 'flights': [{'flight_number': 'HAT076', 'date': '2024-05-23'}, {'flight_number': 'HAT158', 'date': '2024-05-25'}], 'payment_id': 'credit_card_8843042'}),
            Action(name='send_certificate', kwargs={'user_id': 'yusuf_gonzalez_6436', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason_lee_6824',
        instruction='You are Mason Lee, a gold member, who wants to book a one-way flight from Newark (EWR) to Dallas (DFW) on 2024-05-20 in the afternoon in economy class, as flight availability and timing align with your spontaneous travel plans. You would like to add one free checked bag and decline travel insurance, as you prefer to keep the booking simple and cost-effective. You prefer to pay using your saved Mastercard ending in 4633, which is already on file for convenience.\n\nUse mason_lee_6824 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'EWR', 'destination': 'DFW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mason_lee_6824', 'origin': 'EWR', 'destination': 'DFW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT231', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mason', 'last_name': 'Lee', 'dob': '1983-11-18'}], 'payment_methods': [{'payment_id': 'credit_card_3147068', 'amount': 171}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_lopez_8637',
        instruction='You are to book a one-way direct flight from Houston (IAH) to Las Vegas (LAS) on 2024-05-20 for two passengers: Daiki Ito and Olivia Santos, using saved passenger details. You want to book flight HAT112 because it matches the requested route and departure time, with a late evening departure at 10:00 PM. The booking should be in economy class with 2 checked bags included at no extra cost and no travel insurance. You prefer to pay using your Mastercard ending in 1830 on file.\n\nUse anya_lopez_8637 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'anya_lopez_8637', 'origin': 'IAH', 'destination': 'LAS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT112', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Ito', 'dob': '1993-09-04'}, {'first_name': 'Olivia', 'last_name': 'Santos', 'dob': '1961-07-04'}], 'payment_methods': [{'payment_id': 'credit_card_9701690', 'amount': 302}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_kovacs_8102',
        instruction='You are Raj Kovacs, a regular customer, and you want to update your reservation O8IHB3 to include two checked bags for your upcoming one-way business class flight from PHL to SFO on 2024-05-26. You would like this confirmed at no charge, as business class includes complimentary baggage. You prefer to have your Mastercard ending in 5274 on file as a backup payment method in case any fees are incurred, even though none are expected.\n\nUse raj_kovacs_8102 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'O8IHB3'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'O8IHB3', 'total_baggages': 2, 'nonfree_baggages': 0, 'payment_id': 'credit_card_7320675'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia_patel_6859',
        instruction='You are updating the baggage for a reservation under user ID sophia_patel_6859 for passenger Anya Moore on a round-trip business class journey from DTW to MCO via MSP on 2024-05-26 and return on 2024-05-30. You want to add one checked bag to the reservation because business class includes two free bags and no additional charge will apply. You prefer to use your saved Mastercard ending in 7741 for any potential charges, though none are expected.\n\nUse sophia_patel_6859 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'V7KTOK'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'V7KTOK', 'total_baggages': 1, 'nonfree_baggages': 0, 'payment_id': 'credit_card_5278427'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan_moore_9091',
        instruction='You are Juan Moore (DOB: 1973-06-08) and you want to book a one-way flight from ORD to PHL on 2024-05-20 in the evening, specifically flight HAT271 departing at 7:00 PM, in economy class, because it fits your travel plans and is available. You prefer to pay using your Visa card ending in 3005. Later, you want to update your existing reservation S2QS9V by upgrading to business class and changing the return flight from DEN to ORD to the morning flight on 2024-05-20, specifically HAT105 departing at 8:00 AM, to better align with your schedule. You also prefer to use the same Visa card ending in 3005 for any fare difference. After updating the reservation, you would like to review the updated details of S2QS9V. Subsequently, you want to explore one-stop flight options from ORD to PHL on 2024-05-20 to compare with your newly booked direct flight.\n\nUse juan_moore_9091 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ORD', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'juan_moore_9091', 'origin': 'ORD', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT271', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Juan', 'last_name': 'Moore', 'dob': '1973-06-08'}], 'payment_methods': [{'payment_id': 'credit_card_1743355', 'amount': 185}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'S2QS9V', 'cabin': 'business', 'flights': [{'flight_number': 'HAT118', 'date': '2024-05-19'}, {'flight_number': 'HAT105', 'date': '2024-05-20'}], 'payment_id': 'credit_card_1743355'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'S2QS9V'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ORD', 'destination': 'PHL', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia_lopez_6592',
        instruction='You are Mia Lopez, and you want to book a new direct economy flight from Denver to Dallas on May 20th, 2024, departing in the afternoon (at 15:00), because it fits your updated travel plans. You are booking this for one passenger: Mia Lopez, with one total baggage and no insurance, and you prefer to pay using your credit card ending in 3305. Later, you want to update your existing reservation 9NN4K9 by changing your itinerary from Denver to New York on May 17th, 2024, to include a connection via Dallas instead of Miami: first, a flight from Denver to Dallas (DFW) on HAT246, followed by a business class flight from Dallas to Newark (EWR) on HAT142 in the evening (departing at 18:00), because this connection better suits your schedule. You prefer to use the same credit card ending in 3305 for any fare difference associated with the change.\n\nUse mia_lopez_6592 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'DEN', 'destination': 'DFW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mia_lopez_6592', 'origin': 'DEN', 'destination': 'DFW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT246', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mia', 'last_name': 'Lopez', 'dob': '1953-02-01'}], 'payment_methods': [{'payment_id': 'credit_card_9314282', 'amount': 107}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '9NN4K9', 'cabin': 'business', 'flights': [{'flight_number': 'HAT246', 'date': '2024-05-17'}, {'flight_number': 'HAT142', 'date': '2024-05-17'}], 'payment_id': 'credit_card_9314282'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '9NN4K9'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DEN', 'destination': 'JFK', 'date': '2024-05-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_wilson_8118',
        instruction='You are Lucas Wilson, and you want to book a new one-way flight from JFK to DTW on 2024-05-20 for two passengers, yourself and Mei Brown, in economy class, because you are planning a new trip. You prefer to use your Mastercard ending in 2989 for payment and to include two checked bags, both within the free allowance. Later, you want to cancel your existing reservation I6XC2H (MCO-PHX-MCO) due to a change in plans and request a refund to the same credit card. You also want to update your reservation RB76P6 to keep the current business class cabin but confirm the flights: HAT079 from JFK to ORD on 2024-05-23, HAT093 from ORD to ATL on 2024-05-30, and HAT233 from ATL to JFK later on 2024-05-30, and increase your baggage allowance to four total checked bags with one paid option, using the same payment method. After that, since the cancellation of I6XC2H was initiated by you, you would like to receive a compensation certificate as per policy.\n\nUse lucas_wilson_8118 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'lucas_wilson_8118', 'origin': 'JFK', 'destination': 'DTW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT092', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lucas', 'last_name': 'Wilson', 'dob': '1987-10-07'}, {'first_name': 'Mei', 'last_name': 'Brown', 'dob': '1962-04-07'}], 'payment_methods': [{'payment_id': 'credit_card_9240535', 'amount': 346}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'I6XC2H'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RB76P6'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'RB76P6', 'cabin': 'business', 'flights': [{'flight_number': 'HAT079', 'date': '2024-05-23'}, {'flight_number': 'HAT093', 'date': '2024-05-30'}, {'flight_number': 'HAT233', 'date': '2024-05-30'}], 'payment_id': 'credit_card_9240535'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'RB76P6', 'total_baggages': 4, 'nonfree_baggages': 1, 'payment_id': 'credit_card_9240535'}),
            Action(name='send_certificate', kwargs={'user_id': 'lucas_wilson_8118', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_garcia_8677',
        instruction='You are Harper Garcia (DOB 1998-02-27) and you want to book a one-way direct economy flight from ATL to ORD on 2024-05-23, specifically flight HAT227 departing midday, because you decided on a direct option after initially considering one-stop flights. You prefer to pay using your credit card ending in 6617 and include one free baggage without insurance. Later, you would like to update the passenger details in reservation CDXEBS by correcting Ivan Brown’s (DOB 1954-11-22) last name to Browne. After that, you would like to cancel your business class round-trip reservation 7IG5PW and receive a refund to the same credit card ending in 6617.\n\nUse harper_garcia_8677 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'ORD', 'date': '2024-05-23'}),
            Action(name='book_reservation', kwargs={'user_id': 'harper_garcia_8677', 'origin': 'ATL', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT227', 'date': '2024-05-23'}], 'passengers': [{'first_name': 'Harper', 'last_name': 'Garcia', 'dob': '1998-02-27'}], 'payment_methods': [{'payment_id': 'credit_card_5865555', 'amount': 200}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'CDXEBS'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'CDXEBS', 'passengers': [{'first_name': 'Harper', 'last_name': 'Garcia', 'dob': '1998-02-27'}, {'first_name': 'Ivan', 'last_name': 'Browne', 'dob': '1954-11-22'}]}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '7IG5PW'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma_johansson_6252',
        instruction='You are assisting Emma Johansson with rebooking travel for her companion Ava Anderson. You want to book a one-way, one-stop flight from SFO to LGA on 2024-05-20, with the first leg departing SFO in the early morning (flight HAT144) and the second leg departing PHX around noon (flight HAT081), both in economy class, because Ava needs to travel to New York on that date. You prefer to use the saved Visa card ending in 4149 for payment, as it was previously used and is on file. After confirming this new reservation, you would like to cancel the existing reservation MJ0YB6 for the same passenger from ORD to DFW on 2024-05-20, as the itinerary has changed and the flight is no longer needed. You prefer the refund to be issued back to the original payment method, the Visa card ending in 4149, to maintain consistency with prior transactions.\n\nUse emma_johansson_6252 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'emma_johansson_6252', 'origin': 'SFO', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT144', 'date': '2024-05-20'}, {'flight_number': 'HAT081', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ava', 'last_name': 'Anderson', 'dob': '1963-01-14'}], 'payment_methods': [{'payment_id': 'credit_card_4255859', 'amount': 233}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'MJ0YB6'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'MJ0YB6', 'passengers': [{'first_name': 'Ava', 'last_name': 'Anderson', 'dob': '1963-01-14'}]}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'MJ0YB6'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason_smith_9673',
        instruction="You are updating reservation 1ETKA7 for Mason Smyth's one-way trip from DEN to SFO on 2024-05-24, which includes a connection through PHL. You want to correct the passenger's last name from Smith to Smyth to ensure accurate identification. You also want to add one paid checked bag to the reservation, increasing the total to two bags with one being paid, because the current trip requires additional luggage. You prefer to charge the bag fee to your saved Mastercard ending in 9430, as it is your preferred payment method for reservation updates.\n\nUse mason_smith_9673 for authentication.",
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '1ETKA7'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '1ETKA7', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3008313'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '1ETKA7', 'passengers': [{'first_name': 'Mason', 'last_name': 'Smyth', 'dob': '1988-12-15'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_anderson_8280',
        instruction='You are updating reservation ZXIYE7 for Anya Anderson and companion Lei Martinez (corrected from Martin) traveling on a round-trip business class itinerary from MIA to JFK and DEN with return to MIA on 2024-05-25 and 2024-05-26. You want to increase the total checked baggage from 3 to 4, with 1 additional paid bag, because you need extra luggage for the trip. You prefer the baggage fee to be charged to your Visa card ending in 1550, as it is your preferred payment method on file.\n\nUse anya_anderson_8280 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'ZXIYE7'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'ZXIYE7', 'total_baggages': 4, 'nonfree_baggages': 1, 'payment_id': 'credit_card_1757702'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'ZXIYE7', 'passengers': [{'first_name': 'Anya', 'last_name': 'Anderson', 'dob': '1989-12-19'}, {'first_name': 'Lei', 'last_name': 'Martinez', 'dob': '1973-11-22'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia_gonzalez_2305',
        instruction='You are to first cancel the round-trip basic economy reservation Z7GOZK from EWR to IAH and back on 2024-05-28, as the travel plans have changed. Then, you want to book a one-way economy flight from EWR to LAX on 2024-05-17 for Olivia Gonzalez, departing in the early morning (flight HAT041 at 07:00 AM), because it is the only direct option available and matches the requested flight. After that, you would like to view the details of reservation K67C4W for a one-way flight from LAS to MCO on 2024-05-17, and then upgrade the entire reservation to business class on the same flight (HAT137) for all three passengers—Olivia Gonzalez, Mei Johansson, and Yara Lopez—because a more comfortable travel experience is preferred. You prefer to use your credit card ending in 9475 for any fare difference in both the new booking and the upgrade.\n\nUse olivia_gonzalez_2305 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'Z7GOZK'}),
            Action(name='book_reservation', kwargs={'user_id': 'olivia_gonzalez_2305', 'origin': 'EWR', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT041', 'date': '2024-05-17'}], 'passengers': [{'first_name': 'Olivia', 'last_name': 'Gonzalez', 'dob': '1988-06-13'}], 'payment_methods': [{'payment_id': 'credit_card_9969263', 'amount': 111}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_direct_flight', kwargs={'origin': 'EWR', 'destination': 'LAX', 'date': '2024-05-17'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'EWR', 'destination': 'LAX', 'date': '2024-05-17'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'K67C4W'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'K67C4W', 'cabin': 'business', 'flights': [{'flight_number': 'HAT137', 'date': '2024-05-17'}], 'payment_id': 'credit_card_9969263'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_taylor_8297',
        instruction='You are to first cancel the existing reservation RVEZA8 for Fatima Taylor from LAX to DEN via ORD, as the travel plans have changed. Then, you want to book a new one-way economy flight from LAX to EWR on 2024-05-20 for two passengers, Fatima Taylor and Emma Rossi, preferring the late evening direct flight option available on that date, because it is the only direct flight and aligns with the requested travel day. You prefer to use the Visa card ending in 1733 for this booking, as it is the designated payment method. Later, you would like to explore available flight options from LAX to EWR on 2024-05-20, including both direct and one-stop connections, to compare timing and pricing, even though only one direct flight is currently available. After that, you would like to update the business-class round-trip reservation NQD9KO for Fatima Taylor and Emma Rossi from ORD to ATL, adjusting the return flight if better options are found, and you prefer to use the Visa card ending in 1733 for any fare differences, ensuring continuity in payment method.\n\nUse fatima_taylor_8297 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'RVEZA8'}),
            Action(name='book_reservation', kwargs={'user_id': 'fatima_taylor_8297', 'origin': 'LAX', 'destination': 'EWR', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT012', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Fatima', 'last_name': 'Taylor', 'dob': '1983-02-04'}, {'first_name': 'Emma', 'last_name': 'Rossi', 'dob': '1971-10-26'}], 'payment_methods': [{'payment_id': 'credit_card_1366921', 'amount': 258}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAX', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAX', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'NQD9KO'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'NQD9KO', 'cabin': 'business', 'flights': [{'flight_number': 'HAT093', 'date': '2024-05-19'}, {'flight_number': 'HAT227', 'date': '2024-05-20'}], 'payment_id': 'credit_card_1366921'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_patel_1917',
        instruction='You are assisting Daiki Patel (user_id: daiki_patel_1917), who had a business class one-way flight from SFO to PHL on 2024-05-14 (reservation 0W60LB) cancelled, and as a result, you want to issue him a compensation certificate. Later, you would like to book a new one-way economy flight for Daiki Patel from SFO to BOS on 2024-05-20, specifically flight HAT026 departing in the afternoon, because it matches his requested flight and is available. You prefer to charge this booking to his credit card ending in 1765 (payment_id: credit_card_4327297). After that, you would like to cancel his existing round-trip reservation 7WKBKD from PHX to JFK and back, which was booked in business class with insurance and includes passengers Daiki Patel and Ethan Taylor, because he no longer needs it, and you prefer the refund to be issued back to the same credit card ending in 1765.\n\nUse daiki_patel_1917 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'daiki_patel_1917', 'amount': 100}),
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_patel_1917', 'origin': 'SFO', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT026', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Patel', 'dob': '1968-04-24'}], 'payment_methods': [{'payment_id': 'credit_card_4327297', 'amount': 161}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '7WKBKD'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '7WKBKD'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_sanchez_3298',
        instruction='You are Chen Sanchez (user_id: chen_sanchez_3298) and you want to cancel your round-trip business class reservation WNVCCD from SFO to JFK via IAH on 2024-05-17, which was not flown, due to a change in plans. After cancellation, you would like a compensation certificate for $200 (covering both passengers: Yara Patel and Liam Kovacs) to be issued and applied to your account. Subsequently, you want to rebook travel for the same two passengers from SFO to LAX on 2024-05-20. You prefer to see direct flight options, as no valid one-stop itineraries connect to LAX on that date. You are interested in evening flights, specifically around 20:00 or later, based on the available direct flights HAT163 (departing 20:00) and HAT257 (departing 22:00).\n\nUse chen_sanchez_3298 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'WNVCCD'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'WNVCCD'}),
            Action(name='send_certificate', kwargs={'user_id': 'chen_sanchez_3298', 'amount': 200}),
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'LAX', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are assisting Ivan Taylor (user_id: ivan_taylor_6615) regarding reservation 06K2QN for a cancelled one-way basic economy flight from ATL to LAS on 2024-05-08 for two passengers: Ivan Taylor and Ivan Jackson. You want to confirm the cancellation of this flight. You would like to receive a compensation certificate for the cancellation. Later, you would like to explore rebooking options for a future one-way trip from ATL to LAS on 2024-05-20. Since there are no direct flights available on that date, you are interested in one-stop connecting flight options. You prefer an early morning departure from ATL, such as around 02:00, with a connection through SEA or other hubs, arriving in LAS the same or following day. You are open to basic economy or higher cabin classes based on availability and total travel time.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '06K2QN'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '06K2QN'}),
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'LAS', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_garcia_6211',
        instruction='You are Evelyn Garcia, and your flight HAT195 from IAH to EWR on 2024-05-11 was cancelled, so you would like to receive a compensation certificate for this disruption. Later, you want to book a new direct flight for yourself and your travel companion Mei Lee from IAH to ORD on 2024-05-20 in economy class, preferring an early morning departure, as flight HAT116 departs at 08:00. You prefer to pay using your credit card ending in 3459, which is already on file.\n\nUse evelyn_garcia_6211 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_garcia_6211', 'amount': 200}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'evelyn_garcia_6211', 'origin': 'IAH', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT116', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Garcia', 'dob': '1967-04-08'}, {'first_name': 'Mei', 'last_name': 'Lee', 'dob': '1969-05-16'}], 'payment_methods': [{'payment_id': 'credit_card_4906704', 'amount': 358}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_hernandez_5188',
        instruction='You are Mohamed Hernandez (user_id: mohamed_hernandez_5188) and you want to cancel your existing business class round-trip reservation 35V5SM from LAX to SFO because you are changing your travel plans. After that, you would like to rebook a one-stop itinerary to Atlanta instead. You want to book a business class flight from LAX to ORD on 2024-05-20 in the evening (flight HAT030), followed by a connecting business class flight from ORD to ATL on 2024-05-21 in the early morning (flight HAT093), as these times work best for your schedule. You prefer to pay for the new booking and one checked baggage using your Mastercard ending in 7393, which is on file. You also want to ensure the passenger details for Yusuf Lee (DOB: 1951-07-12) are correctly updated in the new reservation.\n\nUse mohamed_hernandez_5188 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '35V5SM'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '35V5SM'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '35V5SM', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_5417084'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '35V5SM', 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Lee', 'dob': '1951-07-12'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '35V5SM', 'cabin': 'business', 'flights': [{'flight_number': 'HAT030', 'date': '2024-05-20'}, {'flight_number': 'HAT093', 'date': '2024-05-21'}], 'payment_id': 'credit_card_5417084'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAX', 'destination': 'ATL', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are Ivan Taylor (ivan_taylor_6615) and you want to receive a $200 compensation certificate due to the cancellation of your flight HAT052 from ATL to LAS on 2024-05-08. You would like to book a new one-way flight from ATL to SEA on 2024-05-20 in economy class for two passengers: yourself (Ivan Taylor) and Alex Taylor (replacing the originally listed Ivan Jackson). You prefer this flight because it departs in the late evening, aligning with your updated travel plans. You want to pay using your Visa card ending in 1656, which is on file. Later, you would like to explore one-stop flight options from ATL to SFO on 2024-05-25, with a preference for the connecting itinerary via SEA (HAT239 followed by HAT274), as it is the only viable one-stop option available on that date with appropriate timing.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'SEA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'ATL', 'destination': 'SEA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT039', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Ivan', 'last_name': 'Jackson', 'dob': '1983-02-26'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 206}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'HATHAT', 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Alex', 'last_name': 'Taylor', 'dob': '1985-04-15'}]}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'SFO', 'date': '2024-05-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are assisting Ivan Taylor (user_id: ivan_taylor_6615), who had a previous reservation (06K2QN) from ATL to LAS on 2024-05-08 that was cancelled, as flight HAT052 was marked as cancelled on that date. Due to this cancellation, you want to request a compensation certificate. You then want to book a new one-way flight from ATL to ORD on 2024-05-20 for two passengers: Ivan Taylor (DOB: 1970-02-21) and Ivan Jackson (DOB: 1983-02-26), in economy class, with no baggage and no insurance. The preferred flight is HAT227, which departs ATL at 11:00 AM and arrives in ORD at 1:00 PM, because it matches the requested route, date, and cabin. You prefer to pay using the Visa card ending in 1656 on file. After booking, you want to cancel the new reservation immediately.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'ATL', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT227', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Ivan', 'last_name': 'Jackson', 'dob': '1983-02-26'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 210}, {'payment_id': 'credit_card_1885633', 'amount': -210}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'HATHAT'}),
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_khan_9974',
        instruction='You are assisting Fatima Khan, who wants to cancel her existing round-trip business class reservation BV2RJH from MCO to IAH via LAS due to changed plans, and have the refund processed to her Mastercard ending in 3471. Later, you are to book a new one-way business class flight for four passengers—Fatima Khan, Raj Li, Yara Brown, and Omar Anderson—from MCO to PHX on 2024-05-17, specifically on flight HAT153, which departs in the afternoon, and charge the same Mastercard ending in 3471. After booking, you are to add two additional checked bags, resulting in a total of six checked bags with two paid, and ensure the extra baggage fee is also charged to the same card.\n\nUse fatima_khan_9974 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'BV2RJH'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'BV2RJH'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MCO', 'destination': 'PHX', 'date': '2024-05-17'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MCO', 'destination': 'PHX', 'date': '2024-05-17'}),
            Action(name='book_reservation', kwargs={'user_id': 'fatima_khan_9974', 'origin': 'MCO', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT153', 'date': '2024-05-17'}], 'passengers': [{'first_name': 'Fatima', 'last_name': 'Khan', 'dob': '1989-01-01'}, {'first_name': 'Raj', 'last_name': 'Li', 'dob': '1967-11-10'}, {'first_name': 'Yara', 'last_name': 'Brown', 'dob': '1956-04-20'}, {'first_name': 'Omar', 'last_name': 'Anderson', 'dob': '1950-06-02'}], 'payment_methods': [{'payment_id': 'credit_card_6225387', 'amount': 1352}], 'total_baggages': 4, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'XMCPH6', 'total_baggages': 6, 'nonfree_baggages': 2, 'payment_id': 'credit_card_6225387'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_muller_1116',
        instruction='You are to first book a one-way flight from LAS to IAH on 2024-05-20 in the afternoon for Daiki Muller and Amelia Kim, traveling in economy class, with one checked baggage included and no insurance, charging the payment to the Visa card ending in 2135 on file. After that, you are to update the existing reservation 59XX6W for the LAS to ATL round-trip by changing the passenger Chen Muller to Omar Ito (DOB 1975-09-19) and adding one checked baggage (setting total_baggages=1 and nonfree_baggages=1), charging the baggage fee to the same Visa card ending in 2135.\n\nUse daiki_muller_1116 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_muller_1116', 'origin': 'LAS', 'destination': 'IAH', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT266', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Muller', 'dob': '1954-07-04'}, {'first_name': 'Amelia', 'last_name': 'Kim', 'dob': '1978-04-20'}], 'payment_methods': [{'payment_id': 'credit_card_2408938', 'amount': 284}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '59XX6W'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '59XX6W', 'passengers': [{'first_name': 'Daiki', 'last_name': 'Muller', 'dob': '1954-07-04'}, {'first_name': 'Omar', 'last_name': 'Ito', 'dob': '1975-09-19'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '59XX6W', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_2408938'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_johnson_4945',
        instruction='You are to book a one-way economy class flight for two passengers, Evelyn Johnson and Mia Lopez, from Chicago (ORD) to Philadelphia (PHL) on 2024-05-20. You prefer flight HAT271, which departs in the evening at 19:00, because it matches the requested flight and timing. You want to include two checked bags with no additional non-free charges and no travel insurance. You prefer to pay using your Mastercard ending in 4357.\n\nUse evelyn_johnson_4945 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ORD', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'evelyn_johnson_4945', 'origin': 'ORD', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT271', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Johnson', 'dob': '1960-07-04'}, {'first_name': 'Mia', 'last_name': 'Lopez', 'dob': '1994-07-05'}], 'payment_methods': [{'payment_id': 'credit_card_4313689', 'amount': 370}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'IZFHZ7'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'IZFHZ7', 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Johnson', 'dob': '1960-07-04'}, {'first_name': 'Mia', 'last_name': 'Lopez', 'dob': '1994-07-05'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'IZFHZ7', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_4313689'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam_lee_5870',
        instruction='You are assisting Liam Lee, who holds reservation ZW36O0 for a round-trip from LAX to SFO in business class with passengers Sofia Jackson and Raj Hernandez. You want to update the outbound flight from LAX to SFO to an earlier date, specifically on 2024-05-20, using flight HAT034, which departs in the early morning, to accommodate a schedule conflict. You prefer to keep the return flight HAT273 on 2024-05-24 unchanged, maintaining business class for all passengers. You prefer to pay any fare difference using your credit card ending in 8261.\n\nUse liam_lee_5870 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'ZW36O0'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'ZW36O0', 'cabin': 'business', 'flights': [{'flight_number': 'HAT034', 'date': '2024-05-20'}, {'flight_number': 'HAT273', 'date': '2024-05-24'}], 'payment_id': 'credit_card_1015550'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAX', 'destination': 'SFO', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_rossi_4467',
        instruction='You are Daiki Rossi, traveling with Sofia Silva, and you want to upgrade both flights in reservation NFFMYQ from economy to business class for added comfort. You want to upgrade flight HAT225 from Denver to Charlotte on 2024-05-24, which departs in the early morning, because you prefer a more comfortable experience on the outbound journey. Later, you want to upgrade flight HAT262 from Charlotte to Denver on 2024-05-26, which departs in the afternoon, for the same reason on the return leg. You prefer to use your credit card ending in 3402 for any additional charges associated with the upgrade.\n\nUse daiki_rossi_4467 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'NFFMYQ'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'NFFMYQ', 'cabin': 'business', 'flights': [{'flight_number': 'HAT225', 'date': '2024-05-24'}, {'flight_number': 'HAT262', 'date': '2024-05-26'}], 'payment_id': 'credit_card_7103786'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DEN', 'destination': 'CLT', 'date': '2024-05-24'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_patel_1045',
        instruction='You are Harper Patel, and you want to book a one-way one-stop flight for your passenger Daiki Moore from MIA to LAX via EWR. You prefer the first leg on 2024-05-20 in the late evening from MIA to EWR (flight HAT192), followed by a connection on 2024-05-21 in the early morning from EWR to LAX (flight HAT041), both in economy class, with one checked bag included at no extra cost. You want to pay using your Mastercard ending in 4111. Later, you want to cancel your original round-trip business class reservation HAGO8B from MIA to JFK, which was also for Daiki Moore, and have the refund processed back to the same card. After that, you would like to receive a compensation certificate for the canceled flight on reservation HAGO8B.\n\nUse harper_patel_1045 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'MIA', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'harper_patel_1045', 'origin': 'MIA', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT192', 'date': '2024-05-20'}, {'flight_number': 'HAT041', 'date': '2024-05-21'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Moore', 'dob': '1998-01-12'}], 'payment_methods': [{'payment_id': 'credit_card_5323638', 'amount': 243}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'HAGO8B'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'HAGO8B'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MIA', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'harper_patel_1045', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yara_patel_3784',
        instruction='You are Yara Patel, a silver member, and you want to book a one-way flight from LAX to DFW on 2024-05-20 in economy class for yourself, preferring an afternoon departure. You prefer to use your Visa card ending in 5696 for payment, as it is your primary credit card on file. After that, you would like to explore available one-stop flight options from LAX to ORD on the same date, 2024-05-20, to consider possibilities for another trip.\n\nUse yara_patel_3784 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '4WSQIE'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAX', 'destination': 'DFW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'yara_patel_3784', 'origin': 'LAX', 'destination': 'DFW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT022', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yara', 'last_name': 'Patel', 'dob': '1970-04-16'}], 'payment_methods': [{'payment_id': 'credit_card_5561400', 'amount': 103}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAX', 'destination': 'ORD', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf_johansson_6921',
        instruction='You are assisting Yusuf Johansson, who wants to first review his existing reservation CPIPWR for a one-way business class flight from SFO to LAX on 2024-05-27 for himself and Noah Nguyen. Then, you are to book a new one-way business class flight from SFO to BOS on 2024-05-20 for the same two passengers, Yusuf Johansson and Noah Nguyen, using his Mastercard ending in 9864, with no checked bags and no travel insurance. The preferred flight is HAT294, which departs SFO in the early morning. After that, you are to search for one-stop flight options from SFO to ORD on 2024-05-20 for potential future travel consideration, with the understanding that the only available option involves an overnight connection through IAH, arriving on 2024-05-21.\n\nUse yusuf_johansson_6921 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'CPIPWR'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'yusuf_johansson_6921', 'origin': 'SFO', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT294', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Johansson', 'dob': '1970-12-06'}, {'first_name': 'Noah', 'last_name': 'Nguyen', 'dob': '1986-12-07'}], 'payment_methods': [{'payment_id': 'credit_card_9880839', 'amount': 630}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'ORD', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_kovacs_8102',
        instruction='You are to cancel the existing reservation O8IHB3 for a business class one-way flight from PHL to SFO on 2024-05-26 for Raj Kovacs and Mason Sanchez, as the customer has decided to change plans. After that, you are to book a new one-way economy flight from PHL to CLT on 2024-05-20 for the same two passengers, specifically on flight HAT243, which departs overnight, because it fits their revised travel needs and is more affordable. You prefer to use the Mastercard ending in 5274 for the new booking.\n\nUse raj_kovacs_8102 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'O8IHB3'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHL', 'destination': 'CLT', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'PHL', 'destination': 'CLT', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'raj_kovacs_8102', 'origin': 'PHL', 'destination': 'CLT', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT243', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Raj', 'last_name': 'Kovacs', 'dob': '1981-05-20'}, {'first_name': 'Mason', 'last_name': 'Sanchez', 'dob': '1976-05-16'}], 'payment_methods': [{'payment_id': 'credit_card_7320675', 'amount': 398}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan_taylor_8806',
        instruction='You are Juan Taylor, and you want to book a new one-way business class flight from CLT to EWR on 2024-05-20 for one passenger, preferring the early morning flight option (HAT108) because it fits your schedule. You prefer to pay using your Mastercard ending in 2923. Later, you want to update your existing reservation 018BE2 to change your outbound journey from CLT to JFK on 2024-05-27 to a connecting itinerary via DTW, consisting of HAT176 from CLT to DTW and HAT240 from DTW to JFK, both in business class, because it offers a more convenient connection than your current booking. You would like any fare difference to be charged to the same Mastercard ending in 2923.\n\nUse juan_taylor_8806 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'CLT', 'destination': 'JFK', 'date': '2024-05-27'}),
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'juan_taylor_8806', 'origin': 'CLT', 'destination': 'EWR', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT108', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Chen', 'last_name': 'Lee', 'dob': '1959-04-10'}], 'payment_methods': [{'payment_id': 'credit_card_2217221', 'amount': 210}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '018BE2', 'cabin': 'business', 'flights': [{'flight_number': 'HAT176', 'date': '2024-05-27'}, {'flight_number': 'HAT240', 'date': '2024-05-27'}], 'payment_id': 'credit_card_2217221'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava_lopez_9068',
        instruction='You are Ava Lopez (user_id: ava_lopez_9068) arranging travel for her colleague Lei Santos. You want to book a one-way, one-stop flight from PHX to IAH via SFO on 2024-05-20, consisting of HAT009 from PHX to SFO in the late afternoon (departing around 17:00) and connecting to HAT082 from SFO to IAH in the evening (departing around 23:00), for one passenger in economy class with one free checked bag, because Lei Santos needs to attend a business meeting in Houston. You prefer to pay using the credit card ending in 8178 on file. Later, you also want to cancel your own reservation VE1ZC3 for a round-trip from PHX to MCO, originally booked for the same period, due to a conflicting prior commitment, and you would like to confirm the updated details after cancellation.\n\nUse ava_lopez_9068 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'PHX', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ava_lopez_9068', 'origin': 'PHX', 'destination': 'IAH', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT009', 'date': '2024-05-20'}, {'flight_number': 'HAT082', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lei', 'last_name': 'Santos', 'dob': '1973-01-10'}], 'payment_methods': [{'payment_id': 'credit_card_3688120', 'amount': 275}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'VE1ZC3'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'VE1ZC3'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_nguyen_6045',
        instruction='You are assisting Ethan Nguyen (user_id: ethan_nguyen_6045) who wants to book a one-way one-stop flight from LGA to LAS via PHX on 2024-05-20. You want to book flight HAT245 departing LGA at 00:00 (overnight) and connecting flight HAT027 departing PHX at 13:00 (early afternoon), both in economy class, for one passenger: Ethan Nguyen (DOB: 1970-04-28), because he has changed his travel plans. You prefer to include 1 total baggage with no non-free charges and no travel insurance, as per his selection. You prefer to pay using the credit card ending in 3303 (payment method on file), as it was his chosen payment method. Later, you would like to cancel the previous reservation L1QGWV, which was a round-trip from LGA to PHL, because it is no longer needed. You also want to review the details of that reservation before cancellation, to confirm its contents.\n\nUse ethan_nguyen_6045 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ethan_nguyen_6045', 'origin': 'LGA', 'destination': 'LAS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT245', 'date': '2024-05-20'}, {'flight_number': 'HAT027', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ethan', 'last_name': 'Nguyen', 'dob': '1970-04-28'}], 'payment_methods': [{'payment_id': 'credit_card_8005628', 'amount': 264}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'L1QGWV'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'L1QGWV'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_thomas_9373',
        instruction='You are Lucas Thomas, and you want a compensation certificate for the cancellation of your reservation MIC7D1 for a flight from MIA to JFK. Later, you would like to book a new one-way flight from MIA to JFK on 2024-05-25 for two passengers, yourself and Daiki Ahmed, in economy class, with no checked bags and no insurance. You prefer an afternoon flight, as it aligns with the only available direct option on that date. You prefer to pay using your Mastercard ending in 9094.\n\nUse lucas_thomas_9373 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'lucas_thomas_9373', 'amount': 100}),
            Action(name='book_reservation', kwargs={'user_id': 'lucas_thomas_9373', 'origin': 'MIA', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT224', 'date': '2024-05-25'}], 'passengers': [{'first_name': 'Lucas', 'last_name': 'Thomas', 'dob': '1972-02-07'}, {'first_name': 'Daiki', 'last_name': 'Ahmed', 'dob': '1965-12-15'}], 'payment_methods': [{'payment_id': 'credit_card_1382059', 'amount': 330}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava_garcia_2940',
        instruction='You are assisting Ava Garcia, who holds reservation 4SW7R4 for a round-trip from SFO to SEA. You want to update the return portion of the trip on 2024-05-16 by replacing the direct flight HAT258 from SEA to SFO with a one-stop itinerary: first, a flight from SEA to PHX in the afternoon (flight HAT236), followed by a late evening flight from PHX to SFO (flight HAT283), both in economy class, to accommodate a schedule preference. After that, you would like to add one checked bag to the new return itinerary, bringing the total to five checked bags with one non-free bag, and you prefer to pay the additional charge using the Visa card ending in 8815 on file. Later, due to ongoing schedule conflicts, you would like to cancel the entire reservation, including the updated return flights and all passengers: Olivia Thomas, Emma Khan, Mohamed Anderson, and the second Emma Khan.\n\nUse ava_garcia_2940 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '4SW7R4'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '4SW7R4', 'total_baggages': 5, 'nonfree_baggages': 1, 'payment_id': 'credit_card_4025240'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '4SW7R4', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT144', 'date': '2024-05-06'}, {'flight_number': 'HAT251', 'date': '2024-05-06'}, {'flight_number': 'HAT236', 'date': '2024-05-16'}, {'flight_number': 'HAT283', 'date': '2024-05-16'}], 'payment_id': 'credit_card_4025240'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '4SW7R4'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction='You are Noah Khan, and you want to book a one-way connecting flight from LAS to MCO on 2024-05-20 for your passenger Yusuf Ahmed, with a stop in ATL, because you need to travel to Orlando on that date. You prefer to use flight HAT077 from LAS to ATL in the early morning (departing at 05:00) and flight HAT010 from ATL to MCO in the evening (departing at 19:00), both in business class, to ensure a full day between connections and a convenient arrival. You want to pay with your Visa card ending in 9691, as it is your preferred payment method, and include one total baggage with no non-free charges and no insurance. After booking, you would like to review the details of your new reservation to confirm accuracy. Subsequently, you want to search for direct flight options from LAS to IAH on 2024-05-20, to explore alternatives for future reference. Later, you would like to request a compensation certificate for your previously cancelled business class flight from LAS to IAH on 2024-05-13 (reservation LUA6DF), as you are entitled to a $100 travel certificate for the disruption.\n\nUse noah_khan_8166 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_khan_8166', 'origin': 'LAS', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT077', 'date': '2024-05-20'}, {'flight_number': 'HAT010', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}], 'payment_methods': [{'payment_id': 'credit_card_5669132', 'amount': 618}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'Y1ZIDC', 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'Y1ZIDC'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'noah_khan_8166', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar_brown_9300',
        instruction='You are Omar Brown (omar_brown_9300) and you want to cancel your one-way economy reservation X4ZXW5 from SEA to LAS on 2024-05-16 because you no longer need that trip. Later, you would like to book a new one-way economy flight from SEA to SFO on 2024-05-20 in the afternoon, specifically flight HAT011 departing at 13:00, for two passengers: Chen Moore and Daiki Kim, with 2 free checked bags and no insurance, because you found this flight suitable and want to travel together. After that, you would like to update your existing round-trip basic economy reservation 3Y4GQ1 (JFK-LAS-SEA-JFK) to add 2 checked bags, increasing total_baggages from 0 to 2 and setting nonfree_baggages=2, because you now need baggage for this trip. You prefer all charges for these changes to be billed to your Visa card ending in 2094 (credit_card_4120592), as it is your preferred payment method on file.\n\nUse omar_brown_9300 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'X4ZXW5'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SEA', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SEA', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'omar_brown_9300', 'origin': 'SEA', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT011', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Chen', 'last_name': 'Moore', 'dob': '1991-12-11'}, {'first_name': 'Daiki', 'last_name': 'Kim', 'dob': '1952-05-25'}], 'payment_methods': [{'payment_id': 'credit_card_4120592', 'amount': 272}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '3Y4GQ1'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '3Y4GQ1', 'total_baggages': 2, 'nonfree_baggages': 2, 'payment_id': 'credit_card_4120592'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia_patel_6859',
        instruction='You are assisting Sophia Patel (user_id: sophia_patel_6859) with two travel matters. First, you want to request a compensation certificate for the cancellation of her flight from JFK to SEA on 2024-05-11 (reservation IPG6ZS), as it caused travel disruption. Later, you would like to update her upcoming round-trip reservation V7KTOK from DTW to MCO on 2024-05-26 in business class by changing the passenger name from Anya Moore to Sophia Patel, adding one checked bag, and paying for the bag with her credit card ending in 7741. You also want to explore switching the connecting outbound flight (DTW to MSP to MCO) to a direct flight on the same date; however, no direct flights are available from DTW to MCO on 2024-05-26, so the current connecting itinerary remains the only option.\n\nUse sophia_patel_6859 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'sophia_patel_6859', 'amount': 100}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'V7KTOK'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'V7KTOK', 'passengers': [{'first_name': 'Sophia', 'last_name': 'Patel', 'dob': '1981-12-25'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'V7KTOK', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_5278427'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'V7KTOK', 'cabin': 'business', 'flights': [{'flight_number': 'HAT111', 'date': '2024-05-26'}, {'flight_number': 'HAT071', 'date': '2024-05-26'}, {'flight_number': 'HAT298', 'date': '2024-05-30'}, {'flight_number': 'HAT127', 'date': '2024-05-30'}], 'payment_id': 'credit_card_5278427'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DTW', 'destination': 'MCO', 'date': '2024-05-26'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei_patel_4436',
        instruction='You are Mei Patel, user mei_patel_4436, and you want to cancel your one-way reservation E17VRA from LGA to SEA via PHX due to changed plans. You would like to book a new direct flight from LGA to PHL on 2024-05-20 for three passengers: Mei Patel, Yara Kim, and Amelia Lopez, in economy class with no checked bags and no insurance. You prefer flight HAT132, which departs in the evening, because it fits your schedule and was selected after comparing direct and one-stop options. You want this booking charged to your credit card ending in 4094. Later, you would like to update your round-trip reservation U1FRZP from PHX to SFO by changing the outbound flight from HAT283 to the earlier HAT159 on 2024-05-18, keeping the same economy cabin, and you prefer to use your credit card ending in 4094 for any fare difference.\n\nUse mei_patel_4436 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'E17VRA'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mei_patel_4436', 'origin': 'LGA', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT132', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mei', 'last_name': 'Patel', 'dob': '1950-04-08'}, {'first_name': 'Yara', 'last_name': 'Kim', 'dob': '1964-02-09'}, {'first_name': 'Amelia', 'last_name': 'Lopez', 'dob': '1998-07-27'}], 'payment_methods': [{'payment_id': 'credit_card_2126547', 'amount': 498}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'U1FRZP', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT159', 'date': '2024-05-18'}, {'flight_number': 'HAT144', 'date': '2024-05-20'}], 'payment_id': 'credit_card_2126547'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sofia_kim_7287',
        instruction='You are assisting Sofia Kim, who wants to book a new one-way flight from MCO to LAS on 2024-05-20 for herself and Mia Jackson in economy class, preferring an early morning flight (HAT101) due to availability and timing. You want to include one checked bag with no insurance and charge the payment method ending in 9725. Later, you would like to update existing reservation OI5L9G (MCO to CLT on 2024-05-25) to increase total checked bags to three (one non-free) and correct passenger Mia Jackson’s last name to Smith, using the same card ending in 9725 for any additional charges.\n\nUse sofia_kim_7287 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'MCO', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'sofia_kim_7287', 'origin': 'MCO', 'destination': 'LAS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT101', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Sofia', 'last_name': 'Kim', 'dob': '1950-06-24'}, {'first_name': 'Mia', 'last_name': 'Jackson', 'dob': '1986-05-05'}], 'payment_methods': [{'payment_id': 'credit_card_9879898', 'amount': 216}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'OI5L9G'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'OI5L9G', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_9879898'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'OI5L9G', 'passengers': [{'first_name': 'Sofia', 'last_name': 'Kim', 'dob': '1950-06-24'}, {'first_name': 'Mia', 'last_name': 'Smith', 'dob': '1986-05-05'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_ito_8544',
        instruction='You are Amelia Ito, a gold member, and you want to book a one-way economy flight from LAS to PHX on 2024-05-20 for yourself and your saved passenger Mason Kim, preferring a morning departure since HAT244 departs at 10:00 AM. You want to include one checked bag at no extra cost and do not want travel insurance, with payment charged to your credit card ending in 5300. Later, you would like to search for one-stop flights from LAS to JFK on 2024-05-23, possibly to explore alternative routing options. After that, you would like to cancel your original reservation 5K63ST, which includes a round-trip business class journey from LAS to JFK via ATL with passenger Sophia Wilson, due to the change in travel plans, and you prefer the refund to be issued back to your credit card ending in 5300.\n\nUse amelia_ito_8544 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'amelia_ito_8544', 'origin': 'LAS', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT244', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Amelia', 'last_name': 'Ito', 'dob': '1960-03-07'}, {'first_name': 'Mason', 'last_name': 'Kim', 'dob': '1976-06-10'}], 'payment_methods': [{'payment_id': 'credit_card_2540841', 'amount': 228}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '5K63ST', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_2540841'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'JFK', 'date': '2024-05-23'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '5K63ST'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '5K63ST'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are Ivan Taylor (ivan_taylor_6615) and you want to cancel your entire round-trip basic economy reservation WGMKL8 for four passengers—Isabella Jackson, Sofia Nguyen, Aarav Kim, and Juan Johnson—because your travel plans have changed. The reservation includes an early morning flight from MCO to LAS on 2024-05-23, a return from LAS to MCO later that day, an early morning flight from MCO to MSP on 2024-05-28, and a late evening return from MSP to MCO on the same day. You want the full refund processed to your credit card ending in 1656, as this payment method was used for the original booking. After the cancellation is complete, you would like to receive a compensation certificate for the inconvenience caused by the trip cancellation, as the reservation was made with insurance that supports such compensation.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'WGMKL8'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MCO', 'destination': 'LAS', 'date': '2024-05-23'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MCO', 'destination': 'MSP', 'date': '2024-05-28'}),
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 400}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are Ivan Taylor (user_id: ivan_taylor_6615), and you want a compensation certificate for the cancelled reservation 06K2QN, which was a one-way basic economy flight from ATL to LAS on 2024-05-08, due to the inconvenience caused. Later, you want to cancel reservation 06K2QN. After that, you would like to book a new one-way flight from ATL to DFW on 2024-05-20, specifically flight HAT252, in economy class, for two passengers: Ivan Taylor and Ivan Jackson, because you need to travel to DFW on that date. You prefer to pay using your credit card ending in 1656. Additionally, you want to review your existing reservation PK9XO8, a round-trip from LAX to IAH via SFO on 2024-05-24 to 2024-05-27, and update it to maintain business class for the same itinerary, using the same credit card, to ensure continued comfort and service for your upcoming trip.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '06K2QN'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'ATL', 'destination': 'DFW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT252', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Ivan', 'last_name': 'Jackson', 'dob': '1983-02-26'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 310}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'PK9XO8'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'PK9XO8', 'cabin': 'business', 'flights': [{'flight_number': 'HAT034', 'date': '2024-05-24'}, {'flight_number': 'HAT278', 'date': '2024-05-24'}, {'flight_number': 'HAT072', 'date': '2024-05-27'}, {'flight_number': 'HAT273', 'date': '2024-05-27'}], 'payment_id': 'credit_card_1885633'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_kim_9822',
        instruction='You are Raj Kim (DOB 1998-05-14), and you hold reservation 91O4DW for a round-trip from SEA to SFO. You want to update your outbound flight on 2024-05-17 to a later evening departure, specifically flight HAT274 departing at 20:00, because it better fits your schedule. You would like to keep your return flight HAT204 on 2024-05-20 as currently booked. Your reservation is already in business class, which meets your cabin preference. You also want to add one additional checked bag, increasing your total to two bags with one being a paid bag, to accommodate your travel needs. You prefer to use your saved credit card ending in 1222 for any applicable charges, as it is your primary payment method on file.\n\nUse raj_kim_9822 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '91O4DW'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '91O4DW', 'cabin': 'business', 'flights': [{'flight_number': 'HAT274', 'date': '2024-05-17'}, {'flight_number': 'HAT204', 'date': '2024-05-20'}], 'payment_id': 'credit_card_9399862'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '91O4DW', 'passengers': [{'first_name': 'Raj', 'last_name': 'Kim', 'dob': '1998-05-14'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '91O4DW', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_9399862'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_garcia_8677',
        instruction='You are assisting Harper Garcia (user_id: harper_garcia_8677) with updating reservation CDXEBS. You want to change the outbound flight from LGA to PHX on 2024-05-26 to flight HAT002, which departs in the evening, because it better fits the updated schedule. Later, you want to change the connecting flight from PHX to SFO on 2024-05-27 to flight HAT159, which departs in the afternoon, to maintain a convenient travel sequence. You prefer both flights to be in business class for greater comfort during the trip. You would like to update the passenger name from Ivan Brown to Lei Sanchez (DOB 1954-08-11) to reflect the correct traveler. You also want to increase the total checked baggage to 3, with 1 paid bag, to accommodate travel needs. Any fare difference and baggage charges should be billed to the credit card ending in 6617, which is already on file for this reservation.\n\nUse harper_garcia_8677 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'CDXEBS'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'CDXEBS', 'cabin': 'business', 'flights': [{'flight_number': 'HAT002', 'date': '2024-05-26'}, {'flight_number': 'HAT159', 'date': '2024-05-27'}], 'payment_id': 'credit_card_5865555'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'CDXEBS', 'passengers': [{'first_name': 'Harper', 'last_name': 'Garcia', 'dob': '1998-02-27'}, {'first_name': 'Lei', 'last_name': 'Sanchez', 'dob': '1954-08-11'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'CDXEBS', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_5865555'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_johnson_1294',
        instruction='You are Daiki Johnson, a gold member, and you want to book a one-way direct flight from IAH to SFO on 2024-05-20 in economy class for yourself, departing in the morning around 09:00, because it fits your schedule and you prefer nonstop travel. You would like to include one free checked bag, as it is part of your travel needs, and you opt out of insurance. You prefer to pay using your Mastercard ending in 2867, as it is your saved payment method.\n\nUse daiki_johnson_1294 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_johnson_1294', 'origin': 'IAH', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT072', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Johnson', 'dob': '1986-01-09'}], 'payment_methods': [{'payment_id': 'credit_card_6241774', 'amount': 100}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_nguyen_2677',
        instruction='You are to book a one-way economy flight for two passengers, Yusuf Nguyen and Liam Santos, on 2024-05-20 from JFK to SEA in the early morning, as the direct flight at 01:00 AM is suitable. You prefer this early morning direct flight to minimize travel time. You want to include 2 standard checked bags, no travel insurance, and pay using your Mastercard ending in 9744.\n\nUse chen_nguyen_2677 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'SEA', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'SEA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'chen_nguyen_2677', 'origin': 'JFK', 'destination': 'SEA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT069', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Nguyen', 'dob': '1975-12-05'}, {'first_name': 'Liam', 'last_name': 'Santos', 'dob': '1970-05-05'}], 'payment_methods': [{'payment_id': 'credit_card_2810906', 'amount': 242}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_patel_1917',
        instruction="You are Daiki Patel, user ID daiki_patel_1917, and you want to update your reservation 7WKBKD for a round-trip business class journey from PHX to JFK with a connection in DTW. First, you want to add 2 checked bags to the reservation, because they were initially forgotten, and you authorize the baggage fees to be charged to your Visa card ending in 1765. Next, you want to correct the date of birth for passenger Ethan Taylor from 1979-09-13 to 1979-09-14, as it was entered incorrectly during booking, while keeping Daiki Patel's details unchanged. Then, you want to reconfirm your flight selections even though they remain the same: you prefer the outbound journey on 2024-05-22 with a morning flight from PHX to DTW (HAT073) followed by an afternoon flight from DTW to JFK (HAT240), and the return journey on 2024-05-25 with an overnight flight from JFK to DTW (HAT033) followed by an afternoon flight from DTW to PHX (HAT035), all in business class, possibly due to a desire to validate the itinerary. You prefer any fare differences to be charged to the same Visa card ending in 1765.\n\nUse daiki_patel_1917 for authentication.",
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '7WKBKD'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '7WKBKD', 'total_baggages': 2, 'nonfree_baggages': 2, 'payment_id': 'credit_card_4327297'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '7WKBKD', 'passengers': [{'first_name': 'Daiki', 'last_name': 'Patel', 'dob': '1968-04-24'}, {'first_name': 'Ethan', 'last_name': 'Taylor', 'dob': '1979-09-14'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '7WKBKD', 'cabin': 'business', 'flights': [{'flight_number': 'HAT073', 'date': '2024-05-22'}, {'flight_number': 'HAT240', 'date': '2024-05-22'}, {'flight_number': 'HAT033', 'date': '2024-05-25'}, {'flight_number': 'HAT035', 'date': '2024-05-25'}], 'payment_id': 'credit_card_4327297'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_anderson_9682',
        instruction="You are Isabella Anderson (user_id: isabella_anderson_9682) with reservation I5QZWG. You want to add one checked bag to your reservation, increasing total_baggages to 2 with 1 non-free bag, because you need additional luggage for your trip. You would like to update the passenger name from Lei Kim to Sam Kim (DOB 1979-03-16) to correct the traveler's name on the ticket. You also want to reconfirm your current flight itinerary to ensure it remains unchanged: a business class flight from LAX to EWR on 2024-05-21 in the evening (HAT228), followed by a business class flight from EWR to CLT on 2024-05-22 in the afternoon (HAT043). You prefer to use your credit card ending in 7228 for any applicable fees or fare differences associated with these updates.\n\nUse isabella_anderson_9682 for authentication.",
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'I5QZWG'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'I5QZWG', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3277516'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'I5QZWG', 'passengers': [{'first_name': 'Isabella', 'last_name': 'Anderson', 'dob': '1967-09-24'}, {'first_name': 'Sam', 'last_name': 'Kim', 'dob': '1979-03-16'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'I5QZWG', 'cabin': 'business', 'flights': [{'flight_number': 'HAT228', 'date': '2024-05-21'}, {'flight_number': 'HAT043', 'date': '2024-05-22'}], 'payment_id': 'credit_card_3277516'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_sanchez_3298',
        instruction='You are Chen Sanchez, and you want to cancel your round-trip business class reservation WNVCCD from SFO to JFK via IAH due to a change in plans, with a refund issued to your Visa card ending in 4181. Later, you would like to book a one-stop economy flight from SFO to LGA on 2024-05-20 for two passengers, Yara Patel and Liam Kovacs, with the first leg departing SFO around 03:00 AM and arriving in PHX at 05:00 AM, followed by a connecting flight from PHX to LGA departing at 08:00 AM and arriving at 12:30 PM, with 2 total bags and no insurance, charged to the same Visa card. After that, you would like to know about direct flight options from SFO to LAX on the same date for travel time comparison; you are interested in a late evening flight option from SFO to LAX on 2024-05-20.\n\nUse chen_sanchez_3298 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'WNVCCD'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'WNVCCD'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'chen_sanchez_3298', 'origin': 'SFO', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT144', 'date': '2024-05-20'}, {'flight_number': 'HAT226', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yara', 'last_name': 'Patel', 'dob': '1962-10-23'}, {'first_name': 'Liam', 'last_name': 'Kovacs', 'dob': '1998-10-20'}], 'payment_methods': [{'payment_id': 'credit_card_6051598', 'amount': 570}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'LAX', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='juan_taylor_8806',
        instruction='You are Juan Taylor, and you want to book a one-way morning flight from Charlotte (CLT) to Boston (BOS) on 2024-05-20 for yourself and your companion Chen Lee in economy class, because flight HAT287 is available and fits your schedule. You prefer to use your Mastercard ending in 2923 for payment and would like to include 2 checked bags with no additional insurance.\n\nUse juan_taylor_8806 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'CLT', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'juan_taylor_8806', 'origin': 'CLT', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT287', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Juan', 'last_name': 'Taylor', 'dob': '1998-12-02'}, {'first_name': 'Chen', 'last_name': 'Lee', 'dob': '1959-04-10'}], 'payment_methods': [{'payment_id': 'credit_card_2217221', 'amount': 356}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '018BE2'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '018BE2', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_2217221'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia_silva_9133',
        instruction='You are Mia Silva, and you want to book a one-way flight from SFO to LAX for yourself and Amelia Johansson on 2024-05-20 in economy class, preferring a late evening flight with one free baggage and no insurance, because you found flight HAT163 suitable. You prefer to pay using your Visa card ending in 7854. Later, you also want to update your existing round-trip reservation IDFCNB (SFO-PHX-SFO) on 2024-05-21 by upgrading both flights to business class and increasing total baggage to two, with one paid bag, because you want more comfort and additional luggage. You authorize all charges to be applied to the same Visa card ending in 7854.\n\nUse mia_silva_9133 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mia_silva_9133', 'origin': 'SFO', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT163', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mia', 'last_name': 'Silva', 'dob': '1990-06-25'}, {'first_name': 'Amelia', 'last_name': 'Johansson', 'dob': '1966-05-22'}], 'payment_methods': [{'payment_id': 'credit_card_3163658', 'amount': 320}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'IDFCNB'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'IDFCNB', 'cabin': 'business', 'flights': [{'flight_number': 'HAT144', 'date': '2024-05-21'}, {'flight_number': 'HAT159', 'date': '2024-05-21'}], 'payment_id': 'credit_card_3163658'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'IDFCNB', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3163658'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_sanchez_5251',
        instruction='You are Anya Sanchez (anya_sanchez_5251) with reservation KDNMCS for a business class one-way flight from DFW to LAX on 2024-05-12, which was cancelled. You want to confirm the details of your reservation and explore available flight options for that route and date, although no direct flights are currently listed. Later, you would like to receive a $100 travel certificate as compensation for the inconvenience caused by the cancellation, as per airline policy for affected passengers.\n\nUse anya_sanchez_5251 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'KDNMCS'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DFW', 'destination': 'LAX', 'date': '2024-05-12'}),
            Action(name='send_certificate', kwargs={'user_id': 'anya_sanchez_5251', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_garcia_6211',
        instruction='You are Evelyn Garcia, traveling with passenger Mei Lee, and you want to verify your reservation 5264D4 due to the cancellation of your original IAH to EWR flight on 2024-05-11. You would like to rebook a direct flight from IAH to EWR on 2024-05-16, preferring a morning flight to accommodate your travel plans. Later, you will request a compensation certificate for the inconvenience caused by the cancellation.\n\nUse evelyn_garcia_6211 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '5264D4'}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'EWR', 'date': '2024-05-16'}),
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_garcia_6211', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia_patel_6859',
        instruction='You are assisting Sophia Patel (user_id: sophia_patel_6859) who initially wants to cancel her existing business class round-trip reservation V7KTOK from DTW to MCO due to a change in travel plans. Later, she would like to update the passenger on her one-way reservation ECQFCR from her own name to Chen Smith, as the trip is now for Chen. After that, she intends to book a new one-way economy flight from DTW to PHX on 2024-05-20 for two passengers—herself and Chen Smith—preferring flight HAT275 because it is a direct flight (despite the initial mention of one-stop, HAT275 is direct and available) departing late evening/overnight, which aligns with her schedule. She prefers to pay using her saved Mastercard ending in 7741, as it is her primary payment method on file, and she wants 0 checked bags and no travel insurance for this booking.\n\nUse sophia_patel_6859 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'V7KTOK'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DTW', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'ECQFCR'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'ECQFCR', 'passengers': [{'first_name': 'Chen', 'last_name': 'Smith', 'dob': '1985-12-19'}]}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'sophia_patel_6859', 'origin': 'DTW', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT275', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Chen', 'last_name': 'Smith', 'dob': '1985-12-19'}, {'first_name': 'Sophia', 'last_name': 'Patel', 'dob': '1981-12-25'}], 'payment_methods': [{'payment_id': 'credit_card_5278427', 'amount': 364}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ava_lopez_9068',
        instruction='You are to first cancel the round-trip economy reservation from PHX to MCO on 2024-05-18 (VE1ZC3), which includes a return on 2024-05-21, because the traveler no longer needs the trip. After that, you are to update the passenger on the business-class round-trip reservation from ATL to EWR (7ABORJ) from Ava Lopez to Lei Johansson (DOB 1986-06-10), as the trip will now be taken by a colleague. Later, you are to book a one-way direct economy flight from PHX to DTW on 2024-05-20 for Lei Johansson, specifically flight HAT073 departing in the early morning, because a direct option was preferred over one-stop alternatives. You prefer to use the credit card ending in 8178 on file for payment, add one free checked bag, and decline travel insurance for this booking.\n\nUse ava_lopez_9068 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'VE1ZC3'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHX', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '7ABORJ'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '7ABORJ', 'passengers': [{'first_name': 'Lei', 'last_name': 'Johansson', 'dob': '1986-06-10'}]}),
            Action(name='search_onestop_flight', kwargs={'origin': 'PHX', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ava_lopez_9068', 'origin': 'PHX', 'destination': 'DTW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT073', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lei', 'last_name': 'Johansson', 'dob': '1986-06-10'}], 'payment_methods': [{'payment_id': 'credit_card_3688120', 'amount': 128}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_khan_4151',
        instruction='You are Isabella Khan, and you want a compensation certificate for your cancelled business-class one-way flight from CLT to LGA on 2024-05-09 (reservation 8POIJI) because it was disrupted. Later, you would like to cancel your upcoming business-class reservation RRMXPX for a trip from MIA to PHX via LAS on 2024-05-27 and 2024-05-28 for passenger Mei Brown. After that, you want to book a new one-way economy flight from MIA to JFK on 2024-05-20 for Mei Brown, who is travelling with one free bag and no insurance. You prefer the flight departing in the mid-afternoon, specifically flight HAT224, as it fits the requested route, date, and class. You prefer to pay using your saved credit card ending in 3445.\n\nUse isabella_khan_4151 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'isabella_khan_4151', 'amount': 300}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'RRMXPX'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MIA', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'isabella_khan_4151', 'origin': 'MIA', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT224', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mei', 'last_name': 'Brown', 'dob': '1959-02-14'}], 'payment_methods': [{'payment_id': 'credit_card_4651498', 'amount': 172}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_nguyen_2677',
        instruction='You are Chen Nguyen, and you want to book a direct flight from EWR to CLT on 2024-05-22 in economy class for two passengers: Yusuf Nguyen and Liam Santos, because you prefer a nonstop option after initially considering one-stop flights. You want to include 2 total checked bags with no non-free bags and no travel insurance, and you prefer to pay using your Mastercard ending in 9744. Later, you would like to review your existing reservation VHV4BG for a trip on 2024-05-25, and you are interested in direct flight options for that date. You prefer a direct flight from EWR to CLT on 2024-05-25 in economy class, ideally around the same time as your previous flight, which departs in the late morning.\n\nUse chen_nguyen_2677 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'EWR', 'destination': 'CLT', 'date': '2024-05-22'}),
            Action(name='book_reservation', kwargs={'user_id': 'chen_nguyen_2677', 'origin': 'EWR', 'destination': 'CLT', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT215', 'date': '2024-05-22'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Nguyen', 'dob': '1975-12-05'}, {'first_name': 'Liam', 'last_name': 'Santos', 'dob': '1970-05-05'}], 'payment_methods': [{'payment_id': 'credit_card_2810906', 'amount': 266}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'VHV4BG'}),
            Action(name='search_direct_flight', kwargs={'origin': 'EWR', 'destination': 'CLT', 'date': '2024-05-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_nguyen_6691',
        instruction='You are to cancel the existing round-trip business-class reservation 5PQ0HT for Chen Nguyen, Aarav Taylor, and Anya Santos, which was originally from ATL to DEN with return via DFW, because the trip has been rescheduled. You want to book a new one-way economy flight from ATL to DFW on 2024-05-20 for the same three passengers, preferring the overnight flight (HAT252) that departs early on that date, as it aligns with the updated business schedule. You prefer to pay for this new booking using your credit card ending in 4526, which is already on file. Later, you would like to receive a compensation certificate for the inconvenience caused by the cancellation of the original trip. After that, you would like to update reservation ULFY27 for Aarav Lopez to increase the total checked bags to three, with one non-free bag, and you prefer to charge the additional baggage fee to the same credit card ending in 4526.\n\nUse chen_nguyen_6691 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '5PQ0HT'}),
            Action(name='book_reservation', kwargs={'user_id': 'chen_nguyen_6691', 'origin': 'ATL', 'destination': 'DFW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT252', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Chen', 'last_name': 'Nguyen', 'dob': '1973-09-23'}, {'first_name': 'Aarav', 'last_name': 'Taylor', 'dob': '1980-05-19'}, {'first_name': 'Anya', 'last_name': 'Santos', 'dob': '1990-12-16'}], 'payment_methods': [{'payment_id': 'credit_card_9800418', 'amount': 465}], 'total_baggages': 3, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'chen_nguyen_6691', 'amount': 300}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'ULFY27'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'ULFY27', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_9800418'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_brown_4047',
        instruction='You are assisting Lucas Brown (lucas_brown_4047), who wants to cancel his existing business class one-way reservation UX0R03 from ORD to LGA via PHL on 2024-05-22 because he no longer needs that trip. Instead, you want to book a new one-way flight for Lucas Brown from ORD to PHL on 2024-05-20 in economy class, specifically on flight HAT271, which departs in the evening at 19:00, because it fits his updated travel plans. You prefer to charge this new booking to his credit card ending in 8056, as it is his saved payment method. Later, you would like to request a compensation certificate for the cancellation of reservation UX0R03 due to the inconvenience caused. After that, you need to update his other reservation Q4TE65, a round-trip from IAH to DTW, to add one checked bag for the journey, increasing total_baggages to 1 and nonfree_baggages to 1, and you prefer to use the same credit card ending in 8056 for this additional charge.\n\nUse lucas_brown_4047 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'UX0R03'}),
            Action(name='book_reservation', kwargs={'user_id': 'lucas_brown_4047', 'origin': 'ORD', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT271', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lucas', 'last_name': 'Brown', 'dob': '1965-01-01'}], 'payment_methods': [{'payment_id': 'credit_card_7872117', 'amount': 185}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'lucas_brown_4047', 'amount': 100}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'Q4TE65'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'Q4TE65', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_7872117'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_martin_8348',
        instruction='You are to cancel the one-way reservation from SEA to LGA (BW2PEH) because Harper Martin has decided not to take this trip. You are then to upgrade the round-trip reservation ER7A5P from economy to business class for the flights on 2024-05-26 (ORD to IAH) and 2024-05-28 (ORD to DEN), as Harper wants a more comfortable journey for these segments. After that, you are to book a direct economy flight from SEA to SFO on 2024-05-20, specifically flight HAT258, for two passengers: Mei Sanchez and Mia Lopez, as this flight fits their schedule and destination needs. Following the booking, you are to add one additional checked bag to this SEA-SFO reservation, resulting in a total of three bags with one being a paid bag, to accommodate their luggage requirements. You prefer all charges, including fare differences and bag fees, to be billed to the credit card ending in 2492, which is on file.\n\nUse harper_martin_8348 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'BW2PEH'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'BW2PEH'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'ER7A5P', 'cabin': 'business', 'flights': [{'flight_number': 'HAT165', 'date': '2024-05-26'}, {'flight_number': 'HAT044', 'date': '2024-05-26'}, {'flight_number': 'HAT238', 'date': '2024-05-28'}, {'flight_number': 'HAT105', 'date': '2024-05-28'}], 'payment_id': 'credit_card_4852851'}),
            Action(name='search_direct_flight', kwargs={'origin': 'SEA', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'harper_martin_8348', 'origin': 'SEA', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT258', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mei', 'last_name': 'Sanchez', 'dob': '1966-12-24'}, {'first_name': 'Mia', 'last_name': 'Lopez', 'dob': '1973-01-15'}], 'payment_methods': [{'payment_id': 'credit_card_4852851', 'amount': 342}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'MU96D4', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_4852851'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lei_kim_3687',
        instruction='You are Lei Kim, and you want to update your existing reservation TOBZP5 for a one-way economy flight from PHL to CLT on 2024-05-19 for three passengers—Lei Kim, Mia Ahmed, and Evelyn Kovacs—to flight HAT122, which departs early morning at 06:00 AM, because it better fits your preferred travel time. You prefer to use your Visa card ending in 8898 for any fare difference. Later, you want to cancel your round-trip business class reservation K4VIZA from SFO to LAS, which includes connecting flights on 2024-05-28 and 2024-05-29 for three passengers—Lei Kim, Emma Anderson, and Mia Ahmed—due to schedule conflicts. As compensation for the cancellation affecting three passengers, you would like a $300 travel certificate issued. After that, you would like to explore one-stop flight options from SFO to LAS on 2024-05-28, particularly interested in evening or overnight connections, for potential future travel.\n\nUse lei_kim_3687 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'PHL', 'destination': 'CLT', 'date': '2024-05-19'}),
            Action(name='book_reservation', kwargs={'user_id': 'lei_kim_3687', 'origin': 'PHL', 'destination': 'CLT', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT122', 'date': '2024-05-19'}], 'passengers': [{'first_name': 'Lei', 'last_name': 'Kim', 'dob': '1998-08-05'}, {'first_name': 'Mia', 'last_name': 'Ahmed', 'dob': '1978-11-28'}, {'first_name': 'Evelyn', 'last_name': 'Kovacs', 'dob': '1988-11-26'}], 'payment_methods': [{'payment_id': 'credit_card_5844339', 'amount': 540}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'TOBZP5', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT122', 'date': '2024-05-19'}], 'payment_id': 'credit_card_5844339'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'K4VIZA'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'K4VIZA'}),
            Action(name='send_certificate', kwargs={'user_id': 'lei_kim_3687', 'amount': 300}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'LAS', 'date': '2024-05-28'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_garcia_6211',
        instruction='You are Evelyn Garcia, contacting on behalf of two passengers: Evelyn Garcia and Mei Lee. You are seeking to rebook a direct flight from IAH to EWR on 2024-05-20, as your original flight on 2024-05-11 (reservation 5264D4) was cancelled. You would like to book the available afternoon flight on that date, as it aligns with the only direct option currently offered. Later, you will request a compensation certificate for the cancelled flight, as airline policy entitles each passenger to $100, totaling $200 for two passengers, to be issued as a travel certificate.\n\nUse evelyn_garcia_6211 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_garcia_6211', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_khan_4151',
        instruction='You are assisting Isabella Khan with two reservation matters. First, for reservation RRMXPX (MIA to PHX via LAS), you want to update the booking by adding 2 checked bags (increasing total_baggages to 3, with 2 nonfree), charging the Mastercard ending in 3445 on file, because additional baggage is needed for the trip. You also want to correct the date of birth for passenger Mei Brown from 1959-02-14 to 1959-02-15, as it was entered incorrectly. Additionally, you confirm the current flights—HAT062 from MIA to LAS on 2024-05-27 and HAT095 from LAS to PHX on 2024-05-28—both in business class, and prefer to keep these flights as scheduled, using the same credit card for any fare adjustments if needed. Later, you would like to request a compensation certificate for the cancelled reservation 8POIJI (CLT to LGA on 2024-05-09, business class), because the flight was cancelled and compensation is expected for the inconvenience.\n\nUse isabella_khan_4151 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RRMXPX'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'RRMXPX', 'total_baggages': 3, 'nonfree_baggages': 2, 'payment_id': 'credit_card_4651498'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'RRMXPX', 'passengers': [{'first_name': 'Mei', 'last_name': 'Brown', 'dob': '1959-02-15'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'RRMXPX', 'cabin': 'business', 'flights': [{'flight_number': 'HAT062', 'date': '2024-05-27'}, {'flight_number': 'HAT095', 'date': '2024-05-28'}], 'payment_id': 'credit_card_4651498'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MIA', 'destination': 'PHX', 'date': '2024-05-27'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MIA', 'destination': 'PHX', 'date': '2024-05-27'}),
            Action(name='send_certificate', kwargs={'user_id': 'isabella_khan_4151', 'amount': 300}),
        ],
        outputs=[],
    ),

    Task(
        user_id='olivia_rossi_1087',
        instruction='You are Olivia Rossi (DOB 1976-02-25), and you want to cancel your round-trip reservation from DTW to SFO (reservation 5JATGA) due to a change in plans, with the refund issued to the original credit card ending in 6883. Later, you would like to book a one-way flight from DTW to JFK on 2024-05-20 in economy class for yourself, preferring the afternoon flight (HAT263) departing around 15:00, including one free checked bag and no travel insurance, charged to the same credit card ending in 6883.\n\nUse olivia_rossi_1087 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '5JATGA'}),
            Action(name='book_reservation', kwargs={'user_id': 'olivia_rossi_1087', 'origin': 'DTW', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT263', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Olivia', 'last_name': 'Rossi', 'dob': '1976-02-25'}], 'payment_methods': [{'payment_id': 'credit_card_8752089', 'amount': 121}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'olivia_rossi_1087', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_rossi_8135',
        instruction='You are to first cancel the existing round-trip business class reservation from DEN to LGA via PHL on 2024-05-28 to 2024-05-29, as the traveler no longer needs it. Then, you want to book a new one-way economy flight for Chen Rossi from DEN to CLT on 2024-05-20, departing in the evening, because he has changed his travel plans. You prefer this flight to include one free checked bag and no travel insurance, as per his request. You prefer to pay for this new booking using the Mastercard ending in 1609 saved in the account, as it was his selected payment method. Later, you would like to request a $100 compensation certificate due to the cancellation of the original reservation, as it was a business-class round-trip booking and compensation is available under policy.\n\nUse chen_rossi_8135 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GBCZYE'}),
            Action(name='book_reservation', kwargs={'user_id': 'chen_rossi_8135', 'origin': 'DEN', 'destination': 'CLT', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT143', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Chen', 'last_name': 'Rossi', 'dob': '1992-03-25'}], 'payment_methods': [{'payment_id': 'credit_card_8191674', 'amount': 159}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'chen_rossi_8135', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_garcia_6211',
        instruction='You are Evelyn Garcia, and you want to claim a compensation certificate for your cancelled flight HAT195 from IAH to EWR on 2024-05-11 because it was disrupted. Later, you want to cancel the entire reservation 5264D4. After that, you would like to book a one-way flight from IAH to JFK on 2024-05-20 in economy class for yourself and Mei Lee, preferring an early morning flight (HAT025) as it fits your schedule. You prefer to pay for this new booking using your credit card ending in 3459. Additionally, you want to update your other reservation I2GNN5 (for Raj Rossi) by adding one checked bag, increasing the total_baggages to 2 with one paid bag, and you prefer this charge also be applied to your credit card ending in 3459.\n\nUse evelyn_garcia_6211 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_garcia_6211', 'amount': 200}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '5264D4'}),
            Action(name='book_reservation', kwargs={'user_id': 'evelyn_garcia_6211', 'origin': 'IAH', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT025', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Garcia', 'dob': '1967-04-08'}, {'first_name': 'Mei', 'last_name': 'Lee', 'dob': '1969-05-16'}], 'payment_methods': [{'payment_id': 'credit_card_4906704', 'amount': 328}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'I2GNN5'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'I2GNN5', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_4906704'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_ahmed_2248',
        instruction='You are to first cancel the existing one-way reservation GIVSHB for Fatima Ahmed from CLT to IAH via EWR on 2024-05-28 in economy class with insurance, as her plans have changed. You want the cancellation processed and the refund issued to her Mastercard ending in 7228. After that, you would like to book a new one-way flight from CLT to BOS on 2024-05-20 in economy class for two passengers, Mohamed Johansson and Lucas Kovacs, with no checked bags and no insurance. You prefer an early morning flight, as HAT216 is the only available direct option on that date. You prefer to charge the new booking to your Mastercard ending in 7228.\n\nUse fatima_ahmed_2248 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GIVSHB'}),
            Action(name='book_reservation', kwargs={'user_id': 'fatima_ahmed_2248', 'origin': 'CLT', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT216', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mohamed', 'last_name': 'Johansson', 'dob': '1996-08-19'}, {'first_name': 'Lucas', 'last_name': 'Kovacs', 'dob': '1957-10-27'}], 'payment_methods': [{'payment_id': 'credit_card_7752823', 'amount': 248}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'GIVSHB'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_martin_3083',
        instruction='You are to first cancel the existing round-trip basic economy reservation KLA174 from BOS to DTW via CLT, which is eligible for cancellation due to travel insurance coverage. Then, you want to book a new one-way flight from BOS to MIA on 2024-05-20 for two passengers, Noah Martin and Raj Muller, in economy class. You prefer a flight in the early morning, specifically between 08:00 and 12:00, which corresponds to flight HAT247. You would like to include one free checked bag per passenger, decline travel insurance, and pay using your saved Visa card ending in 2091.\n\nUse noah_martin_3083 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'KLA174'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_martin_3083', 'origin': 'BOS', 'destination': 'MIA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT247', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Noah', 'last_name': 'Martin', 'dob': '1995-02-28'}, {'first_name': 'Raj', 'last_name': 'Muller', 'dob': '1968-10-20'}], 'payment_methods': [{'payment_id': 'credit_card_7670221', 'amount': 248}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'KLA174'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_sanchez_5251',
        instruction='You are assisting Anya Sanchez, who had her business class flight HAT124 from DFW to LAX on 2024-05-12 cancelled under reservation KDNMCS, and as a result, she wants compensation in the form of a certificate. You want to issue a compensation certificate for this cancelled flight. Later, you would like to book a one-way, one-stop business class flight for Anya from DFW to SFO on 2024-05-20, with the first leg on flight HAT038 from DFW to SEA in the morning and the second leg on flight HAT258 from SEA to SFO in the evening, including one checked bag and no insurance, charged to her Mastercard ending in 1642. After that, you would like to cancel her previous reservation DGLJTR for the trip from PHX to DFW on 2024-05-19, which included two passengers (Anya Sanchez and Liam Anderson), and process a refund back to the original payment method, her Mastercard ending in 3097.\n\nUse anya_sanchez_5251 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'anya_sanchez_5251', 'amount': 100}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DFW', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'anya_sanchez_5251', 'origin': 'DFW', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT038', 'date': '2024-05-20'}, {'flight_number': 'HAT258', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Anya', 'last_name': 'Sanchez', 'dob': '1987-03-13'}], 'payment_methods': [{'payment_id': 'credit_card_1699800', 'amount': 667}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'DGLJTR'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'DGLJTR'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction='You are assisting Noah Khan (user_id: noah_khan_8166) regarding his travel plans. The passenger on all reservations is Yusuf Ahmed. You want to request a compensation certificate for the cancelled one-way business class flight from LAS to IAH on 2024-05-13 (reservation LUA6DF) due to the inconvenience caused. Later, you would like to cancel the round-trip business class reservation Y1ZIDC from DEN to LAS (outbound on 2024-05-25, return on 2024-05-26) because of schedule changes, and you prefer the refund to be issued to the original payment method, which is the Visa card ending in 1892. After that, you would like to explore rebooking options and have requested a search for direct flights from DEN to LAS on 2024-05-25; however, no such flights are currently available in the system.\n\nUse noah_khan_8166 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'noah_khan_8166', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'Y1ZIDC'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DEN', 'destination': 'LAS', 'date': '2024-05-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='harper_ito_2309',
        instruction='You are to cancel the existing reservation N76PP0 for a one-way business class flight from JFK to ORD on 2024-05-27, with refund issued to the Visa card ending in 7986. Later, you would like to book a new one-way economy flight from DTW to ORD on 2024-05-20 for three passengers (Harper Ito, Yara Jackson, and Evelyn Davis), specifically on flight HAT119 departing in the late afternoon, with 3 total bags (0 paid) and no insurance, charged to the same Visa card ending in 7986. After that, you would like to receive a compensation certificate for the inconvenience experienced.\n\nUse harper_ito_2309 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'N76PP0'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DTW', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'harper_ito_2309', 'origin': 'DTW', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT119', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Harper', 'last_name': 'Ito', 'dob': '1984-03-23'}, {'first_name': 'Yara', 'last_name': 'Jackson', 'dob': '1997-05-05'}, {'first_name': 'Evelyn', 'last_name': 'Davis', 'dob': '1957-02-07'}], 'payment_methods': [{'payment_id': 'credit_card_1330512', 'amount': 318}], 'total_baggages': 3, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'N76PP0'}),
            Action(name='send_certificate', kwargs={'user_id': 'harper_ito_2309', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_nguyen_6045',
        instruction='You are Ethan Nguyen, account holder for reservation UDIGI7, and you want to cancel the entire one-way economy reservation from LGA to EWR via CLT for passenger Yusuf Smith on 2024-05-15 because the first flight HAT272 was delayed. You prefer the refund to be issued to the Visa card used for the original payment, ending in 5628. Later, you would like to receive a compensation certificate for the inconvenience caused by the flight delay.\n\nUse ethan_nguyen_6045 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'UDIGI7'}),
            Action(name='send_certificate', kwargs={'user_id': 'ethan_nguyen_6045', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mei_davis_9362',
        instruction='You are Mei Davis, and you want to book a new one-way economy flight from IAH to ORD on 2024-05-20 for one passenger, preferring the late evening flight (HAT044) because it fits your schedule, and you prefer to pay using your Mastercard ending in 6723. Later, you would like to receive a compensation certificate for your previously cancelled round-trip business-class reservation E1VXR2 because it was disrupted. After that, you want to update the passenger details on your round-trip reservation D28MAZ to include your saved passengers Liam Li and Sofia Sanchez, and confirm the flight itinerary: an afternoon flight from SEA to LAS on 2024-05-18 (HAT018), followed by an overnight flight from LAS to ATL on 2024-05-20 (HAT061), and a late evening return flight from ATL to SEA later that same day (HAT039), all in economy class, with payment charged to the same Mastercard ending in 6723.\n\nUse mei_davis_9362 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'ORD', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mei_davis_9362', 'origin': 'IAH', 'destination': 'ORD', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT044', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mei', 'last_name': 'Davis', 'dob': '1997-06-05'}], 'payment_methods': [{'payment_id': 'credit_card_4541014', 'amount': 172}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'mei_davis_9362', 'amount': 100}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'D28MAZ'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'D28MAZ', 'passengers': [{'first_name': 'Liam', 'last_name': 'Li', 'dob': '1968-11-27'}, {'first_name': 'Sofia', 'last_name': 'Sanchez', 'dob': '1974-04-28'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'D28MAZ', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT018', 'date': '2024-05-18'}, {'flight_number': 'HAT061', 'date': '2024-05-20'}, {'flight_number': 'HAT039', 'date': '2024-05-20'}], 'payment_id': 'credit_card_4541014'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mohamed_wilson_5739',
        instruction="You are to first cancel the existing round-trip reservation 5EU2LL from JFK to DFW via ATL and return via SEA, as the customer's plans have changed. After that, you are to book a new one-way direct flight from JFK to SFO for Mohamed Wilson on 2024-05-20. You prefer flight HAT023 departing in the afternoon, as it aligns with the desired travel date and direct routing. The booking should be in economy class with one free checked bag, no insurance, and charged to the credit card ending in 1211 on file.\n\nUse mohamed_wilson_5739 for authentication.",
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '5EU2LL'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mohamed_wilson_5739', 'origin': 'JFK', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mohamed', 'last_name': 'Wilson', 'dob': '1971-07-15'}], 'payment_methods': [{'payment_id': 'credit_card_7921410', 'amount': 191}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_martin_2396',
        instruction='You are assisting Ethan Martin (ethan_martin_2396), who wants to cancel his round-trip reservation GXWCPN from LGA to BOS via CLT on May 27-28, 2024, due to changed plans, and the reservation is eligible for cancellation with refund. You want to process the full cancellation and refund the amount back to his Mastercard ending in 8023 (credit_card_5447957), as that was the original payment method. Later, you would like to book a new one-way flight for Ethan Martin from LGA to PHL on May 20, 2024. You prefer flight HAT091 in economy class, departing in the early morning, because it matches his requested flight and is available at the quoted price. You want to include one free checked bag, decline travel insurance, and charge the total of $121 to the same Mastercard ending in 8023.\n\nUse ethan_martin_2396 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GXWCPN'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'BOS', 'date': '2024-05-27'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ethan_martin_2396', 'origin': 'LGA', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT091', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ethan', 'last_name': 'Martin', 'dob': '1963-05-18'}], 'payment_methods': [{'payment_id': 'credit_card_5447957', 'amount': 121}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yusuf_martin_3470',
        instruction='You are Yusuf Martin, and you want to first review your existing business class reservation BBVDO9 for the one-way trip from JFK to LAX via MIA on 2024-05-22 for yourself and passenger Yusuf Muller. After that, you would like to book a new one-way economy flight from JFK to ATL on 2024-05-20 for two passengers—yourself and another traveler—specifically on flight HAT057, which departs in the early morning. You prefer to use your Mastercard ending in 6182 for this booking. Following the booking, you want to add one checked bag to the new reservation, bringing the total to two bags with one being a paid bag, and you prefer the bag fee to be charged to the same Mastercard ending in 6182.\n\nUse yusuf_martin_3470 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'BBVDO9'}),
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'ATL', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'ATL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'yusuf_martin_3470', 'origin': 'JFK', 'destination': 'ATL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT057', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Martin', 'dob': '1964-02-24'}, {'first_name': 'Yusuf', 'last_name': 'Muller', 'dob': '1956-05-06'}], 'payment_methods': [{'payment_id': 'credit_card_9067289', 'amount': 282}, {'payment_id': 'credit_card_9067289', 'amount': 50}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'HATHAT', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_9067289'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are assisting Ivan Taylor, who had a cancelled flight (reservation 06K2QN) from ATL to LAS on 2024-05-08 with two passengers, Ivan Taylor and Ivan Jackson, and is entitled to compensation. You want to book a new direct flight from ATL to JFK on 2024-05-20 for two passengers, Ivan Taylor and Ivan Jackson, in economy class, specifically flight HAT285, which departs early morning, because it matches their preferred route and timing. You prefer to pay using the credit card ending in 1656, with no checked baggage and no insurance. Later, you would like to explore one-stop flight options from ATL to JFK on the same date (2024-05-20) to compare alternatives. After that, you would like to request a compensation certificate for the earlier cancelled reservation 06K2QN due to the disruption affecting two passengers.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'ATL', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT285', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Ivan', 'last_name': 'Jackson', 'dob': '1983-02-26'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 362}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction='You are assisting Noah Khan (user_id: noah_khan_8166), a regular customer, who had a prior business-class flight from LAS to IAH on reservation LUA6DF cancelled. You want to book a new one-way economy flight for passenger Yusuf Ahmed (DOB 1959-11-21) from DEN to DFW on 2024-05-20, specifically flight HAT046, which departs around midnight and arrives at 02:00 AM, because it matches the requested flight and is available in economy class. You prefer to use the credit card ending in 1892 on file for payment, as specified. Later, you would like to explore one-stop flight options from DEN to DFW on 2024-05-21 for potential alternative travel plans, as there are multiple connecting itineraries available that day. After that, you would like to request a compensation certificate for the cancelled LAS to IAH flight under reservation LUA6DF, as the cancellation qualifies under airline policy for a travel voucher.\n\nUse noah_khan_8166 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'DEN', 'destination': 'DFW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_khan_8166', 'origin': 'DEN', 'destination': 'DFW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT046', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}], 'payment_methods': [{'payment_id': 'credit_card_3240482', 'amount': 143}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DEN', 'destination': 'DFW', 'date': '2024-05-21'}),
            Action(name='send_certificate', kwargs={'user_id': 'noah_khan_8166', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma_smith_9363',
        instruction='You are Emma Smith (emma_smith_9363), and you want to cancel your existing round-trip basic economy reservation E9TZTU (PHL-CLT-DTW and return) due to a change in plans. You would like to book a new one-way economy flight from PHL to LGA on 2024-05-20 for yourself and passenger Ethan Kovacs, preferring the early morning flight departing around 07:00 (flight HAT096), because it fits your schedule and is available. You prefer to pay using your saved Visa card ending in 4249. Later, you would like to explore one-stop flight options from PHL to LGA on the same date (2024-05-20) for potential future consideration. After that, you would like to receive a compensation certificate because flight HAT096 was canceled on three occasions in the past week (May 5, 9, and 10), which caused travel inconvenience, and you are entitled to compensation under policy.\n\nUse emma_smith_9363 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'E9TZTU'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHL', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'emma_smith_9363', 'origin': 'PHL', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT096', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Emma', 'last_name': 'Smith', 'dob': '2000-08-19'}, {'first_name': 'Ethan', 'last_name': 'Kovacs', 'dob': '1965-08-06'}], 'payment_methods': [{'payment_id': 'credit_card_4253816', 'amount': 344}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'E9TZTU'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'PHL', 'destination': 'LGA', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'emma_smith_9363', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction='You are assisting Noah Khan, who is rebooking travel disrupted by a prior cancellation. You want to book a one-way economy flight from LAS to IAH on 2024-05-22 for passenger Yusuf Ahmed (DOB 1959-11-21), preferring direct flight HAT266 departing in the afternoon, because it matches the requested route and date with available economy seating. After booking, you would like to update the passenger name from Yusuf Ahmed to Yusuf Khan, to correct the last name. Then, you want to change the flight to HAT095 on 2024-05-22, same cabin, even though it routes to PHX instead of IAH, as per explicit request, using the same payment method. You prefer to pay using the Visa card ending in 9691 for all charges. Later, you would like a compensation certificate issued for the cancellation of your original business flight HAT175 from LAS to IAH on 2024-05-13 (reservation LUA6DF), due to the inconvenience caused. After that, you want to cancel your round-trip reservation Y1ZIDC from DEN to LAS and return, as the trip is no longer needed. Finally, for your upcoming round-trip reservation T47GQ8 from LAS to PHX, you would like to add one checked bag, increasing total baggage to 7 with 1 non-free bag, and charge the fee to your Visa card ending in 9691, to accommodate additional luggage needs.\n\nUse noah_khan_8166 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'IAH', 'date': '2024-05-22'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'IAH', 'date': '2024-05-22'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_khan_8166', 'origin': 'LAS', 'destination': 'IAH', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT266', 'date': '2024-05-22'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}], 'payment_methods': [{'payment_id': 'credit_card_5669132', 'amount': 149}, {'payment_id': 'credit_card_5669132', 'amount': 26}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'HATHAT', 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Khan', 'dob': '1959-11-21'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'HATHAT', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT095', 'date': '2024-05-22'}], 'payment_id': 'credit_card_5669132'}),
            Action(name='send_certificate', kwargs={'user_id': 'noah_khan_8166', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'Y1ZIDC'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'Y1ZIDC'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'T47GQ8', 'total_baggages': 7, 'nonfree_baggages': 1, 'payment_id': 'credit_card_5669132'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam_sanchez_8204',
        instruction='You are assisting Liam Sanchez (DOB: 1964-12-24), user ID liam_sanchez_8204, who wants to book a one-way, one-stop flight from Seattle to Los Angeles on 2024-05-20. You want to book flight HAT258 from SEA to SFO departing in the evening, followed by flight HAT273 from SFO to LAX departing at 10:00 PM, both in economy class for one passenger, because no direct flights were available. You prefer to pay using your Visa card ending in 4916, with no checked bags and no travel insurance. Later, you would like to cancel your existing round-trip reservation XGS9D8 from Seattle to New York, as your travel plans have changed, and you request a refund to your original payment method. After that, you would like to receive a compensation certificate due to a poor customer experience during the rebooking process.\n\nUse liam_sanchez_8204 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'SEA', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'liam_sanchez_8204', 'origin': 'SEA', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT258', 'date': '2024-05-20'}, {'flight_number': 'HAT273', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Liam', 'last_name': 'Sanchez', 'dob': '1964-12-24'}], 'payment_methods': [{'payment_id': 'credit_card_7979469', 'amount': 274}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'XGS9D8'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'XGS9D8'}),
            Action(name='send_certificate', kwargs={'user_id': 'liam_sanchez_8204', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction='You are Noah Khan (user_id: noah_khan_8166), and you want a compensation certificate for the cancelled business class one-way flight from LAS to IAH on 2024-05-13 under reservation LUA6DF, as it was a significant disruption to your travel plans. Later, you would like to book a new one-way economy flight from LAS to MCO on 2024-05-20 for your passenger Yusuf Ahmed (DOB: 1959-11-21), preferring the morning departure of flight HAT154, as it aligns with your desired travel time. You want to include one free checked bag, decline travel insurance, and pay using your credit card ending in 9691, as this is your preferred and previously used payment method.\n\nUse noah_khan_8166 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'noah_khan_8166', 'amount': 100}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_khan_8166', 'origin': 'LAS', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT154', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}], 'payment_methods': [{'payment_id': 'credit_card_5669132', 'amount': 134}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are assisting Ivan Taylor (user_id ivan_taylor_6615) who had his flight HAT052 from ATL to LAS on 2024-05-08 cancelled and is requesting a compensation certificate for the inconvenience. You want to issue a compensation certificate for this cancelled reservation (06K2QN) as a goodwill gesture. Later, you would like to book a new one-way flight from ATL to SEA on 2024-05-20 for two passengers: Ivan Taylor and Ivan Jackson, in economy class, with two checked bags included at no extra cost and no travel insurance. You prefer the flight departing at 08:00 (HAT239) as it is a morning flight, making it more convenient for travel. After that, you would like to use the saved Visa card ending in 1656 (payment_id credit_card_1885633) for payment, as it is the preferred and previously used payment method.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'SEA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'ATL', 'destination': 'SEA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT239', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Ivan', 'last_name': 'Jackson', 'dob': '1983-02-26'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 360}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mason_lee_7450',
        instruction='You are Mason Lee, and you want to book a direct flight from DFW to SEA on 2024-05-25 for two passengers: yourself (Mason Lee) and Lucas Kim, in economy class, preferring an early morning departure, as flight HAT183 fits that timing and is available. You prefer to pay using your Visa card ending in 2150. Later, you want to upgrade all flights in your existing reservation TBPDWP (from ATL to DEN) to business class—specifically flight HAT102 on 2024-05-20, HAT162 on 2024-05-21, HAT246 on 2024-05-27, and HAT177 on 2024-05-27—using the same passenger names and paying any fare difference with the same Visa card. After that, you would like to cancel reservation TBPDWP as it is no longer needed.\n\nUse mason_lee_7450 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'DFW', 'destination': 'SEA', 'date': '2024-05-25'}),
            Action(name='book_reservation', kwargs={'user_id': 'mason_lee_7450', 'origin': 'DFW', 'destination': 'SEA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT183', 'date': '2024-05-25'}], 'passengers': [{'first_name': 'Mason', 'last_name': 'Lee', 'dob': '1965-11-06'}, {'first_name': 'Lucas', 'last_name': 'Kim', 'dob': '1995-08-18'}], 'payment_methods': [{'payment_id': 'credit_card_9861856', 'amount': 328}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'TBPDWP'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'TBPDWP', 'cabin': 'business', 'flights': [{'flight_number': 'HAT102', 'date': '2024-05-20'}, {'flight_number': 'HAT162', 'date': '2024-05-21'}, {'flight_number': 'HAT246', 'date': '2024-05-27'}, {'flight_number': 'HAT177', 'date': '2024-05-27'}], 'payment_id': 'credit_card_9861856'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'TBPDWP'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_patel_1917',
        instruction='You are Daiki Patel, a gold member, who had a business class flight from SFO to PHL on 2024-05-14 (flight HAT074, reservation 0W60LB) that was cancelled, causing travel disruption. You want to receive a compensation certificate for the inconvenience of the cancelled flight. Later, you would like to update your reservation to rebook the same flight HAT074 from SFO to PHL in business class, but on 2024-05-16, as it is the next available date with business class seats. You prefer to use your saved Visa card ending in 1765 (credit_card_4327297) to cover any fare difference for the new booking.\n\nUse daiki_patel_1917 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'daiki_patel_1917', 'amount': 100}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '0W60LB'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '0W60LB', 'cabin': 'business', 'flights': [{'flight_number': 'HAT074', 'date': '2024-05-16'}], 'payment_id': 'credit_card_4327297'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia_patel_6859',
        instruction='You are assisting Sophia Patel (DOB 1981-12-25), user sophia_patel_6859, who wants to book a one-way flight from JFK to DTW on 2024-05-20. You prefer to book flight HAT033, a direct economy flight departing late evening on 2024-05-20 (around midnight EST), for one passenger, because it matches her requested flight and has available economy seats. You prefer to pay using your Mastercard ending in 7741, as it is your saved payment method, and you want to include one total baggage with no non-free bags and no insurance. Later, you would like to receive a $100 compensation certificate due to the cancellation of your previous JFK to SEA flight (reservation IPG6ZS), to be added to your existing certificate balance. After that, you want to cancel your current business class round-trip reservation V7KTOK from DTW to MCO (passenger: Anya Moore), because you no longer need it. Subsequently, you would like to explore alternative one-stop flight options from DTW to MCO on 2024-05-26, in economy class, to find a suitable replacement itinerary.\n\nUse sophia_patel_6859 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'DTW', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'sophia_patel_6859', 'origin': 'JFK', 'destination': 'DTW', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT033', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Sophia', 'last_name': 'Patel', 'dob': '1981-12-25'}], 'payment_methods': [{'payment_id': 'credit_card_5278427', 'amount': 140}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'sophia_patel_6859', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'V7KTOK'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DTW', 'destination': 'MCO', 'date': '2024-05-26'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_thomas_9373',
        instruction='You are Lucas Thomas, user lucas_thomas_9373, and you want to address a cancelled business class flight from MIA to JFK on 2024-05-10 (reservation MIC7D1) for passenger Amelia Nguyen. You first want to receive a compensation certificate for this cancellation. After that, you want to cancel the reservation MIC7D1. You also want to book a new direct flight from MIA to BOS on 2024-05-20 in economy class for your saved passenger, Daiki Ahmed, because it aligns with your travel plans and the flight is available in the morning. You prefer to pay using your Mastercard ending in 9094. Later, you would like to explore one-stop flight options from MIA to JFK on 2024-05-25 for potential rebooking, as you seek alternative routing after the cancellation of your original flight.\n\nUse lucas_thomas_9373 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'MIA', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'lucas_thomas_9373', 'origin': 'MIA', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT184', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Ahmed', 'dob': '1965-12-15'}], 'payment_methods': [{'payment_id': 'credit_card_1382059', 'amount': 170}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'lucas_thomas_9373', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'MIC7D1'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MIA', 'destination': 'JFK', 'date': '2024-05-25'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia_patel_6859',
        instruction='You are assisting Sophia Patel (DOB: 1981-12-25), user sophia_patel_6859, who wants to book a one-way, one-stop flight from JFK to MCO on 2024-05-20, with a connection in ATL, for one passenger. You prefer to use flight HAT268 from JFK to ATL departing in the morning and connecting to flight HAT146 from ATL to MCO departing at noon, both in economy class, because these were the specified flights. You want to charge your Mastercard ending in 7741 (payment_id credit_card_5278427) and include one free checked bag as part of the fare. After booking, you would like to add one additional paid checked bag to the reservation. Separately, you want to search for direct flights from JFK to SEA on 2024-05-25 for possible future travel, but note that no direct options are currently available. Finally, you request a compensation certificate for your previously cancelled flight on reservation IPG6ZS (JFK to SEA on 2024-05-11), as it was disrupted and you are entitled to redress.\n\nUse sophia_patel_6859 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'JFK', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'sophia_patel_6859', 'origin': 'JFK', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT268', 'date': '2024-05-20'}, {'flight_number': 'HAT146', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Sophia', 'last_name': 'Patel', 'dob': '1981-12-25'}], 'payment_methods': [{'payment_id': 'credit_card_5278427', 'amount': 277}, {'payment_id': 'credit_card_5278427', 'amount': 50}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'HATHAT', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_5278427'}),
            Action(name='search_direct_flight', kwargs={'origin': 'JFK', 'destination': 'SEA', 'date': '2024-05-25'}),
            Action(name='send_certificate', kwargs={'user_id': 'sophia_patel_6859', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_thomas_9373',
        instruction='You are to book a one-way flight from CLT to LGA on 2024-05-20 for three passengers: Lucas Thomas, Ethan Jackson, and Liam Thomas, in economy class. You prefer the flight departing at 02:00 AM (HAT024) because it is an early morning option with available seating and a lower fare. You would like to include 2 checked bags at no extra charge, leveraging your silver membership benefits, and you do not want travel insurance. You prefer to pay using your Mastercard ending in 9094.\n\nUse lucas_thomas_9373 for authentication.',
        actions=[
            Action(name='book_reservation', kwargs={'user_id': 'lucas_thomas_9373', 'origin': 'CLT', 'destination': 'LGA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT024', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Lucas', 'last_name': 'Thomas', 'dob': '1972-02-07'}, {'first_name': 'Ethan', 'last_name': 'Jackson', 'dob': '1986-08-06'}, {'first_name': 'Liam', 'last_name': 'Thomas', 'dob': '2000-06-06'}], 'payment_methods': [{'payment_id': 'credit_card_1382059', 'amount': 540}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_garcia_6211',
        instruction='You are assisting Evelyn Garcia, who had her original flight from IAH to EWR on 2024-05-11 (reservation 5264D4) cancelled. You want to first search for one-stop flights from IAH to EWR on 2024-05-20, but if none are suitable, proceed to book a direct flight. You would like to book flight HAT149 from IAH to EWR on 2024-05-20 in the morning (departing at 08:00 AM) in economy class for two passengers: Evelyn Garcia and Mei Lee, because it is the next available direct option after the cancellation. You prefer to pay using your credit card ending in 3459, include 2 checked bags at no extra charge, and decline travel insurance. Later, you would like to request a compensation certificate for the cancellation of your original flight (reservation 5264D4), as it was disrupted through no fault of your own.\n\nUse evelyn_garcia_6211 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'evelyn_garcia_6211', 'origin': 'IAH', 'destination': 'EWR', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT149', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Garcia', 'dob': '1967-04-08'}, {'first_name': 'Mei', 'last_name': 'Lee', 'dob': '1969-05-16'}], 'payment_methods': [{'payment_id': 'credit_card_4906704', 'amount': 386}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '5264D4'}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'EWR', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'evelyn_garcia_6211', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_patel_1917',
        instruction='You are assisting Daiki Patel (user_id: daiki_patel_1917) who had a business-class one-way flight from SFO to PHL on 2024-05-14 (reservation 0W60LB) that was cancelled, making him eligible for a $100 compensation certificate. You want to first request the issuance of this compensation. Later, you would like to book a new one-way, one-stop business-class flight from SFO to JFK on 2024-05-20, with the first segment on HAT082 from SFO to IAH departing in the late evening (at 23:00) and the second segment on HAT068 from IAH to JFK departing in the morning (at 11:00), ensuring both flights are in business class. The passenger is Daiki Patel, and you prefer to include one checked bag with no insurance. You prefer to pay using the credit card ending in 1765, which is on file.\n\nUse daiki_patel_1917 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_patel_1917', 'origin': 'SFO', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT082', 'date': '2024-05-20'}, {'flight_number': 'HAT068', 'date': '2024-05-21'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Patel', 'dob': '1968-04-24'}], 'payment_methods': [{'payment_id': 'credit_card_4327297', 'amount': 910}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='send_certificate', kwargs={'user_id': 'daiki_patel_1917', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_silva_5208',
        instruction='You are Evelyn Silva (user_id: evelyn_silva_5208) and you want to cancel your existing reservation 90WDMA for a one-way trip from PHX to LAX via SFO on 2024-05-21. You would like to rebook the same journey in economy class using flight HAT283 from PHX to SFO in the evening and connecting flight HAT273 from SFO to LAX in the late evening, both on 2024-05-21, because your plans have changed. You also want to add one paid checked bag (increasing total bags to 3 with 1 non-free bag) for convenience. Additionally, you need to correct the last name of passenger Fatima Davis (DOB: 1958-02-07) to Wilson. All charges and the refund from the original booking should be processed using your saved credit card (credit_card_1638882).\n\nUse evelyn_silva_5208 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '90WDMA'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '90WDMA'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '90WDMA', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_1638882'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '90WDMA', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT283', 'date': '2024-05-21'}, {'flight_number': 'HAT273', 'date': '2024-05-21'}], 'payment_id': 'credit_card_1638882'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '90WDMA', 'passengers': [{'first_name': 'Fatima', 'last_name': 'Anderson', 'dob': '1956-04-23'}, {'first_name': 'Fatima', 'last_name': 'Wilson', 'dob': '1958-02-07'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_khan_4151',
        instruction="You are Isabella Khan (user_id: isabella_khan_4151) managing reservation RRMXPX. You want to cancel the current booking for Mei Brown on flights HAT062 (MIA to LAS) on 2024-05-27 and HAT095 (LAS to PHX) on 2024-05-28. Later, you would like to rebook the same route with updated details: a business class flight from MIA to LAS on 2024-05-29, preferring the late evening departure (HAT062, departs 22:00), followed by a business class flight from LAS to PHX on 2024-05-30, preferring the morning departure (HAT244, departs 10:00), because the original dates no longer suit the traveler's schedule. You also want to update the passenger name from Mei Brown to Raj Lopez (DOB: 1953-05-18) and increase the total checked bags to three, with one paid bag, to accommodate the new traveler's needs. All changes should be charged to your Mastercard ending in 3445, as it is your preferred payment method on file.\n\nUse isabella_khan_4151 for authentication.",
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'RRMXPX'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RRMXPX'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'RRMXPX', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_4651498'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'RRMXPX', 'cabin': 'business', 'flights': [{'flight_number': 'HAT062', 'date': '2024-05-29'}, {'flight_number': 'HAT244', 'date': '2024-05-30'}], 'payment_id': 'credit_card_4651498'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'RRMXPX', 'passengers': [{'first_name': 'Raj', 'last_name': 'Lopez', 'dob': '1953-05-18'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='liam_muller_4931',
        instruction='You are assisting Liam Muller, a gold member, who wants to book a one-way, one-stop flight from ATL to LAX via DFW on 2024-05-20 for one passenger in economy class. You want to book flight HAT297 from ATL to DFW and connecting flight HAT124 from DFW to LAX on the same day, as these flights align with his preferred route and timing. You prefer economy class because it includes one free checked bag, which meets his baggage need. You prefer to pay using his saved Visa card ending in 5565 for convenience and faster checkout.\n\nUse liam_muller_4931 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'JJOY4O'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'liam_muller_4931', 'origin': 'ATL', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT297', 'date': '2024-05-20'}, {'flight_number': 'HAT124', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Liam', 'last_name': 'Muller', 'dob': '1954-03-21'}], 'payment_methods': [{'payment_id': 'credit_card_2602245', 'amount': 235}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar_rossi_1241',
        instruction="You are Omar Rossi, a gold member, and you want to cancel your existing round-trip reservation from Seattle to Dallas (UM3OG5) because you've decided to change your travel plans. Later, you would like to book a new one-way flight from Seattle to New York on 2024-05-20 in the morning, in economy class, for two passengers: yourself and Liam Lee, using your saved passenger details. You prefer this flight because it aligns with your updated schedule and offers a direct connection. You want to pay for this new booking with your Visa card ending in 6437, which is already on file. After that, you would like to update your separate reservation from Los Angeles to San Francisco (5RJ7UH) to add one checked bag, increasing the total to two bags with one being paid, because you need extra luggage for your trip. You prefer to charge the additional baggage fee to the same Visa card ending in 6437.\n\nUse omar_rossi_1241 for authentication.",
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'SEA', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SEA', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'UM3OG5'}),
            Action(name='book_reservation', kwargs={'user_id': 'omar_rossi_1241', 'origin': 'SEA', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT089', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Omar', 'last_name': 'Rossi', 'dob': '1970-06-06'}, {'first_name': 'Liam', 'last_name': 'Lee', 'dob': '1989-08-12'}], 'payment_methods': [{'payment_id': 'credit_card_7407366', 'amount': 368}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '5RJ7UH'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '5RJ7UH', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_7407366'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are Ivan Taylor (ivan_taylor_6615) and you want compensation for your cancelled reservation 06K2QN (ATL to LAS) due to the disruption. You also want to cancel that reservation. After that, you would like to book a one-way flight from ATL to JFK on 2024-05-20 for yourself and Aarav Kim in economy class, specifically flight HAT285 departing in the early morning, because it matches your requested flight and is available. You prefer to pay using your Visa card ending in 1656. Later, you want to update your existing reservation PK9XO8 by changing the first flight from LAX to SFO to flight HAT034 on 2024-05-26, keeping the rest of the itinerary intact, and you want to ensure your passenger details (Ivan Taylor) are confirmed in the reservation. You also prefer to use your Visa card ending in 1656 for any fare difference. Finally, you want to check direct flight availability from ATL to JFK on 2024-05-20, which includes options like HAT285 in the early morning and HAT164 in the late morning.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '06K2QN'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ATL', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'ATL', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT285', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}, {'first_name': 'Aarav', 'last_name': 'Kim', 'dob': '1962-10-28'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 362}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'PK9XO8', 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'PK9XO8', 'cabin': 'business', 'flights': [{'flight_number': 'HAT034', 'date': '2024-05-26'}, {'flight_number': 'HAT278', 'date': '2024-05-24'}, {'flight_number': 'HAT072', 'date': '2024-05-27'}, {'flight_number': 'HAT273', 'date': '2024-05-27'}], 'payment_id': 'credit_card_1885633'}),
            Action(name='search_direct_flight', kwargs={'origin': 'ATL', 'destination': 'JFK', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction='You are Noah Khan, and you want to receive a compensation certificate for your cancelled flight LUA6DF from LAS to IAH on 2024-05-13, which was originally booked in business class. Later, you want to cancel your reservation Y1ZIDC for a business-class round-trip from DEN to LAS on 2024-05-25, because you are changing your travel plans. After that, you would like to book a one-stop economy-class one-way flight from DEN to PHL on 2024-05-25 for one passenger (Yusuf Ahmed), consisting of flight HAT105 from DEN to ORD in the morning and connecting flight HAT139 from ORD to PHL in the evening, with one checked bag included, no additional paid bags, no insurance, and payment using your Visa card ending in 1892. You also want to update the passenger list on reservation T47GQ8 by removing Yara Taylor and adding Seb Smith as a passenger for the existing round-trip from LAS to PHX. Subsequently, you would like to change the outbound flight in reservation T47GQ8 from HAT284 to HAT095 on 2024-05-27 in business class, using the same payment method. Finally, you want to verify direct flight options from LAS to PHX on 2024-05-27, particularly interested in morning and late-night departures, to ensure better timing alignment with your schedule.\n\nUse noah_khan_8166 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'noah_khan_8166', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'Y1ZIDC'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DEN', 'destination': 'PHL', 'date': '2024-05-25'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_khan_8166', 'origin': 'DEN', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT105', 'date': '2024-05-25'}, {'flight_number': 'HAT139', 'date': '2024-05-25'}], 'passengers': [{'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}], 'payment_methods': [{'payment_id': 'credit_card_3240482', 'amount': 339}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'T47GQ8', 'passengers': [{'first_name': 'Noah', 'last_name': 'Khan', 'dob': '1982-01-02'}, {'first_name': 'Yusuf', 'last_name': 'Ahmed', 'dob': '1959-11-21'}, {'first_name': 'Seb', 'last_name': 'Smith', 'dob': '1997-03-01'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'T47GQ8', 'cabin': 'business', 'flights': [{'flight_number': 'HAT095', 'date': '2024-05-27'}, {'flight_number': 'HAT027', 'date': '2024-05-30'}], 'payment_id': 'credit_card_3240482'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'PHX', 'date': '2024-05-27'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_khan_8166',
        instruction="You are assisting Noah Khan (user_id: noah_khan_8166) regarding his reservation LUA6DF, which was a business class flight from LAS to IAH on 2024-05-13 (flight HAT175) that was cancelled, causing inconvenience for passenger Yusuf Ahmed. You want to request a compensation certificate for this cancellation as a goodwill gesture for the disruption. After that, you would like to search for alternative direct flights from LAS to IAH on 2024-05-20 for rebooking purposes, with a preference for an afternoon flight, as the only available direct option departs at 13:00. Subsequently, you would like to cancel the upcoming round-trip reservation Y1ZIDC from DEN to LAS, which includes business class flights on 2024-05-25 and 2024-05-26 for the same passenger, because it is eligible for cancellation due to having travel insurance and the traveler's change of plans.\n\nUse noah_khan_8166 for authentication.",
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'noah_khan_8166', 'amount': 100}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'IAH', 'date': '2024-05-20'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'Y1ZIDC'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_sanchez_5251',
        instruction='You are Anya Sanchez, a business class passenger whose flight from DFW to LAX on 2024-05-12 (reservation KDNMCS) was cancelled, and you would like to receive a compensation certificate for the inconvenience. You want to explore alternative travel options and are interested in direct flights from DFW to LAX on 2024-05-20. You prefer an evening flight, specifically around 19:00, based on the available option. Later, you decide to proceed with cancelling your original reservation KDNMCS.\n\nUse anya_sanchez_5251 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'anya_sanchez_5251', 'amount': 100}),
            Action(name='search_direct_flight', kwargs={'origin': 'DFW', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'KDNMCS'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_lee_7603',
        instruction='You are assisting Daiki Lee (user_id: daiki_lee_7603) who had a business-class one-way flight from LAS to PHX on 2024-05-11 (reservation PMZURQ, flight HAT244) that was cancelled. You want to issue a compensation certificate for this cancelled flight because it was a no-fault cancellation by the airline. Later, you would like to cancel the round-trip reservation 8BVA1W, which includes flights from IAH to ATL via LAS on 2024-05-18 and return from ATL to IAH on 2024-05-29, for two passengers (Daiki Lee and Olivia Johnson), and process a refund to the original payment method (gift card) because the customer no longer needs the travel. You prefer the refund to be issued to the same gift card used for purchase.\n\nUse daiki_lee_7603 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'daiki_lee_7603', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '8BVA1W'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_khan_9974',
        instruction='You are assisting Fatima Khan, a regular flyer, with multiple travel requests. First, you want to book a one-way flight from Orlando (MCO) to Phoenix (PHX) on 2024-05-20 for two passengers: Fatima Khan and her companion Yara Brown, both saved in her account. You prefer flight HAT161 in economy class, departing in the late morning, and you want to pay using her Mastercard ending in 3471. Additionally, you want to update her existing round-trip reservation BV2RJH (MCO-LAS-IAH and return) to add one checked bag, increasing the total to 9 bags with 1 non-free bag, and charge the same Mastercard ending in 3471. Later, you would like to explore available one-stop flight options from MCO to IAH on 2024-05-17 for potential future travel, particularly those connecting through LAS with afternoon or evening onward departures.\n\nUse fatima_khan_9974 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'MCO', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'fatima_khan_9974', 'origin': 'MCO', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT161', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Fatima', 'last_name': 'Khan', 'dob': '1989-01-01'}, {'first_name': 'Yara', 'last_name': 'Brown', 'dob': '1956-04-20'}], 'payment_methods': [{'payment_id': 'credit_card_6225387', 'amount': 346}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'BV2RJH', 'total_baggages': 9, 'nonfree_baggages': 1, 'payment_id': 'credit_card_6225387'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'BV2RJH'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MCO', 'destination': 'IAH', 'date': '2024-05-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james_johansson_8847',
        instruction='You are to assist James Johansson in booking a one-way flight from Orlando (MCO) to Boston (BOS) on 2024-05-20 for himself and his travel companion Liam Li in economy class, as there is a direct flight available in the morning that fits their schedule. You want to use his saved Mastercard ending in 9843 for the booking. After the reservation is confirmed, you would like to add one checked bag for the trip, making it two total bags with one being paid, and charge the additional fee to the same card. You also want to retrieve and display the details of his existing reservation XR266K, which is for a separate trip from MCO to Minneapolis (MSP) on 2024-05-28. Later, you would like to explore available one-stop flight options from MCO to BOS on 2024-05-20 for comparison or potential future planning, but no booking is requested for those at this time.\n\nUse james_johansson_8847 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'MCO', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'james_johansson_8847', 'origin': 'MCO', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT017', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'James', 'last_name': 'Johansson', 'dob': '1990-09-05'}, {'first_name': 'Liam', 'last_name': 'Li', 'dob': '1989-05-13'}], 'payment_methods': [{'payment_id': 'credit_card_3527910', 'amount': 296}, {'payment_id': 'credit_card_3527910', 'amount': 50}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'HATHAT', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_3527910'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'XR266K'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MCO', 'destination': 'BOS', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_sanchez_5251',
        instruction='You are Anya Sanchez, user_id anya_sanchez_5251, and you had a business class flight from DFW to LAX on reservation KDNMCS that was cancelled. You want to receive a compensation certificate for this cancellation because you were inconvenienced. Later, you decided to cancel the original reservation and rebook your travel. You would like to book a new one-way economy flight from DFW to SEA on 2024-05-20, specifically flight HAT099 departing in the afternoon at 16:00, for one passenger, because it fits your schedule and is available. You prefer to pay using your Mastercard ending in 1642, which is on file. You also want to update the passenger on this new reservation to your colleague Amelia Khan, whose details are saved in your account. After completing this booking, you would like to explore available one-stop flight options from DFW to SEA on the same date, 2024-05-20, to compare alternatives, even though you have already booked the direct flight.\n\nUse anya_sanchez_5251 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'anya_sanchez_5251', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'KDNMCS'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DFW', 'destination': 'SEA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'anya_sanchez_5251', 'origin': 'DFW', 'destination': 'SEA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT099', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Anya', 'last_name': 'Sanchez', 'dob': '1987-03-13'}], 'payment_methods': [{'payment_id': 'credit_card_1699800', 'amount': 173}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'HATHAT', 'passengers': [{'first_name': 'Amelia', 'last_name': 'Khan', 'dob': '1983-06-27'}]}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DFW', 'destination': 'SEA', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_patel_1917',
        instruction='You are Daiki Patel (user_id daiki_patel_1917) and you want a compensation certificate for your cancelled one-way business class flight from SFO to PHL on 2024-05-14 (reservation 0W60LB) because it was disrupted. Later, you want to cancel your active round-trip reservation 7WKBKD from PHX to JFK (departure 2024-05-22, return 2024-05-25) after confirming the passenger details are updated to Daiki Patel (DOB 1968-04-24) and Ethan Taylor (DOB 1979-09-13), which are already correct. After that, you would like to book a new one-way flight from PHX to SFO on 2024-05-20 in business class for two passengers (Daiki Patel and Ethan Taylor) on flight HAT159, which departs in the afternoon, because it fits your schedule. You prefer to pay using your credit card ending in 1765. Finally, you are interested in one-stop flight options from PHX to JFK on 2024-05-22 for future consideration, such as via LGA or SFO, to explore alternative routing possibilities.\n\nUse daiki_patel_1917 for authentication.',
        actions=[
            Action(name='send_certificate', kwargs={'user_id': 'daiki_patel_1917', 'amount': 100}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '7WKBKD'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHX', 'destination': 'SFO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_patel_1917', 'origin': 'PHX', 'destination': 'SFO', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT159', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Patel', 'dob': '1968-04-24'}, {'first_name': 'Ethan', 'last_name': 'Taylor', 'dob': '1979-09-13'}], 'payment_methods': [{'payment_id': 'credit_card_4327297', 'amount': 654}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '7WKBKD', 'passengers': [{'first_name': 'Daiki', 'last_name': 'Patel', 'dob': '1968-04-24'}, {'first_name': 'Ethan', 'last_name': 'Taylor', 'dob': '1979-09-13'}]}),
            Action(name='search_onestop_flight', kwargs={'origin': 'PHX', 'destination': 'JFK', 'date': '2024-05-22'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_taylor_4937',
        instruction='You are assisting Amelia Taylor (user_id: amelia_taylor_4937) with her travel plans. You want to book a direct flight from IAH to LAS on 2024-05-20 in economy class for two passengers: Mohamed Davis and Emma Kim, preferring the late evening flight (HAT112, departing at 10:00 PM) because it is the only available direct option and aligns with her schedule. You prefer to pay using her Mastercard ending in 1756, as it is her primary card on file. Later, you would like to update her existing business-class reservation (LT77K6) from IAH to DFW via EWR on 2024-05-21 to increase total_baggages from 3 to 4, adding one nonfree checked bag, and charge the fee to the same Mastercard ending in 1756, to accommodate additional luggage needs. After that, you would like to search for one-stop flight options from IAH to LAS on 2024-05-20 to compare with the direct flight; however, no such connecting flights to LAS are available on that date, so this search yields no alternatives.\n\nUse amelia_taylor_4937 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'amelia_taylor_4937', 'origin': 'IAH', 'destination': 'LAS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT112', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mohamed', 'last_name': 'Davis', 'dob': '1962-08-14'}, {'first_name': 'Emma', 'last_name': 'Kim', 'dob': '1954-10-13'}], 'payment_methods': [{'payment_id': 'credit_card_1430006', 'amount': 302}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'LT77K6', 'total_baggages': 4, 'nonfree_baggages': 1, 'payment_id': 'credit_card_1430006'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'LAS', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav_anderson_6237',
        instruction='You are Aarav Anderson, and you want to book a new one-way flight from SFO to LAX on 2024-05-20 for two passengers in economy class, departing in the evening, because you need to travel for personal plans. You prefer to pay using your Visa card ending in 5537. Later, you want to cancel your existing business class reservation from LGA to PHX (reservation BU71UY) due to a schedule conflict and request a refund to the same Visa card. After that, you would like to update your reservation RH6XFN to increase the total checked bags to three, with one being a paid bag, and use the same card for the additional charge. Since your flight on reservation BU71UY was canceled, you also want to receive a compensation certificate as a gesture of goodwill.\n\nUse aarav_anderson_6237 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'LAX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'aarav_anderson_6237', 'origin': 'SFO', 'destination': 'LAX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT163', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Aarav', 'last_name': 'Anderson', 'dob': '1999-12-16'}, {'first_name': 'Chen', 'last_name': 'Muller', 'dob': '1999-07-01'}], 'payment_methods': [{'payment_id': 'credit_card_5252591', 'amount': 320}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'BU71UY'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'RH6XFN'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'RH6XFN', 'cabin': 'business', 'flights': [{'flight_number': 'HAT101', 'date': '2024-05-19'}, {'flight_number': 'HAT070', 'date': '2024-05-19'}, {'flight_number': 'HAT293', 'date': '2024-05-22'}], 'payment_id': 'credit_card_5252591'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'RH6XFN', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_5252591'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'RH6XFN', 'passengers': [{'first_name': 'Aarav', 'last_name': 'Anderson', 'dob': '1999-12-16'}, {'first_name': 'Chen', 'last_name': 'Muller', 'dob': '1999-07-01'}]}),
            Action(name='send_certificate', kwargs={'user_id': 'aarav_anderson_6237', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ivan_taylor_6615',
        instruction='You are assisting Ivan Taylor (ivan_taylor_6615), who wants compensation for the cancellation of his one-way flight from ATL to LAS (reservation 06K2QN) due to the inconvenience caused. He would like to book a new one-way business class flight from MCO to BOS on 2024-05-20, preferring the early morning flight (HAT028, departs around 05:00) for himself, to be charged to his credit card ending in 1656. Later, he intends to cancel his round-trip reservation WGMKL8 (MCO-LAS-MCO) and update the passenger name on that reservation from Isabella Jackson to Aarav Kim. Additionally, he would like to update the baggage allowance on his business class round-trip reservation PK9XO8 (LAX-IAH) to include a total of 3 checked bags, with 1 additional non-free bag, using the same credit card on file. He prefers all transactions to be processed using his existing card details.\n\nUse ivan_taylor_6615 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'MCO', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MCO', 'destination': 'BOS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ivan_taylor_6615', 'origin': 'MCO', 'destination': 'BOS', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT028', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ivan', 'last_name': 'Taylor', 'dob': '1970-02-21'}], 'payment_methods': [{'payment_id': 'credit_card_1885633', 'amount': 381}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'PK9XO8', 'cabin': 'business', 'flights': [{'flight_number': 'HAT034', 'date': '2024-05-24'}, {'flight_number': 'HAT082', 'date': '2024-05-24'}, {'origin': 'IAH', 'destination': 'SFO', 'flight_number': 'HAT072', 'date': '2024-05-27'}, {'origin': 'SFO', 'destination': 'LAX', 'flight_number': 'HAT273', 'date': '2024-05-27'}], 'payment_id': 'credit_card_1885633'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'WGMKL8'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'PK9XO8'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'PK9XO8', 'total_baggages': 3, 'nonfree_baggages': 1, 'payment_id': 'credit_card_1885633'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'WGMKL8', 'passengers': [{'first_name': 'Aarav', 'last_name': 'Kim', 'dob': '1962-10-28'}, {'first_name': 'Sofia', 'last_name': 'Nguyen', 'dob': '1975-04-24'}, {'first_name': 'Aarav', 'last_name': 'Kim', 'dob': '1962-10-28'}, {'first_name': 'Juan', 'last_name': 'Johnson', 'dob': '1984-07-18'}]}),
            Action(name='send_certificate', kwargs={'user_id': 'ivan_taylor_6615', 'amount': 200}),
        ],
        outputs=[],
    ),

    Task(
        user_id='raj_sanchez_7340',
        instruction='You are Raj Sanchez, and you want to book a one-way direct flight from Miami to New York (JFK) on 2024-05-20 for yourself and Olivia Taylor in economy class, specifically flight HAT224 departing in the afternoon, because it fits your schedule and is available. You prefer to pay using your credit card ending in 4388, as it is your saved payment method. After that, you would like to update your existing reservation MZDDS4 to correct the passenger name from Anya Li to Anya Lee, as the last name was mistakenly entered incorrectly during the original booking.\n\nUse raj_sanchez_7340 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'MIA', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MIA', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'raj_sanchez_7340', 'origin': 'MIA', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT224', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Raj', 'last_name': 'Sanchez', 'dob': '1965-09-13'}, {'first_name': 'Olivia', 'last_name': 'Taylor', 'dob': '1976-06-27'}], 'payment_methods': [{'payment_id': 'credit_card_7891819', 'amount': 344}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'MZDDS4', 'passengers': [{'first_name': 'Raj', 'last_name': 'Sanchez', 'dob': '1965-09-13'}, {'first_name': 'Olivia', 'last_name': 'Taylor', 'dob': '1976-06-27'}, {'first_name': 'Anya', 'last_name': 'Lee', 'dob': '1952-10-21'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_muller_1116',
        instruction='You are assisting Daiki Muller, who wants to search for direct flights from LAS to MCO on 2024-05-20, followed by one-stop options for the same route and date, to evaluate available travel times. After reviewing options, you want to book a one-way direct flight from LAS to MCO on 2024-05-20 in economy class for two passengers: Daiki Muller and his granddaughter Aria Kim, because he prefers a reliable and straightforward journey. You prefer the early morning flight HAT137 departing at 07:00 AM, as it aligns with his travel plans and has available economy seating. You also want to include two total checked bags with no non-free bags and decline travel insurance, to keep the trip simple and cost-effective. You prefer to pay using your Visa card ending in 2135, which is your primary payment method on file. Later, you would like to update your existing reservation 59XX6W for the trip from LAS to ATL on 2024-05-19, by replacing passenger Chen Muller with Aria Kim (DOB 2010-08-15), to ensure your granddaughter is on both legs of the family trip, while keeping the total number of passengers unchanged.\n\nUse daiki_muller_1116 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_muller_1116', 'origin': 'LAS', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT137', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Muller', 'dob': '1954-07-04'}, {'first_name': 'Aria', 'last_name': 'Kim', 'dob': '2010-08-15'}], 'payment_methods': [{'payment_id': 'credit_card_2408938', 'amount': 392}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '59XX6W', 'passengers': [{'first_name': 'Daiki', 'last_name': 'Muller', 'dob': '1954-07-04'}, {'first_name': 'Aria', 'last_name': 'Kim', 'dob': '2010-08-15'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sophia_taylor_9065',
        instruction='You are Sophia Taylor, and you want to update your outbound flight from LGA to PHX on 2024-05-18 to a later afternoon departure, specifically flight HAT219 departing at 14:00, to better align with your meeting schedule. Later, you want to update your return flight from PHX to LGA on 2024-05-19 to an earlier morning departure, specifically flight HAT226 departing at 08:00, to arrive in New York by midday. You prefer both changes to remain in business class and to use your Visa card ending in 9796 for any fare difference. After that, you would like to cancel your old one-way basic economy reservation from BOS to MSP (via MCO) on 2024-05-15 and 2024-05-16, as you no longer need it and it is covered by travel insurance, and you want the refund issued back to the original payment method, your Visa card ending in 5191. Subsequently, you want to book a new one-way business class flight from BOS to MIA on 2024-05-20 for three passengers—yourself (Sophia Taylor), Lucas Davis, and Mason Khan—on flight HAT247 departing at 08:00, as it fits the conference start time. You prefer no paid baggage, no travel insurance, and to pay using your Visa card ending in 9796.\n\nUse sophia_taylor_9065 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'J3SAZF'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'J3SAZF', 'cabin': 'business', 'flights': [{'flight_number': 'HAT219', 'date': '2024-05-18'}, {'flight_number': 'HAT226', 'date': '2024-05-19'}], 'payment_id': 'credit_card_5237144'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'NABCQ2'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'BOS', 'destination': 'MIA', 'date': '2024-05-20'}),
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'MIA', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'sophia_taylor_9065', 'origin': 'BOS', 'destination': 'MIA', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT247', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Sophia', 'last_name': 'Taylor', 'dob': '1999-05-27'}, {'first_name': 'Lucas', 'last_name': 'Davis', 'dob': '1987-10-27'}, {'first_name': 'Mason', 'last_name': 'Khan', 'dob': '1983-09-06'}], 'payment_methods': [{'payment_id': 'credit_card_5237144', 'amount': 1224}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar_anderson_1185',
        instruction='You are to update the passenger on reservation 32J3PL from Omar Anderson (1961-06-18) to Fatima Jackson (1983-07-23) for a one-way economy flight from MIA to DFW via LAX, departing MIA on 2024-05-17 and arriving in DFW on 2024-05-18, because the original booking was made under the wrong passenger name. You want this change completed with no payment adjustment, as it is a correction of passenger information only.\n\nUse omar_anderson_1185 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': '32J3PL'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '32J3PL', 'passengers': [{'first_name': 'Fatima', 'last_name': 'Jackson', 'dob': '1983-07-23'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma_smith_9363',
        instruction="You are updating the passenger details for a round-trip reservation from PHL to DTW with a return via ORD, booked in basic economy. You want to correct the last name of passenger Ethan Kovacs to 'Kovac' in reservation E9TZTU because it was misspelled at the time of booking.\n\nUse emma_smith_9363 for authentication.",
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'E9TZTU'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'E9TZTU', 'passengers': [{'first_name': 'Emma', 'last_name': 'Smith', 'dob': '2000-08-19'}, {'first_name': 'Ethan', 'last_name': 'Kovac', 'dob': '1965-08-06'}]}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_johnson_4945',
        instruction='You are Evelyn Johnson, a gold member, who wants to book a direct economy flight from ORD to PHL on 2024-05-20 for two passengers: yourself and Mia Lopez, because you have changed your travel plans. You prefer the evening flight, specifically departing around 7:00 PM, as it aligns with your schedule. You prefer to pay using your Mastercard ending in 4357, which is your saved payment method. Later, you want to update the passenger list in your original reservation IZFHZ7 by replacing Mia Lopez with Noah Brown, as your companion has changed. After that, you would like to explore one-stop flight options from ORD to PHX on 2024-05-21 for possible future consideration, even though no direct connection to PHX is currently available. Finally, you intend to cancel your original reservation IZFHZ7, as it is no longer needed after the new booking and passenger update.\n\nUse evelyn_johnson_4945 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ORD', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'evelyn_johnson_4945', 'origin': 'ORD', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT271', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Johnson', 'dob': '1960-07-04'}, {'first_name': 'Mia', 'last_name': 'Lopez', 'dob': '1994-07-05'}], 'payment_methods': [{'payment_id': 'credit_card_4313689', 'amount': 370}], 'total_baggages': 2, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'IZFHZ7', 'passengers': [{'first_name': 'Evelyn', 'last_name': 'Johnson', 'dob': '1960-07-04'}, {'first_name': 'Noah', 'last_name': 'Brown', 'dob': '1995-03-15'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'IZFHZ7'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ORD', 'destination': 'PHX', 'date': '2024-05-21'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'IZFHZ7'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_martin_2396',
        instruction='You are assisting Ethan Martin, who wants to book a one-way direct evening flight from LGA to PHL on 2024-05-20 (flight HAT132) for one passenger in economy class, with one checked bag and no insurance, because he has changed his travel plans. You prefer to charge this booking to his Mastercard ending in 8023. After that, you would like to update the passenger name on existing reservation GXWCPN from Ethan Martin to Liam Johnson, who is a saved passenger in the account, to transfer the booking to him. Later, you want to cancel the updated reservation GXWCPN, which is a round-trip from LGA to BOS, because the trip is no longer needed, and you prefer the refund to be issued back to the same credit card ending in 8023.\n\nUse ethan_martin_2396 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ethan_martin_2396', 'origin': 'LGA', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT132', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ethan', 'last_name': 'Martin', 'dob': '1963-05-18'}], 'payment_methods': [{'payment_id': 'credit_card_5447957', 'amount': 166}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'GXWCPN', 'passengers': [{'first_name': 'Liam', 'last_name': 'Johnson', 'dob': '1976-08-23'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'GXWCPN'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'GXWCPN'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='anya_khan_1074',
        instruction='You are Anya Khan, and you want to cancel your one-way economy reservation 77VWO5 from DEN to LGA on 2024-05-18, which included a connection via PHL, because you no longer need that trip. Then, you would like to book a new one-way economy flight from DEN to MIA on 2024-05-20 for two passengers, Noah Muller and Sofia Patel, preferring an early morning departure since it is the only direct option available. You prefer to pay using your Visa card ending in 2560. Additionally, you want to update the passenger on your business-class round-trip reservation 2X85TD from yourself (Anya Khan) to Noah Muller, as he will now be traveling on that itinerary. Later, you would like to review the details of the canceled reservation 77VWO5 and explore alternative flight options from DEN to LGA on the original date of 2024-05-18. After checking, you prefer to see one-stop flight options on that route and date, particularly the connection via CLT departing DEN in the morning and arriving in LGA in the late afternoon, as it is a viable alternative.\n\nUse anya_khan_1074 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '77VWO5'}),
            Action(name='book_reservation', kwargs={'user_id': 'anya_khan_1074', 'origin': 'DEN', 'destination': 'MIA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT255', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Noah', 'last_name': 'Muller', 'dob': '1987-04-21'}, {'first_name': 'Sofia', 'last_name': 'Patel', 'dob': '1999-07-25'}], 'payment_methods': [{'payment_id': 'credit_card_1697462', 'amount': 278}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '2X85TD', 'passengers': [{'first_name': 'Noah', 'last_name': 'Muller', 'dob': '1987-04-21'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '77VWO5'}),
            Action(name='search_direct_flight', kwargs={'origin': 'DEN', 'destination': 'LGA', 'date': '2024-05-18'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'DEN', 'destination': 'LGA', 'date': '2024-05-18'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='aarav_nguyen_8793',
        instruction='You are Aarav Nguyen (DOB 1985-07-20), and you first want to explore flight options from Boston to Miami on May 16, 2024, for potential travel planning. Later, you want to update your existing business class reservation E02WYJ from Denver to Atlanta on May 18, 2024, to instead take a connecting flight via Las Vegas using HAT084 from Denver to Las Vegas in the early morning and HAT070 from Las Vegas to Atlanta in the late evening, both in business class, because you prefer the Las Vegas connection. After that, you want to cancel your basic economy round-trip reservation DIW7K4 from Boston to San Francisco, which was booked for Aarav Kim, and instead book a new one-way business class flight from Atlanta to Orlando on May 20, 2024, for yourself with one free checked bag and no insurance, because your travel plans have changed. You prefer the morning flight from Atlanta to Orlando on that date, and you want all charges and fare differences applied to your Mastercard ending in 6797.\n\nUse aarav_nguyen_8793 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'BOS', 'destination': 'MIA', 'date': '2024-05-16'}),
            Action(name='search_direct_flight', kwargs={'origin': 'BOS', 'destination': 'MIA', 'date': '2024-05-16'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'E02WYJ'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'E02WYJ', 'cabin': 'business', 'flights': [{'flight_number': 'HAT084', 'date': '2024-05-18'}, {'flight_number': 'HAT070', 'date': '2024-05-18'}], 'payment_id': 'credit_card_3207323'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'DIW7K4'}),
            Action(name='book_reservation', kwargs={'user_id': 'aarav_nguyen_8793', 'origin': 'ATL', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT203', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Aarav', 'last_name': 'Nguyen', 'dob': '1985-07-20'}], 'payment_methods': [{'payment_id': 'credit_card_3207323', 'amount': 323}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='ethan_nguyen_6045',
        instruction='You are to first cancel the existing round-trip reservation L1QGWV from LGA to PHL, as Ethan Nguyen has changed his travel plans. Then, you want to book a one-stop trip from LGA to LAS on 2024-05-20 for one passenger (Ethan Nguyen, DOB 1970-04-28) in economy class, consisting of flight HAT201 from LGA to PHX and connecting flight HAT259 from PHX to LAS, because this itinerary matches the requested route and date. You prefer to use the credit card ending in 3303 (Visa) on file for payment, and you want no checked bags or travel insurance added. Later, you would like to check the availability of direct flights from LGA to PHX on 2024-05-20 for future reference, and you note that there are direct options available in the evening, including one around 19:00 and another at 21:00.\n\nUse ethan_nguyen_6045 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'L1QGWV'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LGA', 'destination': 'LAS', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'ethan_nguyen_6045', 'origin': 'LGA', 'destination': 'LAS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT201', 'date': '2024-05-20'}, {'flight_number': 'HAT259', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Ethan', 'last_name': 'Nguyen', 'dob': '1970-04-28'}], 'payment_methods': [{'payment_id': 'credit_card_8005628', 'amount': 302}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LGA', 'destination': 'PHX', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='fatima_rossi_9268',
        instruction="You are to first cancel the existing round-trip economy reservation 5HK4LR from LAS to MIA because the customer's plans have changed. After that, you want to book a new one-way economy flight from LAS to MIA on 2024-05-17 for two passengers (Fatima Rossi and Mei Martin), specifically on flight HAT115, departing in the morning, with 1 total baggage (0 non-free) and no insurance, because the customer has decided on this one-way option. You prefer to pay using the credit card ending in 7369. Later, you would like to check the availability of direct flights from LAS to MIA on 2024-05-17 for future reference, which includes flight HAT115 as the only direct option on that route and date.\n\nUse fatima_rossi_9268 for authentication.",
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': '5HK4LR'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'LAS', 'destination': 'MIA', 'date': '2024-05-17'}),
            Action(name='book_reservation', kwargs={'user_id': 'fatima_rossi_9268', 'origin': 'LAS', 'destination': 'MIA', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT115', 'date': '2024-05-17'}], 'passengers': [{'first_name': 'Fatima', 'last_name': 'Rossi', 'dob': '1963-04-10'}, {'first_name': 'Mei', 'last_name': 'Martin', 'dob': '1952-09-12'}], 'payment_methods': [{'payment_id': 'credit_card_9469188', 'amount': 388}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='search_direct_flight', kwargs={'origin': 'LAS', 'destination': 'MIA', 'date': '2024-05-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='evelyn_rossi_4078',
        instruction='You are assisting Evelyn Rossi, a gold member, who wants to cancel her one-way business class reservation EZGELT for the late evening flight from MIA to LAS on 2024-05-21, as she no longer plans to travel on that route. She also wants to explore alternative flight options on the same route and date, preferring a direct flight if available, and if not, considering one-stop options; however, tool lookups confirm a direct flight (HAT062) is available in the late evening, so no further alternatives are needed. Later, you are to update her round-trip reservation 7SISHT from SFO to LAX, changing the passenger name from Evelyn Rossi to Lei Ahmed, as the trip is now for her saved passenger. You are also to add one additional checked bag, resulting in a total of two checked bags with one being paid, and you prefer to use her Mastercard ending in 7176 for the bag fee, as specified.\n\nUse evelyn_rossi_4078 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'EZGELT'}),
            Action(name='search_direct_flight', kwargs={'origin': 'MIA', 'destination': 'LAS', 'date': '2024-05-21'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'MIA', 'destination': 'LAS', 'date': '2024-05-21'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '7SISHT'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '7SISHT', 'passengers': [{'first_name': 'Lei', 'last_name': 'Ahmed', 'dob': '1997-11-08'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '7SISHT', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_7800202'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='lucas_brown_4047',
        instruction="You are Lucas Brown, and you want to cancel your one-way business class reservation UX0R03 from ORD to LGA on 2024-05-22 because you no longer need the trip. After that, you would like to explore alternative flight options from IAH to DTW on 2024-05-23, specifically checking for both direct and one-stop itineraries, but no such flights are currently available in the system. Separately, you need to update the passenger name in your round-trip reservation Q4TE65 from IAH to DTW on 2024-05-23 to ensure it correctly reflects 'Lucas Brown', although the name is already accurate. You also want to add 2 checked bags to this reservation and prefer to pay the baggage fee using your Mastercard ending in 8056, which is on file.\n\nUse lucas_brown_4047 for authentication.",
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'UX0R03'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'DTW', 'date': '2024-05-23'}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'DTW', 'date': '2024-05-23'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'Q4TE65'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'Q4TE65', 'passengers': [{'first_name': 'Lucas', 'last_name': 'Brown', 'dob': '1965-01-01'}]}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'Q4TE65', 'total_baggages': 2, 'nonfree_baggages': 2, 'payment_id': 'credit_card_7872117'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='daiki_patel_1917',
        instruction='You are assisting Daiki Patel (user_id: daiki_patel_1917) who had a business class flight from SFO to PHL on 2024-05-14 (reservation 0W60LB) that was cancelled. You want to book a new business class flight for Daiki Patel from SFO to PHL on 2024-05-20, specifically flight HAT074, which departs in the early morning, because it is the only available business class option on that date and matches the requested flight. You prefer to pay using the credit card ending in 1765, which is already on file. After that, you would like to cancel the original reservation 0W60LB due to the flight cancellation. Later, you want to update the existing round-trip reservation 7WKBKD (from PHX to JFK) to add one checked bag, increasing total_baggages and nonfree_baggages to 1, and charge the same credit card ending in 1765. Finally, you request a compensation certificate for the inconvenience caused by the cancellation of reservation 0W60LB.\n\nUse daiki_patel_1917 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'daiki_patel_1917', 'origin': 'SFO', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT074', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Daiki', 'last_name': 'Patel', 'dob': '1968-04-24'}], 'payment_methods': [{'payment_id': 'credit_card_4327297', 'amount': 306}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '0W60LB'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '7WKBKD'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '7WKBKD', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_4327297'}),
            Action(name='send_certificate', kwargs={'user_id': 'daiki_patel_1917', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='isabella_nguyen_4239',
        instruction='You are Isabella Nguyen (isabella_nguyen_4239), and you want to book a one-way one-stop flight from PHL to PHX on 2024-05-20, with the first leg on HAT291 departing PHL in the early morning and arriving in SFO, followed by HAT123 departing SFO in the afternoon and arriving in PHX, both in economy class, because this new trip better fits your updated travel plans. You are traveling alone and would like to include one free checked bag, with no insurance, because you prefer to keep costs lower. You prefer to pay using your Visa ending in 5063, as it is your primary card on file. Later, you want to cancel your original reservation 66NJCE for a one-way trip from PHL to EWR via CLT on 2024-05-28, because you no longer need it after booking the new itinerary, and you would like the refund issued back to the same Visa card. After that, you would like to explore direct flight options from PHL to EWR on 2024-05-28, possibly for future consideration or re-accommodation, even though no direct flights are currently available on that route and date.\n\nUse isabella_nguyen_4239 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'PHL', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'isabella_nguyen_4239', 'origin': 'PHL', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT291', 'date': '2024-05-20'}, {'flight_number': 'HAT123', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Isabella', 'last_name': 'Nguyen', 'dob': '1976-12-13'}], 'payment_methods': [{'payment_id': 'credit_card_8035954', 'amount': 249}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': '66NJCE'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '66NJCE'}),
            Action(name='search_direct_flight', kwargs={'origin': 'PHL', 'destination': 'EWR', 'date': '2024-05-28'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_hernandez_8403',
        instruction='You are Amelia Hernandez, and you want to book a new one-way flight from IAH to JFK on 2024-05-20 for four passengers: Mei Rossi, Raj Lopez, Noah Moore, and Olivia Anderson, in economy class, specifically on flight HAT085 departing in the early morning, because it matches your preferred schedule and route. You prefer to pay with your credit card ending in 5684 and want to add one checked bag with no non-free bags and no insurance. Later, you want to update the passenger details on your existing reservation XSPEPD to replace Mei Rossi with Isabella Johnson, because she is now traveling instead. After that, you want to change the flights on reservation XSPEPD to a one-stop itinerary: first, flight HAT190 from IAH to LAS on 2024-05-20 in the early morning, followed by flight HAT242 from LAS to PHX on the same day in the late morning, both in economy class, because this new route better fits your travel plans. You also want to update the baggage allowance on XSPEPD to two total bags, including one non-free bag, and pay any fare difference using your credit card ending in 5684. Separately, you are Daiki Lee, and you want a compensation certificate because your flight HAT244 was cancelled, which entitles you to compensation under airline policy.\n\nUse amelia_hernandez_8403 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'amelia_hernandez_8403', 'origin': 'IAH', 'destination': 'JFK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT085', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mei', 'last_name': 'Rossi', 'dob': '1974-03-22'}, {'first_name': 'Raj', 'last_name': 'Lopez', 'dob': '1963-09-13'}, {'first_name': 'Noah', 'last_name': 'Moore', 'dob': '1960-07-21'}, {'first_name': 'Olivia', 'last_name': 'Anderson', 'dob': '1980-11-11'}], 'payment_methods': [{'payment_id': 'credit_card_8830637', 'amount': 760}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'XSPEPD', 'passengers': [{'first_name': 'Isabella', 'last_name': 'Johnson', 'dob': '2000-04-03'}, {'first_name': 'Raj', 'last_name': 'Lopez', 'dob': '1963-09-13'}, {'first_name': 'Noah', 'last_name': 'Moore', 'dob': '1960-07-21'}, {'first_name': 'Olivia', 'last_name': 'Anderson', 'dob': '1980-11-11'}]}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'XSPEPD', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT190', 'date': '2024-05-20'}, {'flight_number': 'HAT242', 'date': '2024-05-20'}], 'payment_id': 'credit_card_8830637'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': 'XSPEPD', 'total_baggages': 2, 'nonfree_baggages': 1, 'payment_id': 'credit_card_8830637'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'XSPEPD'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'IAH', 'destination': 'JFK', 'date': '2024-05-20'}),
            Action(name='send_certificate', kwargs={'user_id': 'daiki_lee_7603', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='emma_kim_4489',
        instruction='You are Emma Kim, and you want to book a new one-stop flight from MIA to MCO on 2024-05-20 for yourself in economy class, with the first leg from MIA to BOS in the morning (flight HAT184) and the second leg from BOS to MCO in the evening (flight HAT013), because you need to reach Orlando by night. You prefer to pay using your credit card ending in 8019. Later, you want to update your existing round-trip reservation L3C753 from MIA to IAH and back to use a different routing via EWR and JFK in business class, as you prefer a more comfortable journey with preferred connections. Although the flights are already updated to HAT192 (MIA to EWR), HAT056 (EWR to IAH), HAT085 (IAH to JFK), and HAT209 (JFK to MIA) on the requested dates, you still need to change the passenger name from Ethan Anderson to Daiki Li with date of birth 1996-04-13, because the trip is now for a different traveler.\n\nUse emma_kim_4489 for authentication.',
        actions=[
            Action(name='search_onestop_flight', kwargs={'origin': 'MIA', 'destination': 'MCO', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'emma_kim_4489', 'origin': 'MIA', 'destination': 'MCO', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT184', 'date': '2024-05-20'}, {'flight_number': 'HAT013', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Emma', 'last_name': 'Kim', 'dob': '1993-06-15'}], 'payment_methods': [{'payment_id': 'credit_card_2704119', 'amount': 270}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': 'L3C753', 'cabin': 'business', 'flights': [{'flight_number': 'HAT192', 'date': '2024-05-23'}, {'flight_number': 'HAT056', 'date': '2024-05-24'}, {'flight_number': 'HAT085', 'date': '2024-05-28'}, {'flight_number': 'HAT209', 'date': '2024-05-28'}], 'payment_id': 'credit_card_2704119'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'L3C753', 'passengers': [{'first_name': 'Daiki', 'last_name': 'Li', 'dob': '1996-04-13'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'L3C753'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amelia_nguyen_8708',
        instruction='You are assisting Amelia Nguyen with two reservations. First, you want to cancel reservation BANTW5 for the one-way business class flight from ORD to PHL on 2024-05-21 because of a schedule conflict. As a result of this cancellation, you would like a $100 travel certificate issued as compensation for the inconvenience. Later, for reservation 23H76J, you want to upgrade both segments of the one-way economy flight from IAH to DFW via EWR on 2024-05-16 to business class to improve travel comfort. You also want to add one checked baggage to this reservation, paying the associated fee using the Mastercard ending in 1195 on file. Additionally, you want to correct the passenger name from Evelyn Rossi to Evelyn Muller, as the name was entered incorrectly during booking and the correct passenger is already in the account.\n\nUse amelia_nguyen_8708 for authentication.',
        actions=[
            Action(name='cancel_reservation', kwargs={'reservation_id': 'BANTW5'}),
            Action(name='get_reservation_details', kwargs={'reservation_id': '23H76J'}),
            Action(name='update_reservation_flights', kwargs={'reservation_id': '23H76J', 'cabin': 'business', 'flights': [{'flight_number': 'HAT149', 'date': '2024-05-16'}, {'flight_number': 'HAT231', 'date': '2024-05-16'}], 'payment_id': 'credit_card_2427893'}),
            Action(name='update_reservation_baggages', kwargs={'reservation_id': '23H76J', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_2427893'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': '23H76J', 'passengers': [{'first_name': 'Amelia', 'last_name': 'Nguyen', 'dob': '1976-10-21'}, {'first_name': 'Evelyn', 'last_name': 'Muller', 'dob': '1992-09-03'}]}),
            Action(name='search_direct_flight', kwargs={'origin': 'IAH', 'destination': 'DFW', 'date': '2024-05-16'}),
            Action(name='send_certificate', kwargs={'user_id': 'amelia_nguyen_8708', 'amount': 100}),
        ],
        outputs=[],
    ),

    Task(
        user_id='mia_silva_9133',
        instruction='You are Mia Silva, and you want to book a one-way direct afternoon flight from SFO to PHX on 2024-05-20 (flight HAT123) for yourself and Amelia Johansson in economy class, because it fits your travel plans and has available seats. You prefer to pay using your Visa card ending in 7854. Later, you want to update the passenger on your existing business-class round-trip reservation from DFW to LAX (reservation P1D9KS) from Amelia Johansson to yourself, to correct the traveler information. After confirming the update, you would like to cancel that reservation and receive a refund to the same Visa card ending in 7854, because you have travel insurance that allows for cancellations. You do not need to search for one-stop flights, as a suitable direct flight is available.\n\nUse mia_silva_9133 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'SFO', 'destination': 'PHX', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'mia_silva_9133', 'origin': 'SFO', 'destination': 'PHX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT123', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Mia', 'last_name': 'Silva', 'dob': '1990-06-25'}, {'first_name': 'Amelia', 'last_name': 'Johansson', 'dob': '1966-05-22'}], 'payment_methods': [{'payment_id': 'credit_card_3163658', 'amount': 208}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'P1D9KS', 'passengers': [{'first_name': 'Mia', 'last_name': 'Silva', 'dob': '1990-06-25'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'P1D9KS'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'P1D9KS'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'SFO', 'destination': 'PHX', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='chen_lee_6825',
        instruction='You are Chen Lee, a gold member, and you want to book a one-way business class flight from ORD to PHL on 2024-05-20 for yourself, departing in the evening, because you prefer a direct flight on that date. You prefer to pay using your Visa card ending in 9990. You also want to ensure passenger details are accurate in the new reservation and then retrieve the updated reservation details. Later, you want to cancel your existing round-trip business class reservation from ORD to LAS, as you are changing your travel plans. After that, you would like to explore one-stop flight options from ORD to PHL on 2024-05-20 for future consideration.\n\nUse chen_lee_6825 for authentication.',
        actions=[
            Action(name='search_direct_flight', kwargs={'origin': 'ORD', 'destination': 'PHL', 'date': '2024-05-20'}),
            Action(name='book_reservation', kwargs={'user_id': 'chen_lee_6825', 'origin': 'ORD', 'destination': 'PHL', 'flight_type': 'one_way', 'cabin': 'business', 'flights': [{'flight_number': 'HAT139', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Chen', 'last_name': 'Lee', 'dob': '1967-12-12'}], 'payment_methods': [{'payment_id': 'credit_card_4938634', 'amount': 445}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'HATHAT', 'passengers': [{'first_name': 'Chen', 'last_name': 'Lee', 'dob': '1967-12-12'}]}),
            Action(name='get_reservation_details', kwargs={'reservation_id': 'HATHAT'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'JW6LEQ'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ORD', 'destination': 'PHL', 'date': '2024-05-20'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah_li_4844',
        instruction='You are assisting Noah Li (user_id: noah_li_4844) who initially wanted to review his existing reservation OT24RL for a round-trip from ORD to CLT. After reviewing, he decided to cancel this reservation because he prefers to travel one-way from ORD to ATL instead. You want to cancel reservation OT24RL. Later, you would like to book a new one-way flight from ORD to ATL on 2024-05-20 in economy class for one passenger (Noah Li, DOB 1971-10-17), with no checked bags and no insurance. You prefer to use your saved credit card (ending in 6835549) for payment. The preferred flight is HAT093, which departs early morning (02:00 AM) and arrives at 04:00 AM. After that, you would like to confirm that the passenger details on reservation NU92ZQ still reflect Noah Li, which they do. Additionally, due to a previous flight delay, you would like a $50 compensation certificate issued and sent to your account, as per airline policy.\n\nUse noah_li_4844 for authentication.',
        actions=[
            Action(name='get_reservation_details', kwargs={'reservation_id': 'OT24RL'}),
            Action(name='search_direct_flight', kwargs={'origin': 'ORD', 'destination': 'ATL', 'date': '2024-05-20'}),
            Action(name='search_onestop_flight', kwargs={'origin': 'ORD', 'destination': 'ATL', 'date': '2024-05-20'}),
            Action(name='cancel_reservation', kwargs={'reservation_id': 'OT24RL'}),
            Action(name='book_reservation', kwargs={'user_id': 'noah_li_4844', 'origin': 'ORD', 'destination': 'ATL', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT093', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Noah', 'last_name': 'Li', 'dob': '1971-10-17'}], 'payment_methods': [{'payment_id': 'credit_card_6835549', 'amount': 120}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'}),
            Action(name='update_reservation_passengers', kwargs={'reservation_id': 'NU92ZQ', 'passengers': [{'first_name': 'Noah', 'last_name': 'Li', 'dob': '1971-10-17'}]}),
            Action(name='send_certificate', kwargs={'user_id': 'noah_li_4844', 'amount': 50}),
        ],
        outputs=[],
    ),
]
