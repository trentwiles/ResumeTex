import json
import requests
from resume.resume_maker import ResumeMaker

# def generate_resume(json_file, output_file="resume.pdf"):
#     try:
#         with open(json_file, "r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         print(f"Error: The file {json_file} was not found.")
#         return
#     except json.JSONDecodeError:
#         print(f"Error: The file {json_file} contains invalid JSON.")
#         return

#     url = "https://resumetex.asahoo.dev/api/v1/pdf"

#     try:
#         headers = {"Content-Type": "application/json"}
#         response = requests.post(url, json=data, headers=headers)

#         if response.status_code == 200:
#             with open(output_file, "wb") as pdf_file:
#                 pdf_file.write(response.content)
#             print(f"PDF successfully saved as {output_file}")
#         else:
#             print(f"Failed to generate resume. Status code: {response.status_code}")
#             print(f"Response: {response.text}")
#     except requests.RequestException as e:
#         print(f"An error occurred while making the request: {e}")


# if __name__ == "__main__":
#     json_file_name = "sample_input.json"
#     output_pdf_name = "resume.pdf"
#     generate_resume(json_file_name, output_pdf_name)
#     json_file_name = "sample_input_pagebreak.json"
#     output_pdf_name = "resume2.pdf"
#     generate_resume(json_file_name, output_pdf_name)
#     json_file_name = "sample_input_bad_col.json"
#     output_pdf_name = "resume3.pdf"
#     generate_resume(json_file_name, output_pdf_name)

with open('sample_input.json') as f:
    jsonfile = json.load(f)
print(ResumeMaker().generate_latex(jsonfile))