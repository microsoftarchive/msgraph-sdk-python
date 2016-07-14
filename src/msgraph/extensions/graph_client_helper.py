'''
------------------------------------------------------------------------------
 Copyright (c) 2015 Microsoft Corporation

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
------------------------------------------------------------------------------
'''
from ..request.graph_service_client import GraphServiceClient
from ..request.drive_request_builder import DriveRequestBuilder


def item(self, drive=None, id_=None, path=None):
    """Gets an item given the specified (optional) drive,
    (optional) id_, and (optional) path

    Args:
        drive (str): The drive that you want to use
        id_ (str): The id_ of the item to request
        path (str): The path of the item to request

    Returns:
        :class:`ItemRequestBuilder<msgraph.requests.item_request_builder.ItemRequestBuilder>`:
            A request builder for an item given a path or id_
    """
    if id_ is None and path is None:
        raise ValueError("Either 'path' or 'id_' must be specified")
    elif id_ is not None and path is not None:
        raise ValueError("Only one of either 'path' or 'id_' can be specified")

    drive_builder = self.drives[drive] if drive else self.drive

    if path:
        return drive_builder.item_by_path(path)
    elif id_:
        return drive_builder.items[id_]


@property
def drive(self):
    """Gets the user's default drive

    Returns: 
        :class:`DriveRequestBuilder<msgraph.requests.drive_request_builder.DriveRequestBuilder>`:
            User's default drive
    """
    return DriveRequestBuilder(self.base_url + "drive", self)

GraphServiceClient.item = item
GraphServiceClient.drive = drive
