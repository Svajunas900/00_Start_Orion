from .recursiveFibonacci import fibonacci

def lambda_handler(event, context):
    return fibonacci(event.get("user_input"))