
function on_edit(e) {
  
  var wks = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet1');
  // e.value- to get new message text
  // e.user- to get user info 
  // e.range.getRow() - to get row number 
  // e.range.getColumn() - to get column number

  var col= e.range.getColumn();
  var row= e.range.getRow();
  var msgid = wks.getRange('E' + row).getValue();
  
  if(col == 7 && msgid){

   //var admin= e.user.getEmail();
   var admin= Session.getActiveUser().getEmail();

   var groupid = wks.getRange('D' + row).getValue();
   var msgid = wks.getRange('E' + row).getValue();
   var text= e.value;
   var url = "https://api.telegram.org/bot(bot token id)/sendMessage?chat_id=" + groupid + "&text=" + text + "&reply_to_message_id=" + msgid;

   try{
   var response = UrlFetchApp.fetch(url,{'muteHttpExceptions': true});
   var data = JSON.parse(response.getContentText());
   if(data.ok == true ){
   wks.getRange('H' + row).setValue('SENT');
   }
   else{
     wks.getRange('H' + row).setValue(data.description);
   }
   wks.getRange('I' + row).setValue(admin);
   }
   catch(e){}

  }
}



