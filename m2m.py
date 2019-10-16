// in the Google sheet : 3 collumns ID / name / M2M values
// 1st row is the field name
// data starts at row 2
// copy and paste the following code in the script editor (from the tools menu) then run the Script
// once you have run the script once you can start the script from the sheet from the menu "Script" then "concatM2M"

function onOpen()
{
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Script').addItem('Concat M2M', 'concatM2M').addToUi();
}

function isBlank(stringChunk)
{
  if (typeof stringChunk !== "string") return false;
  return stringChunk.trim().length === 0;
}

function concatM2M()
{
  var lastColumn = SpreadsheetApp.getActiveSpreadsheet().getLastColumn();
  var lastRow = 999;//SpreadsheetApp.getActiveSpreadsheet().getLastRow();
  var values = [];
  var initialRow = 2;

  for (row = 2; row < 999 ; row++)
  {
    var id = SpreadsheetApp.getActiveSheet().getRange('A' + row).getValue();
    var m2m = SpreadsheetApp.getActiveSheet().getRange('C' + row).getValue();

    if (isBlank(id) && !isBlank(m2m))
    {
      values.push(m2m);
    }
    else
    {
      if (values.length > 0)
      {
        SpreadsheetApp.getActiveSheet().getRange('D' + initialRow).setValue(values.join(','));
      }
      values = [m2m];
      initialRow = row;
    }
  }
}
