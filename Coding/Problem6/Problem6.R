args <- commandArgs(trailingOnly=TRUE)
db <- read.csv(file=args[1], header = FALSE)
X = args[2]
#X = 3
#db <- read.csv("sample.csv", header = FALSE)
names(db) <- c("type", "symbol", "price", "quantity", "expirydate", "strikeprice", "amendtime", "id", "parentid")
db$amendtime <- as.character(db$amendtime)
totalData <- nrow(db)
n = 0
while(totalData>0)
{
  file1 <- db[db$id[totalData] == db$parentid,]
  id<-db$id[totalData]
  if((nrow(file1)+1)>=X)
  {
    result <- rbind(file1, db[db$id == id,])
    write.table(result, file = paste("Output", n , sep="_"), row.names = FALSE,sep = "\t")
    n = n+1
  }
  file1 <- NULL
  totalData = totalData-1
}


