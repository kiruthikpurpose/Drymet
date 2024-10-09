
# Drymet

**Drymet** is an innovative system designed to enhance rider safety and visibility in adverse weather conditions, particularly rain. The system incorporates several features, including an electric-powered heated visor, a photochromic auto-dimming visor, and a minimal heads-up display (HUD) to provide essential alerts without overwhelming the rider.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Electric-Powered Heated Visor**: Prevents fogging and ensures clear visibility in rainy conditions.
- **Photochromic Auto-Dimming Visor**: Automatically adjusts to light conditions for optimal visibility.
- **Minimal Heads-Up Display (HUD)**: Provides safety alerts and essential information without distractions.
- **Ventilation System**: Integrated vents ensure airflow while keeping moisture out.
- **Waterproof Design**: Protects all electronic components from rain and moisture.
- **Impact-Resistant Shell**: Lightweight and durable, ensuring rider safety.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kiruthikpurpose/Drymet.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Drymet
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the main program:
```bash
python src/main.py
```

This will initiate the Drymet system, managing the visor heating, HUD alerts, and ventilation as per the configurations set in the `config/settings.json` file.

## Configuration

The configuration files are located in the `config` directory.

- **settings.json**: Contains adjustable parameters for the system's features (e.g., battery thresholds, heating settings).
- **alerts.json**: Specifies the alert messages and conditions for the HUD display.

Modify these files as needed to tailor the system's performance to your preferences.

## Testing

To run tests for the various components of the Drymet system:
```bash
pytest tests/
```

Make sure you have [pytest](https://docs.pytest.org/en/6.2.x/) installed, which you can add to your `requirements.txt`.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Make your changes and commit them (`git commit -m 'Add feature xyz'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or suggestions, feel free to reach out:

- **Email**: [My Email](mailto:kiruthikpurpose@gmail.com)
- **GitHub**: [My GitHub](https://github.com/kiruthikpurpose)

---

**Drymet** aims to revolutionize rider safety in adverse weather conditions while ensuring an enjoyable riding experience. Thank you for your interest in the project!
