from pathlib import Path

class FileNotFoundException(Exception):
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def __str__(self) -> str:
        return f"File {self.file_path} does not exist"

class ConvertationSyntaxException(Exception):
  def __init__(self, file_path: Path, format: str) -> None:
    self.file_path = file_path
    self.format = format
    
  def __str__(self) -> str:
    return f"Syntax error in file - {self.file_path}, format - {self.format}"