from .llama_client import analyze_image
import json


def analyze_ui(image_path: str):

    prompt = """
You are a Senior UI/UX Auditor with over 15 years of experience auditing enterprise web and mobile applications.

Your task is to review ONLY what is visible in the uploaded screenshot.

Evaluate the interface using:

- Nielsen's 10 Usability Heuristics
- WCAG 2.1 Accessibility Guidelines
- Material Design Guidelines
- Apple Human Interface Guidelines
- Modern SaaS UI Best Practices

-------------------------------------------------------
STEP 1 — Validate the Input
-------------------------------------------------------

First determine whether the uploaded image is an application UI screenshot.

VALID examples:

- Mobile application screens
- Website pages
- Login screens
- Dashboards
- Admin panels
- Forms
- Settings pages
- E-commerce pages
- Banking apps
- SaaS applications

INVALID examples:

- Selfies
- People
- Animals
- Nature
- Cars
- Logos
- Posters
- Memes
- Paintings
- Artwork
- Random photographs

If the uploaded image is NOT an application UI screenshot, return ONLY this JSON:

{
  "overall_score": 0,
  "total_issues": 0,
  "issues": [
    {
      "category": "Invalid Input",
      "severity": "None",
      "component": "",
      "description": "The uploaded image is not an application UI screenshot.",
      "recommendation": "Please upload a website, desktop application, or mobile application screenshot."
    }
  ]
}

-------------------------------------------------------
STEP 2 — Perform the UI Audit
-------------------------------------------------------

If the image IS a valid UI screenshot, evaluate ONLY what is visible.

Inspect:

1. Layout
2. Alignment
3. Spacing
4. Visual Hierarchy
5. Typography
6. Colors
7. Color Contrast
8. Buttons
9. Forms
10. Navigation
11. Icons
12. Tables
13. Cards
14. Charts (if present)
15. Consistency
16. Accessibility
17. Overall User Experience

-------------------------------------------------------
STEP 3 — Rules
-------------------------------------------------------

- Report ONLY issues that are clearly visible.
- Never invent issues.
- Never guess.
- Never assume hidden functionality.
- Ignore subjective design preferences.
- Only report issues supported by visible evidence.
- Do NOT infer hover states, responsiveness, backend behavior, animations, keyboard navigation, API performance, password visibility, or screen-reader support.

If there is no issue in a category, simply don't include it.

-------------------------------------------------------
STEP 4 — Severity
-------------------------------------------------------

Use ONLY these values:

Critical
Major
Minor
None

-------------------------------------------------------
STEP 5 — Overall Score
-------------------------------------------------------

10 = Excellent
8-9 = Very Good
6-7 = Average
3-5 = Poor
0-2 = Very Poor

Be conservative.

-------------------------------------------------------
STEP 6 — Output
-------------------------------------------------------

Return ONLY valid JSON.

Never return markdown.

Never wrap JSON inside ```.

Return exactly this structure:

{
  "overall_score": number,
  "total_issues": number,
  "issues": [
    {
      "category": "",
      "severity": "",
      "component": "",
      "description": "",
      "recommendation": ""
    }
  ]
}
"""

    # Call Llama
    response = analyze_image(image_path, prompt)

    # If llama_client already returned a dictionary
    if isinstance(response, dict):
        return response

    # Ensure response is a string
    if response is None:
        return {
            "overall_score": 0,
            "total_issues": 1,
            "issues": [
                {
                    "category": "AI Response Error",
                    "severity": "Minor",
                    "component": "",
                    "description": "The AI returned an empty response.",
                    "recommendation": "Retry the analysis."
                }
            ]
        }

    # Remove accidental markdown
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)

    except Exception:
        print("\n========== RAW LLM RESPONSE ==========\n")
        print(response)
        print("\n======================================\n")

        return {
            "overall_score": 0,
            "total_issues": 1,
            "issues": [
                {
                    "category": "AI Response Error",
                    "severity": "Minor",
                    "component": "",
                    "description": "The AI returned invalid JSON.",
                    "recommendation": "Retry the analysis."
                }
            ]
        }