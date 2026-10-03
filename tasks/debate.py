```python
from crewai import Task


def create_debate_task(agent, market_task, business_task, technical_task):
    return Task(
        description="""
You are the Challenger Agent.

Startup idea:

{idea}

Review the Market, Business, and Technical Agent analyses provided through
the task context.

Your job is to challenge the analyses constructively.

Identify:

1. The strongest weakness in the idea
2. The weakest assumption
3. Important customer concerns
4. Important business concerns
5. Important technical concerns
6. Contradictions or disagreements between the analyses
7. Missing information or overlooked risks
8. Specific improvements that should be made

For every important criticism, explain:

- What is the problem?
- Why could it be a problem?
- What should the team do about it?

Be constructive rather than simply negative.

Do not invent statistics.
Do not claim that live web research was performed.
Clearly distinguish assumptions from conclusions.
""",
        expected_output="""
A structured Challenger analysis containing:

- Strongest weaknesses
- Weak assumptions
- Customer concerns
- Business concerns
- Technical concerns
- Disagreements
- Missing considerations
- Specific recommended improvements
""",
        agent=agent,
        context=[
            market_task,
            business_task,
            technical_task,
        ],
    )
```

