import openai
import sys

# dotenv.load_dotenv()
# Initialize OpenAI API key

# Initialize message history for the conversation
message_history = []
openAI_API = 'insert key here'
client = openai.OpenAI(api_key= openAI_API)
openAI_model = 'gpt-4o-mini'
# Define the system prompt to guide the assistant's behavior
system_prompt = (
    "You are a helpful assistant that provides culturally significant information about specific regions. "
    "When given a region, you should return detailed cultural information about that region, such as traditions, "
    "historical sites, festivals, cuisine, and local customs. "
    "Personalize your response based on the user's preferences provided."
)


def get_model():
    completion = client.chat.completions.create(
        model= openAI_model,
        messages= message_history,
        # temperature= temperature,
        # max_tokens= max_tokens,
    )
    return completion

def new_message(all_messages, message):
    """
    Continue communicating with the model after the initial cultural information summary.
    
    Parameters:
    - message (str): The user's message to the assistant.
    
    Returns:
    - str: The assistant's response.
    """
    global message_history

    # Append the user's message to the message history
    message_history.append({"role": "user", "content": message})

    # Call the OpenAI API to get the assistant's response
    response = get_model()

    # Extract the assistant's reply
    # assistant_message = response['choices'][0]['message']['content']
    assistant_message = response.choices[0].message.content
    
    # Append the assistant's reply to the message history
    message_history.append({"role": "assistant", "content": assistant_message})

    return assistant_message



arguments = sys.argv[1:]

print(new_message(arguments[0], arguments[1]))