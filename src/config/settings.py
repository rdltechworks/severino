import os
from dotenv import load_dotenv

# Load environment variables from a .env file at the project root
# This allows for easy management of sensitive information like API keys
load_dotenv()

# --- Project Root --- 
# Dynamically determine the project root, assuming this file is within severino/src/config/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# --- Local Model Paths ---
# Default local LLM model filename. This model should be placed in data/models/.
DEFAULT_LOCAL_LLM_MODEL_FILENAME = "gemma-2b-it.Q4_K_M.gguf"

# Default path to the local LLM GGUF model file for development purposes.
# This assumes the model is downloaded into the 'data/models/' directory
# relative to the project root.
DEFAULT_LOCAL_LLM_MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "data", "models", DEFAULT_LOCAL_LLM_MODEL_FILENAME
)

# --- LLM Settings (Local LLM) ---
# Default maximum output tokens for local LLM generation.
# This helps control response length.
MAX_LOCAL_LLM_OUTPUT_TOKENS = 1000

# --- llama-cpp-python specific settings for local LLM inference ---
# N_GPU_LAYERS: Number of layers to offload to the GPU.
# -1 means all layers (if they fit). Adjust based on your GPU VRAM (RTX 4070 has 12GB).
# For Gemma 7B Q4_K_M, a value like 30-32 is a good starting point for 12GB VRAM.
N_GPU_LAYERS = -1

# N_CTX: Context window size for the local LLM (number of tokens it can process).
# Larger context requires more VRAM. 8192 is a common and good value for Gemma 7B.
N_CTX = 8192

# N_BATCH: Batch size for prompt processing.
# Larger batches can improve throughput but use more VRAM.
N_BATCH = 512

# --- UI Settings ---
# Emoji to prepend to agent responses in chat.
# Can be any valid emoji character.
AGENT_EMOJI = "🐨"

# Enable or disable the Koala Climb progress indicator.
KOALA_THEME_ENABLED = True
# Number of levels/steps for the Koala Climb animation.
KOALA_THEME_LEVELS = 5

# --- Logging Settings ---
LOG_LEVEL = os.getenv("LOG_LEVEL", "CRITICAL").upper() # Default to CRITICAL to suppress most logs
LOG_FILE = os.path.join(
    PROJECT_ROOT,
    ".severino", "logs", "severino.log"
)