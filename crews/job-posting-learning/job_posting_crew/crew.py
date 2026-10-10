from pathlib import Path
from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent


class RoleRequirements(BaseModel):
    skills: List[str] = Field(description="Skills relevant to the job")
    experience: List[str] = Field(description="Experience or background requirements")
    qualities: List[str] = Field(description="Personal and collaboration qualities")


class CompanyResearch(BaseModel):
    mission_and_context: str = Field(description="Company context based only on supplied inputs")
    culture_themes: List[str] = Field(description="Culture themes supported by supplied inputs")
    candidate_message: List[str] = Field(description="Accurate points that may appeal to candidates")


@CrewBase
class JobPostingCrew:
    """A small, local-first job-posting workflow inspired by CrewAI's example."""

    agents_config = str(BASE_DIR / "config" / "agents.yaml")
    tasks_config = str(BASE_DIR / "config" / "tasks.yaml")

    @agent
    def research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["research_analyst"],
            verbose=True,
        )

    @agent
    def job_description_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["job_description_writer"],
            verbose=True,
        )

    @agent
    def review_editor(self) -> Agent:
        return Agent(
            config=self.agents_config["review_editor"],
            verbose=True,
        )

    @task
    def research_company_culture(self) -> Task:
        return Task(
            config=self.tasks_config["research_company_culture"],
            output_pydantic=CompanyResearch,
        )

    @task
    def research_role_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["research_role_requirements"],
            output_pydantic=RoleRequirements,
        )

    @task
    def draft_job_posting(self) -> Task:
        return Task(config=self.tasks_config["draft_job_posting"])

    @task
    def review_and_edit_job_posting(self) -> Task:
        return Task(config=self.tasks_config["review_and_edit_job_posting"])

    @task
    def industry_analysis(self) -> Task:
        return Task(config=self.tasks_config["industry_analysis"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
