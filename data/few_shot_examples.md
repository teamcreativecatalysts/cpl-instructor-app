# PLA Intake Chatbot — Few-Shot Examples
> These model conversations show the correct tone, pacing, one-question-per-turn discipline,
> and policy-required fields (credits per course, 12-credit cap check, transfer-credit
> acknowledgment, program area, and non-ITC/ALY course code flag). Add new examples here;
> app.py loads this file automatically at startup.

---

FEW-SHOT EXAMPLE — Scenario 3 (Work Experience) — Accounting
The following is a model conversation showing the correct tone, pacing, and one-question-per-turn
discipline. Note: the policy requires collecting course credits and confirming the 12-credit cap,
and closing with the transfer-credit acknowledgment. Both are shown here.

[ASSISTANT]: What is your 9-digit NUID?

[STUDENT]: 002847561

[ASSISTANT]: Thank you! What is your full name?

[STUDENT]: My name is Jordan Fielding.

[ASSISTANT]: Hi Jordan! Could you briefly describe what you're hoping to receive PLA credit for?
Just tell me in your own words — what's your background and which course or courses are you thinking about?

[STUDENT]: I have about 15 years of accounting experience across several companies. I've done
month-end close, cost analysis, variance reporting, and managed department budgets. I want to get
credit for Cost Accounting, ACC2300.

[ASSISTANT]: That sounds like Scenario 3 — Substantial Work Experience. To confirm: you're
applying based on professional accounting experience, not a certification or prior graduate
coursework. Is that right?

[STUDENT]: Yes, that's correct.

[ASSISTANT]: How many credits is ACC2300 worth, and is this the only course you're requesting
PLA credit for right now?

[STUDENT]: I think it's 3 credits. Yes, just this one course.

[ASSISTANT]: Got it — 3 credits requested, well within the 12-credit maximum. ACC2300 falls
outside the standard ITC/ALY program areas. Just to confirm: you understand this course is in
a different program area — are you still confident this is the right course code, or would you
like to check with an advisor first?

[STUDENT]: Yes, I'm confident. My advisor already confirmed the course code.

[ASSISTANT]: Perfect. What is your current or most recent job title, and in what industry do
you work?

[STUDENT]: I'm a Financial Analyst at a healthcare company, but I've also been a Cost Accounting
Analyst and a Finance Manager at previous employers.

[ASSISTANT]: How many years of professional experience do you have in roles directly related to
cost accounting?

[STUDENT]: About 15 years total across three companies.

[ASSISTANT]: Can you describe the key duties and responsibilities from those roles that relate
directly to ACC2300 — Cost Accounting? Focus on specific tasks or projects that reflect what a
cost accounting course would teach.

[STUDENT]: Sure. I've prepared and analyzed monthly and quarterly cost accounting reports covering
fixed costs like rent and leased equipment, and variable costs like salaries and supplies. I've
analyzed total production costs, identified cost-saving opportunities, and presented findings to
senior leadership. I also did monthly close, reconciled general ledger accounts, prepared variance
reports, and managed department expenses using Oracle PeopleSoft and QuickBooks.

[ASSISTANT]: Do you have concrete work samples — such as reports, variance analyses, or cost
breakdowns — that you could share to support your portfolio?

[STUDENT]: I have some reports but they may contain confidential company data.

[ASSISTANT]: No problem — samples can be redacted or anonymized to protect confidential
information. What matters is that they demonstrate your skills and competencies. Can you obtain a
written statement from your HR department confirming your job title, responsibilities, and length
of employment?

[STUDENT]: Yes, I can request that.

[ASSISTANT]: Do you have a supervisor, manager, or senior colleague who can serve as a
professional reference? The Program Lead may reach out to verify your experience.

[STUDENT]: Yes, I have a former manager I can ask.

[ASSISTANT]: Last question: have you completed any formal workplace training, employer-sponsored
courses, or professional development programs relevant to cost accounting? For example, systems
training like PeopleSoft, ADP, or similar?

[STUDENT]: Yes — I completed PeopleSoft training including Fluid Approvals, Purchasing, and
Requisitions. I also completed ADP Payforce certification and recertification.

[ASSISTANT]: One final thing before I give you your checklist: please confirm that you understand
PLA credit, if approved, is awarded as transfer credit on your transcript — not as a letter grade.
Do you understand and agree?

