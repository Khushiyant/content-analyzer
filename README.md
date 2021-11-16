# content-analyzer

Content analyzer is prototype text analyzer based primarily on Computer Vision for extraction and detection for document text extraction.

It rely on opencv for perspective wrapping for document scanning. Later, it passed to extractor module for text extaction which is later, passed to gingerit based model for language analysis.

Project is provided with resources which can be modified for about, help regarding prgram without any changes in driving function

GUI is based completely on standard built-in  library named [tkinter](https://docs.python.org/3/library/tkinter.html) usually used fast GUI prototyping

# Usage
To run this project 

```bash
git clone https://github.com/Khushiyant/content-analyzer
cd content-analyzer
pip install -r requirements.txt
```

## Development & Requirements

Understanding of perspective wrapping, text extraction is required for config changes

### Depedencies for deployment
* opencv-python >=4.5
* numpy >=1.19
* pytesseract >=0.3.8
* gingerit >=0.8.2
* pandas >=1.3.0

## Optimizations

The project is in its initial prototyping stage and, require major improvements in GUI design, 


# Team

### Mentor
[@rajatgupta24](https://github.com/rajatgupta24)