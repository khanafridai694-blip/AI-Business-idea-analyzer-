from crewai import Task


def create_market_task(agent):
    return Task(
        description="""
Analyze the following startup/product idea:

{idea}

Provide:
1. Target customers
2. Customer problem
3. Proposed value
4. Possible competitors or alternatives
5. Market opportunity
6. Important assumptions
7. Market risks

Use reasoning based on the idea itself.
Do not invent exact statistics or claim that you performed live web research.
""",
        expected_output="A structured market analysis.",
        agent=agent,
    )


def create_business_task(agent):
    return Task(
        description="""
Analyze this startup/product idea:

{idea}

Provide:
1. Value proposition
2. Possible revenue models
3. Customer acquisition approach
4. Business opportunities
5. Business risks
6. What could make the idea difficult to monetize

Keep the analysis practical.
""",
        expected_output="A structured business analysis.",
        agent=agent,
    )


def create_technical_task(agent):
    return Task(
        description="""
Evaluate the technical feasibility of this idea:

{idea}

Provide:
1. MVP features
2. Recommended technology stack
3. Main system components
4. AI requirements, if any
5. Technical risks
6. Simplest realistic implementation approach

Do not over-engineer the solution.
""",
        expected_output="A structured technical feasibility analysis.",
        agent=agent,
    )
