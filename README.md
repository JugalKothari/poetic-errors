# Poetic Error Handler 📝
Transform your Python error messages into delightful poems! This lightweight error handler converts standard Python errors into poetic form while preserving the original error information.

## Installation
You can install the package using pip:
```bash
pip install poetic-errors
```

## Quick Start
Simply import the module at the start of your Python script:
```python
import poetic_errors
```

That's it! Your error messages will now be displayed as poems.

## Features
- Converts common Python errors into randomly selected poems
- Maintains original error messages for debugging
- Works across all operating systems (Windows, macOS, Linux)
- Handles different error types with specific poem templates:
  - NameError
  - SyntaxError
  - TypeError
  - And a default template for other errors

## Example
If you run code with an undefined variable:
```python
x = y + 1  # y is not defined
```

You'll see output like:
```
.-----------------.
| Poetic Error    |
'-----------------'
Roses are red,
Variables are rare,
On line 1, I looked everywhere,
But y just wasn't there.

Original error: name 'y' is not defined
```

## Development
To contribute or modify the package:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/poetic-errors.git
```

2. Install in development mode:
```bash
pip install -e .
```

## Customization
You can add your own poem templates by modifying the `templates` dictionary in the `PoeticErrorHandler` class. Each error type can have multiple poem templates that will be randomly selected.

## Requirements
- Python 3.6 or higher
- No additional dependencies required

## Contributing
Feel free to contribute by:
- Adding new poem templates
- Supporting additional error types
- Improving error detection and formatting
- Suggesting new features

## License
MIT License - Feel free to use and modify!
