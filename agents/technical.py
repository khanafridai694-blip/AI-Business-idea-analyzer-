from crewai import Agent


def create_technical_agent(llm):
    return Agent(
        role="Technical Architect",
        goal=(
            "Evaluate whether the idea can be technically implemented. "
            "Recommend a practical technology stack, define the MVP "
            "technical requirements, and identify technical risks."
        ),
        backstory=(
            "You are a software architect who specializes in turning "
            "startup ideas into realistic MVPs. "
            "You prefer simple and maintainable technology choices."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
