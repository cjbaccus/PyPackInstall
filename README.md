# PyPackInstall
Just a quick python script to automate the package loads on a new raspberry pi for general home use

## Usage
Just execute :

``` bash
python PyPackinstall.py
```
The script will read each package from the **"package2install"** file.
If you want to add new packages to be installed, just append them in a new line to the **"package2install"** file.

``` bash
echo "masscan" >> package2install
```
## future
Nothing so far.
