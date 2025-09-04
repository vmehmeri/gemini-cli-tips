from google.adk import Agent

# Create a simple agent
hello_agent = Agent(
    name='hello_agent',
    instruction='You are a friendly agent that says "Hello, World!".'
)

# Interact with the agent
response = hello_agent.process('Say hi')

# Print the response
print(response.text)
