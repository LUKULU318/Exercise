function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = JSON.parse(e.postData.contents);

  // Append a new row to the sheet with the username and password
  sheet.appendRow([data.username, data.password, new Date()]);  // Add a timestamp
  return ContentService.createTextOutput(JSON.stringify({ 'result': 'success' }))
                        .setMimeType(ContentService.MimeType.JSON);
}
