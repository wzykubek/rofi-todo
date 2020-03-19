# rofi-todo

## Description
Prototype script to manage JSON-style notes in rofi.

### Features
Function | Status
:--- | :---
Add new notes | **avaible**
Delete notes | **avaible**
Read notes titles | **avaible**
Read notes descriptions | **avaible**

## Installation
* Clone this repo to your drive.
* Install [rofi](https://github.com/davatorium/rofi).
* Make sure are you have python3 and pip installed on your machine.
* Use following command to install python libs.
```bash
pip3 install --user -r requirements
```

## Usage
You must specify path of your notes file as `-f` or `--file` argument for rofi-todo.
```bash
python3 ./rofi-todo.py -f example.json 
```
In this place you can view, add, and delete notes. You can also manual edit your JSON notes file.

You can set key-binding for this script in your WM/DE config.

## Screenshots
![photo1](./screenshots/scr1.png)
![photo2](./screenshots/scr2.png)

#### [Example JSON file](./example.json)
```json
{
  "notes": [
    {
      "name": "Push git changes",
      "description": "Push changes from dotfiles to remote GitHub repo"
    },
    {
      "name": "Stay in the cellar",
      "description": "CoVID-19 etc."
    },
    {
      "name": "Make README",
      "description": "Make README.md file into rofi-todo repo"
    }
  ]
}
```
