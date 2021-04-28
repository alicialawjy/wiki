import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from markdown import markdown
from os.path import exists
from random import randint

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def convert(md_filename):
    """Converts markdown file to html format"""
    #python is case insensitive with file names!
    with open(f"entries/{md_filename}.md",'r') as f:
        text=f.read()
        html=markdown(text)
        return html

def entryexists(md_filename):
     """Function checks if entry's md_file exists."""
     if exists(f'entries/{md_filename}.md'):
        return True
     else:
        return False

def randompage():
    "Picks a random page to bring the user to"
    pick_index = randint(0,len(list_entries()))
    return list_entries()[pick_index]


