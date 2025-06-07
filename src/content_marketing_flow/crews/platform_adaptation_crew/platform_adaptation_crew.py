"""
Platform Adaptation Crew - Hierarchical Process
Handles platform-specific content adaptation with parallel execution
Located at: src/content_marketing_flow/crews/platform_adaptation_crew/platform_adaptation_crew.py
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class PlatformAdaptationCrew():
    """Platform Adaptation Crew for parallel content optimization"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def instagram_adapter(self) -> Agent:
        """Instagram Platform Adapter"""
        return Agent(
            config=self.agents_config['instagram_adapter'],
            verbose=True
        )

    @agent
    def linkedin_adapter(self) -> Agent:
        """LinkedIn Platform Adapter"""
        return Agent(
            config=self.agents_config['linkedin_adapter'],
            verbose=True
        )

    @agent
    def twitter_adapter(self) -> Agent:
        """Twitter Platform Adapter"""
        return Agent(
            config=self.agents_config['twitter_adapter'],
            verbose=True
        )

    @agent
    def facebook_adapter(self) -> Agent:
        """Facebook Platform Adapter"""
        return Agent(
            config=self.agents_config['facebook_adapter'],
            verbose=True
        )

    @agent
    def blog_adapter(self) -> Agent:
        """Blog Platform Adapter"""
        return Agent(
            config=self.agents_config['blog_adapter'],
            verbose=True
        )

    # Platform Adaptation Tasks
    @task
    def adapt_instagram_task(self) -> Task:
        """Adapt content for Instagram"""
        return Task(
            config=self.tasks_config['adapt_instagram_task'],
            agent=self.instagram_adapter(),
            output_file='instagram_post.md'
        )

    @task
    def adapt_linkedin_task(self) -> Task:
        """Adapt content for LinkedIn"""
        return Task(
            config=self.tasks_config['adapt_linkedin_task'],
            agent=self.linkedin_adapter(),
            output_file='linkedin_post.md'
        )

    @task
    def adapt_twitter_task(self) -> Task:
        """Adapt content for Twitter"""
        return Task(
            config=self.tasks_config['adapt_twitter_task'],
            agent=self.twitter_adapter(),
            output_file='twitter_tweet.md'
        )

    @task
    def adapt_facebook_task(self) -> Task:
        """Adapt content for Facebook"""
        return Task(
            config=self.tasks_config['adapt_facebook_task'],
            agent=self.facebook_adapter(),
            output_file='facebook_post.md'
        )

    @task
    def finalize_blog_task(self) -> Task:
        """Finalize blog post"""
        return Task(
            config=self.tasks_config['finalize_blog_task'],
            agent=self.blog_adapter(),
            output_file='blog_post.md'
        )

    @crew
    def crew(self) -> Crew:
        """Create the platform adaptation crew with true parallel execution"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,  # Hierarchical enables parallel execution
            manager_llm="gpt-4o",     # Manager coordinates parallel tasks
            verbose=True,
            memory=True
        )