# More package/installation notes

For printing the dataframe to a pdf, I used the [Workflow from Mark Nagelberg](https://towardsdatascience.com/creating-pdf-reports-with-python-pdfkit-and-jinja2-templates-64a89158fa2d)  
  
  
We will also need to install the pdfkit and Jinja2 packages, which will also 
include wkhtmltopdf installation.  

  

### For installing pdfkit from conda (noarch version)...

First check availability and version:

```
conda search -c conda-forge python-pdfkit

``` 
  
  
Then install python-pdfkit:

```
conda install -c conda-forge python-pdfkit

```
  
  
As mentioned by user [JazzCore](https://github.com/JazzCore/python-pdfkit),
it may be a good idea to install wkhtmltopdf static binary from 
[wkhtmltopdf home](http://wkhtmltopdf.org/).

  
  
Then install Jinja2:

```
conda install Jinja2=2.10.1

```