from crewai import Agent


def create_challenger_agent(llm):
    return Agent(
        role="Critical Challenger",
        goal=(
            "Challenge the market, business, and technical analyses. "
            "Find weak assumptions, missing information, customer problems, "
            "business risks, technical risks, and reasons the idea could fail."
        ),
        backstory=(
            "You are a constructive critic. "
            "Your job is not to reject ideas without reason. "
            "Your job is to identify important weaknesses and propose "
            "specific improvements."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
