## Medical Student Chatbot
This project is a chatbot designed for medical students, built using Meta's LLaMA 2-7B chat model. The bot answers medical queries by leveraging a large language model, with an interactive user interface developed using Streamlit.

### Features
Real-time Medical Query Responses: Medical students can input questions and receive answers instantly.
Powered by Meta LLaMA 2-7B: The chatbot is built using the Meta LLaMA 2-7B model, ensuring high-quality responses.
Streamlit Interface: The app provides an intuitive web interface for user interaction.
Setup Instructions

#### 1. Clone the Repository
Clone the repository or copy the project files to your local machine.
#### 2. Install Dependencies
Install the required Python packages by running the following command:
pip install torch transformers streamlit
#### 3. Run the Streamlit App
Once dependencies are installed, you can start the Streamlit app using the following command:
streamlit run <your_script_name>.py

Replace <your_script_name> with the name of the script file that contains your code.
#### 4. Load the Model
The LLaMA 2-7B chat model will automatically load when you run the app. Ensure you have sufficient memory to load the model.
#### 5. Interact with the Chatbot
Once the app runs, you can interact with the chatbot by typing medical-related queries in the chat input box. The bot will respond based on the LLaMA model's knowledge.

#### Example Usage
1. Launch the app using Streamlit.
2. Type your medical question, such as:
"What are the symptoms of a heart attack?"
3.The chatbot will generate a response using the LLaMA model.

## Customization
- Modify the generate_response function to adjust the response length, sampling method, or other parameters based on your requirements.
You can also tweak the Streamlit interface to better suit your use case or add additional features like saving conversations.

## License
This project is for educational purposes and uses Meta's LLaMA 2 model. Make sure to comply with the licensing terms of both Meta and Hugging Face.
