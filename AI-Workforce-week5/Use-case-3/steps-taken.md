# Steps Taken — Fabrikam Employee Assistant

This file documents the steps taken to create and test the Fabrikam Employee Helper agent in **Copilot Studio**.  
It includes the agent configuration, topics created, prompts used, and responses observed during testing.

---

## Agent Configuration
- **Agent Name:** Fabrikam Employee Helper  
- **Purpose:** Provide quick, accurate answers to common employee questions (office hours, IT contact, company portal).  
- **Tone:** Friendly, concise, and professional.  
- **Scope:** Workplace FAQs only.  

![alt text](assets/image.png)
*Screenshot: Agent configuration page showing name, description, and scope.*

---

## Topics Created

### Topic: Office Hours
- **Trigger phrases:**  
  - “What are the office hours?”  
  - “When is the office open?”  
  - “Working hours Fabrikam”  
  - “What time does the office close?”
- **Response:**  
  - “Fabrikam office hours are Monday–Friday, 9 AM to 5 PM.”

![alt text](assets/image1.png)
*Screenshot: Office Hours topic with trigger phrases and response.*

---

### Topic: IT Contact
- **Trigger phrases:**  
  - “How do I contact IT?”  
  - “IT support number”  
  - “Helpdesk contact”  
  - “Who do I call for tech issues?”
- **Response:**  
  - “You can reach IT at it-support@fabrikam.com or call 555‑1234.”

![alt text](assets/image2.png)
*Screenshot: IT Contact topic with trigger phrases and response.*

---

### Topic: Company Portal
- **Trigger phrases:**  
  - “Where is the company portal?”  
  - “How do I log in to the portal?”  
  - “Portal link Fabrikam”  
- **Response:**  
  - “Go to https://portal.fabrikam.com and sign in with your employee credentials.”

![alt text](assets/image3.png)
*Screenshot: Company Portal topic with trigger phrases and response.*

---

### Topic: Fallback (Off‑Topic Handling)
- **Response:**  
  - “I’m here to help with Fabrikam workplace questions such as office hours, IT support, or the company portal.  
    For other topics, please check the Fabrikam intranet or contact HR directly.”

![alt text](assets/image4.png)
*Screenshot: Fallback topic configuration.*

---

## Testing in the Canvas

### Prompt: “What are the office hours?”
- **Response:** “Fabrikam office hours are Monday–Friday, 9 AM to 5 PM.”  

---

### Prompt: “How do I contact IT?”
- **Response:** “You can reach IT at it-support@fabrikam.com or call 555‑1234.”  

---

### Prompt: “Where is the company portal?”
- **Response:** “Go to https://portal.fabrikam.com and sign in with your employee credentials.”  

---

### Prompt: “Can you reset my Windows password?”
- **Response:** “I’m here to help with Fabrikam workplace questions such as office hours, IT support, or the company portal.  
  For other topics, please check the Fabrikam intranet or contact HR directly.”  

![alt text](assets/image5.png)
*Screenshot: all test prompts*
---

## Summary
- Agent was successfully created with **3 core topics** and a **fallback topic**.  
- All prompts triggered the correct responses in the test canvas.  
- The agent stayed true to its purpose: focused on Fabrikam workplace FAQs.  
- Testing confirmed reliability and scope adherence.  

---
