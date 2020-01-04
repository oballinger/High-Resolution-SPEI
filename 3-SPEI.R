## Load SPEI library, set working directory, and input data
library(SPEI)
setwd('/Users/ollie/Google Drive/')
data = read.csv("SPEI_Input10k.csv")


## Replace nulls 
data$CELL_CODE<-NULL

## Calculate rolling 3, 6, and 12 month SPEI values
spei3 <- spei(data,na.rm=TRUE, 3)
spei6 <- spei(data,na.rm=TRUE, 6)
spei12 <-  spei(data,na.rm=TRUE, 12)


## Export
write.csv(spei3,'SPEI_3_month_raw.csv')
write.csv(spei6,'SPEI_6_month_raw.csv')
write.csv(spei12,'SPEI_12_month_raw.csv')