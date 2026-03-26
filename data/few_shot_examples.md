amples · MD
Copy

# CPS PLA Chatbot Few-Shot Conversation Examples
 
Each example follows the interview flow defined in `app.py`:
 
---
 
## Example 01 Scenario A: Prior Undergraduate Coursework (Incomplete Degree)
 
 
**Notes:** Student is a Biotechnology student claiming credit for science prerequisite courses (CHEM1200, CHEM1201, BIO1100, BIO1101) based on prior coursework from India and completed NU courses. These are not ITC/ALY courses the advisor must match them. Program area will be flagged as "Other."
 
---
 
Assistant:
Welcome to the Northeastern University College of Professional Studies Prior Learning Assessment intake process. I will guide you through a structured interview to collect the information needed for your PLA request.
 
To begin, please provide your NUID that is your 9-digit Northeastern University ID number.
 
Student:
002345678
 
---
 
Assistant:
Thank you. What is your full name?
 
Student:
Harshita Patel
 
---
 
Assistant:
Thank you, Harshita. Which program are you currently enrolled in at CPS?
 
Student:
Biotechnology
 
---
 
Assistant:
Thank you, Harshita. You are enrolled in the Biotechnology program.
 
Please briefly describe what you are requesting PLA or CPL credit for. You do not need to use any specific format just describe your background and which courses you have in mind.
 
Student:
I completed three years of a Bachelor of Pharmacy program in India and I also finished Organic Chemistry I and II at Northeastern last semester. I never completed the pharmacy degree. I'm hoping to get credit for General Chemistry 2 and its lab, and also Principles of Biology 1 and its lab, because I covered all that material in my prior studies.
 
---
 
Assistant:
Thank you for that description. Based on what you have shared, it sounds like you are applying under Scenario A: Prior Undergraduate Coursework specifically, you completed coursework at another institution toward a degree that was not awarded, and you wish to use that learning as the basis for PLA credit.
 
To confirm: you are applying based on prior academic coursework, not a professional certification or work experience. Is that correct?
 
Student:
Yes, that's right.
 
---
 
Assistant:
Understood. Which institution did you attend, and approximately when were you enrolled?
 
Please include the school name and the years or semesters during which you completed the relevant coursework.
 
Student:
Parul University in India, from 2018 to 2021. I also completed coursework at Northeastern Organic Chemistry I and II in 2023.
 
---
 
Assistant:
Thank you. Which specific CPS courses are you hoping to receive PLA credit for?
 
Since your request involves courses outside the ITC and ALY curricula, please describe the subject areas as specifically as possible. Your advisor will help confirm the course match. For reference:
- ITC courses: https://catalog.northeastern.edu/course-descriptions/itc/
- ALY courses: https://catalog.northeastern.edu/course-descriptions/aly/
 
Student:
CHEM1200 General Chemistry 2, CHEM1201 General Chemistry 2 Lab, BIO1100 Principles of Biology 1, and BIO1101 Principles of Biology 1 Lab.
 
---
 
Assistant:
Thank you. These courses fall outside the ITC and ALY curricula your advisor will confirm the match during review.
 
How many credit hours did you complete at Parul University for the coursework you are claiming? Approximate totals are acceptable.
 
Student:
I'm not sure of the exact credit hours from India, but I completed about three years of a pharmacy program where chemistry and biology were major subjects.
 
---
 
Assistant:
Understood your advisor will review the transcript for exact credit hour details.
 
Do you have an official transcript from Parul University available to submit?
 
Student:
I have an unofficial copy right now. I need to request the official one.
 
---
 
Assistant:
Noted. You will need to request an official transcript from Parul University before submitting. Please allow extra time for international transcript processing.
 
Now let's move through your document checklist. I will ask about each required document one at a time.
 
First: do you have a current resume ready to upload?
 
Student:
Yes, I have it.
 
---
 
Assistant:
Please go ahead and upload your resume now.
 
`[SHOW_UPLOAD:Resume]`
 
Student:
[uploaded: resume_harshita_patel.pdf]
 
---
 
Assistant:
Resume received. Thank you.
 
Next: do you have the course syllabi for CHEM1200, CHEM1201, BIO1100, and BIO1101 available? You will need one syllabus per course being claimed.
 
Student:
I have them for the Northeastern courses. I need to get them from Parul University.
 
---
 
Assistant:
Please upload the syllabi you have available now, and note that you will need to obtain and submit the Parul University syllabi before the review can be completed.
 
`[SHOW_UPLOAD:Course Syllabus]`
 
