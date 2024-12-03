# FCB Data Providers

## Getting Started

Welcome to the FCB Data Providers project. This project is designed to help you read and analyze data from various data providers. Follow the instructions below to get started.

### Prerequisites

Make sure you have the following installed:

- Python 3.11 or higher
- pip (Python package installer)
- Jupyter Notebook

### Installation

1. Clone the repository:

   ```sh
   git clone git@github.com:saudBinHabib/fcb_data_analytics.git
   cd fcb_data_analytics
   ```

2. Install the required packages:

   ```sh
   pip install -r requirement/dev.txt
   ```

3. Installing fcb_data_provider package.
   ```sh
   pip install -e .
   ```

## 📊 Features

### Data Processing

- Custom Python package for match data processing
- Efficient event data extraction

## 🛠 Tech Stack

### Backend

- Python 3.11+
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pandas
- Logging
- Docker
- pre-commit hooks

## Using `fcb_data_providers` package

The `src.fcb_data_providers.providers` module contains classes to read data from various data providers. Here's an example of how to use these classes:

```python
from src.fcb_data_providers.providers import StatsPerformProvider

# StatsPerformProvider needs DATABASE_URL, and Data directory as parameters, for which you can either crete variables or get that from your environment variables. e.g.

DATABASE_URL=os.getenv("DATABASE_URL")
DATA_DIR = os.getenv("DATA_DIR")

# Initialize the data provider
stats_perform = StatsPerformProvider(data_path=DATA_DIR, database_url=DATABASE_URL)

# You can get the Events files list like this.
match_event_files = stats_perform.get_match_related_files(file_type="match_event")
stats_perform.logger.info(f"Match event files: {match_event_files}")

# You can get the match stats files list like this.
match_stat_files = stats_perform.get_match_related_files(file_type="match_stats")
stats_perform.logger.info(f"Match stats files: {match_stat_files}")

# You can process match events data like this.
stats_perform.process_match_event_data(file_path_list=match_event_files)

# You can process match stats data like this.
stats_perform.process_match_stats_data(file_path_list=match_event_files)

# Or if you want to do complete processing of the events, and stats data, you can use following.
# This function will read events, and stats file from data_dir, and will do complete processing.
stats_perform.process_data()

```

## Running Tests

To ensure everything is working correctly, you can run the tests included in the project. Use the following command to run the tests:

```sh
pytest
```

Make sure you have `pytest` installed. If not, you can install it using:

```sh
pip install pytest
```

## Data Exploration Using Jupyter Notebooks

The `notebooks` directory contains Jupyter Notebooks for data exploration. To start exploring the data, follow these steps:

1. Navigate to the `notebooks` directory:

   ```sh
   cd notebooks
   ```

2. Create Jupyter Notebook:

   ```sh
   touch data-exploration.ipynb
   ```

3. Open any of the notebooks to start exploring the data.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

    For questions and support, please contact:

    Project Maintainer: Saud Bin Habib
    Technical Support: saud.bin.habib@outlook.com

Made with ⚽️ for FC Bayern Munich
