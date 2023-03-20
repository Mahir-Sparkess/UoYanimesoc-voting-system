function generateSlotForm(){
var slotdata = SpreadsheetApp.getActiveSheet().getDataRange().getValues()
var form = FormApp.create('AnimeSoc Slot A Voting')
form.setConfirmationMessage("Thanks for voting on what shows to watch: https://www.youtube.com/watch?v=XmAVADh4HXk")
form.setAllowResponseEdits(true)
form.setLimitOneResponsePerUser(true)

form.addTextItem().setTitle("Name").setRequired(true)
form.addTextItem().setTitle("Email Address").setRequired(true).setValidation(FormApp.createTextValidation().requireTextIsEmail().build())

for(row = 1;row != slotdata.length;row++){
  form.addPageBreakItem().setTitle(slotdata[row][0]).setHelpText(slotdata[row][1])
  form.addImageItem().setImage(UrlFetchApp.fetch(slotdata[row][3])).setAlignment(FormApp.Alignment.CENTER)
  form.addSectionHeaderItem().setTitle("Nominee Description").setHelpText(slotdata[row][2])
  form.addVideoItem().setVideoUrl(slotdata[row][5])
  form.addSectionHeaderItem().setTitle("MAL Synopsis").setHelpText(slotdata[row][4])
  form.addMultipleChoiceItem().setTitle("Desire to watch").setChoiceValues(['2','1','0','-1','-2']).setRequired(true).setHelpText('(2 = high desire to watch, 0 = neutral, -2 = low desire to watch)')
  
}
}
