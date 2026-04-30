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

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, a patient with Type 2 Diabetes and Hypertension, and your email is sarah.johnson@email.com. You want to reschedule your routine checkup with your primary care provider, Dr. Garcia, from its original date to next Monday at 10:00, because it works better with your schedule. Later, you would like to schedule a new telehealth consultation with your cardiologist, Dr. Smith, on the following Thursday at 16:00 to discuss your hypertension management, as you prefer continuity with your specialist care.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT001', 'new_date': '2024-01-22', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'sarah_johnson_1234'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_johnson_1234', 'provider_id': 'dr_smith_cardiology', 'date': '2024-01-18', 'time': '16:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='nadia.abbasi@tracer-health.org',
        instruction='You are Nadia Abbasi, managing hypertension and type 2 diabetes, and you want to reschedule your medication review appointment with Dr. Garcia from its current date to next Sunday at 09:30 because of a scheduling conflict. Later, you would like to schedule a new routine checkup with Dr. Dana Padilla, a primary care provider, on Tuesday (in 3 days) at 09:00 to maintain continuity in your chronic condition monitoring. You prefer both appointments to be billed to your UnitedHealthcare insurance.\n\nUse nadia.abbasi@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_063', 'new_date': '2025-12-07', 'new_time': '09:30'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'nadia_abbasi_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'nadia_abbasi_tracer_0001', 'provider_id': 'dana_padilla_primary_care_tracer_0001', 'date': '2025-12-02', 'time': '09:00', 'appointment_type': 'routine_checkup', 'bill_insurance': True}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_garcia_primary'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='cynthia.scott@tracer-health.org',
        instruction='You are Cynthia Scott (cynthia.scott@tracer-health.org) and you want to cancel your follow-up appointment with Dr. Camila Ortega scheduled for 2025-12-17 at 09:00 because you need to adjust your schedule. You would like to reschedule your medication review appointment with Dr. Nicholas Salinas from 2025-12-17 at 14:00 to the next day at the same time (14:00) because it works better for your availability. After that, you want to view the updated details of your rescheduled appointment and your full appointment list to confirm the changes. You also want to check for drug interactions after accidentally taking Sertraline, as you are currently on Metformin and Lisinopril for diabetes and hypertension management. Since no high-risk interactions are found, you would like to proceed with updating the supplier for your Lisinopril prescription from Mumbai Cardio Pharma (Lisipril-M) to Hyderabad Heart Meds (brand name Sinopril-H) for personal access or preference reasons, even though it is slightly more expensive.\n\nUse cynthia.scott@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_076'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_098', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_098'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'cynthia_scott_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_065', 'medication': 'Lisinopril', 'supplier_company': 'Hyderabad Heart Meds', 'brand_name': 'Sinopril-H', 'price_usd': 3.1}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, a patient on Warfarin, Sertraline, Aspirin EC, and Metoprolol Succinate, preparing for cardiac ablation and concerned about medication safety and cost. You want to check for potential drug interactions between Sertraline and your other medications because you are anxious about overlapping effects, especially with your upcoming procedure. You would like to update your Sertraline prescription in your medical record to use Triveni Pharma from India, brand name Setrina, priced at $4.55, because it is a lower-cost option that aligns with your budget. You also prefer to receive a full list of available Sertraline suppliers so you can compare all options and make an informed decision about your medication source.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction='You are David Martinez, a patient with generalized anxiety disorder currently taking Sertraline and Claritin, and your email is david.martinez@email.com. You want to check for potential drug interactions between Sertraline and your current medications because you are concerned about safety; the check confirms no high-risk interactions are present. You would like to update your prescription record (REC001) to reflect a new supplier for Sertraline because you found a more affordable option. You prefer to use Gujarat MindCare in India, which provides the medication under the brand name Serenem at $4.65 per unit, to reduce your medication costs.\n\nUse david.martinez@email.com for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction='You are Matthew Smith (matthew.smith@tracer-health.org), a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to confirm there are no harmful interactions with Zolpidem you recently took, because you are concerned about safety with your current regimen. You would like to update your Warfarin prescription in your medical record to use the lower-cost supplier Sunrise Biotech (brand name Warfast), because it reduces your out-of-pocket expense. You prefer to verify that your cardiac event monitor data was fully uploaded on the night of December 14, 2025, because you noticed a sync issue, but the system confirms no data was missing. You want to reschedule your medication review appointment with Dr. Owen Shaw from December 17 to Thursday, December 18 at 14:00, because it better fits your schedule, and the time is available. After that, you would like to review all your upcoming scheduled appointments to ensure accuracy after the change.\n\nUse matthew.smith@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_134', 'medication': 'Warfarin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Warfast', 'price_usd': 4.35}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': None, 'limit': None}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_481', 'date': '2025-12-14'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_190', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'matthew_smith_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and your email is edward.rice@tracer-health.org. You want to discuss the high-severity interaction between Sertraline and Warfarin before considering mood support medication, because it poses a significant bleeding risk. You would like to update your Warfarin prescription to use the supplier VedaRx Labs with brand name Vedarin at $4.28, as it is the most cost-effective option available internationally. You prefer to verify telemetry uploads for your cardiac event monitor (CARDIA_tracer_465), because you had a coaching session on device use and want to confirm compliance, and recent data shows 7.0 hours of usage on 2025-12-17. You want to reschedule your follow-up appointment with Dr. Brandi Dixon from 2025-12-17 to 2025-12-22 at 09:00, because it better fits your schedule, and that slot is available. After that, you would like to review your updated appointment list to confirm all changes.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_129', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_465', 'date': '2025-12-17'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_078', 'new_date': '2025-12-22', 'new_time': '09:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'edward_rice_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, a patient with atrial fibrillation and hyperlipidemia, and your email is shawn.zuniga@tracer-health.org. You want to reschedule your cardiology appointment with Dr. Luis Sims from its original date to Wednesday, December 24th at 3:00 PM because it works better for your schedule. Later, you would like to cancel your other cardiology appointment with Dr. Margaret Thompson on the same day because you only need one specialist consultation. After that, you would like to schedule a new routine checkup with primary care provider Dr. Howard Mccarthy on Wednesday, December 24th at 3:00 PM to maintain continuity in care. You also want to explore other available providers for future healthcare needs.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_128', 'new_date': '2025-12-24', 'new_time': '15:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_179'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_zuniga_tracer_0001', 'provider_id': 'howard_mccarthy_primary_care_tracer_0001', 'date': '2025-12-24', 'time': '15:00', 'appointment_type': 'routine_checkup'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks (scott.sparks@tracer-health.org) and you want to reschedule your cardiology consultation with Dr. Juan Fitzgerald from the original time to the next day at 10:00 because it works better with your daily routine. Later, you will cancel your device coaching session scheduled for the same day as the original appointment because you have resolved the upload issue independently. After that, you would like to schedule a new follow-up appointment with Dr. Bryan Bryant on the following day at 11:00 to review your cardiac rhythm monitoring results, as it aligns with your availability and care plan.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_126', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_162'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'scott_sparks_tracer_0001', 'provider_id': 'bryan_bryant_cardiology_tracer_0001', 'date': '2025-12-19', 'time': '11:00', 'appointment_type': 'follow_up'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction="You are kevin.arnold@tracer-health.org. You want to accomplish these, in order:\n1. Hi, my email is kevin.arnold@tracer-health.org. I need to cancel my appointment APPT_tracer_080 with Dr. Christine Bailey. Also, I'd like to see the details of this appointment and the provider details for Dr. Bailey.\n2. I want to check medication suppliers for Atorvastatin and run a drug interaction check between Atorvastatin and my current medications (Warfarin, Atorvastatin). Then, I'd like to update my prescription supplier for Atorvastatin in record REC_tracer_131 to Sunrise Biotech (brand: Lipistal, price: $4.15). Finally, add a note to this record saying 'Patient requested supplier update for cost savings.'\n3. Please list my assigned telemetry devices and check the upload history for device CARDIA_tracer_489.\n\nUse kevin.arnold@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'christine_bailey_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_131', 'medication': 'Atorvastatin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Lipistal', 'price_usd': 4.15}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_131', 'note': 'Patient requested supplier update for cost savings.'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_489'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='robert.martinez5589@email.com',
        instruction='You are Robert Martinez (robert.martinez5589@email.com), a 61-year-old male with coronary artery disease, hypertension, type 2 diabetes, and hyperlipidemia. You want to cancel your scheduled CABG surgery appointment (APPT058) due to a personal scheduling conflict. After that, you would like to schedule a follow-up cardiology consultation with Dr. Hiroko Saito on Monday, 2025-04-07 at 07:30, because it aligns with your availability and you prefer continuity with a cardiologist before surgery. You prefer this time as it fits your morning routine. Later, you want to check for drug interactions because you accidentally took Sertraline, which could interact with your current medications, particularly increasing bleeding risk with Aspirin. After reviewing the interaction, you would like to update your Atorvastatin prescription in medical record REC028 to use the supplier Sunrise Biotech with brand name Lipistal at $4.15 for cost savings, although this option is not currently available in the supplier network.\n\nUse robert.martinez5589@email.com for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT058'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'robert_martinez_5589', 'provider_id': 'dr_saito_cardiology', 'date': '2025-04-07', 'time': '07:30', 'appointment_type': 'follow_up'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_saito_cardiology'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Atorvastatin', 'Metoprolol', 'Aspirin', 'Metformin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC028', 'medication': 'Atorvastatin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Lipistal', 'price_usd': 4.15}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'robert_martinez_5589'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, a patient with atrial fibrillation and hyperlipidemia, and your email is joshua.wagner@tracer-health.org. You want to cancel your scheduled device coaching appointment on 2025-12-17 at 08:00 because of a scheduling conflict. After that, you would like to schedule a follow-up appointment with Dr. Kelly Brown, a neurology specialist, on 2025-12-22 at 14:30 because it aligns with your availability and the provider’s schedule. Later, you would like to update your Atorvastatin prescription in your medical record to use the supplier Qianlong Remedies, which offers the brand LongStat at a lower cost of 5.4 USD, because you are seeking to reduce your medication expenses. You prefer this change only after confirming there are no safety concerns with switching, which has been verified through a drug interaction check with your current medication Warfarin.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_146'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'joshua_wagner_tracer_0001', 'provider_id': 'kelly_brown_neurology_tracer_0001', 'date': '2025-12-22', 'time': '14:30', 'appointment_type': 'follow_up'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kelly_brown_neurology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Neurology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_130', 'medication': 'Atorvastatin', 'supplier_company': 'Qianlong Remedies', 'brand_name': 'LongStat', 'price_usd': 5.4}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez, authenticated via amanda.martinez@tracer-health.org, and you want to reschedule your medication review appointment with your primary care provider, Dr. John Wise, from December 17 to December 19 at 10:00 AM because the new time better fits your schedule. During this visit, you would like to discuss cost-saving alternatives for your Insulin Lispro prescription and request a drug interaction check between Insulin Lispro and your current medications, including Levothyroxine, to ensure safety before any changes. After confirming no interactions, you prefer to update the prescription in medical record REC_tracer_063 to reflect the new supplier, Lotus Rapid Therapeutics, using the brand name Lispry at $19.75 per unit, even though a slightly lower-cost option exists, because you have a preference for this supplier. Later, you would like to review your continuous glucose monitor (device CONTIN_tracer_464) telemetry data from December 17, 2025, to assess your compliance and usage patterns following a recent coaching session, noting that the device was used for 7 hours that day.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_096', 'new_date': '2025-12-19', 'new_time': '10:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'john_wise_primary_care_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_063', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_464', 'date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction="You are Yumi Tanaka, patient with email yumi.tanaka7410@pacificcare.org, managing atrial fibrillation and anxiety. You want to update the Sertraline prescription in your medical record REC012 to use Gujarat MindCare's brand Serenem at $4.65, because it is a slightly more affordable option than your current supplier. After that, you would like to cancel your upcoming cardiology specialist consultation scheduled for May 19, because you have a scheduling conflict.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT030'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='michelle.adams@tracer-health.org',
        instruction='You are Michelle Adams (michelle.adams@tracer-health.org), a patient with Type 1 Diabetes and hypothyroidism, who initially wants to review the details of your follow-up appointment with Dr. Charles Scott and see all your scheduled visits. You then decide to cancel that appointment due to a scheduling conflict on 2025-12-17 at 09:00. At the same time, you want to explore other endocrinology providers for future care options. Later, you would like to reschedule your other follow-up appointment with Dr. Hector Lane to 13:00 on the same day (2025-12-19) for better convenience, as the later time fits your schedule better, and you prefer continuity with your current endocrinologist for ongoing diabetes management.\n\nUse michelle.adams@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_087'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'michelle_adams_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_087'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_145', 'new_date': '2025-12-19', 'new_time': '13:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'hector_lane_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction="You are Shawn Carter, a patient with atrial fibrillation and hyperlipidemia, managing Warfarin and Atorvastatin. You want to review your current medication regimen and explore more affordable supplier options for Warfarin, particularly considering Sunrise Biotech's brand Warfast at $4.35 per tablet, because it offers a cost-effective alternative to your current supplier. You would like to confirm that your cardiac monitor (CARDIA_tracer_461) has no missing data uploads, especially around 2025-12-14, to ensure continuous cardiac monitoring. You also want to check for potential drug interactions between Aspirin and your current medications, and based on the moderate interaction risk with Warfarin, you prefer to avoid Aspirin unless directed by your cardiologist. After this review, you would like to update your Warfarin prescription in medical record REC_tracer_122 to reflect the new supplier, Sunrise Biotech, with the brand Warfast. Subsequently, you want to cancel your scheduled consultation with Dr. Guzman (APPT_tracer_127) on 2025-12-17, because your follow-up needs are better aligned with your primary cardiologist. After that, you would like to schedule a new follow-up appointment with Dr. Smith, your cardiologist, on 2025-12-19 at 11:00, because it aligns with your schedule and ensures continuity of care.\n\nUse shawn.carter@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_122'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_461', 'date': '2025-12-14'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Aspirin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_122', 'medication': 'Warfarin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Warfast', 'price_usd': 4.35}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_127'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_carter_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-19', 'time': '11:00', 'appointment_type': 'follow_up'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction='You are a telehealth agent supporting Diane Robinson (diane.robinson@tracer-health.org), who has Type 1 Diabetes and Hypothyroidism. You want to first review the details of her scheduled follow-up appointment with Dr. Ashley Schneider (Endocrinology) on 2025-12-17 at 09:00, which is a 30-minute telehealth visit for diabetes and thyroid management. After reviewing, you would like to cancel this appointment because she no longer wishes to proceed with it at this time. You also want to obtain provider details for Dr. Ashley Schneider, including her contact information and specialty, to better understand her clinical background and availability. Later, you would like to check for potential drug interactions between Insulin Lispro and her current medications (Insulin Lispro and Levothyroxine), and the result confirms no high-risk interactions, which supports safe medication management. After that, you would like to update the prescription supplier for Insulin Lispro in medical record REC_tracer_066 from SwiftLis (Bengal EndoCare, $19.20) to Lispry by Lotus Rapid Therapeutics at $19.75, as part of her ongoing cost and treatment optimization strategy, even though the new option is slightly more expensive, because she prefers the reliability and service of the new supplier.\n\nUse diane.robinson@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'ashley_schneider_endocrinology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_066', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'diane_robinson_tracer_0001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction="You are Kevin Arnold (kevin.arnold@tracer-health.org), a cardiology patient managing atrial fibrillation and hyperlipidemia. You want to cancel your scheduled follow-up appointment with Dr. Christine Bailey on 2025-12-17 at 09:00 because you are reviewing alternative cardiology providers. You would like to review Dr. Bailey's credentials and availability, and you are interested in exploring other cardiology specialists for potential continuity of care. Later, you will check for drug interactions because you accidentally took Sertraline, which may interact severely with your current Warfarin regimen, so you need clinical guidance on whether to hold your next dose. After that, you would like to update the supplier for your Atorvastatin prescription in record REC_tracer_131 to Sunrise Biotech (brand: Lipistal, price: $4.15) to reduce medication costs. You also want to review your current and optimized regimen options to evaluate cost, pill burden, and adherence support, with a preference for lower-cost generics and improved medication management.\n\nUse kevin.arnold@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'christine_bailey_cardiology_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_131', 'medication': 'Atorvastatin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Lipistal', 'price_usd': 4.15}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond (kevin.bond@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia managing Warfarin and Atorvastatin. You want to schedule a new specialist consultation with Dr. Margaret Thompson, a cardiologist, on Friday (2025-12-19) at 09:00 because you are seeking a second opinion. You also want to reschedule your follow-up appointment with your current cardiologist, Dr. Hiroko Saito, from Thursday morning to Thursday (2025-12-18) at 10:00 because it better fits your schedule. Later, you would like to cancel your duplicate medication review appointment with Megan Cook on Wednesday (2025-12-17) at 09:00. You are reviewing potential drug interactions and are aware that combining Aspirin with Warfarin carries a moderate risk, so you prefer to avoid Aspirin unless clinically necessary. You would like to update the prescription for Atorvastatin to be supplied by VedaRx Labs (brand Atorveeda, $4.05) to reduce costs and align with your optimized regimen plan, which supports both cost savings and adherence. You prefer to manage your care through cost-effective, coordinated prescriptions and convenient virtual visits with cardiology specialists.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'provider_id': 'dr_thompson_cardiology', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_188'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_081'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_081', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_saito_cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_132', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_132'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold, a patient with atrial fibrillation and hyperlipidemia, and your email is kevin.arnold@tracer-health.org. You want to reschedule your cardiology follow-up appointment with Dr. Christine Bailey from its current date to next Monday, because it works better for your schedule. Later, you will cancel your medication review appointment, as it is no longer needed after the changes to your plan. You would like to check the cardiac monitor data from your device for 2025-12-15, because you want to review your heart rhythm trends. You also need to know if taking Sertraline interacts with your current medications, because you accidentally took it and are concerned about safety. After learning of a high-risk interaction with Warfarin, you prefer to update your Atorvastatin prescription to be supplied by Bharat Lifecare (brand: Cholozen) for cost savings, as it is a lower-cost option. Finally, you want to add a note to your medical record explaining that the supplier change was requested to reduce medication costs.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_080', 'new_date': '2025-12-22', 'new_time': '10:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_187'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'christine_bailey_cardiology_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_473', 'date': '2025-12-15'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_131', 'medication': 'Atorvastatin', 'supplier_company': 'Bharat Lifecare', 'brand_name': 'Cholozen', 'price_usd': 4.3}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_131', 'note': 'Patient requested supplier change for cost savings.'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_131'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kathryn.clark@tracer-health.org',
        instruction='You are Kathryn Clark, a patient managing focal epilepsy and generalized anxiety disorder through telehealth, and you want to optimize your upcoming care coordination. You would like to reschedule your neurology follow-up with Dr. Brian Roman from its current date to the next day, as it better fits your schedule and allows earlier review of your condition. After that, you would like to cancel your scheduled device coaching session with the device coach, as you prefer to address device concerns directly with your neurologist. You also want to schedule a new follow-up appointment with Dr. Kevin Salas, a neurologist, in three days at 09:30, because you value continuity in neurological care and the time works well for your routine. You prefer video visits for all appointments and would like to use your UnitedHealthcare insurance for billing, with copayments as applicable. You are concerned about having taken an extra dose of Sertraline and want to confirm there are no harmful interactions with your current medications, Levetiracetam and Sertraline, which has been checked and shows no high-risk interactions. You also want to review the recent usage data from your wearable EEG device (WEARAB_tracer_463) for the past week, particularly noting a full day with no upload on 2025-12-14, to discuss compliance and patterns with your provider. Finally, you would like to confirm the details of your rescheduled neurology appointment, access the associated medical record, and review your full list of upcoming appointments to ensure everything is coordinated.\n\nUse kathryn.clark@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Neurology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kathryn_clark_tracer_0001', 'provider_id': 'kevin_salas_neurology_tracer_0001', 'date': '2025-12-22', 'time': '09:30', 'appointment_type': 'follow_up'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_135', 'new_date': '2025-12-18', 'new_time': '10:30'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_134'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kevin_salas_neurology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'WEARAB_tracer_463', 'start_date': '2025-12-10', 'end_date': '2025-12-16'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_135'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_135'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kathryn_clark_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond (kevin.bond@tracer-health.org) and you want to review available cardiology providers to understand your specialist options. You then specifically want to learn about Dr. Bryan Bryant, including his availability and $225 consultation fee, to evaluate suitability for your needs. After reviewing his details, you have decided to cancel your scheduled telehealth appointment with him because you no longer wish to proceed with this consultation.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'bryan_bryant_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_121'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='molly.hill@tracer-health.org',
        instruction='You are Molly Hill (molly.hill@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to review available endocrinologists for follow-up care. You would like detailed information about Dr. Kelly Taylor, including her schedule and contact details, because you are considering continuity with your current specialist. After reviewing, you decide to cancel your scheduled follow-up appointment with Dr. Kelly Taylor on December 19, 2025, at 10:00 due to a scheduling conflict.\n\nUse molly.hill@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kelly_taylor_endocrinology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_153'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.barnes@tracer-health.org',
        instruction='You are Sarah Barnes, a patient with Type 2 Diabetes and Hypertension, and you want to check for drug interactions after accidentally taking Sertraline; you are reassured there are no high-risk interactions with your current medications (Metformin and Lisinopril). You would like to update your Lisinopril prescription in your medical record to use the lower-cost supplier Mumbai Cardio Pharma, brand Lisipril-M at $2.80 per unit, because it reduces your monthly medication cost. After that, you want to review your full regimen optimization options, including cost-synchronized generic fills and adherence packaging, to improve affordability and medication adherence.\n\nUse sarah.barnes@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_120', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'sarah_barnes_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.osborne@tracer-health.org',
        instruction='You are Matthew Osborne, a patient with COPD and sleep apnea managing medication costs and device compliance. You want to explore lower-cost suppliers for your Fluticasone Inhaler to reduce financial burden while maintaining treatment effectiveness, and you would like to document this discussion in your medical record REC_tracer_072. You also want to review your ventilator usage data from device PHILIP_tracer_466 for 2025-12-11 to assess compliance, and you would like to confirm there are no harmful interactions between Fluticasone Inhaler and your current medications (Fluticasone Inhaler and Montelukast) to ensure safety. Later, you would like to cancel your scheduled pulmonology follow-up appointment APPT_tracer_141 with Dr. Amelia Quinn due to a scheduling conflict, and you prefer to reschedule it with the same provider on 2025-12-23 at 08:00 because it aligns with your availability and her schedule, ensuring continuity of care.\n\nUse matthew.osborne@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Fluticasone Inhaler'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'matthew_osborne_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_072', 'note': 'Patient discussed lower-cost supplier options for Fluticasone Inhaler during telehealth visit.'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped', 'limit': 5}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'PHILIP_tracer_466', 'date': '2025-12-11'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Fluticasone Inhaler', 'current_medications': ['Fluticasone Inhaler', 'Montelukast']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_141'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'matthew_osborne_tracer_0001', 'provider_id': 'amelia_quinn_pulmonology_tracer_0001', 'date': '2025-12-23', 'time': '08:00', 'appointment_type': 'follow_up'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'amelia_quinn_pulmonology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction="You are Amanda Martinez, a patient with Type 1 Diabetes and Hypothyroidism, managing your care through telehealth. You want to explore more affordable suppliers for your Insulin Lispro medication to reduce out-of-pocket costs, because affordability is a key concern in your treatment plan. You would like to review your current and optimized regimen options, including the 'Cost-Synchronized Generic Fill' and 'Adherence Packaging Option', to make informed decisions about cost and convenience. You prefer to document this discussion in your medical record REC_tracer_063, because it captures the clinical rationale for considering lower-cost alternatives. You also want to check which telemetry devices are assigned to you, and you need to verify the usage hours of your Continuous Glucose Monitor (CONTIN_tracer_464) on the previous day, because you are monitoring adherence and device performance. You would like to confirm there are no drug interactions between Insulin Lispro and your current medications (Insulin Lispro and Levothyroxine), because safety is a priority when evaluating medication changes. Later, you decide to cancel your scheduled medication review appointment with Dr. John Wise on 2025-12-17, because you need a more convenient time. After that, you would like to reschedule the appointment with Dr. John Wise for the next day at 14:00, because it aligns better with your availability and the time is available in his schedule.\n\nUse amanda.martinez@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_063', 'note': 'Patient discussed supplier pricing options for Insulin Lispro during medication cost review.'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped', 'limit': 1}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_464', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_096'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'amanda_martinez_tracer_0001', 'provider_id': 'john_wise_primary_care_tracer_0001', 'date': '2025-12-18', 'time': '14:00', 'appointment_type': 'medication_review'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'john_wise_primary_care_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson (sarah.johnson@email.com), managing hypertension and type 2 diabetes, and you want to maintain continuity with your trusted cardiology provider, Dr. Robert Smith. You would like to schedule a new specialist consultation with him on the next day at 11:00 because it aligns with your ongoing hypertension management plan. You also want to reschedule your routine checkup with Dr. Garcia from 09:00 to 10:00 on the same day to better fit your morning schedule. After that, you would like to review all your current appointments to confirm your upcoming care plan.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_johnson_1234', 'provider_id': 'dr_smith_cardiology', 'date': '2024-01-22', 'time': '11:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT001', 'new_date': '2024-01-15', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'sarah_johnson_1234'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, a patient with hypertension and type 2 diabetes, managing your care through the telehealth portal. You want to schedule a new routine checkup with your primary care provider, Dr. Carlos Garcia, on the next available day (January 16) at 10:00 AM because it fits your schedule and allows timely monitoring of your conditions. Later, you would like to reschedule your existing appointment from January 15 at 09:00 AM to January 17 at 14:00 PM due to a personal conflict, as the new time aligns better with your availability. After that, you want to review your complete list of upcoming appointments to confirm all changes have been applied and ensure continuity in your care plan.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_johnson_1234', 'provider_id': 'dr_garcia_primary', 'date': '2024-01-16', 'time': '10:00', 'appointment_type': 'routine_checkup'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT001', 'new_date': '2024-01-17', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'sarah_johnson_1234'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner (joshua.wagner@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia using a cardiac event monitor. You want to reschedule your device coaching appointment with Riley Stone from 08:00 to 15:00 on 2025-12-17 because the later time works better with your schedule and aligns with the need to address a sync issue shown in your telemetry data (zero usage on 2025-12-14). Later, you would like to cancel your cardiology follow-up appointment with Dr. Bryan Bryant at 09:00 on the same day to avoid overlap. After that, you would like to book a future cardiology follow-up with another provider, preferring someone with availability during morning or early afternoon hours on weekdays for continuity in managing your atrial fibrillation and cholesterol.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_469'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_146', 'new_date': '2025-12-17', 'new_time': '15:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_079'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, with email joshua.wagner@tracer-health.org, who uses a cardiac event monitor (CARDIA_tracer_469) for atrial fibrillation management. You want to review the recent upload history of your device for the past week because you noticed some missed data syncs, particularly on 2025-12-14 when no data was uploaded. You would like to reschedule your device coaching appointment (APPT_tracer_146) with Riley Stone from 2025-12-17 at 08:00 to the next day, 2025-12-18 at 09:00, because it better fits your updated schedule and the time is available. After that, you want to cancel your cardiology follow-up appointment (APPT_tracer_079) with Dr. Bryant on 2025-12-17 at 09:00 due to a planned travel conflict. Later, you would like to see which cardiology providers are currently available for rebooking a follow-up, so you can select a new appointment that aligns with your return and ongoing care needs.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed', 'limit': 1}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_469'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_146', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_079'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='dustin.weber@tracer-health.org',
        instruction='You are Dustin Weber, authenticated via dustin.weber@tracer-health.org, and you want to review the details of your upcoming device coaching appointment on December 17, 2025, at 8:00 AM with Robert Wright, focusing on connectivity issues with your Philips Trilogy Ventilator, because you experienced a missed telemetry upload and want to ensure proper device usage. You also want access to the associated medical record documenting the telemetry compliance review, which notes a partial non-compliance pattern with one missing upload and one below-threshold night, so you can understand the clinical assessment and plan for improving adherence.\n\nUse dustin.weber@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_148'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_148'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks, authenticated via scott.sparks@tracer-health.org, managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to reschedule your device coaching appointment with Joseph Robertson, the device coaching nurse, from its current time to next day at 10:00 because it conflicts with your morning schedule. After that, you would like to cancel your medication review appointment with Dr. Hiroko Saito, the cardiology specialist, because you prefer to address medication costs first through alternative suppliers. Before canceling, you want to review cost-saving options for Atorvastatin, such as lower-priced alternatives like Lipistal from Sunrise Biotech in India, to discuss affordability. You also want provider details for Dr. Saito to understand her expertise in cardiology and potential for future consultations.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_162', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_177'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_saito_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction="You are Laurie Carson, a patient with Type 1 Diabetes and Hypothyroidism, managing your care and medication costs. You want to identify the most affordable suppliers for your Insulin Lispro prescription to reduce out-of-pocket expenses, with Bengal EndoCare in India offering the lowest price. You would like to reschedule your follow-up appointment with Dr. Tami Robinson to Monday, 2025-12-22 at 13:00, because it better fits your schedule and aligns with your provider's availability. Later, you plan to cancel your other scheduled follow-up with Dr. Caleb Turner and would like to retain his provider details—including his contact information and specialty—for potential future reference.\n\nUse laurie.carson@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_169', 'new_date': '2025-12-22', 'new_time': '13:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_082'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'caleb_turner_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, authenticated via shawn.carter@tracer-health.org, and you want to reschedule your cardiology consultation with Dr. Kayla Guzman from 2025-12-17 to 2025-12-18 at 10:00 because it better fits your schedule. Later, you would like to cancel your device coaching appointment with Anthony Moran on 2025-12-17 due to resolved technical issues. You also want to confirm there are no harmful interactions between Bupropion and your current cardiac medications (Warfarin, Atorvastatin) because you plan to start the new antidepressant. After that, you prefer to update your Warfarin prescription in record REC_tracer_122 to use the more affordable supplier VedaRx Labs (brand Vedarin, $4.28) to reduce long-term medication costs, even though it is based in India, because cost is a priority for ongoing management.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_127', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_130'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'kayla_guzman_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Bupropion', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_122', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, authenticated via edward.rice@tracer-health.org, and you want to reschedule your cardiology follow-up appointment with Dr. Brandi Dixon from December 17 to Friday, December 19, 2025, at 11:00, because it better fits your schedule. Later, you would like to discuss starting Zolpidem for sleep support, and you prefer to confirm medication safety in advance; based on your current regimen of Warfarin and Atorvastatin, you are reassured that there are no high-risk interactions with Zolpidem.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_078', 'new_date': '2025-12-19', 'new_time': '11:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brandi_dixon_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction='You are Matthew Smith, a patient with atrial fibrillation and hyperlipidemia managed with Warfarin and Atorvastatin, and your email is matthew.smith@tracer-health.org. You want to reschedule your upcoming cardiology follow-up appointment with Dr. Robert Smith from December 17 to December 18 at 10:00 because it better fits your schedule. After that, you would like a drug interaction check for Sertraline, which you are considering for anxiety, against your current medications due to safety concerns. The interaction check reveals a high-severity interaction between Sertraline and Warfarin, so you prefer to hold the next Warfarin dose, monitor your INR, and seek urgent clinical guidance before starting Sertraline.\n\nUse matthew.smith@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_083', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold, with email kevin.arnold@tracer-health.org, managing atrial fibrillation and hyperlipidemia on Warfarin and Atorvastatin. You want to review the suppliers for Warfarin and Atorvastatin, which are both provided by VedaRx Labs under the preferred brands Vedarin and Atorveeda, because you are considering cost and adherence optimization. You would like to explore your current regimen and the optimized options, including the Cost-Synchronized Generic Fill and Adherence Packaging Option, to reduce monthly costs and support routine. You want to verify that adding Zolpidem is safe, and you are reassured that the interaction with Bupropion is low-risk, so you plan to proceed with monitoring for insomnia or agitation. You prefer to consult with Dr. Brandi Dixon, a cardiology specialist with 20 years of experience, for continuity of care. You need to cancel your follow-up appointment APPT_tracer_080 because you are consolidating visits. You also want to reschedule your specialist consultation APPT_tracer_120 from 2025-12-17 at 10:00 to 2025-12-18 at 09:00, which aligns with your schedule and is available in the morning. You expect no telemetry data upload for 2025-05-15 and will address this gap during your consultation.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_489', 'date': '2025-05-15'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brandi_dixon_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin', 'Bupropion']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_080'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_arnold_tracer_0001'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_120', 'new_date': '2025-12-18', 'new_time': '09:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jeffery.duran@tracer-health.org',
        instruction="You are Jeffery Duran, a patient with COPD and obstructive sleep apnea, who uses the email jeffery.duran@tracer-health.org for telehealth communication. You want to reschedule your device coaching appointment with William Benson, a respiratory therapist and registered nurse, from the original date of 2025-12-17 to the next day, 2025-12-18, at 09:00, because this time aligns with your availability and fits within William Benson's confirmed schedule. You prefer this time as it maintains continuity with your current provider and supports consistent device usage coaching. After rescheduling, you would like to receive confirmation of the updated appointment details, including the new date, time, and virtual meeting link, to ensure the change was processed correctly.\n\nUse jeffery.duran@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'william_benson_device_coaching_tracer_0001'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_172', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_172'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='adrian.reese@tracer-health.org',
        instruction="You are Adrian Reese, a patient with COPD and obstructive sleep apnea, managing medication costs and currently scheduled for a telehealth visit. You want to confirm the availability of your primary care provider, Dr. Howard McCarthy, for your upcoming appointment because you have concerns about your current medication regimen and its affordability. You would like to reschedule your existing appointment from Wednesday to the next day, Thursday, at 14:00, because it better fits your daily routine. You prefer this new time as it aligns with your schedule and remains within Dr. McCarthy's available hours for that day.\n\nUse adrian.reese@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'howard_mccarthy_primary_care_tracer_0001'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_095', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_095'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='tammy.carr@tracer-health.org',
        instruction="You are Tammy Carr, and you want to confirm the details of your upcoming medication review appointment with Dr. Charles Lewis, including the date, time, and telehealth link, because you plan to join the visit remotely and want to ensure everything is set. You prefer the appointment to remain on the next day in the morning, as currently scheduled, because it aligns with your availability. You also want to review Dr. Charles Lewis's credentials, including his specialty in Primary Care, experience, and contact information, because you value knowing your provider's background ahead of the visit. You would like to have his email and phone number available in case you need to reach out before the appointment. You prefer to pay the standard copay for the visit using your insurance, as previously authorized, because it simplifies billing.\n\nUse tammy.carr@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_180'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'charles_lewis_primary_care_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='patrick.rangel@tracer-health.org',
        instruction='You are Patrick Rangel, and your email is patrick.rangel@tracer-health.org. You want to review the details of your upcoming specialist consultation regarding the potential interaction between Bupropion and Zolpidem because you have concerns about medication safety. You would also like to learn more about your provider, Dr. Robert Smith, because he is a cardiologist with 15 years of experience who speaks both English and Spanish, which supports your preference for clear communication in your preferred languages.\n\nUse patrick.rangel@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_124'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='elena.morales9921@westcare.org',
        instruction='You are Elena Morales, a patient with focal epilepsy and generalized anxiety disorder, and your email is elena.morales9921@westcare.org. You want to explore more affordable suppliers for your Aspirin EC medication to reduce out-of-pocket costs, and you would like a note added to your medical record REC015 confirming this cost-saving review. You also want to cancel your scheduled psychology follow-up appointment with Dr. Kendra Hartwell (APPT034) because it conflicts with your current schedule. Later, you would like to schedule a new neurology specialist consultation with Dr. John Hopkins on the next available Monday, specifically at 09:30, to discuss your upcoming telemetry preparation, as this time works better for your availability and aligns with your care coordination needs.\n\nUse elena.morales9921@westcare.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Aspirin EC'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC015', 'note': 'Patient reviewing supplier options for cost savings'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT034'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'elena_morales_9921', 'provider_id': 'john_hopkins_neurology_tracer_0001', 'date': '2025-07-28', 'time': '09:30', 'appointment_type': 'specialist_consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, authenticated via shawn.zuniga@tracer-health.org, with atrial fibrillation and hyperlipidemia, currently on Warfarin and Atorvastatin. You want to report that your assigned cardiac monitor, CARDIA_tracer_493, failed to upload data on January 16, 2026, and request a follow-up on the device connectivity issue because consistent rhythm surveillance is critical for your condition. Additionally, you accidentally took Sertraline and would like a drug interaction analysis performed, which has revealed a high-severity interaction with Warfarin; therefore, you prefer immediate clinical guidance and instruction to hold your next Warfarin dose while INR is monitored, due to the elevated bleeding risk from the interaction.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_493', 'date': '2026-01-16'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction="You are Yumi Tanaka, a patient with atrial fibrillation, hypertension, and generalized anxiety disorder, preparing for an ablation procedure and seeking to optimize medication costs. You want to explore lower-cost suppliers for Sertraline because you are looking to reduce prescription expenses. You prefer Triveni Pharma as the supplier, offering the medication under the brand name Setrina at $4.55, due to its lower cost. You would like to check for potential drug interactions between Sertraline and your current medications—Warfarin, Aspirin EC, Metoprolol Succinate, and Sertraline—because of safety concerns, especially given your anticoagulation therapy. After confirming the interaction risk, you want to update your prescription in medical record REC012 to reflect Triveni Pharma as the new supplier and add a note stating 'Patient requested supplier change for Sertraline to lower cost option' to maintain accurate documentation. Later, you would like to review your upcoming cardiology consultation scheduled with Dr. Margaret Thompson, a senior cardiologist with 25 years of experience, because you want to discuss your treatment plan and ensure continuity of care. You prefer to access the appointment details, provider information, and the associated medical record (REC013) to be fully informed ahead of the visit. Subsequently, you want to check telemetry data for device PHILIP_tracer_452 from January 15 to January 17, 2026, to verify usage compliance, but no uploads were found in that period. Finally, you would like a list of shipped telemetry devices to understand inventory status, particularly for ventilator models like the Philips Trilogy, possibly for future assignment or tracking purposes.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Aspirin EC', 'Metoprolol Succinate', 'Sertraline']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC012', 'note': 'Patient requested supplier change for Sertraline to lower cost option.'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT030'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'PHILIP_tracer_452', 'start_date': '2026-01-15', 'end_date': '2026-01-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.barnes@tracer-health.org',
        instruction='You are Sarah Barnes, a patient with hypertension and type 2 diabetes, and your email is sarah.barnes@tracer-health.org. You want to cancel your scheduled medication review appointment on 2025-12-17 because you have decided to pursue a routine checkup instead. You would like to schedule a new routine checkup with Dr. Debra Nunez, a primary care provider, on the next day, 2025-12-18, at 09:00, because it aligns better with your updated care needs and schedule. After that, you would like a list of all available primary care providers for future reference, so you can have more options for ongoing care management.\n\nUse sarah.barnes@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_176'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'sarah_barnes_tracer_0001', 'provider_id': 'debra_nunez_primary_care_tracer_0001', 'date': '2025-12-18', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='adam.alexander@tracer-health.org',
        instruction='You are Adam Alexander (adam.alexander@tracer-health.org) and you want to cancel your upcoming cardiology consultation currently scheduled for 2025-12-17 at 10:00. You would like to reschedule the consultation with the same provider, Dr. Juan Fitzgerald, on 2025-12-24 at 14:00 because it better fits your availability. You prefer the appointment to be conducted virtually and covered using your Aetna insurance, as previously authorized.\n\nUse adam.alexander@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_113'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'adam_alexander_tracer_0001', 'provider_id': 'juan_fitzgerald_cardiology_tracer_0001', 'date': '2025-12-24', 'time': '14:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are a patient managing atrial fibrillation and hyperlipidemia via telehealth with a cardiac event monitor for rhythm surveillance. You want to review recent telemetry uploads from the device assigned to you for the dates 2025-12-15 to 2025-12-16 because you are checking for any irregularities. Later, you want to cancel your appointment APPT_tracer_081 and reschedule your other appointment APPT_tracer_121 with Dr. Bryant to Friday, December 19, 2025 at 11:00 AM because of a scheduling conflict. After that, you want to check for potential drug interactions with Zolpidem before starting it for sleep support, and then update the supplier for your Warfarin prescription to VedaRx Labs (brand name Vedarin) for more affordable long-term therapy.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_485', 'start_date': '2025-12-15', 'end_date': '2025-12-16'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_081'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_121', 'new_date': '2025-12-19', 'new_time': '11:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_121'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin', 'Bupropion']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_132', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction='You are Matthew Smith (matthew.smith@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia managing care through telehealth. You want to explore cardiology providers, specifically Dr. Bryan Bryant, because you are considering continuity with a cardiologist for ongoing management. You would like to check for drug interactions between your current medications (Warfarin and Atorvastatin) and the proposed switch to Atorveeda (Atorvastatin from VedaRx Labs) to ensure safety, and you prefer to update your Atorvastatin prescription to be supplied by VedaRx Labs under the brand Atorveeda because it offers cost savings without compromising efficacy. Later, you want to reschedule your cardiology follow-up appointment with Dr. Christine Bailey (currently on 2025-12-19) to a more convenient time, and you also want to cancel your device coaching session with Robert Wright scheduled for 2025-12-17 because you have resolved syncing issues independently. After that, you would like to confirm that your cardiac event monitor (CARDIA_tracer_481) recorded 0 hours of usage on 2025-12-14 because you forgot to sync it that day and want to verify no data was captured.\n\nUse matthew.smith@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'bryan_bryant_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_134', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_171', 'new_date': '2025-12-19', 'new_time': '10:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_170'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_171'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_481', 'date': '2025-12-14'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, a patient with atrial fibrillation and hyperlipidemia managing your care through telehealth, and your email is joshua.wagner@tracer-health.org. You want to consult with a cardiology provider about your condition, because you are proactively managing your heart health. You would like to check for drug interactions between Zolpidem and your current medications, Warfarin and Atorvastatin, because you are considering Zolpidem for sleep support. Since no interactions were found, you prefer to update the supplier for your Atorvastatin prescription to VedaRx Labs (brand=Atorveeda, price_usd=4.05) to reduce monthly medication costs. You also want to reschedule your device coaching appointment with Joseph Robertson from its current date to 2025-12-18 at 09:00, because it better fits your schedule. After that, you would like to cancel your follow-up appointment with Dr. Bryan Bryant, because you have resolved the concerns that prompted the visit. Finally, you want to review the telemetry upload for your cardiac monitor on 2025-12-14, because it shows 0 hours of usage, which explains a gap in your recorded data.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'thomas_may_cardiology_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_130', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_146', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_079'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_146'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_469', 'date': '2025-12-14'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='david.martinez@email.com',
        instruction='You are David Martinez, patient david_martinez_5678, with email david.martinez@email.com, managing anxiety and seasonal allergies. You want to check for drug interactions after accidentally taking an extra dose of Sertraline, because you are concerned about potential side effects when combining it with your current medication Claritin. You would like to switch your Sertraline prescription supplier to Triveni Pharma (brand name Setrina) at $4.55, because it reduces your out-of-pocket cost. You prefer this change to be documented in medical record REC001, which contains your current Sertraline 75mg prescription. Later, you also want to confirm that the telemetry device NS-EEG-220 has a missing upload on 2025-07-04, for system audit and compliance purposes.\n\nUse david.martinez@email.com for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'missing_overdue'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'NS-EEG-220', 'date': '2025-07-04'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Claritin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC001', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'david_martinez_5678'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC001', 'note': 'Patient requested supplier change for Sertraline to Triveni Pharma (Setrina) at $4.55'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and using a cardiac event monitor. You want to address a recent accidental intake of Sertraline, which has a high-severity interaction with Warfarin, requiring urgent clinical review and possible dose adjustment. You also want to verify that your telemetry device CARDIA_tracer_469 has a missing upload on January 12, 2026, so it can be resolved promptly. You would like to update your Warfarin prescription in medical record REC_tracer_130 to reflect a switch to the lower-cost supplier VedaRx Labs with the brand name Vedarin at $4.28 per tablet, as this aligns with your goal of reducing medication costs. You prefer this change because it supports long-term affordability without compromising therapeutic efficacy. You also want to add a note in the same medical record discussing the cost-saving benefits of this switch, to ensure the clinical rationale is documented. Finally, you would like to confirm the updated prescription details in your medical record to ensure accuracy and continuity of care.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed', 'limit': 1}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_469', 'date': '2026-01-12'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_130', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_130', 'note': 'Discussed cost-saving options for Warfarin prescription and patient elected to switch to VedaRx Labs (Vedarin) at $4.28 per unit.'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_130'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez, a patient with Type 1 Diabetes and Hypothyroidism, and your email is amanda.martinez@tracer-health.org. You want to cancel your device coaching appointment scheduled for 2025-12-17 at 09:00 because of a scheduling conflict. You would like to check for potential drug interactions between Sertraline and your current medications, Insulin Lispro and Levothyroxine, to ensure safety before starting a new treatment. After confirming no interactions, you prefer to update the prescription for Insulin Lispro to the more affordable supplier Bengal EndoCare (brand name SwiftLis) to reduce out-of-pocket costs. Later, you would like to review the telemetry data from your continuous glucose monitor (device CONTIN_tracer_464) for December 17, 2025, to assess your usage patterns and compliance ahead of your endocrinology follow-up.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_136'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_063', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_464', 'date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='cynthia.scott@tracer-health.org',
        instruction='You are Cynthia Scott (cynthia.scott@tracer-health.org), a patient managing hypertension and type 2 diabetes, who wants to cancel your medication review appointment scheduled for next day at 08:00 because you no longer need it. You would like to see the details of your primary care provider, Dr. Nicholas Salinas, to better understand his background and availability. You prefer to schedule a new specialist consultation with endocrinologist Dr. Hector Lane on the following Friday at 09:00 because it aligns with your need for specialized diabetes and hypertension management. You also want to review a list of available endocrinology providers to explore additional care options. Later, you would like to reschedule your second medication review appointment to Thursday at 09:00 for better time convenience. After that, you would like to review the details of this rescheduled appointment and access the medical record from the original visit to confirm the recommended switch to a lower-cost supplier for Lisinopril.\n\nUse cynthia.scott@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_183'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'nicholas_salinas_primary_care_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'cynthia_scott_tracer_0001', 'provider_id': 'hector_lane_endocrinology_tracer_0001', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_098', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_098'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_098'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, and your email is yumi.tanaka7410@pacificcare.org. You want to explore lower-cost suppliers for Aspirin EC because you are concerned about medication expenses, and you would like to consider options such as CardiShield 81 from Mumbai Care Labs at $1.85 or HeartTabs EC from Heartland Remedies in the USA. Later, you also want a clinical review of a potential high-severity interaction between Warfarin and Sertraline in your current regimen because it may require adjusting your treatment plan for safety, even though both medications are already part of your routine.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Aspirin EC'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Aspirin EC', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='carlos.mendez4521@email.com',
        instruction='You are Carlos Mendez, with email carlos.mendez4521@email.com, managing chronic pain and anxiety. You want to explore available supplier options for your Sertraline medication to evaluate cost and access alternatives. You also need a safety check because you may have double-dosed on Sertraline, and you are currently taking Ibuprofen and Acetaminophen; you would like confirmation that combining these medications does not pose high-risk interaction concerns, which has been confirmed as safe.\n\nUse carlos.mendez4521@email.com for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Ibuprofen', 'Acetaminophen']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='norma.ruiz@tracer-health.org',
        instruction="You are Norma Ruiz, and your email is norma.ruiz@tracer-health.org. You want to cancel your scheduled device coaching appointment on 2025-12-17 at 09:00 because the technical issues with your glucose monitor have been resolved. Later, you would like to schedule a new endocrinology follow-up appointment with Dr. Debra Castro on 2025-12-22 at 13:00 to discuss long-term glucose control, as this time aligns with your availability and the provider's schedule.\n\nUse norma.ruiz@tracer-health.org for authentication.",
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_160'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'norma_ruiz_tracer_0001', 'provider_id': 'debra_castro_endocrinology_tracer_0001', 'date': '2025-12-22', 'time': '13:00', 'appointment_type': 'follow_up'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='margaret.clarke@tracer-health.org',
        instruction='You are Margaret Clarke (margaret.clarke@tracer-health.org), a patient with Focal Epilepsy and Generalized Anxiety Disorder currently taking Levetiracetam and Sertraline. You want to schedule a psychiatry consultation with Dr. Mark Brown on Thursday, July 10th at 13:00 because it aligns with your availability and his afternoon schedule. You also want to review your telemetry data from your Wearable EEG device (WEARAB_tracer_475) and confirm that a data upload was missing on June 1st, so the care team can assess potential gaps in monitoring. Additionally, you would like to confirm that continuing Sertraline in your current regimen does not pose any high-risk interactions with Levetiracetam, as safety and stability in your mental health and seizure management are important to you.\n\nUse margaret.clarke@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Psychiatry'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'mark_brown_psychiatry_tracer_0001'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'margaret_clarke_tracer_0001', 'provider_id': 'mark_brown_psychiatry_tracer_0001', 'date': '2025-07-10', 'time': '13:00', 'appointment_type': 'consultation'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_475', 'date': '2025-06-01'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='laurie.carson@tracer-health.org',
        instruction='You are Laurie Carson (laurie.carson@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, managing your condition with Insulin Lispro and Levothyroxine. You want to review telemetry uploads for your Continuous Glucose Monitor (CONTIN_tracer_480) from December 14 to 16, 2025, because you noticed gaps in data and want to ensure consistent monitoring. You would like to confirm there are no drug interactions between Insulin Lispro and your current medications (Levothyroxine and Insulin Lispro) before making any changes. After confirmation, you prefer to update the prescription for Insulin Lispro in medical record REC_tracer_071 to the lower-cost supplier Bengal EndoCare, using the brand SwiftLis at $19.20, to reduce financial burden while maintaining treatment safety. You also want to cancel your scheduled endocrinology follow-up appointment (APPT_tracer_169) with Dr. Tami Robinson on December 19, 2025, at 10:00 due to a scheduling conflict. Subsequently, you would like to reschedule the follow-up with Dr. Tami Robinson to a new time on the same day, preferably at 13:00, as it aligns with your availability and minimizes disruption to your care plan. If that time is not available, you would accept an alternative slot on Monday, December 22, at either 09:00 or 10:00. You also need the details of your original appointment and medical records reviewed to ensure all information is up to date.\n\nUse laurie.carson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_480', 'date': '2025-12-14'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_071', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_169'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'laurie_carson_tracer_0001', 'provider_id': 'tami_robinson_endocrinology_tracer_0001', 'date': '2025-12-19', 'time': '10:00', 'appointment_type': 'follow_up'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_169'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'laurie_carson_tracer_0001'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'tami_robinson_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez (amanda.martinez@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism managing care via telehealth. You want to review your glucose monitor telemetry data from December 17, 2025, because you are tracking your device usage patterns. After confirming no drug interactions between Insulin Lispro and Levothyroxine, you would like to update your prescription for Insulin Lispro in record REC_tracer_063 to use the more affordable supplier Lotus Rapid Therapeutics (brand: Lispry) priced at $19.75, because you are seeking to reduce medication costs. You also want to cancel your existing follow-up appointment with Dr. Amy Young (APPT_tracer_075) because you prefer continuity with another provider. Later, you would like to schedule a new follow-up appointment with Dr. Ashley Schneider on December 19, 2025, at 13:00, because it aligns with your schedule and the provider specializes in endocrinology. You also need the details of your upcoming medication review appointment (APPT_tracer_182) and your medical records for personal review. Finally, you would like to receive provider details for Dr. Ashley Schneider to learn more about her background and availability.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_464', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_063', 'medication': 'Insulin Lispro', 'supplier_company': 'Lotus Rapid Therapeutics', 'brand_name': 'Lispry', 'price_usd': 19.75}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_075'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'amanda_martinez_tracer_0001', 'provider_id': 'ashley_schneider_endocrinology_tracer_0001', 'date': '2025-12-19', 'time': '13:00', 'appointment_type': 'follow_up'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_182'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'ashley_schneider_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, a patient with atrial fibrillation and hyperlipidemia, and your email is shawn.carter@tracer-health.org. You want to reschedule your cardiology follow-up appointment with Dr. Owen Shaw from December 19, 2025 to December 22, 2025 at 11:00 because it better fits your schedule. You would also like to review the details of this appointment and access your medical record REC_tracer_122, which contains the regimen review note discussing cost and adherence optimization for your warfarin and atorvastatin prescriptions, because you want to understand your medication plan and potential savings. Later, you will check the upload history of your cardiac event monitor (CARDIA_tracer_461) to ensure you are complying with your monitoring protocol, because consistent usage is important for accurate cardiac rhythm assessment. After that, you would like to see a list of available telemetry devices in inventory to understand what alternatives exist, because you are interested in the broader options for remote monitoring.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_131'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_122'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_131', 'new_date': '2025-12-22', 'new_time': '11:00'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_461'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction="You are Joshua Wagner (joshua.wagner@tracer-health.org), and you want to reschedule your cardiology follow-up appointment with Dr. Thomas May from December 19 to December 22 at 14:00 because it better fits your schedule and aligns with the provider's availability on Mondays. Later, you would like to cancel your medication review appointment with Dr. Kayla Guzman on December 17, as you have already reviewed the associated medical record discussing cost and adherence optimization. After that, you want to explore available suppliers for Atorvastatin to evaluate cost-effective options from different manufacturers. Finally, you would like to review your full regimen alternatives, including the cost-synchronized generic fill and adherence-focused packaging options, to make informed decisions about long-term treatment convenience, cost efficiency, and medication adherence.\n\nUse joshua.wagner@tracer-health.org for authentication.",
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_147', 'new_date': '2025-12-22', 'new_time': '14:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_186'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_147'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_130'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction="You are Yumi Tanaka, patient with email yumi.tanaka7410@pacificcare.org, managing atrial fibrillation and anxiety. You want to switch the supplier for your Sertraline prescription in record REC012 to Gujarat MindCare (brand: Serenem) at $4.65 because it is a lower-cost option, and you would like a note added to the record stating 'Patient requested supplier update for cost savings.' You also want to reschedule your cardiology consultation with Dr. Thompson from its current time to 09:00 on the next day, as it better fits your schedule. Later, you would like to book a new specialist consultation with Dr. Brandi Dixon on the following Wednesday at 10:00 for continued cardiology care. After that, you would like to cancel your scheduled care coordination appointment, as it is no longer needed. You prefer to keep all future appointments scheduled via telehealth and will use your preferred payment method for copays.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC012', 'note': 'Patient requested supplier update for cost savings.'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT030', 'new_date': '2025-05-20', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC012'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'yumi_tanaka_7410', 'provider_id': 'brandi_dixon_cardiology_tracer_0001', 'date': '2025-05-21', 'time': '10:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT031'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'yumi_tanaka_7410', 'status_filter': 'scheduled'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jordan.patel@tracer-health.org',
        instruction='You are Jordan Patel (jordan.patel@tracer-health.org), a patient with COPD and Obstructive Sleep Apnea managing Fluticasone Inhaler and Montelukast. You want to update the supplier for your Fluticasone Inhaler to IndiAir Therapeutics, brand name Fluticair, because it offers a lower-cost option at $7.40 while being safe and equivalent, with no interactions between your current medications. You also want to add a note to your medical record about this supplier change for cost-saving purposes. Later, you would like to reschedule your device coaching appointment with Riley Stone from its current date to next Tuesday at 09:00, because it better fits your schedule. After that, you would like to book a follow-up appointment with a primary care provider on the following Monday at 14:00 for ongoing respiratory management. Finally, you would like to cancel your redundant appointment to avoid confusion and streamline your care plan.\n\nUse jordan.patel@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Fluticasone Inhaler'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Fluticasone Inhaler', 'current_medications': ['Fluticasone Inhaler', 'Montelukast']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_033', 'medication': 'Fluticasone Inhaler', 'supplier_company': 'IndiAir Therapeutics', 'brand_name': 'Fluticair', 'price_usd': 7.4}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_033', 'note': 'Patient requested supplier update for Fluticasone Inhaler to lower cost option.'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_068', 'new_date': '2025-12-02', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_068'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_033'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'riley_stone_device_coaching_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'jordan_patel_tracer_0001', 'provider_id': 'dr_chen_primary_care', 'date': '2025-12-08', 'time': '14:00', 'appointment_type': 'follow_up'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_069'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'jordan_patel_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond, a patient with atrial fibrillation and hyperlipidemia, and your email is kevin.bond@tracer-health.org. You want to cancel your scheduled cardiology follow-up with Dr. Hiroko Saito on 2025-12-17 at 07:30 because it no longer fits your schedule. You also want to reschedule your medication review appointment with Dr. Megan Cook from 2025-12-17 at 09:00 to 2025-12-19 at 10:00 because the later date works better for your availability. Later, you would like to explore available cardiology providers and specifically request detailed information about Dr. Robert Smith due to his experience and multilingual capabilities. After that, you would like to identify cost-effective suppliers for your Warfarin prescription to reduce out-of-pocket costs, and you also want to confirm that continuing Atorvastatin alongside Warfarin is safe, which is supported by the absence of high-risk interactions in your regimen.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_081'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_188', 'new_date': '2025-12-19', 'new_time': '10:00'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond (kevin.bond@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia managing Warfarin and Atorvastatin. You want to review your current medication regimen options to understand cost and adherence alternatives, because you are interested in optimizing your treatment plan. You would like to explore supplier options for Atorvastatin to identify potential cost savings, as your current supplier is VedaRx Labs but lower-cost alternatives may be available. You need to see the details of your upcoming cardiology follow-up appointment with Dr. Saito on 2025-12-17 at 07:30, because you want to confirm the virtual visit details. Later, you would like to schedule a new routine cardiology checkup with Dr. Smith on the next day at 09:00, because he is a cardiology specialist and the time works well with your schedule.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_081'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-22', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='megan.jones@tracer-health.org',
        instruction='You are Megan Jones, a patient managing hypertension and type 2 diabetes, with email megan.jones@tracer-health.org. You want to explore more affordable suppliers for your Lisinopril prescription because cost is a concern, and you prefer to stay on effective treatment without financial strain. You would like to review your current medication regimen options to understand potential cost-saving or adherence-improving alternatives. You need the details of your upcoming medication review appointment on December 17, 2025, because it directly addresses your concerns about medication affordability. After that, you would like to schedule a new specialist consultation with Dr. Robert Smith, a cardiologist, on December 18, 2025, at 3:00 PM, because it aligns with your schedule and addresses ongoing cardiovascular concerns.\n\nUse megan.jones@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'megan_jones_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_106'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'megan_jones_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-18', 'time': '15:00', 'appointment_type': 'specialist_consultation'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez, a patient with Type 1 Diabetes and Hypothyroidism, and your email is amanda.martinez@tracer-health.org. You want to reschedule your device coaching appointment with Coach Riley, a telemetry nurse coach fluent in Spanish, from the morning to the late morning on the same day, because it better fits your schedule. Later, you would like to cancel your follow-up appointment with Dr. Young, as you prefer continuity with a provider you have not yet seen. After that, you would like to schedule a new follow-up appointment with Dr. Tami Robinson, an endocrinologist, on the next Friday at 13:00, because the time works well for your routine. You also want to review the upload history for your Continuous Glucose Monitor (CONTIN_tracer_464) to ensure your data is being recorded accurately and to monitor your compliance with daily usage.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_136', 'new_date': '2025-12-17', 'new_time': '11:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'coach_riley_telemetry'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_136'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_136'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_075'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'amanda_martinez_tracer_0001', 'provider_id': 'tami_robinson_endocrinology_tracer_0001', 'date': '2025-12-19', 'time': '13:00', 'appointment_type': 'follow_up'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_464'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='amanda.martinez@tracer-health.org',
        instruction='You are Amanda Martinez (amanda.martinez@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to reschedule your upcoming endocrinology follow-up appointment with Dr. Amy Young from 2025-12-17 at 09:00 to 2025-12-18 at 10:00 due to a scheduling conflict, because the new time better fits your daily routine. You also want to review the provider details for Dr. Amy Young and the appointment details for your follow-up, as well as access your recent medical records related to diabetes management for personal reference. Later, you would like to cancel your medication review appointment with Dr. John Wise on 2025-12-17 at 14:00 due to redundancy with your endocrinology care, and instead schedule a new follow-up appointment with Dr. Ashley Schneider, another endocrinologist, on 2025-12-19 at 13:00, because she is available and you prefer continuity with endocrinology-led care; you want this appointment billed to your insurance and classified as a follow-up visit. After that, you would like to review the recent usage data from your Continuous Glucose Monitor (device ID: CONTIN_tracer_464) for the week of 2025-12-11 to 2025-12-17, noting a gap in uploads on 2025-12-14, to assess your adherence and identify patterns in device use.\n\nUse amanda.martinez@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_075', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'amy_young_endocrinology_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_075'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'amanda_martinez_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_075'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_096'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'amanda_martinez_tracer_0001', 'provider_id': 'ashley_schneider_endocrinology_tracer_0001', 'date': '2025-12-19', 'time': '13:00', 'appointment_type': 'follow_up', 'bill_insurance': True}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_464'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='toni.miller@tracer-health.org',
        instruction='You are Toni Miller (toni.miller@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to safely consider adding Sertraline for mood support because no high-risk interactions were found with your current medications (Insulin Lispro and Levothyroxine). You would like to review your current and optimized regimen options to understand cost and adherence improvements, and you prefer to explore more affordable suppliers for Insulin Lispro to reduce out-of-pocket expenses, although your current supplier (Bengal EndoCare) is already the lowest-cost option. Later, you want to verify the data upload status of your assigned Continuous Glucose Monitor (device ID: CONTIN_tracer_492) because no telemetry data was recorded on December 17, 2025, and you are concerned about device syncing and compliance tracking.\n\nUse toni.miller@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_125', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'toni_miller_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CONTIN_tracer_492', 'date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction="You are Kevin Bond, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, who recently started Sertraline for anxiety. You want to check for potential drug interactions because you're concerned about safety, and the interaction check revealed a high-severity risk between Sertraline and Warfarin that requires urgent clinical review. You would like to update the supplier for your Warfarin prescription in record REC_tracer_132 to VedaRx Labs (brand: Vedarin) at $4.28 to reduce medication costs, as this aligns with your current regimen and optimized options. You also want to review your regimen alternatives to explore further cost and adherence improvements, particularly the Cost-Synchronized Generic Fill and Adherence Packaging Option, both of which maintain your current medications while offering financial and usability benefits. Additionally, you noticed your cardiac event monitor (CARDIA_tracer_485) did not upload data on 2025-12-17 and would like confirmation of the missing telemetry for that date, as it may affect clinical interpretation of your cardiac rhythm during that period.\n\nUse kevin.bond@tracer-health.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_132', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_485', 'date': '2025-12-17'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='audrey.horton@tracer-health.org',
        instruction='You are Audrey Horton (audrey.horton@tracer-health.org), a patient managing focal epilepsy and generalized anxiety disorder with Levetiracetam and Sertraline. You want to review the details of your upcoming neurology follow-up appointment with Dr. John Hopkins, including the associated medical record from your recent device coaching session, because you are preparing for your visit and want to understand your recent telemetry compliance patterns. You also want to confirm there are no drug interactions between Sertraline and your current medications, as you are ensuring your regimen is safe. You prefer to schedule a new follow-up appointment with Dr. Stacey Howell on next Monday (2025-12-22) at 14:30 via telehealth for continuity of care. Later, you would like to reschedule your existing neurology appointment with Dr. John Hopkins to the same day (next Monday) at 09:30, because it better fits your morning routine and allows both visits to be completed in one day.\n\nUse audrey.horton@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_175'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_119'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'john_hopkins_neurology_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'WEARAB_tracer_483', 'date': '2025-12-13'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Levetiracetam', 'Sertraline']}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'audrey_horton_tracer_0001', 'provider_id': 'stacey_howell_neurology_tracer_0001', 'date': '2025-12-22', 'time': '14:30', 'appointment_type': 'follow_up'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_175', 'new_date': '2025-12-22', 'new_time': '09:30'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, a cardiology patient managing atrial fibrillation and hyperlipidemia via telehealth, and you want to schedule a new routine checkup with Dr. Megan Cook, a cardiology provider, on the next available day that aligns with your schedule, specifically preferring the day after your current appointment (originally set for tomorrow), because it allows continuity in your care coordination. You also want to reschedule your existing medication review with Dr. Thompson from tomorrow morning to the following day at 09:00, because it better fits your availability and avoids conflict with other health monitoring tasks. Later, you would like to address a gap in your cardiac event monitor data, as the device failed to upload on the same day as your original appointment, which raises concern about potential missed arrhythmia events. After that, you need clinical guidance regarding an accidental dose of Sertraline, which is not part of your regimen, because a drug interaction check indicates a high-severity interaction with your current Warfarin therapy, requiring urgent review and possible dose adjustment.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_zuniga_tracer_0001', 'provider_id': 'megan_cook_cardiology_tracer_0001', 'date': '2025-12-18', 'time': '10:00', 'appointment_type': 'routine_checkup'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_179', 'new_date': '2025-12-19', 'new_time': '09:00'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_493', 'date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction="You are Shawn Carter, authenticated via shawn.carter@tracer-health.org, and you want to schedule a new cardiology consultation with Dr. Luis Sims on 2024-02-12 at 10:00 because it aligns with your availability and the provider's schedule. Later, you would like to reschedule your existing appointment with Dr. Kayla Guzman from 2025-12-17 to 2024-02-14 at 14:00 for better coordination of care. You also want to review the telemetry data from your cardiac event monitor (CARDIA_tracer_461) for December 11, 2025, because it shows 6.8 hours of recorded usage that may be relevant to your cardiac health. Additionally, you would like to check for drug interactions before starting Sertraline, and the results indicate a high-severity interaction with Warfarin, so you prefer to hold Warfarin and seek urgent clinical guidance before proceeding.\n\nUse shawn.carter@tracer-health.org for authentication.",
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_carter_tracer_0001', 'provider_id': 'luis_sims_cardiology_tracer_0001', 'date': '2024-02-12', 'time': '10:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_127', 'new_date': '2024-02-14', 'new_time': '14:00'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_461', 'date': '2025-12-11'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='norma.ruiz@tracer-health.org',
        instruction='You are Norma Ruiz, a patient with Type 1 Diabetes and Hypothyroidism, managing your telehealth care via norma.ruiz@tracer-health.org. You want to reschedule your endocrinology follow-up currently with Dr. Debra Castro on December 17, 2025, to instead occur on the next day, December 18, 2025, at 10:00 AM with Dr. Michael Moss, because you prefer continuity with him for your diabetes management. Later, you will review the upload history for your Continuous Glucose Monitor (device ID CONTIN_tracer_476) from December 14 to December 16, 2025, to assess recent usage gaps showing zero hours on the 14th and partial compliance on the following days. After that, you would like to cancel your duplicate device coaching session scheduled for December 17, 2025, at 09:00 AM, as it overlaps with your original endocrinology appointment and is no longer needed. You also prefer to continue care with Dr. Michael Moss, an endocrinologist with 16 years of experience, due to established treatment continuity and schedule alignment.\n\nUse norma.ruiz@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_090'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_090', 'new_date': '2025-12-18', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'norma_ruiz_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_476', 'start_date': '2025-12-14', 'end_date': '2025-12-16'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_160'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'michael_moss_endocrinology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='megan.jones@tracer-health.org',
        instruction='You are Megan Jones, a patient managing hypertension and type 2 diabetes, and your email is megan.jones@tracer-health.org. You want to reschedule your medication review appointment with Dr. Garcia from the original date to the next day at 14:00 because it better fits your schedule. Later, you will cancel your overlapping follow-up appointment on the same original day to avoid conflicts. You also prefer to update your Lisinopril prescription to use the lower-cost supplier Mumbai Cardio Pharma, brand name Lisipril-M, priced at 2.8 USD, because it reduces financial strain without compromising safety, as confirmed by drug interaction checks with your current medications.\n\nUse megan.jones@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_106', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'megan_jones_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_084'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_073', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
        ],
        outputs=[],
    ),

    Task(
        user_id='avery.morgan@tracer-health.org',
        instruction='You are a patient with email avery.morgan@tracer-health.org who wants to cancel your scheduled follow-up telehealth appointment with Dr. Smith on 2025-11-30 at 16:00 due to a personal scheduling conflict. After cancellation, you would like to review the full appointment details, including the virtual meeting link and the $45.00 copay amount, to retain this information for your personal records before the visit is officially cancelled.\n\nUse avery.morgan@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_061'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_061'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks (scott.sparks@tracer-health.org), a patient on Warfarin and Atorvastatin for atrial fibrillation and hyperlipidemia, who recently started taking Zolpidem for sleep. You want to confirm there are no harmful interactions between Zolpidem and your current medications, because you are concerned about safety with your cardiac and anticoagulation regimen. You would like your medical record (REC_tracer_121) updated to reflect a change in your Atorvastatin prescription to use Sunrise Biotech (Lipistal) at $4.15, because it reduces your monthly medication cost. You prefer to explore other available suppliers for Atorvastatin to further optimize cost, and you want to review your current and optimized regimen options to evaluate pill burden and cost-efficiency. You also need your telemetry data from device CARDIA_tracer_477 on 2025-12-15 reviewed, because you want to confirm your compliance with monitoring. Later, you decide to cancel your upcoming medication review appointment (APPT_tracer_177) because you no longer need the consultation. After that, you would like a list of available providers and detailed information about Dr. Saito, because she authored your medical record and you may want to consult her in the future.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_121', 'medication': 'Atorvastatin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Lipistal', 'price_usd': 4.15}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_121'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_477', 'date': '2025-12-15'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_177'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_saito_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction='You are Diane Robinson (diane.robinson@tracer-health.org), a patient with Type 1 Diabetes and Hypothyroidism, who wants to ensure the new formulation of Insulin Lispro she started does not interact with her current medications, particularly Levothyroxine, because of safety concerns. You would like to update your prescription supplier for Insulin Lispro to Bengal EndoCare (brand SwiftLis) as it is the lowest-cost option and aligns with your financial needs. Later, you want to cancel your scheduled follow-up appointment with Dr. Schneider (APPT_tracer_077) because you have overlapping visits on the same day. You also need the details of your medication review appointment with Dr. Caleb Turner (APPT_tracer_184) to understand its purpose and timing. After that, you would like a full list of all your scheduled appointments to better coordinate your care plan and avoid duplication.\n\nUse diane.robinson@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_066', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_066'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_184'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_077'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'diane_robinson_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='molly.hill@tracer-health.org',
        instruction='You are Molly Hill, a patient with Type 1 Diabetes and Hypothyroidism, managing medication costs and device adherence. You want to confirm there are no drug interactions between Insulin Lispro and your current medications, which include Levothyroxine, because you are concerned about safety when making changes. After confirmation, you would like to update the supplier for Insulin Lispro in your medical record to Triveni Pharma, brand name Setrina, priced at $4.55, because it is a lower-cost option that fits your budget. You also want to cancel your scheduled medication review appointment (APPT_tracer_111) because you are addressing the cost concerns directly. After that, you would like to review your remaining scheduled appointments, which include device coaching and endocrinology follow-ups, to ensure continuity of care.\n\nUse molly.hill@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_078', 'medication': 'Insulin Lispro', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_078'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_111'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_111'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'molly_hill_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.shelton@tracer-health.org',
        instruction='You are Kevin Shelton (kevin.shelton@tracer-health.org), a patient with COPD and Obstructive Sleep Apnea. You want to reschedule your pulmonology follow-up appointment with Dr. Brian Kim from Friday, December 19th at 10:00 to Monday, December 22nd at 09:00 because it better fits your schedule. Later, you would like to cancel your device coaching session with Chelsea Buck on December 17th, as you have resolved the connectivity issues independently. After that, you would like to schedule a new routine checkup with your primary care provider, Dr. Lisa Chen, on Tuesday, December 23rd at 15:00, and you prefer to bill this visit to your insurance.\n\nUse kevin.shelton@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_157', 'new_date': '2025-12-22', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_157'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_shelton_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brian_kim_pulmonology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_156'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kevin_shelton_tracer_0001', 'provider_id': 'dr_chen_primary_care', 'date': '2025-12-23', 'time': '15:00', 'appointment_type': 'routine_checkup', 'bill_insurance': True}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga (shawn.zuniga@tracer-health.org), a patient with atrial fibrillation and hyperlipidemia managing care via telehealth. You want to schedule a new routine checkup with Dr. Margaret Thompson, a cardiologist, on Friday, 2025-12-19 at 09:00 because it aligns with your availability and fits within her open schedule. After that, you need to cancel your scheduled medication review appointment on 2025-12-17 at 08:00 with Dr. Thompson because you prefer to address those concerns during the new checkup. You also want to reschedule your specialist consultation with Dr. Luis Sims, another cardiologist, from 2025-12-17 at 14:00 to 2025-12-18 at 14:00 because the new time better fits your daily routine. Additionally, you would like to review suppliers for Atorvastatin to evaluate cost and sourcing options, particularly noting VedaRx Labs as your current supplier offering Atorveeda at a competitive price. You are interested in your current and optimized regimen options, especially the Cost-Synchronized Generic Fill and Adherence Packaging Option, both of which maintain clinical effectiveness while supporting cost efficiency and pill burden management. Finally, you want to review recent telemetry data from your cardiac event monitor (device ID: CARDIA_tracer_493) and have noticed no uploads in the past week, so you would like to investigate potential connectivity or usage issues to ensure continuous monitoring for your cardiac condition.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_zuniga_tracer_0001', 'provider_id': 'dr_thompson_cardiology', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_179'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_179'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_128', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'shawn_zuniga_tracer_0001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'shawn_zuniga_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_493', 'start_date': '2025-12-12', 'end_date': '2025-12-18'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, email sarah.johnson@email.com, managing hypertension and type 2 diabetes. You want to reschedule your routine checkup with your primary care provider, Dr. Carlos Garcia, from its current date to the next day at 10:00 AM because it works better with your schedule. Later, you will cancel your cardiology follow-up appointment with Dr. Robert Smith scheduled for March 18, 2025, due to a personal scheduling conflict. After that, you would like to explore available providers in both cardiology and primary care for future care options, preferring providers who are board-certified and offer flexible appointment times.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT001'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT001', 'new_date': '2024-01-16', 'new_time': '10:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'sarah_johnson_1234'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT012'}),
            Action(name='list_available_providers', kwargs={}),
        ],
        outputs=[],
    ),

    Task(
        user_id='heather.mccoy@tracer-health.org',
        instruction='You are Heather McCoy (heather.mccoy@tracer-health.org) and you want to first review the details of your scheduled care coordination appointment because it conflicts with a family commitment. You would like to schedule a new routine checkup with Dr. Riley Stone, a device coaching specialist, on Friday (next day) at 09:00 because it works better with your schedule. After successfully booking the new appointment, you want to cancel your original appointment APPT_tracer_211 to avoid confusion and ensure care continuity.\n\nUse heather.mccoy@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_211'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'heather_mccoy_tracer_0001', 'provider_id': 'riley_stone_device_coaching_tracer_0001', 'date': '2025-12-19', 'time': '09:00', 'appointment_type': 'routine_checkup'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_211'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='jin.park7284@northsoundsleep.org',
        instruction='You are Jin Park, a patient with complex sleep apnea and depression, and your email is jin.park7284@northsoundsleep.org. You want to first review the details of your scheduled specialist consultation with Dr. Anjali Kumar on June 14, 2025, at 09:30, which is for an insurance compliance audit and requires ventilator adherence review. After reviewing, you would like to cancel this appointment because you prefer continuity with your pulmonology follow-up care. Later, you want to schedule a new follow-up appointment with Dr. Sophia Everett, a pulmonologist, on Monday, June 16, 2025, at 08:00, because it better aligns with your availability and care plan. You prefer this time as it is confirmed available and fits your morning routine.\n\nUse jin.park7284@northsoundsleep.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT043'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'jin_park_7284', 'provider_id': 'sophia_everett_pulmonology_tracer_0001', 'date': '2025-06-16', 'time': '08:00', 'appointment_type': 'follow_up'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT043'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yesenia.wiley@tracer-health.org',
        instruction="You are Yesenia Wiley, a caregiver managing family health coordination, and your email is yesenia.wiley@tracer-health.org. You want to cancel your scheduled family consultation with Dr. Daniel Pitts, a pediatrician fluent in Spanish, because of a scheduling conflict. You would like to review all your current appointments to better coordinate care, especially regarding your son Zachary's developmental concerns. You also want to see the details of your appointment with Dr. Pitts to understand the visit context and confirm the chief complaint about family care coordination. You need to access your medical record REC_tracer_149, which contains the care plan from your coordination session, because it outlines next steps for Zachary's evaluation and household tracking. You prefer to have a complete list of your medical records to ensure nothing is missing. After canceling the appointment, you would like to explore available providers for a future visit to address ongoing developmental concerns for your son.\n\nUse yesenia.wiley@tracer-health.org for authentication.",
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_218'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'yesenia_wiley_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_218'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_149'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'yesenia_wiley_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter, authenticated with email shawn.carter@tracer-health.org, managing atrial fibrillation and hyperlipidemia. You want to cancel your scheduled cardiology consultation appointment with Dr. Kayla Guzman because you have decided not to proceed with the visit. You also want to review the details of that appointment to understand the original purpose of the visit. Additionally, you would like to access the medical record (REC_tracer_094) associated with this appointment to review the interaction assessment between Bupropion and Zolpidem. Finally, you want a complete list of all your medical records for personal review and continuity of care.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_127'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_127'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_094'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'shawn_carter_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='noah.ito@email.com',
        instruction='You are Noah Ito, a patient with hypertension managed on Amlodipine, and your email is noah.ito@email.com. You want to cancel your follow-up appointment with Dr. Garcia scheduled for 2025-04-08 because you no longer need the visit. You would like to reschedule your cardiology consultation with Dr. Smith from 2025-04-09 to 2025-04-16 at 15:00 because it works better with your schedule. Later, you want to establish care with a new primary care provider, Dr. Charles Barajas, and schedule a routine checkup on 2025-04-10 at 09:00 because you prefer continuity with a dedicated primary physician. You prefer to use your Aetna insurance for billing the new visit.\n\nUse noah.ito@email.com for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT014'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT015', 'new_date': '2025-04-16', 'new_time': '15:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT014'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Primary Care'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'noah_ito_98187', 'provider_id': 'charles_barajas_primary_care_tracer_0001', 'date': '2025-04-10', 'time': '09:00', 'appointment_type': 'routine_checkup', 'bill_insurance': True}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction='You are Shawn Carter (shawn.carter@tracer-health.org), managing atrial fibrillation and hyperlipidemia, and you want to cancel your scheduled consultation with Dr. Guzman on 2025-12-17 at 14:00 because it no longer aligns with your current care priorities. You would like to reschedule your medication review appointment with Dr. Smith from 2025-12-17 to 2025-12-24 at 15:00 because the new time works better with your availability. After that, you would like to schedule a new routine checkup with Dr. Luis Sims on 2025-12-18 at 10:00 because you prefer consistent cardiac monitoring with a trusted provider, and you prefer to use your insurance for billing.\n\nUse shawn.carter@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_127'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_178', 'new_date': '2025-12-24', 'new_time': '15:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_178'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'shawn_carter_tracer_0001', 'provider_id': 'luis_sims_cardiology_tracer_0001', 'date': '2025-12-18', 'time': '10:00', 'appointment_type': 'routine_checkup', 'bill_insurance': True}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='tammy.carr@tracer-health.org',
        instruction='You are Tammy Carr, a patient with hypertension and type 2 diabetes managing your medications and appointments. You are interested in exploring cost-saving options for your Lisinopril medication, as lower-cost suppliers are available internationally. You want to reschedule your medication review appointment with Dr. Charles Lewis to Thursday, December 18, 2025, at 09:00 because it better fits your schedule. Later, you would like to consult a cardiologist for specialized care related to your cardiovascular health. You prefer to schedule a new appointment with Dr. Owen Shaw, a cardiology specialist, on Friday, December 19, 2025, at 11:00, as it aligns with your availability and care needs. After that, you would like to receive the details of your new appointment with Dr. Shaw for your records. You also want a list of all your medical records to support your personal health tracking and continuity of care.\n\nUse tammy.carr@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_180', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'tammy_carr_tracer_0001', 'provider_id': 'owen_shaw_cardiology_tracer_0001', 'date': '2025-12-19', 'time': '11:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_180'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'tammy_carr_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='nadia.abbasi@tracer-health.org',
        instruction='You are Nadia Abbasi, a patient with hypertension and type 2 diabetes, and your email is nadia.abbasi@tracer-health.org. You want to explore more affordable medication suppliers for Lisinopril because of cost concerns, and you prefer to reschedule your medication review appointment with Dr. Garcia to Friday, December 5th at 10:00 AM because it better fits your schedule. Later, you would like to schedule a new specialist consultation with Dr. Caleb Turner, an endocrinologist, on Monday, December 8th at 9:00 AM to improve management of your chronic conditions. After that, you would like to review the updated details of your rescheduled appointment with Dr. Garcia and obtain a complete list of your medical records to stay informed about your care plan and medication history.\n\nUse nadia.abbasi@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_063', 'new_date': '2025-12-05', 'new_time': '10:00'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'nadia_abbasi_tracer_0001', 'provider_id': 'caleb_turner_endocrinology_tracer_0001', 'date': '2025-12-08', 'time': '09:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_063'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'nadia_abbasi_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction="You are Kevin Bond (kevin.bond@tracer-health.org), a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to review the details of your scheduled specialist consultation with Dr. Bryan Bryant on 2025-12-17 at 10:00, which was intended to discuss a potential medication interaction, and you also want a full list of your upcoming appointments to understand your visit schedule. After reviewing, you would like to identify cost-effective suppliers for Atorvastatin to reduce medication expenses, with Sunrise Biotech in India offering the lowest price at $4.15 per unit, and you want a drug interaction check between Warfarin and your current regimen to ensure safety, which shows no high-risk interactions. Later, you decide to cancel the specialist consultation on 2025-12-17 at 10:00 because it is no longer needed, and you would like to reschedule your follow-up appointment with Dr. Hiroko Saito to Thursday, 2025-12-18 at 08:00, as it aligns better with your availability and fits within Dr. Saito's bookable hours.\n\nUse kevin.bond@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_121'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'status_filter': 'scheduled'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_121'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_081', 'new_date': '2025-12-18', 'new_time': '08:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='megan.jones@tracer-health.org',
        instruction='You are Megan Jones, a patient managing hypertension and type 2 diabetes through telehealth, with email megan.jones@tracer-health.org. You want to review the details of your appointment APPT_tracer_106 and see all your upcoming scheduled appointments because you are organizing your care plan. You are concerned about the cost of your Lisinopril medication, so you would like to explore lower-cost suppliers and have already confirmed that Mumbai Cardio Pharma offers the lowest price at $2.80 per month under the brand name Lisipril-M. You also want to ensure safety by confirming there are no drug interactions between Lisinopril and your current medication Metformin, which has been verified as safe. Later, you decide to cancel your medication review appointment APPT_tracer_106 due to redundancy with other scheduled visits. After that, you would like to reschedule your follow-up appointment APPT_tracer_084 from 2025-12-17 at 09:00 to the next day, 2025-12-18 at 10:00, because it better fits your schedule and the time is available with your provider.\n\nUse megan.jones@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_106'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'megan_jones_tracer_0001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_106'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_084', 'new_date': '2025-12-18', 'new_time': '10:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.smith@tracer-health.org',
        instruction='You are Matthew Smith (matthew.smith@tracer-health.org), a 44-year-old male managing atrial fibrillation and hyperlipidemia via telehealth. You want to confirm a missed telemetry upload on 2025-06-03 for your cardiac event monitor (CARDIA_tracer_481) because you forgot to sync it and are concerned about rhythm surveillance gaps. You also want to check for drug interactions because you took Sertraline and are on Warfarin, which poses a high-risk interaction requiring urgent review. You prefer to update your Atorvastatin prescription in medical record REC_tracer_134 to use Sunrise Biotech (Lipistal) at $4.15 to reduce monthly medication costs while maintaining efficacy. You would like to reschedule your follow-up appointment (APPT_tracer_171) with Dr. Christine Bailey from 2025-12-19 to 2025-12-22 at 14:00 because it better fits your schedule and the time is available. After that, you want to list all your appointments to review your care plan, then cancel your specialist consultation (APPT_tracer_122) on 2025-12-17 because it is no longer needed. You also want to review the details of APPT_tracer_171 for confirmation. Finally, you would like to list all suppliers for Atorvastatin to compare cost options, review your full regimen options to assess cost and adherence improvements, retrieve your medical record REC_tracer_134 for personal reference, and list all your medical records to ensure you have a complete understanding of your ongoing care.\n\nUse matthew.smith@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed', 'limit': 1}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_481', 'date': '2025-06-03'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_134', 'medication': 'Atorvastatin', 'supplier_company': 'Sunrise Biotech', 'brand_name': 'Lipistal', 'price_usd': 4.15}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_171', 'new_date': '2025-12-22', 'new_time': '14:00'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'matthew_smith_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_122'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_171'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'matthew_smith_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_134'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'matthew_smith_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='adrian.reese@tracer-health.org',
        instruction='You are Adrian Reese, a patient with COPD and obstructive sleep apnea, managing medication cost concerns for Fluticasone and Montelukast. You want to cancel your scheduled telehealth medication review appointment on 2025-12-17 because you are unable to attend. After that, you would like to access the details of that appointment to understand the purpose and context of the visit. You also want to retrieve your medical record from that appointment, which contains updated supplier recommendations for more affordable versions of your medications. Finally, you would like a complete list of all your medical records for personal review and record-keeping.\n\nUse adrian.reese@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_095'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_095'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_062'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'adrian_reese_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='gary.barry@tracer-health.org',
        instruction='You are Gary Barry, a patient with COPD and Obstructive Sleep Apnea, and your email is gary.barry@tracer-health.org. You want to cancel your scheduled device coaching appointment on 2025-12-17 at 09:00 because you resolved the ventilator connectivity issue independently. After that, you would like to review the details of that appointment to confirm the cancellation. You also want to retrieve the medical record associated with that visit to understand the clinical summary of your recent telemetry compliance. Finally, you would like to see a list of all your medical records for personal tracking and record-keeping.\n\nUse gary.barry@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_164'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_164'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_114'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'gary_barry_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, a patient with atrial fibrillation and hyperlipidemia, preparing for an upcoming medication review. You want to confirm that your appointment is scheduled with Dr. Margaret Thompson, a cardiologist with 25 years of experience, because she is your trusted provider for cardiac care. You would like to verify the details of your scheduled telehealth visit on December 17, 2025, at 8:00 AM, as it addresses your concerns about medication cost and daily pill burden. You also prefer to ensure that your cardiac event monitor (CARDIA_tracer_493) remains assigned to you for ongoing rhythm surveillance, and you would like to check its upload history, noting that no recent telemetry data has been uploaded, so you can follow up on device usage compliance.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_179'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_493'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.carter@tracer-health.org',
        instruction="You are Shawn Carter, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and your email is shawn.carter@tracer-health.org. You want to check for drug interactions before starting Zolpidem for sleep, because you are concerned about safety with your current regimen; no significant interactions were found. You would like to update your Warfarin prescription in medical record REC_tracer_122 to switch to the lower-cost supplier VedaRx Labs (brand: Vedarin) at $4.28, because you are seeking cost savings, and you want the record note updated to state 'Patient requested supplier change for cost savings'. You also want to review the details of your scheduled device coaching appointment on 2025-12-17 at 08:00, because you are considering canceling it. Later, you would like to confirm that your cardiac monitor (CARDIA_tracer_461) is properly assigned to you and review its telemetry upload history for the past week, because you want to ensure compliance; however, no uploads were found in that period, indicating a potential sync issue to address.\n\nUse shawn.carter@tracer-health.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_122', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_122', 'note': 'Patient requested supplier change for cost savings'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_130'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_130'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_461'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction="You are yumi.tanaka7410@pacificcare.org. You want to accomplish these, in order:\n1. Hi, my email is yumi.tanaka7410@pacificcare.org. I accidentally took a dose of Sertraline twice today. Can you check if this interacts with my current medications: Warfarin, Sertraline, Aspirin EC, and Metoprolol Succinate? Also, I'd like to update the supplier for my Sertraline prescription in record REC012 to a cheaper option. Can you update it to Gujarat MindCare, brand Serenem, at $4.65? Also, can you add a note to record REC012 saying 'Patient requested supplier change for cost savings.'? Also, I need to see the details of my appointment APPT031 and cancel it.\n2. Please list all available telemetry devices and then check the upload history for device NS-EEG-226 from 2025-06-01 to 2025-06-03.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.",
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Sertraline', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Gujarat MindCare', 'brand_name': 'Serenem', 'price_usd': 4.65}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC012', 'note': 'Patient requested supplier change for cost savings.'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT031'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT031'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'available'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'NS-EEG-226', 'start_date': '2025-06-01', 'end_date': '2025-06-03'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='robin.rodriguez@tracer-health.org',
        instruction='You are Robin Rodriguez, a patient with hypertension and type 2 diabetes, who is preparing for an upcoming follow-up appointment and wants to review all relevant health information ahead of the visit. You want to see the details of your scheduled appointment with Dr. Chen because you need to confirm the time, virtual meeting link, and purpose of the visit. You also want a list of all your medical records to ensure nothing is missing from your history. You would like to retrieve the full content of your medical record REC_tracer_060 because it contains the clinical note from your upcoming follow-up and helps you prepare for the discussion. Finally, you want to list all your appointments again to confirm your current schedule and ensure no other visits are pending.\n\nUse robin.rodriguez@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_093'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'robin_rodriguez_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_060'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'robin_rodriguez_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks, authenticated via scott.sparks@tracer-health.org, with atrial fibrillation and hyperlipidemia, currently managing multiple telehealth appointments and medication considerations. You want to review the details of your upcoming specialist consultation (APPT_tracer_126) because it involves discussing potential interactions between Bupropion and Zolpidem. You also want to access all your medical records to ensure comprehensive care coordination, particularly retrieving the interaction review note (REC_tracer_093) which contains the clinical assessment about starting Zolpidem while on Bupropion. Finally, you want to review all your scheduled appointments to understand the sequence and timing of your care activities, especially since you have multiple visits on the same day (device coaching, medication review, and specialist consultation) and a follow-up appointment two days later.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_126'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_093'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, a patient with atrial fibrillation and hyperlipidemia, and your email is edward.rice@tracer-health.org. You want to reschedule your upcoming cardiology follow-up appointment with Dr. Brandi Dixon from its current date to next Monday at 10:00, because it better fits your schedule. You also want to explore more affordable options for your Atorvastatin prescription to reduce monthly costs. After confirming that switching to Atorveeda from VedaRx Labs in India is safe with your current medications—Warfarin, Atorvastatin, Bupropion, and Zolpidem—you would like to update your medical record to reflect this new supplier and brand, as it offers the lowest price at $4.05 without introducing any high-risk drug interactions.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_078', 'new_date': '2025-12-22', 'new_time': '10:00'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin', 'Bupropion', 'Zolpidem']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_129', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction='You are Diane Robinson, email diane.robinson@tracer-health.org, and you want to reschedule your endocrinology medication review appointment with Dr. Caleb Turner from its current date to Friday, December 19, 2025, at 13:00, because it better fits your schedule. You would like to check cost-effective alternatives for your Insulin Lispro prescription. After confirming no drug interactions with your current medications, you prefer to update your prescription in your medical record to use the supplier Bengal EndoCare with the brand name SwiftLis, as it offers a lower cost while maintaining regimen safety and effectiveness.\n\nUse diane.robinson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_184', 'new_date': '2025-12-19', 'new_time': '13:00'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_128', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
        ],
        outputs=[],
    ),

    Task(
        user_id='valerie.mullen@tracer-health.org',
        instruction='You are Valerie Mullen, authenticated with email valerie.mullen@tracer-health.org. You want to reschedule your pediatrics consultation with Dr. Bruce King from its original date to Monday, 2025-12-22 at 10:30 because it better fits your schedule. Later, you will cancel your care coordination appointment with Dr. Brandon Page on 2025-12-18 because you no longer need it. You also want to review the details of Dr. Brandon Page, the appointment you are canceling, and its associated medical record to stay informed about your care plan. Additionally, you would like to list your upcoming appointments and check available providers for care coordination, then schedule a new follow-up appointment with Dr. Brandon Page on 2025-12-19 at 11:00 to continue your care.\n\nUse valerie.mullen@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_214', 'new_date': '2025-12-22', 'new_time': '10:30'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'valerie_mullen_tracer_0001'}),
            Action(name='list_available_providers', kwargs={'specialty': 'Care Coordination'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'valerie_mullen_tracer_0001', 'provider_id': 'brandon_page_care_coordination_tracer_0001', 'date': '2025-12-19', 'time': '11:00', 'appointment_type': 'follow_up'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_215'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brandon_page_care_coordination_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_215'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_215'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='toni.miller@tracer-health.org',
        instruction='You are Toni Miller, a patient with Type 1 Diabetes and Hypothyroidism, and you want to start Sertraline for anxiety management because there are no high-risk interactions with your current medications (Insulin Lispro and Levothyroxine). You would like to update the supplier for your Insulin Lispro prescription in record REC_tracer_125 to Bengal EndoCare, brand SwiftLis, because it aligns with your current and optimized regimen options for cost reduction. You also want to review your overall regimen options to explore further optimization for cost and adherence, particularly the Cost-Synchronized Generic Fill and Adherence Packaging Option. Additionally, you would like to check your recent telemetry data from your Continuous Glucose Monitor (device ID: CONTIN_tracer_492) because no recent uploads are found, and you want to assess your compliance and glucose trends.\n\nUse toni.miller@tracer-health.org for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_125', 'medication': 'Insulin Lispro', 'supplier_company': 'Bengal EndoCare', 'brand_name': 'SwiftLis', 'price_usd': 19.2}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'toni_miller_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_492'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='sarah.johnson@email.com',
        instruction='You are Sarah Johnson, a patient with hypertension and type 2 diabetes, and your email is sarah.johnson@email.com. You want to reschedule your routine checkup with your primary care provider, Dr. Carlos Garcia, from the original date to Sunday, February 11th at 9:30 AM because it better fits your current availability. You would like confirmation that the new appointment time is confirmed, that the telehealth meeting link remains accessible, and that the copay of $25 remains applicable as per your Blue Cross Blue Shield plan.\n\nUse sarah.johnson@email.com for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT001'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT001', 'new_date': '2024-02-11', 'new_time': '09:30'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.arnold@tracer-health.org',
        instruction='You are Kevin Arnold (kevin.arnold@tracer-health.org), a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin. You want to explore cost-effective options for Atorvastatin by reviewing available suppliers, because you are interested in potential savings. You also want a system-based drug interaction check between Atorvastatin and your current medications (Warfarin, Atorvastatin) to confirm safety, because you want to ensure your regimen remains stable. Later, you would like to reschedule your cardiology follow-up appointment with Dr. Christine Bailey from its current date to next Monday at 11:00, because it works better with your schedule and the time is available.\n\nUse kevin.arnold@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Atorvastatin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_080', 'new_date': '2025-12-22', 'new_time': '11:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='richard.nelson@tracer-health.org',
        instruction='You are Richard Nelson, authenticated at richard.nelson@tracer-health.org, and you want to review available cardiologists to understand your care options, with a specific interest in learning more about your current provider, Dr. Margaret Thompson, due to her expertise in cardiology and long-standing care relationship. You would like to confirm that starting Zolpidem is safe given your current medications, Warfarin and Atorvastatin, because you experienced sleep difficulties and want to avoid adverse interactions—this has been confirmed as low-risk. Later, you want to cancel your follow-up appointment on Wednesday, December 17th at 9:00 AM because of a scheduling conflict. After that, you would like to reschedule your specialist consultation (originally on the same day at 10:00 AM) to Thursday, December 18th at 8:00 AM because it better fits your availability, and you prefer morning appointments for consistency with your routine. Finally, you want confirmation of the updated appointment details to ensure the change was processed correctly.\n\nUse richard.nelson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_092'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_125', 'new_date': '2025-12-18', 'new_time': '08:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_125'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='carlos.mendez4521@email.com',
        instruction='You are Carlos Mendez (carlos.mendez4521@email.com), a patient managing chronic pain and anxiety, who wants to cancel your scheduled follow-up appointment with Dr. Chen on 2025-10-14 at 09:00 and reschedule it to a new appointment with the same provider on 2025-10-21 at 10:00 because it better fits your availability. You would like to check for potential drug interactions between a new supplement and your current medications—Sertraline, Ibuprofen, and Acetaminophen—before starting it, to ensure safety. You prefer to update your Sertraline prescription in medical record REC027 to source the medication from Harmony Labs (Sertrawin) at $4.75 for cost savings, and you want this change documented in your record for audit purposes.\n\nUse carlos.mendez4521@email.com for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT056'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT056'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'carlos_mendez_4521', 'provider_id': 'dr_chen_primary_care', 'date': '2025-10-21', 'time': '10:00', 'appointment_type': 'follow_up'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Ibuprofen', 'Acetaminophen']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC027', 'medication': 'Sertraline', 'supplier_company': 'Harmony Labs', 'brand_name': 'Sertrawin', 'price_usd': 4.75}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'carlos_mendez_4521'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC027', 'note': 'Patient requested supplier change for Sertraline to Harmony Labs (Sertrawin) for cost savings. Price updated from previous supplier to $4.75.'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC027'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='megan.jones@tracer-health.org',
        instruction="You are Megan Jones (megan.jones@tracer-health.org), a patient with hypertension and type 2 diabetes, who wants to cancel your scheduled medication review appointment with Dr. Garcia on December 17, 2025, because you prefer to discuss your medication costs on a later date. After that, you would like to schedule a new medication review appointment with Dr. Garcia for Friday, December 26, 2025, at 14:00, because it aligns with your availability and Dr. Garcia's schedule. You are considering switching your Lisinopril supplier to reduce costs and have confirmed there are no interactions with your current medications. You prefer to update your prescription in your medical record to use Hyderabad Heart Meds (brand: Sinopril-H) for Lisinopril, as it is a cost-effective option. You also want to add a note to your medical record stating 'Patient discussed alternative suppliers for Lisinopril and chose Hyderabad Heart Meds for next refill,' to document your decision for future reference.\n\nUse megan.jones@tracer-health.org for authentication.",
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_106'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_106'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'megan_jones_tracer_0001', 'provider_id': 'dr_garcia_primary', 'date': '2025-12-26', 'time': '14:00', 'appointment_type': 'medication_review'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_073', 'medication': 'Lisinopril', 'supplier_company': 'Hyderabad Heart Meds', 'brand_name': 'Sinopril-H', 'price_usd': 3.1}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'megan_jones_tracer_0001'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_073', 'note': 'Patient discussed alternative suppliers for Lisinopril and chose Hyderabad Heart Meds for next refill.'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_073'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='matthew.osborne@tracer-health.org',
        instruction='You are Matthew Osborne (matthew.osborne@tracer-health.org) and you want to reschedule your pulmonology follow-up appointment with Dr. Amelia Quinn from December 19 to December 22 at 09:00 because it better fits your schedule. You would like confirmation that Dr. Quinn is a pulmonology specialist with availability on Mondays, which aligns with your preferred reschedule day. Later, you will want to ensure data integrity by reviewing the upload history for the cardiac event monitor CARDIA_tracer_510, noting that no uploads have been recorded yet. After that, you would like to know what telemetry devices are currently available in the system, particularly looking for cardiac event monitors or other devices that may be needed for ongoing monitoring.\n\nUse matthew.osborne@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_141'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_141', 'new_date': '2025-12-22', 'new_time': '09:00'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='get_provider_details', kwargs={'provider_id': 'amelia_quinn_pulmonology_tracer_0001'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_510'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='gary.barry@tracer-health.org',
        instruction='You are Gary Barry (gary.barry@tracer-health.org), a patient with COPD and Obstructive Sleep Apnea, and you want to cancel your device coaching appointment with Kimberly Rosales because it conflicts with your schedule. You would like to reschedule your follow-up appointment with Dr. Anjali Kumar, your pulmonologist, to next Thursday at 08:00 because it works better for your morning routine. After that, you want to explore more affordable options for your Fluticasone Inhaler to reduce out-of-pocket costs while maintaining treatment effectiveness. You prefer to switch the supplier for your Fluticasone Inhaler to IndiAir Therapeutics, using the brand name Fluticair, as it offers a reliable and cost-effective alternative. You also want to confirm your ventilator usage compliance, which you verified was 7 hours on 2025-12-17, to ensure your treatment plan remains on track.\n\nUse gary.barry@tracer-health.org for authentication.',
        actions=[
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_164'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_165', 'new_date': '2025-12-23', 'new_time': '08:00'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Fluticasone Inhaler'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'gary_barry_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'PHILIP_tracer_478', 'start_date': '2025-12-17', 'end_date': '2025-12-17'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Fluticasone Inhaler', 'current_medications': ['Fluticasone Inhaler', 'Montelukast']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_068', 'medication': 'Fluticasone Inhaler', 'supplier_company': 'IndiAir Therapeutics', 'brand_name': 'Fluticair', 'price_usd': 7.4}),
        ],
        outputs=[],
    ),

    Task(
        user_id='carlos.mendez4521@email.com',
        instruction='You are Carlos Mendez, and you want to verify the safety of a new Sertraline formulation because you recently read about it and are already taking Sertraline, Ibuprofen, and Acetaminophen; the check confirms no high-risk interactions. You would like to update your Sertraline prescription to use Triveni Pharma as the supplier, choosing the brand Setrina for its lower cost. After that, you prefer to reschedule your follow-up appointment with Dr. Chen from Tuesday morning to Wednesday morning at 8:00 AM because it aligns better with your work schedule.\n\nUse carlos.mendez4521@email.com for authentication.',
        actions=[
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Sertraline', 'Ibuprofen', 'Acetaminophen']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC027', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT056', 'new_date': '2025-10-15', 'new_time': '08:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, authenticated via joshua.wagner@tracer-health.org, and you want to cancel your scheduled follow-up appointment with Dr. Bryan Bryant on December 17th at 09:00 because of a scheduling conflict. You would like to reschedule your specialist consultation with Dr. Thomas May, originally set for December 17th at 10:00, to December 18th at 11:00 because it better fits your availability and aligns with your need to discuss the potential interaction between Bupropion and the proposed Zolpidem sleep aid. You prefer this new time to allow continuity in managing your atrial fibrillation and sleep-related concerns with your cardiology specialist.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_119'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_119'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'thomas_may_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_079'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_119', 'new_date': '2025-12-18', 'new_time': '11:00'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='megan.jones@tracer-health.org',
        instruction="You are Megan Jones, a patient with hypertension and type 2 diabetes, and your email is megan.jones@tracer-health.org. You want to reschedule your medication review appointment with Dr. Carlos Garcia from 2025-12-17 at 11:00 to 2024-01-22 at 09:00 because it works better for your schedule. Later, you will cancel the original appointment on 2025-12-17 at 11:00 with Dr. Garcia after confirming the new slot is secured. You would like to reduce your medication costs and prefer to switch your Lisinopril prescription to the lowest-cost supplier, Mumbai Cardio Pharma's Lisipril-M at $2.80 per unit, because it is more affordable. Before updating the prescription in your medical record, you want a drug interaction check between Lisinopril and your current medications (Metformin and Lisinopril) to ensure safety, which has confirmed no high-risk interactions.\n\nUse megan.jones@tracer-health.org for authentication.",
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_084', 'new_date': '2024-01-22', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_084'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_106'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_073', 'medication': 'Lisinopril', 'supplier_company': 'Mumbai Cardio Pharma', 'brand_name': 'Lisipril-M', 'price_usd': 2.8}),
        ],
        outputs=[],
    ),

    Task(
        user_id='edward.rice@tracer-health.org',
        instruction='You are Edward Rice, a patient with atrial fibrillation and hyperlipidemia, who wants to reschedule your medication review appointment with Dr. Juan Fitzgerald from the original date to the next available Friday at 10:00, because it better fits your schedule. You also want to review the details of this appointment and your medical records to stay informed about your treatment plan. Later, you would like to see the suppliers for Atorvastatin to evaluate cost and sourcing options, review your optimized regimen alternatives for potential improvements in cost and adherence, and examine the telemetry upload history for your cardiac event monitor to assess your recent device usage and compliance.\n\nUse edward.rice@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_185', 'new_date': '2025-12-19', 'new_time': '10:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_185'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'edward_rice_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_185'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'edward_rice_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_465'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='toni.miller@tracer-health.org',
        instruction='You are Toni Miller, a patient with Type 1 Diabetes and Hypothyroidism, who wants to reschedule your medication review appointment with your endocrinologist Dr. Amy Young from December 17, 2025 at 13:00 to December 18, 2025 at 14:00 because it better fits your schedule. You would like to review your medical records from this appointment to understand your current medication regimen. Later, you want to explore more affordable supplier options for Insulin Lispro, as you are concerned about the cost, and you prefer to consider suppliers with lower prices such as Bengal EndoCare or Lotus Rapid Therapeutics. After that, you would like to review your regimen optimization options to evaluate potential cost and adherence improvements. Finally, you want to verify the data from your Continuous Glucose Monitor (device ID: CONTIN_tracer_492) to ensure it is functioning properly and providing accurate readings for your diabetes management, as no telemetry uploads have been recorded yet.\n\nUse toni.miller@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_181', 'new_date': '2025-12-18', 'new_time': '14:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_181'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'toni_miller_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_181'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'toni_miller_tracer_0001'}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CONTIN_tracer_492'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'shipped'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='rebecca.washington@tracer-health.org',
        instruction='You are Rebecca Washington, a patient with Type 1 Diabetes and Hypothyroidism, and your email is rebecca.washington@tracer-health.org. You want to reschedule your follow-up appointment with your endocrinologist Dr. Lucia Fernandez from 09:00 to 11:30 on the same day (2025-12-17) because of a scheduling conflict. You also want to check for any potential interactions after accidentally taking an extra dose of Insulin Lispro, given that your current medications are Insulin Lispro and Levothyroxine. You would like to receive the details of your appointment APPT_tracer_091, the medical record from that visit, and a list of all your medical records. Later, you would like to book a new routine checkup with Dr. Fernandez on 2025-12-19 at 10:00, because you prefer continuity with your current provider, and after that, you would like to cancel your original appointment APPT_tracer_091.\n\nUse rebecca.washington@tracer-health.org for authentication.',
        actions=[
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_091', 'new_date': '2025-12-17', 'new_time': '11:30'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_fernandez_endocrinology'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Insulin Lispro', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_091'}),
            Action(name='get_medical_record', kwargs={'appointment_id': 'APPT_tracer_091'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'rebecca_washington_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'rebecca_washington_tracer_0001', 'provider_id': 'dr_fernandez_endocrinology', 'date': '2025-12-19', 'time': '10:00', 'appointment_type': 'routine_checkup'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_091'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='michelle.adams@tracer-health.org',
        instruction='You are Michelle Adams, authenticated via michelle.adams@tracer-health.org, and you want to cancel your scheduled medication review appointment with Dr. Nicholas Salinas on December 17, 2025, because of a scheduling conflict. After that, you would like to schedule a new follow-up appointment with Dr. Michael Moss, an endocrinologist, on Monday, December 22, 2025, at 09:00, because it aligns with your preference for care continuity with a specialist in endocrinology and the time works better for your schedule.\n\nUse michelle.adams@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Endocrinology'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'michael_moss_endocrinology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_110'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'michelle_adams_tracer_0001', 'provider_id': 'michael_moss_endocrinology_tracer_0001', 'date': '2025-12-22', 'time': '09:00', 'appointment_type': 'follow_up'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_110'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'michelle_adams_tracer_0001', 'status_filter': 'scheduled'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner, a patient with atrial fibrillation and hyperlipidemia, managing Warfarin and Atorvastatin, and your authenticated email is joshua.wagner@tracer-health.org. You want to schedule a follow-up appointment with your cardiologist, Dr. Robert Smith, on Friday (next day) at 15:00 via telehealth because it aligns with your preferred time and provider availability. Later, you would like to reschedule your existing consultation with Dr. Thomas May about a new sleep aid (Zolpidem) to Friday (next day) at 09:00, as it fits better with your schedule and allows both visits to be on the same day for convenience. You also want to confirm that your cardiac telemetry device has been used consistently, and since there are no missing uploads from the past three days, you are compliant. You would like to verify that adding Zolpidem to your current regimen is safe, and since no drug interactions were found with Warfarin or Atorvastatin, you feel reassured. After that, you prefer to update your Atorvastatin prescription to use VedaRx Labs (brand name Atorveeda) at a lower cost of 4.05 USD per dose, as it reduces your monthly medication expense. Finally, you want to document this supplier preference in your medical record with a note stating you requested pricing information and preferred VedaRx Labs for Atorvastatin, to support cost-effective care and future refill coordination.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='list_available_providers', kwargs={'specialty': 'Cardiology'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'joshua_wagner_tracer_0001', 'provider_id': 'dr_smith_cardiology', 'date': '2025-12-19', 'time': '15:00', 'appointment_type': 'follow_up'}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_119', 'new_date': '2025-12-19', 'new_time': '09:00'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_119'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_smith_cardiology'}),
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed'}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_469', 'date': '2025-12-15'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_130', 'medication': 'Atorvastatin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Atorveeda', 'price_usd': 4.05}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_130'}),
            Action(name='list_medication_suppliers', kwargs={'medication': 'Atorvastatin'}),
            Action(name='update_medical_record_note', kwargs={'record_id': 'REC_tracer_130', 'note': 'Patient requested supplier pricing info and preferred VedaRx Labs for Atorvastatin.'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='joshua.wagner@tracer-health.org',
        instruction='You are Joshua Wagner (joshua.wagner@tracer-health.org) and you want to review the details of your upcoming specialist consultation on December 17, 2025, with Dr. Thomas May, which is scheduled for 10:00 AM and focuses on adding Zolpidem for sleep issues to your current regimen of Warfarin and Atorvastatin. You would like to access all your medical records, particularly the interaction review note (REC_tracer_086) from this appointment, because it contains important information about the safety of combining Zolpidem with your current medications. You also want to investigate the telemetry data from your Cardiac Event Monitor (CARDIA_tracer_469), specifically the zero usage hours recorded on December 14, 2025, because you recall having trouble with the app interface that day and want to ensure no cardiac events were missed. You prefer to confirm that there are no significant drug interactions between Zolpidem and your current medications (Warfarin and Atorvastatin), because you want to proceed safely with the proposed sleep aid under medical supervision.\n\nUse joshua.wagner@tracer-health.org for authentication.',
        actions=[
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_119'}),
            Action(name='list_patient_medical_records', kwargs={'patient_id': 'joshua_wagner_tracer_0001'}),
            Action(name='get_medical_record', kwargs={'record_id': 'REC_tracer_086'}),
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_469', 'date': '2025-12-14'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Zolpidem', 'current_medications': ['Warfarin', 'Atorvastatin']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kevin.bond@tracer-health.org',
        instruction='You are Kevin Bond, a patient managing atrial fibrillation and hyperlipidemia with Warfarin and Atorvastatin, and your email is kevin.bond@tracer-health.org. You want to explore more affordable suppliers for Warfarin to reduce your monthly medication costs, because you are concerned about expenses and adherence during travel. You would like to confirm there are no harmful interactions between Warfarin and your current medications, particularly Atorvastatin, to ensure safety in any regimen change. You prefer to update your Warfarin prescription to be supplied by VedaRx Labs under the brand name Vedarin at $4.28 per tablet, as it is the lowest-cost option without compromising therapeutic equivalence. You also want to review optimized regimen options to further reduce costs and support adherence, especially through coordinated refills or blister packaging. Separately, you need to review the details of your upcoming medication review appointment on 2025-12-17 with Dr. Megan Cook, because it addresses your concerns about cost and pill management. You would like to schedule a new routine follow-up appointment with Dr. Megan Cook, a cardiologist, on the next day at 10:00, because she is familiar with your case and the time works with your schedule. You prefer this visit to be virtual, as your previous appointments have been. You also want to confirm Dr. Cook’s availability and specialty to ensure continuity of care. After that, you would like to cancel your duplicate specialist consultation on the same day at 10:00, because it is no longer needed and conflicts with your updated plan.\n\nUse kevin.bond@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Warfarin'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_132', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'kevin_bond_tracer_0001'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_188'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'kevin_bond_tracer_0001', 'provider_id': 'megan_cook_cardiology_tracer_0001', 'date': '2025-12-18', 'time': '10:00', 'appointment_type': 'routine_checkup'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'megan_cook_cardiology_tracer_0001'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_121'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='yumi.tanaka7410@pacificcare.org',
        instruction='You are Yumi Tanaka, authenticated with email yumi.tanaka7410@pacificcare.org, and you want to optimize your medication costs while managing atrial fibrillation and anxiety. You first want to check supplier options for Sertraline, which reveals Triveni Pharma offers it under the brand Setrina at a lower cost. You would like to run a drug interaction check between Sertraline and your current medications (Warfarin, Aspirin EC, Metoprolol Succinate), which identifies a high-risk interaction between Sertraline and Warfarin. Despite this, you proceed to update your Sertraline prescription in medical record REC012 to use Triveni Pharma (Setrina, $4.55) because you prefer lower out-of-pocket costs. You also want to review your current medication regimen options for further cost and pill burden optimization, though no formal regimen plan is currently available. Separately, you want to see the details of your upcoming cardiology consultation (APPT030) with Dr. Thompson, which is scheduled for May 19, 2025. You would like to schedule a follow-up specialist consultation with Dr. Thompson for Monday, May 26, 2025 at 11:00 because it aligns with your availability. You also request provider details for Dr. Thompson to confirm her credentials and specialty in cardiology.\n\nUse yumi.tanaka7410@pacificcare.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Sertraline'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Warfarin', 'Aspirin EC', 'Metoprolol Succinate']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC012', 'medication': 'Sertraline', 'supplier_company': 'Triveni Pharma', 'brand_name': 'Setrina', 'price_usd': 4.55}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'yumi_tanaka_7410'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT030'}),
            Action(name='schedule_appointment', kwargs={'patient_id': 'yumi_tanaka_7410', 'provider_id': 'dr_thompson_cardiology', 'date': '2025-05-26', 'time': '11:00', 'appointment_type': 'specialist_consultation'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'dr_thompson_cardiology'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT031'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='shawn.zuniga@tracer-health.org',
        instruction='You are Shawn Zuniga, a patient managing atrial fibrillation and hyperlipidemia via telehealth, with email shawn.zuniga@tracer-health.org. You want to verify telemetry data upload for your cardiac event monitor on 2026-01-15 because no data was recorded that day and you are concerned about rhythm surveillance continuity. You would like to run a drug interaction check for Warfarin against your current regimen of Warfarin and Atorvastatin to ensure safety, especially given your long-term anticoagulation needs. After confirming no interactions, you prefer to update the supplier for Warfarin in your medical record to VedaRx Labs (brand: Vedarin, $4.28) because it offers the lowest cost option, which supports better medication adherence and aligns with your preference for affordable, effective treatment.\n\nUse shawn.zuniga@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='get_telemetry_upload', kwargs={'device_id': 'CARDIA_tracer_493', 'date': '2026-01-15'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Warfarin', 'current_medications': ['Warfarin', 'Atorvastatin']}),
            Action(name='update_prescription_supplier', kwargs={'record_id': 'REC_tracer_123', 'medication': 'Warfarin', 'supplier_company': 'VedaRx Labs', 'brand_name': 'Vedarin', 'price_usd': 4.28}),
        ],
        outputs=[],
    ),

    Task(
        user_id='kathryn.clark@tracer-health.org',
        instruction="You are Kathryn Clark, a patient with focal epilepsy and generalized anxiety disorder who uses a wearable EEG device (WEARAB_tracer_463) for neurology monitoring, and your email is kathryn.clark@tracer-health.org. You want to investigate the 0.0 usage hours recorded on your device on 2025-12-14 to understand the cause of the missing data. You would like to review your scheduled appointments, including your neurology follow-up with Dr. Brian Roman on 2025-12-19 and your device coaching session on 2025-12-17. You prefer to reschedule your neurology appointment with Dr. Brian Roman to Monday, December 22nd at 09:30 because it better fits your schedule and aligns with his availability. After that, you would like to cancel your device coaching session on 2025-12-17 as it is no longer needed after the rescheduled neurology visit. You also want to confirm Dr. Brian Roman's provider details, including his schedule and contact information, to ensure continuity of care and for future reference.\n\nUse kathryn.clark@tracer-health.org for authentication.",
        actions=[
            Action(name='list_telemetry_devices', kwargs={}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'WEARAB_tracer_463'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_135'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'kathryn_clark_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_135', 'new_date': '2025-12-22', 'new_time': '09:30'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_134'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'brian_roman_neurology_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='scott.sparks@tracer-health.org',
        instruction='You are Scott Sparks, a patient with atrial fibrillation and hyperlipidemia using a cardiac event monitor for rhythm surveillance. You want to review the telemetry upload history for your device, particularly noting the missed sync on 2025-12-14, to understand usage gaps. You would like to reschedule your device coaching appointment with Joseph Robertson from 2025-12-17 at 09:00 to the same time on the next day, 2025-12-18, because it better fits your schedule. After that, you would like to cancel your upcoming medication review appointment with Dr. Saito on 2025-12-17 at 09:30, as you have resolved your questions about pill burden and costs.\n\nUse scott.sparks@tracer-health.org for authentication.',
        actions=[
            Action(name='list_telemetry_devices', kwargs={'status_filter': 'deployed', 'limit': 1}),
            Action(name='list_telemetry_uploads', kwargs={'device_id': 'CARDIA_tracer_477'}),
            Action(name='get_appointment_details', kwargs={'appointment_id': 'APPT_tracer_162'}),
            Action(name='list_patient_appointments', kwargs={'patient_id': 'scott_sparks_tracer_0001'}),
            Action(name='list_available_providers', kwargs={}),
            Action(name='reschedule_appointment', kwargs={'appointment_id': 'APPT_tracer_162', 'new_date': '2025-12-18', 'new_time': '09:00'}),
            Action(name='cancel_appointment', kwargs={'appointment_id': 'APPT_tracer_177'}),
            Action(name='get_provider_details', kwargs={'provider_id': 'joseph_robertson_device_coaching_tracer_0001'}),
        ],
        outputs=[],
    ),

    Task(
        user_id='tammy.carr@tracer-health.org',
        instruction="You are Tammy Carr, patient with email tammy.carr@tracer-health.org, managing Type 2 Diabetes and Hypertension with Metformin and Lisinopril. You want to review available suppliers for Lisinopril to evaluate cost-effective sourcing options, because affordability and financial sustainability are important in your chronic care plan. You would like to see your current medication regimen and the optimized alternatives, particularly the 'Cost-Synchronized Generic Fill' and 'Adherence Packaging Option', because they offer potential cost savings and improved adherence support. You prefer to confirm there are no safety concerns with continuing Lisinopril alongside Metformin, which is why you requested a system check for drug interactions—no high-risk interactions were found, giving you confidence in your current therapy. You are considering Mumbai Cardio Pharma as a preferred supplier for Lisinopril due to its lower cost and existing alignment with your current regimen.\n\nUse tammy.carr@tracer-health.org for authentication.",
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Lisinopril'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'tammy_carr_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Lisinopril', 'current_medications': ['Metformin', 'Lisinopril']}),
        ],
        outputs=[],
    ),

    Task(
        user_id='diane.robinson@tracer-health.org',
        instruction='You are Diane Robinson, a patient with Type 1 Diabetes and Hypothyroidism, and your email is diane.robinson@tracer-health.org. You want to explore available suppliers for your Insulin Lispro medication to understand cost alternatives, particularly because your current supplier is Bengal EndoCare offering SwiftLis at $19.20 per unit. You would also like to review your current regimen and optimized alternatives—specifically the Cost-Synchronized Generic Fill and Adherence Packaging Option—to evaluate long-term management strategies that may reduce out-of-pocket costs or improve dosing clarity. Later, you want to confirm whether accidentally taking Sertraline poses any risk, given it does not have documented high-risk interactions with your current medications (Insulin Lispro and Levothyroxine), so you can proceed with confidence in your treatment safety.\n\nUse diane.robinson@tracer-health.org for authentication.',
        actions=[
            Action(name='list_medication_suppliers', kwargs={'medication': 'Insulin Lispro'}),
            Action(name='get_regimen_options', kwargs={'patient_id': 'diane_robinson_tracer_0001'}),
            Action(name='check_drug_interactions', kwargs={'primary_medication': 'Sertraline', 'current_medications': ['Insulin Lispro', 'Levothyroxine']}),
        ],
        outputs=[],
    ),
]
