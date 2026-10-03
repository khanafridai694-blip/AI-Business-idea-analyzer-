from crewai import Agent


def create_market_agent(llm):
    return Agent(
        role="Market Analyst",
        goal=(
            "Analyze the user's idea from the customer and market perspective. "
            "Identify the target customers, problem being solved, competitors, "
            "market opportunity, and important assumptions."
        ),
        backstory=(
            "You are a practical market analyst. "
            "You focus on customers, competition, demand, and market risks. "
            "You do not invent specific market statistics."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
