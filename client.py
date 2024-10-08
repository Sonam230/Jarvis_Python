from openai import OpenAI

client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a virtual assistant skilled in general tasks like Alexa and Google cloud."},
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message)

