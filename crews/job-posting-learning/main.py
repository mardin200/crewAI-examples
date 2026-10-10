
from pathlib import Path
from dotenv import load_dotenv
from job_posting_crew.crew import JobPostingCrew

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR.parent / ".env")
load_dotenv(BASE_DIR / ".env", override=False)


def main():
    inputs = {
        "company_name": "Northstar Media",
        "company_domain": "https://example.com",
        "company_description": (
            "Northstar Media is a fictional media and entertainment company "
            "that produces digital video content and supports production teams. "
            "Its stated priorities are collaboration, safety, reliability, and inclusion."
        ),
        "job_title": "Production Assistant",
        "location": "Los Angeles, California",
        "hiring_needs": (
            "Support production staff with schedules, equipment preparation, "
            "organizing materials, coordinating requests, and keeping production "
            "activities on schedule. Applicants should be organized, dependable, "
            "communicative, and comfortable working in a fast-paced environment."
        ),
        "specific_benefits": (
            "Training opportunities, collaborative teams, and opportunities "
            "to learn production workflows."
        ),
    }

    crew = JobPostingCrew()
    result = crew.crew().kickoff(inputs=inputs)

    # Task outputs follow the order defined in crew.py.
    task_outputs = result.tasks_output

    if len(task_outputs) < 5:
        raise RuntimeError(
            f"Expected 5 task outputs, but received {len(task_outputs)}."
        )

    # Task 4: reviewed job posting
    job_posting = task_outputs[3].raw

    # Task 5: separate industry analysis
    industry_analysis = task_outputs[4].raw

    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    job_posting_file = output_dir / "job_posting.md"
    industry_analysis_file = output_dir / "industry_analysis.md"

    job_posting_file.write_text(job_posting, encoding="utf-8")
    industry_analysis_file.write_text(industry_analysis, encoding="utf-8")

    print("\n===== FINAL REVIEWED JOB POSTING =====\n")
    print(job_posting)
    print(f"\nSaved job posting to: {job_posting_file}")

    print("\n===== INDUSTRY ANALYSIS =====\n")
    print(industry_analysis)
    print(f"\nSaved industry analysis to: {industry_analysis_file}")


if __name__ == "__main__":
    main()