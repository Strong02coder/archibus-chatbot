# Archibus AI Chatbot

Welcome to the Archibus AI Chatbot project! This project leverages Streamlit and Google's Generative AI to create an intelligent assistant for Archibus. The assistant can answer questions related to Archibus, facility management, workflow automation, and integration functions, and it speaks in Japanese.

## Features

- **Archibus Functionality**: Explains specific functions and operation methods.
- **Facility Management**: Provides accurate analysis and guidance on maintenance and cost data.
- **Workflow Automation**: Changes appropriate data based on command input.
- **Integration Functions**: Explains how to link with Slack, Teams, Email, etc.
- **Learning Ability**: Utilizes past question history to provide more appropriate answers.

## Project Structure

```
.gitignore
app.py
Data.txt
requirements.txt
.streamlit/
    secrets.toml
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/archibus-chatbot.git
    cd archibus-chatbot
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your API keys**:
    - Add your Google API key to the `.streamlit/secrets.toml` file:
        ```toml
        [defaults]
        GOOGLE_API_KEY = "your-google-api-key"
        ```

4. **Add custom instructions**:
    - Add your custom instructions to the `Data.txt` file.

### Running the Application

To run the Streamlit application, use the following command:

```sh
streamlit run app.py
```

This will start the Streamlit server, and you can interact with the Archibus AI assistant through the web interface.

## Usage

- Open the Streamlit app in your browser.
- Ask any questions related to Archibus, facility management, workflow automation, or integration functions.
- The assistant will respond in Japanese, providing concise and accurate answers.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai)