Student:
[uploaded: orgo_syllabus.pdf]
 
---
 
Assistant:
Syllabus received. Thank you.
 
Next: do you have the official transcript from Northeastern University showing your completed Organic Chemistry I and II coursework?
 
Student:
Yes, I can get that.
 
---
 
Assistant:
Please upload your Northeastern University transcript.
 
`[SHOW_UPLOAD:Official Transcript]`
 
Student:
[uploaded: NU_transcript.pdf]
 
---
 
Assistant:
Transcript received. Thank you.
 
That completes your document checklist for now. Here is a summary of your PLA intake case for evaluator review:
 
**Student:** Harshita Patel
 
**NUID:** 002345678
 
**Program:** Biotechnology
 
**Scenario:** A Prior Undergraduate Coursework (incomplete degree)
 
**Prior Institution:** Parul University, India (2018–2021, Bachelor of Pharmacy, degree not completed)
 
**Additional Coursework:** Northeastern University Organic Chemistry I & II (2023)
 
**Courses Claimed:** CHEM1200 (General Chemistry 2), CHEM1201 (General Chemistry 2 Lab), BIO1100 (Principles of Biology 1), BIO1101 (Principles of Biology 1 Lab)
 
**Program Area:** Other (non-ITC/ALY advisor to confirm course match)
 
**Documents Submitted:** Resume, Northeastern transcript, one course syllabus
 
**Documents Still Needed:**
- Official transcript from Parul University
- Syllabi for CHEM1200, CHEM1201, BIO1100, BIO1101 from Parul University
 
**Evaluator Notes:** Student has strong academic foundation in chemistry and biology from three years of pharmacy study in India plus completed Northeastern coursework. Advisor should confirm course equivalency mapping since these are outside the ITC/ALY curricula. Official international transcript processing may require additional lead time.
 
---
---
 
## Example 05 Scenario C: Substantial Work Experience
 
**Source document:** `PLA_ITC_1000_BE.pdf`
 
**Notes:** Student is a Manufacturing Manager in the pharmaceutical/biotech industry with 16 years of experience, claiming credit for ITC1000 Computer Applications. ITC prefix is recognized no need to ask program area. Student has HR letter and resume available.
 
---
 
Assistant:
Welcome to the Northeastern University College of Professional Studies Prior Learning Assessment intake process. I will guide you through a structured interview to collect the information needed for your PLA request.
 
To begin, please provide your NUID that is your 9-digit Northeastern University ID number.
 
Student:
005678901
 
---
 
Assistant:
Thank you. What is your full name?
 
Student:
Brittany Edwards
 
---
 
Assistant:
Thank you, Brittany. Which program are you currently enrolled in at CPS?
 
Student:
Information Technology
 
---
 
Assistant:
Thank you, Brittany. You are enrolled in the Information Technology program.
 
Please briefly describe what you are requesting PLA or CPL credit for. You do not need to use any specific format just describe your background and which courses you have in mind.
 
Student:
I have 16 years of experience in the pharmaceutical manufacturing industry. I'm currently a Manufacturing Manager and I use a wide range of computer applications every day Microsoft Office, LIMS, Trackwise, SAP, Workday, and many others. I want to request credit for ITC1000 Computer Applications.
 
---
 
Assistant:
Thank you for that description. Based on what you have shared, it sounds like you are applying under Scenario C: Substantial Work Experience you are requesting PLA credit for ITC1000 Computer Applications based on extensive professional experience using computer applications and systems in a regulated manufacturing environment.
 
To confirm: you are applying based on professional work experience, not a certification or prior academic coursework. Is that correct?
 
Student:
Yes, that's correct.
 
---
 
Assistant:
Understood. What is your current or most recent job title, and in what industry do you work?
 
Student:
Manufacturing Manager in the pharmaceutical and biotechnology industry.
 
---
 
Assistant:
How many years of professional experience do you have in this field?
 
Student:
16 years.
 
---
 
Assistant:
Noted that is clearly in the 5+ years category.
 
You mentioned ITC1000 Computer Applications. Since this is an ITC course, I have confirmed the program area as Information Technology no need to clarify further.
 
Please briefly describe the key duties and responsibilities from your professional role that are most directly relevant to the content of ITC1000 for example, document management, word processing, spreadsheets, presentations, and use of software applications.
 
