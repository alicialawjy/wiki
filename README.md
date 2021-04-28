![Header](https://github.com/alicialawjy/wiki/blob/main/Screenshots/Entry.png)

# Wiki
A Wikipedia-like online encyclopedia. Users are able to search for and view entries, create new entries and edit existing ones. This was my first project on the Harvard x EdX Course: CS50 Web Programming with Python and JavaScript.

## Project Setup
1. Download the zip file to this repository.
2. In your terminal, cd into the 'wiki' directory.
3. Run ```python manage.py runserver``` and visit <a>http://127.0.0.1:8000/</a>

## Tech Stack
- Backend Framework: Django and Python
- Front End Languages: HTML, CSS and Markdown

## Functionality
#### 1. Make a New Entry
- Via 'Create New Page' in the sidebar
- Content has to be written using Markdown. The 'convert' function in util.py will then convert the Markdown content into HTML for rendering.
- If an entry has already been created, the submission will be denied and an error message will show.
- Else, the entry is created and users will be redirected to the entry page.

#### 2. View an Entry
- Visit /wiki/TITLE, where TITLE is the title of an encyclopedia entry.
- If an entry that doesn't exist is visited, users are presented with an error page indicating that their requested page was not found.

#### 3. Edit an Existing Entry
- Via the 'Edit Entry' button next to the search bar, which is only visible when users are viewing an entry.
- Clicking the button will direct users to an Edit form, where the textarea is already pre-populated with the entry's existing content.
- Once the post is edited and saved, users are redirected back to the entry page where they can view their changes.

#### 4. Search for Entries
- Via the search bar at the top of the webpage.
- If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
- Else, users will be directed to a search results page that displays a list of potential entries that have their query as a substring. For example, if the search query were 'Py', then Python should appear in the search results.

#### 5. View a Random Page
- Via the 'Random Page' button in the sidebar.

#### 6. Home page
- Shows a list of all the entries on the site in alphabetical order.
