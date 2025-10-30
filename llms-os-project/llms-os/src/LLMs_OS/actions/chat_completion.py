"""Chat completion action for LLM interactions"""
import os
import re
from ..registry import register

@register('chat_completion')
def chat_completion(task, context):
    """Execute LLM chat completion"""
    provider = task.get('provider', 'openai')
    model = task.get('model', 'gpt-3.5-turbo')
    messages = task.get('messages', [])
    
    # Replace context variables in messages
    for msg in messages:
        if 'content' in msg:
            def replace_var(match):
                var_path = match.group(1).strip()
                parts = var_path.split('.')
                value = context
                for part in parts:
                    if isinstance(value, dict):
                        value = value.get(part)
                        if value is None:
                            return match.group(0)
                    else:
                        return match.group(0)
                return str(value) if value is not None else match.group(0)
            
            msg['content'] = re.sub(r'\{\{\s*(.+?)\s*\}\}', replace_var, msg['content'])
    
    if provider == 'openai':
        try:
            import openai
            openai.api_key = os.getenv('OPENAI_API_KEY')
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages
            )
            return {
                'content': response.choices[0].message.content,
                'model': model,
                'provider': provider
            }
        except Exception as e:
            print(f"⚠️  OpenAI request failed: {e}")
            return None
    
    print(f"⚠️  Provider '{provider}' not supported")
    return None
