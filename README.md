# Filler Agent

An intelligent form-filling agent powered by Google's Agent Development Kit (ADK) that automatically populates web forms by parsing DOM structures and matching them with your profile data.

## 🌟 Overview

Filler Agent is an automated form-filling solution that leverages AI capabilities from Google's ADK to:
- Parse and understand DOM structures from web forms
- Extract form field information intelligently
- Automatically fill forms using your predefined profile data (YAML format)
- Handle various form types and field formats

This project serves as both a practical tool and a learning resource for working with AgenticAI and the Google Agent Development Kit.

## ✨ Features

- **Intelligent DOM Parsing**: Automatically identifies form fields, input types, and required information
- **Profile-Based Filling**: Uses YAML configuration to store and manage your profile information
- **Multi-Field Support**: Handles text inputs, dropdowns, checkboxes, radio buttons, and more
- **Context-Aware**: Uses AI to understand field semantics (e.g., "First Name" vs "Given Name")
- **Extensible**: Easy to customize and extend for specific use cases
- **Privacy-Focused**: All profile data stored locally in YAML format

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.9 or higher
- **Google Cloud Account**: For accessing ADK services
- **pip**: Python package manager
- **git**: For cloning the repository

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JumpingDino/filler-agent.git
   cd filler-agent
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google ADK credentials**
   ```bash
   # Set your Google Cloud project ID
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   
   # Authenticate with Google Cloud
   gcloud auth application-default login
   ```

5. **Install Google ADK**
   ```bash
   pip install google-adk
   ```

## ⚙️ Configuration

### Profile YAML Format

Create a `profile.yaml` file in the project root with your information:

```yaml
# profile.yaml
personal:
  first_name: "John"
  last_name: "Doe"
  middle_name: "Michael"
  full_name: "John Michael Doe"
  date_of_birth: "1990-01-15"
  gender: "Male"
  
contact:
  email: "john.doe@example.com"
  phone: "+1-555-0123"
  alternative_phone: "+1-555-0124"
  
address:
  street: "123 Main Street"
  apt_unit: "Apt 4B"
  city: "San Francisco"
  state: "California"
  zip_code: "94102"
  country: "United States"
  
professional:
  occupation: "Software Engineer"
  company: "Tech Corp"
  years_of_experience: 5
  
social:
  linkedin: "https://linkedin.com/in/johndoe"
  github: "https://github.com/johndoe"
  website: "https://johndoe.com"
  
preferences:
  newsletter: true
  terms_accepted: true
```

### Environment Configuration

Create a `.env` file for sensitive configuration:

```env
GOOGLE_CLOUD_PROJECT=your-project-id
ADK_API_KEY=your-api-key
LOG_LEVEL=INFO
```

## 💻 Usage

### Basic Usage

```python
from filler_agent import FillerAgent

# Initialize the agent
agent = FillerAgent(profile_path="profile.yaml")

# Parse a DOM structure
dom_content = """
<form>
  <input name="firstName" type="text" />
  <input name="email" type="email" />
  <input name="phone" type="tel" />
</form>
"""

# Get filling suggestions
suggestions = agent.analyze_form(dom_content)

# Apply the filling
filled_data = agent.fill_form(suggestions)
print(filled_data)
```

### Command Line Usage

```bash
# Analyze a form from HTML file
python filler_agent.py analyze --input form.html

# Fill a form with your profile
python filler_agent.py fill --input form.html --profile profile.yaml --output filled.json

# Interactive mode
python filler_agent.py interactive
```

### With Browser Extension

```javascript
// Load the agent in a browser context
const agent = new FillerAgent();

// Analyze current page
const formFields = agent.analyzeCurrentPage();

// Fill the form
agent.fillCurrentPage(formFields);
```

## 🔍 How It Works

1. **DOM Parsing**: The agent receives HTML/DOM content from a web form
2. **Field Identification**: Using ADK's NLP capabilities, it identifies:
   - Input field types (text, email, phone, etc.)
   - Field semantics (name, address, contact info)
   - Required vs optional fields
   - Validation patterns
3. **Profile Matching**: Matches identified fields with corresponding data in your profile YAML
4. **Context Understanding**: Uses AI to handle variations in field naming (e.g., "fname" vs "first_name" vs "given_name")
5. **Smart Filling**: Generates appropriate values for each field based on context
6. **Validation**: Ensures filled data meets field requirements

## 📁 Project Structure

```
filler-agent/
├── README.md                 # This file
├── profile.yaml             # User profile configuration
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── filler_agent/
│   ├── __init__.py         # Package initialization
│   ├── agent.py            # Main agent logic
│   ├── dom_parser.py       # DOM parsing utilities
│   ├── profile_manager.py  # Profile YAML handler
│   ├── field_matcher.py    # Field matching logic
│   └── adk_client.py       # Google ADK integration
├── tests/
│   ├── test_agent.py
│   ├── test_parser.py
│   └── fixtures/
├── examples/
│   ├── sample_forms/       # Example HTML forms
│   └── sample_profiles/    # Example profile YAMLs
└── docs/
    ├── architecture.md     # Architecture details
    └── api_reference.md    # API documentation
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=filler_agent

# Run specific test
python -m pytest tests/test_agent.py
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code:
- Follows PEP 8 style guidelines
- Includes appropriate tests
- Updates documentation as needed
- Respects user privacy and data security

## 🔒 Privacy & Security

- **Local Storage**: All profile data is stored locally on your machine
- **No Data Transmission**: Profile data is never transmitted to external servers (except when explicitly using ADK services)
- **Encryption**: Sensitive data in profile.yaml can be encrypted
- **Access Control**: Set appropriate file permissions on your profile.yaml

## 📚 Resources

- [Google AI Platform Documentation](https://cloud.google.com/ai-platform/docs)
- [Google Vertex AI Agent Builder](https://cloud.google.com/vertex-ai/docs/agent-builder/introduction)
- [AgenticAI Concepts](https://cloud.google.com/blog/products/ai-machine-learning)
- [YAML Specification](https://yaml.org/spec/)
- [DOM API Reference](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

## 🐛 Troubleshooting

### Common Issues

**Issue**: ADK authentication fails
```bash
# Solution: Re-authenticate
gcloud auth application-default login
```

**Issue**: Profile YAML not loading
```bash
# Solution: Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('profile.yaml'))"
```

**Issue**: Form fields not recognized
- Ensure the DOM structure is complete
- Check that field names/IDs are present in the HTML
- Verify ADK API quotas haven't been exceeded

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Cloud team for the Agent Development Kit
- Contributors and community members
- Open source projects that inspired this work

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/JumpingDino/filler-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/JumpingDino/filler-agent/discussions)
- **Email**: support@example.com

## 🗺️ Roadmap

- [ ] Browser extension for Chrome/Firefox
- [ ] Support for multi-page forms
- [ ] Machine learning-based field prediction
- [ ] Integration with password managers
- [ ] Multi-language support
- [ ] Form template library
- [ ] Cloud sync for profiles (optional)

---

**Note**: This is a learning project focused on AgenticAI. Always review auto-filled information before submission and ensure compliance with website terms of service.
