"""
Content Creation Crew - Sequential Process
Handles research, strategy, content creation, and SEO optimization
Located at: src/content_marketing_flow/crews/content_creation_crew/content_creation_crew.py
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


@CrewBase
class ContentCreationCrew():
    """Content Creation Crew for research, strategy, and content development"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def research_strategist(self) -> Agent:
        """Research Strategist with web search capabilities"""
        return Agent(
            config=self.agents_config['research_strategist'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            max_iter = 1
        )

    @agent
    def content_strategist(self) -> Agent:
        """Content Strategist for strategic planning"""
        return Agent(
            config=self.agents_config['content_strategist'],
            verbose=True
        )

    @agent
    def content_writer(self) -> Agent:
        """Content Writer for creating initial drafts"""
        return Agent(
            config=self.agents_config['content_writer'],
            verbose=True
        )

    @agent
    def content_editor(self) -> Agent:
        """Content Editor for quality improvement"""
        return Agent(
            config=self.agents_config['content_editor'],
            verbose=True
        )

    @agent
    def seo_optimizer(self) -> Agent:
        """SEO Optimizer for search engine optimization"""
        return Agent(
            config=self.agents_config['seo_optimizer'],
            verbose=True
        )

    # Research Tasks
    @task
    def market_research_task(self) -> Task:
        """Research market trends and competitors"""
        return Task(
            config=self.tasks_config['market_research_task'],
            agent=self.research_strategist()
        )

    @task
    def audience_analysis_task(self) -> Task:
        """Analyze target audience behavior"""
        return Task(
            config=self.tasks_config['audience_analysis_task'],
            agent=self.research_strategist()
        )

    # Strategy Task
    @task
    def content_strategy_task(self) -> Task:
        """Develop content strategy"""
        return Task(
            config=self.tasks_config['content_strategy_task'],
            agent=self.content_strategist(),
            context=[self.market_research_task(), self.audience_analysis_task()]
        )

    # Content Creation Tasks
    @task
    def draft_content_task(self) -> Task:
        """Create initial content draft"""
        return Task(
            config=self.tasks_config['draft_content_task'],
            agent=self.content_writer(),
            context=[self.content_strategy_task()]
        )

    @task
    def edit_content_task(self) -> Task:
        """Edit and improve content quality"""
        return Task(
            config=self.tasks_config['edit_content_task'],
            agent=self.content_editor(),
            context=[self.draft_content_task()]
        )

    @task
    def optimize_blog_seo_task(self) -> Task:
        """Optimize content for SEO"""
        return Task(
            config=self.tasks_config['optimize_blog_seo_task'],
            agent=self.seo_optimizer(),
            context=[self.edit_content_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Create the content creation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Sequential for quality control
            verbose=True,
            memory=True
        )