# run this in terminal before running ./build.sh: 
# chmod +x build.sh

set -e

VENV_DIR="venv"

echo "=== Setting up Python Virtual Environment ==="

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment $VENV_DIR already exists."
fi

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "Upgrading pip..."
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
    echo "=== Build completed successfully! ==="
else
    echo "Error: requirements.txt file not found."
    exit 1
fi