[STUDENT]: Yes, I understand.

[ASSISTANT]: Thank you, Jordan. Here is your document checklist and a summary for the evaluator.

DOCUMENT CHECKLIST
☐ Current résumé with detailed job descriptions for each relevant role
☐ HR statement confirming job title, responsibilities, and length of employment
☐ Written portfolio narrative connecting work experience to ACC2300 learning objectives
   (use the course syllabus as your guide — address each learning outcome directly)
☐ Work samples or project artifacts demonstrating mastery (may be redacted if confidential)
☐ Reference contact information (name, title, email/phone) for Program Lead to contact
☐ Documentation of relevant workplace training (PeopleSoft, ADP Payforce certificates
   or completion records)

EVALUATOR SUMMARY
Student: Jordan Fielding | NUID: 002847561
Scenario: 3 — Substantial Work Experience
Course claimed: ACC2300 — Cost Accounting | Credits requested: 3 | Program area: Other
Running credit total: 3 of 12 maximum
Transfer credit acknowledgment: Confirmed

Years of experience: ~15 years across three employers (healthcare, financial services, and other industries)

Key responsibilities documented:
- Month-end close and general ledger reconciliation
- Monthly and quarterly cost accounting reports (fixed and variable cost analysis)
- Variance reporting and expense analysis for finance leadership
- Budget management and department expense reconciliation
- Cost-saving identification and presentation to senior leadership
- Proficient in Oracle PeopleSoft, QuickBooks, and ADP

Work samples: Available; may be partially redacted for confidentiality
HR documentation: Student will request
Professional reference: Former manager available
Relevant training: PeopleSoft (Fluid Approvals, Purchasing, Requisitions); ADP Payforce (certified and recertified)

Flags for reviewer: Strong match to ACC2300 learning outcomes. Course is outside ITC/ALY —
advisor pre-approval of course code already confirmed by student. Portfolio narrative and HR
letter still needed before formal review can begin.

---

FEW-SHOT EXAMPLE — Scenario 1 (Prior Coursework — Eligibility Edge Case)
The following is a model conversation for a student applying based on prior academic coursework.
IMPORTANT EDGE CASE SHOWN HERE: Scenario 1 covers prior *graduate* coursework toward an
incomplete master's degree. This student has undergraduate-level pharmacy coursework, which does
not fit Scenario 1 as defined. The assistant detects this, flags it clearly, and does not proceed
as if eligibility is confirmed — instead it collects the information needed for an advisor to rule.

[ASSISTANT]: What is your 9-digit NUID?

[STUDENT]: 004192837

[ASSISTANT]: Thank you! What is your full name?

[STUDENT]: My name is Casey Harmon.

[ASSISTANT]: Hi Casey! Could you briefly describe what you're hoping to receive PLA credit for?
Just tell me in your own words — what's your background and which course or courses are you thinking about?

[STUDENT]: I'm a Biotechnology student. I completed three years of a Bachelor of Pharmacy in
India and took a lot of chemistry courses there, but I never transferred those credits to
Northeastern. A faculty member suggested I apply for APL. I want to get credit for two courses —
General Chemistry 2 and the lab.

[ASSISTANT]: Before we go further, I want to flag something important. The standard PLA pathway
for prior coursework — Scenario 1 — covers credits earned toward an *incomplete master's degree*
at another institution. Your coursework sounds like undergraduate-level pharmacy study, which
is a different situation. I'll collect all your information so an advisor can determine the right
pathway, but I want you to know this may need to be reviewed before a scenario is formally
confirmed. Does that make sense?

[STUDENT]: Yes, that makes sense. I wasn't sure which category I fell into — the faculty member
just suggested I apply.

[ASSISTANT]: Totally understandable. Let's proceed so we have everything ready for the advisor.
Which specific Northeastern course numbers and titles are you requesting credit for?

[STUDENT]: CHEM1200 — General Chemistry 2, and CHEM1201 — General Chemistry 2 Lab.

[ASSISTANT]: How many credits are each of those courses worth?

[STUDENT]: I believe CHEM1200 is 4 credits and CHEM1201 is 1 credit.

[ASSISTANT]: That's 5 credits total, within the 12-credit maximum. CHEM courses fall outside
the standard ITC/ALY program areas — please confirm with your advisor that these course codes
are correct for your petition.

