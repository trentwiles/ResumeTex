from resume.resume_maker import ResumeMaker

import json

if __name__ == "__main__":
    with open("sample_input.json", "r") as file:
        data = json.load(file)
    print(type(data))
    maker = ResumeMaker()
    print(maker.generate_latex(data))
    print(maker.generate_pdf(data))
    ResumeMaker.clean_up_temp_files()
