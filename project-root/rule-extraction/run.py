from extractor.rule_parser import RuleParser

def process_uploaded_file(file_path):
    rule_parser = RuleParser()
    return rule_parser.parse_rules(file_path)

if __name__ == "__main__":
    pdf_path = "/app/uploads/your_uploaded_file.pdf"  # This is just an example
    print(process_uploaded_file(pdf_path))
