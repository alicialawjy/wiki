from django.shortcuts import render, redirect
from . import util
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from os.path import exists
from random import randint
from django import forms


# View for home page
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# View for a particular entry
def entry(request, entry):
    # Check if entry exists, if it does:
    if util.entryexists(entry):
        # Convert the content into html
        html = util.convert(entry)
        # Get entry title
        all_entries = util.list_entries()
        title = [e for e in all_entries if entry.lower()==e.lower()]
        # Render the entry's html page
        return render(request, f"encyclopedia/entry.html",{
            'title': title[0],
            'content': html
            })
    
    else: 
        # Present an error page:
        return HttpResponse(f"Sorry, {entries} page does not exist.")

# View for search results: 
def results(request):
    entrylist_normal = util.list_entries()
    entrylist_lower = [i.lower() for i in entrylist_normal]
    # If this was a search query
    search_item = request.POST['search']
    # Check if an entry exists. If there's an EXACT match,
    if util.entryexists(search_item):
        # Then, redirect the user to the entry page.
        return HttpResponseRedirect(reverse('encyclopedia:entry', args=(search_item,))) 
    
    # Else, if the entry does not exist,
    else:
        # Find similar entries
        results = []
        for index, item in enumerate(entrylist_lower):
            # If the search is a substring of an entry, we will show it on the results page
            if len(item.split(search_item.lower()))>1:
                results.append(entrylist_normal[index])
        # Now, show(render) the results page.
        return render(request, 'encyclopedia/result.html', {
            'results':results
            })

# Create a new entry
def create(request):
    # If the POST request was sent (aka entry created)
    if request.method == 'POST':
        # Get the title and content of the post
        title = request.POST['Title']
        content = request.POST['Content']
        # Carry out data-validation (make sure entry does not already exist)
        if not util.entryexists(title):
            # If entry doesn't exist, write and save a md file
            util.save_entry(title,content)
            # Redirect user to the entry page created
            return HttpResponseRedirect(reverse('encyclopedia:entry', args=(title,)))

        # Else, if the entry already exists  
        else:
            # Return an error message
            return render(request,"encyclopedia/create.html",{
                'Error_Message':'ERROR: This entry already exists.'
                })

    # If it's a GET request to view the form page to create a new entry, render the form:
    return render(request,"encyclopedia/create.html")

def edit(request,page):
    # POST request: an edit was submitted
    if request.method == 'POST':
        # Replace the markdown file with the new content.
        content = request.POST['content'] 
        util.save_entry(page.capitalize(),content) 
        # Redirect user back to the entry page to see the update
        return HttpResponseRedirect(reverse('encyclopedia:entry', args=(page,)))
    
    # Else, if it's a GET request to view the edit page
    else:
        # Populate the textarea with the entry's existing content
         with open(f"entries/{page}.md",'r') as f:
            text=f.read()
        # Render the view 
         return render(request,"encyclopedia/edit.html",{
            'entry_title': page,
            'entry_content': text
            })

# Direct users to a random entry
def random(request):
    pick_index = randint(0,len(util.list_entries())-1)
    entry_name=util.list_entries()[pick_index]
    #Redirect to the random page
    return HttpResponseRedirect(reverse('encyclopedia:entry', args=(entry_name,)))









            

