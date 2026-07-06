import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key="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"
)

st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")

st.title("🎓 AI Learning Buddy")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."
        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."
        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions with answers on {topic}."
        else:
            prompt = topic

        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
        )

        st.write(response.choices[0].message.content)
