from tau_emotion_bench.types import Task, Action


TASKS = [
    Task(
        user_id='melanie.chambers@tracer-health.org',
        instruction='You are Melanie Chambers, a patient managing hypertension and type 2 diabetes, and your email is melanie.chambers@tracer-health.org. You want to reschedule your medication review appointment with Dr. Howard McCarthy from the morning of 2025-12-17 to the next day, 2025-12-18, at 09:00, because it works better with your daily routine. Later, you would like to explore lower-cost suppliers for your Lisinopril prescription to reduce out-of-pocket expenses, with a preference for options under $3.00 such as Mumbai Cardio Pharma in India. After that, you would like to review the original details of appointment APPT_tracer_107 to confirm the changes and go over the visit notes.\n\nUse melanie.chambers@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_107', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_107'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, a patient managing atrial fibrillation and hyperlipidemia, with email edward.rice@tracer-health.org. You want to explore lower-cost supplier options for Atorvastatin because you are interested in reducing medication expenses without compromising quality. You would like to review your current medication regimen, which includes Warfarin 5mg and Atorvastatin 20mg taken once daily, to understand cost and adherence optimization opportunities. You prefer to have your telemetry data reviewed for the week leading up to 2025-12-17 because you want to confirm consistent usage of your Cardiac Event Monitor (CARDIA_tracer_465), especially on 2025-12-17 when full-day data was recorded. You also want to verify that there are no adverse interactions between Atorvastatin and your current medications, particularly Warfarin, because you prioritize safety in your dual-therapy regimen, and you are reassured that no high-risk interactions were found.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'edward_rice_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_465'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_465', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, authenticated at edward.rice@tracer-health.org, with atrial fibrillation and hyperlipidemia, currently taking Warfarin and Atorvastatin. You want to evaluate starting Sertraline for depression, but there is a high-severity interaction with Warfarin that may require holding the next dose and urgent clinical review, so you prefer to delay initiating Sertraline until speaking with your provider. You would like to compare costs for Atorvastatin suppliers, noting that VedaRx Labs (current supplier) offers it at $4.05 per tablet, which is among the lowest prices, and you prefer to maintain this supplier unless a lower-cost option with equivalent adherence support is available. You are interested in reviewing your current medication regimen, which includes Warfarin 5mg and Atorvastatin 20mg once daily, with a total pill burden of two tablets, and you prefer the Adherence Packaging Option for better dose tracking. You want telemetry data reviewed for your cardiac event monitor (CARDIA_tracer_465), and you note that on December 17, 2025, it recorded 7.0 hours of usage, which is below full-day coverage, so you would like guidance on improving wear time. You are also interested in available telemetry devices and see that CARDIA_tracer_502, a cardiac event monitor, is currently available, so you would like to discuss upgrading or replacing your current device if it improves data continuity.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'edward_rice_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_465'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_465', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction='You are David Martinez (david.martinez@email.com) and you want to check whether taking Sertraline 75mg instead of your usual 50mg dose interacts with your current medications, including Sertraline and Claritin, because you accidentally took the higher dose and are concerned about safety. You would also like to update your prescription supplier for Sertraline in medical record REC001 to Buenos Spirits (Calmist) at $5.90 per unit because you prefer a more affordable option.\n\nUse david.martinez@email.com for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Buenos Spirits', 'brand_name': 'Calmist', 'price_usd': 5.9}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jin.park7284@northsoundsleep.org',
        instruction="You are jin.park7284@northsoundsleep.org. You want to accomplish these, in order:\n1. Hi, my email is jin.park7284@northsoundsleep.org. I need to check the telemetry uploads for my device VC-449 from 2025-06-01 to 2025-06-03.\n2. I would like to cancel my appointment APPT041 with Coach Riley. Also, can you tell me about Dr. Anjali Kumar's availability for a specialist consultation?\n3. I need to reschedule my appointment APPT042 to 2025-06-17 at 08:00 with Dr. Kumar. Also, please check the medical record REC021 for details on my ventilator compliance.\n\nUse jin.park7284@northsoundsleep.org for authentication.",
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'VC-449', 'start_date': '2025-06-01', 'end_date': '2025-06-03'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT041'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Pulmonology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_kumar_respiratory'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT042', 'new_date': '2025-06-17', 'new_time': '08:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT042'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC021'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold, a patient with atrial fibrillation and hyperlipidemia, and you want to reschedule your medication review appointment with Dr. Luis Sims from December 17, 2025, to Friday, December 19, 2025, at 11:00 AM because it works better with your schedule. After rescheduling, you would like to confirm the updated appointment details. You also want to check which telemetry devices are currently assigned to you and review the upload history for your cardiac event monitor (CARDIA_tracer_489) to ensure it is functioning properly and transmitting data as expected.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_187', 'new_date': '2025-12-19', 'new_time': '11:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_187'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_489'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rebecca.washington@tracer-health.org',
        instruction='You are Rebecca Washington, a patient with Type 1 Diabetes and Hypothyroidism, and you want to reschedule your upcoming telehealth endocrinology follow-up appointment with Dr. Lucia Fernandez from 2025-12-17 at 09:00 to Friday, 2025-12-19 at 13:30 because it better fits your schedule. You would like confirmation of the updated appointment details after the change. Later, you want to review the upload history for your Continuous Glucose Monitor (device ID: CONTIN_tracer_488) to ensure proper data syncing and compliance, but you notice no uploads have been recorded so far.\n\nUse rebecca.washington@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_091', 'new_date': '2025-12-19', 'new_time': '13:30'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_091'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_488'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, a patient with Type 2 Diabetes and Hypertension, and your email is sarah.johnson@email.com. You want to cancel your scheduled routine checkup appointment with your primary care provider, Dr. Carlos Garcia, because you need to reschedule your annual physical. After cancellation, you would like to explore other available providers in case you need to see a different specialist for future care. You also want to review the details of your original appointment and access the associated medical record from your annual physical to understand your current health status and treatment plan. Later, you would like to check alternative suppliers for your medication Lisinopril to explore more affordable options, especially those offering lower-cost generics. Finally, you want to review your current medication regimen and the optimized alternatives, including a cost-optimized generic version and an extended-release option, to discuss potential changes with your provider that could reduce pill burden or monthly costs.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC002'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'sarah_johnson_1234'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='cynthia.scott@tracer-health.org',
        instruction='You are Cynthia Scott, a patient managing hypertension and type 2 diabetes, and your email is cynthia.scott@tracer-health.org. You want to cancel your follow-up appointment scheduled for 2025-12-17 at 09:00 with Dr. Camila Ortega, a primary care provider, due to a scheduling conflict. After that, you would like to explore available primary care providers for potential rebooking, to maintain continuity in your chronic condition management. You also want to review the details of your appointment APPT_tracer_076, because you need to understand the clinical context and plan from that visit. Additionally, you want to access the associated medical record REC_tracer_043, to personally verify the assessment and recommendations made during the appointment. You are interested in identifying cost-effective suppliers for your Lisinopril medication, because you are concerned about ongoing treatment expenses, and Mumbai Cardio Pharma offers it at the lowest price. Finally, you would like to review your current medication regimen and optimized alternatives, because you want to make informed decisions about cost, adherence, and long-term management of your conditions.\n\nUse cynthia.scott@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_076'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_076'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_076'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'cynthia_scott_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, authenticated via shawn.carter@tracer-health.org, managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to explore more affordable supplier options for Atorvastatin to reduce medication costs. You would like to run a drug interaction check between Atorvastatin and your current regimen of Warfarin and Atorvastatin to ensure safety before any change, which confirms no high-risk interactions. After that, you prefer to update your prescription supplier information in medical record REC_tracer_122 to reflect VedaRx Labs as the source for Atorvastatin, using the brand name Atorveeda at a cost of $4.05, to support cost tracking and pharmacy coordination, even though this supplier is not currently listed in the available options.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_122', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
        ],
        outputs=[],
    ),

    Task(
        user_id='nadia.abbasi@tracer-health.org',
        instruction="You are Nadia Abbasi (nadia.abbasi@tracer-health.org), a patient with hypertension and type 2 diabetes managing Metformin and Lisinopril. You want to consult a cardiologist, specifically Dr. Owen Shaw, to discuss long-term cardiovascular management, but his availability could not be confirmed as he is not currently in the provider network. You would like to check for drug interactions due to an accidental extra dose of Lisinopril, and the system confirms no high-risk interactions with your current medications (Metformin and Lisinopril), so the incident is low concern. After that, you prefer to update your Lisinopril prescription supplier from Mumbai Cardio Pharma to Delhi Cardiovascular's CardioPril at $2.95 for brand consistency and supply reliability, even though it is slightly more expensive. Finally, you request that a note be added to medical record REC_tracer_034 stating 'Patient requested supplier change after interaction check and cost review' to document this decision and ensure audit clarity. All actions should be completed in one session for efficiency.\n\nUse nadia.abbasi@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'owen_shaw_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_034', 'medication': 'Lisinopril', 'supplier_company': 'Delhi Cardiovascular', 'brand_name': 'CardioPril', 'price_usd': 2.95}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_034', 'note': 'Patient requested supplier change after interaction check and cost review.'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='tammy.carr@tracer-health.org',
        instruction="You are Tammy Carr (email: tammy.carr@tracer-health.org), a patient with Type 2 Diabetes and Hypertension managing Metformin and Lisinopril. You want to first confirm the availability and details of Dr. Carlos Garcia as a primary care provider because you prefer continuity with a known provider. You would like to check for potential drug interactions between Sertraline, which you took accidentally, and your current medications (Metformin and Lisinopril) to ensure safety, which has been confirmed as no high-risk interactions found. After that, you prefer to update your Lisinopril prescription in medical record REC_tracer_124 to source from Mumbai Cardio Pharma under the brand name Lisipril-M at $2.80 due to lower cost. Finally, you want a note added to the same record stating 'Patient requested supplier change after cost review and interaction check' to document your request for the care team.\n\nUse tammy.carr@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_garcia_primary'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_124', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_124', 'note': 'Patient requested supplier change after cost review and interaction check.'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='toni.miller@tracer-health.org',
        instruction='You are Toni Miller, a patient with Type 1 Diabetes and Hypothyroidism, using a Continuous Glucose Monitor (device ID: CONTIN_tracer_492) to manage your glucose levels. You want to investigate the lack of recent data uploads from your device, as consistent telemetry is important for your diabetes management. You also want to review available Primary Care providers and would like detailed information about Dr. Howard McCarthy, who is experienced in Primary Care with 11 years of practice and speaks both English and Spanish, to help you prepare for an upcoming visit and ensure continuity in your care.\n\nUse toni.miller@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_492'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'howard_mccarthy_primary_care_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction="You are Scott Sparks (scott.sparks@tracer-health.org), a patient with Atrial Fibrillation who uses a cardiac event monitor (CARDIA_tracer_477). You want to first verify the telemetry device status because you noticed it hasn't uploaded data recently; specifically, you need to confirm missing uploads from 2026-01-15 to 2026-01-17, which has been verified. After that, you would like to consult a cardiologist for follow-up, and you prefer Dr. Margaret Thompson because she is a senior specialist with 25 years of experience and strong credentials (MD, FACC, FSCAI). You want to proceed with obtaining her detailed provider information, including her schedule and contact details, to prepare for scheduling a visit.\n\nUse scott.sparks@tracer-health.org for authentication.",
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_477', 'start_date': '2026-01-15', 'end_date': '2026-01-17'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='james.hanson@tracer-health.org',
        instruction="You are James Hanson (james.hanson@tracer-health.org) and you want to first review available providers and learn more about Kyle Neal, your care coordinator, because you prefer continuity with your care team. You would like to cancel your scheduled family consultation with Dr. Katherine Olson because your focus has shifted to personal care coordination. Later, you want to reschedule your care coordination appointment with Kyle Neal from its current time to Friday at 13:00, because it better fits your availability and aligns with your preferred provider's schedule.\n\nUse james.hanson@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kyle_neal_care_coordination_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_204'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_205', 'new_date': '2025-12-19', 'new_time': '13:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka (email: yumi.tanaka7410@pacificcare.org), a patient with atrial fibrillation and generalized anxiety disorder, who wants to schedule a follow-up psychiatry appointment with Dr. Amy Mitchell on Monday, December 22, 2025, at 13:00 because it fits your schedule. You also want to check for interactions between Sertraline and your current medications (Warfarin, Aspirin EC, Metoprolol Succinate), which reveals a high-severity interaction with Warfarin requiring urgent clinical review. After that, you would like to update your Sertraline prescription in record REC012 to use the supplier Triveni Pharma, brand Setrina at $4.55 to reduce costs, but this supplier is not currently available in the system; the most affordable alternative is Harmony Labs (Sertrawin) at $4.75.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Psychiatry'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'yumi_tanaka_7410', 'provider_id': 'amy_mitchell_psychiatry_tracer_0001', 'date': '2025-12-22', 'time': '13:00', 'appointment_type': 'follow_up'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction="You are Scott Sparks, authenticated via scott.sparks@tracer-health.org, and you want to schedule a cardiology consultation with Dr. Ryan Harris, a cardiologist with 20 years of experience, on Monday, June 10, 2024, at 2:00 PM because it aligns with your availability and the provider's schedule.\n\nUse scott.sparks@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'scott_sparks_tracer_0001', 'provider_id': 'ryan_harris_cardiology_tracer_0001', 'date': '2024-06-10', 'time': '14:00', 'appointment_type': 'consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction="You are Kevin Arnold, a patient with atrial fibrillation and hyperlipidemia managing Warfarin and Atorvastatin, who is concerned about missing telemetry data from your cardiac monitor and seeking more affordable medication options. You want to review the upload history for your assigned cardiac event monitor, CARDIA_tracer_489, because there have been no recorded uploads from January 5 to January 11, 2026, which may affect your cardiac rhythm surveillance. You are also exploring lower-cost suppliers for Atorvastatin to reduce out-of-pocket expenses, noting that options like Sunrise Biotech in India offer it at $4.15 per unit, which is lower than your current supplier. You would like to review your optimized regimen options, particularly the 'Cost-Synchronized Generic Fill' plan, because it maintains therapeutic equivalence while potentially lowering your monthly costs. After reviewing these options, you want a note added to your medical record REC_tracer_131 stating 'Patient inquired about Atorvastatin supplier options and cost-effective alternatives' so your care team is aware of your interest in more affordable alternatives for continuity of care.\n\nUse kevin.arnold@tracer-health.org for authentication.",
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_489', 'start_date': '2026-01-05', 'end_date': '2026-01-11'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_131', 'note': 'Patient inquired about Atorvastatin supplier options and cost-effective alternatives.'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez, a patient with Type 1 Diabetes and Hypothyroidism managing your condition with Insulin Lispro and Levothyroxine, and you use a Continuous Glucose Monitor for glucose tracking. You want to review the recent telemetry uploads for your device because you’ve noticed inconsistent data, particularly a full-day gap on December 14, which may affect your treatment insights. You would like to explore more affordable suppliers for Insulin Lispro because your current supply is costly, and you prefer switching to a lower-cost option such as SwiftLis by Bengal EndoCare, which is available at a reduced price and supports long-term adherence. After this, you want a note added to your medical record documenting your inquiry about insulin cost-saving options and adherence packaging, to ensure your care team supports sustainable and accessible medication management.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_464'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_063', 'note': 'Patient inquired about insulin cost-saving options and adherence packaging.'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='norma.ruiz@tracer-health.org',
        instruction='You are Norma Ruiz, a patient with Type 1 Diabetes and Hypothyroidism managing care via telehealth, and your email is norma.ruiz@tracer-health.org. You want to check supplier options for your Insulin Lispro medication because you are reviewing more affordable alternatives. You would like to reschedule your endocrinology follow-up appointment with Dr. Debra Castro from tomorrow to the next day at 14:00 because the new time works better with your schedule and avoids overlap with other commitments. After that, you would like to cancel your device coaching session with Jennifer Roth because it overlaps with the original endocrinology visit and is no longer needed at that time. You also want to receive the professional details of Dr. Debra Castro, your endocrinologist, for future reference and continuity of care.\n\nUse norma.ruiz@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_090', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'debra_castro_endocrinology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_160'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction="You are Kevin Arnold, a patient managing atrial fibrillation and hyperlipidemia with medications including Atorvastatin and Warfarin. You want to explore lower-cost suppliers for Atorvastatin because you are looking to reduce your out-of-pocket expenses. You would like to reschedule your medication review appointment with Dr. Luis Sims, a cardiology specialist, to the next day at 10:00 AM because it allows you more time to prepare and aligns with your schedule. You also want to receive Dr. Sims' provider details to verify his credentials and feel confident in your care. Later, you realize you have two cardiology appointments scheduled at the same time on the same day, so you decide to cancel your follow-up appointment with Dr. Christine Bailey because it appears redundant with your specialist consultation and you prefer to avoid duplicate visits.\n\nUse kevin.arnold@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_187', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'luis_sims_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_080'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond, authenticated via kevin.bond@tracer-health.org, and you want to cancel your scheduled follow-up appointment with Dr. Saito on 2025-12-17 at 07:30 because you prefer care with a different cardiologist. Later, you would like to schedule a new follow-up appointment with Dr. Brandi Dixon, a cardiologist, on 2025-12-22 at 09:00, as it aligns with your preference for morning availability and continuity in cardiology care. You prefer to use your Aetna insurance for the copay.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_081'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_saito_cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'provider_id': 'brandi_dixon_cardiology_tracer_0001', 'date': '2025-12-22', 'time': '09:00', 'appointment_type': 'follow_up', 'bill_insurance': True}),
        ],
        outputs=[],
    ),

    Task(
        user_id='richard.dunn@tracer-health.org',
        instruction='You are Richard Dunn, authenticated at richard.dunn@tracer-health.org, and you want to cancel your scheduled pediatric family consultation with Dr. Daniel Pitts on December 17, 2025, due to a scheduling conflict. After that, you would like to schedule a new routine checkup with a primary care provider on Friday, which is the next available day that fits your schedule, at 9:00 AM, because it aligns with your availability and maintains timely care continuity.\n\nUse richard.dunn@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_196'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'richard_dunn_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'john_wise_primary_care_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'richard_dunn_tracer_0001', 'provider_id': 'john_wise_primary_care_tracer_0001', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='carlos.mendez4521@email.com',
        instruction='You are Carlos Mendez, a patient managing anxiety disorder and chronic pain, currently taking Sertraline, Ibuprofen, and Acetaminophen. You are concerned about potential drug interactions after accidentally taking an extra dose of Sertraline, so you want a drug interaction check performed to ensure your safety. You would like your prescription supplier for Sertraline in medical record REC027 to be updated to Triveni Pharma, brand Setrina, priced at $4.55, because it is a more affordable option. You also want to review your current medical records, particularly REC027, to verify the details of your Sertraline prescription and ensure accuracy before any changes are made.\n\nUse carlos.mendez4521@email.com for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Ibuprofen', 'Acetaminophen']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC027', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC027'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'carlos_mendez_4521'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'carlos_mendez_4521'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction='You are David Martinez (david.martinez@email.com), a patient with generalized anxiety disorder and seasonal allergies, currently taking Sertraline 75mg daily and Claritin 10mg as needed. You want to confirm there are no harmful interactions between Sertraline and Claritin because you are concerned about safety with combined use; the check shows no high-risk interactions, which supports continued use. You would like to update your prescription details in medical record REC001 to reflect Triveni Pharma from India as your preferred supplier for Sertraline, using the brand name Setrina at $4.55, because it is more affordable than other available options. You want to review the full details of your medical record REC001 to understand your treatment plan and progress. You prefer to see all available suppliers for Sertraline to make an informed decision about cost-effective options, and you would like a complete list of your medical records to review your clinical history, even though you currently have only one record.\n\nUse david.martinez@email.com for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'david_martinez_5678'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'david_martinez_5678'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.morgan@tracer-health.org',
        instruction='You are Avery Morgan, a patient with atrial fibrillation who uses a heart monitor and prefers Spanish-language instructions. You want to cancel your scheduled device coaching appointment with Coach Riley on Monday, December 1st, because you are now consistently syncing your device. Later, you would like to reschedule your cardiology follow-up appointment with Dr. Smith from Wednesday, December 3rd at 10:00 AM to Friday, December 5th at 09:00 AM, because the earlier day works better with your work schedule. You prefer Friday morning appointments for specialist visits. After the reschedule, you would like confirmation of the new appointment details and provider information about Dr. Smith, including his specialty, experience, and language capabilities, to feel more prepared for the visit.\n\nUse avery.morgan@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_066'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_071', 'new_date': '2025-12-05', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_071'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='nadia.abbasi@tracer-health.org',
        instruction='You are Nadia Abbasi, and your email is nadia.abbasi@tracer-health.org. You want to cancel your 08:00 appointment on December 1, 2025, with Dr. Camila Ortega because of a scheduling conflict. You would like to reschedule your follow-up appointment, currently set for 09:00 on December 1, 2025, to Monday, December 8, at 10:00, because it better fits your availability and aligns with Dr. Ortega’s schedule. You prefer this new time to maintain continuity with your primary care provider for managing your hypertension and type 2 diabetes. After the changes, you want confirmation of the updated appointment details and provider information to ensure accuracy.\n\nUse nadia.abbasi@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_072'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_060', 'new_date': '2025-12-08', 'new_time': '10:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_060'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'camila_ortega_primary_care_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction="You are Joshua Wagner (joshua.wagner@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia who uses a cardiac event monitor (CARDIA_tracer_469) to track heart rhythm. You want to cancel your scheduled follow-up appointment with Dr. Bryan Bryant on 2025-12-17 at 09:00 because of a scheduling conflict. After that, you would like to schedule a new follow-up appointment with Dr. Juan Fitzgerald on 2025-12-18 at 10:00, as this time works better for your schedule and aligns with the provider's availability. You also want to review the recent telemetry data from your cardiac event monitor for the past week to ensure it has been properly recording, noting that usage hours have been consistent except for zero usage on 2025-12-14, which may require follow-up.\n\nUse joshua.wagner@tracer-health.org for authentication.",
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_079'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'bryan_bryant_cardiology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'joshua_wagner_tracer_0001', 'provider_id': 'juan_fitzgerald_cardiology_tracer_0001', 'date': '2025-12-18', 'time': '10:00', 'appointment_type': 'follow_up'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_469'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson, a patient with Type 1 Diabetes and Hypothyroidism, and your email is laurie.carson@tracer-health.org. You want to schedule a follow-up appointment with Dr. Ashley Schneider, an endocrinologist, on Thursday, December 18, 2025, at 10:00 AM, because it aligns with your preferred morning time and allows continuity in your diabetes and thyroid care. Later, you would like to cancel your device coaching session with Riley Stone, a registered therapist and nurse specializing in device coaching, scheduled for December 17, 2025, at 09:00 AM, because you have decided to reschedule that support session to a later date. You also want to review the details of that cancelled appointment for your personal records. After that, you would like a complete list of all your remaining scheduled appointments to manage your upcoming healthcare commitments.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'laurie_carson_tracer_0001', 'provider_id': 'ashley_schneider_endocrinology_tracer_0001', 'date': '2025-12-18', 'time': '10:00', 'appointment_type': 'follow_up'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_168'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'riley_stone_device_coaching_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_168'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='molly.hill@tracer-health.org',
        instruction='You are Molly Hill (molly.hill@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to schedule a new follow-up appointment with Dr. Caleb Turner, an endocrinologist, on next day at 13:00 because it aligns better with your schedule. Later, you will cancel your existing follow-up appointment with Dr. Kelly Taylor on the following day at 10:00 as it is now redundant. You would like provider details for Dr. Kelly Taylor for your records, and you also want the full details of the appointment you canceled as well as a complete list of your remaining scheduled appointments for personal tracking.\n\nUse molly.hill@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'molly_hill_tracer_0001', 'provider_id': 'caleb_turner_endocrinology_tracer_0001', 'date': '2025-12-18', 'time': '13:00', 'appointment_type': 'follow_up'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_153'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kelly_taylor_endocrinology_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_153'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'molly_hill_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, authenticated with email yumi.tanaka7410@pacificcare.org, and you want to check for potential drug interactions between Sertraline and your current medications—Warfarin, Aspirin EC, and Metoprolol Succinate—because you recently took Sertraline and are concerned about safety. You would also like to update the supplier for Sertraline in your medical record to Turquoise Labs, using the brand name Sertranex, for consistency in your regimen. Later, you want to cancel your care coordination appointment because it is no longer needed. After that, you would like to reschedule your cardiology consultation to an earlier time on Wednesday, as it better fits your schedule and allows for timely follow-up on your atrial fibrillation management.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Turquoise Labs', 'brand_name': 'Sertranex', 'price_usd': 6.05}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT031'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT030', 'new_date': '2025-05-21', 'new_time': '08:30'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks (scott.sparks@tracer-health.org), a patient managing atrial fibrillation and hyperlipidemia with medications including Atorvastatin. You want to explore lower-cost suppliers for Atorvastatin to reduce out-of-pocket expenses, with options available from international suppliers such as VedaRx Labs (India) and Bharat Lifecare (India) offering competitive pricing. You would like to reschedule your device coaching appointment with Joseph Robertson from 09:00 to 10:00 on the same day (2025-12-17), because the later time better fits your morning schedule. After that, you want a review of your telemetry device inventory, confirming that the CARDIA_tracer_477 cardiac event monitor is currently assigned and deployed for your use. You also prefer to see the recent upload history for CARDIA_tracer_477 to verify data continuity, noting that usage has been consistent except for a missed upload on 2025-12-14, which aligns with your concern about upload compliance.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_162', 'new_date': '2025-12-17', 'new_time': '10:00'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_477'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson, a patient managing Type 1 Diabetes and Hypothyroidism, who wants to reduce medication costs and ensure proper device usage. You would like to explore more affordable suppliers for your Insulin Lispro prescription because you are concerned about out-of-pocket expenses, and you prefer options with lower pricing such as those from Indian manufacturers. You also want to reschedule your medication review appointment with your primary care provider, Dr. Debra Nunez, from December 17, 2025, to December 22, 2025, at 09:00 AM because it better fits your schedule and aligns with the provider’s availability. After that, you would like to review recent usage data from your continuous glucose monitor (CGM) for the three days prior to the appointment to ensure consistent device use and support clinical discussion about your glucose management.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_104', 'new_date': '2025-12-22', 'new_time': '09:00'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_480'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson, authenticated at laurie.carson@tracer-health.org, managing Type 1 Diabetes and Hypothyroidism. You want to confirm that starting Sertraline for anxiety does not interact with your current medications (Insulin Lispro and Levothyroxine), because you are beginning a new mental health treatment and want to ensure safety. You would like your Insulin Lispro prescription in record REC_tracer_071 updated to use Lotus Rapid Therapeutics (brand: Lispry) at $19.75, because you are seeking more affordable or accessible insulin options. You prefer to review your current and optimized regimen options, because you are evaluating ways to reduce cost and improve adherence. After that, you would like to review your glucose monitor usage data from your Continuous Glucose Monitor (device ID: CONTIN_tracer_480) for 2025-12-17, because you want to assess your adherence on that day, where you used the device for 7 hours.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_071', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_480', 'date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez, authenticated via amanda.martinez@tracer-health.org, who wants to check for potential drug interactions between Sertraline and your current medications (Insulin Lispro and Levothyroxine) because you recently started taking it for anxiety and want to ensure safety. You would like to update your Insulin Lispro prescription to use the brand Lispry supplied by Lotus Rapid Therapeutics instead of your current supplier, even though it is slightly more expensive, because of a personal preference for this brand. You also want to review your current regimen options to understand cost and adherence implications. Finally, you would like to retrieve your telemetry data from your Continuous Glucose Monitor (device ID: CONTIN_tracer_464) for December 17, 2025, to review your usage pattern, which showed 7.0 hours of use that day.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_063', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_464', 'date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='toni.miller@tracer-health.org',
        instruction="You are Toni Miller (toni.miller@tracer-health.org) and you want to review the details of your scheduled medication review appointment with Dr. Amy Young on 2025-12-17 at 13:00, because it is upcoming and related to managing your Type 1 Diabetes and Hypothyroidism. You would like to schedule a new routine checkup with Dr. Nicholas Salinas, a Primary Care provider with 13 years of experience who speaks both English and Spanish, because you wish to establish ongoing primary care. You prefer the appointment be on 2025-12-22 at 09:00, as it aligns with your schedule and falls within Dr. Salinas's available hours on that Monday.\n\nUse toni.miller@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_181'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'toni_miller_tracer_0001', 'provider_id': 'nicholas_salinas_primary_care_tracer_0001', 'date': '2025-12-22', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'nicholas_salinas_primary_care_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joel.garner@tracer-health.org',
        instruction="You are Joel Garner, authenticated via joel.garner@tracer-health.org, and you want to review the details of your scheduled care coordination appointment on 2025-12-18 at 10:00 with Monica Reyes, which is intended to help organize your family's healthcare needs and prepare for a pediatric consultation. You would like to schedule a new routine checkup with primary care provider Dr. Dana Padilla on Friday, 2025-12-19 at 09:00 because it aligns with your preferred time and provider. You also want to receive Dr. Padilla's details, including her experience, language skills, and availability, and you would like a list of other available primary care providers for future reference.\n\nUse joel.garner@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_213'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'joel_garner_tracer_0001', 'provider_id': 'dana_padilla_primary_care_tracer_0001', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dana_padilla_primary_care_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond (kevin.bond@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia managing Warfarin and Atorvastatin, who uses a cardiac event monitor (CARDIA_tracer_485) that has not uploaded any telemetry data recently. You want to reschedule your medication review appointment (currently on December 17) to December 24 at 09:00 because it better fits your schedule. Later, you would like to cancel your follow-up appointment with Dr. Saito on December 17. After that, you prefer to schedule a new routine checkup with Dr. Smith on December 22 at 09:00 for continuity of care. You also want to switch your Warfarin prescription supplier to VedaRx Labs (brand: Vedarin, $4.28) to reduce medication costs, and you would like confirmation that there are no harmful interactions between Warfarin and your current medications, which has been verified as safe.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed', 'limit': 1}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_485'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-22', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_081'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_132', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_188', 'new_date': '2025-12-24', 'new_time': '09:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'status_filter': 'scheduled'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_132'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_188'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, and your email is sarah.johnson@email.com. You want to confirm the details of your upcoming cardiology appointment scheduled with Dr. Robert Smith, a board-certified cardiologist with 15 years of experience, because you value continuity with a trusted specialist. The appointment is set for next Tuesday at 10:00 AM via telehealth, which fits your morning availability. You also want to verify that adding Lisinopril to your current medication regimen, which includes Metformin, does not pose any high-risk interactions, because you are proactively managing your Type 2 Diabetes and Hypertension safely, and the review confirmed no documented interactions of concern.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT012'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction="You are Joshua Wagner, a patient with atrial fibrillation and hyperlipidemia, and your email is joshua.wagner@tracer-health.org. You want to reschedule your cardiology follow-up appointment with Dr. Thomas May from its current date to next Monday, December 22, at 9:00 AM because it works better with your schedule. You also want to cancel your device coaching session with Riley Stone that was scheduled for earlier this week because the issue with your heart monitor has been resolved. You would like to explore cost-saving options for your Atorvastatin prescription, as you are looking to reduce monthly medication expenses. You prefer to have a note added to your medical record from your recent medication review visit stating 'Discussed medication cost options with patient' to document this discussion. Later, you would like to schedule a new care coordination consultation with Julie Hines, an RN and care coordinator, on the following day, Tuesday, December 23, at 10:00 AM to streamline your treatment plan and improve adherence.\n\nUse joshua.wagner@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_147'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_147', 'new_date': '2025-12-22', 'new_time': '09:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_146'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'thomas_may_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_130', 'note': 'Discussed medication cost options with patient.'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_130'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'joshua_wagner_tracer_0001', 'provider_id': 'julie_hines_care_coordination_tracer_0001', 'date': '2025-12-23', 'time': '10:00', 'appointment_type': 'consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='norma.ruiz@tracer-health.org',
        instruction='You are Norma Ruiz, a patient with Type 1 Diabetes and Hypothyroidism, and your email is norma.ruiz@tracer-health.org. You want to cancel your scheduled endocrinology follow-up appointment with Dr. Debra Castro because of a personal scheduling conflict. Later, you would like to reschedule your other endocrinology follow-up appointment with Dr. Michael Moss to the next day after the canceled visit, which aligns with your preferred morning time slot for better continuity of care. After that, you would like to explore more affordable suppliers for your Insulin Lispro medication to reduce your treatment costs, with a preference for lower-cost international options that maintain medication quality.\n\nUse norma.ruiz@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_090'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'norma_ruiz_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_090'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'debra_castro_endocrinology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_090'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_161', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'norma_ruiz_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'norma_ruiz_tracer_0001', 'provider_id': 'debra_castro_endocrinology_tracer_0001', 'date': '2025-12-17', 'time': '09:00', 'appointment_type': 'follow_up'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='norma.ruiz@tracer-health.org',
        instruction="You are Norma Ruiz, a patient with Type 1 Diabetes and Hypothyroidism, and your email is norma.ruiz@tracer-health.org. You want to cancel your scheduled follow-up appointment with Dr. Debra Castro on 2025-12-17 because you prefer to consult with a provider who speaks Spanish for better communication. You also want to obtain Dr. Castro's provider details for your personal records. Later, you would like to schedule a new virtual follow-up appointment with Dr. Lucia Fernandez, an endocrinologist who speaks Spanish, on the next available Thursday at 15:30, as that time works well with your schedule and ensures continuity in managing your condition.\n\nUse norma.ruiz@tracer-health.org for authentication.",
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_090'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'debra_castro_endocrinology_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'norma_ruiz_tracer_0001', 'provider_id': 'dr_fernandez_endocrinology', 'date': '2025-12-18', 'time': '15:30', 'appointment_type': 'follow_up'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.barnes@tracer-health.org',
        instruction='You are Sarah Barnes, authenticated via sarah.barnes@tracer-health.org, and you want to cancel your scheduled medication review appointment with Dr. Charles Barajas because you prefer to address your concerns about medication cost and pill burden during a follow-up visit instead. You would like to confirm Dr. Barajas’s credentials and availability because you value continuity with your primary care provider who knows your history with hypertension and type 2 diabetes. After that, you prefer to schedule a new follow-up appointment with Dr. Charles Barajas, a board-certified primary care physician with 12 years of experience, on the next day (2025-12-18), ideally at 09:00, because it aligns with your availability and allows timely discussion of your treatment plan.\n\nUse sarah.barnes@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_176'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'charles_barajas_primary_care_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_barnes_tracer_0001', 'provider_id': 'charles_barajas_primary_care_tracer_0001', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'follow_up'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson, a patient with Type 1 Diabetes and Hypothyroidism, whose email is laurie.carson@tracer-health.org. You want to reschedule your endocrinology follow-up appointment with Dr. Caleb Turner from 09:00 to 10:00 on 2025-12-17 because it better fits your morning schedule. Later, you would like to cancel your device coaching session with Dr. Riley Stone due to overlapping timing and because you plan to review your glucose monitor data independently. After that, you are interested in exploring other available providers for a potential new follow-up appointment to ensure continuity of care. You also want to review your recent glucose monitor usage data from your Continuous Glucose Monitor (device ID: CONTIN_tracer_480) to assess your daily compliance, and you would like to see a list of available telemetry devices in the system to understand current inventory options.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_082', 'new_date': '2025-12-17', 'new_time': '10:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_168'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'laurie_carson_tracer_0001', 'provider_id': 'caleb_turner_endocrinology_tracer_0001', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'follow_up'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_480'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction='You are David Martinez (david.martinez@email.com) and you want to check for potential drug interactions after taking an extra dose of Sertraline, because you are concerned about your safety given your current medications (Sertraline and Claritin). You would like to update your Sertraline prescription in medical record REC001 to use a more affordable supplier, Gujarat MindCare, because it offers the brand Serenem at $4.65, which helps reduce your medication costs. You also want a complete list of your medical records for personal tracking and review, because you prefer to stay informed about your health history.\n\nUse david.martinez@email.com for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'david_martinez_5678'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, a patient with atrial fibrillation and anxiety, whose email is yumi.tanaka7410@pacificcare.org. You want to check for potential drug interactions resulting from an accidental extra dose of Sertraline, because it could affect your current regimen of Warfarin, Sertraline, Aspirin EC, and Metoprolol Succinate, especially given your cardiac and mental health conditions. You would also like to update your Sertraline prescription in medical record REC012 to switch from the current brand Sertrawin (Harmony Labs) to Setrina by Triveni Pharma, because it offers a lower cost at $4.55 per unit, supporting your goal of reducing medication expenses without compromising treatment continuity.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'yumi_tanaka_7410'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jamie.huynh@tracer-health.org',
        instruction="You are Jamie Huynh, a patient with focal epilepsy and generalized anxiety disorder, using a wearable EEG device for neurology telemetry. You want to confirm that recent data uploads failed on 2026-01-08, 2026-01-09, and 2026-01-10 because you're concerned about gaps in your neurological monitoring. You would like to verify that starting Sertraline does not pose high-risk interactions with your current medication Levetiracetam, as you've recently begun treatment for anxiety. After confirming safety, you want to review your upcoming neurology follow-up appointment with Dr. Cynthia Perry, a neurologist with 15 years of experience, scheduled for 2025-12-19 at 09:30. You prefer to cancel this appointment after your review, because you have reassessed your care plan and no longer wish to proceed with the visit.\n\nUse jamie.huynh@tracer-health.org for authentication.",
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_471', 'date': '2026-01-08'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_151'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'cynthia_perry_neurology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_151'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='molly.hill@tracer-health.org',
        instruction='You are Molly Hill, a patient with Type 1 Diabetes and Hypothyroidism managing her care through telehealth. You want to investigate the missing telemetry data upload for January 15, 2026, from your Continuous Glucose Monitor (CONTIN_tracer_472) because you noticed a gap in your glucose tracking and need to ensure complete data for your treatment review. You also want to check for potential drug interactions after accidentally taking an additional dose of Insulin Lispro, because you are concerned about safety despite it being part of your current regimen with Levothyroxine. After confirming no high-risk interactions, you would like to review the details of your upcoming endocrinology follow-up appointment with Dr. Christopher Fisher on December 17, 2025, at 09:00, because you have a scheduling conflict. You prefer to cancel this appointment after reviewing the provider and visit details, as you need to resolve the conflict and will reschedule later if necessary.\n\nUse molly.hill@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_472', 'date': '2026-01-15'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_088'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'christopher_fisher_endocrinology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_088'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson, a patient with Type 1 Diabetes and Hypothyroidism, preparing for your upcoming medication review appointment. You want your care team to confirm the details of your scheduled virtual visit with Dr. Debra Nunez on next day, as you need to ensure you can join via the secure telehealth link. You would like to continue with Dr. Nunez for continuity of care, as she is familiar with your medical history and has already documented cost-saving plans for your insulin. You prefer to explore lower-cost suppliers for Insulin Lispro to reduce out-of-pocket expenses, and based on available options, you are interested in SwiftLis from Bengal EndoCare, which is the most affordable and already part of your current regimen. You would like your medical record to reflect that you inquired about lower-cost insulin suppliers and discussed adherence packaging options, to support future care decisions. You also want your recent glucose monitor (Continuous Glucose Monitor) usage data from the past week to be reviewed, as it shows suboptimal daily use (averaging under 7 hours), and you plan to discuss strategies to improve adherence during the appointment. You prefer to pay by standard insurance copay for the visit, as it is already authorized and aligns with your benefits.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'debra_nunez_primary_care_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_104'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_071', 'note': 'Patient inquired about lower-cost insulin suppliers and discussed adherence packaging options.'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_480', 'start_date': '2025-12-10', 'end_date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='cynthia.scott@tracer-health.org',
        instruction="You are Cynthia Scott, a patient managing hypertension and type 2 diabetes with Metformin and Lisinopril, who recently started taking Sertraline and wants to ensure safety. You want to check for potential drug interactions between Sertraline and your current medications because you are concerned about side effects or adverse reactions; the evaluation shows no significant interactions, so it is safe to continue. You would like to update your Lisinopril prescription in your medical record to use Hyderabad Heart Meds with the brand name Sinopril-H at $3.10 per unit, even though it is not the lowest-cost option, because you have a personal preference for this supplier. Later, you want to reschedule your follow-up appointment with Dr. Camila Ortega from Wednesday, December 17, 2025, at 09:00 to Monday, December 22, 2025, at 10:00 because the new time better fits your schedule; the new slot is available and aligns with your provider's office hours. After that, you would like confirmation of the updated appointment details to ensure the change was processed correctly.\n\nUse cynthia.scott@tracer-health.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_065', 'medication': 'Lisinopril', 'supplier_company': 'Hyderabad Heart Meds', 'brand_name': 'Sinopril-H', 'price_usd': 3.1}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_076', 'new_date': '2025-12-22', 'new_time': '10:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_076'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.barnes@tracer-health.org',
        instruction='You are Sarah Barnes (sarah.barnes@tracer-health.org), a patient with Type 2 Diabetes and Hypertension, who recently started taking Sertraline for anxiety. You want to confirm that Sertraline does not interact with your current medications, Metformin and Lisinopril, because you want to ensure your regimen remains safe. After confirmation of no high-risk interactions, you would like to update your Lisinopril prescription in your medical record to use a more affordable supplier, Mumbai Cardio Pharma, with the brand name Lisipril-M priced at $2.80, because you want to reduce your medication costs. You also want to schedule a routine follow-up appointment with your primary care provider, Dr. Nicholas Salinas, on the next available Monday, which is 2025-12-22 at 09:00, because you prefer continuity with your trusted provider and the time works well with your schedule.\n\nUse sarah.barnes@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_120', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_barnes_tracer_0001', 'provider_id': 'nicholas_salinas_primary_care_tracer_0001', 'date': '2025-12-22', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter (shawn.carter@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia currently taking Warfarin and Atorvastatin. You want to reschedule your cardiology consultation with Dr. Kayla Guzman from 14:00 to 15:00 on December 17, 2025, because it better fits your daily schedule. You would like to confirm the details of this appointment afterward. Later, you would like to schedule a new psychiatry consultation with Dr. Jennifer Williams on December 19, 2025, at 14:00 to discuss sleep issues and the potential use of Zolpidem, using your Aetna insurance. Before starting Zolpidem, you want to ensure there are no harmful interactions with your current medications, as safety is a priority. After confirming safety, you would like to update your Warfarin prescription in record REC_tracer_122 to use the lower-cost supplier VedaRx Labs (brand: Vedarin, $4.28) to reduce your monthly medication expenses.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_127', 'new_date': '2025-12-17', 'new_time': '15:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_127'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_carter_tracer_0001', 'provider_id': 'dr_williams_psychiatry', 'date': '2025-12-19', 'time': '14:00', 'appointment_type': 'consultation', 'bill_insurance': True}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_122', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
        ],
        outputs=[],
    ),

    Task(
        user_id='cynthia.scott@tracer-health.org',
        instruction='You are Cynthia Scott, a patient with hypertension and type 2 diabetes managing your care via telehealth. You want to reschedule your medication review appointment with your primary care provider, Dr. Dana Padilla, from its original date to the next day at 14:00 because the new time better fits your daily schedule. After confirming the rescheduled appointment details, you would like to schedule a new specialist consultation with endocrinologist Dr. Christopher Fisher in 3 days at 09:00 to improve long-term management of your chronic conditions. You prefer this time as it aligns with your availability and allows timely specialist input. Later, you want to check for potential drug interactions between Lisinopril and your current medications, Metformin and Lisinopril, to ensure safety. After confirming no interactions, you would like to update the prescription supplier for Lisinopril in your medical record to Mumbai Cardio Pharma, using the brand name Lisipril-M, to reduce your monthly medication costs while maintaining treatment efficacy.\n\nUse cynthia.scott@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_183', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_183'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'cynthia_scott_tracer_0001', 'provider_id': 'christopher_fisher_endocrinology_tracer_0001', 'date': '2025-12-23', 'time': '09:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_127', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction='You are Diane Robinson (diane.robinson@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to cancel your scheduled follow-up appointment with Dr. Ashley Schneider on 2025-12-17 at 09:00 due to a scheduling conflict. You would like to reschedule your medication review appointment with Dr. Caleb Turner from 2025-12-17 at 13:00 to the next day, 2025-12-18, at 09:00 because it better fits your daily routine. You want to verify that your Continuous Glucose Monitor (device ID: CONTIN_tracer_484) has a missing data upload on 2025-12-16 and need support to resolve this gap for accurate monitoring. You would like to confirm there are no drug interactions between Insulin Lispro and your current medication Levothyroxine, which has been verified as safe. Finally, you prefer to update the prescription supplier for Insulin Lispro in your medical record to Lotus Rapid Therapeutics (brand: Lispry) for cost efficiency, as it offers a competitive price while maintaining clinical effectiveness.\n\nUse diane.robinson@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_184', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'diane_robinson_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_484', 'date': '2025-12-16'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_128', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold, a patient with atrial fibrillation and hyperlipidemia, and your email is kevin.arnold@tracer-health.org. You want to cancel your follow-up appointment with Dr. Christine Bailey scheduled for 2025-12-17 at 09:00 because you need to adjust your cardiology visit schedule. Later, you would like to reschedule your specialist consultation with Dr. Brandi Dixon from 2025-12-17 at 10:00 to Monday, 2025-12-22 at 10:00 because it better fits your availability and the slot is open. After that, you would like to report that your cardiac event monitor (CARDIA_tracer_489) has not uploaded data from 2025-12-10 to 2025-12-16 due to a connectivity issue. You also want to check for interactions between Zolpidem, which you took, and your current medications (Warfarin and Atorvastatin), as a precaution despite no high-risk interactions being documented. Finally, you prefer to update the supplier for your Warfarin prescription to VedaRx Labs (brand: Vedarin, $4.28) to reduce medication costs while maintaining treatment efficacy.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_120', 'new_date': '2025-12-22', 'new_time': '10:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_489', 'start_date': '2025-12-10', 'end_date': '2025-12-16'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_131', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, a patient managing atrial fibrillation and hyperlipidemia, and your email is joshua.wagner@tracer-health.org. You want to explore more affordable suppliers for Atorvastatin to reduce your monthly medication costs, as your current regimen with VedaRx Labs is stable but you are interested in cost optimization. You would like to review your current and optimized medication regimen options to evaluate adherence and cost-saving opportunities, particularly around synchronized fills and packaging. You prefer to check the telemetry upload history for your cardiac event monitor (CARDIA_tracer_469) to assess recent usage and ensure data completeness, especially noting a gap on 2025-12-14. You want to reschedule your cardiology follow-up appointment with Dr. Bryan Bryant from the morning of 2025-12-17 to the afternoon of 2025-12-18 at 14:00, because it aligns better with your schedule and avoids a cluster of morning appointments. After that, you would like to confirm the updated appointment schedule to ensure all changes are reflected correctly.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_469'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_079', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and you are considering adding Zolpidem for sleep support. You want to confirm that Zolpidem is safe to take alongside your current medications because you are concerned about potential interactions; the system check shows no high-risk interactions, so it is considered safe. You would also like to identify cost-effective suppliers for Atorvastatin because you are looking to reduce medication expenses, with options available from international and domestic providers at competitive prices. Later, you want to reschedule your cardiology consultation with Dr. Bryant from its current date to the next day at 09:00 because it better fits your availability, and after that, you would like to cancel your follow-up appointment with Dr. Saito due to a scheduling conflict.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_121', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_081'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, a patient with atrial fibrillation and hyperlipidemia, managing your care through telehealth and currently on Warfarin and Atorvastatin. You want to explore lower-cost suppliers for Atorvastatin to reduce your medication expenses. You would like to reschedule your device coaching appointment with Jennifer Roth, the device coach, from Wednesday to Thursday because of a time conflict, and you prefer the appointment on Thursday at 09:00 as it fits better with your schedule. After that, you want to cancel your overlapping medication review appointment to avoid duplication of visits. Later, you would like to review the available telemetry devices in the system to understand current inventory, and you also want to check the recent upload history for your cardiac event monitor because you are concerned about syncing and want to ensure consistent usage tracking.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_138', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_185'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_465'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='dustin.weber@tracer-health.org',
        instruction='You are Dustin Weber (dustin.weber@tracer-health.org), a patient with COPD and obstructive sleep apnea, who wants to reschedule your medication review appointment with your primary care provider, Dr. Camila Ortega, from its current time to 14:00 on the next day (2025-12-18), because it better fits your schedule. Later, you would like to cancel your device coaching session with Dr. Robert Wright, as it is no longer needed. After that, you prefer to schedule a new specialist consultation with cardiologist Dr. Robert Smith at 15:00 on the day after (2025-12-19), to address potential cardiovascular concerns related to your respiratory conditions.\n\nUse dustin.weber@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'dustin_weber_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-19', 'time': '15:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'camila_ortega_primary_care_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_148'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_100', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'dustin_weber_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks, a patient with atrial fibrillation and hyperlipidemia, and your email is scott.sparks@tracer-health.org. You want to cancel your device coaching appointment with Joseph Robertson because the technical issues with your cardiac monitor have been resolved. You would like to reschedule your medication review appointment with Dr. Hiroko Saito to Monday, December 22, 2025 at 09:30, because it works better with your morning schedule. After that, you want to schedule a new routine checkup with Dr. Robert Smith, a cardiology specialist, on Tuesday, December 23, 2025 at 10:00, to maintain continuity in your cardiac care. You prefer to use your Aetna insurance for the new appointment.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'scott_sparks_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-23', 'time': '10:00', 'appointment_type': 'routine_checkup'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_saito_cardiology'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_162'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_177', 'new_date': '2025-12-22', 'new_time': '09:30'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kathryn.clark@tracer-health.org',
        instruction='You are Kathryn Clark, a patient with Focal Epilepsy and Generalized Anxiety Disorder, using a wearable EEG device for neurology telemetry. You want to check whether your device WEARAB_tracer_463 uploaded data on 2026-01-15 because you noticed a potential gap in compliance tracking. You also want to evaluate the potential effects of an accidental extra dose of Sertraline in combination with your current medications—Levetiracetam and Sertraline—because you are concerned about drug interactions. After that, you would like to cancel your upcoming neurology follow-up appointment (APPT_tracer_135) with Dr. Brian Roman because you are reevaluating your care plan. You also prefer to review Dr. Brian Roman’s provider details—including his specialty in Neurology, availability on weekdays, and contact information—so you can make an informed decision about future appointments.\n\nUse kathryn.clark@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_463', 'date': '2026-01-15'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_135'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brian_roman_neurology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kathryn.clark@tracer-health.org',
        instruction="You are Kathryn Clark, a patient with focal epilepsy and generalized anxiety disorder using a wearable EEG device for neurology telemetry. You want to verify the telemetry upload for your device on 2025-12-15, which shows 6.2 hours of usage, to ensure data continuity for your care team's review. You also want to confirm potential drug interactions after taking Sertraline, which is already part of your regimen along with Levetiracetam; no interactions were found, so you are reassured about safety. Later, you would like to cancel your scheduled device coaching appointment on 2025-12-17 at 08:00 with Chelsea Buck, an RN specializing in device coaching, because you have resolved the upload issue independently. After that, you would like to explore cardiology care options and request information about Dr. Margaret Thompson, an experienced cardiologist with 25 years in practice and credentials including MD, FACC, and FSCAI, to evaluate her availability and expertise for potential future consultations.\n\nUse kathryn.clark@tracer-health.org for authentication.",
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_463', 'date': '2025-12-15'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_134'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold (kevin.arnold@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia, who uses a cardiac event monitor (CARDIA_tracer_489) for rhythm surveillance. You want to report that your device has not uploaded any data from January 5 to January 11, 2026, as all seven days are missing, which could impact your cardiac monitoring. You would like to update the prescription supplier for Atorvastatin in your medical record (REC_tracer_131) to VedaRx Labs (brand: Atorveeda, $4.05) to reduce medication costs, especially since there are no interactions between Atorvastatin and your current medication Warfarin. Later, you will cancel your scheduled virtual consultation with Dr. Brandi Dixon (APPT_tracer_120) because your sleep issues have resolved and you no longer need to discuss starting Zolpidem.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_489'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_131', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brandi_dixon_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_120'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction="You are Laurie Carson, a patient with Type 1 Diabetes and Hypothyroidism, managing your care via telehealth. You want to confirm that accidentally taking Sertraline does not pose a risk given your current medications (Insulin Lispro and Levothyroxine), because you're concerned about potential side effects. After confirmation, you would like to update the prescription for Insulin Lispro in your medical record to use Lotus Rapid Therapeutics as the supplier, with the brand name Lispry, because it offers a cost-effective and accessible option. You are also interested in learning more about endocrinologist Dr. Hector Lane, including his specialty, experience, and availability, because you're considering him for ongoing endocrine care and want to ensure continuity and expertise in managing your condition.\n\nUse laurie.carson@tracer-health.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_071', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'hector_lane_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction='You are Matthew Smith (email: matthew.smith@tracer-health.org), and you want to check for potential drug interactions between Sertraline and your current medications, Warfarin and Atorvastatin, due to concerns about mood symptoms. After learning of a high-severity interaction with Warfarin, you would like to update the supplier for your Warfarin prescription to VedaRx Labs (brand: Vedarin, $4.28) to reduce medication costs, as it is a lower-cost option that supports long-term adherence. Later, you would like to explore provider options and request detailed information about endocrinologist Dr. Kelly Taylor, including her specialty, availability, and consultation details, to evaluate her as a potential care provider.\n\nUse matthew.smith@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_134', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kelly_taylor_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond (kevin.bond@tracer-health.org). You want to cancel your medication review appointment with Dr. Megan Cook because your concerns have been resolved. You would like to reschedule your consultation with Dr. Bryan Bryant, a cardiologist, to Thursday, December 18, 2025, at 14:00, because it better fits your work schedule. After that, you would like to schedule a new routine checkup with Dr. Owen Shaw, another cardiologist, on Monday, December 22, 2025, at 15:00, to establish continuity of care. You prefer to bill your insurance for the new appointment.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_188'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_121', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_121'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'bryan_bryant_cardiology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'provider_id': 'owen_shaw_cardiology_tracer_0001', 'date': '2025-12-22', 'time': '15:00', 'appointment_type': 'routine_checkup', 'bill_insurance': True}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, a patient with Atrial Fibrillation and Hyperlipidemia, who wants to cancel your medication review appointment with Dr. Thompson because you no longer need the consultation. You would like to reschedule your specialist consultation with Dr. Luis Sims to a later time on the same day, specifically in the afternoon, because it works better with your schedule. After that, you want to book a new routine checkup with Dr. Thomas May on the next day at 09:00, as he is a trusted cardiologist and the time fits your availability. You prefer all visits to be billed to your insurance.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_179'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_128', 'new_date': '2025-12-17', 'new_time': '15:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_179'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'luis_sims_cardiology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_zuniga_tracer_0001', 'provider_id': 'thomas_may_cardiology_tracer_0001', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'routine_checkup', 'bill_insurance': True}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, a patient with hypertension and type 2 diabetes, and your email is sarah.johnson@email.com. You would like to explore more affordable suppliers for Lisinopril because you are looking to reduce your medication costs. You prefer to consider lower-cost international options, such as those from India, due to their significantly lower prices. You would like your medical record to be updated with a note that you are considering switching to a more affordable supplier for Lisinopril. You also want to confirm the details of your upcoming routine checkup appointment with Dr. Garcia, which is scheduled for January 15, 2024, at 09:00, to ensure you have the correct date and time for your visit.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC002', 'note': 'Patient inquiring about lower-cost suppliers for Lisinopril and considering a switch.'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='dustin.weber@tracer-health.org',
        instruction="You are Dustin Weber, a patient with COPD and obstructive sleep apnea, preparing for a medication review with your primary care provider, Dr. Camila Ortega. You want to explore lower-cost suppliers for your Fluticasone Inhaler because you are concerned about medication affordability. You would like a note added to your medical record stating 'Patient requested supplier pricing information for Fluticasone Inhaler during pre-visit intake' so your provider is aware of your cost concerns ahead of the visit. You also prefer to confirm the details of your upcoming virtual appointment, including the scheduled time and secure meeting link, to ensure you can attend without technical issues.\n\nUse dustin.weber@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Fluticasone Inhaler'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_067', 'note': 'Patient requested supplier pricing information for Fluticasone Inhaler during pre-visit intake'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_100'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='omar.hassan2156@email.com',
        instruction='You are Omar Hassan (omar.hassan2156@email.com), a 44-year-old male with hypertension and recent knee surgery, who wants to maintain continuity in your care while adjusting your appointment schedule. You want to schedule a routine checkup with your primary care provider, Dr. Lisa Chen, on 2025-10-06 at 09:00 because it aligns with your availability and allows for general health monitoring. Later, you would like to reschedule your orthopedic follow-up appointment (APPT054) with Dr. Maria Rodriguez from 2025-10-02 to 2025-10-09 at 11:00 due to a scheduling conflict, as this new time works better for your recovery timeline. After that, you would like to cancel your physical therapy session (APPT055) with PT James Chen because you feel it can be postponed without impacting your recovery.\n\nUse omar.hassan2156@email.com for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'omar_hassan_2156', 'provider_id': 'dr_chen_primary_care', 'date': '2025-10-06', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT054'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT054', 'new_date': '2025-10-09', 'new_time': '11:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT055'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'omar_hassan_2156'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sharon.baird@tracer-health.org',
        instruction="You are Sharon Baird (sharon.baird@tracer-health.org) and you want to review the details of your upcoming device coaching session with Kimberly Wade (RN), scheduled for tomorrow, because you've been having trouble with your nightly EEG device uploads and need clarity ahead of the visit. You would like to schedule a neurology follow-up appointment with Dr. Patel (MD) on the next day at 07:30 for a follow-up on your epilepsy management, as this time aligns with your morning routine and allows continuity in care. You also want to verify the upload data from your telemetry device on the day before yesterday, which showed 6.7 hours of usage, to assess compliance and identify patterns affecting data transmission. You prefer to confirm there are no adverse interactions between Sertraline and your current medication Levetiracetam, which is important for safely managing both your anxiety and epilepsy. Lastly, you would like to explore other available providers across specialties to understand your care options, particularly in case future consultations are needed beyond neurology or device support.\n\nUse sharon.baird@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_166'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sharon_baird_tracer_0001', 'provider_id': 'dr_patel_neurology', 'date': '2025-12-22', 'time': '07:30', 'appointment_type': 'follow_up'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kimberly_wade_device_coaching_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_479', 'date': '2025-12-16'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, a patient managing atrial fibrillation and hyperlipidemia, currently taking Warfarin and Atorvastatin. You want to explore more affordable suppliers for Atorvastatin to reduce medication costs, and you would like to confirm there are no harmful interactions between Atorvastatin and your current medications—especially Warfarin—because you prioritize safe and cost-effective treatment. You also want to learn more about available cardiology providers, with a specific interest in Dr. Brandi Dixon, because she is your scheduled specialist and you value continuity of care. Finally, you would like to review the details of your upcoming follow-up appointment on December 17, 2025, and the associated medical record from that visit, so you can stay informed about your care plan and treatment progress.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brandi_dixon_cardiology_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_078'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_078'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction="You are Matthew Smith, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and your email is matthew.smith@tracer-health.org. You want to explore cost-saving options for your Atorvastatin prescription by reviewing available suppliers, because you are interested in potentially lowering medication expenses. You would like to confirm there are no adverse interactions between Atorvastatin and your current Warfarin therapy, because you want to ensure your regimen remains safe. You prefer to see the list of available cardiology providers and then focus on Dr. Robert Smith's credentials and availability, because you are considering continuity with your current specialist. You would like to review the details of your upcoming follow-up appointment scheduled with Dr. Robert Smith, because you want to confirm the visit logistics and clinical purpose. After that, you want to access the associated medical record from that appointment, because you wish to understand your current care plan and treatment recommendations.\n\nUse matthew.smith@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_083'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_083'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction='You are Diane Robinson, a patient with Type 1 Diabetes and Hypothyroidism, who uses a continuous glucose monitor (CONTIN_tracer_484) and takes Insulin Lispro and Levothyroxine. You want to confirm that the missing telemetry upload on 2026-01-16 is noted for clinical review because it may affect glucose trend accuracy. You would like to verify that taking an extra dose of Insulin Lispro does not pose a high-risk interaction with your current medications, as you are concerned about potential hypoglycemia. You prefer to keep Insulin Lispro supplied by Bengal EndoCare (SwiftLis) at the lower cost of $19.20, as this was already documented in your medical record (REC_tracer_066) from your medication review appointment on 2025-12-17, because it supports long-term affordability without changing therapeutic effectiveness.\n\nUse diane.robinson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_484', 'date': '2026-01-16'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_066', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'diane_robinson_tracer_0001'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'diane_robinson_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_099'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, a patient with atrial fibrillation and anxiety preparing for an ablation, and your email is yumi.tanaka7410@pacificcare.org. You want to verify that your telemetry device WEARAB_tracer_483 has a missing upload on 2026-01-10 because you are tracking compliance ahead of your procedure. You also need to check for drug interactions because you recently took Sertraline, and you are concerned about safety given your current medications—Warfarin, Sertraline, Aspirin EC, and Metoprolol Succinate—which have a high-severity interaction between Sertraline and Warfarin requiring urgent review. Later, you would like to update the supplier for Sertraline in medical record REC012 to Triveni Pharma, brand Setrina, priced at $4.55, because it is more cost-effective than your current supplier. You also want to review your medical records, particularly REC012 from your pre-procedure assessment, and get full details about your upcoming cardiology appointment APPT029 scheduled for May 12, 2025, to ensure all pre-ablation requirements are met.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_483', 'date': '2026-01-10'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'yumi_tanaka_7410'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'yumi_tanaka_7410'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT029'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, a patient managing atrial fibrillation and hyperlipidemia, with email shawn.carter@tracer-health.org. You want to reschedule your follow-up appointment with Dr. Owen Shaw from its current date to Monday, 2025-12-22 at 14:00 because it better fits your schedule. You also want to check for potential drug interactions between Sertraline and your current medications Warfarin and Atorvastatin due to concerns about starting a new antidepressant while on anticoagulation therapy. Later, you would like to review the telemetry data from your cardiac event monitor (device ID CARDIA_tracer_461) for December 17, 2025, to assess your usage compliance. After that, you would like to cancel your scheduled device coaching appointment with Anthony Moran on December 17, 2025, and instead schedule a new medication review appointment with Dr. Robert Smith, a cardiologist, on Thursday, December 18, 2025, at 09:00, because you need a comprehensive review of your current regimen with a specialist. You prefer this visit to be billed to your insurance.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_131', 'new_date': '2025-12-22', 'new_time': '14:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'owen_shaw_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_461', 'date': '2025-12-17'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_130'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_carter_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'medication_review', 'bill_insurance': True}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_130'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='charles.levine@tracer-health.org',
        instruction='You are Charles Levine (charles.levine@tracer-health.org). You want to cancel your scheduled family consultation with Dr. Miller on 2025-12-17 at 08:30 because it is no longer needed. You would like to schedule a new psychiatry consultation with Dr. Philip Mendoza, preferably on 2025-12-19 at 13:00, because he is a trusted provider and the time works well with your schedule. Later, you want to reschedule your care coordination appointment with Dr. Linda Collins from 2025-12-18 at 10:00 to 2025-12-19 at 11:00 to consolidate your visits on the same day for convenience.\n\nUse charles.levine@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_208'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'philip_mendoza_psychiatry_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'charles_levine_tracer_0001', 'provider_id': 'philip_mendoza_psychiatry_tracer_0001', 'date': '2025-12-19', 'time': '13:00', 'appointment_type': 'consultation'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_209', 'new_date': '2025-12-19', 'new_time': '11:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sandra.brown@tracer-health.org',
        instruction='You are Sandra Brown, a patient with hypertension and type 2 diabetes, and you want to review the details of your upcoming follow-up appointment with Dr. Garcia, who is your primary care provider and speaks Spanish, because you prefer continuity of care and effective communication. The appointment is scheduled for the next day and is a virtual visit focused on managing your blood pressure and diabetes. You also want a complete list of your medical records because you are ensuring all your health information is up to date and aligned with your current treatment plan.\n\nUse sandra.brown@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_094'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'sandra_brown_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='nadia.abbasi@tracer-health.org',
        instruction='You are Nadia Abbasi (nadia.abbasi@tracer-health.org), a patient with Type 2 Diabetes and Hypertension, who wants to reduce medication costs and improve adherence. You want to explore lower-cost supplier options for Lisinopril because the current expense is burdensome. You would like to confirm that switching to Lisinopril from Mumbai Cardio Pharma (brand: Lisipril-M) is safe with your current medication, Metformin, because there are no high-risk interactions. You prefer to update your prescription record to use Mumbai Cardio Pharma as the supplier for Lisinopril to benefit from the lower price of $2.80 per tablet. After that, you would like to review optimized regimen options to further reduce costs and improve adherence, such as synchronized refills or unit-dose packaging, because they can minimize pharmacy visits and help prevent missed doses.\n\nUse nadia.abbasi@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_034', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'nadia_abbasi_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, a patient managing atrial fibrillation and anxiety, with email yumi.tanaka7410@pacificcare.org. You want to reschedule your cardiology consultation with Dr. Thompson from May 19 to May 22 at 14:00 because it better fits your schedule. After that, you would like to check for drug interactions due to an accidental extra dose of Sertraline, as you are concerned about safety given your current medications including Warfarin. You also prefer to update the Sertraline prescription in your medical record to a more cost-effective supplier, ideally Triveni Pharma (brand Setrina) at $4.55, but are open to alternatives if not available, because you are proactive about medication affordability.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT030', 'new_date': '2025-05-22', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'yumi_tanaka_7410'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
        ],
        outputs=[],
    ),

    Task(
        user_id='carlos.mendez4521@email.com',
        instruction='You are Carlos Mendez (email: carlos.mendez4521@email.com). You want to reschedule your follow-up appointment with Dr. Chen from the original date to Friday, 2025-10-17 at 10:00 because it better fits your schedule. After that, you would like to check for potential drug interactions between Sertraline and your current medications (Ibuprofen and Acetaminophen) to ensure safety, which has been confirmed as low-risk. Subsequently, you prefer to update the prescription for Sertraline in medical record REC027 to use the supplier Buenos Spirits with the brand name Calmist at $5.90 per unit because it offers a more affordable option while maintaining treatment continuity.\n\nUse carlos.mendez4521@email.com for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT056', 'new_date': '2025-10-17', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'carlos_mendez_4521'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Ibuprofen', 'Acetaminophen']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC027', 'medication': 'Sertraline', 'supplier_company': 'Buenos Spirits', 'brand_name': 'Calmist', 'price_usd': 5.9}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction="You are Yumi Tanaka, a patient with atrial fibrillation and anxiety, who accidentally took an extra dose of Sertraline this morning. You want to run a drug interaction check between Sertraline and your current medications (Warfarin, Aspirin EC, Metoprolol Succinate) because of concerns about potential adverse effects, especially bleeding risk. After the interaction check confirms a high-severity interaction between Sertraline and Warfarin, you would like your Sertraline prescription in medical record REC012 to be updated to use Triveni Pharma's Setrina brand at $4.55, as it is more affordable than your current Harmony Labs (Sertrawin) supplier. After the update, you want a note added to the record confirming the supplier change and that you were advised to monitor for bleeding symptoms due to the interaction risk.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC012', 'note': 'Updated Sertraline prescription supplier to Triveni Pharma (Setrina) at $4.55 per unit after patient reported accidental overdose and requested cost reduction. Patient advised to monitor for bleeding symptoms and report any concerns.'}),
        ],
        outputs=[],
    ),
]
