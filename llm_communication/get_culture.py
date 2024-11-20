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

def get_cultural_information(userPreferences, region):
    """
    Return culturally significant information about the given region, personalized to the user.
    
    Parameters:
    - userPreferences (str): The user's preferences.
    - region (str): The specific region to get information about.
    
    Returns:
    - str: The culturally significant information about the region.
    """
    global message_history
    global attractions

    # Construct the user's message
    user_message = (
        f"Please provide culturally significant information about {region}. "
        f"Personalize it based on the following user preferences: {userPreferences}"
    )
    

    # Append the user's message to the message history
    message_history.append({"role": "user", "content": user_message})

    # Call the OpenAI API to get the assistant's response
    response = get_model()

    # Extract the assistant's reply
    # assistant_message = response['choices'][0]['message']['content']
    assistant_message = response.choices[0].message.content

    # Append the assistant's reply to the message history
    message_history.append({"role": "assistant", "content": assistant_message})
    
    
    summary_prompt = ("your response should only include the main attractions without any other text, mentioning them by name. You should follow this notation [*Attraction1*, *Attraction2*]")
    message_history.append({"role": "user", "content": summary_prompt})
    
    response = get_model()
    
    attractions = response.choices[0].message.content
    
    message_history.pop()

    return assistant_message



arguments = sys.argv[1:]

print(get_cultural_information(arguments[0], arguments[1]))