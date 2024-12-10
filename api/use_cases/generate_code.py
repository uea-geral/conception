from openai import OpenAI
from use_cases.alpaca_prompt import AlpacaPrompt

client = OpenAI(
    base_url='http://localhost:1234/v1',
    api_key='lm-studio'
)

class GenerateCodeUseCase:
    def execute(self, requirements, last_code = ""):
        prompt_template = AlpacaPrompt()
        input_template = f"""
        #### Requirements:
        {",".join(requirements)}
        
        #### Last Code:
        {last_code}
        """
        prompt = prompt_template.build(
            'Generate a HTML,CSS,JS code based on the specific requirements. Just return the code directly.',
            input=input_template)
        completion = client.chat.completions.create(
        model="qwen2.5-coder-3b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7)
        code = completion.choices[0].message
        return code.content.replace('```html', '').replace('```', '')   