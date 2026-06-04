from pptx import Presentation
from pathlib import Path

ppt_path = Path(r'c:/Users/Elijay/Desktop/Platform-Explorers-Cohort-2/Capstone/Platform Explorers Use Case Template.pptx')
output_path = Path(r'c:/Users/Elijay/Desktop/Platform-Explorers-Cohort-2/Capstone/IT Support Request Assistant - Final Presentation.pptx')

prs = Presentation(str(ppt_path))

s1 = prs.slides[0]
s1.shapes[3].text = 'IT SUPPORT REQUEST ASSISTANT'
s1.shapes[5].text = 'Platform Explorers Cohort 2  |  Capstone Project  |  June 2026'

s2 = prs.slides[1]
s2.shapes[8].text = (
    'Organizations depend on IT systems, but request intake is often informal, unstructured, and inconsistent.\\n\\n'
    'Key challenges addressed:\\n'
    '- Unstructured submissions (email, calls, chat) cause missing information\\n'
    '- Poor prioritization delays critical issue response\\n'
    '- Manual handling reduces scalability and increases error risk\\n'
    '- No real-time validation creates rework and longer resolution cycles\\n'
    '- Limited user guidance lowers request quality\\n\\n'
    'Why it matters:\\n'
    '- Slower support response and avoidable downtime\\n'
    '- Inefficient use of IT resources\\n'
    '- Reduced user confidence in support operations\\n\\n'
    'Objective: standardize and automate IT request capture and routing through a conversational assistant.'
)

s3 = prs.slides[2]
s3.shapes[8].text = (
    'Solution overview:\\n'
    'An intelligent conversational assistant built with Microsoft Copilot Studio and integrated with Power Automate.\\n\\n'
    'End-to-end solution flow:\\n'
    '- Conversation Start topic guides users with example request phrases\\n'
    '- Submit a Request captures structured data (name, email, phone, department, issue type, priority, description)\\n'
    '- Priority logic branches for Critical, High, Medium, and Low handling\\n'
    '- Summary and confirmation step validates user input before submission\\n'
    '- Ticket generated dynamically: IT-XXXXXXXX\\n'
    '- Automated handoff to ITReqEmailFlow for HTML-formatted notification email\\n'
    '- Start Over topic supports safe restart with Boolean confirmation logic\\n\\n'
    'Evidence references: Fig-01 to Fig-08 (including Fig-06a Email Delivery Confirmation).'
)

s4 = prs.slides[3]
s4.shapes[8].text = (
    'Technical configuration:\\n'
    '- Platform: Microsoft Copilot Studio + Power Automate + Outlook\\n'
    '- Core topics: Conversation Start, Submit a Request, Start Over\\n\\n'
    'Key variables implemented:\\n'
    '- userName, userEmail, userPhone\\n'
    '- department / departmentText\\n'
    '- issueType / issueTypeText\\n'
    '- priorityLevel / priorityText\\n'
    '- issueDescription, ticketID, Confirm\\n'
    '- System variables: Bot.Name, System.Conversation.Id\\n\\n'
    'Core logic:\\n'
    '- Normalization nodes convert choice values to text fields\\n'
    '- Priority conditions drive response behavior\\n'
    '- Ticket formula: "IT" & "-" & Right(System.Conversation.Id, 8)\\n\\n'
    'Power Automate (ITReqEmailFlow):\\n'
    '- Triggered by Copilot action\\n'
    '- Inputs: userName, department, issueType, issueDescription, priorityLevel, ticketID, userEmail, userPhone\\n'
    '- Compose builds structured HTML body\\n'
    '- Send Email action dispatches request\\n'
    '- Respond to agent returns submission status'
)

s5 = prs.slides[4]
s5.shapes[8].text = (
    'Testing and outcome summary:\\n\\n'
    'Test scenarios executed:\\n'
    '- Standard request -> Success\\n'
    '- Critical issue -> Escalation triggered\\n'
    '- Incorrect input -> Handled\\n'
    '- Restart flow -> Works correctly\\n\\n'
    'Observed business impact:\\n'
    '- Faster IT request processing through guided intake\\n'
    '- Improved data accuracy with structured capture and confirmation\\n'
    '- Better prioritization using rule-based logic\\n'
    '- Reduced manual effort via automated email submission\\n\\n'
    'Integration sequence:\\n'
    'Copilot Studio -> Call Action -> Power Automate -> Email Sent -> Response Returned'
)

s6 = prs.slides[5]
s6.shapes[8].text = (
    'Lessons learnt:\\n'
    '- Structured conversation design improves request quality\\n'
    '- Priority logic is essential for operational automation\\n'
    '- Validation and confirmation reduce rework and communication loops\\n'
    '- End-to-end integration is critical for support efficiency\\n\\n'
    'Improvement actions:\\n'
    '- Attach all remaining evidence screenshots (Fig-02 to Fig-17)\\n'
    '- Add dashboard monitoring for request volume and SLA trends\\n'
    '- Extend connectors to enterprise ticketing systems (ServiceNow/Dynamics 365)\\n'
    '- Add analytics for category trends and escalation root causes\\n'
    '- Introduce role-based routing and policy-driven triage enhancements'
)

prs.save(str(output_path))
print(f'Saved: {output_path}')
