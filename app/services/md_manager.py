from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextLine
import re

class MD_Manager:
    def __init__(self):
        self.documents = []

    def pdf_to_markdown(self, pdf_path, output_path):
        markdown_content = ""
        
        for page_layout in extract_pages(pdf_path):
            page_elements = []
            
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    text = element.get_text().strip()
                    if not text:
                        continue
                    
                    # Analyze character properties
                    chars = []
                    for text_line in element:
                        if isinstance(text_line, LTTextLine):
                            for char in text_line:
                                if isinstance(char, LTChar):
                                    chars.append(char)
                    
                    if chars:
                        # Get font properties
                        font_sizes = [char.height for char in chars]
                        font_names = [getattr(char, 'fontname', '') for char in chars]
                        
                        avg_font_size = sum(font_sizes) / len(font_sizes)
                        common_font = max(set(font_names), key=font_names.count) if font_names else ''
                        
                        is_bold = 'bold' in common_font.lower()
                        is_italic = 'italic' in common_font.lower()
                        
                        page_elements.append({
                            'text': text,
                            'font_size': avg_font_size,
                            'is_bold': is_bold,
                            'is_italic': is_italic,
                            'y_pos': element.y0
                        })
            
            # Sort by vertical position (top to bottom)
            page_elements.sort(key=lambda x: -x['y_pos'])
            
            # Generate markdown
            for elem in page_elements:
                text = elem['text']
                
                # Apply formatting
                if elem['is_bold'] and not any(text.startswith(h) for h in ['#', '##', '###']):
                    text = f"**{text}**"
                if elem['is_italic']:
                    text = f"*{text}*"
                
                # Heading detection
                if elem['font_size'] > 16:
                    markdown_content += f"# {elem['text']}\n\n"
                elif elem['font_size'] > 14:
                    markdown_content += f"## {elem['text']}\n\n"
                elif elem['font_size'] > 12 and elem['is_bold']:
                    markdown_content += f"### {elem['text']}\n\n"
                else:
                    markdown_content += f"{text}\n\n"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

    def pdf_to_markdown(self, pdf_path: str) -> str:
        """
        Convert PDF document to Markdown format.
        """
        # Implement PDF to Markdown conversion logic here
        markdown_content = ""
        return markdown_content

    def markdown_to_pdf(self, markdown_content: str) -> str:
        """
        Convert Markdown content to PDF format.
        """
        # Implement Markdown to PDF conversion logic here
        pdf_path = ""
        return pdf_path