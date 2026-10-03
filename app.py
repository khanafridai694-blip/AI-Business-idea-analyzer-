import os

import streamlit as st

from crew.agentforge_crew import run_agentforge
from utils.ui import (
    show_agent_status,
    show_debate,
    show_final_plan,
)


st.set_page_config(
    page_title="AgentForge",
    page_icon="🚀",
    layout="wide",
)


def load_groq_key():
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
        return

    if os.getenv("GROQ_API_KEY"):
        return

    raise ValueError("GROQ_API_KEY is not configured.")


st.title("🚀 AgentForge")
st.caption("Your AI team for turning ideas into stronger startup plans.")

st.markdown(
    """
Enter any startup, product, app, SaaS, AI, or business idea.
AgentForge will analyze it from multiple perspectives, challenge the
idea, and produce an improved plan.
"""
)

idea = st.text_area(
    "💡 Describe your idea",
    placeholder=(
        "Example: I want to build an AI tool that helps small "
        "restaurants reduce food waste."
    ),
    height=150,
)

analyze = st.button(
    "🚀 Analyze My Idea",
    type="primary",
    use_container_width=True,
)


if analyze:
    if not idea.strip():
        st.warning("Please enter an idea first.")
        st.stop()

    try:
        load_groq_key()
    except ValueError as error:
        st.error(str(error))
        st.stop()

    statuses = {
        "Manager": "Waiting",
        "Market": "Working",
        "Business": "Working",
        "Technical": "Working",
        "Challenger": "Waiting",
    }

    show_agent_status(statuses)

    with st.spinner("AI team is analyzing your idea..."):
        try:
            result = run_agentforge(idea)
        except Exception as error:
            st.error(
                "The analysis could not be completed. "
                "Check your Groq API key and package installation."
            )
            st.exception(error)
            st.stop()

    statuses = {
        "Manager": "Completed",
        "Market": "Completed",
        "Business": "Completed",
        "Technical": "Completed",
        "Challenger": "Completed",
    }

    show_agent_status(statuses)

    st.divider()

    with st.expander("🔎 Market Agent Analysis"):
        st.markdown(result["market"])

    with st.expander("💰 Business Agent Analysis"):
        st.markdown(result["business"])

    with st.expander("💻 Technical Agent Analysis"):
        st.markdown(result["technical"])

    st.divider()

    show_debate(result["debate"])

    st.divider()

    show_final_plan(result["final"])
