from crewai import Task


def create_debate_task(agent, market_task, business_task, technical_task):
    return Task(
        description="""
You are the Challenger Agent.

The startup idea is:

{idea}

Review the outputs from the Market, Business, and Technical agents.

Your job is to challenge their conclusions.

Identify:
1. The strongest weakness in the idea
2. The weakest assumption
3. A customer-related concern
4. A business-related concern
5. A technical concern
6. A disagreement between the analyses, if one exists
7. Specific improvements that could solve the weaknesses

Do not criticize the idea without explaining the reason.
Do not invent facts.

Market analysis:
{market_output}

Business analysis:
{business_output}

Technical analysis:
{technical_output}
""",
        expected_output="A structured challenge and debate analysis.",
        agent=agent,
        context=[market_task, business_task, technical_task],
    )
