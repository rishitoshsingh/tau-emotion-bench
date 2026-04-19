from tau_emotion_bench.types import Task, Action


TASKS = [
    Task(
        user_id='melanie.chambers@tracer-health.org',
        instruction="You are Melanie Chambers (melanie.chambers@tracer-health.org), a patient with hypertension and type 2 diabetes. You want to explore available cardiology specialists for potential referral, because you are considering expanding your care team to better manage your cardiovascular health. You would like to review the details of Dr. Brandi Dixon, a cardiologist with 20 years of experience and board certification, because you are interested in her expertise and availability. You need to cancel your follow-up appointment with Dr. Charles Lewis on December 17, 2025, at 9:00 AM, because of a scheduling conflict. After that, you would like to reschedule your medication review appointment with your primary care provider, Dr. Howard McCarthy, to Friday, December 19, 2025, at 11:00 AM, because that time works better for your schedule and is within Dr. McCarthy's available hours.\n\nUse melanie.chambers@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brandi_dixon_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_085'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_107', 'new_date': '2025-12-19', 'new_time': '11:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction="You are Yumi Tanaka, authenticated via yumi.tanaka7410@pacificcare.org, and you want to explore alternative suppliers for your Warfarin prescription in medical record REC012 to reduce medication costs. You prefer to update your prescription to use VedaRx Labs (brand: Vedarin) at $4.28 because it offers a slightly lower price than your current supplier. You also want a note added to the medical record stating 'Patient requested supplier update after price comparison' to document your decision. After the update, you would like to review the revised medical record to confirm the changes were applied correctly.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC012', 'note': 'Patient requested supplier update after price comparison'}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC012'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elena.morales9921@westcare.org',
        instruction='You are Elena Morales, a patient with focal epilepsy and generalized anxiety disorder, preparing for wearable EEG telemetry and seeking to optimize medication costs. You want to check available suppliers for your Lamotrigine prescription to explore more affordable options, and you would like a note added to your medical record confirming this inquiry for future reference. Later, you would like to cancel your scheduled neurology consultation on 2025-07-22 at 10:30 with Dr. Ivankovic and reschedule it to the following Tuesday at 10:30, which better aligns with your preparation timeline for telemetry setup.\n\nUse elena.morales9921@westcare.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lamotrigine'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC015', 'note': 'Patient requested supplier pricing information for Lamotrigine'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT035'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'elena_morales_9921', 'provider_id': 'dr_ivankovic_neurology', 'date': '2025-07-29', 'time': '10:30', 'appointment_type': 'specialist_consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, and you are considering starting Sertraline for mood support, but due to a high-severity interaction with Warfarin that increases bleeding risk, you want to discuss alternative antidepressants with your care team before proceeding. You would like to reduce the cost of your Atorvastatin prescription and prefer switching to a lower-cost supplier such as Sunrise Biotech (Lipistal, $4.15) from India, which offers significant savings compared to current options. You also want to reschedule your cardiology appointment with Dr. Sims from its current time to the next day at 14:00, as it better fits your schedule, and you plan to confirm this change after reviewing the interaction risks with your provider.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_123', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_128', 'new_date': '2025-12-18', 'new_time': '14:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='renee.freeman@tracer-health.org',
        instruction="You are Renee Freeman, managing care for your children, and you want to reschedule your pediatric consultation with Dr. Nguyen from its current date to next day at 09:00 because it works better with your family's schedule. Later, you would like to cancel your care coordination appointment with Dylan Hampton on the following day, as you will not be able to attend. After that, you would like to confirm the updated details of your rescheduled pediatric appointment and review your full list of scheduled appointments to ensure everything is correct.\n\nUse renee.freeman@tracer-health.org for authentication.",
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_198', 'new_date': '2025-12-19', 'new_time': '09:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_199'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_198'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'renee_freeman_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction='You are Diane Robinson (diane.robinson@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to first review the details of your upcoming endocrinology follow-up appointment on 2025-12-17 and its associated medical record to stay informed about your current treatment plan. After that, you would like to schedule a routine checkup with Dr. Dana Padilla, a primary care provider, on 2025-12-22 at 11:00 because it aligns with your availability and fits within her confirmed bookable hours. You prefer to use your insurance for billing this visit.\n\nUse diane.robinson@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'diane_robinson_tracer_0001', 'provider_id': 'dana_padilla_primary_care_tracer_0001', 'date': '2025-12-22', 'time': '11:00', 'appointment_type': 'routine_checkup', 'bill_insurance': True}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks, a patient managing atrial fibrillation and hyperlipidemia, currently taking Warfarin and Atorvastatin. You want to explore more affordable supplier options for your Atorvastatin medication because you are looking to reduce out-of-pocket costs, and VedaRx Labs in India offers a lower-cost alternative. You would like to reschedule your medication review appointment with Dr. Saito, your cardiologist, from the original date to Friday, because it better fits your schedule. After rescheduling, you would like confirmation of the updated appointment details to ensure the change was processed correctly and that your telehealth visit is set for the new time.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_177', 'new_date': '2025-12-19', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_177'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='patrick.rangel@tracer-health.org',
        instruction='You are Patrick Rangel (patrick.rangel@tracer-health.org), a patient managing depression and insomnia with Sertraline and Zolpidem. You would like to schedule a new routine checkup with Dr. Margaret Thompson, a cardiologist, on the next day at 14:00 for a second opinion. Later, you would like to reschedule your existing specialist consultation with Dr. Robert Smith, also a cardiologist, from the morning to 16:00 on the same day (today) to better fit your schedule.\n\nUse patrick.rangel@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'patrick_rangel_tracer_0001', 'provider_id': 'dr_thompson_cardiology', 'date': '2025-12-18', 'time': '14:00', 'appointment_type': 'routine_checkup'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_124', 'new_date': '2025-12-17', 'new_time': '16:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez (amanda.martinez@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, currently managing your condition with Insulin Lispro and Levothyroxine. You want to evaluate the safety of switching to a new insulin brand, Lispry by Lotus Rapid Therapeutics, because you are seeking more accessible and cost-effective options. After confirming no adverse interactions with your current medications, you would like to update your prescription in medical record REC_tracer_063 to reflect the new supplier details: company Lotus Rapid Therapeutics, brand_name Lispry, and price_usd 19.75, because it aligns with your goal of optimizing medication access. Finally, you want to review your complete regimen options to compare costs, pill burden, and adherence support, so you can make an informed decision about your long-term treatment plan.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lispry', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_063', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold (email: kevin.arnold@tracer-health.org). Because of some time conflicts, you need to cancel my follow-up appointment APPT_tracer_080 scheduled for 2025-12-17 at 09:00 with Dr. Christine Bailey. After this, you want to see all your appointments so that there is nothing conflicting with your other meetings.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='nadia.abbasi@tracer-health.org',
        instruction="You are Nadia Abbasi (nadia.abbasi@tracer-health.org), a patient with hypertension and type 2 diabetes managing medication costs. You want to cancel your medication review appointment with Dr. Garcia on 2025-11-30 at 09:30 because you prefer to address medication concerns during a routine checkup instead. You would like to schedule a new routine checkup with Dr. Garcia on 2025-12-03 at 10:00 because it aligns with your availability and allows for a comprehensive review. Later, you will reschedule your medication review appointment with Dr. Ortega from 2025-12-01 at 08:00 to 2025-12-02 at 09:00 to better coordinate with your work schedule. After that, you would like to update your medical record to reflect a switch to Mumbai Cardio Pharma for Lisinopril (brand: Lisipril-M, price: $2.80) because it significantly reduces your out-of-pocket costs, and you request a note be added stating 'Patient requested supplier update for cost savings.'\n\nUse nadia.abbasi@tracer-health.org for authentication.",
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_063'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_garcia_primary'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_063'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'nadia_abbasi_tracer_0001', 'provider_id': 'dr_garcia_primary', 'date': '2025-12-03', 'time': '10:00', 'appointment_type': 'routine_checkup'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_072', 'new_date': '2025-12-02', 'new_time': '09:00'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_040', 'note': 'Patient requested supplier update for cost savings.'}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_040', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.barnes@tracer-health.org',
        instruction="You are Sarah Barnes, and your email is sarah.barnes@tracer-health.org. You want to reschedule your medication review appointment with Dr. Charles Barajas from December 17, 2025, to December 24, 2025, at 09:00, because it better fits your schedule and the time is available in the provider's calendar. If rescheduling is not possible, you would like to cancel the current appointment. You also want to explore cost-saving options for your Lisinopril prescription because you are concerned about ongoing medication expenses. After identifying Mumbai Cardio Pharma (brand name Lisipril-M) as the lowest-cost supplier at $2.80 per unit, you would like to update your medical record to reflect this supplier information to support future pharmacy fulfillment and adherence.\n\nUse sarah.barnes@tracer-health.org for authentication.",
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_176', 'new_date': '2025-12-24', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_176'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_176'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_barnes_tracer_0001', 'provider_id': 'charles_barajas_primary_care_tracer_0001', 'date': '2025-12-24', 'time': '09:00', 'appointment_type': 'medication_review'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'charles_barajas_primary_care_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_120', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, a patient with atrial fibrillation and hyperlipidemia using a cardiac event monitor, and your email is shawn.carter@tracer-health.org. You want to review the telemetry upload history for your device because you noticed a gap in the data on December 14th when no usage was recorded. You also want to cancel your upcoming cardiology follow-up appointment with Dr. Owen Shaw because of a scheduling conflict. After that, you would like to reschedule your device coaching session with Anthony Moran from the morning of December 17th to 9:00 AM on December 22nd because it works better for your schedule and aligns with the coach’s availability. Later, you want to explore more affordable options for your Warfarin prescription because of cost concerns, and you prefer to update your prescription to use the supplier VedaRx Labs with the brand name Vedarin due to lower per-unit pricing. You also want confirmation that switching to this formulation does not introduce any drug interactions with your current medications, particularly Atorvastatin, which has been confirmed safe.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_461'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_131'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_130', 'new_date': '2025-12-22', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_131'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_122', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction="You are Diane Robinson (diane.robinson@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to cancel your scheduled endocrinology follow-up appointment with Dr. Ashley Schneider on 2025-12-17 at 09:00 due to a scheduling conflict. You would like to review Dr. Caleb Turner's background because you are considering continuity with providers familiar with complex endocrine cases, and you want to explore other available endocrinologists for future care options. You prefer to schedule a new follow-up appointment with Dr. Kelly Taylor on 2025-12-18 at 13:00 because it aligns with your availability and maintains timely diabetes and thyroid management. Additionally, you need to confirm that your Continuous Glucose Monitor (device ID: CONTIN_tracer_484) is properly assigned to you and would like to verify its data upload history to ensure consistent glucose monitoring, especially since recent uploads appear to be missing, which could impact your treatment plan.\n\nUse diane.robinson@tracer-health.org for authentication.",
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'caleb_turner_endocrinology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'diane_robinson_tracer_0001', 'provider_id': 'kelly_taylor_endocrinology_tracer_0001', 'date': '2025-12-18', 'time': '13:00', 'appointment_type': 'follow_up'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_484'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction="You are Laurie Carson (laurie.carson@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to reschedule your endocrinology follow-up appointment with Dr. Caleb Turner (Endocrinology) from its current date to next day at 10:00 because it works better with your schedule. You also want to confirm Dr. Turner's provider details for continuity of care. You would like to verify that switching your Insulin Lispro supplier to Bengal EndoCare (brand: SwiftLis) is safe, which aligns with your current medications and has no interactions. After confirmation, you prefer to update your prescription in your medical record to use the lower-cost supplier to reduce out-of-pocket expenses. Later, you would like to cancel your primary care medication review appointment because the cost discussion will now be covered during your endocrinology visit, and you want to confirm the details of the appointment being cancelled.\n\nUse laurie.carson@tracer-health.org for authentication.",
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_082', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'caleb_turner_endocrinology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_071', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_104'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_104'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction='You are Matthew Smith, a 44-year-old male managing Atrial Fibrillation and Hyperlipidemia through telehealth, with email matthew.smith@tracer-health.org. You want to cancel your device coaching appointment with Robert Wright on 2025-12-17 at 09:00 due to a scheduling conflict. You would like to reschedule your cardiology consultation with Dr. Christine Bailey from 2025-12-17 at 10:00 to 2025-12-22 at 14:00 because the later date better fits your availability. After confirming the safety of adding Zolpidem, you want to check for drug interactions with your current medications (Warfarin, Atorvastatin, Bupropion) to ensure no adverse effects, particularly given the low-risk interaction with Bupropion. Subsequently, you would like to update your Warfarin prescription in medical record REC_tracer_134 to use the more affordable supplier VedaRx Labs, brand name Vedarin, to reduce monthly costs and improve long-term adherence.\n\nUse matthew.smith@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_170'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_122', 'new_date': '2025-12-22', 'new_time': '14:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_122'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'matthew_smith_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin', 'Bupropion']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_134', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, a patient with atrial fibrillation and hyperlipidemia, and you want to reschedule your medication review appointment with Dr. Guzman from its current date to the next day at 14:00 because it works better with your schedule. You would like to confirm there are no harmful interactions between Warfarin and your current medications, particularly Atorvastatin, to ensure safe continuation of your regimen. You prefer to update the supplier for Warfarin in your medical record to VedaRx Labs, using the brand name Vedarin, as it offers a more cost-effective option. Later, you will need to verify the telemetry upload for your cardiac event monitor on the previous day, as the system shows no usage data, which may affect compliance tracking for your upcoming cardiology follow-up. You prefer to pay by standard insurance copay for any services rendered.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_186', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kayla_guzman_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_130', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_469', 'date': '2025-12-14'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond, a patient with atrial fibrillation and hyperlipidemia, and your email is kevin.bond@tracer-health.org. You want to cancel your scheduled cardiology follow-up appointment with Dr. Saito on 2025-12-17 at 07:30 due to a scheduling conflict. You also want to review your other scheduled appointments, which include a medication review with Megan Cook at 09:00 and a specialist consultation with Bryan Bryant at 10:00 on the same day. Later, you would like to check for potential drug interactions between Warfarin and your current medications (Warfarin, Atorvastatin, Bupropion), and upon confirmation of no high-risk interactions, you prefer to update the Warfarin prescription in your medical record to use the supplier VedaRx Labs with brand name Vedarin at a lower cost of 4.28 USD to reduce monthly medication expenses. After that, you want to verify telemetry data uploads for your cardiac event monitor (device ID: CARDIA_tracer_485), specifically noting that no data was uploaded on 2025-12-15, so you would like to investigate and resolve the missing upload for that day.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_081'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin', 'Bupropion']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_132', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_485', 'date': '2025-12-15'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and your email is scott.sparks@tracer-health.org. You want to reschedule your medication review appointment with Dr. Hiroko Saito from the morning of 2025-12-17 to the next day, 2025-12-18, at 10:00 because it better fits your schedule. Later, you would like to cancel your device coaching session on 2025-12-17 at 09:00 since you have independently resolved the upload issue. After that, you would like to review the details of your rescheduled medication appointment with Dr. Saito and access the associated medical record for reference. Finally, you prefer to receive information about available suppliers for Atorvastatin to evaluate cost options, and you would like a comparison of your current regimen with optimized alternatives to assess potential improvements in cost efficiency and medication adherence.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_177', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_162'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_177'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_177'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='nadia.abbasi@tracer-health.org',
        instruction='You are Nadia Abbasi, a patient managing hypertension and type 2 diabetes, and your email is nadia.abbasi@tracer-health.org. You want to explore more affordable options for your Lisinopril medication because of cost concerns, and you would like to document this inquiry in your medical record. You prefer to switch the supplier for your Lisinopril prescription to Mumbai Cardio Pharma (brand: Lisipril-M) because it is a safe, lower-cost option at $2.80 per month and no drug interactions were found with your current medications, including Metformin. Later, you would like to cancel your scheduled medication review appointment on 2025-12-01 because your prescription update has already been planned and documented. After that, you want to explore available providers for a future telehealth visit to continue managing your chronic conditions, with a preference for specialists experienced in internal or endocrine care.\n\nUse nadia.abbasi@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_034', 'note': 'Patient requested supplier pricing information for Lisinopril.'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_034', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_072'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks, authenticated via scott.sparks@tracer-health.org, and you want to cancel your scheduled device coaching appointment with Joseph Robertson (RN) on 2025-12-17 at 09:00 because of a scheduling conflict. You would like to schedule a new cardiology follow-up appointment with Dr. Margaret Thompson (MD) on 2025-12-22 at 09:00, as this time is available and aligns with your preference for a specialist follow-up. You are also reviewing your medication regimen and want information on Atorvastatin suppliers to evaluate cost-effective options, particularly noting international and domestic availability. You would like to confirm there are no interactions between Atorvastatin and your current medications, especially Warfarin, for safety assurance—no high-risk interactions were found. Finally, you want the details of your original appointment APPT_tracer_162 and the professional credentials of your device coach Joseph Robertson for your personal health records.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_162'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'scott_sparks_tracer_0001', 'provider_id': 'dr_thompson_cardiology', 'date': '2025-12-22', 'time': '09:00', 'appointment_type': 'follow_up'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_162'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'joseph_robertson_device_coaching_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='linda.parker@email.com',
        instruction='You are Linda Parker, and your email is linda.parker@email.com. You would like to schedule a new telehealth consultation with Dr. Robert Smith, a cardiologist, for a general heart health evaluation because it aligns with your current health focus. You prefer the appointment on Monday, June 10, 2024, at 10:00 AM, as it fits your schedule. You have Cigna insurance and would like to use it for billing this visit.\n\nUse linda.parker@email.com for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'linda_parker_8899', 'provider_id': 'dr_smith_cardiology', 'date': '2024-06-10', 'time': '10:00', 'appointment_type': 'consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, a patient managing atrial fibrillation and hyperlipidemia, who wants to reduce medication costs and adjust your appointment timing for better convenience. You would like to explore more affordable suppliers for Atorvastatin because you are looking to lower your prescription expenses, and you prefer options with lower pill burden and cost-effective sourcing. Later, you want to reschedule your medication review appointment with Dr. Smith from its current date to next Monday at 11:00 AM, because it works better with your schedule. You prefer telehealth visits for continuity and convenience, and you would like to maintain insurance-based copay billing for the visit.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_178', 'new_date': '2025-12-22', 'new_time': '11:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction="You are Sarah Johnson, a patient managing hypertension and type 2 diabetes, and your email is sarah.johnson@email.com. You would like to explore lower-cost suppliers for your Lisinopril 10mg prescription to reduce out-of-pocket expenses, as there are international options available at significantly lower prices. You also want to reschedule your routine checkup with your primary care provider, Dr. Carlos Garcia, from January 15 to January 17 at 10:00 AM, because the new time better fits your schedule and aligns with the provider's availability. After that, you would like confirmation of both the updated appointment and the supplier options for your medication.\n\nUse sarah.johnson@email.com for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT001', 'new_date': '2024-01-17', 'new_time': '10:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction="You are Kevin Arnold, with email kevin.arnold@tracer-health.org, and you want to reschedule your follow-up cardiology appointment with Dr. Christine Bailey from 2025-12-17 to the next day, 2025-12-18, because of a scheduling conflict. You prefer the appointment at 10:00 AM as it aligns with your availability and fits within the provider's schedule.\n\nUse kevin.arnold@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_080', 'new_date': '2025-12-18', 'new_time': '10:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction="You are Scott Sparks (scott.sparks@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia managing Warfarin and Atorvastatin. You want to consult with available cardiology providers and specifically review Dr. Margaret Thompson's credentials because you are considering long-term cardiac care. You would like to confirm there are no drug interactions between Warfarin and Atorvastatin, which is important for your safety given your dual therapy. You prefer to update your prescription supplier for Warfarin to VedaRx Labs (Vedarin) at $4.28 and for Atorvastatin to VedaRx Labs (Atorveeda) at $4.05 in your medical record, as this is the most cost-effective option. You want to check the available suppliers for both medications to verify pricing and confirm that VedaRx Labs offers the lowest cost. You would like to see your current regimen options to ensure alignment with cost and adherence goals. You need to add a note to your medical record stating 'Updated prescription suppliers based on cost analysis' for audit and continuity. You prefer to reschedule your medication review appointment with Dr. Hiroko Saito from 09:30 to 10:30 on 2025-12-17 because the later time fits better with your morning routine. You also want to cancel your duplicate consultation with Dr. Juan Fitzgerald because it is no longer needed. Finally, you would like to schedule a new specialist consultation with Dr. Margaret Thompson on 2025-12-18 at 09:00 to discuss long-term management of your cardiac conditions, as her expertise and availability align with your care planning.\n\nUse scott.sparks@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_121', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_121', 'note': 'Updated prescription suppliers based on cost analysis.'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_177'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_177', 'new_date': '2025-12-17', 'new_time': '10:30'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_126'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'scott_sparks_tracer_0001', 'provider_id': 'dr_thompson_cardiology', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'specialist_consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='tammy.carr@tracer-health.org',
        instruction='You are Tammy Carr, a patient with Type 2 Diabetes and Hypertension, and your email is tammy.carr@tracer-health.org. You want to reschedule your medication review appointment with your primary care provider, Dr. Charles Lewis, from December 17 to December 18, 2025, at 09:00, because it works better with your schedule. You also want to schedule a new cardiology consultation on December 19, 2025, at 10:00 with Dr. Megan Cook, as she is an available and qualified cardiologist, because you seek a specialist opinion. After confirming the new cardiology appointment, you would like to cancel your original appointment with Dr. Charles Lewis if the new one is confirmed. You prefer to update your Lisinopril prescription to use the lower-cost supplier Mumbai Cardio Pharma (brand: Lisipril-M, $2.80) because it reduces your medication expenses, and you have confirmed that adding Sertraline to your current regimen of Metformin and Lisinopril is safe with no significant interactions.\n\nUse tammy.carr@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_180', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'tammy_carr_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_180'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'charles_lewis_primary_care_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'tammy_carr_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-19', 'time': '10:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_180'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_124', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'tammy_carr_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson, a patient with Type 1 Diabetes and Hypothyroidism managing your care through telehealth. You want to check the telemetry upload for your Continuous Glucose Monitor (CONTIN_tracer_480) on 2025-12-17 because you had connectivity issues that day and want to confirm data was captured. You also want to check for drug interactions between Insulin Lispro and your current medications (Insulin Lispro and Levothyroxine) to ensure safety before making any changes. You would like to update your prescription supplier for Insulin Lispro in record REC_tracer_071 to Bengal EndoCare (brand: SwiftLis) because it is the most affordable option at $19.20 per unit without compromising therapeutic equivalence. Later, you want to reschedule your device coaching appointment with Riley Stone from 2025-12-17 at 09:00 to 2025-12-19 at 10:00 because the new time better fits your schedule. After that, you would like to see all your scheduled appointments to review your upcoming care plan. You then want to cancel your medication review appointment APPT_tracer_104 because its purpose has been addressed in the updated prescription plan. You also need the details for appointment APPT_tracer_168 to access the meeting link and prepare for the rescheduled session. Subsequently, you want to list suppliers for Insulin Lispro to confirm Bengal EndoCare offers the lowest price. You would like to get your regimen options to evaluate cost and adherence improvements. You need to retrieve your medical record REC_tracer_071 to review the updated prescription and clinical rationale. Finally, you want to list all your medical records to ensure comprehensive oversight of your care documentation.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_480', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_071', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_168', 'new_date': '2025-12-19', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_104'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_168'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_071'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='michelle.adams@tracer-health.org',
        instruction='You are Michelle Adams, a patient with Type 1 Diabetes and Hypothyroidism, and your email is michelle.adams@tracer-health.org. You want to cancel your scheduled medication review appointment with Dr. Nicholas Salinas because your cost concerns have been resolved. You would like to reschedule your endocrinology follow-up appointment with Dr. Charles Scott to Thursday, December 18th at 10:00 AM because it better fits your schedule. You prefer Dr. Charles Scott, an endocrinology specialist with 19 years of experience, for continuity of care. You also want to review the details of your upcoming appointment and its associated medical record to stay informed about your treatment plan. After that, you would like to see a list of other available providers in case you need to book with someone else in the future.\n\nUse michelle.adams@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_110'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'charles_scott_endocrinology_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'michelle_adams_tracer_0001', 'provider_id': 'nicholas_salinas_primary_care_tracer_0001', 'date': '2025-12-17', 'time': '08:00', 'appointment_type': 'medication_review'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_087', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_087'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_087'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold, authenticated at kevin.arnold@tracer-health.org, managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to confirm there are no harmful interactions between your medications, which is important for your safety—tool results show no high-risk interactions between Warfarin and Atorvastatin. You would like to update your Warfarin prescription in medical record REC_tracer_131 to use VedaRx Labs with the brand name Vedarin at $4.28 per tablet, because it supports cost efficiency and aligns with your current regimen plan. You prefer to review your full medication regimen options as patient kevin_arnold_tracer_0001 to evaluate cost-synchronized generics and adherence packaging alternatives for better affordability and routine support. You also want to check telemetry data from your device VC-449, specifically the 7.4 hours of usage recorded on 2025-06-01, to ensure consistent monitoring. Later, you intend to cancel your scheduled virtual medication review appointment APPT_tracer_187 with Dr. Luis Sims on 2025-12-17 because you wish to explore other care options. After that, you would like to see available providers and get details about Dr. Luis Sims, a cardiologist with 22 years of experience, to inform your decision on future care continuity.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_131', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_131'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'VC-449', 'date': '2025-06-01'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_187'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'luis_sims_cardiology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, a patient managing atrial fibrillation and hyperlipidemia through telehealth, and your email is shawn.carter@tracer-health.org. You want to cancel your scheduled medication review appointment because you prefer to streamline your care plan. You would like to reschedule your specialist consultation to the next day in the morning because it better aligns with your availability. After that, you want to book a new routine checkup with Dr. Megan Cook, a cardiologist, on the following day at 09:00 because you prefer continuity with a trusted provider. You also want to compare medication suppliers for Atorvastatin to evaluate cost-effective options. You would like to review your current and optimized regimen plans to understand potential savings and adherence benefits. Additionally, you want to see your cardiac event monitor usage data from the past week to ensure you are meeting compliance targets.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_carter_tracer_0001', 'provider_id': 'megan_cook_cardiology_tracer_0001', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_131'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_178'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_127', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_461', 'start_date': '2025-12-10', 'end_date': '2025-12-16'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction="You are Scott Sparks (scott.sparks@tracer-health.org), managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to reduce medication costs by switching your Atorvastatin prescription to a lower-cost supplier, specifically VedaRx Labs (brand Atorveeda, $4.05), because it offers significant savings over other options and there are no high-risk interactions with your current medications, including Warfarin. You would like this change documented in medical record REC_tracer_121, along with a note stating 'Patient requested supplier update for cost savings' to reflect your intent. You also want to confirm the details of your upcoming specialist consultation with Dr. Juan Fitzgerald, a cardiologist with 19 years of experience, scheduled for 2025-12-17 at 14:00 via telehealth, because you need to review potential interactions between your sleep medication and current antidepressant. Finally, you need to verify your cardiac event monitor (CARDIA_tracer_477) usage data, noting a missed upload on 2025-12-14 with 0.0 hours recorded, to ensure compliance with monitoring requirements and maintain accurate health tracking.\n\nUse scott.sparks@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_121', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_121', 'note': 'Patient requested supplier update for cost savings.'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'juan_fitzgerald_cardiology_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_126'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_126'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_477'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='melanie.chambers@tracer-health.org',
        instruction="You are Melanie Chambers, authenticated via melanie.chambers@tracer-health.org, and you want to reschedule your medication review appointment with Dr. Howard McCarthy from Wednesday, December 17th at 08:00 to the next day, Thursday, December 18th at 09:00, because it better fits your schedule. The new time is confirmed as available in Dr. McCarthy's calendar and aligns with your preference for a morning virtual visit.\n\nUse melanie.chambers@tracer-health.org for authentication.",
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_107', 'new_date': '2025-12-18', 'new_time': '09:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, with email edward.rice@tracer-health.org, managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to reduce medication costs by switching the supplier for Atorvastatin to VedaRx Labs with brand name Atorveeda, because it is more affordable, and you have confirmed no dangerous interactions with your current regimen. You would like to review telemetry data for your cardiac monitor device CARDIA_tracer_465, specifically the upload from December 17, 2025, because you want to monitor your cardiac health. You prefer to reschedule your medication review appointment with Dr. Juan Fitzgerald from December 17, 2025 at 09:00 to December 18, 2025 at 14:00, because it better fits your schedule. You would like to see your upcoming appointments and get details for the rescheduled visit. Later, you would like to schedule a new follow-up appointment with Dr. Ryan Harris for December 19, 2025 at 11:00, to ensure continuity of care, and cancel your duplicate appointment APPT_tracer_139 to streamline your care plan.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_129', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'edward_rice_tracer_0001'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'juan_fitzgerald_cardiology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_465', 'date': '2025-12-17'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_185', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'edward_rice_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_185'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'edward_rice_tracer_0001', 'provider_id': 'ryan_harris_cardiology_tracer_0001', 'date': '2025-12-19', 'time': '11:00', 'appointment_type': 'follow_up'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_139'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka (yumi.tanaka7410@pacificcare.org), and you want to reschedule your care coordination appointment with care coordinator Naomi Ito from May 6, 2025, to Wednesday, May 7, 2025, at 09:30, because it better fits your schedule. Later, you would like to check for drug interactions between Sertraline, which you accidentally took, and your current medications (Warfarin, Aspirin EC, and Metoprolol Succinate), due to concerns about potential health risks. You also prefer to update the supplier for your Sertraline prescription in medical record REC012 to a lower-cost option, specifically choosing Triveni Pharma (brand name Setrina) at $4.55, to reduce medication expenses. After that, you would like to cancel your cardiology consultation appointment (APPT030) scheduled for May 19, 2025, and confirm its details before cancellation, as it may overlap with upcoming treatment plans.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT031', 'new_date': '2025-05-07', 'new_time': '09:30'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'care_coordinator_ito'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT030'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.osborne@tracer-health.org',
        instruction="You are Matthew Osborne, a COPD patient with a Philips Trilogy Ventilator, and your email is matthew.osborne@tracer-health.org. You want to schedule a routine telehealth checkup with your primary care provider, Dr. Shannon Anderson, on Wednesday, 2025-07-09 at 09:00 because it aligns with your preferred morning availability and Dr. Anderson's schedule. You also want to review the telemetry data from your Philips Trilogy Ventilator for 2025-12-17, which shows 7.0 hours of usage, to discuss your sleep compliance during the appointment. Additionally, you would like to confirm whether adding Prednisone to your current regimen of Fluticasone Inhaler and Montelukast poses any interaction risks, and you are reassured that no high-risk interactions were found.\n\nUse matthew.osborne@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'shannon_anderson_primary_care_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'matthew_osborne_tracer_0001', 'provider_id': 'shannon_anderson_primary_care_tracer_0001', 'date': '2025-07-09', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'PHILIP_tracer_466', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Prednisone', 'current_medications': ['Fluticasone Inhaler', 'Montelukast']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction="You are David Martinez (david.martinez@email.com), managing anxiety with Sertraline, who recently started Claritin for seasonal allergies and wants to ensure safety between medications. You want to confirm there are no adverse interactions between Sertraline and Claritin, which is important for your ongoing health management. After confirmation, you would like to update your Sertraline prescription in medical record REC001 to switch to Triveni Pharma (brand name Setrina) at $4.55 per unit, because it is the most affordable option and helps reduce your medication costs. You also prefer to add a note in the same medical record stating 'Patient requested supplier change to reduce medication costs' for documentation and audit purposes.\n\nUse david.martinez@email.com for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC001', 'note': 'Patient requested supplier change to reduce medication costs.'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT002'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC001'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'david_martinez_5678'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction="You are David Martinez, patient with generalized anxiety disorder and seasonal allergies, currently taking Sertraline and Claritin. You want to verify potential drug interactions between Sertraline and your current medications because you recently took Sertraline and are concerned about safety; the check confirmed no high-risk interactions. After that, you would like to update your Sertraline prescription supplier to Triveni Pharma, using the brand name Setrina at $4.55, because it is a more affordable option. Finally, you want a note added to medical record REC001 stating 'Patient requested supplier update after interaction check' to document this change in your health record.\n\nUse david.martinez@email.com for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC001', 'note': 'Patient requested supplier update after interaction check.'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT002'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC001'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'david_martinez_5678'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction="You are Yumi Tanaka (yumi.tanaka7410@pacificcare.org), a patient managing atrial fibrillation and anxiety, who wants to reschedule your cardiology appointment APPT030 with Dr. Margaret Thompson from May 19 to May 21 because of a scheduling conflict, and you prefer the 09:00 time slot as it fits your morning routine. You would like to review the details of your rescheduled appointment and Dr. Thompson's provider information for confirmation, to ensure continuity of care with your trusted cardiologist. Later, you want to check for potential drug interactions after accidentally taking an extra dose of rosuvastatin, due to concerns about your current medications interacting, especially with warfarin and sertraline. After that, you would like to update your sertraline prescription in medical record REC012 to use Gujarat MindCare's brand Serenem at $4.65 because it is more affordable, and you prefer this supplier to reduce ongoing medication costs.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.",
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT030', 'new_date': '2025-05-21', 'new_time': '09:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'yumi_tanaka_7410'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'rosuvastatin', 'current_medications': ['warfarin', 'sertraline', 'aspirin ec', 'metoprolol succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, email yumi.tanaka7410@pacificcare.org, managing atrial fibrillation and anxiety, and you want to reduce medication costs. You would like to explore supplier options for Sertraline because it is a long-term medication and small savings matter over time. You prefer to update your prescription record for Sertraline in medical record REC012 to use Gujarat MindCare (brand: Serenem, price: $4.65) instead of Harmony Labs (price: $4.75) for cost documentation purposes, even though a high-risk interaction between Sertraline and Warfarin has been flagged and requires clinical review.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Aspirin EC', 'Metoprolol Succinate', 'Sertraline']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction="You are Kevin Bond (kevin.bond@tracer-health.org), currently on Warfarin and Atorvastatin for atrial fibrillation and hyperlipidemia. You want to check for drug interactions before starting Sertraline for mood support because of potential risks with your current regimen. After learning of the high-severity interaction between Sertraline and Warfarin, you prefer to continue your current medications without adding Sertraline. You would like to update the Warfarin prescription in your medical record (REC_tracer_132) to a lower-cost supplier, VedaRx Labs, using the brand Vedarin at $4.28, to reduce monthly medication expenses. After that update, you want a note added to the same record stating: 'Updated Warfarin supplier to VedaRx Labs (Vedarin) at $4.28 after reviewing drug interaction risks with Sertraline,' to document the change for compliance and continuity of care.\n\nUse kevin.bond@tracer-health.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_132', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_132', 'note': 'Updated Warfarin supplier to VedaRx Labs (Vedarin) at $4.28 after reviewing drug interaction risks with Sertraline.'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, a patient managing Atrial Fibrillation and Hyperlipidemia with Warfarin and Atorvastatin, and your email is shawn.zuniga@tracer-health.org. You want to review the details of your upcoming virtual cardiology consultation with Dr. Luis Sims, scheduled for 2025-12-17 at 14:00, regarding concerns about starting Zolpidem while on Bupropion, because you have questions about potential drug interactions. After reviewing the appointment, you would like to cancel this visit because you no longer wish to proceed with the consultation. Later, you want a complete list of all your currently scheduled appointments to review your upcoming healthcare commitments, including a medication review with Dr. Thompson earlier the same day.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_128'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_128'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'shawn_zuniga_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='carlos.mendez4521@email.com',
        instruction='You are Carlos Mendez, a patient with anxiety disorder and chronic pain, and your email is carlos.mendez4521@email.com. You want to schedule a cardiology consultation with Dr. Thomas May on the next available Monday morning, as the 09:00 slot on that day works well with your schedule. You also want to confirm that taking Sertraline along with Ibuprofen and Acetaminophen is safe, which is important for managing both your anxiety and chronic pain without adverse effects. After that, you would like to update the prescription supplier for Sertraline in your medical record to Gujarat MindCare, using the brand name Serenem, because it offers a more affordable option at $4.65 per unit, helping reduce your medication costs.\n\nUse carlos.mendez4521@email.com for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'carlos_mendez_4521', 'provider_id': 'thomas_may_cardiology_tracer_0001', 'date': '2024-06-10', 'time': '09:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Ibuprofen', 'Acetaminophen']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC027', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction="You are Matthew Smith, a patient with atrial fibrillation and hyperlipidemia, currently managing Warfarin and Atorvastatin. You want to confirm whether taking Zolpidem poses any risk due to interactions with your current medications, because you accidentally took a dose and are concerned about safety; no high-risk interactions were found. You would like to update your Warfarin prescription in your medical record to use the more affordable supplier Sunrise Biotech (brand name Warfast) at $4.35 per unit, because it reduces your monthly medication cost. You also prefer to reschedule your upcoming cardiology consultation with Dr. Christine Bailey from its current date to Thursday, 2025-12-18 at 14:00, because it better fits your schedule; this time is available and aligns with the provider's office hours.\n\nUse matthew.smith@tracer-health.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_134', 'medication': 'Warfarin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Warfast', 'price_usd': 4.35}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_122', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_122'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='tammy.carr@tracer-health.org',
        instruction='You are Tammy Carr, a patient with Type 2 Diabetes and Hypertension, who wants to reduce the cost of your Lisinopril prescription in medical record REC_tracer_124. You would like to check available suppliers for Lisinopril and confirm that switching to a different supplier does not interact with your current medications, Metformin and Lisinopril. After confirming safety, you prefer to update the prescription supplier to Mumbai Cardio Pharma (brand: Lisipril-M, $2.80) because it is the lowest-cost option. You also want to review your full regimen options to discuss cost and adherence improvements during your care planning.\n\nUse tammy.carr@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_124', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'tammy_carr_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='robert.martinez5589@email.com',
        instruction='You are Robert Martinez, a 61-year-old male with coronary artery disease, hypertension, type 2 diabetes, and hyperlipidemia, and your email is robert.martinez5589@email.com. You want to cancel your scheduled CABG surgery appointment with Dr. Robert Kim, a cardiac surgeon, on 2025-11-15 at 07:00 because you have decided to postpone the procedure. After that, you would like to check for potential drug interactions between Atorvastatin and your current medications—Metoprolol, Aspirin, and Metformin—due to concerns about safety, and upon confirmation of no significant interactions, you prefer to update your prescription in medical record REC028 to use VedaRx Labs (brand name Atorveeda) for Atorvastatin at $4.05 per unit to reduce your ongoing medication costs.\n\nUse robert.martinez5589@email.com for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT058'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'robert_martinez_5589'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Atorvastatin', 'Metoprolol', 'Aspirin', 'Metformin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC028', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez, authenticated via amanda.martinez@tracer-health.org, managing Type 1 Diabetes and Hypothyroidism with a Continuous Glucose Monitor and medications including Insulin Lispro and Levothyroxine. You want to review the telemetry data from your Continuous Glucose Monitor for 2025-12-17 because it shows only 7.0 hours of usage, indicating incomplete upload. You also want to check for drug interactions after accidentally taking Sertraline, and upon confirmation of safety, you would like to update your Insulin Lispro prescription to use the more affordable supplier Bengal EndoCare (brand: SwiftLis) to reduce out-of-pocket costs.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_464', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_063', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
        ],
        outputs=[],
    ),

    Task(
        user_id='richard.nelson@tracer-health.org',
        instruction='You are Richard Nelson, authenticated via richard.nelson@tracer-health.org, and you want to first access the details of your upcoming cardiology consultation with Dr. Thompson on December 17, 2025, at 10:00, as well as the associated medical record (REC_tracer_092) that contains the interaction review between Bupropion and Zolpidem, because you need to understand the safety of adding the sleep medication to your current regimen. After that, you would like to schedule a routine primary care checkup on the next day, Thursday, at 09:00, with a primary care provider, as it works better for your schedule and avoids conflict with the specialist visit.\n\nUse richard.nelson@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_125'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_125'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'richard_nelson_tracer_0001', 'provider_id': 'charles_barajas_primary_care_tracer_0001', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction="You are David Martinez (david.martinez@email.com), managing anxiety with Sertraline, and you want to confirm the safety of taking Sertraline alongside Claritin due to concern about potential interactions. After confirmation that no high-risk interactions exist, you would like to reduce medication costs by switching your Sertraline prescription to a more affordable supplier. You prefer to update your medical record (REC001) to reflect the use of Triveni Pharma's formulation of Sertraline (Setrina) at $4.55 per unit, as it offers significant cost savings while maintaining therapeutic effectiveness.\n\nUse david.martinez@email.com for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Serenem', 'price_usd': 4.55}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, a patient with atrial fibrillation, hypertension, and generalized anxiety disorder, managing your care via telehealth with email yumi.tanaka7410@pacificcare.org. You want to review the details of your upcoming cardiology consultation with Dr. Thompson on 2025-05-19, because it includes important follow-up on your lipid control and potential new combination therapy. Additionally, you would like to access your complete medical record history, including the pre-ablation assessment with Dr. Saito and the care coordination note with Coordinator Ito, so you can verify documentation related to your anticoagulation therapy, mental health support, and equipment needs ahead of your procedure.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'yumi_tanaka_7410'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sharon.baird@tracer-health.org',
        instruction='You are Sharon Baird, a patient with focal epilepsy and generalized anxiety disorder who uses a nightly EEG device but is experiencing upload issues. You want to cancel your scheduled device coaching appointment with Kimberly Wade on 2025-12-17 at 09:00 because you prefer to consolidate your concerns into a single neurology visit. Later, you would like to schedule a new follow-up appointment with your neurologist, Dr. Patel, on 2025-12-22 at 09:30, because it aligns with your availability and allows you to discuss both your epilepsy management and device compliance in one session.\n\nUse sharon.baird@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_166'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sharon_baird_tracer_0001', 'provider_id': 'dr_patel_neurology', 'date': '2025-12-22', 'time': '09:30', 'appointment_type': 'follow_up'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='carlos.mendez4521@email.com',
        instruction='You are Carlos Mendez, authenticated via carlos.mendez4521@email.com, and you want to review the details of your upcoming follow-up appointment with Dr. Lisa Chen, a Primary Care provider, before proceeding with cancellation. The appointment is scheduled for a review of chronic pain management and anxiety medication, which you value for continuity of care. After reviewing, you would like to cancel the appointment as it conflicts with your current schedule.\n\nUse carlos.mendez4521@email.com for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT056'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT056'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='heather.mccoy@tracer-health.org',
        instruction='You are Heather Mccoy (heather.mccoy@tracer-health.org) and you want to reschedule your care coordination appointment with Dr. Lisa Larson from Thursday to Friday because of a scheduling conflict. You prefer the appointment on Friday at 13:00 since it aligns with your availability and Dr. Larson has that slot open. You also want confirmation that Dr. Larson is available at that time and that the rescheduled appointment is properly set up for a virtual visit.\n\nUse heather.mccoy@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_211', 'new_date': '2025-12-19', 'new_time': '13:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'lisa_larson_care_coordination_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, a patient with atrial fibrillation and anxiety, managing medications including Sertraline, Warfarin, Aspirin EC, and Metoprolol Succinate, and you want to ensure your care is coordinated safely and affordably. You want to check for potential drug interactions between Sertraline and your other medications because you are concerned about safety, and the interaction check confirms a high-severity risk with Warfarin requiring clinical review. You would like to update the supplier for your Sertraline prescription in record REC012 to Triveni Pharma with brand Setrina at $4.55 because it is a more affordable option and is a valid supplier. You want to review the details of your upcoming cardiology appointment with Dr. Thompson on May 19, 2025, because it is a scheduled specialist consultation for your annual review. Later, you would like to check the telemetry upload data for device WEARAB_tracer_483 on December 17, 2025, because you are involved in a study and need to confirm usage, even though the device is not assigned to you.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'yumi_tanaka_7410'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC012', 'note': 'Patient requested drug interaction check and supplier update for Sertraline.'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_483', 'date': '2025-12-17'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'WEARAB_tracer_483', 'start_date': '2025-12-17', 'end_date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, a cardiology patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and your email is shawn.zuniga@tracer-health.org. You want to explore more affordable suppliers for Atorvastatin because you are concerned about medication costs, and VedaRx Labs offers it at $4.05 per month, which aligns with your current supplier for Warfarin. You would like to review your current medication regimen and the two optimized options—Cost-Synchronized Generic Fill and Adherence Packaging—because you want to reduce out-of-pocket variability and improve adherence without changing effectiveness. You also want confirmation that your cardiac event monitor (CARDIA_tracer_493) failed to upload data on June 1, 2025, because this gap could affect rhythm surveillance. You are considering starting Zolpidem for sleep and would like a drug interaction check with your current medications, which confirms no high-risk interactions with Warfarin or Atorvastatin, so you feel safer proceeding. You prefer to cancel your appointment APPT_tracer_128 with Dr. Sims about the Zolpidem interaction because the interaction check has already been completed and documented. Later, you want to reschedule your medication review appointment APPT_tracer_179 with Dr. Thompson to 08:30 on December 17, 2025, because it better fits your morning routine and the slot is available, while maintaining continuity with your cardiologist.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'shawn_zuniga_tracer_0001'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_493', 'date': '2025-06-01'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_128'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'shawn_zuniga_tracer_0001'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_179', 'new_date': '2025-12-17', 'new_time': '08:30'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.morgan@tracer-health.org',
        instruction='You are Avery Morgan, a patient with atrial fibrillation and hyperlipidemia managing care through telehealth, and your email is avery.morgan@tracer-health.org. You want to reschedule your follow-up appointment with Dr. Smith from its original date to Monday, December 5th, because of a scheduling conflict, and you would like to review your appointment list and learn more about Dr. Smith’s background and specialty to feel more informed ahead of the visit. Later, after reviewing your cardiac event monitor (CARDIA_tracer_451) data showing 7.0 hours of use on December 1st and discovering you accidentally took Sertraline, you checked for drug interactions and learned there is a high-risk interaction with your current Warfarin regimen, which prompted a change in plans. As a result, you now want to cancel your upcoming appointment with Dr. Saito on December 1st and instead schedule a new follow-up appointment with Dr. Owen Shaw, a cardiologist, on Monday, December 8th at 09:00, because you need urgent clinical guidance to address the medication interaction and discuss device compliance, and this time works well with your schedule.\n\nUse avery.morgan@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_061', 'new_date': '2025-12-05', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'avery_morgan_tracer_0001'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_451', 'date': '2025-12-01'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_059'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'avery_morgan_tracer_0001', 'provider_id': 'owen_shaw_cardiology_tracer_0001', 'date': '2025-12-08', 'time': '09:00', 'appointment_type': 'follow_up'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez, a patient with Type 1 Diabetes and Hypothyroidism, who uses a Continuous Glucose Monitor (CONTIN_tracer_464) to track glucose levels. You want to investigate missing device data uploads from 2026-01-10 to 2026-01-12 because you noticed gaps in your glucose tracking. After reviewing the data, you would like to cancel your scheduled device coaching appointment on 2025-12-17 at 09:00 with Coach Riley due to a personal scheduling conflict. You also want to confirm your updated appointment schedule to ensure the cancellation is reflected and to manage your upcoming visits, which include a medication review and endocrinology follow-ups later that day and the next day.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_464', 'start_date': '2026-01-10', 'end_date': '2026-01-12'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_136'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_136'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rebecca.washington@tracer-health.org',
        instruction='You are Rebecca Washington, a patient with Type 1 Diabetes and Hypothyroidism, and you want to check the upload history of your Continuous Glucose Monitor (CONTIN_tracer_488) because you noticed it has not been syncing data recently. After confirming no recent uploads, you want to review the details of your upcoming telehealth follow-up appointment with Dr. Fernandez scheduled for December 17, 2025, and then cancel it because you wish to clear your schedule. After cancellation, you would like a full list of your remaining scheduled appointments to confirm none are left.\n\nUse rebecca.washington@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_488'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_091'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_091'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'rebecca_washington_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.morgan@tracer-health.org',
        instruction='You are Avery Morgan, a patient managing atrial fibrillation and hyperlipidemia, and your contact email is avery.morgan@tracer-health.org. You want to reschedule your follow-up appointment with Dr. Smith from Sunday, November 30 to Tuesday, December 2 at 10:00 AM because it better fits your schedule. Later, you would like to cancel your earlier scheduled follow-up with Dr. Saito on Monday, December 1 at 7:30 AM as it is no longer needed, to free up the slot for other patients.\n\nUse avery.morgan@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_061'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_061', 'new_date': '2025-12-02', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'avery_morgan_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_059'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction="You are Edward Rice, a patient managing atrial fibrillation and hyperlipidemia via telehealth, with email edward.rice@tracer-health.org. You want to review the telemetry uploads for your cardiac event monitor (CARDIA_tracer_465) for the past week because you've experienced connectivity issues and suspect data may be missing. You would like to confirm there are no harmful interactions between Atorvastatin and your current medications (Warfarin and Atorvastatin) before making any changes, as you're considering switching suppliers to reduce costs. After confirming safety, you prefer to update your Atorvastatin prescription in your medical record to use VedaRx Labs' brand Atorveeda due to its lower price. Later, you would like to cancel your scheduled medication review appointment with Dr. Juan Fitzgerald on December 17, 2025, because of a scheduling conflict, even though it was intended to discuss cost-saving options.\n\nUse edward.rice@tracer-health.org for authentication.",
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_465'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_129', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'juan_fitzgerald_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_185'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez (amanda.martinez@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to reschedule your device coaching session with Coach Riley from the morning of 2025-12-17 to 10:00 on 2025-12-19 because it better fits your schedule for reviewing your Continuous Glucose Monitor usage. You also want to cancel your medication review appointment with Dr. Ashley Schneider on 2025-12-17 at 13:00 due to a scheduling conflict. Before finalizing these changes, you would like to confirm all your scheduled appointments and review recent telemetry uploads from your CGM (device ID: CONTIN_tracer_464) from 2025-12-10 to 2025-12-16, noting a missing upload on 2025-12-14 that you want to address during the rescheduled coaching session. After cancellation, you would like to explore other available endocrinology providers for future care options and review Dr. Schneider’s credentials and availability for reference, as you value continuity and informed decision-making in your diabetes and thyroid management.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_136'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_136', 'new_date': '2025-12-19', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_464', 'start_date': '2025-12-10', 'end_date': '2025-12-16'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_182'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'ashley_schneider_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kathryn.clark@tracer-health.org',
        instruction='You are Kathryn Clark, authenticated via kathryn.clark@tracer-health.org, and you want to review the details of your upcoming neurology follow-up appointment scheduled for December 19, 2025, because it involves monitoring for epilepsy and device compliance. You would like to schedule a follow-up appointment with your neurologist, Dr. Brian Roman, on Friday, December 26, 2025, at 10:30 AM, because it aligns with your preferred time and supports continuity of care with your current specialist. You also want to verify the telemetry data from your wearable EEG device (assigned ID WEARAB_tracer_463) for December 17, 2025, which shows 7.0 hours of usage, because you are tracking device compliance for your condition. You request a drug interaction check for Sertraline in combination with your current medications, Levetiracetam and Sertraline, and are reassured that no high-risk interactions were found, because you want to ensure your anxiety treatment is safe alongside your seizure medication. Finally, you would like a list of all available providers in the system, because you may be exploring additional care options across specialties such as care coordination, device coaching, endocrinology, pediatrics, and psychiatry.\n\nUse kathryn.clark@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_135'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kathryn_clark_tracer_0001', 'provider_id': 'brian_roman_neurology_tracer_0001', 'date': '2025-12-26', 'time': '10:30', 'appointment_type': 'follow_up'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brian_roman_neurology_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_463', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson (sarah.johnson@email.com), a patient with Type 2 Diabetes and Hypertension, who wants to reschedule your routine checkup with your primary care provider, Dr. Carlos Garcia, from its original time to 2024-01-16 at 10:00 because it better fits your schedule. After that, you would like to cancel your upcoming cardiology consultation with Dr. Robert Smith on 2025-03-18 and instead schedule a new specialist consultation with the same provider on 2025-03-19 at 15:00 to maintain continuity in your cardiac care.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT001', 'new_date': '2024-01-16', 'new_time': '10:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT001'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'sarah_johnson_1234'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_garcia_primary'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT012'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_johnson_1234', 'provider_id': 'dr_smith_cardiology', 'date': '2025-03-19', 'time': '15:00', 'appointment_type': 'specialist_consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sharon.baird@tracer-health.org',
        instruction='You are Sharon Baird, a patient managing epilepsy and anxiety through telehealth, with current medications Levetiracetam and Sertraline. You want to schedule a new routine primary care checkup with Dr. Lisa Chen on the next available Monday morning, preferably at 09:00, because it aligns with your weekly schedule. Later, you would like to reschedule your device coaching session with Kimberly Wade from the original date to the following Thursday at 15:00, because the new time better fits your availability. After that, you would like to cancel your upcoming neurology follow-up appointment, because your condition has stabilized and the session is no longer needed. You also want to know if taking Warfarin accidentally could cause a high-risk interaction with your current medications, because you are concerned about potential health risks—this is urgent due to a known high-risk interaction between Warfarin and Sertraline. Additionally, you want to review the usage data for your wearable EEG device (WEARAB_tracer_479) over the past few days to ensure compliance, specifically checking uploads from two days ago through yesterday, because you want to confirm consistent use ahead of any clinical review.\n\nUse sharon.baird@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sharon_baird_tracer_0001', 'provider_id': 'dr_chen_primary_care', 'date': '2025-12-15', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_166', 'new_date': '2025-12-18', 'new_time': '15:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_167'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kimberly_wade_device_coaching_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'WEARAB_tracer_479', 'start_date': '2025-12-10', 'end_date': '2025-12-12'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_166'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_166'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'sharon_baird_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='michelle.adams@tracer-health.org',
        instruction="You are Michelle Adams (michelle.adams@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to reorganize your upcoming endocrinology appointments for better convenience and cost efficiency. You want to cancel your scheduled follow-up with Dr. Hector Lane on Friday, 2025-12-19 at 10:00, because it conflicts with a rescheduled visit and a new appointment you prefer to prioritize. You would like to reschedule your follow-up with Dr. Charles Scott from Wednesday, 2025-12-17 at 09:00 to Thursday, 2025-12-18 at 10:00, because the new time better fits your schedule and aligns with Dr. Scott’s availability. After that, you would like to schedule a new follow-up appointment with Dr. Debra Castro, an endocrinologist, on Friday, 2025-12-19 at 09:00, because it is the earliest available slot with a different provider to maintain continuity of care. You prefer to bill your Cigna insurance for this visit. You also want to confirm that switching to Insulin Lispro supplied by Bengal EndoCare (brand SwiftLis, $19.20) is safe, which is supported by no detected drug interactions with your current medications (Insulin Lispro and Levothyroxine). You prefer to update the prescription in your medical record (REC_tracer_077) to reflect this cost-effective supplier change to reduce out-of-pocket expenses. Finally, you would like a note added to the same record stating: 'Updated prescription supplier for Insulin Lispro to Bengal EndoCare (SwiftLis) at $19.20 per unit to reduce patient's out-of-pocket costs. Patient notified and consent obtained,' to ensure audit compliance and documentation of informed consent.\n\nUse michelle.adams@tracer-health.org for authentication.",
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_145'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_087', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_145'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_145'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'charles_scott_endocrinology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'michelle_adams_tracer_0001', 'provider_id': 'debra_castro_endocrinology_tracer_0001', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'follow_up', 'bill_insurance': True}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_077', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'michelle_adams_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_077', 'note': "Updated prescription supplier for Insulin Lispro to Bengal EndoCare (SwiftLis) at $19.20 per unit to reduce patient's out-of-pocket costs. Patient notified and consent obtained."}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson, a patient with Type 1 Diabetes and Hypothyroidism, managing your care through telehealth and using a continuous glucose monitor. You want to schedule a new endocrinology follow-up with Dr. Charles Scott on the next day at 13:00 because it aligns with your preferred provider and fits your schedule. Later, you would like to reschedule your existing follow-up with Dr. Tami Robinson from the next day to three days later at 13:00 to better coordinate with your device coaching and medication review. After that, you would like to cancel your medication review appointment on today because you have already addressed cost concerns through updated prescription planning. You prefer to review your medical records, especially the note from your primary care provider about medication cost savings, to confirm the switch to a lower-cost insulin supplier. You are concerned about device compliance and want to address the missing telemetry upload on 2025-12-10 to maintain accurate glucose monitoring. You also want to confirm there are no drug interactions between Insulin Lispro and your current medications, which include Levothyroxine, to ensure safety. You prefer to update your Insulin Lispro prescription to use SwiftLis from Bengal EndoCare at $19.20 per unit for cost efficiency without changing efficacy. Finally, you would like to review your optimized regimen options to improve cost and adherence, particularly through synchronized refills or adherence packaging, to support long-term management of your conditions.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'charles_scott_endocrinology_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'laurie_carson_tracer_0001', 'provider_id': 'charles_scott_endocrinology_tracer_0001', 'date': '2025-12-18', 'time': '13:00', 'appointment_type': 'follow_up'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_169', 'new_date': '2025-12-22', 'new_time': '13:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_189'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_189'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_071'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped', 'limit': 1}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_480', 'date': '2025-12-10'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_071', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks (scott.sparks@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia, who wants to schedule a follow-up cardiology appointment with Dr. Margaret Thompson on December 18, 2025 at 09:00 because it aligns with your preferred provider and time. You also want to reschedule your existing cardiology follow-up from December 19, 2025 at 10:00 to the same time slot on December 18, 2025 at 09:00 with Dr. Thompson for continuity of care. Later, you would like to cancel your consultation with Dr. Juan Fitzgerald on December 17, 2025 at 14:00 about sleep medication interactions because you no longer need the review. You want to review the details of your appointment on December 19, 2025 at 10:00 with Dr. Bryan Bryant, your complete list of appointments, and your medical record from December 17, 2025 related to medication cost review. You would like to check telemetry uploads for your cardiac monitor on December 14, 2025, which showed no usage that day, and evaluate drug interactions between Warfarin and your current medications, which showed no significant risks. After that, you prefer to update the prescription supplier for Warfarin in your medical record to VedaRx Labs with brand name Vedarin due to lower cost, and finally review your available medication regimen options to assess cost and adherence improvements.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'scott_sparks_tracer_0001', 'provider_id': 'dr_thompson_cardiology', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'follow_up'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_163', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_163'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_126'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_121'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_477', 'start_date': '2025-12-14', 'end_date': '2025-12-14'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_121', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction='You are Matthew Smith, a 44-year-old male with Atrial Fibrillation and Hyperlipidemia, using a Cardiac Event Monitor (CARDIA_tracer_481) for rhythm surveillance. You want to review the telemetry data from your cardiac monitor on 2025-12-17 because you are monitoring for any rhythm irregularities following a recent medication error. You also want to check for drug interactions after accidentally taking Zolpidem, as you are concerned about potential effects on your current regimen of Warfarin and Atorvastatin; however, no high-risk interactions were found. You would like to update your Warfarin prescription in record REC_tracer_134 to use VedaRx Labs (brand: Vedarin, $4.28) because it offers a lower-cost option that aligns with your goal of reducing medication expenses. You prefer to reschedule your medication review appointment (APPT_tracer_190) from 09:00 on 2025-12-17 to 15:00 on 2025-12-22 because the later time better fits your schedule. You also want to cancel your device coaching session (APPT_tracer_170) because you have resolved the syncing issue independently. After that, you would like to schedule a new follow-up appointment with Dr. Robert Smith at 16:00 on 2025-12-22 for continuity of care, and you prefer to bill this visit to your insurance.\n\nUse matthew.smith@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_481', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_134', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'matthew_smith_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_190'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_134'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'matthew_smith_tracer_0001'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_190', 'new_date': '2025-12-22', 'new_time': '15:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_170'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'matthew_smith_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-22', 'time': '16:00', 'appointment_type': 'follow_up', 'bill_insurance': True}),
        ],
        outputs=[],
    ),

    Task(
        user_id='dustin.weber@tracer-health.org',
        instruction='You are Dustin Weber, authenticated at dustin.weber@tracer-health.org, and you want to cancel your scheduled device coaching appointment with provider Dr. Robert Wright on 2025-12-17 at 08:00 due to a change in care preferences. After that, you would like to explore all available providers across specialties to consider alternative care options, with no filter on specialty or availability, because you are evaluating broader choices for managing your COPD and Obstructive Sleep Apnea.\n\nUse dustin.weber@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_148'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, a patient with Type 2 Diabetes and Hypertension, and your email is sarah.johnson@email.com. You want to explore more affordable supplier options for your Lisinopril medication because you are looking to reduce your monthly prescription costs. You would also like to review your current medication regimen, which includes Metformin 500mg twice daily and Lisinopril 10mg once daily, along with optimized alternatives such as a cost-optimized generic version from ValueMeds Direct that reduces monthly expenses while maintaining efficacy, or an extended-release Metformin option that decreases daily pill burden. You plan to discuss these options with your provider during your next visit to evaluate affordability, convenience, and clinical suitability.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'sarah_johnson_1234'}),
        ],
        outputs=[],
    ),
]
