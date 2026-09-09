# ATS Resume Checker - By Swetha S | Hyderabad | 2026
# Placement Project - Original Code

def ats_checker():
    print("=== Swetha's Resume ATS Checker ===\n")
    
    # Keywords for SDE jobs in Hyderabad
    keywords = ["python", "dsa", "oops", "sql", "git", "github", 
                "project", "api", "debugging", "problem solving",
                "teamwork", "communication"]
    
    print("Paste your resume text below.")
    print("Type END on new line when done:\n")
    
    resume_lines = []
    while True:
        line = input()
        if line.upper() == "END":
            break
        resume_lines.append(line)
    
    resume = " ".join(resume_lines).lower()
    
    found = [k for k in keywords if k in resume]
    missing = [k for k in keywords if k not in resume]
    
    score = len(found) * 100 // len(keywords)
    
    print(f"\n--- RESULT ---")
    print(f"ATS Score: {score}%")
    print(f"Matched: {', '.join(found) if found else 'None'}")
    print(f"Missing: {', '.join(missing) if missing else 'None'}")
    
    if score >= 80:
        print("\n🎉 Excellent! Ready for top companies!")
    elif score >= 50:
        print("\n👍 Good! Add 2-3 missing keywords.")
    else:
        print("\n⚠️ Improve resume - add projects & skills.")
    
    # My special feature - Save report
    if input("\nSave report? (yes/no): ").lower() == "yes":
        with open("ats_report.txt", "w") as f:
            f.write(f"Score: {score}%\nFound: {found}\nMissing: {missing}")
        print("Saved as ats_report.txt!")

ats_checker()