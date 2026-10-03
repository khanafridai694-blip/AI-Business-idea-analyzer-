from crewai import Agent


def create_manager_agent(llm):
    return Agent(
        role="Startup Team Manager",
        goal=(
            "Coordinate the specialist analyses, evaluate the debate, "
            "resolve important disagreements, and create a practical "
            "improved startup plan."
        ),
        backstory=(
            "You are an experienced startup team manager. "
            "You combine different specialist opinions into one clear plan. "
            "You prioritize practical recommendations over exaggerated claims."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
