from crewai import Task


def create_final_plan_task(agent, market_task, business_task, technical_task, debate_task):
    return Task(
        description="""
Create the final improved startup/product plan.

Original idea:
{idea}

Use the specialist analyses and the Challenger's debate.

Your final answer must contain:

1. Executive Summary
2. Problem
3. Target Customers
4. Proposed Solution
5. Key Differentiator
6. Market Analysis
7. Business Model
8. MVP Features
9. Technical Architecture
10. Main Risks
11. Improvements After Debate
12. 90-Day Development Roadmap
13. 30-Second Elevator Pitch

Important:
- Do not claim that real market research was performed.
- Do not invent statistics.
- Clearly distinguish assumptions from conclusions.
- Keep the MVP realistic.
- Incorporate useful Challenger feedback.
""",
        expected_output="A complete improved startup/product plan.",
        agent=agent,
        context=[
            market_task,
            business_task,
            technical_task,
            debate_task,
        ],
    )
