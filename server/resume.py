# %-------------------------
# % Resume in Latex
# % Author : Jake Gutierrez -> Modified by Anish Sahoo
# % Based off of: https://github.com/sb2nov/resume
# % License : MIT
# %------------------------

font_set = {
    'fira' : r'\usepackage[sfdefault]{FiraSans}', 
    'roboto': r'\usepackage[sfdefault]{roboto}',
    'noto-sans': r'\usepackage[sfdefault]{noto-sans}', 
    'sourcesanspro': r'\usepackage[default]{sourcesanspro}', 
    'cormorantgaramond': r'\usepackage{CormorantGaramond}', 
    'charter': r'\usepackage{charter}',
    '': ''
}

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
    
    def add_section(self, section):
        self.code += section.code
    
    def add_skill(self, skill):
        self.code += skill.code
    
    def add_work_experience(self, work_experience):
        self.code += work_experience.code
        
    def add_custom_section(self, custom_section):
        self.code += custom_section.code
        
    def get_complete_latex(self):
        return self.preamble + r"\begin{document}" + self.code + r"\end{document}"
    
    
if __name__ == '__main__':
    resume = Resume(font_size=11, font='fira')
    print(resume.get_complete_latex())