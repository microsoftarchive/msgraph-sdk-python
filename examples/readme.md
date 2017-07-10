# CommandLineFileExplorer sample

The CommandLineFileExplorer sample is a sample app written in Python and uses the Graph SDK for Python.
The sample shows you how to work with a user's files and folders on OneDrive. In this sample, you will learn how to upload or download a file, get a sharing link, explore files and folder, and more.

## Set up

1. If you don't have Python installed, go to [Python.org](http://python.org) and scroll over **Downloads** to choose the install for your platform. For example, choose **Download for Windows** and download Python 3.5 or newer for Windows. Follow the instructions in [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html) to complete your Python set up.
2. Download the [Graph SDK for Python](https://github.com/MicrosoftGraph/msgraph-sdk-python/) to get the sample.
3. In the command prompt, type `pip install pillow` to install [Pillow](https://pypi.python.org/pypi/Pillow/3.0.0).
4. Next, type `pip install msgraph` to install the Graph SDK for Python.

## Run the sample

1. Open a command prompt and type `py -3 -V` on Windows or `python3 -V` on macOS/Linux to make sure that you are running Python 3.5 or newer.
2. Navigate to where you downloaded the CommandLineFileExplorer.py sample. If you installed a .zip of the Graph SDK for Python, the file should be located in ../graph-sdk-python/examples/.
3. Type `py -3 CommandLineFileExplorer.py` or `python3 CommandLineFileExplorer.py` to run the sample.
4. The app needs permissions to access your OneDrive. Click **Accept** in the browser to grant permissions access to your OneDrive.

## API features

### Sign in and authentication

This sample uses the [code flow](https://dev.onedrive.com/auth/msa_oauth.htm#code-flow) to sign the user in and authenticate the app. `get_default_client` is called to get a Graph client. `get_auth_url` returns the `redirect_uri` that contains the authorization code. Next, `get_auth_code` is called to process the authorization code from the `auth_url`. Finally, `authenticate` is called to authenticate the app with the `code`.

```python
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
client = graph.get_default_client(client_id='your_client_id',
                                  scopes=scopes)
auth_url = client.auth_provider.get_auth_url(redirect_uri)

# Block thread until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
# Finally, authenticate!
client.auth_provider.authenticate(code, redirect_uri, client_secret)
```

### List item children

The sample displays all items in the user's Graph, starting with the root:

```python
item_id = "root"
...
items = navigate(client, item_id)
...
def navigate(client, item_id):
    items = client.item(id=item_id).children.get()
    return items
```
### View thumbnails for an item

Once an item is selected, the thumbnail for the item is downloaded into a temporary JPG file, and then displayed:

```python
client.item(id=item_id).thumbnails[0].small.download("./tmp_thumb.jpg")
image = Image.open("./tmp_thumb.jpg")
image.show()
```

### Delete an item

To delete an item, call `delete()` with the `item_id`:

```python
def delete(client, item_id):
    confirm = input("Confirm delete? Y/N: ")
    if confirm == "Y":
        client.item(id=item_id).delete()
```

### Copy an item

In this example, a new `ItemReference()` object is created, and then the item is copied to the ItemReference.

```python
def paste(client, item_id, copy_item_ids):
    ref = microsoft.ItemReference()
    ref.id = item_id
    for id in copy_item_ids:
        client.item(id=id).copy(parent_reference=ref).post()
```

### Get a sharing link

This example gets a sharing link by calling the `create_link` method with `post()`. The type of link requires an input from the user.

```python
def get_sharing_link(client, item_id):
    action = int(input("Type? 1:View 2:Edit... "))
    permission = client.item(id=item_id).create_link("view" if action == 1 else "edit").post()
    print()
    print(permission.link.web_url)
    print()
```

### List changes for an item

Graph keeps track of changes for an item. In this example, the `delta` method is called on an item to list all changes for that item. The token represents the last sync token you got from the call to 'delta'.

```python
def list_changes(client, item_id, token):
    collection_page = client.item(id=item_id).delta(token).get()
    for item in collection_page:
        print(item.name)

    print("TOKEN:", collection_page.token)
```

## More resources

* [Graph SDK for Python](https://github.com/MicrosoftGraph/msgraph-sdk-python/)
* [Graph API](https://graph.microsoft.io)
* [Python](https://python.org)

## Copyright

Copyright (c) Microsoft. All rights reserved.
