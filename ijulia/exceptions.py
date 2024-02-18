from pathlib import Path

class CodeExecutionException(Exception):
  def __init__(self, message_id: str) -> None:
    self.message_id = message_id
  def __str__(self) -> str:
    return f"Code excecution exception. message_id: {self.message_id}"

class ConvertationSyntaxException(Exception):
  def __init__(self, file_path: Path, format: str) -> None:
    self.file_path = file_path
    self.format = format
    
  def __str__(self) -> str:
    return f"Syntax error in file - {self.file_path}, format - {self.format}"