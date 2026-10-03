import streamlit as st


def show_agent_status(statuses):
    st.subheader("🤖 AI Team")

    columns = st.columns(5)

    agents = [
        ("🧠", "Manager"),
        ("🔎", "Market"),
        ("💰", "Business"),
        ("💻", "Technical"),
        ("⚔️", "Challenger"),
    ]

    for column, (icon, name) in zip(columns, agents):
        with column:
            state = statuses.get(name, "Waiting")

            if state == "Completed":
                symbol = "🟢"
            elif state == "Working":
                symbol = "🟡"
            else:
                symbol = "⚪"

            st.markdown(
                f"""
                **{icon} {name}**

                {symbol} {state}
                """
            )


def show_debate(debate):
    st.subheader("⚔️ AI Debate")

    st.markdown(debate)


def show_final_plan(final_plan):
    st.subheader("🚀 Improved Startup Plan")

    st.markdown(final_plan)
