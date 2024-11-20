import openai
import os

# Initialize OpenAI API key
API_KEY = 'sk-7XD_SRlQVTSFdwWJyxtQj4joNe05oSRzLoQ1jE5Q3cT3BlbkFJOv3QnPzVPzkWrKWGHXtP9G64dkD58s2wz_dSQyTEYA'  # Ensure your API key is set in the environment variables

# Initialize message history for the conversation
message_history = []

client = openai.OpenAI(api_key= API_KEY)
openAI_model = 'gpt-4o-mini'
# Define the system prompt to guide the assistant's behavior
system_prompt = (
    "You are a helpful assistant that provides culturally significant information about specific regions. "
    "When given a region, you should return detailed cultural information about that region, such as traditions, "
    "historical sites, festivals, cuisine, and local customs. "
    "Personalize your response based on the user's preferences provided."
)

# Append the system prompt to the message history
message_history.append({"role": "system", "content": system_prompt})


def get_model():
    completion = client.chat.completions.create(
        model= openAI_model,
        messages= message_history,
        # temperature= temperature,
        # max_tokens= max_tokens,
    )
    return completion

def user_pref():
    """
    Retrieve the user's preferences.
    
    This is a placeholder function. In a real application, this function would retrieve
    the user's preferences from a database or user input.
    """
    # Example user preferences
    return "I enjoy historical sites, traditional music, and local cuisine."

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

    return assistant_message

def new_message(message):
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

# Example usage:
if __name__ == "__main__":
    # Retrieve user preferences and define the region
    userPreferences = user_pref()
    region = "Kyoto, Japan"

    # Get the personalized cultural information
    cultural_info = get_cultural_information(userPreferences, region)
    print("Cultural Information:")
    print(cultural_info)
    print()

    # Continue the conversation with a new message
    follow_up = "Can you tell me more about the local festivals?"
    response = new_message(follow_up)
    print("Assistant Response:")
    print(response)