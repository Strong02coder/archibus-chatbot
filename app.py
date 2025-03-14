import streamlit as st  # Importing Streamlit library for creating web apps
import google.generativeai as genai  # Importing Google's Generative AI library


# Fetch the API key from the secrets file
api_key = st.secrets['defaults']['GOOGLE_API_KEY']
# Configure the Generative AI with the API key
genai.configure(api_key=api_key)

# Define generation parameters for the AI model
generation_config = {
    "temperature": 1,  # Controls the randomness of the output
    "top_p": 0.95,  # Controls the diversity of the output
    "top_k": 40,  # Limits the sampling pool to the top k tokens
    "max_output_tokens": 8192,  # Maximum number of tokens in the output
    "response_mime_type": "text/plain",  # MIME type of the response
}

# Base system instruction for the AI assistant
base_instruction = """
You are a professional AI assistant for Archibus.

Your name is Archibus AI.

Please answer user questions according to the following rules:

1. Questions related to Archibus: Explain specific functions and operation methods

2. Facility management, maintenance, and cost data: Provide accurate analysis and guidance

3. Workflow automation: Change appropriate data based on command input

4. Integration functions (Slack, Teams, Email): Explain how to link

5. Learning ability: Utilize past question history to provide more appropriate answers

Always answer concisely and accurately, and speak in Japanese.

"""

# Load custom instruction from file
with open("Data.txt", "r") as file:
    custom_instruction = file.read().strip()

# Combine static system instruction with custom instruction
full_instruction = f"{base_instruction}\n\n{custom_instruction}"

# Store the combined instruction in session state (without displaying it)
if "custom_instruction" not in st.session_state:
    st.session_state.custom_instruction = full_instruction

# Create the GenerativeModel instance with the combined instructions
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    system_instruction=st.session_state.custom_instruction,  # Pass combined instruction
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to display chat history
def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Function to handle user input and get assistant response
def handle_user_input(prompt: str):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            conversation_history = [
                {"role": message["role"], "parts": [message["content"]]}
                for message in st.session_state.messages
            ]

            try:
                # Start chat with system instruction (without displaying it)
                chat_session = model.start_chat(history=conversation_history)
                response = chat_session.send_message(prompt)

                # Display and store assistant response
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.messages.append({"role": "assistant", "content": "Sorry, an error occurred."})

# Main function for Streamlit app
def main():
    st.set_page_config(page_title="Archibus AI", layout="wide")
    st.title("Archibus AI")
    st.markdown("Welcome to Archibus AI")

    # Display chat history
    display_chat_history()

    # Handle user input
    if prompt := st.chat_input("Ask me anything..."):
        handle_user_input(prompt)

if __name__ == "__main__":
    main()
