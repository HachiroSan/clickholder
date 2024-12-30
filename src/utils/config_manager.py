import json
import os
import threading
from typing import Dict, Any, Optional

class ConfigManager:
    """Thread-safe configuration manager with validation."""
    _instance = None
    _lock = threading.Lock()
    
    DEFAULT_CONFIG = {
        "start_minimized": False,
        "sound_enabled": True,
        "trigger_key": "Key.alt_l"
    }

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self):
        self._config: Dict[str, Any] = {}
        self._config_path = "config.json"
        self._load_config()

    def _load_config(self) -> None:
        """Load configuration with error handling."""
        try:
            if os.path.exists(self._config_path):
                with open(self._config_path, 'r') as f:
                    loaded_config = json.load(f)
                    self._config = self._validate_config(loaded_config)
            else:
                self._config = self.DEFAULT_CONFIG.copy()
                self._save_config()
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config: {e}. Using defaults.")
            self._config = self.DEFAULT_CONFIG.copy()
            self._save_config()

    def _save_config(self) -> None:
        """Save configuration with error handling."""
        try:
            with open(self._config_path, 'w') as f:
                json.dump(self._config, f, indent=4)
        except IOError as e:
            print(f"Error saving config: {e}")

    def _validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and sanitize configuration values."""
        validated = self.DEFAULT_CONFIG.copy()
        
        if isinstance(config.get('start_minimized'), bool):
            validated['start_minimized'] = config['start_minimized']
            
        if isinstance(config.get('sound_enabled'), bool):
            validated['sound_enabled'] = config['sound_enabled']
            
        if isinstance(config.get('trigger_key'), str):
            validated['trigger_key'] = config['trigger_key']
            
        return validated

    def get_config(self) -> Dict[str, Any]:
        """Thread-safe config getter."""
        with self._lock:
            return self._config.copy()

    def update_config(self, key: str, value: Any) -> bool:
        """Thread-safe config update with validation."""
        with self._lock:
            if key not in self.DEFAULT_CONFIG:
                return False
                
            if not isinstance(value, type(self.DEFAULT_CONFIG[key])):
                return False
                
            self._config[key] = value
            self._save_config()
            return True

    def reset_to_defaults(self) -> None:
        """Reset configuration to defaults."""
        with self._lock:
            self._config = self.DEFAULT_CONFIG.copy()
            self._save_config() 