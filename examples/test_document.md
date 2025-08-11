# Enhanced Document Support Test

This is a **test markdown file** to verify our enhanced document loader works correctly.

## Features

The enhanced loader now supports:

- PDF files (.pdf)
- Text files (.txt)
- Word documents (.docx)
- Markdown files (.md)

## Text Processing

The system now includes:

1. **Smart chunking** - sentence-aware text splitting
2. **Better preprocessing** - removes extra whitespace and special characters
3. **Auto-detection** - automatically detects file type based on extension

### Code Example

```python
# This code block should be removed during preprocessing
loader = DocumentLoader()
text = loader.load_document("example.md")
```

## Links and Formatting

This [link](https://example.com) should become just "link" after processing.

_Italic text_ and **bold text** should lose their formatting markers.

## Conclusion

This test file helps verify that our markdown processing works correctly!
