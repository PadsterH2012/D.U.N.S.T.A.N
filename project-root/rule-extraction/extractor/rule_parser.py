import PyPDF2

class RuleParser:
    def parse_rules(self, pdf_path):
        rules = []
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                rules.append(page.extract_text())
        return rules