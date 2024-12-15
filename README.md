# Latex Resume Generator

- Heard about Jake's resume but don't know how to use Latex?
- This web app lets you use drag and drop tools for the same purpose!
- And you can get a latex file back!

The JSON file should follow this structure:
```json
{
    "font": "fira",
    "font_size": 12,
    "personal_info": {
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
    },
    "education": [
        {
            "school": "Northeastern University",
            "time": "Expected Graduation: December 2026",
            "degree": "Bachelor of Science in Computer Science",
            "location": "Boston, MA",
            "details": [
                "Major GPA: 3.95",
                "Coursework: Machine Learning & Artificial Intelligence, 4% acceptance rate"
            ]
        },
        {
            "school": "Unknown",
            "time": "Expected Graduation: December 2026",
            "degree": "Master of Science in Computer Science",
            "location": "Boston, MA",
            "details": [
                "Major GPA: 3.952",
                "Coursework: Machine Learning & Artificial Intelligence, 4% acceptance rate"
            ]
        }
    ],
    "projects": [
        {
            "title": "Project 1",
            "subtitle": "Subtitle",
            "time": "January 2022 - March 2022",
            "details": [
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nunc nec ultricies.",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nunc nec ultricies."
            ],
            "technologies": ["Python", "Docker", "Kubernetes"]
        },
        {
            "title": "Project 2",
            "time": "April 2022 - June 2022",
            "details": [
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nunc nec ultricies.",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nunc nec ultricies."
            ],
            "technologies": ["React", "Node.js", "MongoDB"]
        }
    ],
    "skills": [
        {
            "title": "Languages",
            "items": ["Python", "Java", "JavaScript", "C++", "C", "SQL"]
        },
        {
            "title": "Technologies",
            "items": [
                "React",
                "Node.js",
                "Express",
                "MongoDB",
                "Docker",
                "Kubernetes"
            ]
        }
    ],
    "interests": [
        "Machine Learning",
        "Artificial Intelligence",
        "Software Engineering",
        "Web Development"
    ]
}
```