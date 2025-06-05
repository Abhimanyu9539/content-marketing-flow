# Content Marketing Flow

A multi-agent AI system built with CrewAI for automated content creation and platform adaptation across various social media channels.

## 📁 Project Structure

```
content_marketing_flow/
├── .venv/                          # Virtual environment
├── src/content_marketing_flow/     # Main source code
│   ├── __pycache__/               # Python cache files
│   └── crews/                     # CrewAI crew configurations
│       ├── content_creation_crew/  # Content creation agents
│       │   ├── __pycache__/
│       │   ├── config/            # Agent and task configurations
│       │   └── content_creation_crew.py
│       └── platform_adaptation_crew/ # Platform-specific adaptation
│           ├── __pycache__/
│           ├── config/            # Agent and task configurations
│           └── platform_adaptation_crew.py
├── tools/                         # Custom tools and utilities
│   ├── __init__.py
│   ├── flow.py                   # Main flow orchestration
│   └── main.py                   # Entry point
├── tests/                        # Test files
├── .env                         # Environment variables
├── .gitignore                   # Git ignore rules
└── Content Templates/           # Platform-specific templates
    ├── 1_blog_post.md
    ├── 2_facebook_post.md
    ├── 3_instagram_post.md
    └── 4_linkedin_post.md
```

## 🚀 Features

- **Multi-Agent Content Creation**: Specialized AI agents for different aspects of content creation
- **Platform Adaptation**: Automatic adaptation of content for different social media platforms
- **Template-Based Generation**: Pre-defined templates for consistent content formatting
- **Modular Architecture**: Separate crews for content creation and platform adaptation

## 🛠️ Setup

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd content_marketing_flow
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configurations
   ```

### Environment Variables

Create a `.env` file with the following variables:

```env
# OpenAI API Key (or your preferred LLM provider)
OPENAI_API_KEY=your_openai_api_key_here

# Other API keys as needed
SERPER_API_KEY=your_serper_api_key_here

# CrewAI specific configurations
CREWAI_TELEMETRY_OPT_OUT=true
```

## 🏃‍♂️ Usage

### Running the Content Marketing Flow

1. **Start the main flow**
   ```bash
   python tools/main.py
   ```

2. **Run specific crews independently**
   ```bash
   # Content creation only
   python src/content_marketing_flow/crews/content_creation_crew/content_creation_crew.py
   
   # Platform adaptation only
   python src/content_marketing_flow/crews/platform_adaptation_crew/platform_adaptation_crew.py
   ```

### Content Templates

The system uses predefined templates for different platforms:

- **Blog Post** (`1_blog_post.md`): Long-form content template
- **Facebook Post** (`2_facebook_post.md`): Engaging social media format
- **Instagram Post** (`3_instagram_post.md`): Visual-focused with hashtags
- **LinkedIn Post** (`4_linkedin_post.md`): Professional networking content

## 🤖 Crews Overview

### Content Creation Crew

Located in `src/content_marketing_flow/crews/content_creation_crew/`

**Purpose**: Handles the initial content creation process including research, writing, and editing.

**Typical Agents**:
- Research Agent: Gathers information and data
- Writer Agent: Creates initial content drafts
- Editor Agent: Reviews and refines content

### Platform Adaptation Crew

Located in `src/content_marketing_flow/crews/platform_adaptation_crew/`

**Purpose**: Adapts created content for specific social media platforms and formats.

**Typical Agents**:
- Social Media Strategist: Determines platform-specific approaches
- Content Adapter: Modifies content for different platforms
- Hashtag Specialist: Adds relevant tags and optimization


## 📝 Configuration

### Agent Configuration

Agent configurations are stored in `config/` directories within each crew:

- `agents.yaml`: Defines agent roles, goals, and backstories
- `tasks.yaml`: Defines tasks and their relationships

### Customizing Crews

1. **Modify agent configurations** in the respective `config/` folders
2. **Add new agents** by updating the crew files
3. **Create custom tools** in the `tools/` directory

## 🔧 Tools

The `tools/` directory contains:

- **flow.py**: Main orchestration logic for connecting crews
- **main.py**: Entry point and CLI interface
- **Custom tools**: Additional utilities for content processing

## 📊 Output

Generated content will be saved according to your crew configurations, typically including:

- Original research and data
- Base content versions
- Platform-adapted content
- Performance metrics and suggestions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure virtual environment is activated and dependencies installed
2. **API Key Issues**: Verify all required API keys are set in `.env`
3. **CrewAI Delegation Errors**: Update to the latest CrewAI version if experiencing delegation issues

### Getting Help

- Check the [CrewAI Documentation](https://docs.crewai.com/)
- Review existing issues in the repository
- Create a new issue with detailed error information

## 🔄 Updates

To update the project:

```bash
git pull origin main
pip install --upgrade -r requirements.txt
```

---

*Built with [CrewAI](https://crewai.com/) - Framework for orchestrating role-playing, autonomous AI agents.*