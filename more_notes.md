# More package/installation notes

We will also need the pdfkit and Jinja2 packages installed, which will also 
include the need for wkhtmltopdf installation.

### For installing pdfkit from conda (noarch version)...

First check availability and version:

```
conda search -c conda-forge python-pdfkit

``` 

Then install:

```
conda install -c conda-forge python-pdfkit

```

As mentioned by JazzCore, https://github.com/JazzCore/python-pdfkit,
it may be a good idea to install wkhtmltopdf static binary from [wkhtmltopdf home]
(http://wkhtmltopdf.org/).


Then install Jinja2:

```
conda install Jinja2=2.10.1

```