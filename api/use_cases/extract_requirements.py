from openai import OpenAI
from use_cases.alpaca_prompt import AlpacaPrompt

client = OpenAI(
    base_url='http://localhost:1234/v1',
    api_key='lm-studio'
)

TOKEN = "[END_OF_REQ]"

class ExtractRequirementsUseCase:
    def execute(self, prompt):
        prompt_template = AlpacaPrompt()
        prompt = prompt_template.build(
            f'Extract the features of this software. Divide each feature using the token {TOKEN}',
            input=prompt)
        completion = client.chat.completions.create(
        model="qwen2.5-coder-3b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7)
        code = completion.choices[0].message
        return code.content.split(TOKEN)