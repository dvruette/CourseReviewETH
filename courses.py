import json
import requests

STATIC_COURSES = [
    {
        "number": "263-5056-00L",
        "name": "Applications of Deep Learning on Graphs"
    },
    {
        "number": "252-3400-00L",
        "name": "Seminar on Machine Learning Systems"
    },
    {
        "number": "252-0463-00L",
        "name": "Security Engineering"
    },
    {
        "number": "252-0543-01L",
        "name": "Computer Graphics"
    },
    {
        "number": "263-3210-00L",
        "name": "Deep Learning"
    },
    {
        "number": "263-2520-00L",
        "name": "Formal Foundations of Programming Languages"
    },
    {
        "number": "252-5051-00L",
        "name": "Advanced Topics in Machine Learning"
    },
    {
        "number": "401-3628-14L",
        "name": "Bayesian Statistics"
    },
    {
        "number": "263-4657-00L",
        "name": "Advanced Encryption Schemes"
    },
    {
        "number": "263-4640-00L",
        "name": "Network Security"
    },
    {
        "number": "227-0417-00L",
        "name": "Information Theory I"
    },
    {
        "number": "851-0762-00L",
        "name": "Computational Social Science with Images and Audio"
    },
    {
        "number": "851-0760-00L",
        "name": "Building a Robot Judge: Data Science for Decision-Making"
    },
    {
        "number": "401-0674-AAL",
        "name": "Numerical Methods for Partial Differential Equations"
    },
    {
        "number": "101-0250-00L",
        "name": "Solving Partial Differential Equations in Parallel on GPUs"
    },
    {
        "number": "252-2810-00L",
        "name": "Fundamentals of Web Engineering"
    },
    {
        "number": "363-0565-00L",
        "name": "Principles of Macroeconomics"
    },
    {
        "number": "252-1411-00L",
        "name": "Security of Wireless Networks"
    },
    {
        "number": "252-1414-00L",
        "name": "System Security"
    },
    {
        "number": "851-0251-00L",
        "name": "Psychedelic Science: Psychology, Pharmacology, Physiology Psychotherapy, Philosophy"
    },
    {
        "number": "151-0532-00L",
        "name": "Nonlinear Dynamics and Chaos I"
    },
    {
        "number": "227-2037-00L",
        "name": "Physical Modelling and Simulation"
    },
    {
        "number": "263-0009-00L",
        "name": "Information Security Lab"
    },
    {
        "number": "263-5352-00L",
        "name": "Advanced Formal Language Theory"
    },
    {
        "number": "402-0810-00L",
        "name": "Computational Quantum Physics"
    },
    {
        "number": "227-0579-00L",
        "name": "Hardware Security"
    },
    {
        "number": "252-0030-00L",
        "name": "Algorithmen und Wahrscheinlichkeit"
    },
    {
        "number": "401-0053-00L",
        "name": "Diskrete Mathematik"
    },
    {
        "number": "227-0447-00L",
        "name": "Image Analysis and Computer Vision"
    },
    {
        "number": "151-0709-00L",
        "name": "Stochastic Methods for Engineers and Natural Scientists"
    },
    {
        "number": "252-0408-00L",
        "name": "Cryptographic Protocols"
    },
    {
        "number": "263-4656-00L",
        "name": "Digital Signatures"
    },
    {
        "number": "401-3632-00L",
        "name": "Computational Statistics"
    },
    {
        "number": "263-5354-00L",
        "name": "Large Language Models"
    },
    {
        "number": "401-0131-00L",
        "name": "Lineare Algebra"
    },
    {
        "number": "851-0708-00L",
        "name": "Grundz\u00fcge des Rechts"
    },
    {
        "number": "252-5706-00L",
        "name": "Mathematical Foundations of Computer Graphics and Vision"
    },
    {
        "number": "252-0570-00L",
        "name": "Game Programming Laboratory"
    },
    {
        "number": "263-0008-00L",
        "name": "Computational Intelligence Lab"
    },
    {
        "number": "252-0546-00L",
        "name": "Physically-Based Simulation in Computer Graphics"
    },
    {
        "number": "261-5110-00L",
        "name": "Optimization for Data Science"
    },
    {
        "number": "851-0877-00L",
        "name": "Chinesisch I A1.1"
    },
    {
        "number": "401-0302-10L",
        "name": "Komplexe Analysis"
    },
    {
        "number": "252-0820-00L",
        "name": "Information Technology in Practice"
    },
    {
        "number": "851-0585-48L",
        "name": "Controversies in Game Theory"
    },
    {
        "number": "252-0535-00L",
        "name": "Advanced Machine Learning"
    },
    {
        "number": "263-2815-00L",
        "name": "Automated Software Testing"
    },
    {
        "number": "263-3850-00L",
        "name": "Informal Methods"
    },
    {
        "number": "401-0151-00L",
        "name": "Lineare Algebra"
    },
    {
        "number": "263-2400-00L",
        "name": "Reliable and Trustworthy Artificial Intelligence"
    },
    {
        "number": "401-2813-00L",
        "name": "Programming Techniques for Scientific Simulations I"
    },
    {
        "number": "401-2673-00L",
        "name": "Numerical Methods for CSE"
    },
    {
        "number": "851-0746-00L",
        "name": "Algorithms and Fairness"
    },
    {
        "number": "263-3710-00L",
        "name": "Machine Perception"
    },
    {
        "number": "252-0055-00L",
        "name": "Informationstheorie"
    },
    {
        "number": "860-0024-00L",
        "name": "Digital Society: Ethical, Societal and Economic Challenges"
    },
    {
        "number": "227-0731-00L",
        "name": "Power Market I - Portfolio and Risk Management"
    },
    {
        "number": "252-0232-00L",
        "name": "Software Engineering"
    },
    {
        "number": "701-0412-00L",
        "name": "Klimasysteme"
    },
    {
        "number": "263-5000-00L",
        "name": "Computational Semantics for Natural Language Processing"
    },
    {
        "number": "252-0216-00L",
        "name": "Rigorous Software Engineering"
    },
    {
        "number": "252-4102-00L",
        "name": "Seminar on Randomized Algorithms and Probabilistic Methods"
    },
    {
        "number": "252-0500-00L",
        "name": "Bachelor-Arbeit"
    },
    {
        "number": "252-5053-00L",
        "name": "What Kind of AI Do We Want? Bringing Artistic and Technological Practices Together"
    },
    {
        "number": "851-0252-13L",
        "name": "Network Modeling"
    },
    {
        "number": "853-0047-01L",
        "name": "Weltpolitik seit 1945: Geschichte der int. Beziehungen (ohne Uebungen)"
    },
    {
        "number": "851-0739-01L",
        "name": "Natural Language Processing for Law and Social Science"
    },
    {
        "number": "401-4623-00L",
        "name": "Time Series Analysis"
    },
    {
        "number": "401-3621-00L",
        "name": "Fundamentals of Mathematical Statistics"
    },
    {
        "number": "401-0353-00L",
        "name": "Analysis 3"
    },
    {
        "number": "851-0742-00L",
        "name": "Contract Design I"
    },
    {
        "number": "263-5902-00L",
        "name": "Computer Vision"
    },
    {
        "number": "263-0006-00L",
        "name": "Algorithms Lab"
    },
    {
        "number": "252-0237-00L",
        "name": "Concepts of Object-Oriented Programming"
    },
    {
        "number": "853-0038-00L",
        "name": "Schweizerische Aussenpolitik"
    },
    {
        "number": "376-1177-00L",
        "name": "Human Factors I"
    },
    {
        "number": "151-0317-00L",
        "name": "Visualization, Simulation and Interaction - Virtual Reality II"
    },
    {
        "number": "402-0209-00L",
        "name": "Quantum Physics for Non-Physicists"
    },
    {
        "number": "252-0025-01L",
        "name": "Diskrete Mathematik"
    },
    {
        "number": "227-0116-00L",
        "name": "VLSI 1: HDL Based Design for FPGAs"
    },
    {
        "number": "351-1158-00L",
        "name": "\u00d6konomie"
    },
    {
        "number": "227-0124-00L",
        "name": "Embedded Systems"
    },
    {
        "number": "263-5210-00L",
        "name": "Probabilistic Artificial Intelligence"
    },
    {
        "number": "401-3054-14L",
        "name": "Probabilistic Methods in Combinatorics"
    },
    {
        "number": "252-0417-00L",
        "name": "Randomized Algorithms and Probabilistic Methods"
    },
    {
        "number": "851-0727-02L",
        "name": "E-Business-Recht"
    },
    {
        "number": "853-0726-00L",
        "name": "Geschichte II: Global (Anti-Imperialismus und Dekolonisation, 1919-1975)"
    },
    {
        "number": "853-0725-00L",
        "name": "Geschichte I: Europa (Grossbritannien, Mutterland der Moderne, 1789-1914)"
    },
    {
        "number": "252-4225-00L",
        "name": "Presenting Theoretical Computer Science"
    },
    {
        "number": "851-0467-00L",
        "name": "From Traffic Modeling to Smart Cities and Digital Democracies"
    },
    {
        "number": "151-0854-00L",
        "name": "Autonomous Mobile Robots"
    },
    {
        "number": "263-5052-00L",
        "name": "Interactive Machine Learning: Visualization & Explainability"
    },
    {
        "number": "401-0663-00L",
        "name": "Numerical Methods for Computer Science"
    },
    {
        "number": "851-0738-00L",
        "name": "Geistiges Eigentum: Eine Einf\u00fchrung"
    },
    {
        "number": "252-2600-05L",
        "name": "Software Engineering Seminar"
    },
    {
        "number": "252-0293-00L",
        "name": "Wireless Networking and Mobile Computing"
    },
    {
        "number": "851-0851-00L",
        "name": "Russisch I A1.1"
    },
    {
        "number": "252-4900-00L",
        "name": "Didactic Basics for Student Teaching Assistants @ ETH"
    },
    {
        "number": "851-0588-00L",
        "name": "Introduction to Game Theory"
    },
    {
        "number": "851-0184-00L",
        "name": "Pluralist Philosophy of Mathematics"
    },
    {
        "number": "252-0209-00L",
        "name": "Algorithms, Probability, and Computing"
    },
    {
        "number": "252-0217-00L",
        "name": "Computer Systems"
    },
    {
        "number": "252-0210-00L",
        "name": "Compiler Design"
    },
    {
        "number": "851-0093-00L",
        "name": "Grundprobleme der Wirtschaftsethik"
    },
    {
        "number": "252-3005-00L",
        "name": "Natural Language Processing"
    },
    {
        "number": "376-0210-00L",
        "name": "Biomechatronics"
    },
    {
        "number": "851-0101-86L",
        "name": "Complex Social Systems: Modeling Agents, Learning, and Games"
    },
    {
        "number": "851-0650-00L",
        "name": "AI4Good"
    },
    {
        "number": "529-0002-00L",
        "name": "Algorithmen und Programmieren f\u00fcr die Chemie"
    },
    {
        "number": "551-0317-00L",
        "name": "Immunology I"
    },
    {
        "number": "851-0101-74L",
        "name": "Sustainable Development - Bridging Art and Science"
    },
    {
        "number": "851-0197-00L",
        "name": "Medieval and Early Modern Science and Philosophy"
    },
    {
        "number": "529-0058-00L",
        "name": "Analytische Chemie II"
    },
    {
        "number": "529-0051-00L",
        "name": "Analytische Chemie I"
    },
    {
        "number": "402-0263-00L",
        "name": "Astrophysics I"
    },
    {
        "number": "529-0434-00L",
        "name": "Physical Chemistry V: Spectroscopy"
    },
    {
        "number": "529-0432-00L",
        "name": "Physikalische Chemie IV: Magnetische Resonanz"
    },
    {
        "number": "551-0314-00L",
        "name": "Microbiology (Part II)"
    },
    {
        "number": "551-0313-00L",
        "name": "Microbiology (Part I)"
    },
    {
        "number": "535-0230-00L",
        "name": "Medizinische Chemie I"
    },
    {
        "number": "252-0211-00L",
        "name": "Information Security"
    },
    {
        "number": "151-0306-00L",
        "name": "Visualization, Simulation and Interaction - Virtual Reality I"
    },
    {
        "number": "252-0029-00L",
        "name": "Parallele Programmierung"
    },
    {
        "number": "401-0241-00L",
        "name": "Analysis I"
    },
    {
        "number": "252-0028-00L",
        "name": "Digital Design and Computer Architecture"
    },
    {
        "number": "401-0213-16L",
        "name": "Analysis II"
    },
    {
        "number": "252-0064-00L",
        "name": "Computer Networks"
    },
    {
        "number": "252-0063-00L",
        "name": "Data Modelling and Databases"
    },
    {
        "number": "252-0058-00L",
        "name": "Formal Methods and Functional Programming"
    },
    {
        "number": "252-0061-00L",
        "name": "Systems Programming and Computer Architecture"
    },
    {
        "number": "252-0057-00L",
        "name": "Theoretische Informatik"
    },
    {
        "number": "401-2604-00L",
        "name": "Wahrscheinlichkeit und Statistik"
    },
    {
        "number": "252-3110-00L",
        "name": "Human Computer Interaction"
    },
    {
        "number": "651-4271-00L",
        "name": "Erdwissenschaftliche Datenanalyse und Visualisierung mit Matlab"
    },
    {
        "number": "853-8002-00L",
        "name": "Die Rolle von Technologie in nationaler und internationaler Sicherheitspolitik"
    },
    {
        "number": "252-0341-01L",
        "name": "Information Retrieval"
    },
    {
        "number": "252-3810-00L",
        "name": "Datacenter Network Monitoring and Management"
    },
    {
        "number": "860-0023-00L",
        "name": "International Environmental Politics"
    },
    {
        "number": "252-0220-00L",
        "name": "Introduction to Machine Learning"
    },
    {
        "number": "851-0125-65L",
        "name": "A Sampler of Histories and Philosophies of Mathematics"
    },
    {
        "number": "263-3010-00L",
        "name": "Big Data"
    },
    {
        "number": "263-3712-00L",
        "name": "Advanced Seminar on Computational Haptics"
    },
    {
        "number": "151-0757-00L",
        "name": "Umwelt-Management"
    },
    {
        "number": "252-0026-00L",
        "name": "Algorithmen und Datenstrukturen"
    },
    {
        "number": "851-0557-00L",
        "name": "Soccer Analytics"
    },
    {
        "number": "252-4811-00L",
        "name": "Machine Learning Seminar"
    },
    {
        "number": "252-0206-00L",
        "name": "Visual Computing"
    },
    {
        "number": "853-0061-00L",
        "name": "Einf\u00fchrung in die Cybersicherheitspolitik"
    },
    {
        "number": "363-0564-00L",
        "name": "Entrepreneurial Risks"
    },
    {
        "number": "252-0027-00L",
        "name": "Einf\u00fchrung in die Programmierung"
    },
    {
        "number": "851-0125-81L",
        "name": "Wie frei sind wir? Philosophische Theorien \u00fcber Freiheit und Determinismus"
    },
    {
        "number": "252-5707-00L",
        "name": "Seminar on Media Innovation"
    },
    {
        "number": "851-0370-00L",
        "name": "Didactic Basics for Student Teaching Assistants"
    },
    {
        "number": "227-0664-00L",
        "name": "Technology and Policy of Electrical Energy Storage"
    },
    {
        "number": "252-0538-00L",
        "name": "Shape Modeling and Geometry Processing"
    },
    {
        "number": "351-0778-00L",
        "name": "Discovering Management"
    },
    {
        "number": "227-1037-00L",
        "name": "Introduction to Neuroinformatics"
    },
    {
        "number": "851-0252-15L",
        "name": "Network Analysis"
    },
    {
        "number": "851-0101-56L",
        "name": "From Cotton to Cocaine: Commodities That Made History (c.1700-1950)"
    },
    {
        "number": "851-0240-00L",
        "name": "Menschliches Lernen (EW1)"
    },
    {
        "number": "252-3510-00L",
        "name": "Computing Platforms"
    },
    {
        "number": "363-0541-00L",
        "name": "Systems Dynamics and Complexity"
    },
    {
        "number": "227-0707-00L",
        "name": "Optimization Methods for Engineers"
    },
    {
        "number": "227-0803-00L",
        "name": "Energy, Resources, Environment: Risks and Prospects"
    },
    {
        "number": "402-1701-00L",
        "name": "Physik I"
    },
    {
        "number": "701-0071-00L",
        "name": "Mathematik III: Systemanalyse"
    },
    {
        "number": "252-3800-00L",
        "name": "Advanced Topics in Mixed Reality"
    },
    {
        "number": "851-0525-00L",
        "name": "Das Pers\u00f6nliche und der Computer. Zur Geschichte des PC"
    }
]

def get_courses(url="https://n.ethz.ch/~lteufelbe/coursereview/courses.json"):
    try:
        course_strings = requests.get(url).json()
        parsed_courses = []
        for course_str in course_strings:
            number = course_str[:12].strip()
            name = course_str[12:].strip()
            parsed_courses.append({
                "number": number,
                "name": name
            })
        return parsed_courses
    except Exception as e:
        print(e)
        print("Falling back to static courses.")
        return STATIC_COURSES