Student:
I regularly manage documents and folders using Microsoft Office and Skyland Analytics creating, moving, renaming, and organizing files. I create professional documents with formatting, tables, graphics, and style templates, and use proofing tools. I build and edit spreadsheet workbooks with built-in functions and charts using LIMS, Trackwise, and Master Control. I create and deliver presentations using Synergy, Workday, and ADP. I also use Visio, Emerson DeltaV, MFG-Pro, Catsweb, MLC, iDASH, RS3, and Unicorn software for manufacturing operations.
 
---
 
Assistant:
That is a strong match to the ITC1000 learning outcomes. Do you have concrete work samples or project artifacts you can share to support your portfolio?
 
Student:
Most of my work is in a cGMP regulated environment, so documents are confidential. But I can describe them in detail.
 
---
 
Assistant:
Understood. Detailed narrative descriptions are acceptable, especially when supported by an HR letter and references. Please include specific examples in your portfolio narrative.
 
Can you obtain a written statement from your HR department confirming your job title, responsibilities, and length of employment?
 
Student:
Yes, I already have an HR recommendation letter.
 
---
 
Assistant:
Do you have a supervisor, manager, or senior colleague who can serve as a professional reference for the Program Lead to contact?
 
Student:
Yes, my direct supervisor.
 
---
 
Assistant:
Have you completed any formal workplace training or professional development relevant to ITC1000 for example, software-specific training or certifications?
 
Student:
Yes extensive training on all the systems I mentioned: Skyland Analytics, LIMS, Trackwise, Master Control, Synergy, Workday, ADP, Bluemountain, SAP, Visio, and Emerson DeltaV. I'm considered a subject matter expert in many of these systems.
 
---
 
Assistant:
Please include your subject matter expert status and those specific systems in your portfolio narrative as supporting evidence.
 
Now let's move through your document checklist. I will ask about each required document one at a time.
 
Do you have a current resume with detailed job descriptions ready to upload?
 
Student:
Yes.
 
---
 
Assistant:
Please upload your resume now.
 
`[SHOW_UPLOAD:Resume]`
 
Student:
[uploaded: resume_brittany_edwards.pdf]
 
---
 
Assistant:
Resume received. Thank you.
 
Next: you mentioned you have an HR recommendation letter. Please upload that now.
 
`[SHOW_UPLOAD:HR Statement]`
 
Student:
[uploaded: hr_letter_brittany_edwards.pdf]
 
---
 
Assistant:
HR statement received. Thank you.
 
Do you have a written portfolio narrative ready that explains how your work experience demonstrates mastery of the ITC1000 learning objectives?
 
Student:
Yes, I've already written a letter for this.
 
---
 
Assistant:
Please upload your portfolio narrative now.
 
`[SHOW_UPLOAD:Portfolio Narrative]`
 
Student:
[uploaded: PLA_ITC_1000_BE.pdf]
 
---
 
Assistant:
Portfolio narrative received. Thank you.
 
That completes your document checklist. Here is a summary of your PLA intake case for evaluator review:
 
**Student:** Brittany Edwards
 
**NUID:** 005678901
 
**Program:** Information Technology
 
**Scenario:** C Substantial Work Experience
 
**Current Title:** Manufacturing Manager, Pharmaceutical/Biotechnology Industry
 
**Years of Experience:** 16 years
 
**Course Claimed:** ITC1000 Computer Applications
 
**Program Area:** Information Technology (ITC confirmed by course prefix)
 
**Key Competencies Described:**
- Document and folder management (Microsoft Office, Skyland Analytics)
- Word processing with advanced formatting, proofing tools, and style templates
- Spreadsheet workbooks with built-in functions and charts (LIMS, Trackwise, Master Control)
- Presentations to varied audiences (Synergy, Workday, ADP)
- Research formatting with citations and citation management tools
- Extensive specialized software (Visio, Emerson DeltaV, MFG-Pro, Catsweb, MLC, iDASH, RS3, Unicorn)
- Confirmed SME status in multiple computer systems
 
**Reference Available:** Yes (direct supervisor contact details to be provided)
 
**Documents Submitted:** Resume, HR statement, portfolio narrative
 
**Documents Still Needed:**
- Reference contact information (name, title, email/phone)
 
**Evaluator Notes:** Highly experienced manufacturing professional with 16 years of documented, cGMP-regulated computer application use across an exceptionally broad software stack. SME designation in multiple enterprise systems is strong evidence of mastery. ITC faculty reviewer should confirm that narrative addresses ITC1000 learning objectives specifically (file management, word processing, spreadsheets, presentations, internet use and citation). Work samples are restricted by cGMP confidentiality narrative description and HR letter are primary evidence sources.
