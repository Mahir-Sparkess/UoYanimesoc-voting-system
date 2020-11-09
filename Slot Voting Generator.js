function generateSlotForm(){
var slotdata = SpreadsheetApp.getActiveSheet().getDataRange().getValues()
var form = FormApp.create('AnimeSoc Slot _ Voting: Round _')
form.setConfirmationMessage("Thanks for voting on what shows to watch: https://www.youtube.com/watch?v=XmAVADh4HXk")
form.setAllowResponseEdits(true)
form.setLimitOneResponsePerUser(true)

form.addSectionHeaderItem().setTitle("AnimeSoc Voting").setHelpText("This round 1 will consist of a seeding system and minor elimination. You will be asked to rate your desire to watch each show from -2 to 2 (-2 being low desire to watch, 0 being neutral, 2 being high desire to watch). This will be used to seed each show for the next round, which will be an elimination bracket.")
form.addTextItem().setTitle("Name").setRequired(true)
form.addTextItem().setTitle("Email Address").setRequired(true).setValidation(FormApp.createTextValidation().requireTextIsEmail().build())

for(row = 1;row != slotdata.length;row++){
  form.addPageBreakItem().setTitle(slotdata[row][0]).setHelpText(slotdata[row][1])
  form.addImageItem().setImage(UrlFetchApp.fetch(slotdata[row][3])).setAlignment(FormApp.Alignment.CENTER)
  form.addSectionHeaderItem().setTitle("Nominee Description").setHelpText(slotdata[row][2])
  form.addSectionHeaderItem().setTitle("MAL Synopsis").setHelpText(slotdata[row][4])
  form.addMultipleChoiceItem().setTitle("Desire to watch").setChoiceValues(['2','1','0','-1','-2']).setRequired(true)
  
}
}
