#!/usr/bin/env python
"""
Content Marketing Flow - Main Entry Point
Located at: src/content_marketing_flow/main.py
"""
import os
import warnings
from datetime import datetime
from crewai.flow.flow import Flow, listen, start

# Import crews from the correct paths
from content_marketing_flow.crews.content_creation_crew.content_creation_crew import ContentCreationCrew
from content_marketing_flow.crews.platform_adaptation_crew.platform_adaptation_crew import PlatformAdaptationCrew

import agentops
agentops.init()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


class ContentMarketingFlow(Flow):
    """
    Content Marketing Flow
    Orchestrates two crews: Content Creation and Platform Adaptation
    """

    def __init__(self):
        super().__init__()

    @start()
    def content_creation_phase(self):
        """
        Phase 1: Content Creation (Sequential Process)
        Research → Strategy → Content → SEO
        """
        print("📝 Starting Content Creation Phase...")
        print("   🔍 Research & Strategy")
        print("   ✍️  Content Writing & Editing")
        print("   🔍 SEO Optimization")

        # Get inputs from flow state
        inputs = self.state.copy()
        
        # Add current date
        inputs['current_date'] = datetime.now().strftime("%B %d, %Y")

        # Execute content creation crew
        content_crew = ContentCreationCrew()
        result = content_crew.crew().kickoff(inputs=inputs)

        print("✅ Content Creation Phase completed")
        return result

    @listen(content_creation_phase)
    def platform_adaptation_phase(self, content_results):
        """
        Phase 2: Platform Adaptation (Hierarchical Process - Parallel)
        All platform adaptations run in parallel
        """
        print("\n🚀 Starting Platform Adaptation Phase...")
        print("   📱 Instagram | 💼 LinkedIn | 🐦 Twitter | 📘 Facebook | 📝 Blog")
        print("   ⚡ Running all adaptations in PARALLEL...")

        # Get inputs from flow state
        inputs = self.state.copy()
        
        # Add current date
        inputs['current_date'] = datetime.now().strftime("%B %d, %Y")

        # Execute platform adaptation crew (hierarchical for parallel execution)
        platform_crew = PlatformAdaptationCrew()
        result = platform_crew.crew().kickoff(inputs=inputs)

        print("✅ Platform Adaptation Phase completed")
        print("\n🎉 Content Marketing Flow Completed Successfully!")
        print("📁 Generated Files:")
        print("   📱 instagram_post.md")
        print("   💼 linkedin_post.md")
        print("   🐦 twitter_tweet.md")
        print("   📘 facebook_post.md")
        print("   📝 blog_post.md")

        return {
            'content_results': content_results,
            'platform_results': result,
            'status': 'completed'
        }


def run():
    """
    Entry point for crewai run command
    """
    # Content configuration
    inputs = {
        'topic': 'AI in Digital Marketing',
        'target_audience': 'Marketing professionals and business owners',
        'brand_tone': 'Professional yet approachable',
        'key_messages': [
            'AI makes marketing more efficient and effective',
            'Automation saves time while improving results',
            'Modern marketing tools are accessible to businesses of all sizes',
            'Data-driven decisions lead to better marketing outcomes'
        ],
        'call_to_action': 'Schedule a free consultation to discover how AI can transform your marketing strategy'
    }
    
    print("🎬 Starting Content Marketing Flow")
    print("=" * 60)
    print(f"📋 Topic: {inputs['topic']}")
    print(f"🎯 Audience: {inputs['target_audience']}")
    print(f"🗣️  Tone: {inputs['brand_tone']}")
    print(f"📢 Key Messages: {len(inputs['key_messages'])} strategic points")
    print("=" * 60)
    
    try:
        # Initialize and run the flow
        flow = ContentMarketingFlow()
        
        result = flow.kickoff(inputs=inputs)
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error during execution: {str(e)}")
        raise


def kickoff():
    """
    Alternative entry point for different command structures
    """
    return run()


if __name__ == "__main__":
    run()