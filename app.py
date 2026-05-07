import streamlit as st
import ollama

st.set_page_config(
    page_title="Gemma-Rescue Edge",
    layout="centered"
)

st.title("🚨 Gemma-Rescue Edge")

st.markdown(
    "Offline AI-powered disaster rescue assessment system"
)

thermal = st.slider(
    "Thermal Reading (°C)",
    30,
    45,
    38
)

movement = st.selectbox(
    "Movement Level",
    [
        "none",
        "low",
        "moderate",
        "high"
    ]
)

environment = st.selectbox(
    "Environment",
    [
        "earthquake rubble",
        "collapsed building",
        "flood zone",
        "wildfire area",
        "landslide area",
        "safe evacuation zone"
    ]
)

if st.button("Analyze Victim"):

    prompt = f"""
    Analyze this disaster victim.

    Respond ONLY in this format:

    Priority:
    Condition:
    Action:

    Thermal Reading: {thermal}C
    Movement: {movement}
    Environment: {environment}
    """

    with st.spinner("Analyzing victim condition..."):

        response = ollama.chat(
            model="gemma-rescue-edge",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response["message"]["content"]

        # Clean response
        lines = result.split("\n")

        cleaned_lines = []

        for line in lines:

            if (
                "Priority" in line or
                "Condition" in line or
                "Action" in line
            ):
                cleaned_lines.append(line)

        cleaned_result = "\n".join(cleaned_lines[:3])

    st.subheader("🚑 Rescue Assessment")

    st.success(cleaned_result)