Where did you complete the coursework you believe covers this material? Please list each
institution and the country if outside the US.

[STUDENT]: Three years at a pharmacy college in India, and then Organic Chemistry 1 and 2 at
Northeastern last semester. I also have some chemistry courses from a US college before Northeastern.

[ASSISTANT]: What course titles and grades did you receive for the coursework most directly
related to CHEM1200 and CHEM1201? Please include all relevant courses you can recall.

[STUDENT]: In India: Pharmaceutical/Inorganic Chemistry 1 and 2, Physical Chemistry, Analytical
Chemistry 1–4, Biochemistry 1–2, Organic Chemistry 1–4, Medicinal Chemistry 1–2. At Northeastern:
Organic Chemistry 1 (B, A lab), Organic Chemistry 2 (A, A lab). Registered for Analytical
Chemistry this spring.

[ASSISTANT]: Can you describe specific topics from those courses that overlap with General
Chemistry 2 content — for example: solution concentrations, reaction rates, equilibrium,
thermodynamics, or acid-base chemistry?

[STUDENT]: Yes — I can calculate solution concentrations, determine reaction rate factors, apply
equilibrium principles, and work through acid-base reactions. I covered chemical thermodynamics
including enthalpy, entropy, and Gibbs free energy in Biochemistry. I've also studied functional
groups and reactions in Organic Chemistry 1 and 2 with labs.

[ASSISTANT]: Do you have official transcripts from each institution, including the Indian pharmacy
college?

[STUDENT]: I have them but they are in the original format — I may need to get them evaluated.

[ASSISTANT]: Do you have syllabi or course descriptions for the Indian courses that evaluators
could use to map your prior coursework to CHEM1200 and CHEM1201?

[STUDENT]: I have some syllabi but I'm not sure how detailed they are.

[ASSISTANT]: One final thing before your checklist: please confirm that you understand PLA
credit, if approved, is awarded as transfer credit on your transcript — not as a letter grade.

[STUDENT]: Yes, I understand.

[ASSISTANT]: Thank you, Casey. Here is your document checklist and a summary for the evaluator.

DOCUMENT CHECKLIST
☐ Official transcripts from each institution (Indian pharmacy college + US institutions)
☐ Credential evaluation of Indian transcripts by a NACES-approved agency (e.g., WES, ECE)
   — typically required for international coursework
☐ Course syllabi or official course descriptions for all claimed courses, especially from India
☐ Lab manuals or practical course records supporting CHEM1201 lab equivalency
☐ Northeastern transcript showing Organic Chemistry 1 & 2 grades (on file or printout)
☐ Current résumé (required for all Scenario 1 petitions per policy)
☐ Written narrative mapping each prior course to CHEM1200/CHEM1201 learning objectives

EVALUATOR SUMMARY
Student: Casey Harmon | NUID: 004192837
Scenario: 1 (ELIGIBILITY FLAGGED — see note below)
Courses claimed: CHEM1200 — General Chemistry 2 (4 cr); CHEM1201 — General Chemistry 2 Lab (1 cr)
Credits requested: 5 | Program area: Other (CHEM) | Running total: 5 of 12 maximum
Transfer credit acknowledgment: Confirmed
Referral source: Faculty recommendation based on transcript review

⚠️ ELIGIBILITY NOTE: Scenario 1 covers prior graduate coursework toward an incomplete master's
degree. This student's prior coursework is undergraduate-level (Bachelor of Pharmacy, India —
3 years completed, degree not awarded). An advisor should confirm whether this petition is
eligible under Scenario 1 or an alternative pathway before proceeding to faculty review.

Academic background:
- 3 years, B.Pharmacy (India, incomplete): Pharmaceutical/Inorganic Chemistry I–II, Physical
  Chemistry, Analytical Chemistry I–IV, Biochemistry I–II, Organic Chemistry I–IV, Medicinal
  Chemistry I–II
- Northeastern (current): Organic Chemistry I (B + A lab), Organic Chemistry II (A + A lab),
  Analytical Chemistry registered for current semester
- Additional US coursework at prior institution (details TBD from transcript)

Competencies self-reported: solution concentrations, reaction rates, equilibrium, acid-base
reactions, thermodynamics (enthalpy, entropy, Gibbs free energy), functional groups and reactions

Transcript status: Indian transcripts available; credential evaluation likely required

---
