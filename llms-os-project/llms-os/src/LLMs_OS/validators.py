"""YAML validation for LLMs_OS"""
import jsonschema

WORKFLOW_SCHEMA = {
    "type": "object",
    "properties": {
        "metadata": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "version": {"type": "string"}
            }
        },
        "tasks": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["action"],
                "properties": {
                    "action": {"type": "string"}
                }
            }
        }
    },
    "required": ["tasks"]
}

def validate_workflow(data):
    """Validate workflow YAML structure"""
    try:
        jsonschema.validate(instance=data, schema=WORKFLOW_SCHEMA)
        return True
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError(f"Invalid workflow: {e.message}")
