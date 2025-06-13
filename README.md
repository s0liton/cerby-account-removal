# Cerby Account Removal Tool

This tool helps you quickly remove accounts from your Cerby workspace via the Cerby API.

## Requirements

- **Access Token:** You will need a valid Cerby API access token.
- **Subdomain:** Know the subdomain of your Cerby workspace.
- **Python 3.8+** installed on your system.
- **Optional - Text File** A file with one account ID per line.

## Installation

You can install the required dependencies in two ways:

### Option 1: Install Directly

```sh
pip install -r requirements.txt
```

### Option 2: Using a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. **Provide Credentials:** Enter your access token and workspace subdomain when prompted.
2. **Choose Input Method:**
   - **Individual Account IDs:** Enter one or more account IDs manually.
   - **CSV File:** Use a CSV file containing a single account ID per line.

Follow the prompts to complete the account removal process.
