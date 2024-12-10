from PyPDF2 import PdfReader


class ExtractRequirementsFileUseCase:
    def execute(self, file):
        reader = PdfReader(file)
        text = ""
        print(reader.pages[0])
        text = reader.pages[0].extract_text()
        return [text]