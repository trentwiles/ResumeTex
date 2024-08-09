# %-------------------------
# % Resume in Latex
# % Author : Jake Gutierrez -> Modified by Anish Sahoo
# % Based off of: https://github.com/sb2nov/resume
# % License : MIT
# %------------------------

import os

font_set = {
    'fira' : r'\usepackage[sfdefault]{FiraSans}', 
    'roboto': r'\usepackage[sfdefault]{roboto}',
    'noto-sans': r'\usepackage[sfdefault]{noto-sans}', 
    'sourcesanspro': r'\usepackage[default]{sourcesanspro}', 
    'cormorantgaramond': r'\usepackage{CormorantGaramond}', 
    'charter': r'\usepackage{charter}',
    '': ''
}

def latexify(text: str) -> str:
    text = text.replace('\\', r'\textbackslash')\
        .replace('&', r'\&')\
        .replace('%', r'\%')\
        .replace('$', r'\$')\
        .replace('#', r'\#')\
        .replace('_', r'\_')\
        .replace('{', r'\{')\
        .replace('}', r'\}')\
        .replace('~', r'\textasciitilde')\
        .replace('^', r'\^')
        
    
    return r"{}".format(text)

class Resume:
    def __init__(self, **kwargs):
        font_size = kwargs.get('font_size', 11)
        font = kwargs.get('font', '')
        
        self.preamble = r"""
\documentclass[letterpaper,""" + str(font_size) + r"""pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[american]{babel}
\usepackage{tabularx}
\input{glyphtounicode}

""" + font_set[font] + r"""

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
\vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
\item\small{
    {#1 \vspace{-2pt}}
}
}

\newcommand{\resumeSubheading}[4]{
\vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
    \textbf{#1} & #2 \\
    \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubheadingSmall}[2]{
\vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
    \textbf{#1} & #2 \\
    \end{tabular*}\vspace{-9pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
    \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
    \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
        self.code = ""
    
    '''
    Example input:
    {
        "name": "Anish Sahoo",
        "phone": "123-456-7890",
        "email": "anish@email.email",
        "links": [
            {
                "url": "https://www.linkedin.com/in/anish-sahoo",
                "text": "linkedin.com/in/anish-sahoo"  
            }, 
            {
                "url": "https://asahoo.dev"
                "text": "asahoo.dev"
            }
        ]
    }
    '''
    def add_personal_info(self, personal_info):
        name = latexify(personal_info.get('name', ''))
        phone = latexify(personal_info.get('phone', ''))
        email = latexify(personal_info.get('email', ''))
        links = personal_info.get('links', [])
        
        self.code += r"\begin{center}" + os.linesep
        
        if name != '':
            self.code += r"\textbf{\Huge \scshape " + name + r"} \\ \vspace{1pt}" + os.linesep
        
        if phone != '':
            self.code += r"\small " + phone + r" $|$ " + os.linesep
        
        if email != '':
            self.code += r"\href{mailto:" + email + r"}{\underline{" + email + r"}} $|$ " + os.linesep
        
        for link in links:
            self.code += r"\href{" + latexify(link['url']) + r"}{\underline{" + latexify(link['text']) + r"}} $|$ " + os.linesep
        
        self.code += r"\end{center}" + os.linesep
        
    '''
    Example input:
    [
        {
            "school": 'Northeastern University',
            "time": 'Expected Graduation: December 2026',
            "degree": 'Bachelor of Science in Computer Science',
            "location": 'Boston, MA',
            "details": [
                'Major GPA: 3.95',
                'Coursework: Machine Learning, Artificial Intelligence',
            ],
        }
    ]'''
    def add_education(self, education):
        self.code += os.linesep + r"\section{Education}" + os.linesep
        self.code += r"\resumeSubHeadingListStart" + os.linesep
        tabs = 0
        for edu in education:
            tabs += 4
            self.code += r"\resumeSubheading" \
                + r"{" + latexify(edu['school'] or '') + r"}"  \
                + r"{" + latexify(edu['time'] or '') + r"}" \
                + r"{" + latexify(edu['degree'] or '') + r"}" \
                + r"{" + latexify(edu['location'] or '') + r"}" \
                + os.linesep        
            tabs -= 4
            self.code += r"\resumeItemListStart" + os.linesep
            tabs += 4
            for item in edu['details']:
                self.code += (" "*tabs) + r"\resumeItem{" + latexify(item) + r"}" + os.linesep
            tabs -= 4
            self.code += r"\resumeItemListEnd" + os.linesep
    
        self.code += r"\resumeSubHeadingListEnd" + os.linesep
    
    '''
    Sample input:
    [
        {
            "company": "Company",
            "jobs": [
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "location": "Boston, MA",
                    "details": [
                        "Developed a web application to manage data",
                        "Implemented a feature to allow users to upload files"
                    ]
                }
            ]
        },
        {
            "company": "Company",
            "jobs": [
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "details": [
                        "Developed a web application to manage data",
                        "Implemented a feature to allow users to upload files"
                    ]
                },
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "details": [
                        "Developed a web application to manage data",
                    ]
                }
            ]
        }
    ]
    '''
    def add_work_experience(self, work_experience):
        self.code += os.linesep + r"\section{Experience}" + os.linesep
        self.code += r"\resumeSubHeadingListStart" + os.linesep
        tabs = 0
        for exp in work_experience:
            if len(exp['jobs']) > 1:
                self.code += r"\resumeSubheadingSmall" \
                    + r"{" + latexify(exp['company'] or '') + r"}"  \
                    + r"{" + latexify(exp['jobs'][0]['time'] or '') + r"}"
                self.code += os.linesep
                for job in exp['jobs']:
                    tabs += 4
                    self.code += r"\resumeSubSubheading" \
                        + r"{" + latexify(job['title'] or '') + r"}"  \
                        + r"{" + latexify(job['time'] or '') + r"}" \
                        + os.linesep
                    self.code += r"\resumeItemListStart" + os.linesep
                    tabs += 4
                    for item in job['details']:
                        self.code += (" "*tabs) + r"\resumeItem{" + latexify(item) + r"}" + os.linesep
                    tabs -= 4
                    self.code += r"\resumeItemListEnd" + os.linesep
                    tabs -= 4
            else:
                job = exp['jobs'][0]
                self.code += r"\resumeSubheading" \
                    + r"{" + latexify(exp['company'] or '') + r"}"  \
                    + r"{" + latexify(job['time'] or '') + r"}" \
                    + r"{" + latexify(job['title'] or '') + r"}" \
                    + r"{" + latexify(job['location'] or '') + r"}" \
                    + os.linesep
                self.code += r"\resumeItemListStart" + os.linesep
                tabs += 4
                for item in job['details']:
                    self.code += (" "*tabs) + r"\resumeItem{" + latexify(item) + r"}" + os.linesep
                tabs -= 4
                self.code += r"\resumeItemListEnd" + os.linesep
            
            self.code += os.linesep
        
        self.code += r"\resumeSubHeadingListEnd" + os.linesep
    
    def add_page_break(self):
        self.code += r"\pagebreak" + os.linesep
        
    def get_complete_latex(self):
        return self.preamble + r"\begin{document}"\
            + os.linesep + self.code + os.linesep + r"\end{document}"
    
if __name__ == '__main__':
    resume = Resume(font_size=11, font='fira')
    resume.add_personal_info({
        "name": "Anish Sahoo",
        "phone": "123-456-7890",
        "email": "anish@email.email",
        "links": [
            {
                "url": "https://www.linkedin.com/in/anish-sahoo",
                "text": "linkedin.com/in/anish-sahoo"  
            }, 
            {
                "url": "https://asahoo.dev",
                "text": "asahoo.dev"
            }
        ]
    })
    resume.add_education([
        {
            "school": 'Northeastern University',
            "time": 'Expected Graduation: December 2026',
            "degree": 'Bachelor of Science in Computer Science',
            "location": 'Boston, MA',
            "details": [
                'Major GPA: 3.95',
                'Coursework: Machine Learning & Artificial Intelligence, 4% acceptance rate',
            ],
        },
        {
            "school": 'Unknown',
            "time": 'Expected Graduation: December 2026',
            "degree": 'Master of Science in Computer Science',
            "location": 'Boston, MA',
            "details": [
                'Major GPA: 3.952',
                'Coursework: Machine Learning & Artificial Intelligence, 4% acceptance rate',
            ],
        }
    ])
    resume.add_work_experience([
        {
            "company": "Company",
            "jobs": [
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "location": "Boston, MA",
                    "details": [
                        "Developed a web application to manage data",
                        "Implemented a feature to allow users to upload files"
                    ]
                }
            ]
        },
        {
            "company": "Company",
            "jobs": [
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "details": [
                        "Developed a web application to manage data",
                        "Implemented a feature to allow users to upload files"
                    ]
                },
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "details": [
                        "Developed a web application to manage data",
                    ]
                }
            ]
        }
    ])
    print(resume.get_complete_latex())