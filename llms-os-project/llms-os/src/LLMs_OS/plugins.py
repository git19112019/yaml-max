"""Plugin system for LLMs_OS"""
import importlib
import os
from pathlib import Path
from typing import List, Dict, Any

class PluginManager:
    """Manage dynamic plugin loading"""
    
    def __init__(self):
        self.plugins = {}
    
    def load_plugin(self, plugin_path: str):
        """Load a plugin from a Python file"""
        plugin_name = Path(plugin_path).stem
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.plugins[plugin_name] = module
        return module
    
    def load_plugins_from_directory(self, directory: str):
        """Load all plugins from a directory"""
        plugin_dir = Path(directory)
        if not plugin_dir.exists():
            return
        
        for plugin_file in plugin_dir.glob('*.py'):
            if plugin_file.name.startswith('_'):
                continue
            self.load_plugin(str(plugin_file))
    
    def get_plugin(self, name: str):
        """Get a loaded plugin by name"""
        return self.plugins.get(name)
    
    def list_plugins(self) -> List[str]:
        """List all loaded plugins"""
        return list(self.plugins.keys())
