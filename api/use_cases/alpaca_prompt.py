class AlpacaPrompt:
    def build(self, instruction: str, input: str):
        prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request
        ### Instruction:
        {}
        
        ### Input:
        {}
        
        ### Response:
        """
        return prompt.format(instruction, input)