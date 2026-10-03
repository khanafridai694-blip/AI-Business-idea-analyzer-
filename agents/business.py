from crewai import Agent


def create_business_agent(llm):
    return Agent(
        role="Business Strategist",
        goal=(
            "Analyze how the idea could become a sustainable business. "
            "Define the value proposition, possible revenue models, "
            "business opportunities, and business risks."
        ),
        backstory=(
            "You are a startup business strategist. "
            "You focus on practical business models and customer value. "
            "You avoid unrealistic revenue claims."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
